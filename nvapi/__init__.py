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

# ***********************************************************************************


# **********************************************************************************************************************
# Copyright 2012 NVIDIA Corporation. All rights reserved.
# NOTICE TO USER:
# This software is subject to NVIDIA ownership rights under U.S. and international Copyright laws.
# This software and the information contained herein are PROPRIETARY and CONFIDENTIAL to NVIDIA
# and are being provided solely under the terms and conditions of an NVIDIA software license agreement.
# Otherwise, you have no rights to use or access this software in any manner.
#
# If not covered by the applicable NVIDIA software license agreement:
# NVIDIA MAKES NO REPRESENTATION ABOUT THE SUITABILITY OF THIS SOFTWARE FOR ANY PURPOSE.
# IT IS PROVIDED "AS IS" WITHOUT EXPRESS OR IMPLIED WARRANTY OF ANY KIND.
# NVIDIA DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY, NONINFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.
# IN NO EVENT SHALL NVIDIA BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL DAMAGES,
# OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOURCE CODE.
#
# U.S. Government End Users.
# This software is a "commercial item" as that term is defined at 48 C.F.R. 2.101 (OCT 1995),
# consisting of "commercial computer software" and "commercial computer software documentation"
# as such terms are used in 48 C.F.R. 12.212 (SEPT 1995) and is provided to the U.S. Government only as a commercial
# end item.
# Consistent with 48 C.F.R.12.212 and 48 C.F.R. 227.7202-1 through 227.7202-4 (JUNE 1995),
# all U.S. Government End Users acquire the software with only those rights set forth herein.
#
# Any use of this software in individual and commercial software must include,
# in the user documentation and internal comments to the code,
# the above Disclaimer (as applicable) and U.S. Government End Users Notice.
#
# **********************************************************************************************************************

from .nvapi_h import *
from .nvapi_gpu_info_ext_h import *  # noqa
from .edid import decode_edid, EdidInfo, EdidChromaticity, EdidPoint, EdidDetailedTiming, EdidRangeLimits
import ctypes
import six
from collections import namedtuple


ColorCoordinates = namedtuple('ColorCoordinates', ['red', 'green', 'blue', 'white'])
RedCoordinate = namedtuple('RedCoordinate', ['x', 'y'])
GreenCoordinate = namedtuple('RedCoordinate', ['x', 'y'])
BlueCoordinate = namedtuple('RedCoordinate', ['x', 'y'])
WhiteCoordinate = namedtuple('RedCoordinate', ['x', 'y'])

ArchitectureInfo = namedtuple('ArchitectureInfo', ['architecture', 'implementation', 'revision'])
LicenseFeatureDetail = namedtuple('LicenseFeatureDetail', ['is_enabled', 'is_feature_enabled', 'feature_code', 'product_name'])
LicensableFeatures = namedtuple('LicensableFeatures', ['is_license_supported', 'features'])
GPUInfo = namedtuple('GPUInfo', ['is_external_gpu', 'ray_tracing_cores', 'tensor_cores'])
MemoryInfoEx = namedtuple('MemoryInfoEx', [
    'dedicated_video_memory',
    'available_dedicated_video_memory',
    'system_video_memory',
    'shared_system_memory',
    'current_available_dedicated_video_memory',
    'dedicated_video_memory_evictions_size',
    'dedicated_video_memory_eviction_count',
    'dedicated_video_memory_promotions_size',
    'dedicated_video_memory_promotion_count',
])
NVLinkCaps = namedtuple('NVLinkCaps', [
    'caps_table', 'lowest_nvlink_version', 'highest_nvlink_version',
    'lowest_nci_version', 'highest_nci_version', 'link_mask',
])
NVLinkLinkStatus = namedtuple('NVLinkLinkStatus', [
    'link_index', 'is_connected', 'link_state', 'sublink_width',
    'nvlink_version', 'nci_version', 'nvlink_common_clock_speed_mhz',
    'nvlink_link_clock_mhz', 'remote_device_uuid',
])
NVLinkStatus = namedtuple('NVLinkStatus', ['link_mask', 'links'])
EncoderStatistics = namedtuple('EncoderStatistics', ['sessions_count', 'average_fps', 'average_latency'])
# configured/consistent are lists of NVAPI_GPU_WORKSTATION_FEATURE_MASK
# flags, per NvAPI_GPU_WorkstationFeatureQuery's own doc comment:
# configured = features requested for use by client drivers, consistent =
# which of those have all resources allocated for completeness.
WorkstationFeatureQuery = namedtuple('WorkstationFeatureQuery', ['configured', 'consistent'])
ThermalSensorInfo = namedtuple('ThermalSensorInfo', [
    'controller', 'default_minimum_temp', 'default_maximum_temp', 'current_temp', 'target',
])
# legacy "Cooler" API (undocumented) -- levels/temps are all percentages
# unless noted otherwise.
CoolerSetting = namedtuple('CoolerSetting', [
    'cooler_type', 'controller', 'default_minimum_level', 'default_maximum_level',
    'current_minimum_level', 'current_maximum_level', 'current_level',
    'default_policy', 'current_policy', 'target', 'control_mode', 'is_active',
])
CoolerPolicyTableEntry = namedtuple('CoolerPolicyTableEntry', ['entry_id', 'current_level', 'default_level'])
CoolerPolicyTable = namedtuple('CoolerPolicyTable', ['policy', 'entries'])
# modern "ClientFanCoolers" API (undocumented) -- what current-generation
# GPUs use.
FanCoolerInfo = namedtuple('FanCoolerInfo', ['cooler_id', 'maximum_rpm'])
FanCoolersInfo = namedtuple('FanCoolersInfo', ['is_supported', 'coolers'])
FanCoolerStatus = namedtuple('FanCoolerStatus', [
    'cooler_id', 'current_rpm', 'current_minimum_level', 'current_maximum_level', 'current_level',
])
FanCoolerControl = namedtuple('FanCoolerControl', ['cooler_id', 'control_mode', 'level'])
# graphics/memory/processor/video match NV_GPU_PUBLIC_CLOCK_ID -- the only
# 4 of the 32 possible clock-domain slots the driver ever populates. A
# field is None if that domain isn't present on this GPU.
ClockDomainFrequencies = namedtuple('ClockDomainFrequencies', ['graphics', 'memory', 'processor', 'video'])
ClockFrequencies = namedtuple('ClockFrequencies', ['current', 'base', 'boost'])
EncoderSessionInfo = namedtuple('EncoderSessionInfo', [
    'session_id', 'process_id', 'vgpu_instance', 'codec_type',
    'h_resolution', 'v_resolution', 'average_encode_fps', 'average_encode_latency',
])
HdrMetadata = namedtuple('HdrMetadata', [
    'display_primary_0', 'display_primary_1', 'display_primary_2', 'white_point',
    'max_display_mastering_luminance', 'min_display_mastering_luminance',
    'max_content_light_level', 'max_frame_average_light_level',
])
DisplayColorimetry = namedtuple('DisplayColorimetry', [
    'min_luminance', 'max_full_frame_luminance', 'max_luminance',
    'hdr_brightness_luminance_scaling_factor',
    'red_primary', 'green_primary', 'blue_primary', 'white_point',
])
AdaptiveSyncData = namedtuple('AdaptiveSyncData', [
    'max_frame_interval', 'is_adaptive_sync_disabled', 'is_frame_splitting_disabled',
    'last_flip_refresh_count', 'last_flip_timestamp',
])
VirtualRefreshRateData = namedtuple('VirtualRefreshRateData', ['frame_interval_us', 'refresh_rate_x1000', 'is_gaming_vrr'])
PreferredStereoDisplay = namedtuple('PreferredStereoDisplay', ['display_id'])
ManagedDedicatedDisplay = namedtuple('ManagedDedicatedDisplay', ['display_id', 'is_acquired', 'is_mosaic'])
DedicatedDisplayMetadata = namedtuple('DedicatedDisplayMetadata', [
    'position_x', 'position_y', 'position_is_available', 'name', 'name_is_available',
])
DisplayIdInfo = namedtuple('DisplayIdInfo', ['adapter_luid', 'target_id'])
VRRInfo = namedtuple('VRRInfo', [
    'is_vrr_enabled', 'is_vrr_possible', 'is_vrr_requested',
    'is_vrr_indicator_enabled', 'is_display_in_vrr_mode',
])
DisplayDriverInfo = namedtuple('DisplayDriverInfo', [
    'driver_version', 'build_branch', 'build_base_branch', 'is_dch_driver',
    'is_studio_package', 'is_game_ready_package',
    'is_rtx_production_branch_package', 'is_rtx_new_feature_branch_package',
])
SystemGpuHandle = namedtuple('SystemGpuHandle', ['adapter_type'])
TimingInfo = namedtuple('TimingInfo', [
    'h_visible', 'h_border', 'h_front_porch', 'h_sync_width', 'h_total', 'h_sync_polarity',
    'v_visible', 'v_border', 'v_front_porch', 'v_sync_width', 'v_total', 'v_sync_polarity',
    'is_interlaced', 'pixel_clock_10khz',
])
MonitorCapsVSDB = namedtuple('MonitorCapsVSDB', [
    'source_physical_address', 'supports_dual_dvi_operation',
    'supports_deep_color_ycbcr444', 'supports_deep_color_30bits',
    'supports_deep_color_36bits', 'supports_deep_color_48bits', 'supports_ai',
    'max_tmds_clock', 'supports_graphics_text_content', 'supports_photo_content',
    'supports_cinema_content', 'supports_game_content', 'has_vic_entries',
    'has_interlaced_latency_field', 'has_latency_field', 'video_latency',
    'audio_latency', 'interlaced_video_latency', 'interlaced_audio_latency',
    'has_3d_entries',
])
MonitorCapsVCDB = namedtuple('MonitorCapsVCDB', [
    'quantization_range_ycc', 'quantization_range_rgb',
    'scan_info_preferred_video_format', 'scan_info_it_video_formats',
    'scan_info_ce_video_formats',
])
MonitorColorCap = namedtuple('MonitorColorCap', ['color_format', 'backend_bit_depth'])
ColorData = namedtuple('ColorData', [
    'color_format', 'colorimetry', 'dynamic_range', 'bpc', 'color_selection_policy', 'depth',
])
DisplayPortInfo = namedtuple('DisplayPortInfo', [
    'dpcd_version', 'max_link_rate', 'max_lane_count', 'current_link_rate', 'current_lane_count',
    'color_format', 'dynamic_range', 'colorimetry', 'bpc', 'is_dp', 'is_internal_dp',
    'is_color_control_supported',
])
HdmiSupportInfo = namedtuple('HdmiSupportInfo', [
    'is_gpu_hdmi_capable', 'is_monitor_underscan_capable', 'is_monitor_basic_audio_capable',
    'is_monitor_ycbcr444_capable', 'is_monitor_ycbcr422_capable', 'is_monitor_xvycc601_capable',
    'is_monitor_xvycc709_capable', 'is_monitor_hdmi', 'edid_861_extension_revision',
])
DisplayConfigTarget = namedtuple('DisplayConfigTarget', ['display_id', 'target_id'])
DisplayConfigPath = namedtuple('DisplayConfigPath', [
    'source_id', 'targets', 'resolution', 'position', 'is_gdi_primary',
])
EdidPage = namedtuple('EdidPage', ['data', 'edid_id', 'size'])
CustomDisplay = namedtuple('CustomDisplay', [
    'width', 'height', 'depth', 'color_format', 'src_partition', 'x_ratio', 'y_ratio',
    'timing', 'hw_mode_set_only',
])
IllumDeviceInfo = namedtuple('IllumDeviceInfo', ['type', 'ctrl_mode_mask', 'i2c_device_index'])
IllumDeviceControl = namedtuple('IllumDeviceControl', ['type', 'needs_sync', 'sync_timestamp_ms'])
IllumZoneInfo = namedtuple('IllumZoneInfo', ['type', 'illum_device_index', 'provider_index', 'zone_location'])
IllumRGBColor = namedtuple('IllumRGBColor', ['r', 'g', 'b', 'brightness_pct'])
IllumPiecewiseLinearTiming = namedtuple('IllumPiecewiseLinearTiming', [
    'cycle_type', 'group_count', 'rise_time_ms', 'fall_time_ms',
    'a_time_ms', 'b_time_ms', 'group_idle_time_ms', 'phase_offset_ms',
])
# colors/brightness_pcts hold a 1-tuple for MANUAL_RGB ctrl_mode or a
# 2-tuple (color/brightness A, B) for PIECEWISE_LINEAR_RGB, matching
# NV_GPU_CLIENT_ILLUM_CTRL_MODE_PIECEWISE_LINEAR_COLOR_ENDPOINTS; whichever
# of colors/brightness_pcts applies depends on zone `type` (RGB vs
# COLOR_FIXED). timing is only populated for PIECEWISE_LINEAR_RGB.
IllumZoneControl = namedtuple('IllumZoneControl', ['type', 'ctrl_mode', 'colors', 'brightness_pcts', 'timing'])
Rect = namedtuple('Rect', ['x', 'y', 'width', 'height'])
ScanoutConfiguration = namedtuple('ScanoutConfiguration', ['desktop_rect', 'scanout_rect'])
ScanoutInformation = namedtuple('ScanoutInformation', [
    'source_desktop_rect', 'source_viewport_rect', 'target_viewport_rect',
    'target_display_width', 'target_display_height', 'clone_importance', 'source_to_target_rotation',
])
EccStatusInfo = namedtuple('EccStatusInfo', ['is_supported', 'configuration_options', 'is_enabled'])
EccErrorCounts = namedtuple('EccErrorCounts', ['single_bit_errors', 'double_bit_errors'])
EccErrorInfo = namedtuple('EccErrorInfo', ['current', 'aggregate'])
EccConfigurationInfo = namedtuple('EccConfigurationInfo', ['is_enabled', 'is_enabled_by_default'])
ConnectorInfo = namedtuple('ConnectorInfo', ['connector_type', 'connector_index'])
FramebufferWidthAndLocation = namedtuple('FramebufferWidthAndLocation', ['width', 'location'])
ChipsetInfo = namedtuple('ChipsetInfo', [
    'vendor_id', 'device_id', 'vendor_name', 'chipset_name', 'flags',
    'sub_sys_vendor_id', 'sub_sys_device_id', 'sub_sys_vendor_name',
    'hb_vendor_id', 'hb_device_id', 'hb_vendor_name',
    'hb_sub_sys_vendor_id', 'hb_sub_sys_device_id', 'hb_sub_sys_vendor_name',
])

# PCI-SIG vendor ID -> name, for chipset_info's hb_vendor_id /
# hb_sub_sys_vendor_id fields -- unlike vendor_id/sub_sys_vendor_id, NV_CHIPSET_INFO
# has no driver-provided name string for these (no szHBVendorName field
# exists in the struct). Intentionally small: only IDs that are certain,
# not the full PCI-SIG database (thousands of vendors, out of scope).
# AMD and Super Micro Computer, Inc. verified directly against real
# hardware output; Intel and NVIDIA are well-established IDs.
_PCI_VENDOR_NAMES = {
    0x8086: 'Intel',
    0x1022: 'AMD',
    0x10DE: 'NVIDIA',
    0x15D9: 'Super Micro Computer, Inc.',
}


def _pci_vendor_name(vendor_id):
    return _PCI_VENDOR_NAMES.get(vendor_id)
LidDockInfo = namedtuple('LidDockInfo', [
    'current_lid_state', 'current_dock_state', 'current_lid_policy', 'current_dock_policy',
    'forced_lid_mechanism_present', 'forced_dock_mechanism_present',
])


def _timing_from_struct(t):
    return TimingInfo(
        t.HVisible, t.HBorder, t.HFrontPorch, t.HSyncWidth, t.HTotal, t.HSyncPol,
        t.VVisible, t.VBorder, t.VFrontPorch, t.VSyncWidth, t.VTotal, t.VSyncPol,
        bool(t.interlaced), t.pclk,
    )


def _timing_to_struct(s, t):
    s.HVisible = t.h_visible
    s.HBorder = t.h_border
    s.HFrontPorch = t.h_front_porch
    s.HSyncWidth = t.h_sync_width
    s.HTotal = t.h_total
    s.HSyncPol = t.h_sync_polarity
    s.VVisible = t.v_visible
    s.VBorder = t.v_border
    s.VFrontPorch = t.v_front_porch
    s.VSyncWidth = t.v_sync_width
    s.VTotal = t.v_total
    s.VSyncPol = t.v_sync_polarity
    s.interlaced = 1 if t.is_interlaced else 0
    s.pclk = t.pixel_clock_10khz


def _custom_display_from_struct(c):
    return CustomDisplay(
        c.width, c.height, c.depth, NV_FORMAT.get(c.colorFormat),
        (c.srcPartition.x, c.srcPartition.y, c.srcPartition.w, c.srcPartition.h),
        c.xRatio, c.yRatio, _timing_from_struct(c.timing), bool(c.hwModeSetOnly),
    )


def _custom_display_to_struct(cd):
    s = NV_CUSTOM_DISPLAY()
    s.version = NV_CUSTOM_DISPLAY_VER
    s.width = cd.width
    s.height = cd.height
    s.depth = cd.depth
    s.colorFormat = int(cd.color_format)
    s.srcPartition.x, s.srcPartition.y, s.srcPartition.w, s.srcPartition.h = cd.src_partition
    s.xRatio = cd.x_ratio
    s.yRatio = cd.y_ratio
    _timing_to_struct(s.timing, cd.timing)
    s.hwModeSetOnly = 1 if cd.hw_mode_set_only else 0
    return s


def _illum_device_info_from_struct(d):
    i2c_idx = None
    if d.type == NV_GPU_CLIENT_ILLUM_DEVICE_TYPE_MCUV10:
        i2c_idx = d.data.mcuv10.i2cDevIdx

    return IllumDeviceInfo(NV_GPU_CLIENT_ILLUM_DEVICE_TYPE.get(d.type), d.ctrlModeMask, i2c_idx)


def _illum_device_control_from_struct(d):
    return IllumDeviceControl(
        NV_GPU_CLIENT_ILLUM_DEVICE_TYPE.get(d.type), bool(d.syncData.bSync), d.syncData.timeStampms,
    )


def _illum_device_control_to_struct(s, dc):
    s.type = int(dc.type)
    s.syncData.bSync = 1 if dc.needs_sync else 0
    s.syncData.timeStampms = dc.sync_timestamp_ms if dc.sync_timestamp_ms else 0


def _illum_rgb_params_from_struct(p):
    return IllumRGBColor(p.colorR, p.colorG, p.colorB, p.brightnessPct)


def _illum_rgb_params_to_struct(s, c):
    s.colorR = c.r
    s.colorG = c.g
    s.colorB = c.b
    s.brightnessPct = c.brightness_pct


def _illum_piecewise_timing_from_struct(t):
    return IllumPiecewiseLinearTiming(
        NV_GPU_CLIENT_ILLUM_PIECEWISE_LINEAR_CYCLE_TYPE.get(t.cycleType), t.grpCount,
        t.riseTimems, t.fallTimems, t.ATimems, t.BTimems, t.grpIdleTimems, t.phaseOffsetms,
    )


def _illum_piecewise_timing_to_struct(s, t):
    s.cycleType = int(t.cycle_type)
    s.grpCount = t.group_count
    s.riseTimems = t.rise_time_ms
    s.fallTimems = t.fall_time_ms
    s.ATimems = t.a_time_ms
    s.BTimems = t.b_time_ms
    s.grpIdleTimems = t.group_idle_time_ms
    s.phaseOffsetms = t.phase_offset_ms


def _illum_zone_info_from_struct(z):
    return IllumZoneInfo(
        NV_GPU_CLIENT_ILLUM_ZONE_TYPE.get(z.type), z.illumDeviceIdx, z.provIdx,
        NV_GPU_CLIENT_ILLUM_ZONE_LOCATION.get(z.zoneLocation),
    )


