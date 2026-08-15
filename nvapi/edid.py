# -*- coding: utf-8 -*-
#
# ***********************************************************************************
# MIT License
#
# Copyright (c) 2020 Kevin G. Schlosser
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is furnished
# to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# ***********************************************************************************
"""
VESA E-EDID 1.4 base-block decoder.

Deliberately standalone -- no dependency on ctypes/the driver/nvapi_h.py --
so it can decode EDID bytes obtained from anywhere (Display.edid_data,
PhysicalGPU.get_edid, a file, another library) and be unit tested without a
GPU or driver present.

Only the 128-byte base block is decoded. CEA-861/DisplayID extension
blocks (bytes 128+, one 128-byte block per NV_EDID_DATA/EdidPage beyond the
first, per the EDID's own extension_count field) are not parsed here.
"""
from collections import namedtuple


EdidChromaticity = namedtuple('EdidChromaticity', ['red', 'green', 'blue', 'white'])
EdidPoint = namedtuple('EdidPoint', ['x', 'y'])
EdidDetailedTiming = namedtuple('EdidDetailedTiming', [
    'pixel_clock_khz', 'h_active', 'h_blanking', 'v_active', 'v_blanking',
    'h_sync_offset', 'h_sync_width', 'v_sync_offset', 'v_sync_width',
    'h_image_size_mm', 'v_image_size_mm', 'h_border', 'v_border',
    'interlaced', 'refresh_rate_hz',
])
EdidRangeLimits = namedtuple('EdidRangeLimits', [
    'min_vertical_hz', 'max_vertical_hz', 'min_horizontal_khz', 'max_horizontal_khz', 'max_pixel_clock_mhz',
])
EdidInfo = namedtuple('EdidInfo', [
    'is_valid_header', 'checksum_valid',
    'manufacturer_id', 'product_code', 'serial_number',
    'manufacture_week', 'manufacture_year', 'model_year',
    'edid_version', 'edid_revision',
    'is_digital', 'bit_depth', 'video_interface',
    'h_screen_size_cm', 'v_screen_size_cm',
    'gamma', 'chromaticity',
    'established_timings', 'standard_timings',
    'preferred_timing', 'detailed_timings',
    'monitor_name', 'serial_number_string', 'unspecified_text', 'range_limits',
    'extension_count',
])

_ESTABLISHED_TIMINGS = [
    # (byte_index_into_bytes_35_37, bit, description)
    (0, 0x80, '720x400@70Hz'),
    (0, 0x40, '720x400@88Hz'),
    (0, 0x20, '640x480@60Hz'),
    (0, 0x10, '640x480@67Hz'),
    (0, 0x08, '640x480@72Hz'),
    (0, 0x04, '640x480@75Hz'),
    (0, 0x02, '800x600@56Hz'),
    (0, 0x01, '800x600@60Hz'),
    (1, 0x80, '800x600@72Hz'),
    (1, 0x40, '800x600@75Hz'),
    (1, 0x20, '832x624@75Hz'),
    (1, 0x10, '1024x768@87Hz(i)'),
    (1, 0x08, '1024x768@60Hz'),
    (1, 0x04, '1024x768@70Hz'),
    (1, 0x02, '1024x768@75Hz'),
    (1, 0x01, '1280x1024@75Hz'),
    (2, 0x80, '1152x870@75Hz'),
]

_STANDARD_TIMING_ASPECT = {
    0b00: (16, 10),
    0b01: (4, 3),
    0b10: (5, 4),
    0b11: (16, 9),
}

_VIDEO_INTERFACE = {
    0x0: 'Undefined',
    0x1: 'HDMI-a',
    0x2: 'HDMI-b',
    0x3: 'MDDI',
    0x4: 'DisplayPort',
}

_DESCRIPTOR_DUMMY = 0x10
_DESCRIPTOR_CVT = 0xF8
_DESCRIPTOR_ESTABLISHED_III = 0xF7
_DESCRIPTOR_COLOR_MANAGEMENT = 0xF9
_DESCRIPTOR_STANDARD_TIMING = 0xFA
_DESCRIPTOR_WHITE_POINT = 0xFB
_DESCRIPTOR_NAME = 0xFC
_DESCRIPTOR_RANGE_LIMITS = 0xFD
_DESCRIPTOR_UNSPECIFIED_TEXT = 0xFE
_DESCRIPTOR_SERIAL_NUMBER = 0xFF


