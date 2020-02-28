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
from ..utils import *


class DXGI_RATIONAL(ctypes.Structure):
    pass


class DXGI_SAMPLE_DESC(ctypes.Structure):
    pass


DXGI_RATIONAL._fields_ = [
    ('Numerator', UINT),
    ('Denominator', UINT),
]

# The following values are used with DXGI_SAMPLE_DESC::Quality:
DXGI_STANDARD_MULTISAMPLE_QUALITY_PATTERN = 0xFFFFFFFF
DXGI_CENTER_MULTISAMPLE_QUALITY_PATTERN = 0xFFFFFFFE


DXGI_SAMPLE_DESC._fields_ = [
    ('Count', UINT),
    ('Quality', UINT),
]


class DXGI_COLOR_SPACE_TYPE(ENUM):
    DXGI_COLOR_SPACE_RGB_FULL_G22_NONE_P709 = 0
    DXGI_COLOR_SPACE_RGB_FULL_G10_NONE_P709 = 1
    DXGI_COLOR_SPACE_RGB_STUDIO_G22_NONE_P709 = 2
    DXGI_COLOR_SPACE_RGB_STUDIO_G22_NONE_P2020 = 3
    DXGI_COLOR_SPACE_RESERVED = 4
    DXGI_COLOR_SPACE_YCBCR_FULL_G22_NONE_P709_X601 = 5
    DXGI_COLOR_SPACE_YCBCR_STUDIO_G22_LEFT_P601 = 6
    DXGI_COLOR_SPACE_YCBCR_FULL_G22_LEFT_P601 = 7
    DXGI_COLOR_SPACE_YCBCR_STUDIO_G22_LEFT_P709 = 8
    DXGI_COLOR_SPACE_YCBCR_FULL_G22_LEFT_P709 = 9
    DXGI_COLOR_SPACE_YCBCR_STUDIO_G22_LEFT_P2020 = 10
    DXGI_COLOR_SPACE_YCBCR_FULL_G22_LEFT_P2020 = 11
    DXGI_COLOR_SPACE_RGB_FULL_G2084_NONE_P2020 = 12
    DXGI_COLOR_SPACE_YCBCR_STUDIO_G2084_LEFT_P2020 = 13
    DXGI_COLOR_SPACE_RGB_STUDIO_G2084_NONE_P2020 = 14
    DXGI_COLOR_SPACE_YCBCR_STUDIO_G22_TOPLEFT_P2020 = 15
    DXGI_COLOR_SPACE_YCBCR_STUDIO_G2084_TOPLEFT_P2020 = 16
    DXGI_COLOR_SPACE_RGB_FULL_G22_NONE_P2020 = 17
    DXGI_COLOR_SPACE_YCBCR_STUDIO_GHLG_TOPLEFT_P2020 = 18
    DXGI_COLOR_SPACE_YCBCR_FULL_GHLG_TOPLEFT_P2020 = 19
    DXGI_COLOR_SPACE_RGB_STUDIO_G24_NONE_P709 = 20
    DXGI_COLOR_SPACE_RGB_STUDIO_G24_NONE_P2020 = 21
    DXGI_COLOR_SPACE_YCBCR_STUDIO_G24_LEFT_P709 = 22
    DXGI_COLOR_SPACE_YCBCR_STUDIO_G24_LEFT_P2020 = 23
    DXGI_COLOR_SPACE_YCBCR_STUDIO_G24_TOPLEFT_P2020 = 24
    DXGI_COLOR_SPACE_CUSTOM = 0xFFFFFFFF