def _illum_zone_control_from_struct(z):
    colors = None
    brightness_pcts = None
    timing = None

    if z.type == NV_GPU_CLIENT_ILLUM_ZONE_TYPE_RGB:
        rgb = z.data.rgb.data
        if z.ctrlMode == NV_GPU_CLIENT_ILLUM_CTRL_MODE_MANUAL_RGB:
            colors = (_illum_rgb_params_from_struct(rgb.manualRGB.rgbParams),)
        elif z.ctrlMode == NV_GPU_CLIENT_ILLUM_CTRL_MODE_PIECEWISE_LINEAR_RGB:
            colors = tuple(_illum_rgb_params_from_struct(p) for p in rgb.piecewiseLinearRGB.rgbParams)
            timing = _illum_piecewise_timing_from_struct(rgb.piecewiseLinearRGB.piecewiseLinearData)
    elif z.type == NV_GPU_CLIENT_ILLUM_ZONE_TYPE_COLOR_FIXED:
        fixed = z.data.colorFixed.data
        if z.ctrlMode == NV_GPU_CLIENT_ILLUM_CTRL_MODE_MANUAL_RGB:
            brightness_pcts = (fixed.manualColorFixed.colorFixedParams.brightnessPct,)
        elif z.ctrlMode == NV_GPU_CLIENT_ILLUM_CTRL_MODE_PIECEWISE_LINEAR_RGB:
            brightness_pcts = tuple(p.brightnessPct for p in fixed.piecewiseLinearColorFixed.colorFixedParams)
            timing = _illum_piecewise_timing_from_struct(fixed.piecewiseLinearColorFixed.piecewiseLinearData)

    return IllumZoneControl(
        NV_GPU_CLIENT_ILLUM_ZONE_TYPE.get(z.type), NV_GPU_CLIENT_ILLUM_CTRL_MODE.get(z.ctrlMode),
        colors, brightness_pcts, timing,
    )


def _illum_zone_control_to_struct(s, zc):
    s.type = int(zc.type)
    s.ctrlMode = int(zc.ctrl_mode)

    if zc.type == NV_GPU_CLIENT_ILLUM_ZONE_TYPE_RGB:
        if zc.ctrl_mode == NV_GPU_CLIENT_ILLUM_CTRL_MODE_MANUAL_RGB:
            _illum_rgb_params_to_struct(s.data.rgb.data.manualRGB.rgbParams, zc.colors[0])
        elif zc.ctrl_mode == NV_GPU_CLIENT_ILLUM_CTRL_MODE_PIECEWISE_LINEAR_RGB:
            for i, c in enumerate(zc.colors):
                _illum_rgb_params_to_struct(s.data.rgb.data.piecewiseLinearRGB.rgbParams[i], c)
            _illum_piecewise_timing_to_struct(s.data.rgb.data.piecewiseLinearRGB.piecewiseLinearData, zc.timing)
    elif zc.type == NV_GPU_CLIENT_ILLUM_ZONE_TYPE_COLOR_FIXED:
        if zc.ctrl_mode == NV_GPU_CLIENT_ILLUM_CTRL_MODE_MANUAL_RGB:
            s.data.colorFixed.data.manualColorFixed.colorFixedParams.brightnessPct = zc.brightness_pcts[0]
        elif zc.ctrl_mode == NV_GPU_CLIENT_ILLUM_CTRL_MODE_PIECEWISE_LINEAR_RGB:
            for i, pct in enumerate(zc.brightness_pcts):
                s.data.colorFixed.data.piecewiseLinearColorFixed.colorFixedParams[i].brightnessPct = pct
            _illum_piecewise_timing_to_struct(s.data.colorFixed.data.piecewiseLinearColorFixed.piecewiseLinearData, zc.timing)


def _rect_from_sbox(b):
    return Rect(b.sX, b.sY, b.sWidth, b.sHeight)


def _sbox_from_rect(r):
    return NvSBox(r.x, r.y, r.width, r.height)