def _decode_text(raw):
    # descriptor text fields are ASCII, padded with 0x0A then 0x20 (space)
    text = raw.split(b'\x0a', 1)[0]
    return text.decode('ascii', 'replace').strip()


def _decode_manufacturer_id(b8, b9):
    value = (b8 << 8) | b9
    c1 = ((value >> 10) & 0x1F) + ord('A') - 1
    c2 = ((value >> 5) & 0x1F) + ord('A') - 1
    c3 = (value & 0x1F) + ord('A') - 1
    return ''.join(chr(c) for c in (c1, c2, c3))


def _decode_chromaticity(data):
    # bytes 25-34 (10 bytes): 2 low-order bits per point packed into
    # bytes 25-26, high 8 bits of each coordinate in bytes 27-34.
    red_green_lo = data[25]
    blue_white_lo = data[26]
    red_x_hi, red_y_hi, green_x_hi, green_y_hi = data[27], data[28], data[29], data[30]
    blue_x_hi, blue_y_hi, white_x_hi, white_y_hi = data[31], data[32], data[33], data[34]

    def point(hi_x, hi_y, lo_byte, x_shift, y_shift):
        x = (hi_x << 2) | ((lo_byte >> x_shift) & 0x3)
        y = (hi_y << 2) | ((lo_byte >> y_shift) & 0x3)
        return EdidPoint(x / 1024.0, y / 1024.0)

    return EdidChromaticity(
        red=point(red_x_hi, red_y_hi, red_green_lo, 6, 4),
        green=point(green_x_hi, green_y_hi, red_green_lo, 2, 0),
        blue=point(blue_x_hi, blue_y_hi, blue_white_lo, 6, 4),
        white=point(white_x_hi, white_y_hi, blue_white_lo, 2, 0),
    )


def _decode_established_timings(data):
    bytes35_37 = data[35:38]
    return [desc for idx, bit, desc in _ESTABLISHED_TIMINGS if bytes35_37[idx] & bit]


def _decode_standard_timings(data):
    timings = []
    for i in range(8):
        b1, b2 = data[38 + i * 2], data[38 + i * 2 + 1]
        if b1 in (0x00, 0x01) and b2 == 0x00:
            continue
        width = (b1 + 31) * 8
        aspect_w, aspect_h = _STANDARD_TIMING_ASPECT[(b2 >> 6) & 0x3]
        height = int(round(width * aspect_h / float(aspect_w)))
        refresh = (b2 & 0x3F) + 60
        timings.append((width, height, refresh))

    return timings


def _decode_detailed_timing(block):
    pixel_clock_khz = (block[0] | (block[1] << 8)) * 10
    if pixel_clock_khz == 0:
        return None

    h_active = block[2] | ((block[4] >> 4) << 8)
    h_blanking = block[3] | ((block[4] & 0xF) << 8)
    v_active = block[5] | ((block[7] >> 4) << 8)
    v_blanking = block[6] | ((block[7] & 0xF) << 8)
    h_sync_offset = block[8] | ((block[11] >> 6) << 8)
    h_sync_width = block[9] | (((block[11] >> 4) & 0x3) << 8)
    v_sync_offset = (block[10] >> 4) | (((block[11] >> 2) & 0x3) << 4)
    v_sync_width = (block[10] & 0xF) | ((block[11] & 0x3) << 4)
    h_image_size_mm = block[12] | ((block[14] >> 4) << 8)
    v_image_size_mm = block[13] | ((block[14] & 0xF) << 8)
    h_border = block[15]
    v_border = block[16]
    interlaced = bool(block[17] & 0x80)

    h_total = h_active + h_blanking
    v_total = v_active + v_blanking
    refresh_rate_hz = (pixel_clock_khz * 1000.0) / (h_total * v_total) if h_total and v_total else 0.0

    return EdidDetailedTiming(
        pixel_clock_khz, h_active, h_blanking, v_active, v_blanking,
        h_sync_offset, h_sync_width, v_sync_offset, v_sync_width,
        h_image_size_mm, v_image_size_mm, h_border, v_border,
        interlaced, refresh_rate_hz,
    )


def _decode_range_limits(block):
    min_v, max_v, min_h, max_h, max_clock = block[5], block[6], block[7], block[8], block[9]
    return EdidRangeLimits(
        min_vertical_hz=min_v, max_vertical_hz=max_v,
        min_horizontal_khz=min_h, max_horizontal_khz=max_h,
        max_pixel_clock_mhz=max_clock * 10 if max_clock != 0xFF else None,
    )