class Display(object):
    # NvAPI_GPU_GetEDID/NvAPI_GPU_SetEDID are wired on PhysicalGPU (legacy
    # hPhysicalGpu + single-bit output mask signature, not displayId-based --
    # see PhysicalGPU.get_edid/set_edid). Display.edid_data (NvAPI_DISP_GetEdidData)
    # is the modern, displayId-based, extension-block-aware equivalent.

    @property
    def scanout_configuration(self):
        desktopRect = NvSBox()
        scanoutRect = NvSBox()
        nvStatus = NvAPI_GPU_GetScanoutConfiguration(self.display_id, ctypes.byref(desktopRect), ctypes.byref(scanoutRect))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetScanoutConfiguration returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return ScanoutConfiguration(_rect_from_sbox(desktopRect), _rect_from_sbox(scanoutRect))

    @property
    def scanout_configuration_ex(self):
        p = NV_SCANOUT_INFORMATION()
        p.version = NV_SCANOUT_INFORMATION_VER
        nvStatus = NvAPI_GPU_GetScanoutConfigurationEx(self.display_id, ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetScanoutConfigurationEx returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return ScanoutInformation(
            _rect_from_sbox(p.sourceDesktopRect), _rect_from_sbox(p.sourceViewportRect),
            _rect_from_sbox(p.targetViewportRect), p.targetDisplayWidth, p.targetDisplayHeight,
            p.cloneImportance, NV_ROTATE.get(p.sourceToTargetRotation),
        )

    @property
    def scanout_intensity_enabled(self):
        p = NV_SCANOUT_INTENSITY_STATE_DATA()
        p.version = NV_SCANOUT_INTENSITY_STATE_VER
        nvStatus = NvAPI_GPU_GetScanoutIntensityState(self.display_id, ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetScanoutIntensityState returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return bool(p.bEnabled)

    def set_scanout_intensity(self, width, height, blending_texture, offset_texture=None, offset_tex_channels=0):
        # blending_texture/offset_texture are flat sequences of floats
        # (RGB intensity texture, width*height*3 values). Used for
        # projector edge-blending setups, not the 3D rendering pipeline.
        data = NV_SCANOUT_INTENSITY_DATA()
        data.version = NV_SCANOUT_INTENSITY_DATA_VER
        data.width = width
        data.height = height
        blendArray = (FLOAT * len(blending_texture))(*blending_texture)
        data.blendingTexture = ctypes.cast(blendArray, POINTER(FLOAT))
        if offset_texture is not None:
            offsetArray = (FLOAT * len(offset_texture))(*offset_texture)
            data.offsetTexture = ctypes.cast(offsetArray, POINTER(FLOAT))
            data.offsetTexChannels = offset_tex_channels

        pbSticky = ctypes.c_int()
        nvStatus = NvAPI_GPU_SetScanoutIntensity(self.display_id, ctypes.byref(data), ctypes.byref(pbSticky))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_SetScanoutIntensity returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return bool(pbSticky.value)

    @property
    def scanout_warping_enabled(self):
        p = NV_SCANOUT_WARPING_STATE_DATA()
        p.version = NV_SCANOUT_WARPING_STATE_VER
        nvStatus = NvAPI_GPU_GetScanoutWarpingState(self.display_id, ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetScanoutWarpingState returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return bool(p.bEnabled)

    def set_scanout_warping(self, vertices, vertex_format=NV_GPU_WARPING_VERTICE_FORMAT_TRIANGLESTRIP_XYUVRQ, texture_rect=None):
        # vertices is a flat sequence of floats, 6 per vertex (X,Y,U,V,R,Q).
        data = NV_SCANOUT_WARPING_DATA()
        data.version = NV_SCANOUT_WARPING_VER
        vertexArray = (FLOAT * len(vertices))(*vertices)
        data.vertices = ctypes.cast(vertexArray, POINTER(FLOAT))
        data.vertexFormat = int(vertex_format)
        data.numVertices = len(vertices) // 6
        if texture_rect is not None:
            rect = _sbox_from_rect(texture_rect)
            data.textureRect = ctypes.pointer(rect)

        maxNumVertices = ctypes.c_int()
        pbSticky = ctypes.c_int()
        nvStatus = NvAPI_GPU_SetScanoutWarping(self.display_id, ctypes.byref(data), ctypes.byref(maxNumVertices), ctypes.byref(pbSticky))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_SetScanoutWarping returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return maxNumVertices.value, bool(pbSticky.value)

    def get_scanout_composition_parameter(self, parameter):
        parameterData = NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE()
        pContainer = FLOAT()
        nvStatus = NvAPI_GPU_GetScanoutCompositionParameter(
            self.display_id, NV_GPU_SCANOUT_COMPOSITION_PARAMETER(int(parameter)),
            ctypes.byref(parameterData), ctypes.byref(pContainer),
        )
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetScanoutCompositionParameter returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE.get(parameterData), pContainer.value

    def set_scanout_composition_parameter(self, parameter, parameter_value, container=0.0):
        pContainer = FLOAT(container)
        nvStatus = NvAPI_GPU_SetScanoutCompositionParameter(
            self.display_id, NV_GPU_SCANOUT_COMPOSITION_PARAMETER(int(parameter)),
            NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE(int(parameter_value)), ctypes.byref(pContainer),
        )
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_SetScanoutCompositionParameter returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    def infoframe_control(self, pInfoframeData):
        # low-level passthrough -- caller populates version/size/cmd/type/
        # infoframe on an NV_INFOFRAME_DATA instance (see NV_INFOFRAME_CMD,
        # NV_INFOFRAME_PROPERTY/_VIDEO/_AUDIO). Too raw/niche a control
        # surface to justify inventing an unverified high-level API on top.
        nvStatus = NvAPI_Disp_InfoFrameControl(self.display_id, ctypes.byref(pInfoframeData))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_InfoFrameControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pInfoframeData

    @property
    def color_data(self):
        pColorData = NV_COLOR_DATA()
        pColorData.version = NV_COLOR_DATA_VER
        pColorData.cmd = NV_COLOR_CMD_GET
        nvStatus = NvAPI_Disp_ColorControl(self.display_id, ctypes.byref(pColorData))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_ColorControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        d = pColorData.data
        return ColorData(
            NV_COLOR_FORMAT.get(d.colorFormat),
            NV_COLOR_COLORIMETRY.get(d.colorimetry),
            NV_DYNAMIC_RANGE.get(d.dynamicRange),
            NV_BPC.get(d.bpc),
            NV_COLOR_SELECTION_POLICY.get(d.colorSelectionPolicy),
            NV_DESKTOP_COLOR_DEPTH.get(d.depth),
        )

    @color_data.setter
    def color_data(self, value):
        pColorData = NV_COLOR_DATA()
        pColorData.version = NV_COLOR_DATA_VER
        pColorData.cmd = NV_COLOR_CMD_SET
        pColorData.data.colorFormat = int(value.color_format)
        pColorData.data.colorimetry = int(value.colorimetry)
        pColorData.data.dynamicRange = int(value.dynamic_range)
        pColorData.data.bpc = int(value.bpc)
        pColorData.data.colorSelectionPolicy = int(value.color_selection_policy)
        pColorData.data.depth = int(value.depth)
        nvStatus = NvAPI_Disp_ColorControl(self.display_id, ctypes.byref(pColorData))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_ColorControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    def get_timing(self, width, height, refresh_rate, timing_type=NV_TIMING_OVERRIDE.NV_TIMING_OVERRIDE_CURRENT):
        timingInput = NV_TIMING_INPUT()
        timingInput.version = NV_TIMING_INPUT_VER
        timingInput.width = width
        timingInput.height = height
        timingInput.rr = refresh_rate
        timingInput.type = timing_type

        pTiming = NV_TIMING()
        nvStatus = NvAPI_DISP_GetTiming(self.display_id, ctypes.byref(timingInput), ctypes.byref(pTiming))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_GetTiming returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return TimingInfo(
            pTiming.HVisible, pTiming.HBorder, pTiming.HFrontPorch, pTiming.HSyncWidth, pTiming.HTotal, pTiming.HSyncPol,
            pTiming.VVisible, pTiming.VBorder, pTiming.VFrontPorch, pTiming.VSyncWidth, pTiming.VTotal, pTiming.VSyncPol,
            bool(pTiming.interlaced), pTiming.pclk,
        )

    def _monitor_capabilities(self, info_type):
        pMonitorCapabilities = NV_MONITOR_CAPABILITIES()
        pMonitorCapabilities.version = NV_MONITOR_CAPABILITIES_VER
        pMonitorCapabilities.infoType = info_type
        nvStatus = NvAPI_DISP_GetMonitorCapabilities(self.display_id, ctypes.byref(pMonitorCapabilities))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_GetMonitorCapabilities returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        if not pMonitorCapabilities.bIsValidInfo:
            return None

        return pMonitorCapabilities

    @property
    def monitor_capabilities_vsdb(self):
        caps = self._monitor_capabilities(NV_MONITOR_CAPS_TYPE_HDMI_VSDB)
        if caps is None:
            return None

        vsdb = caps.data.vsdb
        return MonitorCapsVSDB(
            (vsdb.sourcePhysicalAddressA << 12) | (vsdb.sourcePhysicalAddressB << 8) |
            (vsdb.sourcePhysicalAddressC << 4) | vsdb.sourcePhysicalAddressD,
            bool(vsdb.supportDualDviOperation), bool(vsdb.supportDeepColorYCbCr444),
            bool(vsdb.supportDeepColor30bits), bool(vsdb.supportDeepColor36bits),
            bool(vsdb.supportDeepColor48bits), bool(vsdb.supportAI), vsdb.maxTmdsClock,
            bool(vsdb.cnc0SupportGraphicsTextContent), bool(vsdb.cnc1SupportPhotoContent),
            bool(vsdb.cnc2SupportCinemaContent), bool(vsdb.cnc3SupportGameContent),
            bool(vsdb.hasVicEntries), bool(vsdb.hasInterlacedLatencyField), bool(vsdb.hasLatencyField),
            vsdb.videoLatency, vsdb.audioLatency, vsdb.interlacedVideoLatency, vsdb.interlacedAudioLatency,
            bool(vsdb.has3dEntries),
        )

    @property
    def monitor_capabilities_vcdb(self):
        caps = self._monitor_capabilities(NV_MONITOR_CAPS_TYPE_HDMI_VCDB)
        if caps is None:
            return None

        vcdb = caps.data.vcdb
        return MonitorCapsVCDB(
            bool(vcdb.quantizationRangeYcc), bool(vcdb.quantizationRangeRgb),
            vcdb.scanInfoPreferredVideoFormat, vcdb.scanInfoITVideoFormats, vcdb.scanInfoCEVideoFormats,
        )

    @property
    def monitor_color_capabilities(self):
        pColorCapsCount = NvU32(0)
        nvStatus = NvAPI_DISP_GetMonitorColorCapabilities(self.display_id, None, ctypes.byref(pColorCapsCount))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_GetMonitorColorCapabilities returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        if pColorCapsCount.value == 0:
            return []

        caps = (NV_MONITOR_COLOR_CAPS * pColorCapsCount.value)()
        for c in caps:
            c.version = NV_MONITOR_COLOR_CAPS_VER

        nvStatus = NvAPI_DISP_GetMonitorColorCapabilities(self.display_id, caps, ctypes.byref(pColorCapsCount))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_GetMonitorColorCapabilities returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return [
            MonitorColorCap(NV_DP_COLOR_FORMAT.get(c.colorFormat), NV_DP_BPC.get(c.backendBitDepths))
            for c in caps[:pColorCapsCount.value]
        ]
    def enum_custom_displays(self):
        index = 0
        while True:
            pCustDisp = NV_CUSTOM_DISPLAY()
            pCustDisp.version = NV_CUSTOM_DISPLAY_VER
            nvStatus = NvAPI_DISP_EnumCustomDisplay(self.display_id, NvU32(index), ctypes.byref(pCustDisp))
            if nvStatus == NvAPI_Status.NVAPI_END_ENUMERATION:
                return
            if NvAPI_Status.NVAPI_OK != nvStatus:
                szDesc = NvAPI_ShortString()
                NvAPI_GetErrorMessage(nvStatus, szDesc)
                raise RuntimeError("NvAPI_DISP_EnumCustomDisplay returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))
            yield _custom_display_from_struct(pCustDisp)
            index += 1


    @staticmethod
    def enum_display_handles():
        # legacy per-display enumeration handle -- distinct ID space from
        # the modern persistent displayId used elsewhere in this class.
        count = 0
        while True:
            hNvDisplay = NvDisplayHandle()
            nvStatus = NvAPI_EnumNvidiaDisplayHandle(NvU32(count), ctypes.byref(hNvDisplay))
            if nvStatus == NvAPI_Status.NVAPI_END_ENUMERATION:
                return
            if NvAPI_Status.NVAPI_OK != nvStatus:
                szDesc = NvAPI_ShortString()
                NvAPI_GetErrorMessage(nvStatus, szDesc)
                raise RuntimeError("NvAPI_EnumNvidiaDisplayHandle returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))
            yield hNvDisplay
            count += 1

    @staticmethod
    def enum_unattached_display_handles():
        count = 0
        while True:
            hNvUnAttachedDisp = NvUnAttachedDisplayHandle()
            nvStatus = NvAPI_EnumNvidiaUnAttachedDisplayHandle(NvU32(count), ctypes.byref(hNvUnAttachedDisp))
            if nvStatus == NvAPI_Status.NVAPI_END_ENUMERATION:
                return
            if NvAPI_Status.NVAPI_OK != nvStatus:
                szDesc = NvAPI_ShortString()
                NvAPI_GetErrorMessage(nvStatus, szDesc)
                raise RuntimeError("NvAPI_EnumNvidiaUnAttachedDisplayHandle returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))
            yield hNvUnAttachedDisp
            count += 1

    @staticmethod
    def create_display_from_unattached_display(hNvUnAttachedDisp):
        hNvDisplay = NvDisplayHandle()
        nvStatus = NvAPI_CreateDisplayFromUnAttachedDisplay(hNvUnAttachedDisp, ctypes.byref(hNvDisplay))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_CreateDisplayFromUnAttachedDisplay returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return hNvDisplay

    @staticmethod
    def get_associated_display_handle(display_name):
        hNvDisplay = NvDisplayHandle()
        nvStatus = NvAPI_GetAssociatedNvidiaDisplayHandle(display_name.encode('ascii'), ctypes.byref(hNvDisplay))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GetAssociatedNvidiaDisplayHandle returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return hNvDisplay

    @staticmethod
    def get_associated_unattached_display_handle(display_name):
        hNvUnAttachedDisp = NvUnAttachedDisplayHandle()
        nvStatus = NvAPI_DISP_GetAssociatedUnAttachedNvidiaDisplayHandle(display_name.encode('ascii'), ctypes.byref(hNvUnAttachedDisp))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_GetAssociatedUnAttachedNvidiaDisplayHandle returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return hNvUnAttachedDisp

    @staticmethod
    def get_associated_display_name(hNvDisplay):
        szDisplayName = NvAPI_ShortString()
        nvStatus = NvAPI_GetAssociatedNvidiaDisplayName(hNvDisplay, szDisplayName)
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GetAssociatedNvidiaDisplayName returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return szDisplayName.value.decode('ascii', 'replace')

    @staticmethod
    def get_unattached_display_name(hNvUnAttachedDisp):
        szDisplayName = NvAPI_ShortString()
        nvStatus = NvAPI_GetUnAttachedAssociatedDisplayName(hNvUnAttachedDisp, szDisplayName)
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GetUnAttachedAssociatedDisplayName returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return szDisplayName.value.decode('ascii', 'replace')

    @staticmethod
    def get_associated_display_output_id(hNvDisplay):
        pOutputId = NvU32()
        nvStatus = NvAPI_GetAssociatedDisplayOutputId(hNvDisplay, ctypes.byref(pOutputId))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GetAssociatedDisplayOutputId returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pOutputId.value

    @staticmethod
    def enable_hw_cursor(hNvDisplay):
        nvStatus = NvAPI_EnableHWCursor(hNvDisplay)
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_EnableHWCursor returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @staticmethod
    def disable_hw_cursor(hNvDisplay):
        nvStatus = NvAPI_DisableHWCursor(hNvDisplay)
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DisableHWCursor returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @staticmethod
    def get_vblank_counter(hNvDisplay):
        pCounter = NvU32()
        nvStatus = NvAPI_GetVBlankCounter(hNvDisplay, ctypes.byref(pCounter))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GetVBlankCounter returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pCounter.value

    @staticmethod
    def set_refresh_rate_override(hNvDisplay, outputs_mask, refresh_rate, deferred=False):
        nvStatus = NvAPI_SetRefreshRateOverride(hNvDisplay, NvU32(outputs_mask), ctypes.c_float(refresh_rate), NvU32(1 if deferred else 0))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_SetRefreshRateOverride returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    # display_port_info/hdmi_support_info moved to Port -- they're physical-
    # link properties (DPCD version, HDMI capability of the connector
    # itself), not per-display content, and their own doc comments confirm
    # they key off the output/connector, not the display's signal state.

    def __init__(self, gpu, display_id):
        
        self.gpu = gpu
        self.display_id = display_id

    @property
    def is_primary(self):
        displayId = NvU32()
        nvStatus = NvAPI_DISP_GetGDIPrimaryDisplayId(ctypes.byref(displayId))

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_GetGDIPrimaryDisplayId returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return self.display_id == displayId.value

    @property
    def _hPhysicalGpu(self):
        hPhysicalGpu = NvPhysicalGpuHandle()
        nvStatus = NvAPI_SYS_GetPhysicalGpuFromDisplayId(self.display_id, ctypes.byref(hPhysicalGpu))

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_SYS_GetPhysicalGpuFromDisplayId returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return hPhysicalGpu

    @property
    def __display_data(self):
        displayIdCount = NvU32(16)
        flags = NvU32(0)
        displayIdArray = (NV_GPU_DISPLAYIDS * 16)()
        displayIdArray[0].version = NV_GPU_DISPLAYIDS_VER

        hPhysicalGpu = NvPhysicalGpuHandle()

        NvAPI_SYS_GetPhysicalGpuFromDisplayId(
            self.display_id,
            ctypes.byref(hPhysicalGpu)
        )

        nvStatus = NvAPI_GPU_GetConnectedDisplayIds(
            hPhysicalGpu,
            displayIdArray, 
            ctypes.byref(displayIdCount), 
            flags
        )

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetConnectedDisplayIds returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        for i in range(displayIdCount.value):
            if displayIdArray[i].displayId == self.display_id:
                return displayIdArray[i]

    @property
    def __hdr_data(self):
        hdrCapabilities = NV_HDR_CAPABILITIES()
        hdrCapabilities.version = NV_HDR_CAPABILITIES_VER

        nvStatus = NvAPI_Disp_GetHdrCapabilities(
            self.display_id,
            ctypes.byref(hdrCapabilities)
        )

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_GetHdrCapabilities returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return hdrCapabilities

    @property
    def hdr(self):
        if not self.is_hdr_supported:
            return False

        hdrColorData = NV_HDR_COLOR_DATA()

        hdrColorData.version = NV_HDR_COLOR_DATA_VER
        hdrColorData.cmd = NV_HDR_CMD_GET
        hdrColorData.static_metadata_descriptor_id = NV_STATIC_METADATA_TYPE_1

        nvStatus = NvAPI_Disp_HdrColorControl(
            self.display_id,
            ctypes.byref(hdrColorData)
        )

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_HdrColorControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return hdrColorData.hdrMode != NV_HDR_MODE_OFF

    @hdr.setter
    def hdr(self, value):
        if self.is_hdr_supported:
            hdrColorData = NV_HDR_COLOR_DATA()

            hdrColorData.version = NV_HDR_COLOR_DATA_VER
            hdrColorData.cmd = NV_HDR_CMD_SET
            hdrColorData.static_metadata_descriptor_id = NV_STATIC_METADATA_TYPE_1

            if value:
                hdrColorData.hdrMode = NV_HDR_MODE_UHDA
            else:
                hdrColorData.hdrMode = NV_HDR_MODE_OFF

            nvStatus = NvAPI_Disp_HdrColorControl(
                self.display_id,
                ctypes.byref(hdrColorData)
            )

            if NvAPI_Status.NVAPI_OK != nvStatus:
                szDesc = NvAPI_ShortString()
                NvAPI_GetErrorMessage(nvStatus, szDesc)
                raise RuntimeError("NvAPI_Disp_HdrColorControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def connector_type(self):
        # __display_data is None when this display isn't in the
        # currently-connected set (it can still exist as a display ID from
        # GetAllDisplayIds without being connected right now)
        dd = self.__display_data
        if dd is None:
            return None
        return NV_MONITOR_CONN_TYPE.get(dd.connectorType)

    @property
    def is_dynamic(self):
        dd = self.__display_data
        return dd is not None and bool(dd.isDynamic)

    @property
    def is_multi_stream_root_node(self):
        dd = self.__display_data
        return dd is not None and bool(dd.isMultiStreamRootNode)

    @property
    def is_active(self):
        dd = self.__display_data
        return dd is not None and bool(dd.isActive)

    @property
    def is_cluster(self):
        dd = self.__display_data
        return dd is not None and bool(dd.isCluster)

    @property
    def is_visible(self):
        dd = self.__display_data
        return dd is not None and bool(dd.isOSVisible)

    @property
    def is_wireless_display(self):
        dd = self.__display_data
        return dd is not None and bool(dd.isWFD)

    @property
    def is_connected(self):
        dd = self.__display_data
        return dd is not None and bool(dd.isConnected)

    @property
    def is_physically_connected(self):
        dd = self.__display_data
        return dd is not None and bool(dd.isConnected) and bool(dd.isPhysicallyConnected)

    @property
    def is_hdr_supported(self):
        return self.is_st2048etof_supported

    @property
    def is_st2048etof_supported(self):
        # HDMI2.0a UHDA HDR with ST2084 EOTF (CEA861.3).
        return bool(self.__hdr_data.isST2084EotfSupported)

    @property
    def is_traditional_gamma_supported(self):
        # HDMI2.0a traditional HDR gamma (CEA861.3).
        return bool(self.__hdr_data.isTraditionalHdrGammaSupported)

    @property
    def is_edr_supported(self):
        # Extended Dynamic Range on SDR displays.
        return bool(self.__hdr_data.isEdrSupported)

    @property
    def is_traditional_sdr_gamma_supported(self):
        # HDMI2.0a traditional SDR gamma (CEA861.3).
        return bool(self.__hdr_data.isTraditionalSdrGammaSupported)

    @property
    def is_dolby_vision_supported(self):
        # Dolby Vision Support.
        return bool(self.__hdr_data.isDolbyVisionSupported)

    @property
    def hdr_dynamic_range(self):
        hdrColorData = NV_HDR_COLOR_DATA()

        hdrColorData.version = NV_HDR_COLOR_DATA_VER
        hdrColorData.cmd = NV_HDR_CMD_GET
        hdrColorData.static_metadata_descriptor_id = NV_STATIC_METADATA_TYPE_1

        nvStatus = NvAPI_Disp_HdrColorControl(
            self.display_id,
            ctypes.byref(hdrColorData)
        )

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_HdrColorControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return NV_DYNAMIC_RANGE.get(hdrColorData.hdrDynamicRange)

    @hdr_dynamic_range.setter
    def hdr_dynamic_range(self, value):
        hdrColorData = NV_HDR_COLOR_DATA()

        hdrColorData.version = NV_HDR_COLOR_DATA_VER
        hdrColorData.cmd = NV_HDR_CMD_GET
        hdrColorData.static_metadata_descriptor_id = NV_STATIC_METADATA_TYPE_1

        nvStatus = NvAPI_Disp_HdrColorControl(
            self.display_id,
            ctypes.byref(hdrColorData)
        )

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_HdrColorControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        hdrColorData.cmd = NV_HDR_CMD_SET

        value = NV_DYNAMIC_RANGE.get(value)
        if value is None:
            return

        hdrColorData.hdrDynamicRange = value

        nvStatus = NvAPI_Disp_HdrColorControl(
            self.display_id,
            ctypes.byref(hdrColorData)
        )
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_HdrColorControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def hdr_color_format(self):
        hdrColorData = NV_HDR_COLOR_DATA()

        hdrColorData.version = NV_HDR_COLOR_DATA_VER
        hdrColorData.cmd = NV_HDR_CMD_GET
        hdrColorData.static_metadata_descriptor_id = NV_STATIC_METADATA_TYPE_1

        nvStatus = NvAPI_Disp_HdrColorControl(
            self.display_id,
            ctypes.byref(hdrColorData)
        )

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_HdrColorControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return NV_COLOR_FORMAT.get(hdrColorData.hdrColorFormat)

    @hdr_color_format.setter
    def hdr_color_format(self, value):
        hdrColorData = NV_HDR_COLOR_DATA()

        hdrColorData.version = NV_HDR_COLOR_DATA_VER
        hdrColorData.cmd = NV_HDR_CMD_GET
        hdrColorData.static_metadata_descriptor_id = NV_STATIC_METADATA_TYPE_1

        nvStatus = NvAPI_Disp_HdrColorControl(
            self.display_id,
            ctypes.byref(hdrColorData)
        )

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_HdrColorControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        hdrColorData.cmd = NV_HDR_CMD_SET

        value = NV_DYNAMIC_RANGE.get(value)
        if value is None:
            return

        hdrColorData.hdrDynamicRange = value

        nvStatus = NvAPI_Disp_HdrColorControl(
            self.display_id,
            ctypes.byref(hdrColorData)
        )
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_HdrColorControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def hdr_primary_color_coordinates(self):
        #  [0x0000-0xC350] = [0.0 - 1.0]
        dd = self.__hdr_data.display_data

        red = RedCoordinate(x=dd.displayPrimary_x0, y=dd.displayPrimary_y0)
        green = GreenCoordinate(x=dd.displayPrimary_x1, y=dd.displayPrimary_y1)
        blue = BlueCoordinate(x=dd.displayPrimary_x2, y=dd.displayPrimary_y2)
        white = WhiteCoordinate(x=dd.displayWhitePoint_x, y=dd.displayWhitePoint_y)

        return ColorCoordinates(
            red=red,
            green=green,
            blue=blue,
            white=white
        )

    @hdr_primary_color_coordinates.setter
    def hdr_primary_color_coordinates(self, value):
        if not self.is_hdr_supported:
            return

        mdd = self._hdr_mastering_display_data
        mdd.displayPrimary_x0 = value.red.x
        mdd.displayPrimary_y0 = value.red.y
        mdd.displayPrimary_x1 = value.green.x
        mdd.displayPrimary_y1 = value.green.y
        mdd.displayPrimary_x2 = value.blue.x
        mdd.displayPrimary_y2 = value.blue.y
        mdd.displayWhitePoint_x = value.white.x
        mdd.displayWhitePoint_y = value.white.y

        hdrColorData = NV_HDR_COLOR_DATA()
        hdrColorData.mastering_display_data = mdd
        hdrColorData.version = NV_HDR_COLOR_DATA_VER
        hdrColorData.cmd = NV_HDR_CMD_SET
        hdrColorData.static_metadata_descriptor_id = NV_STATIC_METADATA_TYPE_1

        nvStatus = NvAPI_Disp_HdrColorControl(
            self.display_id,
            ctypes.byref(hdrColorData)
        )

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_HdrColorControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def hdr_maximum_content_light_level(self):
        if not self.is_hdr_supported:
            return

        return self._hdr_mastering_display_data.max_content_light_level

    @hdr_maximum_content_light_level.setter
    def hdr_maximum_content_light_level(self, value):
        if not self.is_hdr_supported:
            return

        mdd = self._hdr_mastering_display_data
        mdd.max_content_light_level = value

        hdrColorData = NV_HDR_COLOR_DATA()
        hdrColorData.mastering_display_data = mdd
        hdrColorData.version = NV_HDR_COLOR_DATA_VER
        hdrColorData.cmd = NV_HDR_CMD_SET
        hdrColorData.static_metadata_descriptor_id = NV_STATIC_METADATA_TYPE_1

        nvStatus = NvAPI_Disp_HdrColorControl(
            self.display_id,
            ctypes.byref(hdrColorData)
        )

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_HdrColorControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def _hdr_mastering_display_data(self):
        hdrColorData = NV_HDR_COLOR_DATA()

        hdrColorData.version = NV_HDR_COLOR_DATA_VER
        hdrColorData.cmd = NV_HDR_CMD_GET
        hdrColorData.static_metadata_descriptor_id = NV_STATIC_METADATA_TYPE_1

        nvStatus = NvAPI_Disp_HdrColorControl(
            self.display_id,
            ctypes.byref(hdrColorData)
        )

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_HdrColorControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return hdrColorData.mastering_display_data

    @property
    def hdr_maximum_luminance(self):
        # Maximum display luminance = desired max luminance of HDR
        # content ([0x0001-0xFFFF] = [1.0 - 65535.0] cd/m^2)
        dd = self.__hdr_data.display_data
        return dd.desired_content_max_luminance

    @hdr_maximum_luminance.setter
    def hdr_maximum_luminance(self, value):
        if not self.is_hdr_supported:
            return

        mdd = self._hdr_mastering_display_data
        mdd.max_display_mastering_luminance = value

        hdrColorData = NV_HDR_COLOR_DATA()
        hdrColorData.mastering_display_data = mdd
        hdrColorData.version = NV_HDR_COLOR_DATA_VER
        hdrColorData.cmd = NV_HDR_CMD_SET
        hdrColorData.static_metadata_descriptor_id = NV_STATIC_METADATA_TYPE_1

        nvStatus = NvAPI_Disp_HdrColorControl(
            self.display_id,
            ctypes.byref(hdrColorData)
        )

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_HdrColorControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def hdr_minimum_luminance(self):
        # Minimum display luminance = desired min luminance of HDR
        # content ([0x0001-0xFFFF] = [1.0 - 6.55350] cd/m^2)
        dd = self.__hdr_data.display_data
        return dd.desired_content_min_luminance

    @hdr_minimum_luminance.setter
    def hdr_minimum_luminance(self, value):
        if not self.is_hdr_supported:
            return

        mdd = self._hdr_mastering_display_data
        mdd.min_display_mastering_luminance = value

        hdrColorData = NV_HDR_COLOR_DATA()
        hdrColorData.mastering_display_data = mdd
        hdrColorData.version = NV_HDR_COLOR_DATA_VER
        hdrColorData.cmd = NV_HDR_CMD_SET
        hdrColorData.static_metadata_descriptor_id = NV_STATIC_METADATA_TYPE_1

        nvStatus = NvAPI_Disp_HdrColorControl(
            self.display_id,
            ctypes.byref(hdrColorData)
        )

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_HdrColorControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def hdr_maximum_frame_average_luminance(self):
        # Desired maximum Frame-Average Light Level (MaxFALL) of HDR
        # content ([0x0001-0xFFFF] = [1.0 - 65535.0] cd/m^2)
        dd = self.__hdr_data.display_data
        return dd.desired_content_max_frame_average_luminance

    @hdr_maximum_frame_average_luminance.setter
    def hdr_maximum_frame_average_luminance(self, value):
        if not self.is_hdr_supported:
            return

        mdd = self._hdr_mastering_display_data
        mdd.max_frame_average_light_level = value

        hdrColorData = NV_HDR_COLOR_DATA()
        hdrColorData.mastering_display_data = mdd
        hdrColorData.version = NV_HDR_COLOR_DATA_VER
        hdrColorData.cmd = NV_HDR_CMD_SET
        hdrColorData.static_metadata_descriptor_id = NV_STATIC_METADATA_TYPE_1

        nvStatus = NvAPI_Disp_HdrColorControl(
            self.display_id,
            ctypes.byref(hdrColorData)
        )

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_HdrColorControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def hdr_supports_2160p60hz(self):
        # If set sink is capable of 4kx2k @ 60hz
        dvsm = self.__hdr_data.dv_static_metadata
        return bool(dvsm.supports_2160p60hz)

    @property
    def hdr_supports_yuv422_12bit(self):
        # If set, sink is capable of YUV422-12 bit
        dvsm = self.__hdr_data.dv_static_metadata
        return bool(dvsm.supports_YUV422_12bit)

    @property
    def hdr_supports_global_dimming(self):
        # Indicates if sink supports global dimming
        dvsm = self.__hdr_data.dv_static_metadata
        return bool(dvsm.supports_global_dimming)

    @property
    def hdr_colorimetry(self):
        # If set indicates sink supports DCI P3 colorimetry, REc709 otherwise
        dvsm = self.__hdr_data.dv_static_metadata
        if bool(dvsm.colorimetry):
            return 'DCI P3'
        else:
            return 'REc709'

    @property
    def hdr_supports_backlight_control(self):
        # This is set when sink is using lowlatency interface and can control its backlight.
        dvsm = self.__hdr_data.dv_static_metadata
        return bool(dvsm.supports_backlight_control)

    @property
    def hdr_backlight_minimum(self):
        # It is the level for Backlt min luminance value.
        dvsm = self.__hdr_data.dv_static_metadata
        return dvsm.backlt_min_luma

    @property
    def hdr_interface_supported_by_sink(self):
        # Indicates the interface (standard or low latency) supported by the sink.
        dvsm = self.__hdr_data.dv_static_metadata
        return dvsm.interface_supported_by_sink

    @property
    def hdr_supports_10b_12b_444(self):
        # It is set when interface supported is low latency,
        # it tells whether it supports 10 bit or 12 bit RGB 4:4:4 or YCbCr 4:4:4 or both.
        dvsm = self.__hdr_data.dv_static_metadata
        return dvsm.supports_10b_12b_444

    @property
    def hdr_minimum_sink_luminance(self):
        # Represents min luminance level of Sink
        dvsm = self.__hdr_data.dv_static_metadata
        return dvsm.target_min_luminance

    @property
    def hdr_maximum_sink_luminance(self):
        # Represents max luminance level of sink
        dvsm = self.__hdr_data.dv_static_metadata
        return dvsm.target_max_luminance

    @property
    def hdr_primary_chromaticity_coordinates(self):
        dvsm = self.__hdr_data.dv_static_metadata

        red = RedCoordinate(x=dvsm.cc_red_x, y=dvsm.cc_red_y)
        green = GreenCoordinate(x=dvsm.cc_green_x, y=dvsm.cc_green_y)
        blue = BlueCoordinate(x=dvsm.cc_blue_x, y=dvsm.cc_blue_y)
        white = WhiteCoordinate(x=dvsm.cc_white_x, y=dvsm.cc_white_y)

        return ColorCoordinates(
            red=red,
            green=green,
            blue=blue,
            white=white
        )

    @property
    def source_color_space(self):
        # per-process value; NVAPI_ERROR here typically just means this
        # process hasn't called set_source_color_space itself yet, not a
        # hardware fault
        pColorSpaceType = ctypes.c_int()
        nvStatus = NvAPI_Disp_GetSourceColorSpace(self.display_id, ctypes.byref(pColorSpaceType), NV_SOURCE_PID_CURRENT)
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_GetSourceColorSpace returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return NV_COLORSPACE_TYPE.get(pColorSpaceType.value)

    @source_color_space.setter
    def source_color_space(self, value):
        nvStatus = NvAPI_Disp_SetSourceColorSpace(self.display_id, value)
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_SetSourceColorSpace returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def source_hdr_metadata(self):
        pMetadata = NV_HDR_METADATA()
        pMetadata.version = NV_HDR_METADATA_VER
        nvStatus = NvAPI_Disp_GetSourceHdrMetadata(self.display_id, ctypes.byref(pMetadata), NV_SOURCE_PID_CURRENT)
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_GetSourceHdrMetadata returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return HdrMetadata(
            display_primary_0=RedCoordinate(x=pMetadata.displayPrimary_x0, y=pMetadata.displayPrimary_y0),
            display_primary_1=GreenCoordinate(x=pMetadata.displayPrimary_x1, y=pMetadata.displayPrimary_y1),
            display_primary_2=BlueCoordinate(x=pMetadata.displayPrimary_x2, y=pMetadata.displayPrimary_y2),
            white_point=WhiteCoordinate(x=pMetadata.displayWhitePoint_x, y=pMetadata.displayWhitePoint_y),
            max_display_mastering_luminance=pMetadata.max_display_mastering_luminance,
            min_display_mastering_luminance=pMetadata.min_display_mastering_luminance,
            max_content_light_level=pMetadata.max_content_light_level,
            max_frame_average_light_level=pMetadata.max_frame_average_light_level,
        )

    @source_hdr_metadata.setter
    def source_hdr_metadata(self, value):
        # value: an HdrMetadata namedtuple (or anything with the same
        # attribute names, e.g. a plain object) -- the same shape returned
        # by the source_hdr_metadata getter.
        pMetadata = NV_HDR_METADATA()
        pMetadata.version = NV_HDR_METADATA_VER
        pMetadata.displayPrimary_x0 = value.display_primary_0.x
        pMetadata.displayPrimary_y0 = value.display_primary_0.y
        pMetadata.displayPrimary_x1 = value.display_primary_1.x
        pMetadata.displayPrimary_y1 = value.display_primary_1.y
        pMetadata.displayPrimary_x2 = value.display_primary_2.x
        pMetadata.displayPrimary_y2 = value.display_primary_2.y
        pMetadata.displayWhitePoint_x = value.white_point.x
        pMetadata.displayWhitePoint_y = value.white_point.y
        pMetadata.max_display_mastering_luminance = value.max_display_mastering_luminance
        pMetadata.min_display_mastering_luminance = value.min_display_mastering_luminance
        pMetadata.max_content_light_level = value.max_content_light_level
        pMetadata.max_frame_average_light_level = value.max_frame_average_light_level

        nvStatus = NvAPI_Disp_SetSourceHdrMetadata(self.display_id, ctypes.byref(pMetadata))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_SetSourceHdrMetadata returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def output_mode(self):
        pDisplayMode = ctypes.c_int()
        nvStatus = NvAPI_Disp_GetOutputMode(self.display_id, ctypes.byref(pDisplayMode))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_GetOutputMode returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return NV_DISPLAY_OUTPUT_MODE.get(pDisplayMode.value)

    @output_mode.setter
    def output_mode(self, value):
        pDisplayMode = ctypes.c_int(value)
        nvStatus = NvAPI_Disp_SetOutputMode(self.display_id, ctypes.byref(pDisplayMode))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_SetOutputMode returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def hdr_tone_mapping(self):
        pHdrTonemapping = ctypes.c_int()
        nvStatus = NvAPI_Disp_GetHdrToneMapping(self.display_id, ctypes.byref(pHdrTonemapping))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_GetHdrToneMapping returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return NV_HDR_TONEMAPPING_METHOD.get(pHdrTonemapping.value)

    @hdr_tone_mapping.setter
    def hdr_tone_mapping(self, value):
        nvStatus = NvAPI_Disp_SetHdrToneMapping(self.display_id, value)
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_SetHdrToneMapping returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def colorimetry(self):
        # requires driver release 580+
        pColorimetry = NV_DISPLAY_COLORIMETRY()
        pColorimetry.version = NV_DISPLAY_COLORIMETRY_VER
        nvStatus = NvAPI_Disp_GetColorimetry(self.display_id, ctypes.byref(pColorimetry))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_GetColorimetry returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return DisplayColorimetry(
            min_luminance=pColorimetry.min_luminance,
            max_full_frame_luminance=pColorimetry.max_full_frame_luminance,
            max_luminance=pColorimetry.max_luminance,
            hdr_brightness_luminance_scaling_factor=pColorimetry.hdrBrightnessLuminanceScalingFactor,
            red_primary=RedCoordinate(x=pColorimetry.red_primary_x, y=pColorimetry.red_primary_y),
            green_primary=GreenCoordinate(x=pColorimetry.green_primary_x, y=pColorimetry.green_primary_y),
            blue_primary=BlueCoordinate(x=pColorimetry.blue_primary_x, y=pColorimetry.blue_primary_y),
            white_point=WhiteCoordinate(x=pColorimetry.white_point_x, y=pColorimetry.white_point_y),
        )

    @property
    def edid_data(self):
        # modern replacement for the fixed-256-byte NvAPI_GPU_GetEDID
        # elsewhere in this package; two-pass allocation handles large/
        # extended EDIDs correctly
        pEdid = NV_EDID_DATA()
        pEdid.version = NV_EDID_DATA_VER
        pFlag = ctypes.c_int(0)
        nvStatus = NvAPI_DISP_GetEdidData(self.display_id, ctypes.byref(pEdid), ctypes.byref(pFlag))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_GetEdidData returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        if not pEdid.sizeOfEDID:
            return b''

        buf = (NvU8 * pEdid.sizeOfEDID)()
        pEdid2 = NV_EDID_DATA()
        pEdid2.version = NV_EDID_DATA_VER
        pEdid2.pEDID = ctypes.cast(buf, ctypes.POINTER(NvU8))
        pEdid2.sizeOfEDID = pEdid.sizeOfEDID
        nvStatus = NvAPI_DISP_GetEdidData(self.display_id, ctypes.byref(pEdid2), ctypes.byref(pFlag))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_GetEdidData returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return bytes(buf)

    @property
    def edid_info(self):
        # decoded form of edid_data -- see nvapi.edid.decode_edid for the
        # full field breakdown (manufacturer/model, native resolution,
        # supported timings, etc.)
        data = self.edid_data
        if len(data) < 128:
            return None

        return decode_edid(data)

    @property
    def adaptive_sync_data(self):
        pAdaptiveSyncData = NV_GET_ADAPTIVE_SYNC_DATA()
        pAdaptiveSyncData.version = NV_GET_ADAPTIVE_SYNC_DATA_VER
        nvStatus = NvAPI_DISP_GetAdaptiveSyncData(self.display_id, ctypes.byref(pAdaptiveSyncData))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_GetAdaptiveSyncData returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return AdaptiveSyncData(
            max_frame_interval=pAdaptiveSyncData.maxFrameInterval,
            is_adaptive_sync_disabled=bool(pAdaptiveSyncData.flags & 1),
            is_frame_splitting_disabled=bool(pAdaptiveSyncData.flags & 2),
            last_flip_refresh_count=pAdaptiveSyncData.lastFlipRefreshCount,
            last_flip_timestamp=pAdaptiveSyncData.lastFlipTimeStamp,
        )

    @adaptive_sync_data.setter
    def adaptive_sync_data(self, value):
        # value: (max_frame_interval_ns, disable_adaptive_sync, disable_frame_splitting) tuple.
        max_frame_interval_ns, disable_adaptive_sync, disable_frame_splitting = value
        pAdaptiveSyncData = NV_SET_ADAPTIVE_SYNC_DATA()
        pAdaptiveSyncData.version = NV_SET_ADAPTIVE_SYNC_DATA_VER
        pAdaptiveSyncData.maxFrameIntervalNs = max_frame_interval_ns
        pAdaptiveSyncData.flags = (1 if disable_adaptive_sync else 0) | (2 if disable_frame_splitting else 0)

        nvStatus = NvAPI_DISP_SetAdaptiveSyncData(self.display_id, ctypes.byref(pAdaptiveSyncData))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_SetAdaptiveSyncData returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def virtual_refresh_rate_data(self):
        pVirtualRefreshRateData = NV_GET_VIRTUAL_REFRESH_RATE_DATA()
        pVirtualRefreshRateData.version = NV_GET_VIRTUAL_REFRESH_RATE_DATA_VER
        nvStatus = NvAPI_DISP_GetVirtualRefreshRateData(self.display_id, ctypes.byref(pVirtualRefreshRateData))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_GetVirtualRefreshRateData returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return VirtualRefreshRateData(
            frame_interval_us=pVirtualRefreshRateData.frameIntervalUs,
            refresh_rate_x1000=pVirtualRefreshRateData.rrx1k,
            is_gaming_vrr=bool(pVirtualRefreshRateData.bIsGamingVrr),
        )

    @virtual_refresh_rate_data.setter
    def virtual_refresh_rate_data(self, value):
        # value: (frame_interval_us, refresh_rate_x1000, is_gaming_vrr) tuple.
        frame_interval_us, refresh_rate_x1000, is_gaming_vrr = value
        pVirtualRefreshRateData = NV_SET_VIRTUAL_REFRESH_RATE_DATA()
        pVirtualRefreshRateData.version = NV_SET_VIRTUAL_REFRESH_RATE_DATA_VER
        pVirtualRefreshRateData.frameIntervalUs = frame_interval_us
        pVirtualRefreshRateData.rrx1k = refresh_rate_x1000
        pVirtualRefreshRateData.bIsGamingVrr = 1 if is_gaming_vrr else 0

        nvStatus = NvAPI_DISP_SetVirtualRefreshRateData(self.display_id, ctypes.byref(pVirtualRefreshRateData))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_SetVirtualRefreshRateData returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def dedicated_display_metadata(self):
        pMetadata = NV_MANAGED_DEDICATED_DISPLAY_METADATA()
        pMetadata.version = NV_MANAGED_DEDICATED_DISPLAY_METADATA_VER
        pMetadata.displayId = self.display_id
        nvStatus = NvAPI_DISP_GetNvManagedDedicatedDisplayMetadata(ctypes.byref(pMetadata))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_GetNvManagedDedicatedDisplayMetadata returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return DedicatedDisplayMetadata(
            position_x=pMetadata.positionX,
            position_y=pMetadata.positionY,
            position_is_available=bool(pMetadata.flags & 4),
            name=pMetadata.name.decode('ascii', 'replace').rstrip('\x00'),
            name_is_available=bool(pMetadata.flags & 32),
        )

    @dedicated_display_metadata.setter
    def dedicated_display_metadata(self, value):
        # value: (position_x, position_y, name) tuple. position_x/position_y
        # must both be set together to update position; either may be None
        # (along with name) to leave that part unchanged.
        position_x, position_y, name = value
        pMetadata = NV_MANAGED_DEDICATED_DISPLAY_METADATA()
        pMetadata.version = NV_MANAGED_DEDICATED_DISPLAY_METADATA_VER
        pMetadata.displayId = self.display_id

        flags = 0
        if position_x is not None and position_y is not None:
            flags |= 1  # bSetPosition
            pMetadata.positionX = position_x
            pMetadata.positionY = position_y
        if name is not None:
            flags |= 8  # bSetName
            pMetadata.name = name.encode('ascii', 'replace')
        pMetadata.flags = flags

        nvStatus = NvAPI_DISP_SetNvManagedDedicatedDisplayMetadata(ctypes.byref(pMetadata))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_SetNvManagedDedicatedDisplayMetadata returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    def acquire_dedicated_display(self):
        pDisplaySourceHandle = ctypes.c_uint64()
        nvStatus = NvAPI_DISP_AcquireDedicatedDisplay(self.display_id, ctypes.byref(pDisplaySourceHandle))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_AcquireDedicatedDisplay returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pDisplaySourceHandle.value

    def release_dedicated_display(self):
        nvStatus = NvAPI_DISP_ReleaseDedicatedDisplay(self.display_id)
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_ReleaseDedicatedDisplay returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def display_id_info(self):
        pDisplayIdInfoData = NV_DISPLAY_ID_INFO_DATA()
        pDisplayIdInfoData.version = NV_DISPLAY_ID_INFO_DATA_VER
        nvStatus = NvAPI_Disp_GetDisplayIdInfo(self.display_id, ctypes.byref(pDisplayIdInfoData))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_GetDisplayIdInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return DisplayIdInfo(
            adapter_luid='%08x-%08x' % (pDisplayIdInfoData.adapterId.HighPart & 0xFFFFFFFF, pDisplayIdInfoData.adapterId.LowPart),
            target_id=pDisplayIdInfoData.targetId,
        )

    @property
    def grid_display_ids(self):
        # every displayId sharing this display's (adapterId, targetId)
        # pair -- more than one entry only when part of a Mosaic/Surround
        # display grid
        pDisplayIdInfoData = NV_DISPLAY_ID_INFO_DATA()
        pDisplayIdInfoData.version = NV_DISPLAY_ID_INFO_DATA_VER
        nvStatus = NvAPI_Disp_GetDisplayIdInfo(self.display_id, ctypes.byref(pDisplayIdInfoData))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_GetDisplayIdInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        pTargetInfoData = NV_TARGET_INFO_DATA()
        pTargetInfoData.version = NV_TARGET_INFO_DATA_VER
        pTargetInfoData.adapterId = pDisplayIdInfoData.adapterId
        pTargetInfoData.targetId = pDisplayIdInfoData.targetId
        nvStatus = NvAPI_Disp_GetDisplayIdsFromTarget(ctypes.byref(pTargetInfoData))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_GetDisplayIdsFromTarget returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return [pTargetInfoData.displayId[i] for i in range(pTargetInfoData.displayIdCount)]

    @property
    def vrr_info(self):
        pVrrInfo = NV_GET_VRR_INFO()
        pVrrInfo.version = NV_GET_VRR_INFO_VER
        nvStatus = NvAPI_Disp_GetVRRInfo(self.display_id, ctypes.byref(pVrrInfo))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_Disp_GetVRRInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return VRRInfo(
            is_vrr_enabled=bool(pVrrInfo.flags & 1),
            is_vrr_possible=bool(pVrrInfo.flags & 2),
            is_vrr_requested=bool(pVrrInfo.flags & 4),
            is_vrr_indicator_enabled=bool(pVrrInfo.flags & 8),
            is_display_in_vrr_mode=bool(pVrrInfo.flags & 16),
        )


def _get_bit(byteval, idx):
    return byteval & (1 << idx) != 0


class PhysicalGPU(object):
    @property
    def _hdcp_support_status(self):
        pGetHDCPSupportStatus = NV_GPU_GET_HDCP_SUPPORT_STATUS()
        pGetHDCPSupportStatus.version = NV_GPU_GET_HDCP_SUPPORT_STATUS_VER
        nvStatus = NvAPI_GPU_GetHDCPSupportStatus(self._hPhysicalGpu,  ctypes.byref(pGetHDCPSupportStatus))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetHDCPSupportStatus returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pGetHDCPSupportStatus

    @property
    def hdcp_fuse_state(self):

        return NV_GPU_HDCP_FUSE_STATE.get(self._hdcp_support_status.hdcpFuseState)

    @property
    def hdcp_key_source(self):

        return NV_GPU_HDCP_KEY_SOURCE.get(self._hdcp_support_status.hdcpKeySource)

    @property
    def hdcp_key_source_state(self):

        return NV_GPU_HDCP_KEY_SOURCE_STATE.get(self._hdcp_support_status.hdcpKeySourceState)

    @property
    def shader_sub_pipe_count(self):
        hPhysicalGpu = self._hPhysicalGpu
        pCount = NvU32()
        nvStatus = NvAPI_GPU_GetShaderSubPipeCount(hPhysicalGpu, ctypes.byref(pCount))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetShaderSubPipeCount returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pCount.value

    @property
    def core_count(self):
        hPhysicalGpu = self._hPhysicalGpu
        pCount = NvU32()
        nvStatus = NvAPI_GPU_GetGpuCoreCount(hPhysicalGpu, ctypes.byref(pCount))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetGpuCoreCount returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pCount.value

    @property
    def all_outputs(self):
        pOutputsMask = NvU32()
        nvStatus = NvAPI_GPU_GetAllOutputs(self._hPhysicalGpu, ctypes.byref(pOutputsMask))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetAllOutputs returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pOutputsMask.value

    @property
    def connected_outputs(self):
        pOutputsMask = NvU32()
        nvStatus = NvAPI_GPU_GetConnectedOutputs(self._hPhysicalGpu, ctypes.byref(pOutputsMask))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetConnectedOutputs returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pOutputsMask.value

    @property
    def connected_sli_outputs(self):
        pOutputsMask = NvU32()
        nvStatus = NvAPI_GPU_GetConnectedSLIOutputs(self._hPhysicalGpu, ctypes.byref(pOutputsMask))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetConnectedSLIOutputs returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pOutputsMask.value

    @property
    def connected_outputs_with_lid_state(self):
        pOutputsMask = NvU32()
        nvStatus = NvAPI_GPU_GetConnectedOutputsWithLidState(self._hPhysicalGpu, ctypes.byref(pOutputsMask))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetConnectedOutputsWithLidState returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pOutputsMask.value

    @property
    def connected_sli_outputs_with_lid_state(self):
        pOutputsMask = NvU32()
        nvStatus = NvAPI_GPU_GetConnectedSLIOutputsWithLidState(self._hPhysicalGpu, ctypes.byref(pOutputsMask))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetConnectedSLIOutputsWithLidState returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pOutputsMask.value

    @property
    def system_type(self):
        pSystemType = NV_SYSTEM_TYPE()
        nvStatus = NvAPI_GPU_GetSystemType(self._hPhysicalGpu,  ctypes.byref(pSystemType))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetConnectedDisplayIds returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return NV_SYSTEM_TYPE.get(pSystemType)

    @property
    def active_outputs(self):
        pOutputsMask = NvU32()
        nvStatus = NvAPI_GPU_GetActiveOutputs(self._hPhysicalGpu, ctypes.byref(pOutputsMask))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetActiveOutputs returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pOutputsMask.value

    def output_type(self, output_id):
        pOutputType = NV_GPU_OUTPUT_TYPE()
        nvStatus = NvAPI_GPU_GetOutputType(self._hPhysicalGpu, NvU32(output_id), ctypes.byref(pOutputType))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetOutputType returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return NV_GPU_OUTPUT_TYPE.get(pOutputType)

    def connector_info(self, output_id):
        # NvAPI_GPU_GetConnectorInfo -- reverse-engineered, undocumented.
        # See the comment on NV_GPU_CONNECTOR_INFO in nvapi_gpu_info_ext_h.py
        # for how the struct layout was determined and what's been verified.
        info = NV_GPU_CONNECTOR_INFO()
        info.version = NV_GPU_CONNECTOR_INFO_VER
        nvStatus = NvAPI_GPU_GetConnectorInfo(self._hPhysicalGpu, NvU32(output_id), ctypes.byref(info))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetConnectorInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return ConnectorInfo(NV_GPU_CONNECTOR_TYPE.get(info.connectorType), info.connectorIndex)

    def validate_output_combination(self, outputs_mask):
        nvStatus = NvAPI_GPU_ValidateOutputCombination(self._hPhysicalGpu, NvU32(outputs_mask))
        if nvStatus == NvAPI_Status.NVAPI_INVALID_COMBINATION:
            return False
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_ValidateOutputCombination returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return True

    def get_edid(self, output_id, edid_id=0, offset=0):
        # legacy 256-byte-page EDID accessor (single bit set in output_id).
        # Display.edid_data (NvAPI_DISP_GetEdidData) is the modern,
        # displayId-based equivalent that assembles the full multi-page
        # EDID for you -- prefer it unless you specifically need this
        # GPU+output-bitmask entry point.
        edid = NV_EDID()
        edid.version = NV_EDID_VER
        edid.edidId = edid_id
        edid.offset = offset
        nvStatus = NvAPI_GPU_GetEDID(self._hPhysicalGpu, NvU32(output_id), ctypes.byref(edid))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetEDID returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return EdidPage(bytes(edid.EDID_Data), edid.edidId, edid.sizeofEDID)

    def set_edid(self, output_id, edid_bytes):
        edid = NV_EDID()
        edid.version = NV_EDID_VER
        data = bytes(edid_bytes)[:NV_EDID_DATA_SIZE]
        ctypes.memmove(edid.EDID_Data, data, len(data))
        edid.sizeofEDID = len(data)
        nvStatus = NvAPI_GPU_SetEDID(self._hPhysicalGpu, NvU32(output_id), ctypes.byref(edid))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_SetEDID returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def full_name(self):
        szName = NvAPI_ShortString()
        nvStatus = NvAPI_GPU_GetFullName(self._hPhysicalGpu, szName)
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetFullName returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return szName.value.decode('ascii', 'replace')

    @property
    def short_name(self):
        # e.g. "TU104GL-A" -- the GPU die codename, distinct from
        # full_name's marketing name (e.g. "Quadro RTX 4000"). Undocumented
        # -- see the comment on this group of functions in
        # nvapi_gpu_info_ext_h.py for sourcing/verification.
        szName = NvAPI_ShortString()
        nvStatus = NvAPI_GPU_GetShortName(self._hPhysicalGpu, szName)
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetShortName returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return szName.value.decode('ascii', 'replace')

    @property
    def ram_type(self):
        pMemType = NvU32()
        nvStatus = NvAPI_GPU_GetRamType(self._hPhysicalGpu, ctypes.byref(pMemType))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetRamType returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return NV_GPU_RAM_TYPE.get(pMemType.value)

    @property
    def ram_maker(self):
        pRamMaker = NvU32()
        nvStatus = NvAPI_GPU_GetRamMaker(self._hPhysicalGpu, ctypes.byref(pRamMaker))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetRamMaker returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return NV_GPU_RAM_MAKER.get(pRamMaker.value)

    @property
    def ram_bank_count(self):
        pRamBankCount = NvU32()
        nvStatus = NvAPI_GPU_GetRamBankCount(self._hPhysicalGpu, ctypes.byref(pRamBankCount))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetRamBankCount returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pRamBankCount.value

    @property
    def foundry(self):
        pFoundry = NvU32()
        nvStatus = NvAPI_GPU_GetFoundry(self._hPhysicalGpu, ctypes.byref(pFoundry))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetFoundry returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return NV_GPU_FOUNDRY.get(pFoundry.value)

    @property
    def shader_pipe_count(self):
        # distinct real metric from shader_sub_pipe_count -- verified live
        # to return a different value (5 vs 18 on the test GPU), not an
        # alias of it.
        pCount = NvU32()
        nvStatus = NvAPI_GPU_GetShaderPipeCount(self._hPhysicalGpu, ctypes.byref(pCount))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetShaderPipeCount returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pCount.value

    @property
    def partition_count(self):
        pPartitionCount = NvU32()
        nvStatus = NvAPI_GPU_GetPartitionCount(self._hPhysicalGpu, ctypes.byref(pPartitionCount))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetPartitionCount returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pPartitionCount.value

    @property
    def driver_model(self):
        # raw value, meaning undocumented -- exposed as-is rather than
        # guessed at.
        pDriverModel = NvU32()
        nvStatus = NvAPI_GetDriverModel(self._hPhysicalGpu, ctypes.byref(pDriverModel))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GetDriverModel returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pDriverModel.value

    @property
    def framebuffer_width_and_location(self):
        pWidth = NvU32()
        pLocation = NvU32()
        nvStatus = NvAPI_GPU_GetFBWidthAndLocation(self._hPhysicalGpu, ctypes.byref(pWidth), ctypes.byref(pLocation))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetFBWidthAndLocation returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return FramebufferWidthAndLocation(pWidth.value, pLocation.value)

    @property
    def _pci_identifiers(self):
        pDeviceId = NvU32()
        pSubSystemId = NvU32()
        pRevisionId = NvU32()
        pExtDeviceId = NvU32()
        nvStatus = NvAPI_GPU_GetPCIIdentifiers(
            self._hPhysicalGpu,
            ctypes.byref(pDeviceId),
            ctypes.byref(pSubSystemId),
            ctypes.byref(pRevisionId),
            ctypes.byref(pExtDeviceId)
        )
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetPCIIdentifiers returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return (
            pDeviceId.value,
            pSubSystemId.value,
            pRevisionId.value,
            pExtDeviceId.value
        )

    @property
    def pci_device_id(self):
        return self._pci_identifiers[0]

    @property
    def pci_subsystem_id(self):
        return self._pci_identifiers[1]

    @property
    def pci_revision_id(self):
        return self._pci_identifiers[2]

    @property
    def pci_ext_device_id(self):
        return self._pci_identifiers[3]

    @property
    def gpu_type(self):
        pGpuType = NV_GPU_TYPE()
        nvStatus = NvAPI_GPU_GetGPUType(self._hPhysicalGpu, ctypes.byref(pGpuType))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetGPUType returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return NV_GPU_TYPE.get(pGpuType)

    @property
    def bus_type(self):
        pBusType = NV_GPU_BUS_TYPE()
        nvStatus = NvAPI_GPU_GetBusType(self._hPhysicalGpu, ctypes.byref(pBusType))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetBusType returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return NV_GPU_BUS_TYPE.get(pBusType)

    @property
    def bus_id(self):
        pBusId = NvU32()
        nvStatus = NvAPI_GPU_GetBusId(self._hPhysicalGpu, ctypes.byref(pBusId))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetBusId returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pBusId.value

    @property
    def bus_slot_id(self):
        pBusSlotId = NvU32()
        nvStatus = NvAPI_GPU_GetTachReading(self._hPhysicalGpu, ctypes.byref(pBusSlotId))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetTachReading returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pBusSlotId.value

    @property
    def irq(self):
        pIRQ = NvU32()
        nvStatus = NvAPI_GPU_GetIRQ(self._hPhysicalGpu, ctypes.byref(pIRQ))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetIRQ returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pIRQ.value

    @property
    def vbios_revision(self):
        pBiosRevision = NvU32()
        nvStatus = NvAPI_GPU_GetVbiosRevision(self._hPhysicalGpu, ctypes.byref(pBiosRevision))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetVbiosRevision returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))
        return pBiosRevision.value

    @property
    def oem_vbios_revision(self):
        # (NvPhysicalGpuHandle hPhysicalGpu,NvU32 *);
        pBiosRevision = NvU32()
        nvStatus = NvAPI_GPU_GetVbiosOEMRevision(self._hPhysicalGpu, ctypes.byref(pBiosRevision))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetVbiosOEMRevision returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pBiosRevision.value

    @property
    def vbios_version(self):
        szBiosRevision = NvAPI_ShortString()
        nvStatus = NvAPI_GPU_GetVbiosVersionString(self._hPhysicalGpu, szBiosRevision)

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetVbiosVersionString returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return szBiosRevision.value

    @property
    def agp_aperture(self):
        # (NvPhysicalGpuHandle hPhysicalGpu,NvU32 *);
        pSize = NvU32()
        nvStatus = NvAPI_GPU_GetAGPAperture(self._hPhysicalGpu, ctypes.byref(pSize))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetAGPAperture returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pSize.value

    @property
    def current_agp_rate(self):
        pRate = NvU32()
        nvStatus = NvAPI_GPU_GetCurrentAGPRate(self._hPhysicalGpu, ctypes.byref(pRate))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetCurrentAGPRate returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pRate.value

    @property
    def current_pcie_downstream_width(self):
        pWidth = NvU32()
        nvStatus = NvAPI_GPU_GetCurrentPCIEDownstreamWidth(self._hPhysicalGpu, ctypes.byref(pWidth))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetCurrentPCIEDownstreamWidth returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pWidth.value

    @property
    def physical_frame_buffer_size(self):
        pSize = NvU32()
        nvStatus = NvAPI_GPU_GetPhysicalFrameBufferSize(self._hPhysicalGpu, ctypes.byref(pSize))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetPhysicalFrameBufferSize returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pSize.value

    @property
    def virtual_frame_buffer_size(self):
        pSize = NvU32()
        nvStatus = NvAPI_GPU_GetVirtualFrameBufferSize(self._hPhysicalGpu, ctypes.byref(pSize))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetVirtualFrameBufferSize returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pSize.value

    @property
    def quadro_status(self):
        pStatus = NvU32()
        nvStatus = NvAPI_GPU_GetQuadroStatus(self._hPhysicalGpu, ctypes.byref(pStatus))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetQuadroStatus returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return 'Quadro' if pStatus.value else 'GeForce'

    @property
    def serial_number(self):
        pBoardInfo = NV_BOARD_INFO()
        pBoardInfo.version = NV_BOARD_INFO_VER
        nvStatus = NvAPI_GPU_GetBoardInfo(self._hPhysicalGpu, ctypes.byref(pBoardInfo))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetBoardInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        # BoardNum is a fixed 16-byte NUL-terminated buffer (NvU8 * 16, not
        # a char array, so it doesn't auto-unwrap) -- the previous chr()-
        # per-byte loop included the buffer's tail past the terminator as
        # literal characters, which show up as invisible junk after the
        # real serial number.
        chars = []
        for b in bytes(pBoardInfo.BoardNum):
            if b == 0x00:
                break
            if 0x20 <= b <= 0x7e:
                chars.append(chr(b))

        return ''.join(chars)

    @property
    def tach_reading(self):
        pValue = NvU32()
        nvStatus = NvAPI_GPU_GetTachReading(self._hPhysicalGpu,  ctypes.byref(pValue))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetTachReading returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pValue.value

    # --- legacy "Cooler" API (undocumented, older GPUs) ---
    # verified live: returns NVAPI_NOT_SUPPORTED on this Turing-based
    # Quadro RTX 4000 -- a legitimate per-GPU "not supported" result (this
    # generation uses the ClientFanCoolers API below instead), not a bug.

    @property
    def cooler_settings(self):
        p = NV_GPU_COOLER_SETTINGS()
        p.version = NV_GPU_COOLER_SETTINGS_VER
        nvStatus = NvAPI_GPU_GetCoolerSettings(self._hPhysicalGpu, NvU32(int(NV_COOLER_TARGET.NVAPI_COOLER_TARGET_ALL)), ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetCoolerSettings returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        res = []
        for i in range(p.count):
            s = p.settings[i]
            res.append(CoolerSetting(
                cooler_type=NV_COOLER_TYPE.get(s.coolerType),
                controller=NV_COOLER_CONTROLLER.get(s.controller),
                default_minimum_level=s.defaultMinLevel,
                default_maximum_level=s.defaultMaxLevel,
                current_minimum_level=s.currentMinLevel,
                current_maximum_level=s.currentMaxLevel,
                current_level=s.currentLevel,
                default_policy=NV_COOLER_POLICY.decode_flags(s.defaultPolicy),
                current_policy=NV_COOLER_POLICY.decode_flags(s.currentPolicy),
                target=NV_COOLER_TARGET.decode_flags(s.target),
                control_mode=NV_COOLER_CONTROL_MODE.get(s.controlMode),
                is_active=bool(s.isActive),
            ))
        return res

    @property
    def current_fan_speed_level(self):
        # legacy API's fan speed level, in percentage
        pLevel = NvU32()
        nvStatus = NvAPI_GPU_GetCurrentFanSpeedLevel(self._hPhysicalGpu, ctypes.byref(pLevel))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetCurrentFanSpeedLevel returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pLevel.value

    def set_cooler_levels(self, index, level, policy=None):
        # WRITE: changes live fan behavior on real hardware. Do not call
        # without the user's explicit go-ahead.
        #
        # UNVERIFIED: falahati/NvAPIWrapper (used below) declares this
        # function as (gpu, index, *levels, count) -- 4 args. A second,
        # independent source (JustAMan/pynvraw) declares it as (gpu,
        # index, *levels) -- 3 args, no count -- and fills every slot in
        # a fixed-size 20-entry array rather than passing a count. These
        # disagree and this path has not been tested against real
        # hardware to resolve it; if this call misbehaves, try dropping
        # the trailing NvU32(1) argument first.
        if policy is None:
            policy = NV_COOLER_POLICY.NVAPI_COOLER_POLICY_MANUAL

        p = NV_GPU_COOLER_LEVELS()
        p.version = NV_GPU_COOLER_LEVELS_VER
        p.levels[0].currentLevel = level
        p.levels[0].currentPolicy = int(policy)
        nvStatus = NvAPI_GPU_SetCoolerLevels(self._hPhysicalGpu, NvU32(index), ctypes.byref(p), NvU32(1))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_SetCoolerLevels returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    def restore_cooler_settings(self, indexes=None):
        # WRITE: resets fan policy/level to the driver default. Do not
        # call without the user's explicit go-ahead.
        if indexes:
            arr = (NvU32 * len(indexes))(*indexes)
            pIndexes = ctypes.cast(arr, ctypes.POINTER(NvU32))
            count = len(indexes)
        else:
            pIndexes = None
            count = 0

        nvStatus = NvAPI_GPU_RestoreCoolerSettings(self._hPhysicalGpu, pIndexes, NvU32(count))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_RestoreCoolerSettings returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    def cooler_policy_table(self, index, policy):
        p = NV_GPU_COOLER_POLICY_TABLE()
        p.version = NV_GPU_COOLER_POLICY_TABLE_VER
        p.policy = int(policy)
        pCount = NvU32()
        nvStatus = NvAPI_GPU_GetCoolerPolicyTable(self._hPhysicalGpu, NvU32(index), ctypes.byref(p), ctypes.byref(pCount))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetCoolerPolicyTable returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        entries = [
            CoolerPolicyTableEntry(p.entries[i].entryId, p.entries[i].currentLevel, p.entries[i].defaultLevel)
            for i in range(pCount.value)
        ]
        return CoolerPolicyTable(policy=NV_COOLER_POLICY.decode_flags(p.policy), entries=entries)

    def set_cooler_policy_table(self, index, policy, entries):
        # WRITE: changes live fan policy on real hardware. Do not call
        # without the user's explicit go-ahead. entries: list of
        # (entry_id, current_level, default_level) tuples.
        p = NV_GPU_COOLER_POLICY_TABLE()
        p.version = NV_GPU_COOLER_POLICY_TABLE_VER
        p.policy = int(policy)
        for i, (entry_id, current_level, default_level) in enumerate(entries):
            p.entries[i].entryId = entry_id
            p.entries[i].currentLevel = current_level
            p.entries[i].defaultLevel = default_level

        nvStatus = NvAPI_GPU_SetCoolerPolicyTable(self._hPhysicalGpu, NvU32(index), ctypes.byref(p), NvU32(len(entries)))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_SetCoolerPolicyTable returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    def restore_cooler_policy_table(self, policy, indexes=None):
        # WRITE: resets fan policy table to the driver default. Do not
        # call without the user's explicit go-ahead.
        if indexes:
            arr = (NvU32 * len(indexes))(*indexes)
            pIndexes = ctypes.cast(arr, ctypes.POINTER(NvU32))
            count = len(indexes)
        else:
            pIndexes = None
            count = 0

        nvStatus = NvAPI_GPU_RestoreCoolerPolicyTable(self._hPhysicalGpu, pIndexes, NvU32(count), NvU32(int(policy)))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_RestoreCoolerPolicyTable returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    # --- modern "ClientFanCoolers" API (undocumented, current-gen GPUs) ---

    @property
    def fan_coolers_info(self):
        p = NV_GPU_CLIENT_FAN_COOLERS_INFO()
        p.version = NV_GPU_CLIENT_FAN_COOLERS_INFO_VER
        nvStatus = NvAPI_GPU_ClientFanCoolersGetInfo(self._hPhysicalGpu, ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_ClientFanCoolersGetInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return FanCoolersInfo(
            is_supported=bool(p.supported),
            coolers=[
                FanCoolerInfo(p.entries[i].coolerId, p.entries[i].maximumRPM)
                for i in range(p.count)
            ],
        )

    @property
    def fan_coolers_status(self):
        p = NV_GPU_CLIENT_FAN_COOLERS_STATUS()
        p.version = NV_GPU_CLIENT_FAN_COOLERS_STATUS_VER
        nvStatus = NvAPI_GPU_ClientFanCoolersGetStatus(self._hPhysicalGpu, ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_ClientFanCoolersGetStatus returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return [
            FanCoolerStatus(
                p.entries[i].coolerId, p.entries[i].currentRPM, p.entries[i].currentMinimumLevel,
                p.entries[i].currentMaximumLevel, p.entries[i].currentLevel,
            )
            for i in range(p.count)
        ]

    @property
    def fan_coolers_control(self):
        p = NV_GPU_CLIENT_FAN_COOLERS_CONTROL()
        p.version = NV_GPU_CLIENT_FAN_COOLERS_CONTROL_VER
        nvStatus = NvAPI_GPU_ClientFanCoolersGetControl(self._hPhysicalGpu, ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_ClientFanCoolersGetControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return [
            FanCoolerControl(
                p.entries[i].coolerId, NV_FAN_COOLERS_CONTROL_MODE.get(p.entries[i].controlMode),
                p.entries[i].level,
            )
            for i in range(p.count)
        ]

    @fan_coolers_control.setter
    def fan_coolers_control(self, entries):
        # WRITE: changes live fan behavior on real hardware. Do not call
        # without the user's explicit go-ahead. entries: list of
        # (cooler_id, control_mode, level) tuples -- control_mode is
        # NV_FAN_COOLERS_CONTROL_MODE.NVAPI_FAN_COOLERS_CONTROL_MODE_AUTO
        # or _MANUAL; level (percentage) only matters for Manual.
        p = NV_GPU_CLIENT_FAN_COOLERS_CONTROL()
        p.version = NV_GPU_CLIENT_FAN_COOLERS_CONTROL_VER
        p.count = len(entries)
        for i, (cooler_id, control_mode, level) in enumerate(entries):
            p.entries[i].coolerId = cooler_id
            p.entries[i].controlMode = int(control_mode)
            p.entries[i].level = level

        nvStatus = NvAPI_GPU_ClientFanCoolersSetControl(self._hPhysicalGpu, ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_ClientFanCoolersSetControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    # --- voltage (undocumented) ---

    @property
    def current_voltage(self):
        # actual present core voltage, in volts
        p = NV_GPU_VOLTAGE_STATUS()
        p.version = NV_GPU_VOLTAGE_STATUS_VER
        nvStatus = NvAPI_GPU_GetCurrentVoltage(self._hPhysicalGpu, ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetCurrentVoltage returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return p.voltage_uV / 1000000.0

    @property
    def core_voltage_boost_percent(self):
        p = NV_GPU_VOLTAGE_BOOST_PERCENT()
        p.version = NV_GPU_VOLTAGE_BOOST_PERCENT_VER
        nvStatus = NvAPI_GPU_GetCoreVoltageBoostPercent(self._hPhysicalGpu, ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetCoreVoltageBoostPercent returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return p.percent

    def set_core_voltage_boost_percent(self, percent):
        # WRITE: overvolts/undervolts the GPU core on real hardware.
        # Undocumented by NVIDIA and NEVER tested against real hardware
        # by this library -- an incorrect or excessive value can damage
        # your GPU, other hardware, or cause system instability. The
        # authors of this library are not responsible for any damage
        # caused by using this feature. Requires interactive
        # confirmation; will not run under a non-interactive stdin.
        print('!' * 70)
        print('WARNING: about to change the GPU core voltage boost to %s%%.' % percent)
        print('This function is UNDOCUMENTED by NVIDIA and UNTESTED against')
        print('real hardware by this library. An incorrect or excessive value')
        print('can damage your GPU, other hardware, or cause system instability.')
        print('The authors of this library are NOT responsible for any damage')
        print('caused by using this feature. Proceed at your own risk.')
        print('!' * 70)
        response = input("Type Continue (exact case, no quotes) to proceed, anything else aborts: ")
        if response != 'Continue':
            raise RuntimeError("Core voltage boost change aborted -- confirmation not given.")

        p = NV_GPU_VOLTAGE_BOOST_PERCENT()
        p.version = NV_GPU_VOLTAGE_BOOST_PERCENT_VER
        p.percent = percent
        nvStatus = NvAPI_GPU_SetCoreVoltageBoostPercent(self._hPhysicalGpu, ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_SetCoreVoltageBoostPercent returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    def _i2c_info(self, display_mask, i2c_dev_address, reg_address, is_ddc_port, speed_khz, port_id):
        info = NV_I2C_INFO()
        info.version = NV_I2C_INFO_VER
        info.displayMask = display_mask
        info.bIsDDCPort = 1 if is_ddc_port else 0
        info.i2cDevAddress = i2c_dev_address
        if reg_address is not None:
            regArray = (NvU8 * len(reg_address))(*bytearray(reg_address))
            info.pbI2cRegAddress = ctypes.cast(regArray, POINTER(NvU8))
            info.regAddrSize = len(reg_address)
            info._reg_address_buffer = regArray
        else:
            info.regAddrSize = 0
        info.i2cSpeed = NVAPI_I2C_SPEED_DEPRECATED
        info.i2cSpeedKhz = int(speed_khz)
        if port_id is not None:
            info.portId = port_id
            info.bIsPortIdSet = 1

        return info

    def i2c_read(self, display_mask, i2c_dev_address, size, reg_address=None,
                 is_ddc_port=True, speed_khz=NVAPI_I2C_SPEED_DEFAULT, port_id=None):
        info = self._i2c_info(display_mask, i2c_dev_address, reg_address, is_ddc_port, speed_khz, port_id)
        dataBuf = (NvU8 * size)()
        info.pbData = ctypes.cast(dataBuf, POINTER(NvU8))
        info.cbSize = size

        nvStatus = NvAPI_I2CRead(self._hPhysicalGpu, ctypes.byref(info))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_I2CRead returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return bytes(dataBuf)

    def i2c_write(self, display_mask, i2c_dev_address, data, reg_address=None,
                  is_ddc_port=True, speed_khz=NVAPI_I2C_SPEED_DEFAULT, port_id=None):
        info = self._i2c_info(display_mask, i2c_dev_address, reg_address, is_ddc_port, speed_khz, port_id)
        data = bytearray(data)
        dataArray = (NvU8 * len(data))(*data)
        info.pbData = ctypes.cast(dataArray, POINTER(NvU8))
        info.cbSize = len(data)

        nvStatus = NvAPI_I2CWrite(self._hPhysicalGpu, ctypes.byref(info))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_I2CWrite returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    def workstation_feature_setup(self, enable_mask, disable_mask):
        nvStatus = NvAPI_GPU_WorkstationFeatureSetup(self._hPhysicalGpu, NvU32(enable_mask), NvU32(disable_mask))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_WorkstationFeatureSetup returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def workstation_feature_query(self):
        pConfigured = NvU32()
        pConsistent = NvU32()
        nvStatus = NvAPI_GPU_WorkstationFeatureQuery(self._hPhysicalGpu, ctypes.byref(pConfigured), ctypes.byref(pConsistent))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_WorkstationFeatureQuery returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return WorkstationFeatureQuery(
            configured=NVAPI_GPU_WORKSTATION_FEATURE_MASK.decode_flags(pConfigured.value),
            consistent=NVAPI_GPU_WORKSTATION_FEATURE_MASK.decode_flags(pConsistent.value),
        )

    def query_workstation_feature_support(self, feature):
        nvStatus = NvAPI_GPU_QueryWorkstationFeatureSupport(self._hPhysicalGpu, NV_GPU_WORKSTATION_FEATURE_TYPE(int(feature)))
        if nvStatus == NvAPI_Status.NVAPI_NOT_SUPPORTED:
            return False
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_QueryWorkstationFeatureSupport returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return True

    @property
    def ecc_status_info(self):
        p = NV_GPU_ECC_STATUS_INFO()
        p.version = NV_GPU_ECC_STATUS_INFO_VER
        nvStatus = NvAPI_GPU_GetECCStatusInfo(self._hPhysicalGpu, ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetECCStatusInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return EccStatusInfo(bool(p.isSupported), NV_ECC_CONFIGURATION.get(p.configurationOptions), bool(p.isEnabled))

    @property
    def ecc_error_info(self):
        p = NV_GPU_ECC_ERROR_INFO()
        p.version = NV_GPU_ECC_ERROR_INFO_VER
        nvStatus = NvAPI_GPU_GetECCErrorInfo(self._hPhysicalGpu, ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetECCErrorInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return EccErrorInfo(
            EccErrorCounts(p.current.singleBitErrors, p.current.doubleBitErrors),
            EccErrorCounts(p.aggregate.singleBitErrors, p.aggregate.doubleBitErrors),
        )

    def reset_ecc_error_info(self, reset_current=True, reset_aggregate=True):
        nvStatus = NvAPI_GPU_ResetECCErrorInfo(self._hPhysicalGpu, NvU8(1 if reset_current else 0), NvU8(1 if reset_aggregate else 0))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_ResetECCErrorInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def ecc_configuration_info(self):
        p = NV_GPU_ECC_CONFIGURATION_INFO()
        p.version = NV_GPU_ECC_CONFIGURATION_INFO_VER
        nvStatus = NvAPI_GPU_GetECCConfigurationInfo(self._hPhysicalGpu, ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetECCConfigurationInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return EccConfigurationInfo(bool(p.isEnabled), bool(p.isEnabledByDefault))

    @ecc_configuration_info.setter
    def ecc_configuration_info(self, value):
        # value: (enable, enable_immediately) tuple.
        enable, enable_immediately = value
        nvStatus = NvAPI_GPU_SetECCConfiguration(self._hPhysicalGpu, NvU8(1 if enable else 0), NvU8(1 if enable_immediately else 0))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_SetECCConfiguration returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def perf_decrease_info(self):
        pPerfDecrInfo = NvU32()
        nvStatus = NvAPI_GPU_GetPerfDecreaseInfo(self._hPhysicalGpu, ctypes.byref(pPerfDecrInfo))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetPerfDecreaseInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pPerfDecrInfo.value

    @property
    def performance_monitor(self):
        pPerfPstatesInfo = NV_GPU_PERF_PSTATES_INFO()
        pPerfPstatesInfo.version = NV_GPU_PERF_PSTATES_INFO_VER
        inputFlags = NvU32()
        nvStatus = NvAPI_GPU_GetPstatesInfoEx(self._hPhysicalGpu,  ctypes.byref(pPerfPstatesInfo),  inputFlags)
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetPstatesInfoEx returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        pPstatesInfo = NV_GPU_PERF_PSTATES20_INFO()
        pPstatesInfo.version = NV_GPU_PERF_PSTATES20_INFO_VER
        nvStatus = NvAPI_GPU_GetPstates20(self._hPhysicalGpu, ctypes.byref(pPstatesInfo))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetPstates20 returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        res = {}

        if _get_bit(pPerfPstatesInfo.flags, 0):

            for i in range(pPerfPstatesInfo.numPstates):
                pstate = pPerfPstatesInfo.pstates[i]
                state_info = pPstatesInfo.pstates[i]

                ps = {'clocks': [], 'voltages': []}
                res[pstate.pstateId] = ps

                if _get_bit(pstate.flags, 0):
                    ps['pcie_limit'] = 'GEN2'
                else:
                    ps['pcie_limit'] = 'GEN1'

                for j in range(pPerfPstatesInfo.numClocks):
                    clock = pstate.clocks[j]
                    state_info_clock = state_info.clocks[j]
                    type_id = NV_GPU_PERF_PSTATE20_CLOCK_TYPE_ID.get(clock.typeId)

                    data = {
                        'type': NV_GPU_PUBLIC_CLOCK_ID.get(clock.domainId),
                        'info_type': type_id,
                        'freq_delta_khz': state_info_clock.freqDelta_kHz.value,
                        'freq_delta_maximum_khz': state_info_clock.freqDelta_kHz.valueRange.max,
                        'freq_delta_minimum_khz': state_info_clock.freqDelta_kHz.valueRange.min,
                        'can_overclock': _get_bit(clock.flags, 0),
                        'freq_khz': clock.freq
                    }

                    if type_id == 'Single':
                        data['freq_khz'] = state_info_clock.data.single.freq_kHz
                    else:
                        data['minimum_freq_khz'] = state_info_clock.data.range.minFreq_kHz
                        data['maximum_freq_khz'] = state_info_clock.data.range.maxFreq_kHz
                        data['minimum_voltage'] = state_info_clock.data.range.minVoltage_uV
                        data['maximum_voltage'] = state_info_clock.data.range.maxVoltage_uV

                    ps['clocks'] += [data]

                for j in range(pPerfPstatesInfo.numVoltages):
                    voltage = pstate.voltages[j]
                    base_voltage = state_info.baseVoltages[j]

                    ps['voltages'] += [
                        {
                            'type': NV_GPU_PERF_VOLTAGE_INFO_DOMAIN_ID.get(voltage.domainId),
                            'mvolt': voltage.mvolt,
                            'volt': base_voltage.volt_uV,
                            'volt_delta': base_voltage.voltDelta_uV.value,
                            'volt_delta_maximum': base_voltage.voltDelta_uV.valueRange.max,
                            'volt_delta_minimum': base_voltage.voltDelta_uV.valueRange.min
                        }
                    ]

            pDynamicPstatesInfoEx = NV_GPU_DYNAMIC_PSTATES_INFO_EX()
            NvAPI_GPU_GetDynamicPstatesInfoEx(self._hPhysicalGpu,  ctypes.byref(pDynamicPstatesInfoEx))
            res['utilization'] = []
            if _get_bit(pDynamicPstatesInfoEx.flags, 0):
                for i in range(NVAPI_MAX_GPU_UTILIZATIONS):
                    util = pDynamicPstatesInfoEx.utilization[i]
                    if util.bIsPresent:
                        res['utilization'] += [util.percentage]
                    else:
                        res['utilization'] += [None]

        # TODO: pPstatesInfo.ov

        return res

    @property
    def current_pstate(self):
        pCurrentPstate = NV_GPU_PERF_PSTATE_ID()
        nvStatus = NvAPI_GPU_GetCurrentPstate(self._hPhysicalGpu, ctypes.byref(pCurrentPstate))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetCurrentPstate returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return NV_GPU_PERF_PSTATE_ID.get(pCurrentPstate)

    @property
    def thermal_sensors(self):
        sensorIndex = NvU32(NVAPI_THERMAL_TARGET_ALL)
        pThermalSettings = NV_GPU_THERMAL_SETTINGS()
        pThermalSettings.version = NV_GPU_THERMAL_SETTINGS_VER
        nvStatus = NvAPI_GPU_GetThermalSettings(self._hPhysicalGpu, sensorIndex,  ctypes.byref(pThermalSettings))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetThermalSettings returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        res = []

        for i in range(pThermalSettings.count):
            sensr = pThermalSettings.sensor[i]
            res.append(ThermalSensorInfo(
                controller=NV_THERMAL_CONTROLLER.get(sensr.controller),
                default_minimum_temp=sensr.defaultMinTemp,
                default_maximum_temp=sensr.defaultMaxTemp,
                current_temp=sensr.currentTemp,
                target=NV_THERMAL_TARGET.get(sensr.target),
            ))

        return res

    @property
    def clock_frequencies(self):
        # ClockType is an INPUT selector on the outer struct (one query
        # per call picks Current/Base/Boost) -- it is not a per-domain
        # output field, so getting all three means three separate calls,
        # not reading pClkFreqs.domain[i].ClockType (which doesn't exist;
        # only bIsPresent/frequency are on the per-domain struct).
        #
        # domain[i] is indexed by NV_GPU_PUBLIC_CLOCK_ID -- graphics=0,
        # memory=4, processor=7, video=8 are the only 4 of the 32 possible
        # slots the driver ever populates.
        res = {}
        for type_name, clock_type in (
            ('current', NV_GPU_CLOCK_FREQUENCIES_CURRENT_FREQ),
            ('base', NV_GPU_CLOCK_FREQUENCIES_BASE_CLOCK),
            ('boost', NV_GPU_CLOCK_FREQUENCIES_BOOST_CLOCK),
        ):
            pClkFreqs = NV_GPU_CLOCK_FREQUENCIES()
            # NV_GPU_CLOCK_FREQUENCIES aliases the V2 struct, but the
            # generic _VER constant encodes V3's size -- must use the
            # V2-specific version constant to match the struct actually
            # being allocated
            pClkFreqs.version = NV_GPU_CLOCK_FREQUENCIES_VER_2
            pClkFreqs.ClockType = clock_type

            nvStatus = NvAPI_GPU_GetAllClockFrequencies(self._hPhysicalGpu, ctypes.byref(pClkFreqs))
            if NvAPI_Status.NVAPI_OK != nvStatus:
                szDesc = NvAPI_ShortString()
                NvAPI_GetErrorMessage(nvStatus, szDesc)
                raise RuntimeError("NvAPI_GPU_GetAllClockFrequencies returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

            def domain_freq(clock_id):
                domain = pClkFreqs.domain[clock_id]
                return domain.frequency if domain.bIsPresent else None

            res[type_name] = ClockDomainFrequencies(
                graphics=domain_freq(NV_GPU_PUBLIC_CLOCK_ID.NVAPI_GPU_PUBLIC_CLOCK_GRAPHICS),
                memory=domain_freq(NV_GPU_PUBLIC_CLOCK_ID.NVAPI_GPU_PUBLIC_CLOCK_MEMORY),
                processor=domain_freq(NV_GPU_PUBLIC_CLOCK_ID.NVAPI_GPU_PUBLIC_CLOCK_PROCESSOR),
                video=domain_freq(NV_GPU_PUBLIC_CLOCK_ID.NVAPI_GPU_PUBLIC_CLOCK_VIDEO),
            )

        return ClockFrequencies(**res)

    def query_illumination_support(self, attribute):
        p = NV_GPU_QUERY_ILLUMINATION_SUPPORT_PARM()
        p.version = NV_GPU_QUERY_ILLUMINATION_SUPPORT_PARM_VER
        p.hPhysicalGpu = self._hPhysicalGpu
        p.Attribute = int(attribute)
        nvStatus = NvAPI_GPU_QueryIlluminationSupport(ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_QueryIlluminationSupport returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return bool(p.bSupported)

    def get_illumination(self, attribute):
        p = NV_GPU_GET_ILLUMINATION_PARM()
        p.version = NV_GPU_GET_ILLUMINATION_PARM_VER
        p.hPhysicalGpu = self._hPhysicalGpu
        p.Attribute = int(attribute)
        nvStatus = NvAPI_GPU_GetIllumination(ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetIllumination returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return p.Value

    def set_illumination(self, attribute, value):
        p = NV_GPU_SET_ILLUMINATION_PARM()
        p.version = NV_GPU_SET_ILLUMINATION_PARM_VER
        p.hPhysicalGpu = self._hPhysicalGpu
        p.Attribute = int(attribute)
        p.Value = value
        nvStatus = NvAPI_GPU_SetIllumination(ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_SetIllumination returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def client_illum_devices_info(self):
        p = NV_GPU_CLIENT_ILLUM_DEVICE_INFO_PARAMS()
        p.version = NV_GPU_CLIENT_ILLUM_DEVICE_INFO_PARAMS_VER
        nvStatus = NvAPI_GPU_ClientIllumDevicesGetInfo(self._hPhysicalGpu, ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_ClientIllumDevicesGetInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return [_illum_device_info_from_struct(p.devices[i]) for i in range(p.numIllumDevices)]

    @property
    def client_illum_devices_control(self):
        p = NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_PARAMS()
        p.version = NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_PARAMS_VER
        nvStatus = NvAPI_GPU_ClientIllumDevicesGetControl(self._hPhysicalGpu, ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_ClientIllumDevicesGetControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return [_illum_device_control_from_struct(p.devices[i]) for i in range(p.numIllumDevices)]

    @client_illum_devices_control.setter
    def client_illum_devices_control(self, value):
        devices = list(value)
        p = NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_PARAMS()
        p.version = NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_PARAMS_VER
        p.numIllumDevices = len(devices)
        for i, dc in enumerate(devices):
            _illum_device_control_to_struct(p.devices[i], dc)

        nvStatus = NvAPI_GPU_ClientIllumDevicesSetControl(self._hPhysicalGpu, ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_ClientIllumDevicesSetControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def client_illum_zones_info(self):
        p = NV_GPU_CLIENT_ILLUM_ZONE_INFO_PARAMS()
        p.version = NV_GPU_CLIENT_ILLUM_ZONE_INFO_PARAMS_VER
        nvStatus = NvAPI_GPU_ClientIllumZonesGetInfo(self._hPhysicalGpu, ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_ClientIllumZonesGetInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return [_illum_zone_info_from_struct(p.zones[i]) for i in range(p.numIllumZones)]

    def client_illum_zones_control(self, default=False):
        p = NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_PARAMS()
        p.version = NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_PARAMS_VER
        p.bDefault = 1 if default else 0
        nvStatus = NvAPI_GPU_ClientIllumZonesGetControl(self._hPhysicalGpu, ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_ClientIllumZonesGetControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return [_illum_zone_control_from_struct(p.zones[i]) for i in range(p.numIllumZonesControl)]

    def set_client_illum_zones_control(self, zones, default=False):
        zones = list(zones)
        p = NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_PARAMS()
        p.version = NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_PARAMS_VER
        p.bDefault = 1 if default else 0
        p.numIllumZonesControl = len(zones)
        for i, zc in enumerate(zones):
            _illum_zone_control_to_struct(p.zones[i], zc)

        nvStatus = NvAPI_GPU_ClientIllumZonesSetControl(self._hPhysicalGpu, ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_ClientIllumZonesSetControl returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    def __init__(self, logical_gpu, physical_gpu_index):
        self.logical_gpu = logical_gpu
        self.physical_gpu_index = physical_gpu_index

    @property
    def dedicated_memory(self):
        # Size(in kb) of the physical framebuffer.
        return self._memory_info.dedicatedVideoMemory

    @property
    def available_dedicated_memory(self):
        # Size(in kb) of the available physical framebuffer for allocating
        # video memory surfaces.
        return self._memory_info.availableDedicatedVideoMemory

    @property
    def system_memory(self):
        # Size(in kb) of system memory the driver allocates at load time.
        return self._memory_info.systemVideoMemory

    @property
    def shared_system_memory(self):
        # Size(in kb) of shared system memory that driver is allowed to
        # commit for surfaces across all allocations.
        return self._memory_info.sharedSystemMemory

    @property
    def current_available_dedicated_memory(self):
        # Size(in kb) of the current available physical framebuffer for
        # allocating video memory surfaces.
        return self._memory_info.curAvailableDedicatedVideoMemory

    @property
    def dedicated_memory_eviction_size(self):
        # Size(in kb) of the total size of memory released as a result of
        # the evictions.
        return self._memory_info.dedicatedVideoMemoryEvictionsSize

    @property
    def dedicated_memory_eviction_count(self):
        # Indicates the number of eviction events that caused an allocation
        # to be removed from dedicated video memory to free GPU
        #
        # NOTE: unlike every size field on this struct (which are exact
        # KB-vs-bytes conversions of their memory_info_ex counterpart --
        # e.g. dedicated_memory * 1024 == memory_info_ex.dedicated_video_memory),
        # this count and memory_info_ex.dedicated_video_memory_eviction_count
        # are NOT the same counter scaled differently. They come from separate,
        # unsynchronized internal counters maintained by this deprecated call
        # (NvAPI_GPU_GetMemoryInfo, deprecated since driver release 520) versus
        # the modern NvAPI_GPU_GetMemoryInfoEx, and were observed to disagree
        # substantially (e.g. 2 vs 2373) on real hardware. This is a genuine
        # driver-side discrepancy between the two code paths, not a decode bug
        # here -- every other field on this struct was individually verified
        # against memory_info_ex's equivalent and matched exactly.
        return self._memory_info.dedicatedVideoMemoryEvictionCount

    @property
    def physical_gpu_id(self):
        pGpuId = NvU32()
        nvStatus = NvAPI_GetGPUIDfromPhysicalGPU(self._hPhysicalGpu, ctypes.byref(pGpuId))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GetGPUIDfromPhysicalGPU returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pGpuId.value

    @property
    def ram_bus_width(self):
        pBusWidth = NvU32()
        nvStatus = NvAPI_GPU_GetRamBusWidth(self._hPhysicalGpu, ctypes.byref(pBusWidth))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetRamBusWidth returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pBusWidth.value

    @property
    def architecture_info(self):
        pArchInfo = NV_GPU_ARCH_INFO()
        pArchInfo.version = NV_GPU_ARCH_INFO_VER
        nvStatus = NvAPI_GPU_GetArchInfo(self._hPhysicalGpu, ctypes.byref(pArchInfo))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetArchInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        architecture = NV_GPU_ARCHITECTURE_ID.get(pArchInfo.architecture)
        impl_name = get_arch_implementation_name(pArchInfo.architecture, pArchInfo.implementation)
        implementation = (
            EnumItem(pArchInfo.implementation).set_string(impl_name)
            if impl_name is not None else pArchInfo.implementation
        )

        return ArchitectureInfo(
            architecture=architecture if architecture is not None else pArchInfo.architecture,
            implementation=implementation,
            revision=NV_GPU_CHIP_REVISION.get(pArchInfo.revision),
        )

    @property
    def uuid(self):
        # requires driver release 595+
        pGpuUuid = NV_GPU_UUID()
        pGpuUuid.version = NV_GPU_UUID_VER
        nvStatus = NvAPI_GPU_GetUUID(self._hPhysicalGpu, ctypes.byref(pGpuUuid))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetUUID returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return bytes(pGpuUuid.uuid).hex()

    @property
    def virtualization_mode(self):
        pVirtualizationInfo = NV_GPU_VIRTUALIZATION_INFO()
        pVirtualizationInfo.version = NV_GPU_VIRTUALIZATION_INFO_VER
        nvStatus = NvAPI_GPU_GetVirtualizationInfo(self._hPhysicalGpu, ctypes.byref(pVirtualizationInfo))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetVirtualizationInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return NV_VIRTUALIZATION_MODE.get(pVirtualizationInfo.virtualizationMode)

    @property
    def licensable_features(self):
        pLicensableFeatures = NV_LICENSABLE_FEATURES()
        pLicensableFeatures.version = NV_LICENSABLE_FEATURES_VER
        nvStatus = NvAPI_GPU_GetLicensableFeatures(self._hPhysicalGpu, ctypes.byref(pLicensableFeatures))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetLicensableFeatures returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        features = []
        for i in range(pLicensableFeatures.licensableFeatureCount):
            detail = pLicensableFeatures.licenseDetails[i]
            features += [LicenseFeatureDetail(
                is_enabled=bool(detail.flags & 1),
                is_feature_enabled=bool(detail.flags & 2),
                feature_code=NV_LICENSE_FEATURE_TYPE.get(detail.featureCode),
                product_name=detail.productName.decode('ascii', 'replace').rstrip('\x00'),
            )]

        return LicensableFeatures(
            is_license_supported=bool(pLicensableFeatures.flags & 1),
            features=features,
        )

    @property
    def gpu_info(self):
        pGpuInfo = NV_GPU_INFO()
        pGpuInfo.version = NV_GPU_INFO_VER
        nvStatus = NvAPI_GPU_GetGPUInfo(self._hPhysicalGpu, ctypes.byref(pGpuInfo))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetGPUInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return GPUInfo(
            is_external_gpu=bool(pGpuInfo.flags & 1),
            ray_tracing_cores=pGpuInfo.rayTracingCores,
            tensor_cores=pGpuInfo.tensorCores,
        )

    @property
    def is_vr_ready(self):
        pGpuVrReadyData = NV_GPU_VR_READY()
        pGpuVrReadyData.version = NV_GPU_VR_READY_VER
        nvStatus = NvAPI_GPU_GetVRReadyData(self._hPhysicalGpu, ctypes.byref(pGpuVrReadyData))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetVRReadyData returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return bool(pGpuVrReadyData.flags & 1)

    @property
    def gsp_firmware_version(self):
        pGspInfo = NV_GPU_GSP_INFO()
        pGspInfo.version = NV_GPU_GSP_INFO_VER
        nvStatus = NvAPI_GPU_GetGspFeatures(self._hPhysicalGpu, ctypes.byref(pGspInfo))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetGspFeatures returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return bytes(pGspInfo.firmwareVersion).split(b'\x00')[0].decode('ascii', 'replace')

    @property
    def is_overclocking_detected(self):
        # requires a recent driver
        pOverclockStatus = NV_GPU_OVERCLOCK_STATUS()
        pOverclockStatus.version = NV_GPU_OVERCLOCK_STATUS_VER
        nvStatus = NvAPI_GPU_GetOverclockStatus(self._hPhysicalGpu, ctypes.byref(pOverclockStatus))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetOverclockStatus returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return bool(pOverclockStatus.flags & 1)

    @property
    def memory_info_ex(self):
        # modern replacement for _memory_info (NvAPI_GPU_GetMemoryInfo has
        # been deprecated since driver release 520); units are bytes here,
        # not KB, and it adds promotion accounting the older call doesn't
        # have. Every size field here was individually verified to equal
        # its dedicated_memory*/etc. counterpart on PhysicalGPU multiplied
        # by exactly 1024 (KB -> bytes) -- except
        # dedicated_video_memory_eviction_count, which is backed by a
        # separate, unsynchronized counter from the deprecated call's
        # dedicated_memory_eviction_count and can disagree substantially
        # (observed 2373 vs 2 on real hardware); see the note on
        # PhysicalGPU.dedicated_memory_eviction_count.
        pMemoryInfo = NV_GPU_MEMORY_INFO_EX()
        pMemoryInfo.version = NV_GPU_MEMORY_INFO_EX_VER
        nvStatus = NvAPI_GPU_GetMemoryInfoEx(self._hPhysicalGpu, ctypes.byref(pMemoryInfo))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetMemoryInfoEx returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return MemoryInfoEx(
            dedicated_video_memory=pMemoryInfo.dedicatedVideoMemory,
            available_dedicated_video_memory=pMemoryInfo.availableDedicatedVideoMemory,
            system_video_memory=pMemoryInfo.systemVideoMemory,
            shared_system_memory=pMemoryInfo.sharedSystemMemory,
            current_available_dedicated_video_memory=pMemoryInfo.curAvailableDedicatedVideoMemory,
            dedicated_video_memory_evictions_size=pMemoryInfo.dedicatedVideoMemoryEvictionsSize,
            dedicated_video_memory_eviction_count=pMemoryInfo.dedicatedVideoMemoryEvictionCount,
            dedicated_video_memory_promotions_size=pMemoryInfo.dedicatedVideoMemoryPromotionsSize,
            dedicated_video_memory_promotion_count=pMemoryInfo.dedicatedVideoMemoryPromotionCount,
        )

    @property
    def adapter_luid(self):
        pOSAdapterId = NvLUID()
        nvStatus = NvAPI_GPU_GetAdapterIdFromPhysicalGpu(self._hPhysicalGpu, ctypes.byref(pOSAdapterId))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetAdapterIdFromPhysicalGpu returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return '%08x-%04x-%04x-%s' % (
            pOSAdapterId.data1, pOSAdapterId.data2, pOSAdapterId.data3,
            bytes(pOSAdapterId.data4[:]).hex()
        )

    @property
    def nvlink_caps(self):
        # linkMask == 0 means no active NVLink connections -- normal for
        # a single card with no NVLink bridge, even when capsTbl shows
        # the silicon itself is NVLink-capable
        pCaps = NVLINK_GET_CAPS()
        pCaps.version = NVLINK_GET_CAPS_VER
        nvStatus = NvAPI_GPU_NVLINK_GetCaps(self._hPhysicalGpu, ctypes.byref(pCaps))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_NVLINK_GetCaps returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return NVLinkCaps(
            caps_table=NVAPI_NVLINK_CAPS.decode_flags(pCaps.capsTbl),
            lowest_nvlink_version=NVAPI_NVLINK_VERSION.get(pCaps.lowestNvlinkVersion),
            highest_nvlink_version=NVAPI_NVLINK_VERSION.get(pCaps.highestNvlinkVersion),
            lowest_nci_version=NVAPI_NVLINK_VERSION.get(pCaps.lowestNciVersion),
            highest_nci_version=NVAPI_NVLINK_VERSION.get(pCaps.highestNciVersion),
            link_mask=[i for i in range(NVAPI_NVLINK_MAX_LINKS) if pCaps.linkMask & (1 << i)],
        )

    @property
    def nvlink_status(self):
        pStatus = NVLINK_GET_STATUS()
        pStatus.version = NVLINK_GET_STATUS_VER
        nvStatus = NvAPI_GPU_NVLINK_GetStatus(self._hPhysicalGpu, ctypes.byref(pStatus))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_NVLINK_GetStatus returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        links = []
        for i in range(NVAPI_NVLINK_MAX_LINKS):
            if not (pStatus.linkMask & (1 << i)):
                continue
            info = pStatus.linkInfo[i]
            links += [NVLinkLinkStatus(
                link_index=i,
                is_connected=bool(info.flags & 1),
                link_state=info.linkState,
                sublink_width=info.subLinkWidth,
                nvlink_version=NVAPI_NVLINK_VERSION.get(info.nvlinkVersion),
                nci_version=NVAPI_NVLINK_VERSION.get(info.nciVersion),
                nvlink_common_clock_speed_mhz=info.nvlinkCommonClockSpeedMhz,
                nvlink_link_clock_mhz=info.nvlinkLinkClockMhz,
                remote_device_uuid=bytes(info.remoteDeviceInfo.deviceUUID).hex(),
            )]

        return NVLinkStatus(
            link_mask=[i for i in range(NVAPI_NVLINK_MAX_LINKS) if pStatus.linkMask & (1 << i)],
            links=links,
        )

    @property
    def encoder_statistics(self):
        pEncoderStatistics = NV_ENCODER_STATISTICS()
        pEncoderStatistics.version = NV_ENCODER_STATISTICS_VER
        nvStatus = NvAPI_GPU_GetEncoderStatistics(self._hPhysicalGpu, ctypes.byref(pEncoderStatistics))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetEncoderStatistics returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return EncoderStatistics(
            sessions_count=pEncoderStatistics.sessionsCount,
            average_fps=pEncoderStatistics.averageFps,
            average_latency=pEncoderStatistics.averageLatency,
        )

    @property
    def encoder_sessions(self):
        # caller-allocated array, per the header's own doc comment
        buf = (NV_ENCODER_PER_SESSION_INFO_V1 * NV_ENCODER_SESSION_INFO_MAX_ENTRIES_V1)()
        pSessionsInfo = NV_ENCODER_SESSIONS_INFO()
        pSessionsInfo.version = NV_ENCODER_SESSIONS_INFO_VER
        pSessionsInfo.pSessionInfo = ctypes.cast(buf, ctypes.POINTER(NV_ENCODER_PER_SESSION_INFO_V1))

        nvStatus = NvAPI_GPU_GetEncoderSessionsInfo(self._hPhysicalGpu, ctypes.byref(pSessionsInfo))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetEncoderSessionsInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        sessions = []
        for i in range(pSessionsInfo.sessionsCount):
            info = buf[i]
            sessions += [EncoderSessionInfo(
                session_id=info.sessionId,
                process_id=info.processId,
                vgpu_instance=info.vgpuInstance,
                codec_type=NV_ENCODER_TYPE.get(info.codecType),
                h_resolution=info.hResolution,
                v_resolution=info.vResolution,
                average_encode_fps=info.averageEncodeFps,
                average_encode_latency=info.averageEncodeLatency,
            )]

        return sessions

    @property
    def is_cuda_compute_capable(self):
        # NvAPI_GPU_CudaEnumComputeCapableGpus itself is deprecated (since
        # driver release 319) but its interface ID is still in NVIDIA's
        # current published ID table, and it's the only NVAPI-level check
        # for this; superseded in NVIDIA's own recommendation by CUDA's
        # own runtime API, not by anything else in NVAPI itself.
        #
        # NOTE: verified live that this driver's implementation of this
        # deprecated call reports gpuCount correctly but does NOT populate
        # the per-entry hPhysicalGpu handles (they come back NULL) -- so
        # this can only answer "is at least one GPU in the system compute
        # capable", not "is *this* GPU specifically" on multi-GPU systems.
        buf = (NV_COMPUTE_GPU * NVAPI_MAX_GPU_PER_TOPOLOGY)()
        pComputeTopo = NV_COMPUTE_GPU_TOPOLOGY()
        pComputeTopo.version = NV_COMPUTE_GPU_TOPOLOGY_VER
        pComputeTopo.computeGpus = buf
        nvStatus = NvAPI_GPU_CudaEnumComputeCapableGpus(ctypes.byref(pComputeTopo))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_CudaEnumComputeCapableGpus returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pComputeTopo.gpuCount > 0

    @property
    def _hPhysicalGpu(self):
        return self.logical_gpu._logical_gpu_info.physicalGpuHandles[self.physical_gpu_index]

    @property
    def _memory_info(self):
        hPhysicalGpu = self._hPhysicalGpu
        pMemoryInfo = NV_DISPLAY_DRIVER_MEMORY_INFO()
        pMemoryInfo.version = NV_DISPLAY_DRIVER_MEMORY_INFO_VER

        nvStatus = NvAPI_GPU_GetMemoryInfo(hPhysicalGpu, ctypes.byref(pMemoryInfo))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetMemoryInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pMemoryInfo

    def _all_display_ids(self):
        # every displayId NVAPI has ever seen on this physical GPU --
        # currently connected or historical -- used by Port.__iter__ to
        # find EDID matches for a given output.
        displayIdCount = NvU32(16)
        displayIdArray = (NV_GPU_DISPLAYIDS * 16)()
        displayIdArray[0].version = NV_GPU_DISPLAYIDS_VER

        nvStatus = NvAPI_GPU_GetAllDisplayIds(self._hPhysicalGpu, displayIdArray, ctypes.byref(displayIdCount))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetAllDisplayIds returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        for i in range(displayIdCount.value):
            yield displayIdArray[i].displayId


def _iter_set_bits(mask, width=32):
    for i in range(width):
        bit = 1 << i
        if mask & bit:
            yield bit


class Port(object):
    # A physical connector on a PhysicalGPU, identified by NvAPI_GPU_
    # GetConnectorInfo's connectorIndex -- reverse-engineered (see
    # nvapi_gpu_info_ext_h.NV_GPU_CONNECTOR_INFO for how/why) since neither
    # it nor GetConnectorInfoEx -- the APIs NVIDIA's own header comments
    # point to for real connector identity -- are declared in any published
    # NVAPI header, past or current, or implemented by any community port
    # checked (nvapi-rs, NvAPIWrapper, the Pascal/FPC port).
    #
    # output_ids holds every legacy output-bitmask bit sharing this
    # connectorIndex -- on real hardware a single physical jack can claim
    # more than one bit (observed: 2 per DisplayPort connector on a Quadro
    # RTX 4000), so a Port is a connectorIndex plus the set of bits that
    # collapse to it, not a single bit.
    def __init__(self, physical_gpu, connector_index, output_ids):
        self.physical_gpu = physical_gpu
        self.connector_index = connector_index
        self.output_ids = tuple(output_ids)

    def _active_output_id(self):
        # prefer whichever bit is actually carrying a connection; fall
        # back to the first bit for a port with nothing plugged in
        for output_id in self.output_ids:
            if self.physical_gpu.connected_outputs & output_id:
                return output_id

        return self.output_ids[0]

    def _married_display_id(self):
        # NvAPI_GetDisplayPortInfo/SetDisplayPort/GetHDMISupportInfo's own
        # doc comment says outputId accepts either the legacy bitmask or a
        # displayId -- but live testing showed that's only true for a
        # displayId; passing the raw legacy bit here fails with
        # NVAPI_EXPECTED_DISPLAY_HANDLE. So these need the married
        # display's displayId, not self._active_output_id().
        for display in self:
            return display.display_id

        raise RuntimeError("Port has no married display to query link info for (nothing connected)")

    @property
    def connector_type(self):
        return self.physical_gpu.connector_info(self._active_output_id()).connector_type

    @property
    def output_type(self):
        return self.physical_gpu.output_type(self._active_output_id())

    @property
    def is_connected(self):
        return any(self.physical_gpu.connected_outputs & output_id for output_id in self.output_ids)

    @property
    def is_active(self):
        return any(self.physical_gpu.active_outputs & output_id for output_id in self.output_ids)

    @property
    def display_port_info(self):
        pInfo = NV_DISPLAY_PORT_INFO()
        pInfo.version = NV_DISPLAY_PORT_INFO_VER
        nvStatus = NvAPI_GetDisplayPortInfo(NvDisplayHandle(), self._married_display_id(), ctypes.byref(pInfo))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GetDisplayPortInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return DisplayPortInfo(
            pInfo.dpcd_ver, NV_DP_LINK_RATE.get(pInfo.maxLinkRate), NV_DP_LANE_COUNT.get(pInfo.maxLaneCount),
            NV_DP_LINK_RATE.get(pInfo.curLinkRate), NV_DP_LANE_COUNT.get(pInfo.curLaneCount),
            NV_DP_COLOR_FORMAT.get(pInfo.colorFormat), NV_DP_DYNAMIC_RANGE.get(pInfo.dynamicRange),
            NV_DP_COLORIMETRY.get(pInfo.colorimetry), NV_DP_BPC.get(pInfo.bpc),
            bool(pInfo.isDp), bool(pInfo.isInternalDp), bool(pInfo.isColorCtrlSupported),
        )

    @display_port_info.setter
    def display_port_info(self, value):
        # value: (link_rate, lane_count, color_format, dynamic_range, colorimetry, bpc) tuple.
        link_rate, lane_count, color_format, dynamic_range, colorimetry, bpc = value
        pCfg = NV_DISPLAY_PORT_CONFIG()
        pCfg.version = NV_DISPLAY_PORT_CONFIG_VER
        pCfg.linkRate = int(link_rate)
        pCfg.laneCount = int(lane_count)
        pCfg.colorFormat = int(color_format)
        pCfg.dynamicRange = int(dynamic_range)
        pCfg.colorimetry = int(colorimetry)
        pCfg.bpc = int(bpc)
        nvStatus = NvAPI_SetDisplayPort(NvDisplayHandle(), self._married_display_id(), ctypes.byref(pCfg))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_SetDisplayPort returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def hdmi_support_info(self):
        pInfo = NV_HDMI_SUPPORT_INFO()
        pInfo.version = NV_HDMI_SUPPORT_INFO_VER
        nvStatus = NvAPI_GetHDMISupportInfo(NvDisplayHandle(), self._married_display_id(), ctypes.byref(pInfo))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GetHDMISupportInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return HdmiSupportInfo(
            bool(pInfo.isGpuHDMICapable), bool(pInfo.isMonUnderscanCapable), bool(pInfo.isMonBasicAudioCapable),
            bool(pInfo.isMonYCbCr444Capable), bool(pInfo.isMonYCbCr422Capable), bool(pInfo.isMonxvYCC601Capable),
            bool(pInfo.isMonxvYCC709Capable), bool(pInfo.isMonHDMI), pInfo.EDID861ExtRev,
        )

    def __iter__(self):
        # Correlates displays to this port by reading the EDID off the
        # port's active (or first) legacy output bit (NvAPI_GPU_GetEDID)
        # and matching it byte-for-byte against each display's modern EDID
        # (Display.edid_data) -- a driver-verified match, not an assumption
        # about displayId/output-bit encoding. If nothing is plugged into
        # this port (or its EDID isn't readable), this yields nothing --
        # there is no way to determine a "married" display for a port with
        # no signal, since there's nothing to read.
        #
        # NOTE on splitters/MST: NvAPI_GPU_GetEDID is a pre-MST API tied to
        # a single legacy output bit. Whether it returns each downstream
        # monitor's own EDID or just one (e.g. the hub's) on a true MST/
        # splitter topology is unverified -- untested against real MST
        # hardware. For a simple point-to-point connection (the common
        # case) this is exact.
        try:
            port_edid = self.physical_gpu.get_edid(self._active_output_id()).data
        except RuntimeError:
            return

        port_edid_base = port_edid[:128]
        if len(port_edid_base) < 128:
            return

        for display_id in self.physical_gpu._all_display_ids():
            display = Display(self.physical_gpu.logical_gpu, display_id)
            try:
                display_edid = display.edid_data
            except RuntimeError:
                continue

            if display_edid[:128] == port_edid_base:
                yield display


class LogicalGPU(object):

    @property
    def _pLogicalGPU(self):
        thisEnum = NvU32(self.gpu_index)
        hNvDisplay = NvDisplayHandle()
        nvStatus = NvAPI_EnumNvidiaDisplayHandle(thisEnum, ctypes.byref(hNvDisplay))

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_EnumNvidiaDisplayHandle returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        pLogicalGPU = NvLogicalGpuHandle()

        nvStatus = NvAPI_GetLogicalGPUFromDisplay(
            hNvDisplay,
            ctypes.byref(pLogicalGPU)
        )

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GetLogicalGPUFromDisplay returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return pLogicalGPU

    def __len__(self):
        return

    @property
    def physical_gpus(self):
        for i in range(self._logical_gpu_info.physicalGpuCount):
            yield PhysicalGPU(self, i)

    @property
    def _logical_gpu_info(self):
        pLogicalGpuData = NV_LOGICAL_GPU_DATA()
        pLogicalGpuData.version = NV_LOGICAL_GPU_DATA_VER

        # per the struct's own doc comment: "[out] Returns OS-AdapterId.
        # User must send memory buffer of size atleast equal to the size
        # of LUID structure before calling the NVAPI." -- pOSAdapterId is
        # a bare void* with nothing behind it otherwise, so the driver
        # faults writing into it (NVAPI_INVALID_POINTER). NvLUID is kept
        # alive on the returned struct itself so it isn't collected while
        # pOSAdapterId still points at it.
        luid_buffer = NvLUID()
        pLogicalGpuData.pOSAdapterId = ctypes.cast(ctypes.byref(luid_buffer), POINTER(VOID))

        nvStatus = NvAPI_GPU_GetLogicalGpuInfo(
            self._pLogicalGPU,
            ctypes.byref(pLogicalGpuData)
        )

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetLogicalGpuInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        pLogicalGpuData._luid_buffer = luid_buffer
        return pLogicalGpuData

    @property
    def os_adpater_id(self):
        return ctypes.cast(self._logical_gpu_info.pOSAdapterId, ctypes.c_void_p).value

    # NvAPI_Stereo_CreateHandleFromIUnknown(IUnknown *pDevice, StereoHandle *pStereoHandle);
    # NvAPI_Stereo_DestroyHandle(StereoHandle stereoHandle);
    # NvAPI_Stereo_Activate(StereoHandle stereoHandle);
    # NvAPI_Stereo_Deactivate(StereoHandle stereoHandle);
    # NvAPI_Stereo_IsActivated(StereoHandle stereoHandle, NvU8 *pIsStereoOn);
    # NvAPI_Stereo_GetSeparation(StereoHandle stereoHandle, float *pSeparationPercentage);
    # NvAPI_Stereo_SetSeparation(StereoHandle stereoHandle, float newSeparationPercentage);
    # NvAPI_Stereo_GetConvergence(StereoHandle stereoHandle, float *pConvergence);
    # NvAPI_Stereo_SetConvergence(StereoHandle stereoHandle, float newConvergence);
    # NvAPI_Stereo_SetActiveEye(StereoHandle hStereoHandle, NV_STEREO_ACTIVE_EYE StereoEye);
    # NvAPI_Stereo_GetEyeSeparation(StereoHandle hStereoHandle,  float *pSeparation );
    # NvAPI_Stereo_GetSurfaceCreationMode(__in StereoHandle hStereoHandle,__in NVAPI_STEREO_SURFACECREATEMODE* pCreationMode);
    # NvAPI_Stereo_Debug_WasLastDrawStereoized(__in StereoHandle hStereoHandle, __out NvU8 *pWasStereoized);

    def __init__(self, gpu_index):
        self.gpu_index = gpu_index

    def __iter__(self):
        # yields Port, not Display -- iterate a Port to get the display(s)
        # (zero, one, or more with a splitter) actually attached to it.
        # Multiple legacy output-mask bits can share one physical
        # connector (observed: 2 per DisplayPort jack on a Quadro RTX
        # 4000), so bits are grouped by their real connectorIndex
        # (NvAPI_GPU_GetConnectorInfo) rather than yielding one Port per bit.
        for physical_gpu in self.physical_gpus:
            groups = {}
            for output_id in _iter_set_bits(physical_gpu.all_outputs):
                index = physical_gpu.connector_info(output_id).connector_index
                groups.setdefault(index, []).append(output_id)

            for index in sorted(groups):
                yield Port(physical_gpu, index, groups[index])


class Singleton(type):
    
    def __init__(cls, name, bases, dct):
        super(Singleton, cls).__init__(name, bases, dct)
        
        cls._instance = None
    
    def __call__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__()
            
        return cls._instance
    

@six.add_metaclass(Singleton)
class GPUs(object):
    @property
    def interface_version(self):
        szDesc = NvAPI_ShortString()
        nvStatus = NvAPI_GetInterfaceVersionString(szDesc)
        if NvAPI_Status.NVAPI_OK != nvStatus:
            raise RuntimeError("NvAPI_GetInterfaceVersionString returned error code %d" % (nvStatus,))

        return szDesc.value.decode('ascii', 'replace')

    @property
    def chipset_info(self):
        p = NV_CHIPSET_INFO()
        p.version = NV_CHIPSET_INFO_VER
        nvStatus = NvAPI_SYS_GetChipSetInfo(ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_SYS_GetChipSetInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return ChipsetInfo(
            p.vendorId, p.deviceId, p.szVendorName.decode('ascii', 'replace'),
            p.szChipsetName.decode('ascii', 'replace'), p.flags,
            p.subSysVendorId, p.subSysDeviceId, p.szSubSysVendorName.decode('ascii', 'replace'),
            p.HBvendorId, p.HBdeviceId, _pci_vendor_name(p.HBvendorId),
            p.HBsubSysVendorId, p.HBsubSysDeviceId, _pci_vendor_name(p.HBsubSysVendorId),
        )

    @property
    def lid_and_dock_info(self):
        p = NV_LID_DOCK_PARAMS()
        p.version = NV_LID_DOCK_PARAMS_VER
        nvStatus = NvAPI_SYS_GetLidAndDockInfo(ctypes.byref(p))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_SYS_GetLidAndDockInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return LidDockInfo(
            p.currentLidState, p.currentDockState, p.currentLidPolicy, p.currentDockPolicy,
            bool(p.forcedLidMechanismPresent), bool(p.forcedDockMechanismPresent),
        )

    # NvAPI_GPU_{Query,Get,Set}Illumination are wired on PhysicalGPU
    # (query_illumination_support/get_illumination/set_illumination) --
    # hPhysicalGpu is an explicit field on their param structs, so they fit
    # there alongside the newer ClientIllum* zone-based API.


    # NvAPI_Stereo_Enable(void);
    # NvAPI_Stereo_Disable(void);
    # NvAPI_Stereo_IsEnabled(NvU8 *pIsStereoEnabled);

    # NvAPI_Stereo_IsWindowedModeSupported(NvU8* bSupported);
    # NvAPI_Stereo_SetDriverMode( NV_STEREO_DRIVER_MODE mode );
    def __init__(self):
        InitNV()
    
    def __iter__(self):
        # NvAPI_EnumNvidiaDisplayHandle enumerates per-DISPLAY, not
        # per-GPU -- a single logical GPU driving 3 monitors resolves to
        # the same NvLogicalGpuHandle 3 times (once per display index).
        # LogicalGPU(count) itself re-derives everything it needs (its
        # physical GPUs, and via those all of their displays) from
        # `count` independently, so it's enough to remember which actual
        # GPU handle each count already resolved to and only yield the
        # first display index that reaches a given GPU -- iterating the
        # yielded LogicalGPU still walks its *entire* display set, not
        # just the one display used to find it.
        count = 0
        hNvDisplay = NvDisplayHandle()
        nvStatus = NvAPI_EnumNvidiaDisplayHandle(NvU32(count), ctypes.byref(hNvDisplay))
        seen_gpu_handles = set()

        while nvStatus == NvAPI_Status.NVAPI_OK:
            pLogicalGPU = NvLogicalGpuHandle()
            if NvAPI_GetLogicalGPUFromDisplay(
                    hNvDisplay,
                    ctypes.byref(pLogicalGPU)
            ) == NvAPI_Status.NVAPI_OK:

                handle_value = ctypes.cast(pLogicalGPU, ctypes.c_void_p).value
                if handle_value not in seen_gpu_handles:
                    seen_gpu_handles.add(handle_value)
                    yield LogicalGPU(count)

            count += 1
            nvStatus = NvAPI_EnumNvidiaDisplayHandle(NvU32(count), ctypes.byref(hNvDisplay))

        if nvStatus != NvAPI_Status.NVAPI_END_ENUMERATION:
            raise RuntimeError("NvAPI_EnumNvidiaDisplayHandle returned error code %d" % (nvStatus,))

    @property
    def preferred_stereo_display(self):
        # system-wide (no displayId parameter) -- the display driving the
        # 3-pin DIN stereo signal, if any
        pPreferredStereoDisplay = NV_GET_PREFERRED_STEREO_DISPLAY()
        pPreferredStereoDisplay.version = NV_GET_PREFERRED_STEREO_DISPLAY_VER
        nvStatus = NvAPI_DISP_GetPreferredStereoDisplay(ctypes.byref(pPreferredStereoDisplay))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_GetPreferredStereoDisplay returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return PreferredStereoDisplay(display_id=pPreferredStereoDisplay.displayId)

    @preferred_stereo_display.setter
    def preferred_stereo_display(self, display_id):
        # display_id=0 resets to the driver default selection
        pPreferredStereoDisplay = NV_SET_PREFERRED_STEREO_DISPLAY()
        pPreferredStereoDisplay.version = NV_SET_PREFERRED_STEREO_DISPLAY_VER
        pPreferredStereoDisplay.displayId = display_id
        nvStatus = NvAPI_DISP_SetPreferredStereoDisplay(ctypes.byref(pPreferredStereoDisplay))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_SetPreferredStereoDisplay returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @property
    def nv_managed_dedicated_displays(self):
        # system-wide (no displayId parameter); two-pass allocation
        pDedicatedDisplayCount = NvU32(0)
        nvStatus = NvAPI_DISP_GetNvManagedDedicatedDisplays(ctypes.byref(pDedicatedDisplayCount), None)
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_GetNvManagedDedicatedDisplays returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        if not pDedicatedDisplayCount.value:
            return []

        buf = (NV_MANAGED_DEDICATED_DISPLAY_INFO * pDedicatedDisplayCount.value)()
        for entry in buf:
            entry.version = NV_MANAGED_DEDICATED_DISPLAY_INFO_VER

        nvStatus = NvAPI_DISP_GetNvManagedDedicatedDisplays(ctypes.byref(pDedicatedDisplayCount), buf)
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_GetNvManagedDedicatedDisplays returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return [
            ManagedDedicatedDisplay(
                display_id=entry.displayId,
                is_acquired=bool(entry.flags & 1),
                is_mosaic=bool(entry.flags & 2),
            )
            for entry in buf[:pDedicatedDisplayCount.value]
        ]

    @property
    def driver_info(self):
        pDriverInfo = NV_DISPLAY_DRIVER_INFO()
        pDriverInfo.version = NV_DISPLAY_DRIVER_INFO_VER
        nvStatus = NvAPI_SYS_GetDisplayDriverInfo(ctypes.byref(pDriverInfo))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_SYS_GetDisplayDriverInfo returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return DisplayDriverInfo(
            driver_version=pDriverInfo.driverVersion,
            build_branch=pDriverInfo.szBuildBranch.decode('ascii', 'replace').rstrip('\x00'),
            build_base_branch=pDriverInfo.szBuildBaseBranch.decode('ascii', 'replace').rstrip('\x00'),
            is_dch_driver=bool(pDriverInfo.flags & 1),
            is_studio_package=bool(pDriverInfo.flags & 2),
            is_game_ready_package=bool(pDriverInfo.flags & 4),
            is_rtx_production_branch_package=bool(pDriverInfo.flags & 8),
            is_rtx_new_feature_branch_package=bool(pDriverInfo.flags & 16),
        )

    @property
    def system_physical_gpus(self):
        # newer, adapter-type-aware alternative to NvAPI_EnumPhysicalGPUs
        pPhysicalGPUs = NV_PHYSICAL_GPUS()
        pPhysicalGPUs.version = NV_PHYSICAL_GPUS_VER
        nvStatus = NvAPI_SYS_GetPhysicalGPUs(ctypes.byref(pPhysicalGPUs))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_SYS_GetPhysicalGPUs returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return [
            SystemGpuHandle(adapter_type=NV_ADAPTER_TYPE.get(entry.adapterType))
            for entry in pPhysicalGPUs.gpuHandleData[:pPhysicalGPUs.gpuHandleCount]
        ]

    @property
    def system_logical_gpus(self):
        pLogicalGPUs = NV_LOGICAL_GPUS()
        pLogicalGPUs.version = NV_LOGICAL_GPUS_VER
        nvStatus = NvAPI_SYS_GetLogicalGPUs(ctypes.byref(pLogicalGPUs))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_SYS_GetLogicalGPUs returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return [
            SystemGpuHandle(adapter_type=NV_ADAPTER_TYPE.get(entry.adapterType))
            for entry in pLogicalGPUs.gpuHandleData[:pLogicalGPUs.gpuHandleCount]
        ]

    @property
    def display_config(self):
        # 3-pass protocol per NvAPI_DISP_GetDisplayConfig's own doc comment:
        # get path count, then per-path targetInfoCount, then the actual
        # per-target array once its size is known.
        pathInfoCount = NvU32(0)
        nvStatus = NvAPI_DISP_GetDisplayConfig(ctypes.byref(pathInfoCount), None)
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_GetDisplayConfig returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        if pathInfoCount.value == 0:
            return []

        pathInfo = (NV_DISPLAYCONFIG_PATH_INFO * pathInfoCount.value)()
        sourceModeInfo = (NV_DISPLAYCONFIG_SOURCE_MODE_INFO * pathInfoCount.value)()
        for i in range(pathInfoCount.value):
            pathInfo[i].version = NV_DISPLAYCONFIG_PATH_INFO_VER
            pathInfo[i].sourceModeInfo = ctypes.pointer(sourceModeInfo[i])

        nvStatus = NvAPI_DISP_GetDisplayConfig(ctypes.byref(pathInfoCount), pathInfo)
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_GetDisplayConfig returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        targetArrays = []
        for i in range(pathInfoCount.value):
            count = pathInfo[i].targetInfoCount
            if count:
                arr = (NV_DISPLAYCONFIG_PATH_TARGET_INFO * count)()
                targetArrays.append(arr)
                pathInfo[i].targetInfo = ctypes.cast(arr, POINTER(NV_DISPLAYCONFIG_PATH_TARGET_INFO))
            else:
                targetArrays.append(None)

        if any(targetArrays):
            nvStatus = NvAPI_DISP_GetDisplayConfig(ctypes.byref(pathInfoCount), pathInfo)
            if NvAPI_Status.NVAPI_OK != nvStatus:
                szDesc = NvAPI_ShortString()
                NvAPI_GetErrorMessage(nvStatus, szDesc)
                raise RuntimeError("NvAPI_DISP_GetDisplayConfig returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        result = []
        for i in range(pathInfoCount.value):
            p = pathInfo[i]
            targets = tuple(
                DisplayConfigTarget(p.targetInfo[j].displayId, p.targetInfo[j].targetId)
                for j in range(p.targetInfoCount)
            )
            sm = sourceModeInfo[i]
            result.append(DisplayConfigPath(
                p.sourceId, targets,
                (sm.resolution.width, sm.resolution.height, sm.resolution.colorDepth),
                (sm.position.x, sm.position.y),
                bool(sm.bGDIPrimary),
            ))

        return result

    @display_config.setter
    def display_config(self, value):
        # value: (paths, flags) tuple. paths is an iterable of
        # DisplayConfigPath (as returned by the display_config getter) or
        # any object exposing the same attributes; flags is a bitmask of
        # NV_DISPLAYCONFIG_FLAGS (0 to just apply). Advanced per-target
        # settings (rotation/scaling/timing overrides) are not supported
        # through this entry point -- pass details=NULL, matching what
        # the getter itself reads back.
        paths, flags = value
        paths = list(paths)
        pathInfo = (NV_DISPLAYCONFIG_PATH_INFO * len(paths))()
        sourceModeInfo = (NV_DISPLAYCONFIG_SOURCE_MODE_INFO * len(paths))()
        targetArrays = []

        for i, path in enumerate(paths):
            pathInfo[i].version = NV_DISPLAYCONFIG_PATH_INFO_VER
            pathInfo[i].sourceId = path.source_id

            width, height, colorDepth = path.resolution
            sourceModeInfo[i].resolution.width = width
            sourceModeInfo[i].resolution.height = height
            sourceModeInfo[i].resolution.colorDepth = colorDepth
            x, y = path.position
            sourceModeInfo[i].position.x = x
            sourceModeInfo[i].position.y = y
            sourceModeInfo[i].bGDIPrimary = 1 if path.is_gdi_primary else 0
            pathInfo[i].sourceModeInfo = ctypes.pointer(sourceModeInfo[i])

            targets = list(path.targets)
            arr = (NV_DISPLAYCONFIG_PATH_TARGET_INFO * len(targets))()
            for j, target in enumerate(targets):
                arr[j].displayId = target.display_id
                arr[j].targetId = target.target_id
            targetArrays.append(arr)
            pathInfo[i].targetInfoCount = len(targets)
            pathInfo[i].targetInfo = ctypes.cast(arr, POINTER(NV_DISPLAYCONFIG_PATH_TARGET_INFO))

        nvStatus = NvAPI_DISP_SetDisplayConfig(NvU32(len(paths)), pathInfo, NvU32(flags))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_SetDisplayConfig returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @staticmethod
    def try_custom_display(display_ids, custom_displays):
        # Applies a custom-timing modeset trial to hardware without saving
        # it -- follow up with save_custom_display to persist, or
        # revert_custom_display_trial to undo.
        display_ids = list(display_ids)
        custom_displays = list(custom_displays)
        idArray = (NvU32 * len(display_ids))(*display_ids)
        custDispArray = (NV_CUSTOM_DISPLAY * len(custom_displays))(*[_custom_display_to_struct(cd) for cd in custom_displays])
        nvStatus = NvAPI_DISP_TryCustomDisplay(idArray, NvU32(len(display_ids)), custDispArray)
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_TryCustomDisplay returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @staticmethod
    def delete_custom_display(display_ids, custom_display):
        display_ids = list(display_ids)
        idArray = (NvU32 * len(display_ids))(*display_ids)
        custDisp = _custom_display_to_struct(custom_display)
        nvStatus = NvAPI_DISP_DeleteCustomDisplay(idArray, NvU32(len(display_ids)), ctypes.byref(custDisp))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_DeleteCustomDisplay returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @staticmethod
    def save_custom_display(display_ids, is_this_output_id_only=False, is_this_monitor_id_only=False):
        # Must be called right after try_custom_display -- persists the
        # trial that's currently active on the hardware.
        display_ids = list(display_ids)
        idArray = (NvU32 * len(display_ids))(*display_ids)
        nvStatus = NvAPI_DISP_SaveCustomDisplay(
            idArray, NvU32(len(display_ids)),
            NvU32(1 if is_this_output_id_only else 0), NvU32(1 if is_this_monitor_id_only else 0),
        )
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_SaveCustomDisplay returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

    @staticmethod
    def revert_custom_display_trial(display_ids):
        display_ids = list(display_ids)
        idArray = (NvU32 * len(display_ids))(*display_ids)
        nvStatus = NvAPI_DISP_RevertCustomDisplayTrial(idArray, NvU32(len(display_ids)))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_DISP_RevertCustomDisplayTrial returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))