def decode_edid(data):
    """Decode a 128-byte (or longer) raw EDID base block into an EdidInfo.

    Only the base block is parsed; any bytes beyond the first 128 (CEA-861/
    DisplayID extension blocks) are ignored. Raises ValueError if data is
    shorter than 128 bytes -- there's nothing to decode. A bad header or
    checksum does not raise; it's reported via is_valid_header/
    checksum_valid so callers can decide how strict to be about a
    marginal/corrupted read (e.g. from a flaky DDC channel).
    """
    data = bytes(data)
    if len(data) < 128:
        raise ValueError("EDID data must be at least 128 bytes, got %d" % len(data))

    is_valid_header = data[0:8] == b'\x00\xff\xff\xff\xff\xff\xff\x00'
    checksum_valid = (sum(data[0:128]) & 0xFF) == 0

    manufacturer_id = _decode_manufacturer_id(data[8], data[9])
    product_code = data[10] | (data[11] << 8)
    serial_number = data[12] | (data[13] << 8) | (data[14] << 16) | (data[15] << 24)

    week = data[16]
    year_byte = data[17]
    if week == 0xFF:
        manufacture_week = None
        manufacture_year = None
        model_year = year_byte + 1990
    else:
        manufacture_week = week if week != 0 else None
        manufacture_year = year_byte + 1990
        model_year = None

    edid_version = data[18]
    edid_revision = data[19]

    video_input = data[20]
    is_digital = bool(video_input & 0x80)
    # bits 6-0 of a digital "video input definition" byte only carry
    # bit-depth/interface info from EDID 1.4 onward; in 1.3 and earlier
    # they're a different, mostly-reserved layout (DFP 1.x compatibility
    # flag etc.), so decoding them as bit-depth/interface there would just
    # be making up values that don't mean that on this EDID version.
    is_edid_1_4_or_later = (edid_version, edid_revision) >= (1, 4)
    if is_digital and is_edid_1_4_or_later:
        bit_depth_code = (video_input >> 4) & 0x7
        bit_depth = {0b001: 6, 0b010: 8, 0b011: 10, 0b100: 12, 0b101: 14, 0b110: 16}.get(bit_depth_code)
        video_interface = _VIDEO_INTERFACE.get(video_input & 0xF, 'Reserved(0x%x)' % (video_input & 0xF))
    else:
        bit_depth = None
        video_interface = None

    h_screen_size_cm = data[21] or None
    v_screen_size_cm = data[22] or None

    gamma = None if data[23] == 0xFF else (data[23] + 100) / 100.0
    chromaticity = _decode_chromaticity(data)
    established_timings = _decode_established_timings(data)
    standard_timings = _decode_standard_timings(data)

    preferred_timing = None
    detailed_timings = []
    monitor_name = None
    serial_number_string = None
    unspecified_text = None
    range_limits = None

    for offset in (54, 72, 90, 108):
        block = data[offset:offset + 18]
        if block[0] == 0x00 and block[1] == 0x00:
            descriptor_type = block[3]
            if descriptor_type == _DESCRIPTOR_NAME:
                monitor_name = _decode_text(block[5:18])
            elif descriptor_type == _DESCRIPTOR_SERIAL_NUMBER:
                serial_number_string = _decode_text(block[5:18])
            elif descriptor_type == _DESCRIPTOR_UNSPECIFIED_TEXT:
                unspecified_text = _decode_text(block[5:18])
            elif descriptor_type == _DESCRIPTOR_RANGE_LIMITS:
                range_limits = _decode_range_limits(block)
            # dummy/CVT/established-III/color-management/standard-timing/
            # white-point descriptors carry no info useful at this level
            continue

        timing = _decode_detailed_timing(block)
        if timing is not None:
            detailed_timings.append(timing)
            if preferred_timing is None:
                preferred_timing = timing

    extension_count = data[126]

    return EdidInfo(
        is_valid_header, checksum_valid,
        manufacturer_id, product_code, serial_number,
        manufacture_week, manufacture_year, model_year,
        edid_version, edid_revision,
        is_digital, bit_depth, video_interface,
        h_screen_size_cm, v_screen_size_cm,
        gamma, chromaticity,
        established_timings, standard_timings,
        preferred_timing, detailed_timings,
        monitor_name, serial_number_string, unspecified_text, range_limits,
        extension_count,
    )
