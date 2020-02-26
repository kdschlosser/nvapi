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

import ctypes
import comtypes
from comtypes.GUID import GUID
from ctypes import POINTER
from ctypes.wintypes import BOOL, UINT, FLOAT, LPCWSTR


D3D12_GPU_VIRTUAL_ADDRESS = ctypes.c_uint64
STDMETHOD = comtypes.STDMETHOD


class NV_EDID_V1(ctypes.Structure):
    pass


class NV_EDID_V2(ctypes.Structure):
    pass


class NV_EDID_V3(ctypes.Structure):
    pass


class NV_VIEWPORTF(ctypes.Structure):
    pass


class tagNV_TIMINGEXT(ctypes.Structure):
    pass


NV_TIMINGEXT = tagNV_TIMINGEXT


class _NV_TIMING(ctypes.Structure):
    pass


NV_TIMING = _NV_TIMING


class NV_VIEW_TARGET_INFO(ctypes.Structure):
    pass


class NV_DISPLAY_PATH(ctypes.Structure):
    pass


class NV_DISPLAY_PATH_INFO_V3(ctypes.Structure):
    pass


class NV_DISPLAY_PATH_INFO(ctypes.Structure):
    pass


class _NV_POSITION(ctypes.Structure):
    pass


NV_POSITION = _NV_POSITION


class _NV_RESOLUTION(ctypes.Structure):
    pass


NV_RESOLUTION = _NV_RESOLUTION


class _NV_DISPLAYCONFIG_PATH_ADVANCED_TARGET_INFO_V1(ctypes.Structure):
    pass


NV_DISPLAYCONFIG_PATH_ADVANCED_TARGET_INFO_V1 = _NV_DISPLAYCONFIG_PATH_ADVANCED_TARGET_INFO_V1


class _NV_DISPLAYCONFIG_PATH_TARGET_INFO_V1(ctypes.Structure):
    pass


NV_DISPLAYCONFIG_PATH_TARGET_INFO_V1 = _NV_DISPLAYCONFIG_PATH_TARGET_INFO_V1


class _NV_DISPLAYCONFIG_PATH_TARGET_INFO_V2(ctypes.Structure):
    pass


NV_DISPLAYCONFIG_PATH_TARGET_INFO_V2 = _NV_DISPLAYCONFIG_PATH_TARGET_INFO_V2


class _NV_DISPLAYCONFIG_SOURCE_MODE_INFO_V1(ctypes.Structure):
    pass


NV_DISPLAYCONFIG_SOURCE_MODE_INFO_V1 = _NV_DISPLAYCONFIG_SOURCE_MODE_INFO_V1


class _NV_DISPLAYCONFIG_PATH_INFO_V1(ctypes.Structure):
    pass


NV_DISPLAYCONFIG_PATH_INFO_V1 = _NV_DISPLAYCONFIG_PATH_INFO_V1


class _NV_DISPLAYCONFIG_PATH_INFO_V2(ctypes.Structure):
    pass


NV_DISPLAYCONFIG_PATH_INFO_V2 = _NV_DISPLAYCONFIG_PATH_INFO_V2


class NV_GPU_PERF_PSTATES20_PARAM_DELTA(ctypes.Structure):
    pass


class NV_GPU_PSTATE20_CLOCK_ENTRY_V1(ctypes.Structure):
    pass


class NV_GPU_PSTATE20_BASE_VOLTAGE_ENTRY_V1(ctypes.Structure):
    pass


class NV_GPU_PERF_PSTATES20_INFO_V1(ctypes.Structure):
    pass


class _NV_GPU_PERF_PSTATES20_INFO_V2(ctypes.Structure):
    pass


NV_GPU_PERF_PSTATES20_INFO_V2 = _NV_GPU_PERF_PSTATES20_INFO_V2


class NV_DISPLAY_DRIVER_VERSION(ctypes.Structure):
    pass


class _NV_GPU_DISPLAYIDS(ctypes.Structure):
    pass


NV_GPU_DISPLAYIDS = _NV_GPU_DISPLAYIDS


class _NV_BOARD_INFO(ctypes.Structure):
    pass


NV_BOARD_INFO_V1 = _NV_BOARD_INFO


class NV_I2C_INFO_V1(ctypes.Structure):
    pass


class NV_I2C_INFO_V2(ctypes.Structure):
    pass


class NV_I2C_INFO_V3(ctypes.Structure):
    pass


class NV_GPU_GET_HDCP_SUPPORT_STATUS(ctypes.Structure):
    pass


class NV_GPU_ECC_STATUS_INFO(ctypes.Structure):
    pass


class NV_GPU_ECC_ERROR_INFO(ctypes.Structure):
    pass


class NV_GPU_ECC_CONFIGURATION_INFO(ctypes.Structure):
    pass


class NV_SCANOUT_INTENSITY_DATA_V1(ctypes.Structure):
    pass


class NV_SCANOUT_INTENSITY_DATA_V2(ctypes.Structure):
    pass


class _NV_SCANOUT_INTENSITY_STATE_DATA(ctypes.Structure):
    pass


NV_SCANOUT_INTENSITY_STATE_DATA = _NV_SCANOUT_INTENSITY_STATE_DATA


class NV_SCANOUT_WARPING_DATA(ctypes.Structure):
    pass


class _NV_SCANOUT_WARPING_STATE_DATA(ctypes.Structure):
    pass


NV_SCANOUT_WARPING_STATE_DATA = _NV_SCANOUT_WARPING_STATE_DATA


class _NV_SCANOUT_INFORMATION(ctypes.Structure):
    pass


NV_SCANOUT_INFORMATION = _NV_SCANOUT_INFORMATION


class _NV_LOGICAL_GPU_DATA_V1(ctypes.Structure):
    pass


NV_LOGICAL_GPU_DATA_V1 = _NV_LOGICAL_GPU_DATA_V1


class NV_GPU_PERF_PSTATES_INFO_V1(ctypes.Structure):
    pass


class NV_GPU_PERF_PSTATES_INFO_V2(ctypes.Structure):
    pass


class NV_GPU_DYNAMIC_PSTATES_INFO_EX(ctypes.Structure):
    pass


class NV_GPU_THERMAL_SETTINGS_V1(ctypes.Structure):
    pass


class NV_GPU_THERMAL_SETTINGS_V2(ctypes.Structure):
    pass


class NV_GPU_CLOCK_FREQUENCIES_V1(ctypes.Structure):
    pass


class NV_GPU_CLOCK_FREQUENCIES_V2(ctypes.Structure):
    pass


class _NV_GPU_QUERY_ILLUMINATION_SUPPORT_PARM_V1(ctypes.Structure):
    pass


NV_GPU_QUERY_ILLUMINATION_SUPPORT_PARM_V1 = _NV_GPU_QUERY_ILLUMINATION_SUPPORT_PARM_V1


class _NV_GPU_GET_ILLUMINATION_PARM_V1(ctypes.Structure):
    pass


NV_GPU_GET_ILLUMINATION_PARM_V1 = _NV_GPU_GET_ILLUMINATION_PARM_V1


class _NV_GPU_SET_ILLUMINATION_PARM_V1(ctypes.Structure):
    pass


NV_GPU_SET_ILLUMINATION_PARM_V1 = _NV_GPU_SET_ILLUMINATION_PARM_V1


class _NV_GPU_CLIENT_ILLUM_DEVICE_INFO_DATA_MCUV10(ctypes.Structure):
    pass


NV_GPU_CLIENT_ILLUM_DEVICE_INFO_DATA_MCUV10 = _NV_GPU_CLIENT_ILLUM_DEVICE_INFO_DATA_MCUV10


class _NV_GPU_CLIENT_ILLUM_DEVICE_INFO_V1(ctypes.Structure):
    pass


NV_GPU_CLIENT_ILLUM_DEVICE_INFO_V1 = _NV_GPU_CLIENT_ILLUM_DEVICE_INFO_V1


class _NV_GPU_CLIENT_ILLUM_DEVICE_INFO_PARAMS_V1(ctypes.Structure):
    pass


NV_GPU_CLIENT_ILLUM_DEVICE_INFO_PARAMS_V1 = _NV_GPU_CLIENT_ILLUM_DEVICE_INFO_PARAMS_V1


class NV_GPU_CLIENT_ILLUM_DEVICE_SYNC_V1(ctypes.Structure):
    pass


class NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_V1(ctypes.Structure):
    pass


class NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_PARAMS_V1(ctypes.Structure):
    pass


class _NV_GPU_CLIENT_ILLUM_ZONE_INFO_DATA_RGB(ctypes.Structure):
    pass


NV_GPU_CLIENT_ILLUM_ZONE_INFO_DATA_RGB = _NV_GPU_CLIENT_ILLUM_ZONE_INFO_DATA_RGB


class _NV_GPU_CLIENT_ILLUM_ZONE_INFO_V1(ctypes.Structure):
    pass


NV_GPU_CLIENT_ILLUM_ZONE_INFO_V1 = _NV_GPU_CLIENT_ILLUM_ZONE_INFO_V1


class _NV_GPU_CLIENT_ILLUM_ZONE_INFO_PARAMS_V1(ctypes.Structure):
    pass


NV_GPU_CLIENT_ILLUM_ZONE_INFO_PARAMS_V1 = _NV_GPU_CLIENT_ILLUM_ZONE_INFO_PARAMS_V1


class _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_RGB_PARAMS(ctypes.Structure):
    pass


NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_RGB_PARAMS = _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_RGB_PARAMS


class _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_RGB(ctypes.Structure):
    pass


NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_RGB = _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_RGB


class _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_PIECEWISE_LINEAR(ctypes.Structure):
    pass


NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_PIECEWISE_LINEAR = _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_PIECEWISE_LINEAR


class _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_PIECEWISE_LINEAR_RGB(ctypes.Structure):
    pass


NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_PIECEWISE_LINEAR_RGB = _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_PIECEWISE_LINEAR_RGB


class _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_RGB(ctypes.Structure):
    pass


NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_RGB = _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_RGB


class _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_COLOR_FIXED_PARAMS(ctypes.Structure):
    pass


NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_COLOR_FIXED_PARAMS = _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_COLOR_FIXED_PARAMS


class _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_COLOR_FIXED(ctypes.Structure):
    pass


NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_COLOR_FIXED = _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_COLOR_FIXED


class _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_PIECEWISE_LINEAR_COLOR_FIXED(ctypes.Structure):
    pass


NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_PIECEWISE_LINEAR_COLOR_FIXED = _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_PIECEWISE_LINEAR_COLOR_FIXED


class _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_COLOR_FIXED(ctypes.Structure):
    pass


NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_COLOR_FIXED = _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_COLOR_FIXED


class _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_V1(ctypes.Structure):
    pass


NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_V1 = _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_V1


class _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_PARAMS_V1(ctypes.Structure):
    pass


NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_PARAMS_V1 = _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_PARAMS_V1


class _NV_DISPLAY_PORT_INFO_V1(ctypes.Structure):
    pass


NV_DISPLAY_PORT_INFO_V1 = _NV_DISPLAY_PORT_INFO_V1


class NV_DISPLAY_PORT_CONFIG(ctypes.Structure):
    pass


class _NV_HDMI_SUPPORT_INFO_V1(ctypes.Structure):
    pass


NV_HDMI_SUPPORT_INFO_V1 = _NV_HDMI_SUPPORT_INFO_V1


class _NV_HDMI_SUPPORT_INFO_V2(ctypes.Structure):
    pass


NV_HDMI_SUPPORT_INFO_V2 = _NV_HDMI_SUPPORT_INFO_V2


class NV_INFOFRAME_PROPERTY(ctypes.Structure):
    pass


class NV_INFOFRAME_VIDEO(ctypes.Structure):
    pass


class NV_INFOFRAME_AUDIO(ctypes.Structure):
    pass


class NV_INFOFRAME_DATA(ctypes.Structure):
    pass


class _NV_COLOR_DATA_V1(ctypes.Structure):
    pass


NV_COLOR_DATA_V1 = _NV_COLOR_DATA_V1


class _NV_COLOR_DATA_V2(ctypes.Structure):
    pass


NV_COLOR_DATA_V2 = _NV_COLOR_DATA_V2


class _NV_COLOR_DATA_V3(ctypes.Structure):
    pass


NV_COLOR_DATA_V3 = _NV_COLOR_DATA_V3


class _NV_COLOR_DATA_V4(ctypes.Structure):
    pass


NV_COLOR_DATA_V4 = _NV_COLOR_DATA_V4


class _NV_COLOR_DATA_V5(ctypes.Structure):
    pass


NV_COLOR_DATA_V5 = _NV_COLOR_DATA_V5


class _NV_HDR_CAPABILITIES_V1(ctypes.Structure):
    pass


NV_HDR_CAPABILITIES_V1 = _NV_HDR_CAPABILITIES_V1


class _NV_HDR_CAPABILITIES_V2(ctypes.Structure):
    pass


NV_HDR_CAPABILITIES_V2 = _NV_HDR_CAPABILITIES_V2


class _NV_HDR_COLOR_DATA_V1(ctypes.Structure):
    pass


NV_HDR_COLOR_DATA_V1 = _NV_HDR_COLOR_DATA_V1


class _NV_HDR_COLOR_DATA_V2(ctypes.Structure):
    pass


NV_HDR_COLOR_DATA_V2 = _NV_HDR_COLOR_DATA_V2


class NV_TIMING_FLAG(ctypes.Structure):
    pass


class _NV_TIMING_INPUT(ctypes.Structure):
    pass


NV_TIMING_INPUT = _NV_TIMING_INPUT


class _NV_MONITOR_CAPS_VCDB(ctypes.Structure):
    pass


NV_MONITOR_CAPS_VCDB = _NV_MONITOR_CAPS_VCDB


class _NV_MONITOR_CAPS_VSDB(ctypes.Structure):
    pass


NV_MONITOR_CAPS_VSDB = _NV_MONITOR_CAPS_VSDB


class _NV_MONITOR_CAPABILITIES_V1(ctypes.Structure):
    pass


NV_MONITOR_CAPABILITIES_V1 = _NV_MONITOR_CAPABILITIES_V1


class _NV_MONITOR_COLOR_DATA(ctypes.Structure):
    pass


NV_MONITOR_COLOR_CAPS_V1 = _NV_MONITOR_COLOR_DATA


class NV_CUSTOM_DISPLAY(ctypes.Structure):
    pass


class NV_MOSAIC_TOPO_DETAILS(ctypes.Structure):
    pass


class NV_MOSAIC_TOPO_BRIEF(ctypes.Structure):
    pass


class _NV_MOSAIC_DISPLAY_SETTING_V1(ctypes.Structure):
    pass


NV_MOSAIC_DISPLAY_SETTING_V1 = _NV_MOSAIC_DISPLAY_SETTING_V1


class NV_MOSAIC_DISPLAY_SETTING_V2(ctypes.Structure):
    pass


class _NV_MOSAIC_SUPPORTED_TOPO_INFO_V1(ctypes.Structure):
    pass


NV_MOSAIC_SUPPORTED_TOPO_INFO_V1 = _NV_MOSAIC_SUPPORTED_TOPO_INFO_V1


class _NV_MOSAIC_SUPPORTED_TOPO_INFO_V2(ctypes.Structure):
    pass


NV_MOSAIC_SUPPORTED_TOPO_INFO_V2 = _NV_MOSAIC_SUPPORTED_TOPO_INFO_V2


class NV_MOSAIC_TOPO_GROUP(ctypes.Structure):
    pass


class _NV_MOSAIC_GRID_TOPO_DISPLAY_V1(ctypes.Structure):
    pass


NV_MOSAIC_GRID_TOPO_DISPLAY_V1 = _NV_MOSAIC_GRID_TOPO_DISPLAY_V1


class _NV_MOSAIC_GRID_TOPO_DISPLAY_V2(ctypes.Structure):
    pass


NV_MOSAIC_GRID_TOPO_DISPLAY_V2 = _NV_MOSAIC_GRID_TOPO_DISPLAY_V2


class _NV_MOSAIC_GRID_TOPO_V1(ctypes.Structure):
    pass


NV_MOSAIC_GRID_TOPO_V1 = _NV_MOSAIC_GRID_TOPO_V1


class _NV_MOSAIC_GRID_TOPO_V2(ctypes.Structure):
    pass


NV_MOSAIC_GRID_TOPO_V2 = _NV_MOSAIC_GRID_TOPO_V2


class NV_MOSAIC_DISPLAY_TOPO_STATUS(ctypes.Structure):
    pass


class NV_MOSAIC_TOPOLOGY(ctypes.Structure):
    pass


class NV_MOSAIC_SUPPORTED_TOPOLOGIES(ctypes.Structure):
    pass


class _NV_GSYNC_CAPABILITIES_V1(ctypes.Structure):
    pass


NV_GSYNC_CAPABILITIES_V1 = _NV_GSYNC_CAPABILITIES_V1


class _NV_GSYNC_CAPABILITIES_V2(ctypes.Structure):
    pass


NV_GSYNC_CAPABILITIES_V2 = _NV_GSYNC_CAPABILITIES_V2


class _NV_GSYNC_GPU(ctypes.Structure):
    pass


NV_GSYNC_GPU = _NV_GSYNC_GPU


class _NV_GSYNC_DISPLAY(ctypes.Structure):
    pass


NV_GSYNC_DISPLAY = _NV_GSYNC_DISPLAY


class _NV_GSYNC_DELAY(ctypes.Structure):
    pass


NV_GSYNC_DELAY = _NV_GSYNC_DELAY


class _NV_GSYNC_CONTROL_PARAMS(ctypes.Structure):
    pass


NV_GSYNC_CONTROL_PARAMS = _NV_GSYNC_CONTROL_PARAMS


class _NV_GSYNC_STATUS(ctypes.Structure):
    pass


NV_GSYNC_STATUS = _NV_GSYNC_STATUS


class _NV_GSYNC_STATUS_PARAMS_V1(ctypes.Structure):
    pass


NV_GSYNC_STATUS_PARAMS_V1 = _NV_GSYNC_STATUS_PARAMS_V1


class _NV_GSYNC_STATUS_PARAMS_V2(ctypes.Structure):
    pass


NV_GSYNC_STATUS_PARAMS_V2 = _NV_GSYNC_STATUS_PARAMS_V2


class _NV_DX_VIDEO_STEREO_INFO(ctypes.Structure):
    pass


NV_DX_VIDEO_STEREO_INFO = _NV_DX_VIDEO_STEREO_INFO


class NvAPI_D3D11_RASTERIZER_DESC_EX(ctypes.Structure):
    pass


class NVAPI_ANSEL_FEATURE_CONFIGURATION_STRUCT(ctypes.Structure):
    pass


class NVAPI_ANSEL_CONFIGURATION_STRUCT_V1(ctypes.Structure):
    pass


class _NV_D3D11_FEATURE_DATA_RASTERIZER_SUPPORT(ctypes.Structure):
    pass


NV_D3D11_FEATURE_DATA_RASTERIZER_SUPPORT = _NV_D3D11_FEATURE_DATA_RASTERIZER_SUPPORT


class _NV_CUSTOM_SEMANTIC(ctypes.Structure):
    pass


NV_CUSTOM_SEMANTIC = _NV_CUSTOM_SEMANTIC


class NvAPI_D3D11_CREATE_GEOMETRY_SHADER_EX_V5(ctypes.Structure):
    pass


class NvAPI_D3D11_CREATE_VERTEX_SHADER_EX_V1(ctypes.Structure):
    pass


class NvAPI_D3D11_CREATE_VERTEX_SHADER_EX_V2(ctypes.Structure):
    pass


class NvAPI_D3D11_CREATE_VERTEX_SHADER_EX_V3(ctypes.Structure):
    pass


class NvAPI_D3D11_CREATE_HULL_SHADER_EX_V1(ctypes.Structure):
    pass


class NvAPI_D3D11_CREATE_HULL_SHADER_EX_V2(ctypes.Structure):
    pass


class NvAPI_D3D11_CREATE_DOMAIN_SHADER_EX_V1(ctypes.Structure):
    pass


class NvAPI_D3D11_CREATE_DOMAIN_SHADER_EX_V2(ctypes.Structure):
    pass


class NvAPI_D3D11_CREATE_DOMAIN_SHADER_EX_V3(ctypes.Structure):
    pass


class NvAPI_D3D11_CREATE_PIXEL_SHADER_EX_V1(ctypes.Structure):
    pass


class NvAPI_D3D11_CREATE_PIXEL_SHADER_EX_V2(ctypes.Structure):
    pass


class NvAPI_D3D11_CREATE_FASTGS_EXPLICIT_DESC_V1(ctypes.Structure):
    pass


class NVAPI_D3D12_PSO_EXTENSION_DESC_V1(ctypes.Structure):
    pass


class NVAPI_META_COMMAND_DESC(ctypes.Structure):
    pass


class NV_META_COMMAND_TENSOR_DESC(ctypes.Structure):
    pass


class NV_META_COMMAND_ACTIVATION_DESC(ctypes.Structure):
    pass


class NV_META_COMMAND_PADDING_DESC(ctypes.Structure):
    pass


class NV_META_COMMAND_CREATE_CONVOLUTION_EX_DESC(ctypes.Structure):
    pass


class NV_META_COMMAND_CONVOLUTION_FUSE_DESC(ctypes.Structure):
    pass


class NV_META_COMMAND_CREATE_GEMM_DESC(ctypes.Structure):
    pass


class NV_D3D11_META_COMMAND_RESOURCE(ctypes.Structure):
    pass


class NV_D3D11_META_COMMAND_INITIALIZE_CONVOLUTION_EX_DESC(ctypes.Structure):
    pass


class NV_D3D11_META_COMMAND_EXECUTE_CONVOLUTION_EX_DESC(ctypes.Structure):
    pass


class NV_D3D11_META_COMMAND_INITIALIZE_GEMM_DESC(ctypes.Structure):
    pass


class NV_D3D11_META_COMMAND_EXECUTE_GEMM_DESC(ctypes.Structure):
    pass


class NV_D3D12_META_COMMAND_INITIALIZE_CONVOLUTION_EX_DESC(ctypes.Structure):
    pass


class NV_D3D12_META_COMMAND_EXECUTE_CONVOLUTION_EX_DESC(ctypes.Structure):
    pass


class NV_D3D12_META_COMMAND_INITIALIZE_GEMM_DESC(ctypes.Structure):
    pass


class NV_D3D12_META_COMMAND_EXECUTE_GEMM_DESC(ctypes.Structure):
    pass


class _NV_MULTIGPU_CAPS_V1(ctypes.Structure):
    pass


NV_MULTIGPU_CAPS_V1 = _NV_MULTIGPU_CAPS_V1
PNV_MULTIGPU_CAPS_V1 = POINTER(_NV_MULTIGPU_CAPS_V1)


class _NV_MULTIGPU_CAPS_V2(ctypes.Structure):
    pass


NV_MULTIGPU_CAPS_V2 = _NV_MULTIGPU_CAPS_V2
PNV_MULTIGPU_CAPS_V2 = POINTER(_NV_MULTIGPU_CAPS_V2)


class _NV_QUERY_SINGLE_PASS_STEREO_SUPPORT_PARAMS_V1(ctypes.Structure):
    pass


NV_QUERY_SINGLE_PASS_STEREO_SUPPORT_PARAMS_V1 = _NV_QUERY_SINGLE_PASS_STEREO_SUPPORT_PARAMS_V1


class _NV_QUERY_SINGLE_PASS_STEREO_SUPPORT_PARAMS_V2(ctypes.Structure):
    pass


NV_QUERY_SINGLE_PASS_STEREO_SUPPORT_PARAMS_V2 = _NV_QUERY_SINGLE_PASS_STEREO_SUPPORT_PARAMS_V2


class _NV_QUERY_MULTIVIEW_SUPPORT_PARAMS_V1(ctypes.Structure):
    pass


NV_QUERY_MULTIVIEW_SUPPORT_PARAMS_V1 = _NV_QUERY_MULTIVIEW_SUPPORT_PARAMS_V1


class _NV_MULTIVIEW_PARAMS_V1(ctypes.Structure):
    pass


NV_MULTIVIEW_PARAMS_V1 = _NV_MULTIVIEW_PARAMS_V1


class _NV_QUERY_MODIFIED_W_SUPPORT_PARAMS(ctypes.Structure):
    pass


NV_QUERY_MODIFIED_W_SUPPORT_PARAMS_V1 = _NV_QUERY_MODIFIED_W_SUPPORT_PARAMS


class _NV_MODIFIED_W_COEFFICIENTS(ctypes.Structure):
    pass


NV_MODIFIED_W_COEFFICIENTS = _NV_MODIFIED_W_COEFFICIENTS


class _NV_MODIFIED_W_PARAMS(ctypes.Structure):
    pass


NV_MODIFIED_W_PARAMS_V1 = _NV_MODIFIED_W_PARAMS


class _NV_D3D_LATELATCH_OBJECT_DESC_V1(ctypes.Structure):
    pass


NV_D3D_LATELATCH_OBJECT_DESC_V1 = _NV_D3D_LATELATCH_OBJECT_DESC_V1


class _NV_QUERY_LATELATCH_SUPPORT_PARAMS(ctypes.Structure):
    pass


NV_QUERY_LATELATCH_SUPPORT_PARAMS_V1 = _NV_QUERY_LATELATCH_SUPPORT_PARAMS


class _NV_D3D12_MOSAIC_GETCOMPANIONALLOCATIONS(ctypes.Structure):
    pass


NV_D3D12_MOSAIC_GETCOMPANIONALLOCATIONS_V1 = _NV_D3D12_MOSAIC_GETCOMPANIONALLOCATIONS


class _NV_D3D12_MOSAIC_GETVIEWPORTANDGPUPARTITIONS(ctypes.Structure):
    pass


NV_D3D12_MOSAIC_GETVIEWPORTANDGPUPARTITIONS_V1 = _NV_D3D12_MOSAIC_GETVIEWPORTANDGPUPARTITIONS


class _NV_D3D1x_GRAPHICS_CAPS_V1(ctypes.Structure):
    pass


NV_D3D1x_GRAPHICS_CAPS_V1 = _NV_D3D1x_GRAPHICS_CAPS_V1


class _NV_D3D1x_GRAPHICS_CAPS_V2(ctypes.Structure):
    pass


NV_D3D1x_GRAPHICS_CAPS_V2 = _NV_D3D1x_GRAPHICS_CAPS_V2


class _NV_D3D11_EXCLUSIVE_SCISSOR_RECT_DESC_V1(ctypes.Structure):
    pass


NV_D3D11_EXCLUSIVE_SCISSOR_RECT_DESC_V1 = _NV_D3D11_EXCLUSIVE_SCISSOR_RECT_DESC_V1


class _NV_D3D11_EXCLUSIVE_SCISSOR_RECTS_DESC_V1(ctypes.Structure):
    pass


NV_D3D11_EXCLUSIVE_SCISSOR_RECTS_DESC_V1 = _NV_D3D11_EXCLUSIVE_SCISSOR_RECTS_DESC_V1


class _NV_D3D11_VIEWPORT_SHADING_RATE_DESC_V1(ctypes.Structure):
    pass


NV_D3D11_VIEWPORT_SHADING_RATE_DESC_V1 = _NV_D3D11_VIEWPORT_SHADING_RATE_DESC_V1


class _NV_D3D11_VIEWPORTS_SHADING_RATE_DESC_V1(ctypes.Structure):
    pass


NV_D3D11_VIEWPORTS_SHADING_RATE_DESC_V1 = _NV_D3D11_VIEWPORTS_SHADING_RATE_DESC_V1


class _NV_TEX2D_SRRV(ctypes.Structure):
    pass


NV_TEX2D_SRRV = _NV_TEX2D_SRRV


class _NV_TEX2D_ARRAY_SRRV(ctypes.Structure):
    pass


NV_TEX2D_ARRAY_SRRV = _NV_TEX2D_ARRAY_SRRV


class _NV_D3D11_SHADING_RATE_RESOURCE_VIEW_DESC_V1(ctypes.Structure):
    pass


NV_D3D11_SHADING_RATE_RESOURCE_VIEW_DESC_V1 = _NV_D3D11_SHADING_RATE_RESOURCE_VIEW_DESC_V1


class _NV_PIXEL_SRSO_1x2(ctypes.Structure):
    pass


NV_PIXEL_SRSO_1x2 = _NV_PIXEL_SRSO_1x2


class _NV_PIXEL_SRSO_2x1(ctypes.Structure):
    pass


NV_PIXEL_SRSO_2x1 = _NV_PIXEL_SRSO_2x1


class _NV_PIXEL_SRSO_2x2(ctypes.Structure):
    pass


NV_PIXEL_SRSO_2x2 = _NV_PIXEL_SRSO_2x2


class _NV_PIXEL_SRSO_2x4(ctypes.Structure):
    pass


NV_PIXEL_SRSO_2x4 = _NV_PIXEL_SRSO_2x4


class _NV_PIXEL_SRSO_4x2(ctypes.Structure):
    pass


NV_PIXEL_SRSO_4x2 = _NV_PIXEL_SRSO_4x2


class _NV_PIXEL_SRSO_4x4(ctypes.Structure):
    pass


NV_PIXEL_SRSO_4x4 = _NV_PIXEL_SRSO_4x4


class _NV_PIXEL_SHADING_RATE_SAMPLE_ORDER_TABLE_V1(ctypes.Structure):
    pass


NV_PIXEL_SHADING_RATE_SAMPLE_ORDER_TABLE_V1 = _NV_PIXEL_SHADING_RATE_SAMPLE_ORDER_TABLE_V1


class _NV_VRS_HELPER_LATCH_GAZE_PARAMS_V1(ctypes.Structure):
    pass


NV_VRS_HELPER_LATCH_GAZE_PARAMS_V1 = _NV_VRS_HELPER_LATCH_GAZE_PARAMS_V1


class _NV_FOVEATED_RENDERING_CUSTOM_SHADING_RATE_PRESET_DESC_V1(ctypes.Structure):
    pass


NV_FOVEATED_RENDERING_CUSTOM_SHADING_RATE_PRESET_DESC_V1 = _NV_FOVEATED_RENDERING_CUSTOM_SHADING_RATE_PRESET_DESC_V1


class _NV_FOVEATED_RENDERING_CUSTOM_FOVEATION_PATTERN_PRESET_DESC_V1(ctypes.Structure):
    pass


NV_FOVEATED_RENDERING_CUSTOM_FOVEATION_PATTERN_PRESET_DESC_V1 = _NV_FOVEATED_RENDERING_CUSTOM_FOVEATION_PATTERN_PRESET_DESC_V1


class _NV_FOVEATED_RENDERING_DESC_V1(ctypes.Structure):
    pass


NV_FOVEATED_RENDERING_DESC_V1 = _NV_FOVEATED_RENDERING_DESC_V1


class _NV_VRS_HELPER_ENABLE_PARAMS_V1(ctypes.Structure):
    pass


NV_VRS_HELPER_ENABLE_PARAMS_V1 = _NV_VRS_HELPER_ENABLE_PARAMS_V1


class _NV_VRS_HELPER_DISABLE_PARAMS_V1(ctypes.Structure):
    pass


NV_VRS_HELPER_DISABLE_PARAMS_V1 = _NV_VRS_HELPER_DISABLE_PARAMS_V1


class _NV_VRS_HELPER_GET_SHADING_RATE_RESOURCE_PARAMS_V1(ctypes.Structure):
    pass


NV_VRS_HELPER_GET_SHADING_RATE_RESOURCE_PARAMS_V1 = _NV_VRS_HELPER_GET_SHADING_RATE_RESOURCE_PARAMS_V1


class _NV_VRS_HELPER_PURGE_INTERNAL_RESOURCES_PARAMS_V1(ctypes.Structure):
    pass


NV_VRS_HELPER_PURGE_INTERNAL_RESOURCES_PARAMS_V1 = _NV_VRS_HELPER_PURGE_INTERNAL_RESOURCES_PARAMS_V1


class _NV_VRS_HELPER_INIT_PARAMS_V1(ctypes.Structure):
    pass


NV_VRS_HELPER_INIT_PARAMS_V1 = _NV_VRS_HELPER_INIT_PARAMS_V1


class _NV_FOVEATED_RENDERING_GAZE_DATA_PER_EYE(ctypes.Structure):
    pass


NV_FOVEATED_RENDERING_GAZE_DATA_PER_EYE_V1 = _NV_FOVEATED_RENDERING_GAZE_DATA_PER_EYE


class _NV_FOVEATED_RENDERING_UPDATE_GAZE_DATA_PARAMS(ctypes.Structure):
    pass


NV_FOVEATED_RENDERING_UPDATE_GAZE_DATA_PARAMS_V1 = _NV_FOVEATED_RENDERING_UPDATE_GAZE_DATA_PARAMS


class _NV_GAZE_HANDLER_INIT_PARAMS_V1(ctypes.Structure):
    pass


NV_GAZE_HANDLER_INIT_PARAMS_V1 = _NV_GAZE_HANDLER_INIT_PARAMS_V1


class _NV_MRS_CUSTOM_CONFIG_V1(ctypes.Structure):
    pass


NV_MRS_CUSTOM_CONFIG_V1 = _NV_MRS_CUSTOM_CONFIG_V1


class _NV_MRS_INSTANCED_STEREO_CONFIG_V1(ctypes.Structure):
    pass


NV_MRS_INSTANCED_STEREO_CONFIG_V1 = _NV_MRS_INSTANCED_STEREO_CONFIG_V1


class _NV_LMS_CUSTOM_CONFIG_V1(ctypes.Structure):
    pass


NV_LMS_CUSTOM_CONFIG_V1 = _NV_LMS_CUSTOM_CONFIG_V1


class _NV_LMS_INSTANCED_STEREO_CONFIG_V1(ctypes.Structure):
    pass


NV_LMS_INSTANCED_STEREO_CONFIG_V1 = _NV_LMS_INSTANCED_STEREO_CONFIG_V1


class _NV_CUSTOM_RECTS_V1(ctypes.Structure):
    pass


NV_CUSTOM_RECTS_V1 = _NV_CUSTOM_RECTS_V1


class _NV_SMP_ASSIST_ENABLE_PARAMS_V1(ctypes.Structure):
    pass


NV_SMP_ASSIST_ENABLE_PARAMS_V1 = _NV_SMP_ASSIST_ENABLE_PARAMS_V1


class _NV_SMP_ASSIST_DISABLE_PARAMS_V1(ctypes.Structure):
    pass


NV_SMP_ASSIST_DISABLE_PARAMS_V1 = _NV_SMP_ASSIST_DISABLE_PARAMS_V1


class _NV_SMP_ASSIST_FASTGSCBDATA_V1(ctypes.Structure):
    pass


NV_SMP_ASSIST_FASTGSCBDATA_V1 = _NV_SMP_ASSIST_FASTGSCBDATA_V1


class _NV_SMP_ASSIST_FASTGSCBDATA_MRS_INSTANCED_STEREO_V1(ctypes.Structure):
    pass


NV_SMP_ASSIST_FASTGSCBDATA_MRS_INSTANCED_STEREO_V1 = _NV_SMP_ASSIST_FASTGSCBDATA_MRS_INSTANCED_STEREO_V1


class _NV_SMP_ASSIST_REMAPCBDATA_V1(ctypes.Structure):
    pass


NV_SMP_ASSIST_REMAPCBDATA_V1 = _NV_SMP_ASSIST_REMAPCBDATA_V1


class _NV_SMP_ASSIST_GET_CONSTANTS_V3(ctypes.Structure):
    pass


NV_SMP_ASSIST_GET_CONSTANTS_V3 = _NV_SMP_ASSIST_GET_CONSTANTS_V3


class _NV_SMP_ASSIST_SETUP_PARAMS_V1(ctypes.Structure):
    pass


NV_SMP_ASSIST_SETUP_PARAMS_V1 = _NV_SMP_ASSIST_SETUP_PARAMS_V1


class _NV_SMP_ASSIST_UPDATE_INSTANCEDSTEREO_DATA_PARAMS_V1(ctypes.Structure):
    pass


NV_SMP_ASSIST_UPDATE_INSTANCEDSTEREO_DATA_PARAMS_V1 = _NV_SMP_ASSIST_UPDATE_INSTANCEDSTEREO_DATA_PARAMS_V1


class _NV_SMP_ASSIST_INITIALIZE_PARAMS_V1(ctypes.Structure):
    pass


NV_SMP_ASSIST_INITIALIZE_PARAMS_V1 = _NV_SMP_ASSIST_INITIALIZE_PARAMS_V1


class _NV_QUERY_SMP_ASSIST_SUPPORT_PARAMS_V1(ctypes.Structure):
    pass


NV_QUERY_SMP_ASSIST_SUPPORT_PARAMS_V1 = _NV_QUERY_SMP_ASSIST_SUPPORT_PARAMS_V1


class _NVVIOCAPS(ctypes.Structure):
    pass


NVVIOCAPS = _NVVIOCAPS


class _NVVIOCHANNELSTATUS(ctypes.Structure):
    pass


NVVIOCHANNELSTATUS = _NVVIOCHANNELSTATUS


class _NVVIOINPUTSTATUS(ctypes.Structure):
    pass


NVVIOINPUTSTATUS = _NVVIOINPUTSTATUS


class _NVVIOOUTPUTSTATUS(ctypes.Structure):
    pass


NVVIOOUTPUTSTATUS = _NVVIOOUTPUTSTATUS


class _NVVIOSTATUS(ctypes.Structure):
    pass


NVVIOSTATUS = _NVVIOSTATUS


class _NVVIOOUTPUTREGION(ctypes.Structure):
    pass


NVVIOOUTPUTREGION = _NVVIOOUTPUTREGION


class _NVVIOGAMMARAMP8(ctypes.Structure):
    pass


NVVIOGAMMARAMP8 = _NVVIOGAMMARAMP8


class _NVVIOGAMMARAMP10(ctypes.Structure):
    pass


NVVIOGAMMARAMP10 = _NVVIOGAMMARAMP10


class _NVVIOSYNCDELAY(ctypes.Structure):
    pass


NVVIOSYNCDELAY = _NVVIOSYNCDELAY


class _NVVIOVIDEOMODE(ctypes.Structure):
    pass


NVVIOVIDEOMODE = _NVVIOVIDEOMODE


class _NVVIOSIGNALFORMATDETAIL(ctypes.Structure):
    pass


NVVIOSIGNALFORMATDETAIL = _NVVIOSIGNALFORMATDETAIL


class _NVVIODATAFORMATDETAIL(ctypes.Structure):
    pass


NVVIODATAFORMATDETAIL = _NVVIODATAFORMATDETAIL


class _NVVIOCOLORCONVERSION(ctypes.Structure):
    pass


NVVIOCOLORCONVERSION = _NVVIOCOLORCONVERSION


class _NVVIOGAMMACORRECTION(ctypes.Structure):
    pass


NVVIOGAMMACORRECTION = _NVVIOGAMMACORRECTION


class _NVVIOCOMPOSITERANGE(ctypes.Structure):
    pass


NVVIOCOMPOSITERANGE = _NVVIOCOMPOSITERANGE


class _NVVIOOUTPUTCONFIG_V1(ctypes.Structure):
    pass


NVVIOOUTPUTCONFIG_V1 = _NVVIOOUTPUTCONFIG_V1


class _NVVIOOUTPUTCONFIG_V2(ctypes.Structure):
    pass


NVVIOOUTPUTCONFIG_V2 = _NVVIOOUTPUTCONFIG_V2


class _NVVIOOUTPUTCONFIG_V3(ctypes.Structure):
    pass


NVVIOOUTPUTCONFIG_V3 = _NVVIOOUTPUTCONFIG_V3


class _NVVIOSTREAM(ctypes.Structure):
    pass


NVVIOSTREAM = _NVVIOSTREAM


class _NVVIOINPUTCONFIG(ctypes.Structure):
    pass


NVVIOINPUTCONFIG = _NVVIOINPUTCONFIG


class _NVVIOCONFIG_V1(ctypes.Structure):
    pass


NVVIOCONFIG_V1 = _NVVIOCONFIG_V1


class _NVVIOCONFIG_V2(ctypes.Structure):
    pass


NVVIOCONFIG_V2 = _NVVIOCONFIG_V2


class _NVVIOCONFIG_V3(ctypes.Structure):
    pass


NVVIOCONFIG_V3 = _NVVIOCONFIG_V3


class NVVIOTOPOLOGYTARGET(ctypes.Structure):
    pass


class _NV_VIO_TOPOLOGY(ctypes.Structure):
    pass


NV_VIO_TOPOLOGY = _NV_VIO_TOPOLOGY
NVVIOTOPOLOGY = _NV_VIO_TOPOLOGY


class _NVVIOPCIINFO(ctypes.Structure):
    pass


NVVIOPCIINFO_V1 = _NVVIOPCIINFO


class _NVAPI_STEREO_CAPS(ctypes.Structure):
    pass


NVAPI_STEREO_CAPS_V1 = _NVAPI_STEREO_CAPS


class _NVDRS_GPU_SUPPORT(ctypes.Structure):
    pass


NVDRS_GPU_SUPPORT = _NVDRS_GPU_SUPPORT


class _NVDRS_BINARY_SETTING(ctypes.Structure):
    pass


NVDRS_BINARY_SETTING = _NVDRS_BINARY_SETTING


class _NVDRS_SETTING_VALUES(ctypes.Structure):
    pass


NVDRS_SETTING_VALUES = _NVDRS_SETTING_VALUES


class _NVDRS_SETTING_V1(ctypes.Structure):
    pass


NVDRS_SETTING_V1 = _NVDRS_SETTING_V1


class _NVDRS_APPLICATION_V1(ctypes.Structure):
    pass


NVDRS_APPLICATION_V1 = _NVDRS_APPLICATION_V1


class _NVDRS_APPLICATION_V2(ctypes.Structure):
    pass


NVDRS_APPLICATION_V2 = _NVDRS_APPLICATION_V2


class _NVDRS_APPLICATION_V3(ctypes.Structure):
    pass


NVDRS_APPLICATION_V3 = _NVDRS_APPLICATION_V3


class _NVDRS_APPLICATION_V4(ctypes.Structure):
    pass


NVDRS_APPLICATION_V4 = _NVDRS_APPLICATION_V4


class _NVDRS_PROFILE_V1(ctypes.Structure):
    pass


NVDRS_PROFILE_V1 = _NVDRS_PROFILE_V1


class NV_CHIPSET_INFO_v4(ctypes.Structure):
    pass


class NV_CHIPSET_INFO_v3(ctypes.Structure):
    pass


class NV_CHIPSET_INFO_v2(ctypes.Structure):
    pass


class NV_CHIPSET_INFO_v1(ctypes.Structure):
    pass


class NV_LID_DOCK_PARAMS(ctypes.Structure):
    pass


from .nvapi_lite_d3dext_h import *  # NOQA
from .nvapi_lite_surround_h import *  # NOQA
from .nvapi_lite_common_h import *  # NOQA
from .nvapi_lite_sli_h import *  # NOQA
from .nvapi_lite_stereo_h import *  # NOQA

#
# /////////////////////////////////////////////////////////////////////////////
# Date: Nov 15, 2019
# File: nvapi.h
# NvAPI provides an interface to NVIDIA devices. This file contains the
# interface constants, structure definitions and function prototypes.
# Target Profile: developer
# Target Platform: windows
# /////////////////////////////////////////////////////////////////////////////


# == == == == == == == == == == == == == == == == == == == == == == == ==
# == ==
# Universal NvAPI Definitions
# == == == == == == == == == == == == == == == == == == == == == == == ==
# == ==


# not @}
# not \ingroup nvapistatus
# not < Fix typo in error code


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Initialize
# not This function initializes the NvAPI library
# (if not already initialized) but always increments the ref-counter.
# not This must be called before calling other NvAPI_ functions.
# not Note: It is now mandatory to call NvAPI_Initialize before calling
# any other NvAPI.
# not NvAPI_Unload should be called to unload the NVAPI Library.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 80
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not   specific meaning for this API, they are listed below.
# not \retval NVAPI_LIBRARY_NOT_FOUND Failed to load the NVAPI support
# library
# not \sa nvapistatus
# not \ingroup nvapifunctions
# ///////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_Initialize();
NvAPI_Initialize = hDll.Initialize
NvAPI_Initialize.restype = NVAPI_INTERFACE

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Unload
# not DESCRIPTION: Decrements the ref-counter and when it reaches ZERO,
# unloads NVAPI library.
# not    This must be called in pairs with NvAPI_Initialize.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not  If the client wants unload functionality, it is recommended to
# always call NvAPI_Initialize and NvAPI_Unload in pairs.
# not
# not Unloading NvAPI library is not supported when the library is in a
# resource locked state.
# not Some functions in the NvAPI library initiates an operation or
# allocates certain resources
# not and there are corresponding functions available, to complete the
# operation or free the
# not allocated resources. All such function pairs are designed to prevent
# unloading NvAPI library.
# not
# not For example, if NvAPI_Unload is called after NvAPI_XXX which locks a
# resource, it fails with
# not NVAPI_ERROR. Developers need to call the corresponding NvAPI_YYY to
# unlock the resources,
# not before calling NvAPI_Unload again.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not   specific meaning for this API, they are listed below.
# not \retval NVAPI_API_IN_USE  Atleast an API is still being called hence
# cannot unload requested driver.
# not
# not \ingroup nvapifunctions
# ///////////////////////////////////////////////////////////////////////
NvAPI_Unload = hDll.Unload
NvAPI_Unload.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Unload();

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetErrorMessage
# not This function converts an NvAPI error code into a null terminated
# string.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 80
# not
# not \param nr The error code to convert
# not \param szDesc The string corresponding to the error code
# not
# not \return NULL terminated string (always, never NULL)
# not \ingroup nvapifunctions
# ///////////////////////////////////////////////////////////////////////
NvAPI_GetErrorMessage = hDll.GetErrorMessage
NvAPI_GetErrorMessage.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GetErrorMessage(NvAPI_Status nr,NvAPI_ShortString szDesc);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetInterfaceVersionString
# not This function returns a string describing the version of the NvAPI
# library.
# not   The contents of the string are human readable. Do not assume a
# fixed
# not    format.
# not
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 80
# not
# not \param szDesc User readable string giving NvAPI version information
# not
# not \return See \ref nvapistatus for the list of possible return values.
# not \ingroup nvapifunctions
# ///////////////////////////////////////////////////////////////////////
NvAPI_GetInterfaceVersionString = hDll.GetInterfaceVersionString
NvAPI_GetInterfaceVersionString.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GetInterfaceVersionString(NvAPI_ShortString szDesc);

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# All display port related data types definition starts
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# This category is intentionally added before the ifdef. The endif should
# also be in the same scope

# not /ingroup dispcontrol
# not Used in NV_DISPLAY_PORT_INFO.
class _NV_DP_LINK_RATE(ENUM):
    NV_DP_1_62GBPS = 6
    NV_DP_2_70GBPS = 0xA
    NV_DP_5_40GBPS = 0x14
    NV_DP_8_10GBPS = 0x1E


NV_DP_LINK_RATE = _NV_DP_LINK_RATE


# not \ingroup dispcontrol
# not Used in NV_DISPLAY_PORT_INFO.
class _NV_DP_LANE_COUNT(ENUM):
    NV_DP_1_LANE = 1
    NV_DP_2_LANE = 2
    NV_DP_4_LANE = 4


NV_DP_LANE_COUNT = _NV_DP_LANE_COUNT


# not \ingroup dispcontrol
# not Used in NV_DISPLAY_PORT_INFO.
class _NV_DP_COLOR_FORMAT(ENUM):
    NV_DP_COLOR_FORMAT_RGB = 0
    NV_DP_COLOR_FORMAT_YCbCr422 = 1
    NV_DP_COLOR_FORMAT_YCbCr444 = 2


NV_DP_COLOR_FORMAT = _NV_DP_COLOR_FORMAT


# not \ingroup dispcontrol
# not Used in NV_DISPLAY_PORT_INFO.
class _NV_DP_COLORIMETRY(ENUM):
    NV_DP_COLORIMETRY_RGB = 0
    NV_DP_COLORIMETRY_YCbCr_ITU601 = 1
    NV_DP_COLORIMETRY_YCbCr_ITU709 = 2


NV_DP_COLORIMETRY = _NV_DP_COLORIMETRY


# not \ingroup dispcontrol
# not Used in NV_DISPLAY_PORT_INFO.
class _NV_DP_DYNAMIC_RANGE(ENUM):
    NV_DP_DYNAMIC_RANGE_VESA = 0
    NV_DP_DYNAMIC_RANGE_CEA = 1


NV_DP_DYNAMIC_RANGE = _NV_DP_DYNAMIC_RANGE


# not \ingroup dispcontrol
# not Used in NV_DISPLAY_PORT_INFO.
class _NV_DP_BPC(ENUM):
    NV_DP_BPC_DEFAULT = 0
    NV_DP_BPC_6 = 1
    NV_DP_BPC_8 = 2
    NV_DP_BPC_10 = 3
    NV_DP_BPC_12 = 4
    NV_DP_BPC_16 = 5


NV_DP_BPC = _NV_DP_BPC

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# All display port related data types definitions end
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetEDID
# not \fn
# NvAPI_GPU_GetEDID(NvPhysicalGpuHandle hPhysicalGpu, NvU32 displayOutputId, NV_EDID *pEDID)
#
# not This function returns the EDID data for the specified GPU handle and
# connection bit mask.
# not displayOutputId should have exactly 1 bit set to indicate a single
# display. See \ref handles.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 85
# not
# not \retval NVAPI_INVALID_ARGUMENT   pEDID is NULL; displayOutputId has
# 0 or > 1 bits set
# not \retval NVAPI_OK     *pEDID contains valid data.
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found.
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle.
# not \retval NVAPI_DATA_NOT_FOUND   The requested display does not
# contain an EDID.
# ///////////////////////////////////////////////////////////////////////
# not \ingroup gpu
# not @{
NV_EDID_V1_DATA_SIZE = 256
NV_EDID_DATA_SIZE = NV_EDID_V1_DATA_SIZE

NV_EDID_V1._fields_ = [
    # structure version
    ('version', NvU32),
    ('EDID_Data', NvU8 * NV_EDID_DATA_SIZE),
]

# not Used in NvAPI_GPU_GetEDID()
NV_EDID_V2._fields_ = [
    # not < Structure version
    ('version', NvU32),
    ('EDID_Data', NvU8 * NV_EDID_DATA_SIZE),
    ('(ctypes.sizeofEDID', NvU32),
]

# not Used in NvAPI_GPU_GetEDID()
NV_EDID_V3._fields_ = [
    # not < Structure version
    ('version', NvU32),
    ('EDID_Data', NvU8 * NV_EDID_DATA_SIZE),
    ('(ctypes.sizeofEDID', NvU32),
    # not < ID which always returned in a monotonically increasing counter.
    ('edidId', NvU32),
    # not < Which 256-byte page of the EDID we want to read. Start at 0.
    ('offset', NvU32),
]

NV_EDID = NV_EDID_V3
NV_EDID_VER1 = MAKE_NVAPI_VERSION(NV_EDID_V1, 1)
NV_EDID_VER2 = MAKE_NVAPI_VERSION(NV_EDID_V2, 2)
NV_EDID_VER3 = MAKE_NVAPI_VERSION(NV_EDID_V3, 3)
NV_EDID_VER = NV_EDID_VER3
# not @}
# not \ingroup gpu
NvAPI_GPU_GetEDID = hDll.GPU_GetEDID
NvAPI_GPU_GetEDID.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GPU_GetEDID(NvPhysicalGpuHandle hPhysicalGpu, NvU32 displayOutputId, NV_EDID *pEDID);


# not \ingroup gpu
# not Used in NV_GPU_CONNECTOR_DATA
class _NV_GPU_CONNECTOR_TYPE(ENUM):
    NVAPI_GPU_CONNECTOR_VGA_15_PIN = 0x00000000
    NVAPI_GPU_CONNECTOR_TV_COMPOSITE = 0x00000010
    NVAPI_GPU_CONNECTOR_TV_SVIDEO = 0x00000011
    NVAPI_GPU_CONNECTOR_TV_HDTV_COMPONENT = 0x00000013
    NVAPI_GPU_CONNECTOR_TV_SCART = 0x00000014
    NVAPI_GPU_CONNECTOR_TV_COMPOSITE_SCART_ON_EIAJ4120 = 0x00000016
    NVAPI_GPU_CONNECTOR_TV_HDTV_EIAJ4120 = 0x00000017
    NVAPI_GPU_CONNECTOR_PC_POD_HDTV_YPRPB = 0x00000018
    NVAPI_GPU_CONNECTOR_PC_POD_SVIDEO = 0x00000019
    NVAPI_GPU_CONNECTOR_PC_POD_COMPOSITE = 0x0000001A
    NVAPI_GPU_CONNECTOR_DVI_I_TV_SVIDEO = 0x00000020
    NVAPI_GPU_CONNECTOR_DVI_I_TV_COMPOSITE = 0x00000021
    NVAPI_GPU_CONNECTOR_DVI_I = 0x00000030
    NVAPI_GPU_CONNECTOR_DVI_D = 0x00000031
    NVAPI_GPU_CONNECTOR_ADC = 0x00000032
    NVAPI_GPU_CONNECTOR_LFH_DVI_I_1 = 0x00000038
    NVAPI_GPU_CONNECTOR_LFH_DVI_I_2 = 0x00000039
    NVAPI_GPU_CONNECTOR_SPWG = 0x00000040
    NVAPI_GPU_CONNECTOR_OEM = 0x00000041
    NVAPI_GPU_CONNECTOR_DISPLAYPORT_EXTERNAL = 0x00000046
    NVAPI_GPU_CONNECTOR_DISPLAYPORT_INTERNAL = 0x00000047
    NVAPI_GPU_CONNECTOR_DISPLAYPORT_MINI_EXT = 0x00000048
    NVAPI_GPU_CONNECTOR_HDMI_A = 0x00000061
    NVAPI_GPU_CONNECTOR_HDMI_C_MINI = 0x00000063
    NVAPI_GPU_CONNECTOR_LFH_DISPLAYPORT_1 = 0x00000064
    NVAPI_GPU_CONNECTOR_LFH_DISPLAYPORT_2 = 0x00000065
    NVAPI_GPU_CONNECTOR_VIRTUAL_WFD = 0x00000070
    NVAPI_GPU_CONNECTOR_USB_C = 0x00000071
    NVAPI_GPU_CONNECTOR_UNKNOWN = 0xFFFFFFFF


NV_GPU_CONNECTOR_TYPE = _NV_GPU_CONNECTOR_TYPE


# ////////////////////////////////////////////////////////////////////////
# NvAPI_TVOutput Information
# ///////////////////////////////////////////////////////////////////////
# not \ingroup tvapi
# not Used in NV_DISPLAY_TV_OUTPUT_INFO
class _NV_DISPLAY_TV_FORMAT(ENUM):
    NV_DISPLAY_TV_FORMAT_NONE = 0
    NV_DISPLAY_TV_FORMAT_SD_NTSCM = 0x00000001
    NV_DISPLAY_TV_FORMAT_SD_NTSCJ = 0x00000002
    NV_DISPLAY_TV_FORMAT_SD_PALM = 0x00000004
    NV_DISPLAY_TV_FORMAT_SD_PALBDGH = 0x00000008
    NV_DISPLAY_TV_FORMAT_SD_PALN = 0x00000010
    NV_DISPLAY_TV_FORMAT_SD_PALNC = 0x00000020
    NV_DISPLAY_TV_FORMAT_SD_576i = 0x00000100
    NV_DISPLAY_TV_FORMAT_SD_480i = 0x00000200
    NV_DISPLAY_TV_FORMAT_ED_480p = 0x00000400
    NV_DISPLAY_TV_FORMAT_ED_576p = 0x00000800
    NV_DISPLAY_TV_FORMAT_HD_720p = 0x00001000
    NV_DISPLAY_TV_FORMAT_HD_1080i = 0x00002000
    NV_DISPLAY_TV_FORMAT_HD_1080p = 0x00004000
    NV_DISPLAY_TV_FORMAT_HD_720p50 = 0x00008000
    NV_DISPLAY_TV_FORMAT_HD_1080p24 = 0x00010000
    NV_DISPLAY_TV_FORMAT_HD_1080i50 = 0x00020000
    NV_DISPLAY_TV_FORMAT_HD_1080p50 = 0x00040000
    NV_DISPLAY_TV_FORMAT_UHD_4Kp30 = 0x00080000
    NV_DISPLAY_TV_FORMAT_UHD_4Kp30_3840 = NV_DISPLAY_TV_FORMAT_UHD_4Kp30
    NV_DISPLAY_TV_FORMAT_UHD_4Kp25 = 0x00100000
    NV_DISPLAY_TV_FORMAT_UHD_4Kp25_3840 = NV_DISPLAY_TV_FORMAT_UHD_4Kp25
    NV_DISPLAY_TV_FORMAT_UHD_4Kp24 = 0x00200000
    NV_DISPLAY_TV_FORMAT_UHD_4Kp24_3840 = NV_DISPLAY_TV_FORMAT_UHD_4Kp24
    NV_DISPLAY_TV_FORMAT_UHD_4Kp24_SMPTE = 0x00400000
    NV_DISPLAY_TV_FORMAT_UHD_4Kp50_3840 = 0x00800000
    NV_DISPLAY_TV_FORMAT_UHD_4Kp60_3840 = 0x00900000
    NV_DISPLAY_TV_FORMAT_UHD_4Kp30_4096 = 0x00A00000
    NV_DISPLAY_TV_FORMAT_UHD_4Kp25_4096 = 0x00B00000
    NV_DISPLAY_TV_FORMAT_UHD_4Kp24_4096 = 0x00C00000
    NV_DISPLAY_TV_FORMAT_UHD_4Kp50_4096 = 0x00D00000
    NV_DISPLAY_TV_FORMAT_UHD_4Kp60_4096 = 0x00E00000
    NV_DISPLAY_TV_FORMAT_SD_OTHER = 0x01000000
    NV_DISPLAY_TV_FORMAT_ED_OTHER = 0x02000000
    NV_DISPLAY_TV_FORMAT_HD_OTHER = 0x04000000
    NV_DISPLAY_TV_FORMAT_ANY = 0x80000000


NV_DISPLAY_TV_FORMAT = _NV_DISPLAY_TV_FORMAT

# not \ingroup dispcontrol
# not @{
NVAPI_MAX_VIEW_TARGET = 2
NVAPI_ADVANCED_MAX_VIEW_TARGET = 4


# not Used in NvAPI_SetView().
class _NV_TARGET_VIEW_MODE(ENUM):
    NV_VIEW_MODE_STANDARD = 0
    NV_VIEW_MODE_CLONE = 1
    NV_VIEW_MODE_HSPAN = 2
    NV_VIEW_MODE_VSPAN = 3
    NV_VIEW_MODE_DUALVIEW = 4
    NV_VIEW_MODE_MULTIVIEW = 5


NV_TARGET_VIEW_MODE = _NV_TARGET_VIEW_MODE


# not @}
# Following definitions are used in NvAPI_SetViewEx.
# not Scaling modes - used in NvAPI_SetViewEx().
# not \ingroup dispcontrol
class _NV_SCALING(ENUM):
    NV_SCALING_DEFAULT = 0
    NV_SCALING_GPU_SCALING_TO_CLOSEST = 1
    NV_SCALING_GPU_SCALING_TO_NATIVE = 2
    NV_SCALING_GPU_SCANOUT_TO_NATIVE = 3
    NV_SCALING_GPU_SCALING_TO_ASPECT_SCANOUT_TO_NATIVE = 5
    NV_SCALING_GPU_SCALING_TO_ASPECT_SCANOUT_TO_CLOSEST = 6
    NV_SCALING_GPU_SCANOUT_TO_CLOSEST = 7
    NV_SCALING_GPU_INTEGER_ASPECT_SCALING = 8
    NV_SCALING_MONITOR_SCALING = NV_SCALING_GPU_SCALING_TO_CLOSEST
    NV_SCALING_ADAPTER_SCALING = NV_SCALING_GPU_SCALING_TO_NATIVE
    NV_SCALING_CENTERED = NV_SCALING_GPU_SCANOUT_TO_NATIVE
    NV_SCALING_ASPECT_SCALING = (
        NV_SCALING_GPU_SCALING_TO_ASPECT_SCANOUT_TO_NATIVE
    )
    NV_SCALING_CUSTOMIZED = 255


NV_SCALING = _NV_SCALING


# not Rotate modes- used in NvAPI_SetViewEx().
# not \ingroup dispcontrol
class _NV_ROTATE(ENUM):
    NV_ROTATE_0 = 0
    NV_ROTATE_90 = 1
    NV_ROTATE_180 = 2
    NV_ROTATE_270 = 3
    NV_ROTATE_IGNORED = 4


NV_ROTATE = _NV_ROTATE


# not Color formats- used in NvAPI_SetViewEx().
# not \ingroup dispcontrol
def NVFORMAT_MAKEFOURCC(ch0, ch1, ch2, ch3):
    return ch0 | ch1 << 8 | ch2 << 16 | ch3 << 24


# not Color formats- used in NvAPI_SetViewEx().
# not \ingroup dispcontrol
class _NV_FORMAT(ENUM):
    NV_FORMAT_UNKNOWN = 0
    NV_FORMAT_P8 = 41
    NV_FORMAT_R5G6B5 = 23
    NV_FORMAT_A8R8G8B8 = 21
    NV_FORMAT_A16B16G16R16F = 113


NV_FORMAT = _NV_FORMAT

# TV standard
NV_VIEWPORTF._fields_ = [
    # not < x-coordinate of the viewport top-left point
    ('x', FLOAT),
    # not < y-coordinate of the viewport top-left point
    ('y', FLOAT),
    # not < Width of the viewport
    ('w', FLOAT),
    # not < Height of the viewport
    ('h', FLOAT),
]


# not \ingroup dispcontrol
# not The timing override is not supported yet; must be set to _AUTO. \n
class _NV_TIMING_OVERRIDE(ENUM):
    NV_TIMING_OVERRIDE_CURRENT = 0
    NV_TIMING_OVERRIDE_AUTO = 1
    NV_TIMING_OVERRIDE_EDID = 2
    NV_TIMING_OVERRIDE_DMT = 3
    NV_TIMING_OVERRIDE_DMT_RB = 4
    NV_TIMING_OVERRIDE_CVT = 5
    NV_TIMING_OVERRIDE_CVT_RB = 6
    NV_TIMING_OVERRIDE_GTF = 7
    NV_TIMING_OVERRIDE_EIA861 = 8
    NV_TIMING_OVERRIDE_ANALOG_TV = 9
    NV_TIMING_OVERRIDE_CUST = 10
    NV_TIMING_OVERRIDE_NV_PREDEFINED = 11
    NV_TIMING_OVERRIDE_NV_PSF = NV_TIMING_OVERRIDE_NV_PREDEFINED
    NV_TIMING_OVERRIDE_NV_ASPR = 12
    NV_TIMING_OVERRIDE_SDI = 13
    NV_TIMING_OVRRIDE_MAX = 14


NV_TIMING_OVERRIDE = _NV_TIMING_OVERRIDE

# **********************
# The Timing Structure
# **********************
# not \ingroup dispcontrol
# not NVIDIA-specific timing extras \n
# not Used in NV_TIMING.
tagNV_TIMINGEXT._fields_ = [
    # not < Reserved for NVIDIA hardware-based enhancement, such as
    # double-scan.
    ('flag', NvU32),
    # not < Logical refresh rate to present
    ('rr', NvU16),
    # not < Physical vertical refresh rate in 0.001Hz
    ('rrx1k', NvU32),
    # not < Display aspect ratio Hi(aspect):horizontal-aspect,
    # Low(aspect):vertical-aspect
    ('aspect', NvU32),
    # not < Bit-wise pixel repetition factor: 0x1:no pixel repetition;
    # 0x2:each pixel repeats twice horizontally,..
    ('rep', NvU16),
    # not < Timing standard
    ('status', NvU32),
    # not < Timing name
    ('name', NvU8 * 40),
]

# not \ingroup dispcontrol
# not The very basic timing structure based on the VESA standard:
# not \code
# not   | <
# ----------------------------htotal--------------------------.|
# not   ---------"active" video-------. | < -------blanking-----. | <
# -----
# not   | < -------hvisible-------. | < -hb. | < -hfp. | < -hsw. | <
# -hbp. | < -hb.|
# not --------- - + -------------------------+ |  |  |  | |
# not A A |     | |  |  |  | |
# not : : |     | |  |  |  | |
# not : : |     | |  |  |  | |
# not :vertical| addressable video | |  |  |  | |
# not : visible|     | |  |  |  | |
# not : : |     | |  |  |  | |
# not : : |     | |  |  |  | |
# not vertical V |     | |  |  |  | |
# not total -- + -------------------------+ |  |  |  | |
# not : vb  border   |  |  |  | |
# not : -----------------------------------+  |  |  | |
# not : vfp  front porch    |  |  | |
# not : -------------------------------------------+  |  | |
# not : vsw  sync width     |  | |
# not : ---------------------------------------------------+  | |
# not : vbp  back porch       | |
# not : -----------------------------------------------------------+ |
# not V vb  border         |
# not
# ---------------------------------------------------------------------------+
#
# not \endcode
_NV_TIMING._fields_ = [
    # not < horizontal visible
    ('HVisible', NvU16),
    # not < horizontal border
    ('HBorder', NvU16),
    # not < horizontal front porch
    ('HFrontPorch', NvU16),
    # not < horizontal sync width
    ('HSyncWidth', NvU16),
    # not < horizontal total
    ('HTotal', NvU16),
    # not < horizontal sync polarity: 1-negative, 0-positive
    ('HSyncPol', NvU8),
    # not < vertical visible
    ('VVisible', NvU16),
    # not < vertical border
    ('VBorder', NvU16),
    # not < vertical front porch
    ('VFrontPorch', NvU16),
    # not < vertical sync width
    ('VSyncWidth', NvU16),
    # not < vertical total
    ('VTotal', NvU16),
    # not < vertical sync polarity: 1-negative, 0-positive
    ('VSyncPol', NvU8),
    # not < 1-interlaced, 0-progressive
    ('interlaced', NvU16),
    # not < pixel clock in 10 kHz
    ('pclk', NvU32),
    # other timing related extras
    ('etc', NV_TIMINGEXT),
]

# not \addtogroup dispcontrol
# not Timing-related constants
# not @{
NV_TIMING_H_SYNC_POSITIVE = 0
NV_TIMING_H_SYNC_NEGATIVE = 1
NV_TIMING_H_SYNC_DEFAULT = NV_TIMING_H_SYNC_NEGATIVE
NV_TIMING_V_SYNC_POSITIVE = 0
NV_TIMING_V_SYNC_NEGATIVE = 1
NV_TIMING_V_SYNC_DEFAULT = NV_TIMING_V_SYNC_POSITIVE
NV_TIMING_PROGRESSIVE = 0
NV_TIMING_INTERLACED = 1
NV_TIMING_INTERLACED_EXTRA_VBLANK_ON_FIELD2 = 1
NV_TIMING_INTERLACED_NO_EXTRA_VBLANK_ON_FIELD2 = 2


# not @}
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_SetView
# not \fn
# NvAPI_SetView(NvDisplayHandle hNvDisplay, NV_VIEW_TARGET_INFO *pTargetInfo, NV_TARGET_VIEW_MODE targetView)
#
# not This function lets the caller modify the target display arrangement
# of the selected source display handle in any nView mode.
# not It can also modify or extend the source display in Dualview mode.
# not \note Maps the selected source to the associated target Ids.
# not \note Display PATH with this API is limited to single GPU. DUALVIEW
# across GPUs cannot be enabled with this API.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_DISP_SetDisplayConfig.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 90
# not
# not \param [in] hNvDisplay  NVIDIA Display selection.
# NVAPI_DEFAULT_HANDLE is not allowed, it has to be a handle enumerated
# with NvAPI_EnumNVidiaDisplayHandle().
# not \param [in] pTargetInfo Pointer to array of NV_VIEW_TARGET_INFO,
# specifying device properties in this view.
# not      The first device entry in the array is the physical primary.
# not      The device entry with the lowest source id is the desktop
# primary.
# not \param [in] targetCount Count of target devices specified in
# pTargetInfo.
# not \param [in] targetView  Target view selected from
# NV_TARGET_VIEW_MODE.
# not
# not \retval NVAPI_OK   Completed request
# not \retval NVAPI_ERROR  Miscellaneous error occurred
# not \retval NVAPI_INVALID_ARGUMENT Invalid input parameter.
# ///////////////////////////////////////////////////////////////////////
# not \ingroup dispcontrol
# not Used in NvAPI_SetView() and NvAPI_GetView()

class target(ctypes.Structure):
    pass


target._fields_ = [
    # not < (IN/OUT) Device mask
    ('deviceMask', NvU32),
    # not < (IN/OUT) Source ID - values will be based on the number of
    # heads exposed per GPU.
    ('sourceId', NvU32),
    # not < (OUT) Indicates if this is the GPU's primary view target. This
    # is not the desktop GDI primary.
    ('bPrimary', NvU32, 1),
    # not < (IN/OUT) Indicates if the timing being used on this monitor is
    # interlaced.
    ('bInterlaced', NvU32, 1),
    # not < (IN/OUT) Indicates if this is the desktop GDI primary.
    ('bGDIPrimary', NvU32, 1),
    # not < (IN) Used only on Win7 and higher during a call to
    # NvAPI_SetView(). Turns off optimization & forces OS to set supplied
    # mode.
    ('bForceModeSet', NvU32, 1),
]
NV_VIEW_TARGET_INFO.target = target

NV_VIEW_TARGET_INFO._fields_ = [
    # not < (IN) structure version
    ('version', NvU32),
    # not < (IN) target count
    ('count', NvU32),
    ('target', NV_VIEW_TARGET_INFO.target * NVAPI_MAX_VIEW_TARGET),
]

# not \ingroup dispcontrol
NV_VIEW_TARGET_INFO_VER = MAKE_NVAPI_VERSION(NV_VIEW_TARGET_INFO, 2)

# not \ingroup dispcontrol
NvAPI_SetView = hDll.SetView
NvAPI_SetView.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_SetView(NvDisplayHandle hNvDisplay, NV_VIEW_TARGET_INFO *pTargetInfo, NV_TARGET_VIEW_MODE targetView);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_SetViewEx
# not \fn
# NvAPI_SetViewEx(NvDisplayHandle hNvDisplay, NV_DISPLAY_PATH_INFO *pPathInfo, NV_TARGET_VIEW_MODE displayView)
#
# not This function lets caller to modify the display arrangement for
# selected source display handle in any of the nview modes.
# not It also allows to modify or extend the source display in dualview
# mode.
# not \note Maps the selected source to the associated target Ids.
# not \note Display PATH with this API is limited to single GPU. DUALVIEW
# across GPUs cannot be enabled with this API.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_DISP_SetDisplayConfig.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 95
# not
# not \param [in] hNvDisplay NVIDIA Display selection.
# NVAPI_DEFAULT_HANDLE is not allowed, it has to be a handle enumerated
# with
# not     NvAPI_EnumNVidiaDisplayHandle().
# not \param [in] pPathInfo Pointer to array of NV_VIEW_PATH_INFO,
# specifying device properties in this view.
# not     The first device entry in the array is the physical primary.
# not     The device entry with the lowest source id is the desktop
# primary.
# not \param [in] pathCount Count of paths specified in pPathInfo.
# not \param [in] displayView Display view selected from
# NV_TARGET_VIEW_MODE.
# not
# not \retval NVAPI_OK   Completed request
# not \retval NVAPI_ERROR   Miscellaneous error occurred
# not \retval NVAPI_INVALID_ARGUMENT Invalid input parameter.
# ///////////////////////////////////////////////////////////////////////
# not \ingroup dispcontrol
NVAPI_MAX_DISPLAY_PATH = NVAPI_MAX_VIEW_TARGET

# not \ingroup dispcontrol
NVAPI_ADVANCED_MAX_DISPLAY_PATH = NVAPI_ADVANCED_MAX_VIEW_TARGET

# not \ingroup dispcontrol
# not Used in NV_DISPLAY_PATH_INFO.
NV_DISPLAY_PATH._fields_ = [
    # not < (IN) Device mask
    ('deviceMask', NvU32),
    # not < (IN) Values will be based on the number of heads exposed per
    # GPU(0, 1?)
    ('sourceId', NvU32),
    # not < (IN/OUT) Indicates if this is the GPU's primary view target.
    # This is not the desktop GDI primary.
    ('bPrimary', NvU32, 1),
    # not < (IN) Specify connector type. For TV only.
    ('connector', NV_GPU_CONNECTOR_TYPE),
    # not < (IN) Width of the mode
    ('width', NvU32),
    # not < (IN) Height of the mode
    ('height', NvU32),
    # not < (IN) Depth of the mode
    ('depth', NvU32),
    # not < Color format if it needs to be specified. Not used now.
    ('colorFormat', NV_FORMAT),
    # not < (IN) Rotation setting.
    ('rotation', NV_ROTATE),
    # not < (IN) Scaling setting
    ('scaling', NV_SCALING),
    # not < (IN) Refresh rate of the mode
    ('refreshRate', NvU32),
    # not < (IN) Interlaced mode flag
    ('interlaced', NvU32, 1),
    # not < (IN) To choose the last TV format set this value to
    # NV_DISPLAY_TV_FORMAT_NONE
    ('tvFormat', NV_DISPLAY_TV_FORMAT),
    # not < (IN/OUT) X-offset of this display on the Windows desktop
    ('posx', NvU32),
    # not < (IN/OUT) Y-offset of this display on the Windows desktop
    ('posy', NvU32),
    # not < (IN/OUT) Indicates if this is the desktop GDI primary.
    ('bGDIPrimary', NvU32, 1),
    # not < (IN) Used only on Win7 and higher during a call to
    # NvAPI_SetViewEx(). Turns off optimization & forces OS to set
    # supplied mode.
    ('bForceModeSet', NvU32, 1),
    # not < (IN) If set, this display path should have the focus after the
    # GPU topology change
    ('bFocusDisplay', NvU32, 1),
    # not < (IN) the physical display/target Gpu id which is the owner of
    # the scan out (for SLI multimon, display from the slave Gpu)
    ('gpuId', NvU32, 24),
]

# not \ingroup dispcontrol
# not Used in NvAPI_SetViewEx() and NvAPI_GetViewEx().
NV_DISPLAY_PATH_INFO_V3._fields_ = [
    # not < (IN) Structure version
    ('version', NvU32),
    # not < (IN) Path count
    ('count', NvU32),
    ('path', NV_DISPLAY_PATH * NVAPI_MAX_DISPLAY_PATH),
]

# not \ingroup dispcontrol
# not Used in NvAPI_SetViewEx() and NvAPI_GetViewEx().
NV_DISPLAY_PATH_INFO._fields_ = [
    # not < (IN) Structure version
    ('version', NvU32),
    # not < (IN) Path count
    ('count', NvU32),
    ('path', NV_DISPLAY_PATH * NVAPI_ADVANCED_MAX_DISPLAY_PATH),
]

# not \addtogroup dispcontrol
# not Macro for constructing the version fields of NV_DISPLAY_PATH_INFO
# not @{
NV_DISPLAY_PATH_INFO_VER4 = MAKE_NVAPI_VERSION(NV_DISPLAY_PATH_INFO, 4)
NV_DISPLAY_PATH_INFO_VER3 = MAKE_NVAPI_VERSION(NV_DISPLAY_PATH_INFO, 3)
NV_DISPLAY_PATH_INFO_VER2 = MAKE_NVAPI_VERSION(NV_DISPLAY_PATH_INFO, 2)
NV_DISPLAY_PATH_INFO_VER1 = MAKE_NVAPI_VERSION(NV_DISPLAY_PATH_INFO, 1)
NV_DISPLAY_PATH_INFO_VER = NV_DISPLAY_PATH_INFO_VER4

# not @}
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_SetViewEx
# not \fn
# NvAPI_SetViewEx(NvDisplayHandle hNvDisplay, NV_DISPLAY_PATH_INFO *pPathInfo, NV_TARGET_VIEW_MODE displayView)
#
# not This function lets caller to modify the display arrangement for
# selected source display handle in any of the nview modes.
# not It also allows to modify or extend the source display in dualview
# mode.
# not \note Maps the selected source to the associated target Ids.
# not \note Display PATH with this API is limited to single GPU. DUALVIEW
# across GPUs cannot be enabled with this API.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_DISP_SetDisplayConfig.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 95
# not
# not \param [in] hNvDisplay NVIDIA Display selection.
# NVAPI_DEFAULT_HANDLE is not allowed, it has to be a handle enumerated
# with
# not     NvAPI_EnumNVidiaDisplayHandle().
# not \param [in] pPathInfo Pointer to array of NV_VIEW_PATH_INFO,
# specifying device properties in this view.
# not     The first device entry in the array is the physical primary.
# not     The device entry with the lowest source id is the desktop
# primary.
# not \param [in] pathCount Count of paths specified in pPathInfo.
# not \param [in] displayView Display view selected from
# NV_TARGET_VIEW_MODE.
# not
# not \retval NVAPI_OK   Completed request
# not \retval NVAPI_ERROR   Miscellaneous error occurred
# not \retval NVAPI_INVALID_ARGUMENT Invalid input parameter.
# ///////////////////////////////////////////////////////////////////////
# not \ingroup dispcontrol
NvAPI_SetViewEx = hDll.SetViewEx
NvAPI_SetViewEx.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_SetViewEx(NvDisplayHandle hNvDisplay, NV_DISPLAY_PATH_INFO *pPathInfo, NV_TARGET_VIEW_MODE displayView);


# ///////////////////////////////////////////////////////////////////////
# SetDisplayConfig/GetDisplayConfig
# ///////////////////////////////////////////////////////////////////////
# not \ingroup dispcontrol
_NV_POSITION._fields_ = [
    ('x', NvS32),
    ('y', NvS32),
]

# not \ingroup dispcontrol
_NV_RESOLUTION._fields_ = [
    ('width', NvU32),
    ('height', NvU32),
    ('colorDepth', NvU32),
]

# not \ingroup dispcontrol
_TEMP__NV_DISPLAYCONFIG_PATH_ADVANCED_TARGET_INFO_V1 = [
    ('version', NvU32),
    # not < (IN) rotation setting.
    ('rotation', NV_ROTATE),
    # not < (IN) scaling setting.
    ('scaling', NV_SCALING),
    # not < (IN) Non-interlaced Refresh Rate of the mode, multiplied by
    # 1000, 0 = ignored
    ('refreshRate1K', NvU32),
    # not < (IN) Interlaced mode flag, ignored if refreshRate == 0
    ('interlaced', NvU32, 1),
    # not < (IN) Declares primary display in clone configuration. This is
    # *NOT* GDI Primary.
    ('primary', NvU32, 1),
]

_TEMP__NV_DISPLAYCONFIG_PATH_ADVANCED_TARGET_INFO_V1 += [
    # not < Whether on this target Pan and Scan is enabled or has to
    # be enabled. Valid only
    ('isPanAndScanTarget', NvU32, 1),
]

_TEMP__NV_DISPLAYCONFIG_PATH_ADVANCED_TARGET_INFO_V1 += [
    ('disableVirtualModeSupport', NvU32, 1),
    ('isPreferredUnscaledTarget', NvU32, 1),
    ('reserved', NvU32, 27),
    # not < Specify connector type. For TV only, ignored if tvFormat ==
    # NV_DISPLAY_TV_FORMAT_NONE
    ('connector', NV_GPU_CONNECTOR_TYPE),
    # not < (IN) to choose the last TV format set this value to
    # NV_DISPLAY_TV_FORMAT_NONE
    ('tvFormat', NV_DISPLAY_TV_FORMAT),
    # not < Ignored if timingOverride == NV_TIMING_OVERRIDE_CURRENT
    ('timingOverride', NV_TIMING_OVERRIDE),
    # not < Scan out timing, valid only if timingOverride ==
    # NV_TIMING_OVERRIDE_CUST
    ('timing', NV_TIMING),
]
_NV_DISPLAYCONFIG_PATH_ADVANCED_TARGET_INFO_V1._fields_ = _TEMP__NV_DISPLAYCONFIG_PATH_ADVANCED_TARGET_INFO_V1

# not \ingroup dispcontrol
NV_DISPLAYCONFIG_PATH_ADVANCED_TARGET_INFO = NV_DISPLAYCONFIG_PATH_ADVANCED_TARGET_INFO_V1

# not \ingroup dispcontrol
NV_DISPLAYCONFIG_PATH_ADVANCED_TARGET_INFO_VER1 = (
    MAKE_NVAPI_VERSION(NV_DISPLAYCONFIG_PATH_ADVANCED_TARGET_INFO_V1, 1)
)

# not \ingroup dispcontrol
NV_DISPLAYCONFIG_PATH_ADVANCED_TARGET_INFO_VER = (
    NV_DISPLAYCONFIG_PATH_ADVANCED_TARGET_INFO_VER1
)

# not \ingroup dispcontrol
_NV_DISPLAYCONFIG_PATH_TARGET_INFO_V1._fields_ = [
    # not < Display ID
    ('displayId', NvU32),
    # not < May be NULL if no advanced settings are required. NULL for
    # Non-NVIDIA Display.
    ('details', POINTER(NV_DISPLAYCONFIG_PATH_ADVANCED_TARGET_INFO)),
]

# not \ingroup dispcontrol
_NV_DISPLAYCONFIG_PATH_TARGET_INFO_V2._fields_ = [
    # not < Display ID
    ('displayId', NvU32),
    # not < May be NULL if no advanced settings are required
    ('details', POINTER(NV_DISPLAYCONFIG_PATH_ADVANCED_TARGET_INFO)),
    # not < Windows CCD target ID. Must be present only for non-NVIDIA
    # adapter, for NVIDIA adapter this parameter is ignored.
    ('targetId', NvU32),
]

# not \ingroup dispcontrol
# not As version is not defined for this structure, we will be using
# version of NV_DISPLAYCONFIG_PATH_INFO
NV_DISPLAYCONFIG_PATH_TARGET_INFO = NV_DISPLAYCONFIG_PATH_TARGET_INFO_V2


# not \ingroup dispcontrol
class _NV_DISPLAYCONFIG_SPANNING_ORIENTATION(ENUM):
    NV_DISPLAYCONFIG_SPAN_NONE = 0
    NV_DISPLAYCONFIG_SPAN_HORIZONTAL = 1
    NV_DISPLAYCONFIG_SPAN_VERTICAL = 2


NV_DISPLAYCONFIG_SPANNING_ORIENTATION = _NV_DISPLAYCONFIG_SPANNING_ORIENTATION

# not \ingroup dispcontrol
_NV_DISPLAYCONFIG_SOURCE_MODE_INFO_V1._fields_ = [
    ('resolution', NV_RESOLUTION),
    # not < Ignored at present, must be NV_FORMAT_UNKNOWN (0)
    ('colorFormat', NV_FORMAT),
    # not < Is all positions are 0 or invalid, displays will be
    # automatically
    ('position', NV_POSITION),
    # not < Spanning is only supported on XP
    ('spanningOrientation', NV_DISPLAYCONFIG_SPANNING_ORIENTATION),
    ('bGDIPrimary', NvU32, 1),
    ('bSLIFocus', NvU32, 1),
    # not < Must be 0
    ('reserved', NvU32, 30),
]

# not \ingroup dispcontrol
_NV_DISPLAYCONFIG_PATH_INFO_V1._fields_ = [
    ('version', NvU32),
    # not < This field is reserved. There is ongoing debate if we need
    # this field.
    ('reserved_sourceId', NvU32),
    # not < Number of elements in targetInfo array
    ('targetInfoCount', NvU32),
    ('targetInfo', POINTER(NV_DISPLAYCONFIG_PATH_TARGET_INFO_V1)),
    # not < May be NULL if mode info is not important
    ('sourceModeInfo', POINTER(NV_DISPLAYCONFIG_SOURCE_MODE_INFO_V1)),
]

# not \ingroup dispcontrol
# not This define is temporary and must be removed once DVS failure is
# fixed.
_NV_DISPLAYCONFIG_PATH_INFO = _NV_DISPLAYCONFIG_PATH_INFO_V2


# not \ingroup dispcontrol
# not < Identifies sourceId used by Windows CCD. This can be optionally
# set.
class _Union_1(ctypes.Union):
    pass


_Union_1._fields_ = [
    ('sourceId', NvU32),
    # not < Only for compatibility
    ('reserved_sourceId', NvU32),
]
_NV_DISPLAYCONFIG_PATH_INFO_V2._Union_1 = _Union_1

_NV_DISPLAYCONFIG_PATH_INFO_V2._anonymous_ = (
    '_Union_1',
)

_NV_DISPLAYCONFIG_PATH_INFO_V2._fields_ = [
    ('version', NvU32),
    ('_Union_1', _NV_DISPLAYCONFIG_PATH_INFO_V2._Union_1),
    # not < Number of elements in targetInfo array
    ('targetInfoCount', NvU32),
    ('targetInfo', POINTER(NV_DISPLAYCONFIG_PATH_TARGET_INFO_V2)),
    # not < May be NULL if mode info is not important
    ('sourceModeInfo', POINTER(NV_DISPLAYCONFIG_SOURCE_MODE_INFO_V1)),
    # not < True for non-NVIDIA adapter.
    ('IsNonNVIDIAAdapter', NvU32, 1),
    # not < Must be 0
    ('reserved', NvU32, 31),
    # not < Used by Non-NVIDIA adapter for pointer to OS Adapter of LUID
    ('pOSAdapterID', POINTER(VOID)),
]

# not \ingroup dispcontrol
NV_DISPLAYCONFIG_PATH_INFO_VER1 = (
    MAKE_NVAPI_VERSION(NV_DISPLAYCONFIG_PATH_INFO_V1, 1)
)

# not \ingroup dispcontrol
NV_DISPLAYCONFIG_PATH_INFO_VER2 = (
    MAKE_NVAPI_VERSION(NV_DISPLAYCONFIG_PATH_INFO_V2, 2)
)

NV_DISPLAYCONFIG_PATH_INFO = NV_DISPLAYCONFIG_PATH_INFO_V2
NV_DISPLAYCONFIG_PATH_INFO_VER = NV_DISPLAYCONFIG_PATH_INFO_VER2
NV_DISPLAYCONFIG_SOURCE_MODE_INFO = NV_DISPLAYCONFIG_SOURCE_MODE_INFO_V1


# not \ingroup dispcontrol
class _NV_DISPLAYCONFIG_FLAGS(ENUM):
    NV_DISPLAYCONFIG_VALIDATE_ONLY = 0x00000001
    NV_DISPLAYCONFIG_SAVE_TO_PERSISTENCE = 0x00000002
    NV_DISPLAYCONFIG_DRIVER_RELOAD_ALLOWED = 0x00000004
    NV_DISPLAYCONFIG_FORCE_MODE_ENUMERATION = 0x00000008
    NV_FORCE_COMMIT_VIDPN = 0x00000010


NV_DISPLAYCONFIG_FLAGS = _NV_DISPLAYCONFIG_FLAGS
NVAPI_UNICODE_STRING_MAX = 2048
NVAPI_BINARY_DATA_MAX = 4096
NvAPI_UnicodeString = NvU16 * NVAPI_UNICODE_STRING_MAX
NvAPI_LPCWSTR = POINTER(NvU16)

# Common
# not \ingroup gpuclock
# not @{
NVAPI_MAX_GPU_CLOCKS = 32
NVAPI_MAX_GPU_PUBLIC_CLOCKS = 32
NVAPI_MAX_GPU_PERF_CLOCKS = 32
NVAPI_MAX_GPU_PERF_VOLTAGES = 16
NVAPI_MAX_GPU_PERF_PSTATES = 16


# not @}
# not \ingroup gpuclock
class _NV_GPU_PERF_VOLTAGE_INFO_DOMAIN_ID(ENUM):
    NVAPI_GPU_PERF_VOLTAGE_INFO_DOMAIN_CORE = 0
    NVAPI_GPU_PERF_VOLTAGE_INFO_DOMAIN_UNDEFINED = (
        NVAPI_MAX_GPU_PERF_VOLTAGES
    )


NV_GPU_PERF_VOLTAGE_INFO_DOMAIN_ID = _NV_GPU_PERF_VOLTAGE_INFO_DOMAIN_ID


# not \ingroup gpuclock
class _NV_GPU_PUBLIC_CLOCK_ID(ENUM):
    NVAPI_GPU_PUBLIC_CLOCK_GRAPHICS = 0
    NVAPI_GPU_PUBLIC_CLOCK_MEMORY = 4
    NVAPI_GPU_PUBLIC_CLOCK_PROCESSOR = 7
    NVAPI_GPU_PUBLIC_CLOCK_VIDEO = 8
    NVAPI_GPU_PUBLIC_CLOCK_UNDEFINED = NVAPI_MAX_GPU_PUBLIC_CLOCKS


NV_GPU_PUBLIC_CLOCK_ID = _NV_GPU_PUBLIC_CLOCK_ID


# not \addtogroup gpupstate
# not @{
class _NV_GPU_PERF_PSTATE_ID(ENUM):
    NVAPI_GPU_PERF_PSTATE_P0 = 0
    NVAPI_GPU_PERF_PSTATE_P1 = 1
    NVAPI_GPU_PERF_PSTATE_P2 = 2
    NVAPI_GPU_PERF_PSTATE_P3 = 3
    NVAPI_GPU_PERF_PSTATE_P4 = 4
    NVAPI_GPU_PERF_PSTATE_P5 = 5
    NVAPI_GPU_PERF_PSTATE_P6 = 6
    NVAPI_GPU_PERF_PSTATE_P7 = 7
    NVAPI_GPU_PERF_PSTATE_P8 = 8
    NVAPI_GPU_PERF_PSTATE_P9 = 9
    NVAPI_GPU_PERF_PSTATE_P10 = 10
    NVAPI_GPU_PERF_PSTATE_P11 = 11
    NVAPI_GPU_PERF_PSTATE_P12 = 12
    NVAPI_GPU_PERF_PSTATE_P13 = 13
    NVAPI_GPU_PERF_PSTATE_P14 = 14
    NVAPI_GPU_PERF_PSTATE_P15 = 15
    NVAPI_GPU_PERF_PSTATE_UNDEFINED = NVAPI_MAX_GPU_PERF_PSTATES
    NVAPI_GPU_PERF_PSTATE_ALL = 16


NV_GPU_PERF_PSTATE_ID = _NV_GPU_PERF_PSTATE_ID

# not @}
# not \addtogroup gpupstate
# not @{
NVAPI_MAX_GPU_PSTATE20_PSTATES = 16
NVAPI_MAX_GPU_PSTATE20_CLOCKS = 8
NVAPI_MAX_GPU_PSTATE20_BASE_VOLTAGES = 4


# not Used to identify clock type
class NV_GPU_PERF_PSTATE20_CLOCK_TYPE_ID(ENUM):
    NVAPI_GPU_PERF_PSTATE20_CLOCK_TYPE_SINGLE = 0
    NVAPI_GPU_PERF_PSTATE20_CLOCK_TYPE_RANGE = 1


NVAPI_GPU_PERF_PSTATE20_CLOCK_TYPE_SINGLE = NV_GPU_PERF_PSTATE20_CLOCK_TYPE_ID.NVAPI_GPU_PERF_PSTATE20_CLOCK_TYPE_SINGLE
NVAPI_GPU_PERF_PSTATE20_CLOCK_TYPE_RANGE = NV_GPU_PERF_PSTATE20_CLOCK_TYPE_ID.NVAPI_GPU_PERF_PSTATE20_CLOCK_TYPE_RANGE


# not Used to describe both voltage and frequency deltas
class valueRange(ctypes.Structure):
    pass


valueRange._fields_ = [
    # not Min value allowed for parameter delta
    # (in respective units [kHz, uV])
    ('min', NvS32),
    # not Max value allowed for parameter delta
    # (in respective units [kHz, uV])
    ('max', NvS32),
]
NV_GPU_PERF_PSTATES20_PARAM_DELTA.valueRange = valueRange

NV_GPU_PERF_PSTATES20_PARAM_DELTA._fields_ = [
    # not Value of parameter delta (in respective units [kHz, uV])
    ('value', NvS32),
    ('valueRange', NV_GPU_PERF_PSTATES20_PARAM_DELTA.valueRange),
]


# not Used to describe single clock entry
class data(ctypes.Union):
    pass


class single(ctypes.Structure):
    pass


single._fields_ = [
    # not Clock frequency within given pstate in (kHz)
    ('freq_kHz', NvU32),
]
data.single = single


class _range(ctypes.Structure):
    pass


_range._fields_ = [
    # not Min clock frequency within given pstate in (kHz)
    ('minFreq_kHz', NvU32),
    # not Max clock frequency within given pstate in (kHz)
    ('maxFreq_kHz', NvU32),
    # not Voltage domain ID and value range in (uV) required for this clock
    ('domainId', NV_GPU_PERF_VOLTAGE_INFO_DOMAIN_ID),
    ('minVoltage_uV', NvU32),
    ('maxVoltage_uV', NvU32),
]
data._range = _range

data._fields_ = [
    ('single', data.single),
    ('range', data._range),
]
NV_GPU_PSTATE20_CLOCK_ENTRY_V1.data = data

NV_GPU_PSTATE20_CLOCK_ENTRY_V1._fields_ = [
    # not ID of the clock domain
    ('domainId', NV_GPU_PUBLIC_CLOCK_ID),
    # not Clock type ID
    ('typeId', NV_GPU_PERF_PSTATE20_CLOCK_TYPE_ID),
    ('bIsEditable', NvU32, 1),
    # not These bits are reserved for future use (must be always 0)
    ('reserved', NvU32, 31),
    # not Current frequency delta from nominal settings in (kHz)
    ('freqDelta_kHz', NV_GPU_PERF_PSTATES20_PARAM_DELTA),
    # not Clock domain type dependant information
    ('data', NV_GPU_PSTATE20_CLOCK_ENTRY_V1.data),
]

# not Used to describe single base voltage entry
NV_GPU_PSTATE20_BASE_VOLTAGE_ENTRY_V1._fields_ = [
    # not ID of the voltage domain
    ('domainId', NV_GPU_PERF_VOLTAGE_INFO_DOMAIN_ID),
    ('bIsEditable', NvU32, 1),
    # not These bits are reserved for future use (must be always 0)
    ('reserved', NvU32, 31),
    # not Current base voltage settings in [uV]
    ('volt_uV', NvU32),
    # Current base voltage delta from nominal settings in [uV]
    ('voltDelta_uV', NV_GPU_PERF_PSTATES20_PARAM_DELTA),
]


# not Used in NvAPI_GPU_GetPstates20() interface call.
class pstates(ctypes.Structure):
    pass


pstates._fields_ = [
    # not ID of the P-State
    ('pstateId', NV_GPU_PERF_PSTATE_ID),
    ('bIsEditable', NvU32, 1),
    # not These bits are reserved for future use (must be always 0)
    ('reserved', NvU32, 31),
    # not Valid index range is 0 to numClocks-1
    ('clocks', NV_GPU_PSTATE20_CLOCK_ENTRY_V1 * NVAPI_MAX_GPU_PSTATE20_CLOCKS),
    # not Valid index range is 0 to numBaseVoltages-1
    ('baseVoltages', NV_GPU_PSTATE20_BASE_VOLTAGE_ENTRY_V1 * NVAPI_MAX_GPU_PSTATE20_BASE_VOLTAGES),
]
NV_GPU_PERF_PSTATES20_INFO_V1.pstates = pstates

NV_GPU_PERF_PSTATES20_INFO_V1._fields_ = [
    # not Version info of the structure
    # (NV_GPU_PERF_PSTATES20_INFO_VER < n > )
    ('version', NvU32),
    ('bIsEditable', NvU32, 1),
    # not These bits are reserved for future use (must be always 0)
    ('reserved', NvU32, 31),
    # not Number of populated pstates
    ('numPstates', NvU32),
    # not Number of populated clocks (per pstate)
    ('numClocks', NvU32),
    # not Number of populated base voltages (per pstate)
    ('numBaseVoltages', NvU32),
    # not Valid index range is 0 to numPstates-1
    ('pstates', NV_GPU_PERF_PSTATES20_INFO_V1.pstates * NVAPI_MAX_GPU_PSTATE20_PSTATES),
]


# not Used in NvAPI_GPU_GetPstates20() interface call.
class pstates(ctypes.Structure):
    pass


pstates._fields_ = [
    # not ID of the P-State
    ('pstateId', NV_GPU_PERF_PSTATE_ID),
    ('bIsEditable', NvU32, 1),
    # not These bits are reserved for future use (must be always 0)
    ('reserved', NvU32, 31),
    # not Valid index range is 0 to numClocks-1
    ('clocks', NV_GPU_PSTATE20_CLOCK_ENTRY_V1 * NVAPI_MAX_GPU_PSTATE20_CLOCKS),
    # not Valid index range is 0 to numBaseVoltages-1
    ('baseVoltages', NV_GPU_PSTATE20_BASE_VOLTAGE_ENTRY_V1 * NVAPI_MAX_GPU_PSTATE20_BASE_VOLTAGES),
]
_NV_GPU_PERF_PSTATES20_INFO_V2.pstates = pstates


class ov(ctypes.Structure):
    pass


ov._fields_ = [
    # not Number of populated voltages
    ('numVoltages', NvU32),
    # not Valid index range is 0 to numVoltages-1
    ('voltages', NV_GPU_PSTATE20_BASE_VOLTAGE_ENTRY_V1 * NVAPI_MAX_GPU_PSTATE20_BASE_VOLTAGES),
]
_NV_GPU_PERF_PSTATES20_INFO_V2.ov = ov

_NV_GPU_PERF_PSTATES20_INFO_V2._fields_ = [
    # not Version info of the structure
    # (NV_GPU_PERF_PSTATES20_INFO_VER < n > )
    ('version', NvU32),
    ('bIsEditable', NvU32, 1),
    # not These bits are reserved for future use (must be always 0)
    ('reserved', NvU32, 31),
    # not Number of populated pstates
    ('numPstates', NvU32),
    # not Number of populated clocks (per pstate)
    ('numClocks', NvU32),
    # not Number of populated base voltages (per pstate)
    ('numBaseVoltages', NvU32),
    # not Valid index range is 0 to numPstates-1
    ('pstates', _NV_GPU_PERF_PSTATES20_INFO_V2.pstates * NVAPI_MAX_GPU_PSTATE20_PSTATES),
    # not Valid index range is 0 to numVoltages-1
    ('ov', _NV_GPU_PERF_PSTATES20_INFO_V2.ov),
]
NV_GPU_PERF_PSTATES20_INFO = NV_GPU_PERF_PSTATES20_INFO_V2
# not Macro for constructing the version field of
# NV_GPU_PERF_PSTATES20_INFO_V1
NV_GPU_PERF_PSTATES20_INFO_VER1 = (
    MAKE_NVAPI_VERSION(NV_GPU_PERF_PSTATES20_INFO_V1, 1)
)

# not Macro for constructing the version field of
# NV_GPU_PERF_PSTATES20_INFO_V2
NV_GPU_PERF_PSTATES20_INFO_VER2 = (
    MAKE_NVAPI_VERSION(NV_GPU_PERF_PSTATES20_INFO_V2, 2)
)

# not Macro for constructing the version field of
# NV_GPU_PERF_PSTATES20_INFO_V2
NV_GPU_PERF_PSTATES20_INFO_VER3 = (
    MAKE_NVAPI_VERSION(NV_GPU_PERF_PSTATES20_INFO_V2, 3)
)

# not Macro for constructing the version field of
# NV_GPU_PERF_PSTATES20_INFO
NV_GPU_PERF_PSTATES20_INFO_VER = NV_GPU_PERF_PSTATES20_INFO_VER3

# not @}
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetDisplayDriverVersion
# not \fn
# NvAPI_GetDisplayDriverVersion(NvDisplayHandle hNvDisplay, NV_DISPLAY_DRIVER_VERSION *pVersion)
#
# not This function returns a struct that describes aspects of the display
# driver
# not    build.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_SYS_GetDriverAndBranchVersion.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 80
# not
# not \param [in] hNvDisplay NVIDIA display handle.
# not \param [out] pVersion Pointer to NV_DISPLAY_DRIVER_VERSION struc
# not
# not \retval NVAPI_ERROR
# not \retval NVAPI_OK
# ///////////////////////////////////////////////////////////////////////
NvAPI_GetDisplayDriverVersion = hDll.GetDisplayDriverVersion
NvAPI_GetDisplayDriverVersion.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GetDisplayDriverVersion(NvDisplayHandle hNvDisplay, NV_DISPLAY_DRIVER_VERSION *pVersion);


# not \ingroup driverapi
# not Used in NvAPI_GetDisplayDriverVersion()
NV_DISPLAY_DRIVER_VERSION._fields_ = [

    # Structure version
    ('version', NvU32),
    ('drvVersion', NvU32),
    ('bldChangeListNum', NvU32),
    ('szBuildBranchString', NvAPI_ShortString),
    ('szAdapterString', NvAPI_ShortString),
]
# not \ingroup driverapi
NV_DISPLAY_DRIVER_VERSION_VER = (
    MAKE_NVAPI_VERSION(NV_DISPLAY_DRIVER_VERSION, 1)
)
# not \ingroup driverapi
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_OGL_ExpertModeSet[Get]
# not \name NvAPI_OGL_ExpertModeSet[Get] Functions
# @{
# not This function configures OpenGL Expert Mode, an API usage feedback
# and
# not advice reporting mechanism. The effects of this call are
# not applied only to the current context, and are reset to the
# not defaults when the context is destroyed.
# not
# not \note This feature is valid at runtime only when GLExpert
# not  functionality has been built into the OpenGL driver
# not  installed on the system. All Windows Vista OpenGL
# not  drivers provided by NVIDIA have this instrumentation
# not  included by default. Windows XP, however, requires a
# not  special display driver available with the NVIDIA
# not  PerfSDK found at developer.nvidia.com.
# not
# not \note These functions are valid only for the current OpenGL
# not  context. Calling these functions prior to creating a
# not  context and calling MakeCurrent with it will result
# not  in errors and undefined behavior.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 80
# not
# not \param expertDetailMask Mask made up of NVAPI_OGLEXPERT_DETAIL bits,
# not      this parameter specifies the detail level in
# not      the feedback stream.
# not
# not \param expertReportMask Mask made up of NVAPI_OGLEXPERT_REPORT bits,
# not      this parameter specifies the areas of
# not      functional interest.
# not
# not \param expertOutputMask Mask made up of NVAPI_OGLEXPERT_OUTPUT bits,
# not      this parameter specifies the feedback output
# not      location.
# not
# not \param expertCallback Used in conjunction with OUTPUT_TO_CALLBACK,
# not      this is a simple callback function the user
# not      may use to obtain the feedback stream. The
# not      function will be called once per fully
# not      qualified feedback stream extry.
# not
# not \retval NVAPI_API_NOT_INTIALIZED  NVAPI not initialized
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU found
# not \retval NVAPI_OPENGL_CONTEXT_NOT_CURRENT No NVIDIA OpenGL context
# not        which supports GLExpert
# not        has been made current
# not \retval NVAPI_ERROR     OpenGL driver failed to load properly
# not \retval NVAPI_OK     Success
# ///////////////////////////////////////////////////////////////////////
# not \addtogroup oglapi
# not @{
NVAPI_OGLEXPERT_DETAIL_NONE = 0x00000000
NVAPI_OGLEXPERT_DETAIL_ERROR = 0x00000001
NVAPI_OGLEXPERT_DETAIL_SWFALLBACK = 0x00000002
NVAPI_OGLEXPERT_DETAIL_BASIC_INFO = 0x00000004
NVAPI_OGLEXPERT_DETAIL_DETAILED_INFO = 0x00000008
NVAPI_OGLEXPERT_DETAIL_PERFORMANCE_WARNING = 0x00000010
NVAPI_OGLEXPERT_DETAIL_QUALITY_WARNING = 0x00000020
NVAPI_OGLEXPERT_DETAIL_USAGE_WARNING = 0x00000040
NVAPI_OGLEXPERT_DETAIL_ALL = 0xFFFFFFFF
NVAPI_OGLEXPERT_REPORT_NONE = 0x00000000
NVAPI_OGLEXPERT_REPORT_ERROR = 0x00000001
NVAPI_OGLEXPERT_REPORT_SWFALLBACK = 0x00000002
NVAPI_OGLEXPERT_REPORT_PIPELINE_VERTEX = 0x00000004
NVAPI_OGLEXPERT_REPORT_PIPELINE_GEOMETRY = 0x00000008
NVAPI_OGLEXPERT_REPORT_PIPELINE_XFB = 0x00000010
NVAPI_OGLEXPERT_REPORT_PIPELINE_RASTER = 0x00000020
NVAPI_OGLEXPERT_REPORT_PIPELINE_FRAGMENT = 0x00000040
NVAPI_OGLEXPERT_REPORT_PIPELINE_ROP = 0x00000080
NVAPI_OGLEXPERT_REPORT_PIPELINE_FRAMEBUFFER = 0x00000100
NVAPI_OGLEXPERT_REPORT_PIPELINE_PIXEL = 0x00000200
NVAPI_OGLEXPERT_REPORT_PIPELINE_TEXTURE = 0x00000400
NVAPI_OGLEXPERT_REPORT_OBJECT_BUFFEROBJECT = 0x00000800
NVAPI_OGLEXPERT_REPORT_OBJECT_TEXTURE = 0x00001000
NVAPI_OGLEXPERT_REPORT_OBJECT_PROGRAM = 0x00002000
NVAPI_OGLEXPERT_REPORT_OBJECT_FBO = 0x00004000
NVAPI_OGLEXPERT_REPORT_FEATURE_SLI = 0x00008000
NVAPI_OGLEXPERT_REPORT_ALL = 0xFFFFFFFF
NVAPI_OGLEXPERT_OUTPUT_TO_NONE = 0x00000000
NVAPI_OGLEXPERT_OUTPUT_TO_CONSOLE = 0x00000001
NVAPI_OGLEXPERT_OUTPUT_TO_DEBUGGER = 0x00000004
NVAPI_OGLEXPERT_OUTPUT_TO_CALLBACK = 0x00000008
NVAPI_OGLEXPERT_OUTPUT_TO_ALL = 0xFFFFFFFF
# not @}
# ///////////////////////////////////////////////////////////////////////
# FUNCTION TYPE: NVAPI_OGLEXPERT_CALLBACK
# not DESCRIPTION: Used in conjunction with OUTPUT_TO_CALLBACK, this is a
# simple
# not    callback function the user may use to obtain the feedback
# not    stream. The function will be called once per fully qualified
# not    feedback stream entry.
# not
# not \param categoryId Contains the bit from the NVAPI_OGLEXPERT_REPORT
# not     mask that corresponds to the current message
# not \param messageId  Unique ID for the current message
# not \param detailLevel Contains the bit from the NVAPI_OGLEXPERT_DETAIL
# not     mask that corresponds to the current message
# not \param objectId Unique ID of the object that corresponds to the
# not     current message
# not \param messageStr Text string from the current message
# not
# not \ingroup oglapi
# ///////////////////////////////////////////////////////////////////////
# VOID (* NVAPI_OGLEXPERT_CALLBACK) (unsigned INT categoryId, UINT messageId, UINT detailLevel, INT objectId, CHAR *messageStr);
NVAPI_OGLEXPERT_CALLBACK = ctypes.WINFUNCTYPE(
    VOID,
    INT,
    UINT,
    UINT,
    INT,
    POINTER(CHAR),
)

# not \ingroup oglapi
# not SUPPORTED OS: Windows 7 and higher
NvAPI_OGL_ExpertModeSet = hDll.OGL_ExpertModeSet
NvAPI_OGL_ExpertModeSet.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_OGL_ExpertModeSet(NvU32 expertDetailLevel,
#                                         NvU32 expertReportMask,
#                                         NvU32 expertOutputMask,
#                      NVAPI_OGLEXPERT_CALLBACK expertCallback);

# not
# not \addtogroup oglapi
# not SUPPORTED OS: Windows 7 and higher
NvAPI_OGL_ExpertModeGet = hDll.OGL_ExpertModeGet
NvAPI_OGL_ExpertModeGet.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_OGL_ExpertModeGet(NvU32 *pExpertDetailLevel,
#                                         NvU32 *pExpertReportMask,
#                                         NvU32 *pExpertOutputMask,
#                      NVAPI_OGLEXPERT_CALLBACK *pExpertCallback);

# not
# @}
# ///////////////////////////////////////////////////////////////////////
# not \name NvAPI_OGL_ExpertModeDefaultsSet[Get] Functions
# not
# @{
# not This function configures OpenGL Expert Mode global defaults. These
# settings
# not apply to any OpenGL application which starts up after these
# not values are applied (i.e. these settings *do not* apply to
# not currently running applications).
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 80
# not
# not \param expertDetailLevel Value which specifies the detail level in
# not      the feedback stream. This is a mask made up
# not      of NVAPI_OGLEXPERT_LEVEL bits.
# not
# not \param expertReportMask Mask made up of NVAPI_OGLEXPERT_REPORT bits,
# not      this parameter specifies the areas of
# not      functional interest.
# not
# not \param expertOutputMask Mask made up of NVAPI_OGLEXPERT_OUTPUT bits,
# not      this parameter specifies the feedback output
# not      location. Note that using OUTPUT_TO_CALLBACK
# not      here is meaningless and has no effect, but
# not      using it will not cause an error.
# not
# not \return ::NVAPI_ERROR or ::NVAPI_OK
# ///////////////////////////////////////////////////////////////////////
# not \ingroup oglapi
# not SUPPORTED OS: Windows 7 and higher
NvAPI_OGL_ExpertModeDefaultsSet = hDll.OGL_ExpertModeDefaultsSet
NvAPI_OGL_ExpertModeDefaultsSet.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_OGL_ExpertModeDefaultsSet(NvU32 expertDetailLevel,
#                                                 NvU32 expertReportMask,
#                                                 NvU32 expertOutputMask);

# not
# not \addtogroup oglapi
# not SUPPORTED OS: Windows 7 and higher
NvAPI_OGL_ExpertModeDefaultsGet = hDll.OGL_ExpertModeDefaultsGet
NvAPI_OGL_ExpertModeDefaultsGet.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_OGL_ExpertModeDefaultsGet(NvU32 *pExpertDetailLevel,
#                                                 NvU32 *pExpertReportMask,
#                                                 NvU32 *pExpertOutputMask);

# not
# @}
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_EnumTCCPhysicalGPUs
# not This function returns an array of physical GPU handles that are in
# TCC Mode.
# not Each handle represents a physical GPU present in the system in TCC
# Mode.
# not That GPU may not be visible to the OS directly.
# not
# not The array nvGPUHandle will be filled with physical GPU handle
# values. The returned
# not gpuCount determines how many entries in the array are valid.
# not
# not NOTE: Handles enumerated by this API are only valid for NvAPIs that
# are tagged as TCC_SUPPORTED
# not  If handle is passed to any other API, it will fail with
# NVAPI_INVALID_HANDLE
# not
# not  For WDDM GPU handles please use NvAPI_EnumPhysicalGPUs()
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not
# not \param [out] nvGPUHandle Physical GPU array that will contain all
# TCC Physical GPUs
# not \param [out] pGpuCount  count represent the number of valid entries
# in nvGPUHandle
# not
# not
# not \retval NVAPI_INVALID_ARGUMENT  nvGPUHandle or pGpuCount is NULL
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_EnumTCCPhysicalGPUs = hDll.EnumTCCPhysicalGPUs
NvAPI_EnumTCCPhysicalGPUs.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_EnumTCCPhysicalGPUs( NvPhysicalGpuHandle nvGPUHandle[NVAPI_MAX_PHYSICAL_GPUS], NvU32 *pGpuCount);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_EnumLogicalGPUs
# not This function returns an array of logical GPU handles.
# not
# not Each handle represents one or more GPUs acting in concert as a
# single graphics device.
# not
# not At least one GPU must be present in the system and running an NVIDIA
# display driver.
# not
# not The array nvGPUHandle will be filled with logical GPU handle values.
# The returned
# not gpuCount determines how many entries in the array are valid.
# not
# not \note All logical GPUs handles get invalidated on a GPU topology
# change, so the calling
# not  application is required to renum the logical GPU handles to get
# latest physical handle
# not  mapping after every GPU topology change activated by a call to
# NvAPI_SetGpuTopologies().
# not
# not To detect if SLI rendering is enabled, use
# NvAPI_D3D_GetCurrentSLIState().
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 80
# not
# not \retval NVAPI_INVALID_ARGUMENT  nvGPUHandle or pGpuCount is NULL
# not \retval NVAPI_OK     One or more handles were returned
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND No NVIDIA GPU driving a
# display was found
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_EnumLogicalGPUs = hDll.EnumLogicalGPUs
NvAPI_EnumLogicalGPUs.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_EnumLogicalGPUs(NvLogicalGpuHandle nvGPUHandle[NVAPI_MAX_LOGICAL_GPUS], NvU32 *pGpuCount);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetPhysicalGPUsFromDisplay
# not This function returns an array of physical GPU handles associated
# with the specified display.
# not
# not At least one GPU must be present in the system and running an NVIDIA
# display driver.
# not
# not The array nvGPUHandle will be filled with physical GPU handle
# values. The returned
# not gpuCount determines how many entries in the array are valid.
# not
# not If the display corresponds to more than one physical GPU, the first
# GPU returned
# not is the one with the attached active output.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 80
# not
# not \retval NVAPI_INVALID_ARGUMENT  hNvDisp is not valid; nvGPUHandle or
# pGpuCount is NULL
# not \retval NVAPI_OK     One or more handles were returned
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND no NVIDIA GPU driving a
# display was found
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GetPhysicalGPUsFromDisplay = hDll.GetPhysicalGPUsFromDisplay
NvAPI_GetPhysicalGPUsFromDisplay.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GetPhysicalGPUsFromDisplay(NvDisplayHandle hNvDisp, NvPhysicalGpuHandle nvGPUHandle[NVAPI_MAX_PHYSICAL_GPUS], NvU32 *pGpuCount);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetPhysicalGPUFromUnAttachedDisplay
# not This function returns a physical GPU handle associated with the
# specified unattached display.
# not The source GPU is a physical render GPU which renders the frame
# buffer but may or may not drive the scan out.
# not
# not At least one GPU must be present in the system and running an NVIDIA
# display driver.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 80
# not
# not \retval NVAPI_INVALID_ARGUMENT  hNvUnAttachedDisp is not valid or
# pPhysicalGpu is NULL.
# not \retval NVAPI_OK     One or more handles were returned
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND No NVIDIA GPU driving a
# display was found
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GetPhysicalGPUFromUnAttachedDisplay = hDll.GetPhysicalGPUFromUnAttachedDisplay
NvAPI_GetPhysicalGPUFromUnAttachedDisplay.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GetPhysicalGPUFromUnAttachedDisplay(NvUnAttachedDisplayHandle hNvUnAttachedDisp, NvPhysicalGpuHandle *pPhysicalGpu);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetLogicalGPUFromDisplay
# not This function returns the logical GPU handle associated with the
# specified display.
# not At least one GPU must be present in the system and running an NVIDIA
# display driver.
# not hNvDisp can be NVAPI_DEFAULT_HANDLE or a handle enumerated from
# NvAPI_EnumNVidiaDisplayHandle().
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 80
# not
# not \retval NVAPI_INVALID_ARGUMENT  hNvDisp is not valid; pLogicalGPU is
# NULL
# not \retval NVAPI_OK     One or more handles were returned
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND No NVIDIA GPU driving a
# display was found
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GetLogicalGPUFromDisplay = hDll.GetLogicalGPUFromDisplay
NvAPI_GetLogicalGPUFromDisplay.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GetLogicalGPUFromDisplay(NvDisplayHandle hNvDisp, NvLogicalGpuHandle *pLogicalGPU);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetLogicalGPUFromPhysicalGPU
# not This function returns the logical GPU handle associated with
# specified physical GPU handle.
# not At least one GPU must be present in the system and running an NVIDIA
# display driver.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 80
# not
# not \retval NVAPI_INVALID_ARGUMENT  hPhysicalGPU is not valid;
# pLogicalGPU is NULL
# not \retval NVAPI_OK     One or more handles were returned
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND No NVIDIA GPU driving a
# display was found
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GetLogicalGPUFromPhysicalGPU = hDll.GetLogicalGPUFromPhysicalGPU
NvAPI_GetLogicalGPUFromPhysicalGPU.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GetLogicalGPUFromPhysicalGPU(NvPhysicalGpuHandle hPhysicalGPU, NvLogicalGpuHandle *pLogicalGPU);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetPhysicalGPUsFromLogicalGPU
# not This function returns the physical GPU handles associated with the
# specified logical GPU handle.
# not At least one GPU must be present in the system and running an NVIDIA
# display driver.
# not
# not The array hPhysicalGPU will be filled with physical GPU handle
# values. The returned
# not gpuCount determines how many entries in the array are valid.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 80
# not
# not \retval NVAPI_INVALID_ARGUMENT   hLogicalGPU is not valid;
# hPhysicalGPU is NULL
# not \retval NVAPI_OK     One or more handles were returned
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND No NVIDIA GPU driving a
# display was found
# not \retval NVAPI_EXPECTED_LOGICAL_GPU_HANDLE hLogicalGPU was not a
# logical GPU handle
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GetPhysicalGPUsFromLogicalGPU = hDll.GetPhysicalGPUsFromLogicalGPU
NvAPI_GetPhysicalGPUsFromLogicalGPU.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GetPhysicalGPUsFromLogicalGPU(NvLogicalGpuHandle hLogicalGPU,NvPhysicalGpuHandle hPhysicalGPU[NVAPI_MAX_PHYSICAL_GPUS], NvU32 *pGpuCount);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetShaderSubPipeCount
# not DESCRIPTION: This function retrieves the number of Shader SubPipes
# on the GPU
# not    On newer architectures, this corresponds to the number of SM units
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 170
# not
# not RETURN STATUS: NVAPI_INVALID_ARGUMENT: pCount is NULL
# not    NVAPI_OK: *pCount is set
# not    NVAPI_NVIDIA_DEVICE_NOT_FOUND: no NVIDIA GPU driving a display
# was found
# not    NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE: hPhysicalGpu was not a
# physical GPU handle
# not
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetShaderSubPipeCount = hDll.GPU_GetShaderSubPipeCount
NvAPI_GPU_GetShaderSubPipeCount.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetShaderSubPipeCount(NvPhysicalGpuHandle hPhysicalGpu,NvU32 *pCount);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetGpuCoreCount
# not DESCRIPTION: Retrieves the total number of cores defined for a GPU.
# not    Returns 0 on architectures that don't define GPU cores.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \retval ::NVAPI_INVALID_ARGUMENT   pCount is NULL
# not \retval ::NVAPI_OK     *pCount is set
# not \retval ::NVAPI_NVIDIA_DEVICE_NOT_FOUND  no NVIDIA GPU driving a
# display was found
# not \retval ::NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle
# not \retval ::NVAPI_NOT_SUPPORTED    API call is not supported on
# current architecture
# not
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetGpuCoreCount = hDll.GPU_GetGpuCoreCount
NvAPI_GPU_GetGpuCoreCount.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetGpuCoreCount(NvPhysicalGpuHandle hPhysicalGpu,NvU32 *pCount);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetAllOutputs
# not This function returns set of all GPU-output identifiers as a bitmask.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_GPU_GetAllDisplayIds.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 85
# not
# not \retval NVAPI_INVALID_ARGUMENT   hPhysicalGpu or pOutputsMask is
# NULL.
# not \retval NVAPI_OK     *pOutputsMask contains a set of GPU-output
# identifiers.
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found.
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle.
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetAllOutputs = hDll.GPU_GetAllOutputs
NvAPI_GPU_GetAllOutputs.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetAllOutputs(NvPhysicalGpuHandle hPhysicalGpu,NvU32 *pOutputsMask);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetConnectedOutputs
# not This function is the same as NvAPI_GPU_GetAllOutputs() but returns
# only the set of GPU output
# not identifiers that are connected to display devices.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_GPU_GetConnectedDisplayIds.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 80
# not
# not \retval NVAPI_INVALID_ARGUMENT   hPhysicalGpu or pOutputsMask is
# NULL.
# not \retval NVAPI_OK     *pOutputsMask contains a set of GPU-output
# identifiers.
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found.
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle.
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetConnectedOutputs = hDll.GPU_GetConnectedOutputs
NvAPI_GPU_GetConnectedOutputs.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetConnectedOutputs(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pOutputsMask);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetConnectedSLIOutputs
# not DESCRIPTION: This function is the same as
# NvAPI_GPU_GetConnectedOutputs() but returns only the set of GPU-output
# not    identifiers that can be selected in an SLI configuration.
# not   NOTE: This function matches NvAPI_GPU_GetConnectedOutputs()
# not   - On systems which are not SLI capable.
# not   - If the queried GPU is not part of a valid SLI group.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_GPU_GetConnectedDisplayIds.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 170
# not
# not \retval NVAPI_INVALID_ARGUMENT   hPhysicalGpu or pOutputsMask is NULL
# not \retval NVAPI_OK     *pOutputsMask contains a set of GPU-output
# identifiers
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE: hPhysicalGpu was not a
# physical GPU handle
# not
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetConnectedSLIOutputs = hDll.GPU_GetConnectedSLIOutputs
NvAPI_GPU_GetConnectedSLIOutputs.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GPU_GetConnectedSLIOutputs(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pOutputsMask);


# not \ingroup gpu
class NV_MONITOR_CONN_TYPE(ENUM):
    NV_MONITOR_CONN_TYPE_UNINITIALIZED = 0
    NV_MONITOR_CONN_TYPE_VGA = 1
    NV_MONITOR_CONN_TYPE_COMPONENT = 2
    NV_MONITOR_CONN_TYPE_SVIDEO = 3
    NV_MONITOR_CONN_TYPE_HDMI = 4
    NV_MONITOR_CONN_TYPE_DVI = 5
    NV_MONITOR_CONN_TYPE_LVDS = 6
    NV_MONITOR_CONN_TYPE_DP = 7
    NV_MONITOR_CONN_TYPE_COMPOSITE = 8
    NV_MONITOR_CONN_TYPE_UNKNOWN = - 1


NV_MONITOR_CONN_TYPE_UNINITIALIZED = NV_MONITOR_CONN_TYPE.NV_MONITOR_CONN_TYPE_UNINITIALIZED
NV_MONITOR_CONN_TYPE_VGA = NV_MONITOR_CONN_TYPE.NV_MONITOR_CONN_TYPE_VGA
NV_MONITOR_CONN_TYPE_COMPONENT = NV_MONITOR_CONN_TYPE.NV_MONITOR_CONN_TYPE_COMPONENT
NV_MONITOR_CONN_TYPE_SVIDEO = NV_MONITOR_CONN_TYPE.NV_MONITOR_CONN_TYPE_SVIDEO
NV_MONITOR_CONN_TYPE_HDMI = NV_MONITOR_CONN_TYPE.NV_MONITOR_CONN_TYPE_HDMI
NV_MONITOR_CONN_TYPE_DVI = NV_MONITOR_CONN_TYPE.NV_MONITOR_CONN_TYPE_DVI
NV_MONITOR_CONN_TYPE_LVDS = NV_MONITOR_CONN_TYPE.NV_MONITOR_CONN_TYPE_LVDS
NV_MONITOR_CONN_TYPE_DP = NV_MONITOR_CONN_TYPE.NV_MONITOR_CONN_TYPE_DP
NV_MONITOR_CONN_TYPE_COMPOSITE = NV_MONITOR_CONN_TYPE.NV_MONITOR_CONN_TYPE_COMPOSITE
NV_MONITOR_CONN_TYPE_UNKNOWN = NV_MONITOR_CONN_TYPE.NV_MONITOR_CONN_TYPE_UNKNOWN

# not \addtogroup gpu
# not @{
# not < Get uncached connected devices
NV_GPU_CONNECTED_IDS_FLAG_UNCACHED = NV_BIT(0)
# not < Get devices such that those can be selected in an SLI configuration
NV_GPU_CONNECTED_IDS_FLAG_SLI = NV_BIT(1)
# not < Get devices such that to reflect the Lid State
NV_GPU_CONNECTED_IDS_FLAG_LIDSTATE = NV_BIT(2)
# not < Get devices that includes the fake connected monitors
NV_GPU_CONNECTED_IDS_FLAG_FAKE = NV_BIT(3)
# not < Excludes devices that are part of the multi stream topology.
NV_GPU_CONNECTED_IDS_FLAG_EXCLUDE_MST = NV_BIT(4)
# not @}
# not \ingroup gpu

_NV_GPU_DISPLAYIDS._fields_ = [
    ('version', NvU32),
    # not < out: vga, tv, dvi, hdmi and dp. This is reserved for future
    # use and clients should not rely on this information. Instead get the
    ('connectorType', NV_MONITOR_CONN_TYPE),
    # not < this is a unique identifier for each device
    ('displayId', NvU32),
    # not < if bit is set then this display is part of MST topology and
    # it's a dynamic
    ('isDynamic', NvU32, 1),
    # not < if bit is set then this displayID belongs to a multi stream
    # enabled connector(root node). Note that when multi stream is enabled
    # and
    ('isMultiStreamRootNode', NvU32, 1),
    # not < if bit is set then this display is being actively driven
    ('isActive', NvU32, 1),
    # not < if bit is set then this display is the representative display
    ('isCluster', NvU32, 1),
    # not < if bit is set, then this display is reported to the OS
    ('isOSVisible', NvU32, 1),
    # not < if bit is set, then this display is wireless
    ('isWFD', NvU32, 1),
    # not < if bit is set, then this display is connected
    ('isConnected', NvU32, 1),
    # not < Do not use
    ('reservedInternal', NvU32, 10),
    # not < if bit is set, then this display is a phycially connected
    # display; Valid only when isConnected bit is set
    ('isPhysicallyConnected', NvU32, 1),
    # not < must be zero
    ('reserved', NvU32, 14),
]

# not \ingroup gpu
# not Macro for constructing the version field of ::_NV_GPU_DISPLAYIDS
NV_GPU_DISPLAYIDS_VER1 = MAKE_NVAPI_VERSION(NV_GPU_DISPLAYIDS, 1)
NV_GPU_DISPLAYIDS_VER2 = MAKE_NVAPI_VERSION(NV_GPU_DISPLAYIDS, 3)
NV_GPU_DISPLAYIDS_VER = NV_GPU_DISPLAYIDS_VER2

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetConnectedDisplayIds
# not \code
# not DESCRIPTION: Due to space limitation NvAPI_GPU_GetConnectedOutputs
# can return maximum 32 devices, but
# not    this is no longer true for DPMST.
# NvAPI_GPU_GetConnectedDisplayIds will return all
# not    the connected display devices in the form of displayIds for the
# associated hPhysicalGpu.
# not    This function can accept set of flags to request cached,
# uncached, sli and lid to get the connected devices.
# not    Default value for flags will be cached .
# not HOW TO USE:
# 1) for each PhysicalGpu, make a call to get the number of connected displayId's
#
# not    using NvAPI_GPU_GetConnectedDisplayIds by passing the pDisplayIds
# as NULL
# not    On call success:
# not
# 2) If pDisplayIdCount is greater than 0, allocate memory based on pDisplayIdCount.
# Then make a call NvAPI_GPU_GetConnectedDisplayIds to populate DisplayIds.
#
# not    However, if pDisplayIdCount is 0, do not make this call.
# not SUPPORTED OS: Windows 7 and higher
# not
# not PARAMETERS:  hPhysicalGpu (IN) - GPU selection
# not   flags  (IN) - One or more defines from NV_GPU_CONNECTED_IDS_FLAG_*
# as valid flags.
# not   pDisplayIds (IN/OUT) - Pointer to an NV_GPU_DISPLAYIDS struct,
# each entry represents a one displayID and its attributes
# not   pDisplayIdCount(OUT)- Number of displayId's.
# not
# not RETURN STATUS: NVAPI_INVALID_ARGUMENT: hPhysicalGpu or pDisplayIds
# or pDisplayIdCount is NULL
# not    NVAPI_OK: *pDisplayIds contains a set of GPU-output identifiers
# not    NVAPI_NVIDIA_DEVICE_NOT_FOUND: no NVIDIA GPU driving a display
# was found
# not    NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE: hPhysicalGpu was not a
# physical GPU handle
# not \endcode
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetConnectedDisplayIds = hDll.GPU_GetConnectedDisplayIds
NvAPI_GPU_GetConnectedDisplayIds.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetConnectedDisplayIds(__in NvPhysicalGpuHandle hPhysicalGpu,  __inout_ecount_part_opt(*pDisplayIdCount, *pDisplayIdCount) NV_GPU_DISPLAYIDS* pDisplayIds, __inout NvU32* pDisplayIdCount, __in NvU32 flags);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetAllDisplayIds
# not DESCRIPTION: This API returns display IDs for all possible outputs
# on the GPU.
# not    For DPMST connector, it will return display IDs for all the video
# sinks in the topology. \n
# not HOW TO USE: 1. The first call should be made to get the all display
# ID count. To get the display ID count, send in \n
# not    a) hPhysicalGpu - a valid GPU handle(enumerated using
# NvAPI_EnumPhysicalGPUs()) as input, \n
# not
# b) pDisplayIds - NULL, as we just want to get the display ID count.  \n
# not
# c) pDisplayIdCount - a valid pointer to NvU32, whose value is set to ZERO. \n
#
# not    If all parameters are correct and this call is successful, this
# call will return the display ID's count. \n
# not   2. To get the display ID array, make the second call to
# NvAPI_GPU_GetAllDisplayIds() with \n
# not
# a) hPhysicalGpu - should be same value which was sent in first call,  \n
# not
# b) pDisplayIds - pointer to the display ID array allocated by caller based on display ID count, \n
#
# not       eg.
# malloc((ctypes.sizeof(NV_GPU_DISPLAYIDS) * pDisplayIdCount). \n
# not
# c) pDisplayIdCount - a valid pointer to NvU32. This indicates for how many display IDs \n
#
# not       the memory is allocated(pDisplayIds) by the caller.     \n
# not    If all parameters are correct and this call is successful, this
# call will return the display ID array and actual
# not    display ID count
# (which was obtained in the first call to NvAPI_GPU_GetAllDisplayIds). If
# the input display ID count is
# not    less than the actual display ID count, it will overwrite the
# input and give the pDisplayIdCount as actual count and the
# not    API will return NVAPI_INSUFFICIENT_BUFFER.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  hPhysicalGpu  GPU selection.
# not \param [in,out] DisplayIds   Pointer to an array of
# NV_GPU_DISPLAYIDS structures, each entry represents one displayID
# not       and its attributes.
# not \param [in,out] pDisplayIdCount As input, this parameter indicates
# the number of display's id's for which caller has
# not       allocated the memory. As output, it will return the actual
# number of display IDs.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not   specific meaning for this API, they are listed below.
# not
# not \retval NVAPI_INSUFFICIENT_BUFFER When the input buffer(pDisplayIds)
# is less than the actual number of display IDs, this API
# not       will return NVAPI_INSUFFICIENT_BUFFER.
# not
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetAllDisplayIds = hDll.GPU_GetAllDisplayIds
NvAPI_GPU_GetAllDisplayIds.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetAllDisplayIds(__in NvPhysicalGpuHandle hPhysicalGpu, __inout_ecount_part_opt(*pDisplayIdCount, *pDisplayIdCount) NV_GPU_DISPLAYIDS* pDisplayIds, __inout NvU32* pDisplayIdCount);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetConnectedOutputsWithLidState
# not This function is similar to NvAPI_GPU_GetConnectedOutputs(), and
# returns the connected display identifiers that are connected
# not as an output mask but unlike NvAPI_GPU_GetConnectedOutputs() this
# API "always" reflects the Lid State in the output mask.
# not Thus if you expect the LID close state to be available in the
# connection mask use this API.
# not - If LID is closed then this API will remove the LID panel from the
# connected display identifiers.
# not - If LID is open then this API will reflect the LID panel in the
# connected display identifiers.
# not
# not \note This API should be used on notebook systems and on systems
# where the LID state is required in the connection
# not  output mask. On desktop systems the returned identifiers will match
# NvAPI_GPU_GetConnectedOutputs().
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_GPU_GetConnectedDisplayIds.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 95
# not
# not \retval NVAPI_INVALID_ARGUMENT   hPhysicalGpu or pOutputsMask is NULL
# not \retval NVAPI_OK     *pOutputsMask contains a set of GPU-output
# identifiers
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetConnectedOutputsWithLidState = hDll.GPU_GetConnectedOutputsWithLidState
NvAPI_GPU_GetConnectedOutputsWithLidState.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetConnectedOutputsWithLidState(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pOutputsMask);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetConnectedSLIOutputsWithLidState
# not DESCRIPTION: This function is the same as
# NvAPI_GPU_GetConnectedOutputsWithLidState() but returns only the set
# not    of GPU-output identifiers that can be selected in an SLI
# configuration. With SLI disabled,
# not    this function matches NvAPI_GPU_GetConnectedOutputsWithLidState().
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_GPU_GetConnectedDisplayIds.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 170
# not
# not \retval NVAPI_INVALID_ARGUMENT   hPhysicalGpu or pOutputsMask is NULL
# not \retval NVAPI_OK     *pOutputsMask contains a set of GPU-output
# identifiers
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle
# not
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetConnectedSLIOutputsWithLidState = hDll.GPU_GetConnectedSLIOutputsWithLidState
NvAPI_GPU_GetConnectedSLIOutputsWithLidState.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GPU_GetConnectedSLIOutputsWithLidState(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pOutputsMask);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetSystemType
# not \fn
# NvAPI_GPU_GetSystemType(NvPhysicalGpuHandle hPhysicalGpu, NV_SYSTEM_TYPE *pSystemType)
#
# not This function identifies whether the GPU is a notebook GPU or a
# desktop GPU.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 95
# not
# not \retval NVAPI_INVALID_ARGUMENT   hPhysicalGpu or pOutputsMask is NULL
# not \retval NVAPI_OK     *pSystemType contains the GPU system type
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE: hPhysicalGpu was not a
# physical GPU handle
# ///////////////////////////////////////////////////////////////////////
# not \ingroup gpu
# not Used in NvAPI_GPU_GetSystemType()
class NV_SYSTEM_TYPE(ENUM):
    NV_SYSTEM_TYPE_UNKNOWN = 0
    NV_SYSTEM_TYPE_LAPTOP = 1
    NV_SYSTEM_TYPE_DESKTOP = 2


NV_SYSTEM_TYPE_UNKNOWN = NV_SYSTEM_TYPE.NV_SYSTEM_TYPE_UNKNOWN
NV_SYSTEM_TYPE_LAPTOP = NV_SYSTEM_TYPE.NV_SYSTEM_TYPE_LAPTOP
NV_SYSTEM_TYPE_DESKTOP = NV_SYSTEM_TYPE.NV_SYSTEM_TYPE_DESKTOP

# not \ingroup gpu
NvAPI_GPU_GetSystemType = hDll.GPU_GetSystemType
NvAPI_GPU_GetSystemType.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetSystemType(NvPhysicalGpuHandle hPhysicalGpu, NV_SYSTEM_TYPE *pSystemType);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetActiveOutputs
# not This function is the same as NvAPI_GPU_GetAllOutputs but returns
# only the set of GPU output
# not identifiers that are actively driving display devices.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 85
# not
# not \retval NVAPI_INVALID_ARGUMENT   hPhysicalGpu or pOutputsMask is
# NULL.
# not \retval NVAPI_OK     *pOutputsMask contains a set of GPU-output
# identifiers.
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found.
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle.
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetActiveOutputs = hDll.GPU_GetActiveOutputs
NvAPI_GPU_GetActiveOutputs.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetActiveOutputs(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pOutputsMask);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_SetEDID
# not Thus function sets the EDID data for the specified GPU handle and
# connection bit mask.
# not User can either send (Gpu handle & output id) or only display Id in
# variable displayOutputId parameter & hPhysicalGpu parameter can be
# default handle (0).
# not \note The EDID will be cached across the boot session and will be
# enumerated to the OS in this call.
# not  To remove the EDID set (ctypes.sizeofEDID to zero.
# not  OS and NVAPI connection status APIs will reflect the newly set or
# removed EDID dynamically.
# not
# not    This feature will NOT be supported on the following boards:
# not    - GeForce
# not    - Quadro VX
# not    - Tesla
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 100
# not
# not \retval NVAPI_INVALID_ARGUMENT   pEDID is NULL; displayOutputId has
# 0 or > 1 bits set
# not \retval NVAPI_OK     *pEDID data was applied to the requested
# displayOutputId.
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found.
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE: hPhysicalGpu was not a
# physical GPU handle.
# not \retval NVAPI_NOT_SUPPORTED    For the above mentioned GPUs
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_SetEDID = hDll.GPU_SetEDID
NvAPI_GPU_SetEDID.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GPU_SetEDID(NvPhysicalGpuHandle hPhysicalGpu, NvU32 displayOutputId, NV_EDID *pEDID);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetOutputType
# not \fn
# NvAPI_GPU_GetOutputType(NvPhysicalGpuHandle hPhysicalGpu, NvU32 outputId, NV_GPU_OUTPUT_TYPE *pOutputType)
#
# not This function returns the output type. User can either specify both
# 'physical GPU handle and outputId
# (exactly 1 bit set - see \ref handles)' or
# not a valid displayId in the outputId parameter.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \Version Earliest supported ForceWare version: 82.61
# not
# not \retval  NVAPI_INVALID_ARGUMENT   outputId, pOutputType is NULL; or
# if outputId parameter is not displayId and either it has > 1 bit set or
# hPhysicalGpu is NULL.
# not \retval  NVAPI_OK     *pOutputType contains a NvGpuOutputType value
# not \retval  NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found
# not \retval  NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle
# ///////////////////////////////////////////////////////////////////////
# not \ingroup gpu
# not used in NvAPI_GPU_GetOutputType()
class _NV_GPU_OUTPUT_TYPE(ENUM):
    NVAPI_GPU_OUTPUT_UNKNOWN = 0
    NVAPI_GPU_OUTPUT_CRT = 1
    NVAPI_GPU_OUTPUT_DFP = 2
    NVAPI_GPU_OUTPUT_TV = 3


NV_GPU_OUTPUT_TYPE = _NV_GPU_OUTPUT_TYPE

# not \ingroup gpu
NvAPI_GPU_GetOutputType = hDll.GPU_GetOutputType
NvAPI_GPU_GetOutputType.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetOutputType(NvPhysicalGpuHandle hPhysicalGpu, NvU32 outputId, NV_GPU_OUTPUT_TYPE *pOutputType);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_ValidateOutputCombination
# not This function determines if a set of GPU outputs can be active
# not simultaneously. While a GPU may have < n > outputs, typically they
# cannot
# not all be active at the same time due to internal resource sharing.
# not
# not Given a physical GPU handle and a mask of candidate outputs, this
# call
# not will return NVAPI_OK if all of the specified outputs can be driven
# not simultaneously. It will return NVAPI_INVALID_COMBINATION if they
# cannot.
# not
# not Use NvAPI_GPU_GetAllOutputs() to determine which outputs are
# candidates.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 85
# not
# not \retval NVAPI_OK     Combination of outputs in outputsMask are valid
# (can be active simultaneously).
# not \retval NVAPI_INVALID_COMBINATION   Combination of outputs in
# outputsMask are NOT valid.
# not \retval NVAPI_INVALID_ARGUMENT   hPhysicalGpu or outputsMask does
# not have at least 2 bits set.
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle.
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found.
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_ValidateOutputCombination = hDll.GPU_ValidateOutputCombination
NvAPI_GPU_ValidateOutputCombination.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_ValidateOutputCombination(NvPhysicalGpuHandle hPhysicalGpu, NvU32 outputsMask);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetFullName
# not This function retrieves the full GPU name as an ASCII string - for
# example, "Quadro FX 1400".
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 90
# not
# not \return NVAPI_ERROR or NVAPI_OK
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetFullName = hDll.GPU_GetFullName
NvAPI_GPU_GetFullName.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetFullName(NvPhysicalGpuHandle hPhysicalGpu, NvAPI_ShortString szName);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetPCIIdentifiers
# not This function returns the PCI identifiers associated with this GPU.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 90
# not
# not \param DeviceId The internal PCI device identifier for the GPU.
# not \param SubSystemId The internal PCI subsystem identifier for the GPU.
# not \param RevisionId The internal PCI device-specific revision
# identifier for the GPU.
# not \param ExtDeviceId The external PCI device identifier for the GPU.
# not
# not \retval NVAPI_INVALID_ARGUMENT   hPhysicalGpu or an argument is NULL
# not \retval NVAPI_OK     Arguments are populated with PCI identifiers
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetPCIIdentifiers = hDll.GPU_GetPCIIdentifiers
NvAPI_GPU_GetPCIIdentifiers.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GPU_GetPCIIdentifiers(NvPhysicalGpuHandle hPhysicalGpu,NvU32 *pDeviceId,NvU32 *pSubSystemId,NvU32 *pRevisionId,NvU32 *pExtDeviceId);


# not \ingroup gpu
# not Used in NvAPI_GPU_GetGPUType().
class _NV_GPU_TYPE(ENUM):
    NV_SYSTEM_TYPE_GPU_UNKNOWN = 0
    NV_SYSTEM_TYPE_IGPU = 1
    NV_SYSTEM_TYPE_DGPU = 2


NV_GPU_TYPE = _NV_GPU_TYPE

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetGPUType
# not DESCRIPTION: This function returns the GPU type
# (integrated or discrete).
# not   See ::NV_GPU_TYPE.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 173
# not
# not \retval NVAPI_INVALID_ARGUMENT   hPhysicalGpu
# not \retval NVAPI_OK     *pGpuType contains the GPU type
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE: hPhysicalGpu was not a
# physical GPU handle
# not
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetGPUType = hDll.GPU_GetGPUType
NvAPI_GPU_GetGPUType.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GPU_GetGPUType(__in NvPhysicalGpuHandle hPhysicalGpu, __inout NV_GPU_TYPE *pGpuType);


# not \ingroup gpu
# not Used in NvAPI_GPU_GetBusType()
class _NV_GPU_BUS_TYPE(ENUM):
    NVAPI_GPU_BUS_TYPE_UNDEFINED = 0
    NVAPI_GPU_BUS_TYPE_PCI = 1
    NVAPI_GPU_BUS_TYPE_AGP = 2
    NVAPI_GPU_BUS_TYPE_PCI_EXPRESS = 3
    NVAPI_GPU_BUS_TYPE_FPCI = 4
    NVAPI_GPU_BUS_TYPE_AXI = 5


NV_GPU_BUS_TYPE = _NV_GPU_BUS_TYPE

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetBusType
# not This function returns the type of bus associated with this GPU.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 90
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not   specific meaning for this API, they are listed below.
# not \retval NVAPI_INVALID_ARGUMENT   hPhysicalGpu or pBusType is NULL.
# not \retval NVAPI_OK     *pBusType contains bus identifier.
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetBusType = hDll.GPU_GetBusType
NvAPI_GPU_GetBusType.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetBusType(NvPhysicalGpuHandle hPhysicalGpu,NV_GPU_BUS_TYPE *pBusType);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetBusId
# not DESCRIPTION: Returns the ID of the bus associated with this GPU.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 167
# not
# not \retval NVAPI_INVALID_ARGUMENT   hPhysicalGpu or pBusId is NULL.
# not \retval NVAPI_OK     *pBusId contains the bus ID.
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found.
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle.
# not
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetBusId = hDll.GPU_GetBusId
NvAPI_GPU_GetBusId.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetBusId(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pBusId);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetBusSlotId
# not DESCRIPTION: Returns the ID of the bus slot associated with this GPU.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 167
# not
# not \retval NVAPI_INVALID_ARGUMENT   hPhysicalGpu or pBusSlotId is NULL.
# not \retval NVAPI_OK     *pBusSlotId contains the bus slot ID.
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found.
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle.
# not
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetBusSlotId = hDll.GPU_GetBusSlotId
NvAPI_GPU_GetBusSlotId.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetBusSlotId(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pBusSlotId);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetIRQ
# not This function returns the interrupt number associated with this GPU.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 90
# not
# not \retval NVAPI_INVALID_ARGUMENT   hPhysicalGpu or pIRQ is NULL.
# not \retval NVAPI_OK     *pIRQ contains interrupt number.
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found.
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle.
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetIRQ = hDll.GPU_GetIRQ
NvAPI_GPU_GetIRQ.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetIRQ(NvPhysicalGpuHandle hPhysicalGpu,NvU32 *pIRQ);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetVbiosRevision
# not This function returns the revision of the video BIOS associated with
# this GPU.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 90
# not
# not \retval NVAPI_INVALID_ARGUMENT   hPhysicalGpu or pBiosRevision is
# NULL.
# not \retval NVAPI_OK     *pBiosRevision contains revision number.
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found.
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle.
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetVbiosRevision = hDll.GPU_GetVbiosRevision
NvAPI_GPU_GetVbiosRevision.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetVbiosRevision(NvPhysicalGpuHandle hPhysicalGpu,NvU32 *pBiosRevision);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetVbiosOEMRevision
# not This function returns the OEM revision of the video BIOS associated
# with this GPU.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 90
# not
# not \retval NVAPI_INVALID_ARGUMENT   hPhysicalGpu or pBiosRevision is
# NULL
# not \retval NVAPI_OK     *pBiosRevision contains revision number
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetVbiosOEMRevision = hDll.GPU_GetVbiosOEMRevision
NvAPI_GPU_GetVbiosOEMRevision.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetVbiosOEMRevision(NvPhysicalGpuHandle hPhysicalGpu,NvU32 *pBiosRevision);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetVbiosVersionString
# not This function returns the full video BIOS version string in the form
# of xx.xx.xx.xx.yy where
# not - xx numbers come from NvAPI_GPU_GetVbiosRevision() and
# not - yy comes from NvAPI_GPU_GetVbiosOEMRevision().
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 90
# not
# not \retval NVAPI_INVALID_ARGUMENT   hPhysicalGpu is NULL.
# not \retval NVAPI_OK     szBiosRevision contains version string.
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found.
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle.
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetVbiosVersionString = hDll.GPU_GetVbiosVersionString
NvAPI_GPU_GetVbiosVersionString.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetVbiosVersionString(NvPhysicalGpuHandle hPhysicalGpu,NvAPI_ShortString szBiosRevision);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetAGPAperture
# not This function returns the AGP aperture in megabytes.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 90
# not
# not \retval NVAPI_INVALID_ARGUMENT   pSize is NULL.
# not \retval NVAPI_OK     Call successful.
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found.
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle.
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetAGPAperture = hDll.GPU_GetAGPAperture
NvAPI_GPU_GetAGPAperture.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetAGPAperture(NvPhysicalGpuHandle hPhysicalGpu,NvU32 *pSize);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetCurrentAGPRate
# not This function returns the current AGP Rate
# (0 = AGP not present, 1 = 1x, 2 = 2x, etc.).
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 90
# not
# not \retval NVAPI_INVALID_ARGUMENT   pRate is NULL.
# not \retval NVAPI_OK     Call successful.
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found.
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle.
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetCurrentAGPRate = hDll.GPU_GetCurrentAGPRate
NvAPI_GPU_GetCurrentAGPRate.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetCurrentAGPRate(NvPhysicalGpuHandle hPhysicalGpu,NvU32 *pRate);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetCurrentPCIEDownstreamWidth
# not This function returns the number of PCIE lanes being used for the
# PCIE interface
# not downstream from the GPU.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 90
# not
# not \retval NVAPI_INVALID_ARGUMENT   pWidth is NULL.
# not \retval NVAPI_OK     Call successful.
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found.
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle.
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetCurrentPCIEDownstreamWidth = hDll.GPU_GetCurrentPCIEDownstreamWidth
NvAPI_GPU_GetCurrentPCIEDownstreamWidth.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetCurrentPCIEDownstreamWidth(NvPhysicalGpuHandle hPhysicalGpu,NvU32 *pWidth);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetPhysicalFrameBufferSize
# not This function returns the physical size of framebuffer in KB. This
# does NOT include any
# not system RAM that may be dedicated for use by the GPU.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 90
# not
# not \retval NVAPI_INVALID_ARGUMENT   pSize is NULL
# not \retval NVAPI_OK     Call successful
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetPhysicalFrameBufferSize = hDll.GPU_GetPhysicalFrameBufferSize
NvAPI_GPU_GetPhysicalFrameBufferSize.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetPhysicalFrameBufferSize(NvPhysicalGpuHandle hPhysicalGpu,NvU32 *pSize);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetVirtualFrameBufferSize
# not This function returns the virtual size of framebuffer in KB. This
# includes the physical RAM plus any
# not system RAM that has been dedicated for use by the GPU.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 90
# not
# not \retval NVAPI_INVALID_ARGUMENT   pSize is NULL.
# not \retval NVAPI_OK     Call successful.
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND  No NVIDIA GPU driving a
# display was found.
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu was not a
# physical GPU handle.
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetVirtualFrameBufferSize = hDll.GPU_GetVirtualFrameBufferSize
NvAPI_GPU_GetVirtualFrameBufferSize.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetVirtualFrameBufferSize(NvPhysicalGpuHandle hPhysicalGpu,NvU32 *pSize);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetQuadroStatus
# not This function retrieves the Quadro status for the GPU
# (1 if Quadro, 0 if GeForce)
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 80
# not
# not \return NVAPI_ERROR or NVAPI_OK
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetQuadroStatus = hDll.GPU_GetQuadroStatus
NvAPI_GPU_GetQuadroStatus.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetQuadroStatus(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pStatus);


# not \ingroup gpu
_NV_BOARD_INFO._fields_ = [
    # not < structure version
    ('version', NvU32),
    # not < Board Serial Number
    ('BoardNum', NvU8 * 16),
]

NV_BOARD_INFO_VER1 = MAKE_NVAPI_VERSION(NV_BOARD_INFO_V1, 1)

# not \ingroup gpu
NV_BOARD_INFO = NV_BOARD_INFO_V1
# not \ingroup gpu
# not \ingroup gpu
NV_BOARD_INFO_VER = NV_BOARD_INFO_VER1
# END IF


# not SUPPORTED OS: Windows 7 and higher
# not
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetBoardInfo
# not DESCRIPTION: This API Retrieves the Board information
# (a unique GPU Board Serial Number) stored in the InfoROM.
# not
# not \param [in] hPhysicalGpu  Physical GPU Handle.
# not \param [in,out] NV_BOARD_INFO Board Information.
# not
# not TCC_SUPPORTED
# not
# not \retval ::NVAPI_OK    completed request
# not \retval ::NVAPI_ERROR   miscellaneous error occurred
# not \retval ::NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE handle passed is not a
# physical GPU handle
# not \retval ::NVAPI_API_NOT_INTIALIZED  NVAPI not initialized
# not \retval ::NVAPI_INVALID_POINTER   pBoardInfo is NULL
# not \retval ::NVAPI_INCOMPATIBLE_STRUCT_VERSION the version of the INFO
# struct is not supported
# not
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetBoardInfo = hDll.GPU_GetBoardInfo
NvAPI_GPU_GetBoardInfo.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetBoardInfo(NvPhysicalGpuHandle hPhysicalGpu, NV_BOARD_INFO *pBoardInfo);


# ///////////////////////////////////////////////////////////////////////////
# I2C API
# Provides ability to read or write data using I2C protocol.
# These APIs allow I2C access only to DDC monitors
# not \addtogroup i2capi
# not @{
NVAPI_MAX_SIZEOF_I2C_DATA_BUFFER = 4096
NVAPI_MAX_SIZEOF_I2C_REG_ADDRESS = 4
NVAPI_DISPLAY_DEVICE_MASK_MAX = 24
NVAPI_I2C_SPEED_DEPRECATED = 0xFFFF


class NV_I2C_SPEED(ENUM):
    # not < Set i2cSpeedKhz to I2C_SPEED_DEFAULT if default I2C speed is
    # to be chosen, ie.use the current frequency setting.
    NVAPI_I2C_SPEED_DEFAULT = 1
    NVAPI_I2C_SPEED_3KHZ = 2
    NVAPI_I2C_SPEED_10KHZ = 3
    NVAPI_I2C_SPEED_33KHZ = 4
    NVAPI_I2C_SPEED_100KHZ = 5
    NVAPI_I2C_SPEED_200KHZ = 6
    NVAPI_I2C_SPEED_400KHZ = 7


NVAPI_I2C_SPEED_DEFAULT = NV_I2C_SPEED.NVAPI_I2C_SPEED_DEFAULT
NVAPI_I2C_SPEED_3KHZ = NV_I2C_SPEED.NVAPI_I2C_SPEED_3KHZ
NVAPI_I2C_SPEED_10KHZ = NV_I2C_SPEED.NVAPI_I2C_SPEED_10KHZ
NVAPI_I2C_SPEED_33KHZ = NV_I2C_SPEED.NVAPI_I2C_SPEED_33KHZ
NVAPI_I2C_SPEED_100KHZ = NV_I2C_SPEED.NVAPI_I2C_SPEED_100KHZ
NVAPI_I2C_SPEED_200KHZ = NV_I2C_SPEED.NVAPI_I2C_SPEED_200KHZ
NVAPI_I2C_SPEED_400KHZ = NV_I2C_SPEED.NVAPI_I2C_SPEED_400KHZ

# not Used in NvAPI_I2CRead() and NvAPI_I2CWrite()
NV_I2C_INFO_V1._fields_ = [
    # not < The structure version.
    ('version', NvU32),
    # not < The Display Mask of the concerned display.
    ('displayMask', NvU32),
    # not < This flag indicates either the DDC port (TRUE) or the
    # communication port
    ('bIsDDCPort', NvU8),
    # not < The address of the I2C slave. The address should be shifted
    # left by one. For
    ('i2cDevAddress', NvU8),
    # not < The I2C target register address. May be NULL, which indicates
    # no register
    ('pbI2cRegAddress', POINTER(NvU8)),
    # not < The size in bytes of target register address. If
    # pbI2cRegAddress is NULL, this
    ('regAddrSize', NvU32),
    # not < The buffer of data which is to be read or written
    # (depending on the command).
    ('pbData', POINTER(NvU8)),
    # not < The size of the data buffer, pbData, to be read or written.
    ('cbSize', NvU32),
    # not < The target speed of the transaction
    # (between 28Kbps to 40Kbps; not guaranteed).
    ('i2cSpeed', NvU32),
]

# not Used in NvAPI_I2CRead() and NvAPI_I2CWrite()
NV_I2C_INFO_V2._fields_ = [
    # not < The structure version.
    ('version', NvU32),
    # not < The Display Mask of the concerned display.
    ('displayMask', NvU32),
    # not < This flag indicates either the DDC port (TRUE) or the
    # communication port
    ('bIsDDCPort', NvU8),
    # not < The address of the I2C slave. The address should be shifted
    # left by one. For
    ('i2cDevAddress', NvU8),
    # not < The I2C target register address. May be NULL, which indicates
    # no register
    ('pbI2cRegAddress', POINTER(NvU8)),
    # not < The size in bytes of target register address. If
    # pbI2cRegAddress is NULL, this
    ('regAddrSize', NvU32),
    # not < The buffer of data which is to be read or written
    # (depending on the command).
    ('pbData', POINTER(NvU8)),
    # not < The size of the data buffer, pbData, to be read or written.
    ('cbSize', NvU32),
    # not < Deprecated, Must be set to NVAPI_I2C_SPEED_DEPRECATED.
    ('i2cSpeed', NvU32),
    # not < The target speed of the transaction in (kHz)
    # (Chosen from the enum NV_I2C_SPEED).
    ('i2cSpeedKhz', NV_I2C_SPEED),
]

# not Used in NvAPI_I2CRead() and NvAPI_I2CWrite()
NV_I2C_INFO_V3._fields_ = [
    # not < The structure version.
    ('version', NvU32),
    # not < The Display Mask of the concerned display.
    ('displayMask', NvU32),
    # not < This flag indicates either the DDC port (TRUE) or the
    # communication port
    ('bIsDDCPort', NvU8),
    # not < The address of the I2C slave. The address should be shifted
    # left by one. For
    ('i2cDevAddress', NvU8),
    # not < The I2C target register address. May be NULL, which indicates
    # no register
    ('pbI2cRegAddress', POINTER(NvU8)),
    # not < The size in bytes of target register address. If
    # pbI2cRegAddress is NULL, this
    ('regAddrSize', NvU32),
    # not < The buffer of data which is to be read or written
    # (depending on the command).
    ('pbData', POINTER(NvU8)),
    # not < The size of the data buffer, pbData, to be read or written.
    ('cbSize', NvU32),
    # not < Deprecated, Must be set to NVAPI_I2C_SPEED_DEPRECATED.
    ('i2cSpeed', NvU32),
    # not < The target speed of the transaction in (kHz)
    # (Chosen from the enum NV_I2C_SPEED).
    ('i2cSpeedKhz', NV_I2C_SPEED),
    # not < The portid on which device is connected
    # (remember to set bIsPortIdSet if this value is set)
    ('portId', NvU8),
    # not < set this flag on if and only if portid value is set
    ('bIsPortIdSet', NvU32),
]

NV_I2C_INFO = NV_I2C_INFO_V3
NV_I2C_INFO_VER3 = MAKE_NVAPI_VERSION(NV_I2C_INFO_V3, 3)
NV_I2C_INFO_VER2 = MAKE_NVAPI_VERSION(NV_I2C_INFO_V2, 2)
NV_I2C_INFO_VER1 = MAKE_NVAPI_VERSION(NV_I2C_INFO_V1, 1)
NV_I2C_INFO_VER = NV_I2C_INFO_VER3

# not @}
# *************************************************************************
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_I2CRead
# not This function reads the data buffer from the I2C port.
# not   The I2C request must be for a DDC port: pI2cInfo.bIsDDCPort = 1.
# not
# not   A data buffer size larger than 16 bytes may be rejected if a
# register address is specified. In such a case,
# not   NVAPI_ARGUMENT_EXCEED_MAX_SIZE would be returned.
# not
# not   If a register address is specified (i.e. regAddrSize is positive),
# then the transaction will be performed in
# not   the combined format described in the I2C specification. The
# register address will be written, followed by
# not   reading into the data buffer.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 85
# not
# not \param [in] hPhysicalGPU  GPU selection.
# not \param [out] NV_I2C_INFO  *pI2cInfo The I2C data input structure
# not
# not \retval NVAPI_OK     Completed request
# not \retval NVAPI_ERROR     Miscellaneous error occurred.
# not \retval NVAPI_HANDLE_INVALIDATED  Handle passed has been invalidated
# (see user guide).
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE Handle passed is not a
# physical GPU handle.
# not \retval NVAPI_INCOMPATIBLE_STRUCT_VERSION Structure version is not
# supported.
# not \retval NVAPI_INVALID_ARGUMENT - argument does not meet specified
# requirements
# not \retval NVAPI_ARGUMENT_EXCEED_MAX_SIZE - an argument exceeds the
# maximum
# not
# not \ingroup i2capi
# ///////////////////////////////////////////////////////////////////////
NvAPI_I2CRead = hDll.I2CRead
NvAPI_I2CRead.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_I2CRead(NvPhysicalGpuHandle hPhysicalGpu, NV_I2C_INFO *pI2cInfo);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_I2CWrite
# not This function writes the data buffer to the I2C port.
# not
# not   The I2C request must be for a DDC port: pI2cInfo.bIsDDCPort = 1.
# not
# not   A data buffer size larger than 16 bytes may be rejected if a
# register address is specified. In such a case,
# not   NVAPI_ARGUMENT_EXCEED_MAX_SIZE would be returned.
# not
# not   If a register address is specified (i.e. regAddrSize is positive),
# then the register address will be written
# not   and the data buffer will immediately follow without a restart.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 85
# not
# not \param [in] hPhysicalGPU  GPU selection.
# not \param [in] pI2cInfo  The I2C data input structure
# not
# not \retval NVAPI_OK     Completed request
# not \retval NVAPI_ERROR     Miscellaneous error occurred.
# not \retval NVAPI_HANDLE_INVALIDATED  Handle passed has been invalidated
# (see user guide).
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE Handle passed is not a
# physical GPU handle.
# not \retval NVAPI_INCOMPATIBLE_STRUCT_VERSION Structure version is not
# supported.
# not \retval NVAPI_INVALID_ARGUMENT   Argument does not meet specified
# requirements
# not \retval NVAPI_ARGUMENT_EXCEED_MAX_SIZE Argument exceeds the maximum
# not
# not \ingroup i2capi
# ///////////////////////////////////////////////////////////////////////
NvAPI_I2CWrite = hDll.I2CWrite
NvAPI_I2CWrite.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_I2CWrite(NvPhysicalGpuHandle hPhysicalGpu, NV_I2C_INFO *pI2cInfo);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_WorkstationFeatureSetup
# not \fn
# NvAPI_GPU_WorkstationFeatureSetup(NvPhysicalGpuHandle hPhysicalGpu, NvU32 featureEnableMask, NvU32 featureDisableMask)
#
# not DESCRIPTION: This API configures the driver for a set of workstation
# features.
# not    The driver can allocate the memory resources accordingly.
# not
# not SUPPORTED OS: Windows 7
# not
# not
# not \param [in] hPhysicalGpu  Physical GPU Handle of the display adapter
# to be configured. GPU handles may be retrieved
# not       using NvAPI_EnumPhysicalGPUs. A value of NULL is permitted and
# applies the same operation
# not       to all GPU handles enumerated by NvAPI_EnumPhysicalGPUs.
# not \param [in] featureEnableMask Mask of features the caller requests
# to enable for use
# not \param [in] featureDisableMask Mask of features the caller requests
# to disable
# not
# not    As a general rule, features in the enable and disable masks are
# expected to be disjoint, although the disable
# not    mask has precedence and a feature flagged in both masks will be
# disabled.
# not
# not \retval ::NVAPI_OK     configuration request succeeded
# not \retval ::NVAPI_ERROR     configuration request failed
# not \retval ::NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu is not a
# physical GPU handle.
# not \retval ::NVAPI_GPU_WORKSTATION_FEATURE_INCOMPLETE requested feature
# set does not have all resources allocated for completeness.
# not \retval ::NVAPI_NO_IMPLEMENTATION   OS below Win7, implemented only
# for Win7 but returns NVAPI_OK on OS above Win7 to
# not        keep compatibility with apps written against Win7.
# ///////////////////////////////////////////////////////////////////////
# not \ingroup gpu
class NVAPI_GPU_WORKSTATION_FEATURE_MASK(ENUM):
    NVAPI_GPU_WORKSTATION_FEATURE_MASK_SWAPGROUP = 0x00000001
    NVAPI_GPU_WORKSTATION_FEATURE_MASK_STEREO = 0x00000010
    NVAPI_GPU_WORKSTATION_FEATURE_MASK_WARPING = 0x00000100
    NVAPI_GPU_WORKSTATION_FEATURE_MASK_PIXINTENSITY = 0x00000200
    NVAPI_GPU_WORKSTATION_FEATURE_MASK_GRAYSCALE = 0x00000400
    NVAPI_GPU_WORKSTATION_FEATURE_MASK_BPC10 = 0x00001000


NVAPI_GPU_WORKSTATION_FEATURE_MASK_SWAPGROUP = NVAPI_GPU_WORKSTATION_FEATURE_MASK.NVAPI_GPU_WORKSTATION_FEATURE_MASK_SWAPGROUP
NVAPI_GPU_WORKSTATION_FEATURE_MASK_STEREO = NVAPI_GPU_WORKSTATION_FEATURE_MASK.NVAPI_GPU_WORKSTATION_FEATURE_MASK_STEREO
NVAPI_GPU_WORKSTATION_FEATURE_MASK_WARPING = NVAPI_GPU_WORKSTATION_FEATURE_MASK.NVAPI_GPU_WORKSTATION_FEATURE_MASK_WARPING
NVAPI_GPU_WORKSTATION_FEATURE_MASK_PIXINTENSITY = NVAPI_GPU_WORKSTATION_FEATURE_MASK.NVAPI_GPU_WORKSTATION_FEATURE_MASK_PIXINTENSITY
NVAPI_GPU_WORKSTATION_FEATURE_MASK_GRAYSCALE = NVAPI_GPU_WORKSTATION_FEATURE_MASK.NVAPI_GPU_WORKSTATION_FEATURE_MASK_GRAYSCALE
NVAPI_GPU_WORKSTATION_FEATURE_MASK_BPC10 = NVAPI_GPU_WORKSTATION_FEATURE_MASK.NVAPI_GPU_WORKSTATION_FEATURE_MASK_BPC10

# not \ingroup gpu
NvAPI_GPU_WorkstationFeatureSetup = hDll.GPU_WorkstationFeatureSetup
NvAPI_GPU_WorkstationFeatureSetup.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_WorkstationFeatureSetup(__in NvPhysicalGpuHandle hPhysicalGpu, __in NvU32 featureEnableMask, __in NvU32 featureDisableMask);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_WorkstationFeatureQuery
# not DESCRIPTION: This API queries the current set of workstation
# features.
# not
# not SUPPORTED OS: Windows 7
# not
# not
# not \param [in] hPhysicalGpu  Physical GPU Handle of the display adapter
# to be configured. GPU handles may be retrieved
# not       using NvAPI_EnumPhysicalGPUs.
# not \param [out] pConfiguredFeatureMask Mask of features requested for
# use by client drivers
# not \param [out] pConsistentFeatureMask Mask of features that have all
# resources allocated for completeness.
# not
# not \retval ::NVAPI_OK     configuration request succeeded
# not \retval ::NVAPI_ERROR     configuration request failed
# not \retval ::NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE hPhysicalGpu is not a
# physical GPU handle.
# not \retval ::NVAPI_NO_IMPLEMENTATION   OS below Win7, implemented only
# for Win7 but returns NVAPI_OK on OS above Win7 to
# not        keep compatibility with apps written against Win7.
# ///////////////////////////////////////////////////////////////////////
# not \ingroup gpu
NvAPI_GPU_WorkstationFeatureQuery = hDll.GPU_WorkstationFeatureQuery
NvAPI_GPU_WorkstationFeatureQuery.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GPU_WorkstationFeatureQuery(__in NvPhysicalGpuHandle hPhysicalGpu, __out_opt NvU32 *pConfiguredFeatureMask, __out_opt NvU32 *pConsistentFeatureMask);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetHDCPSupportStatus
# not \fn
# NvAPI_GPU_GetHDCPSupportStatus(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_GET_HDCP_SUPPORT_STATUS *pGetHDCPSupportStatus)
#
# not DESCRIPTION: This function returns a GPU's HDCP support status.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 175
# not
# not \retval ::NVAPI_OK
# not \retval ::NVAPI_ERROR
# not \retval ::NVAPI_INVALID_ARGUMENT
# not \retval ::NVAPI_HANDLE_INVALIDATED
# not \retval ::NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE
# not \retval ::NVAPI_INCOMPATIBLE_STRUCT_VERSION
# ////////////////////////////////////////////////////////////////////////
# not \addtogroup gpu
# not @{
# not HDCP fuse states - used in NV_GPU_GET_HDCP_SUPPORT_STATUS
class _NV_GPU_HDCP_FUSE_STATE(ENUM):
    NV_GPU_HDCP_FUSE_STATE_UNKNOWN = 0
    NV_GPU_HDCP_FUSE_STATE_DISABLED = 1
    NV_GPU_HDCP_FUSE_STATE_ENABLED = 2


NV_GPU_HDCP_FUSE_STATE = _NV_GPU_HDCP_FUSE_STATE


# not HDCP key sources - used in NV_GPU_GET_HDCP_SUPPORT_STATUS
class _NV_GPU_HDCP_KEY_SOURCE(ENUM):
    NV_GPU_HDCP_KEY_SOURCE_UNKNOWN = 0
    NV_GPU_HDCP_KEY_SOURCE_NONE = 1
    NV_GPU_HDCP_KEY_SOURCE_CRYPTO_ROM = 2
    NV_GPU_HDCP_KEY_SOURCE_SBIOS = 3
    NV_GPU_HDCP_KEY_SOURCE_I2C_ROM = 4
    NV_GPU_HDCP_KEY_SOURCE_FUSES = 5


NV_GPU_HDCP_KEY_SOURCE = _NV_GPU_HDCP_KEY_SOURCE


# not HDCP key source states - used in NV_GPU_GET_HDCP_SUPPORT_STATUS
class _NV_GPU_HDCP_KEY_SOURCE_STATE(ENUM):
    NV_GPU_HDCP_KEY_SOURCE_STATE_UNKNOWN = 0
    NV_GPU_HDCP_KEY_SOURCE_STATE_ABSENT = 1
    NV_GPU_HDCP_KEY_SOURCE_STATE_PRESENT = 2


NV_GPU_HDCP_KEY_SOURCE_STATE = _NV_GPU_HDCP_KEY_SOURCE_STATE

# not HDPC support status - used in NvAPI_GPU_GetHDCPSupportStatus()
NV_GPU_GET_HDCP_SUPPORT_STATUS._fields_ = [
    # not Structure version constucted by macro
    # NV_GPU_GET_HDCP_SUPPORT_STATUS
    ('version', NvU32),
    # not GPU's HDCP fuse state
    ('hdcpFuseState', NV_GPU_HDCP_FUSE_STATE),
    # not GPU's HDCP key source
    ('hdcpKeySource', NV_GPU_HDCP_KEY_SOURCE),
    # not GPU's HDCP key source state
    ('hdcpKeySourceState', NV_GPU_HDCP_KEY_SOURCE_STATE),
]

# not Macro for constructing the version for structure
# NV_GPU_GET_HDCP_SUPPORT_STATUS
NV_GPU_GET_HDCP_SUPPORT_STATUS_VER = (
    MAKE_NVAPI_VERSION(NV_GPU_GET_HDCP_SUPPORT_STATUS, 1)
)

# not @}
# not \ingroup gpu
NvAPI_GPU_GetHDCPSupportStatus = hDll.GPU_GetHDCPSupportStatus
NvAPI_GPU_GetHDCPSupportStatus.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetHDCPSupportStatus(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_GET_HDCP_SUPPORT_STATUS *pGetHDCPSupportStatus);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetTachReading
# not DESCRIPTION: This API retrieves the fan speed tachometer reading for
# the specified physical GPU.
# not
# not HOW TO USE:
# not   - NvU32 Value = 0;
# not   - ret = NvAPI_GPU_GetTachReading(hPhysicalGpu, & Value);
# not   - On call success:
# not   - Value contains the tachometer reading
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \param [in] hPhysicalGpu GPU selection.
# not \param [out] pValue  Pointer to a variable to get the tachometer
# reading
# not
# not \retval ::NVAPI_OK - completed request
# not \retval ::NVAPI_ERROR - miscellaneous error occurred
# not \retval ::NVAPI_NOT_SUPPORTED - functionality not supported
# not \retval ::NVAPI_API_NOT_INTIALIZED - nvapi not initialized
# not \retval ::NVAPI_INVALID_ARGUMENT - invalid argument passed
# not \retval ::NVAPI_HANDLE_INVALIDATED - handle passed has been
# invalidated (see user guide)
# not \retval ::NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE - handle passed is not
# a physical GPU handle
# not
# not \ingroup gpucooler
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetTachReading = hDll.GPU_GetTachReading
NvAPI_GPU_GetTachReading.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GPU_GetTachReading(NvPhysicalGpuHandle hPhysicalGPU, NvU32 *pValue);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetECCStatusInfo
# not \fn NvAPI_GPU_GetECCStatusInfo(NvPhysicalGpuHandle hPhysicalGpu,
# not        NV_GPU_ECC_STATUS_INFO *pECCStatusInfo);
# not DESCRIPTION:  This function returns ECC memory status information.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \param [in] hPhysicalGpu A handle identifying the physical GPU for
# which ECC
# not       status information is to be retrieved.
# not \param [out]  pECCStatusInfo A pointer to an ECC status structure.
# not
# not \retval ::NVAPI_OK   The request was completed successfully.
# not \retval ::NVAPI_ERROR   An unknown error occurred.
# not \retval ::NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE The provided GPU handle
# is not a physical GPU handle.
# not \retval ::NVAPI_INVALID_HANDLE The provided GPU handle is invalid.
# not \retval ::NVAPI_HANDLE_INVALIDATED The provided GPU handle is no
# longer valid.
# not \retval ::NVAPI_INVALID_POINTER  An invalid argument pointer was
# provided.
# not \retval ::NVAPI_NOT_SUPPORTED  The request is not supported.
# not \retval ::NVAPI_API_NOT_INTIALIZED NvAPI was not yet initialized.
# ///////////////////////////////////////////////////////////////////////

# not \addtogroup gpuecc
# not Used in NV_GPU_ECC_STATUS_INFO.
class _NV_ECC_CONFIGURATION(ENUM):
    NV_ECC_CONFIGURATION_NOT_SUPPORTED = 0
    NV_ECC_CONFIGURATION_DEFERRED = 1
    NV_ECC_CONFIGURATION_IMMEDIATE = 2


NV_ECC_CONFIGURATION = _NV_ECC_CONFIGURATION

# not \ingroup gpuecc
# not Used in NvAPI_GPU_GetECCStatusInfo().
NV_GPU_ECC_STATUS_INFO._fields_ = [
    # not < Structure version
    ('version', NvU32),
    # not < ECC memory feature support
    ('isSupported', NvU32, 1),
    # not < Supported ECC memory feature configuration options
    ('configurationOptions', NV_ECC_CONFIGURATION),
    # not < Active ECC memory setting
    ('isEnabled', NvU32, 1),
]

# not \ingroup gpuecc
# not Macro for constructing the version field of NV_GPU_ECC_STATUS_INFO
NV_GPU_ECC_STATUS_INFO_VER = (
    MAKE_NVAPI_VERSION(NV_GPU_ECC_STATUS_INFO, 1)
)

# not \ingroup gpuecc
NvAPI_GPU_GetECCStatusInfo = hDll.GPU_GetECCStatusInfo
NvAPI_GPU_GetECCStatusInfo.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GPU_GetECCStatusInfo(NvPhysicalGpuHandle hPhysicalGpu,
#                                           NV_GPU_ECC_STATUS_INFO *pECCStatusInfo);


# not \ingroup gpuecc
# not Used in NvAPI_GPU_GetECCErrorInfo()/
class current(ctypes.Structure):
    pass


current._fields_ = [
    # not < Number of single-bit ECC errors detected since last boot
    ('singleBitErrors', NvU64),
    # not < Number of double-bit ECC errors detected since last boot
    ('doubleBitErrors', NvU64),
]
NV_GPU_ECC_ERROR_INFO.current = current


class aggregate(ctypes.Structure):
    pass


aggregate._fields_ = [
    # not < Number of single-bit ECC errors detected since last counter
    # reset
    ('singleBitErrors', NvU64),
    # not < Number of double-bit ECC errors detected since last counter
    # reset
    ('doubleBitErrors', NvU64),
]
NV_GPU_ECC_ERROR_INFO.aggregate = aggregate

NV_GPU_ECC_ERROR_INFO._fields_ = [
    # not < Structure version
    ('version', NvU32),
    ('current', NV_GPU_ECC_ERROR_INFO.current),
    ('aggregate', NV_GPU_ECC_ERROR_INFO.aggregate),
]

# not \ingroup gpuecc
# not Macro for constructing the version field of NV_GPU_ECC_ERROR_INFO
NV_GPU_ECC_ERROR_INFO_VER = MAKE_NVAPI_VERSION(NV_GPU_ECC_ERROR_INFO, 1)

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetECCErrorInfo
# not \fn NvAPI_GPU_GetECCErrorInfo(NvPhysicalGpuHandle hPhysicalGpu,
# not        NV_GPU_ECC_ERROR_INFO *pECCErrorInfo);
# not
# not DESCRIPTION:  This function returns ECC memory error information.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \param [in] hPhysicalGpu A handle identifying the physical GPU for
# not      which ECC error information is to be
# not      retrieved.
# not \param [out]  pECCErrorInfo A pointer to an ECC error structure.
# not
# not \retval ::NVAPI_OK The request was completed successfully.
# not \retval ::NVAPI_ERROR An unknown error occurred.
# not \retval ::NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE The provided GPU handle
# is not a physical GPU handle.
# not \retval ::NVAPI_INVALID_ARGUMENT incorrect param value
# not \retval ::NVAPI_INVALID_POINTER An invalid argument pointer was
# provided.
# not \retval ::NVAPI_INCOMPATIBLE_STRUCT_VERSION structure version is not
# supported, initialize to NV_GPU_ECC_ERROR_INFO_VER.
# not \retval ::NVAPI_HANDLE_INVALIDATED The provided GPU handle is no
# longer valid.
# not \retval ::NVAPI_NOT_SUPPORTED The request is not supported.
# not \retval ::NVAPI_API_NOT_INTIALIZED NvAPI was not yet initialized.
# ///////////////////////////////////////////////////////////////////////
# not \ingroup gpuecc
NvAPI_GPU_GetECCErrorInfo = hDll.GPU_GetECCErrorInfo
NvAPI_GPU_GetECCErrorInfo.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetECCErrorInfo(NvPhysicalGpuHandle hPhysicalGpu,
#                                          NV_GPU_ECC_ERROR_INFO *pECCErrorInfo);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_ResetECCErrorInfo
# not DESCRIPTION:  This function resets ECC memory error counters.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \requires Administrator privileges since release 430.39
# not
# not \param [in]  hPhysicalGpu  A handle identifying the physical GPU for
# not       which ECC error information is to be
# not       cleared.
# not \param [in]  bResetCurrent Reset the current ECC error counters.
# not \param [in]  bResetAggregate Reset the aggregate ECC error counters.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not   specific meaning for this API, they are listed below.
# not
# not \retval ::NVAPI_INVALID_USER_PRIVILEGE  - The application will
# require Administrator privileges to access this API.
# not         The application can be elevated to a higher permission level
# by selecting "Run as Administrator".
# not
# not \ingroup gpuecc
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_ResetECCErrorInfo = hDll.GPU_ResetECCErrorInfo
NvAPI_GPU_ResetECCErrorInfo.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_ResetECCErrorInfo(NvPhysicalGpuHandle hPhysicalGpu, NvU8 bResetCurrent,
#                                             NvU8 bResetAggregate);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetECCConfigurationInfo
# not \fn
# NvAPI_GPU_GetECCConfigurationInfo(NvPhysicalGpuHandle hPhysicalGpu,
# not     NV_GPU_ECC_CONFIGURATION_INFO *pECCConfigurationInfo);
# not DESCRIPTION:  This function returns ECC memory configuration
# information.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \param [in] hPhysicalGpu A handle identifying the physical GPU for
# not      which ECC configuration information
# not      is to be retrieved.
# not \param [out]  pECCConfigurationInfo A pointer to an ECC
# not         configuration structure.
# not
# not \retval ::NVAPI_OK The request was completed successfully.
# not \retval ::NVAPI_ERROR An unknown error occurred.
# not \retval ::NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE The provided GPU handle
# is not a physical GPU handle.
# not \retval ::NVAPI_INVALID_HANDLE The provided GPU handle is invalid.
# not \retval ::NVAPI_HANDLE_INVALIDATED The provided GPU handle is no
# longer valid.
# not \retval ::NVAPI_INVALID_POINTER An invalid argument pointer was
# provided.
# not \retval ::NVAPI_NOT_SUPPORTED The request is not supported.
# not \retval ::NVAPI_API_NOT_INTIALIZED NvAPI was not yet initialized.
# ///////////////////////////////////////////////////////////////////////
# not \ingroup gpuecc
# not Used in NvAPI_GPU_GetECCConfigurationInfo().
NV_GPU_ECC_CONFIGURATION_INFO._fields_ = [
    # not Structure version
    ('version', NvU32),
    # not Current ECC configuration stored in non-volatile memory
    ('isEnabled', NvU32, 1),
    # not Factory default ECC configuration (static)
    ('isEnabledByDefault', NvU32, 1),
]

# not \ingroup gpuecc
# not Macro for consstructing the verion field of
# NV_GPU_ECC_CONFIGURATION_INFO
NV_GPU_ECC_CONFIGURATION_INFO_VER = (
    MAKE_NVAPI_VERSION(NV_GPU_ECC_CONFIGURATION_INFO, 1)
)

# not \ingroup gpuecc
NvAPI_GPU_GetECCConfigurationInfo = hDll.GPU_GetECCConfigurationInfo
NvAPI_GPU_GetECCConfigurationInfo.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetECCConfigurationInfo(NvPhysicalGpuHandle hPhysicalGpu,
#                                                  NV_GPU_ECC_CONFIGURATION_INFO *pECCConfigurationInfo);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_SetECCConfiguration
# not DESCRIPTION:  This function updates the ECC memory configuration
# setting.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \requires Administrator privileges since release 430.39
# not
# not \param [in] hPhysicalGpu A handle identifying the physical GPU for
# not       which to update the ECC configuration
# not       setting.
# not \param [in] bEnable  The new ECC configuration setting.
# not \param [in] bEnableImmediately Request that the new setting take
# effect immediately.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not   specific meaning for this API, they are listed below.
# not
# not \retval ::NVAPI_INVALID_CONFIGURATION  - Possibly SLI is enabled.
# Disable SLI and retry.
# not \retval ::NVAPI_INVALID_USER_PRIVILEGE  - The application will
# require Administrator privileges to access this API.
# not         The application can be elevated to a higher permission level
# by selecting "Run as Administrator".
# not
# not \ingroup gpuecc
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_SetECCConfiguration = hDll.GPU_SetECCConfiguration
NvAPI_GPU_SetECCConfiguration.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GPU_SetECCConfiguration(NvPhysicalGpuHandle hPhysicalGpu, NvU8 bEnable,
#                                              NvU8 bEnableImmediately);


# not \ingroup gpu
class _NV_GPU_WORKSTATION_FEATURE_TYPE(ENUM):
    NV_GPU_WORKSTATION_FEATURE_TYPE_QUADRO_VR_READY = 1


NV_GPU_WORKSTATION_FEATURE_TYPE = _NV_GPU_WORKSTATION_FEATURE_TYPE

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_QueryWorkstationFeatureSupport
# not \fn
# NvAPI_GPU_QueryWorkstationFeatureSupport(NvPhysicalGpuHandle physicalGpu, NV_GPU_WORKSTATION_FEATURE_TYPE gpuWorkstationFeature)
#
# not \code
# not DESCRIPTION:  Indicates whether a queried workstation feature is
# supported by the requested GPU.
# not
# not SUPPORTED OS: Windows 10 and higher
# not
# not \since Release: 440
# not
# not DESCRIPTION:  This API, when called with a valid physical gpu handle
# as Input, lets caller know whether the given workstation feature is
# supported by this GPU.
# not
# not PARAMETERS: physicalGpu(IN)  : The handle of the GPU for the which
# caller wants to get the support information.
# not    gpuWorkstationFeature(IN ) : The feature for the GPU in question.
# One of the values from enum NV_GPU_WORKSTATION_FEATURE_TYPE.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status listed below
# not
# not \retval ::NVAPI_OK the queried workstation feature is supported on
# the given GPU.
# not \retval ::NVAPI_NO_IMPLEMENTATION the current driver doesn't support
# this interface.
# not \retval ::NVAPI_INVALID_HANDLE the incoming physicalGpu handle is
# invalid.
# not \retval ::NVAPI_NOT_SUPPORTED the requested gpuWorkstationFeature is
# not supported in the selected GPU.
# not \retval ::NVAPI_SETTING_NOT_FOUND the requested
# gpuWorkstationFeature is unknown to the current driver version.
# not
# not \endcode
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_QueryWorkstationFeatureSupport = hDll.GPU_QueryWorkstationFeatureSupport
NvAPI_GPU_QueryWorkstationFeatureSupport.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_QueryWorkstationFeatureSupport(NvPhysicalGpuHandle physicalGpu, NV_GPU_WORKSTATION_FEATURE_TYPE gpuWorkstationFeature);


# not \ingroup gpu
NV_SCANOUT_INTENSITY_DATA_V1._fields_ = [
    # not < version of this structure
    ('version', NvU32),
    # not < width of the input texture
    ('width', NvU32),
    # not < height of the input texture
    ('height', NvU32),
    # not < array of floating values building an intensity RGB texture
    ('blendingTexture', POINTER(FLOAT)),
]

# not \ingroup gpu
NV_SCANOUT_INTENSITY_DATA_V2._fields_ = [
    # not < version of this structure
    ('version', NvU32),
    # not < width of the input texture
    ('width', NvU32),
    # not < height of the input texture
    ('height', NvU32),
    # not < array of floating values building an intensity RGB texture
    ('blendingTexture', POINTER(FLOAT)),
    # not < array of floating values building an offset texture
    ('offsetTexture', POINTER(FLOAT)),
    # not < number of channels per pixel in the offset texture
    ('offsetTexChannels', NvU32),
]
NV_SCANOUT_INTENSITY_DATA = NV_SCANOUT_INTENSITY_DATA_V2

# not \ingroup gpu
NV_SCANOUT_INTENSITY_DATA_VER1 = (
    MAKE_NVAPI_VERSION(NV_SCANOUT_INTENSITY_DATA_V1, 1)
)
NV_SCANOUT_INTENSITY_DATA_VER2 = (
    MAKE_NVAPI_VERSION(NV_SCANOUT_INTENSITY_DATA_V2, 2)
)
NV_SCANOUT_INTENSITY_DATA_VER = NV_SCANOUT_INTENSITY_DATA_VER2

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_SetScanoutIntensity
# not DESCRIPTION: This API enables and sets up per-pixel intensity
# feature on the specified display.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] displayId   combined physical display and GPU identifier
# of the display to apply the intensity control.
# not \param [in] scanoutIntensityData the intensity texture info.
# not \param [out] pbSticky(OUT)   indicates whether the settings will be
# kept over a reboot.
# not
# not \retval ::NVAPI_INVALID_ARGUMENT Invalid input parameters.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI not initialized.
# not \retval ::NVAPI_NOT_SUPPORTED Interface not supported by the driver
# used, or only supported on selected GPUs
# not \retval ::NVAPI_INVALID_ARGUMENT Invalid input data.
# not \retval ::NVAPI_INCOMPATIBLE_STRUCT_VERSION
# NV_SCANOUT_INTENSITY_DATA structure version mismatch.
# not \retval ::NVAPI_OK Feature enabled.
# not \retval ::NVAPI_ERROR Miscellaneous error occurred.
# not
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_SetScanoutIntensity = hDll.GPU_SetScanoutIntensity
NvAPI_GPU_SetScanoutIntensity.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_SetScanoutIntensity(NvU32 displayId, NV_SCANOUT_INTENSITY_DATA* scanoutIntensityData, int *pbSticky);


# not \ingroup gpu
_NV_SCANOUT_INTENSITY_STATE_DATA._fields_ = [
    # not < version of this structure
    ('version', NvU32),
    # not < intensity is enabled or not
    ('bEnabled', NvU32),
]

# not \ingroup gpu
NV_SCANOUT_INTENSITY_STATE_VER = (
    MAKE_NVAPI_VERSION(NV_SCANOUT_INTENSITY_STATE_DATA, 1)
)

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetScanoutIntensityState
# not DESCRIPTION: This API queries current state of the intensity feature
# on the specified display.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  displayId     combined physical display and GPU
# identifier of the display to query the configuration.
# not \param [in,out] scanoutIntensityStateData  intensity state data.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not   specific meaning for this API, they are listed below.
# not
# not \retval ::NVAPI_INVALID_ARGUMENT Invalid input parameters.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI not initialized.
# not \retval ::NVAPI_NOT_SUPPORTED Interface not supported by the driver
# used, or only supported on selected GPUs.
# not \retval ::NVAPI_OK Feature enabled.
# not \retval ::NVAPI_ERROR Miscellaneous error occurred.
# not
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetScanoutIntensityState = hDll.GPU_GetScanoutIntensityState
NvAPI_GPU_GetScanoutIntensityState.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GPU_GetScanoutIntensityState(__in NvU32 displayId, __inout NV_SCANOUT_INTENSITY_STATE_DATA* scanoutIntensityStateData);


# not \ingroup gpu
class NV_GPU_WARPING_VERTICE_FORMAT(ENUM):
    NV_GPU_WARPING_VERTICE_FORMAT_TRIANGLESTRIP_XYUVRQ = 0
    NV_GPU_WARPING_VERTICE_FORMAT_TRIANGLES_XYUVRQ = 1


NV_GPU_WARPING_VERTICE_FORMAT_TRIANGLESTRIP_XYUVRQ = NV_GPU_WARPING_VERTICE_FORMAT.NV_GPU_WARPING_VERTICE_FORMAT_TRIANGLESTRIP_XYUVRQ
NV_GPU_WARPING_VERTICE_FORMAT_TRIANGLES_XYUVRQ = NV_GPU_WARPING_VERTICE_FORMAT.NV_GPU_WARPING_VERTICE_FORMAT_TRIANGLES_XYUVRQ

# not \ingroup gpu
NV_SCANOUT_WARPING_DATA._fields_ = [
    # not < version of this structure
    ('version', NvU32),
    # not < width of the input texture
    ('vertices', POINTER(FLOAT)),
    # not < format of the input vertices
    ('vertexFormat', NV_GPU_WARPING_VERTICE_FORMAT),
    # not < number of the input vertices
    ('numVertices', INT),
    # not < rectangle in desktop coordinates describing the source area
    # for the warping
    ('textureRect', POINTER(NvSBox)),
]

# not \ingroup gpu
NV_SCANOUT_WARPING_VER = MAKE_NVAPI_VERSION(NV_SCANOUT_WARPING_DATA, 1)

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_SetScanoutWarping
# not DESCRIPTION: This API enables and sets up the warping feature on the
# specified display.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] displayId   Combined physical display and GPU identifier
# of the display to apply the intensity control
# not \param [in] scanoutWarpingData The warping data info
# not \param [out] pbSticky   Indicates whether the settings will be kept
# over a reboot.
# not
# not \retval ::NVAPI_INVALID_ARGUMENT Invalid input parameters.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI not initialized.
# not \retval ::NVAPI_NOT_SUPPORTED Interface not supported by the driver
# used, or only supported on selected GPUs
# not \retval ::NVAPI_INVALID_ARGUMENT Invalid input data.
# not \retval ::NVAPI_INCOMPATIBLE_STRUCT_VERSION NV_SCANOUT_WARPING_DATA
# structure version mismatch.
# not \retval ::NVAPI_OK Feature enabled.
# not \retval ::NVAPI_ERROR Miscellaneous error occurred.
# not
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_SetScanoutWarping = hDll.GPU_SetScanoutWarping
NvAPI_GPU_SetScanoutWarping.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_SetScanoutWarping(NvU32 displayId, NV_SCANOUT_WARPING_DATA* scanoutWarpingData, int* piMaxNumVertices, int* pbSticky);


# not \ingroup gpu
_NV_SCANOUT_WARPING_STATE_DATA._fields_ = [
    # not < version of this structure
    ('version', NvU32),
    # not < warping is enabled or not
    ('bEnabled', NvU32),
]

# not \ingroup gpu
NV_SCANOUT_WARPING_STATE_VER = (
    MAKE_NVAPI_VERSION(NV_SCANOUT_WARPING_STATE_DATA, 1)
)

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetScanoutWarpingState
# not DESCRIPTION: This API queries current state of the warping feature
# on the specified display.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  displayId    combined physical display and GPU
# identifier of the display to query the configuration.
# not \param [in,out] scanoutWarpingStateData  warping state data.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not   specific meaning for this API, they are listed below.
# not
# not \retval ::NVAPI_INVALID_ARGUMENT Invalid input parameters.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI not initialized.
# not \retval ::NVAPI_NOT_SUPPORTED Interface not supported by the driver
# used, or only supported on selected GPUs.
# not \retval ::NVAPI_OK Feature enabled.
# not \retval ::NVAPI_ERROR Miscellaneous error occurred.
# not
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetScanoutWarpingState = hDll.GPU_GetScanoutWarpingState
NvAPI_GPU_GetScanoutWarpingState.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GPU_GetScanoutWarpingState(__in NvU32 displayId, __inout NV_SCANOUT_WARPING_STATE_DATA* scanoutWarpingStateData);


class NV_GPU_SCANOUT_COMPOSITION_PARAMETER(ENUM):
    NV_GPU_SCANOUT_COMPOSITION_PARAMETER_WARPING_RESAMPLING_METHOD = 0


NV_GPU_SCANOUT_COMPOSITION_PARAMETER_WARPING_RESAMPLING_METHOD = NV_GPU_SCANOUT_COMPOSITION_PARAMETER.NV_GPU_SCANOUT_COMPOSITION_PARAMETER_WARPING_RESAMPLING_METHOD


# not This enum defines a collection of possible scanout composition
# values that can be used to configure
# not possible scanout composition settings.
# (Currently the only parameter defined is the WARPING_RESAMPLING_METHOD).
class NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE(ENUM):
    NV_GPU_SCANOUT_COMPOSITION_PARAMETER_SET_TO_DEFAULT = 0
    NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BILINEAR = (
        0x100
    )
    NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BICUBIC_TRIANGULAR = (
        0x101
    )
    NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BICUBIC_BELL_SHAPED = (
        0x102
    )
    NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BICUBIC_BSPLINE = (
        0x103
    )
    NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BICUBIC_ADAPTIVE_TRIANGULAR = (
        0x104
    )
    NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BICUBIC_ADAPTIVE_BELL_SHAPED = (
        0x105
    )
    NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BICUBIC_ADAPTIVE_BSPLINE = (
        0x106
    )


NV_GPU_SCANOUT_COMPOSITION_PARAMETER_SET_TO_DEFAULT = NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE.NV_GPU_SCANOUT_COMPOSITION_PARAMETER_SET_TO_DEFAULT
NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BILINEAR = NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE.NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BILINEAR
NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BICUBIC_TRIANGULAR = NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE.NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BICUBIC_TRIANGULAR
NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BICUBIC_BELL_SHAPED = NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE.NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BICUBIC_BELL_SHAPED
NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BICUBIC_BSPLINE = NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE.NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BICUBIC_BSPLINE
NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BICUBIC_ADAPTIVE_TRIANGULAR = NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE.NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BICUBIC_ADAPTIVE_TRIANGULAR
NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BICUBIC_ADAPTIVE_BELL_SHAPED = NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE.NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BICUBIC_ADAPTIVE_BELL_SHAPED
NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BICUBIC_ADAPTIVE_BSPLINE = NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE.NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE_WARPING_RESAMPLING_METHOD_BICUBIC_ADAPTIVE_BSPLINE

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_SetScanoutCompositionParameter
# not DESCRIPTION: This API sets various parameters that configure the
# scanout composition feature on the specified display.
# not
# (currently there is only one configurable parameter defined: WARPING_RESAMPLING_METHOD,
#
# not   but this function is designed to support the addition of
# parameters as needed.)
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] displayId   Combined physical display and GPU identifier
# of the display to apply the intensity control
# not \param [in] parameter   The scanout composition parameter to be set
# not \param [in] parameterValue  The data to be set for the specified
# parameter
# not \param [in] pContainer   Additional container for data associated
# with the specified parameter
# not
# not \retval ::NVAPI_INVALID_ARGUMENT Invalid input parameters.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI not initialized.
# not \retval ::NVAPI_NOT_SUPPORTED Interface not supported by the driver
# used, or only supported on selected GPUs
# not \retval ::NVAPI_INVALID_ARGUMENT Invalid input data.
# not \retval ::NVAPI_OK Feature enabled.
# not \retval ::NVAPI_ERROR Miscellaneous error occurred.
# not
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_SetScanoutCompositionParameter = hDll.GPU_SetScanoutCompositionParameter
NvAPI_GPU_SetScanoutCompositionParameter.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_SetScanoutCompositionParameter(NvU32 displayId, NV_GPU_SCANOUT_COMPOSITION_PARAMETER parameter,
#                                                         NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE parameterValue, float *pContainer);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetScanoutCompositionParameter
# not DESCRIPTION: This API queries current state of one of the various
# scanout composition parameters on the specified display.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  displayId   combined physical display and GPU
# identifier of the display to query the configuration.
# not \param [in]  parameter   scanout composition parameter to by queried.
# not \param [out] parameterData  scanout composition parameter data.
# not \param [out] pContainer   Additional container for returning data
# associated with the specified parameter
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not   specific meaning for this API, they are listed below.
# not
# not \retval ::NVAPI_INVALID_ARGUMENT Invalid input parameters.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI not initialized.
# not \retval ::NVAPI_NOT_SUPPORTED Interface not supported by the driver
# used, or only supported on selected GPUs.
# not \retval ::NVAPI_OK Feature enabled.
# not \retval ::NVAPI_ERROR Miscellaneous error occurred.
# not
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetScanoutCompositionParameter = hDll.GPU_GetScanoutCompositionParameter
NvAPI_GPU_GetScanoutCompositionParameter.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetScanoutCompositionParameter(__in NvU32 displayId, __in NV_GPU_SCANOUT_COMPOSITION_PARAMETER parameter,
#                                                         __out NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE *parameterData, __out float *pContainer);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetScanoutConfiguration
# not DESCRIPTION: This API queries the desktop and scanout portion of the
# specified display.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  displayId  combined physical display and GPU identifier
# of the display to query the configuration.
# not \param [in,out] desktopRect  desktop area of the display in desktop
# coordinates.
# not \param [in,out] scanoutRect  scanout area of the display relative to
# desktopRect.
# not
# not \retval ::NVAPI_INVALID_ARGUMENT Invalid input parameters.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI not initialized.
# not \retval ::NVAPI_NOT_SUPPORTED Interface not supported by the driver
# used, or only supported on selected GPUs.
# not \retval ::NVAPI_OK Feature enabled.
# not \retval ::NVAPI_ERROR Miscellaneous error occurred.
# not
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetScanoutConfiguration = hDll.GPU_GetScanoutConfiguration
NvAPI_GPU_GetScanoutConfiguration.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetScanoutConfiguration(NvU32 displayId, NvSBox* desktopRect, NvSBox* scanoutRect);


# not \ingroup gpu
# not Used in NvAPI_GPU_GetScanoutConfigurationEx().
_NV_SCANOUT_INFORMATION._fields_ = [
    # not < Structure version, needs to be initialized with
    # NV_SCANOUT_INFORMATION_VER.
    ('version', NvU32),
    # not < Operating system display device rect in desktop coordinates
    # displayId is scanning out from.
    ('sourceDesktopRect', NvSBox),
    # not < Area inside the sourceDesktopRect which is scanned out to the
    # display.
    ('sourceViewportRect', NvSBox),
    # not < Area inside the rect described by targetDisplayWidth/Height
    # sourceViewportRect is scanned out to.
    ('targetViewportRect', NvSBox),
    # not < Horizontal size of the active resolution scanned out to the
    # display.
    ('targetDisplayWidth', NvU32),
    # not < Vertical size of the active resolution scanned out to the
    # display.
    ('targetDisplayHeight', NvU32),
    # not < If targets are cloned views of the sourceDesktopRect the
    # cloned targets have an importance assigned
    # (0:primary,1 secondary,...).
    ('cloneImportance', NvU32),
    # not < Rotation performed between the sourceViewportRect and the
    # targetViewportRect.
    ('sourceToTargetRotation', NV_ROTATE),
]
NV_SCANOUT_INFORMATION_VER = (
    MAKE_NVAPI_VERSION(NV_SCANOUT_INFORMATION, 1)
)

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetScanoutConfigurationEx
# not DESCRIPTION: This API queries the desktop and scanout portion of the
# specified display.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not \since Release: 331
# not
# not \param [in]  displayId  combined physical display and GPU identifier
# of the display to query the configuration.
# not \param [in,out] pScanoutInformation desktop area to displayId
# mapping information.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetScanoutConfigurationEx = hDll.GPU_GetScanoutConfigurationEx
NvAPI_GPU_GetScanoutConfigurationEx.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetScanoutConfigurationEx(__in NvU32 displayId, __inout NV_SCANOUT_INFORMATION *pScanoutInformation);


# not \ingroup gpu
_NV_LOGICAL_GPU_DATA_V1._fields_ = [
    # not < [in] Structure version.
    ('version', NvU32),
    # not < [out] Returns OS-AdapterId. User must send memory buffer of
    # size atleast equal to the size of LUID structure before calling the
    # NVAPI.
    ('pOSAdapterId', POINTER(VOID)),
    # not < [out] Number of physical GPU handles associated with the
    # specified logical GPU handle.
    ('physicalGpuCount', NvU32),
    # not < [out] This array will be filled with physical GPU handles
    # associated with the given logical GPU handle.
    ('physicalGpuHandles', NvPhysicalGpuHandle * NVAPI_MAX_PHYSICAL_GPUS),
    # not < Reserved for future use. Should be set to ZERO.
    ('reserved', NvU32 * 8),
]

NV_LOGICAL_GPU_DATA = NV_LOGICAL_GPU_DATA_V1
NV_LOGICAL_GPU_DATA_VER1 = MAKE_NVAPI_VERSION(NV_LOGICAL_GPU_DATA_V1, 1)
NV_LOGICAL_GPU_DATA_VER = NV_LOGICAL_GPU_DATA_VER1

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetLogicalGpuInfo
# not This function is used to query Logical GPU information.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 421
# not
# not \param [in] hLogicalGpu  logical GPU Handle.
# not \param [inout] pLogicalGpuData  Pointer to NV_LOGICAL_GPU_DATA
# structure.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not   specific meaning for this API, they are listed below.
# not
# not \ingroup gpu
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetLogicalGpuInfo = hDll.GPU_GetLogicalGpuInfo
NvAPI_GPU_GetLogicalGpuInfo.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GPU_GetLogicalGpuInfo(__in NvLogicalGpuHandle hLogicalGpu, __inout NV_LOGICAL_GPU_DATA *pLogicalGpuData);


# not Used in NvAPI_GPU_GetPerfDecreaseInfo.
# not Bit masks for knowing the exact reason for performance decrease
class _NVAPI_GPU_PERF_DECREASE(ENUM):
    NV_GPU_PERF_DECREASE_NONE = 0
    NV_GPU_PERF_DECREASE_REASON_THERMAL_PROTECTION = 0x00000001
    NV_GPU_PERF_DECREASE_REASON_POWER_CONTROL = 0x00000002
    NV_GPU_PERF_DECREASE_REASON_AC_BATT = 0x00000004
    NV_GPU_PERF_DECREASE_REASON_API_TRIGGERED = 0x00000008
    NV_GPU_PERF_DECREASE_REASON_INSUFFICIENT_POWER = 0x00000010
    NV_GPU_PERF_DECREASE_REASON_UNKNOWN = 0x80000000


NVAPI_GPU_PERF_DECREASE = _NVAPI_GPU_PERF_DECREASE

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetPerfDecreaseInfo
# not DESCRIPTION: This function retrieves - in NvU32 variable - reasons
# for the current performance decrease.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not \param [in] hPhysicalGPU (IN) - GPU for which performance decrease
# is to be evaluated.
# not \param [out] pPerfDecrInfo (OUT) - Pointer to a NvU32 variable
# containing performance decrease info
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not
# not \ingroup gpuPerf
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetPerfDecreaseInfo = hDll.GPU_GetPerfDecreaseInfo
NvAPI_GPU_GetPerfDecreaseInfo.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GPU_GetPerfDecreaseInfo(__in NvPhysicalGpuHandle hPhysicalGpu, __inout NvU32 *pPerfDecrInfo);


# not \ingroup gpupstate
# not Used in NvAPI_GPU_GetPstatesInfoEx()
class pstates(ctypes.Structure):
    pass


class clocks(ctypes.Structure):
    pass


clocks._fields_ = [
    # not < ID of the clock domain
    ('domainId', NV_GPU_PUBLIC_CLOCK_ID),
    # not < Reserved. Must be set to 0
    ('flags', NvU32),
    # not < Clock frequency in kHz
    ('freq', NvU32),
]
pstates.clocks = clocks

pstates._fields_ = [
    # not < ID of the p-state.
    ('pstateId', NV_GPU_PERF_PSTATE_ID),
    # - bit 0 indicates if the PCIE limit is GEN1 or GEN2
    # - bit 1 indicates if the Pstate is overclocked or not
    # - bit 2 indicates if the Pstate is overclockable or not
    # - all other bits must be set to 0
    ('flags', NvU32),
    # not < - all other bits must be set to 0
    ('clocks', pstates.clocks * NVAPI_MAX_GPU_PERF_CLOCKS),
]
NV_GPU_PERF_PSTATES_INFO_V1.pstates = pstates

NV_GPU_PERF_PSTATES_INFO_V1._fields_ = [
    ('version', NvU32),
    # - bit 0 indicates if perfmon is enabled or not
    # - bit 1 indicates if dynamic Pstate is capable or not
    # - bit 2 indicates if dynamic Pstate is enable or not
    # - all other bits must be set to 0
    ('flags', NvU32),
    # not < The number of available p-states
    ('numPstates', NvU32),
    # not < The number of clock domains supported by each P-State
    ('numClocks', NvU32),
    ('pstates', NV_GPU_PERF_PSTATES_INFO_V1.pstates * NVAPI_MAX_GPU_PERF_PSTATES),
]


# not \ingroup gpupstate
class pstates(ctypes.Structure):
    pass


class clocks(ctypes.Structure):
    pass


clocks._fields_ = [
    ('domainId', NV_GPU_PUBLIC_CLOCK_ID),
    # not < bit 0 indicates if this clock is overclockable
    ('flags', NvU32),
    # not < all other bits must be set to 0
    ('freq', NvU32),
]
pstates.clocks = clocks


class voltages(ctypes.Structure):
    pass


voltages._fields_ = [
    # not < ID of the voltage domain, containing flags and mvolt info
    ('domainId', NV_GPU_PERF_VOLTAGE_INFO_DOMAIN_ID),
    # not < Reserved for future use. Must be set to 0
    ('flags', NvU32),
    # not < Voltage in mV
    ('mvolt', NvU32),
]
pstates.voltages = voltages

pstates._fields_ = [
    # not < ID of the p-state.
    ('pstateId', NV_GPU_PERF_PSTATE_ID),
    # not < - bit 0 indicates if the PCIE limit is GEN1 or GEN2
    ('flags', NvU32),
    # not < - all other bits must be set to 0
    ('clocks', pstates.clocks * NVAPI_MAX_GPU_PERF_CLOCKS),
    ('voltages', pstates.voltages * NVAPI_MAX_GPU_PERF_VOLTAGES),
]
NV_GPU_PERF_PSTATES_INFO_V2.pstates = pstates

NV_GPU_PERF_PSTATES_INFO_V2._fields_ = [
    ('version', NvU32),
    # not < - bit 0 indicates if perfmon is enabled or not
    ('flags', NvU32),
    # not < The number of available p-states
    ('numPstates', NvU32),
    # not < The number of clock domains supported by each P-State
    ('numClocks', NvU32),
    ('numVoltages', NvU32),
    ('pstates', NV_GPU_PERF_PSTATES_INFO_V2.pstates * NVAPI_MAX_GPU_PERF_PSTATES)
    # not  <  Valid index range is 0 to numVoltages-1),
]

# not \ingroup gpupstate
NV_GPU_PERF_PSTATES_INFO = NV_GPU_PERF_PSTATES_INFO_V2

# not \ingroup gpupstate
# not @{
# not Macro for constructing the version field of
# NV_GPU_PERF_PSTATES_INFO_V1
NV_GPU_PERF_PSTATES_INFO_VER1 = (
    MAKE_NVAPI_VERSION(NV_GPU_PERF_PSTATES_INFO_V1, 1)
)
# not Macro for constructing the version field of
# NV_GPU_PERF_PSTATES_INFO_V2
NV_GPU_PERF_PSTATES_INFO_VER2 = (
    MAKE_NVAPI_VERSION(NV_GPU_PERF_PSTATES_INFO_V2, 2)
)
# not Macro for constructing the version field of
# NV_GPU_PERF_PSTATES_INFO_V2
NV_GPU_PERF_PSTATES_INFO_VER3 = (
    MAKE_NVAPI_VERSION(NV_GPU_PERF_PSTATES_INFO_V2, 3)
)
# not Macro for constructing the version field of NV_GPU_PERF_PSTATES_INFO
NV_GPU_PERF_PSTATES_INFO_VER = NV_GPU_PERF_PSTATES_INFO_VER3
# not @}
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetPstatesInfoEx
# not DESCRIPTION:  This API retrieves all performance states (P-States)
# information. This is the same as
# not    NvAPI_GPU_GetPstatesInfo(), but supports an input flag for
# various options.
# not
# not    P-States are GPU active/executing performance capability and
# power consumption states.
# not
# not    P-States ranges from P0 to P15, with P0 being the highest
# performance/power state, and
# not    P15 being the lowest performance/power state. Each P-State, if
# available, maps to a
# not    performance level. Not all P-States are available on a given
# system. The definitions
# not    of each P-State are currently as follows: \n
# not    - P0/P1 - Maximum 3D performance
# not    - P2/P3 - Balanced 3D performance-power
# not    - P8 - Basic HD video playback
# not    - P10 - DVD playback
# not    - P12 - Minimum idle power consumption
# not
# not \deprecated Do not use this function - it is deprecated in release
# 304. Instead, use NvAPI_GPU_GetPstates20.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  hPhysicalGPU  GPU selection.
# not \param [out] pPerfPstatesInfo P-States information retrieved, as
# detailed below: \n
# not    - flags is reserved for future use.
# not    - numPstates is the number of available P-States
# not    - numClocks is the number of clock domains supported by each
# P-State
# not    - pstates has valid index range from 0 to numPstates - 1
# not    - pstates[i].pstateId is the ID of the P-State,
# not     containing the following info:
# not    - pstates[i].flags containing the following info:
# not     - bit 0 indicates if the PCIE limit is GEN1 or GEN2
# not     - bit 1 indicates if the Pstate is overclocked or not
# not     - bit 2 indicates if the Pstate is overclockable or not
# not    - pstates[i].clocks has valid index range from 0 to numClocks -1
# not    - pstates[i].clocks[j].domainId is the public ID of the clock
# domain,
# not     containing the following info:
# not     - pstates[i].clocks[j].flags containing the following info:
# not     bit 0 indicates if the clock domain is overclockable or not
# not     - pstates[i].clocks[j].freq is the clock frequency in kHz
# not    - pstates[i].voltages has a valid index range from 0 to
# numVoltages - 1
# not    - pstates[i].voltages[j].domainId is the ID of the voltage domain,
# not     containing the following info:
# not     - pstates[i].voltages[j].flags is reserved for future use.
# not     - pstates[i].voltages[j].mvolt is the voltage in mV
# not    inputFlags(IN) - This can be used to select various options:
# not    - if bit 0 is set, pPerfPstatesInfo would contain the default
# settings
# not     instead of the current, possibily overclocked settings.
# not    - if bit 1 is set, pPerfPstatesInfo would contain the maximum
# clock
# not     frequencies instead of the nominal frequencies.
# not    - if bit 2 is set, pPerfPstatesInfo would contain the minimum
# clock
# not     frequencies instead of the nominal frequencies.
# not    - all other bits must be set to 0.
# not
# not \retval ::NVAPI_OK     Completed request
# not \retval ::NVAPI_ERROR     Miscellaneous error occurred
# not \retval ::NVAPI_HANDLE_INVALIDATED  Handle passed has been
# invalidated (see user guide)
# not \retval ::NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE Handle passed is not a
# physical GPU handle
# not \retval ::NVAPI_INCOMPATIBLE_STRUCT_VERSION The version of the
# NV_GPU_PERF_PSTATES struct is not supported
# not
# not \ingroup gpupstate
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetPstatesInfoEx = hDll.GPU_GetPstatesInfoEx
NvAPI_GPU_GetPstatesInfoEx.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetPstatesInfoEx(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_PERF_PSTATES_INFO *pPerfPstatesInfo, NvU32 inputFlags);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetPstates20
# not DESCRIPTION: This API retrieves all performance states (P-States)
# 2.0 information.
# not
# not   P-States are GPU active/executing performance capability states.
# not   They range from P0 to P15, with P0 being the highest performance
# state,
# not   and P15 being the lowest performance state. Each P-State, if
# available,
# not   maps to a performance level. Not all P-States are available on a
# given system.
# not   The definition of each P-States are currently as follow:
# not   - P0/P1 - Maximum 3D performance
# not   - P2/P3 - Balanced 3D performance-power
# not   - P8 - Basic HD video playback
# not   - P10 - DVD playback
# not   - P12 - Minimum idle power consumption
# not
# not TCC_SUPPORTED
# not
# not \since Release: 295
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hPhysicalGPU GPU selection
# not \param [out] pPstatesInfo P-States information retrieved, as
# documented in declaration above
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   If there are return error codes with specific meaning for this API,
# not   they are listed below.
# not
# not \ingroup gpupstate
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetPstates20 = hDll.GPU_GetPstates20
NvAPI_GPU_GetPstates20.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetPstates20(__in NvPhysicalGpuHandle hPhysicalGpu, __inout NV_GPU_PERF_PSTATES20_INFO *pPstatesInfo);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetCurrentPstate
# not DESCRIPTION:  This function retrieves the current performance state
# (P-State).
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 165
# not
# not TCC_SUPPORTED
# not
# not \param [in] hPhysicalGPU  GPU selection
# not \param [out]  pCurrentPstate The ID of the current P-State of the
# GPU - see \ref NV_GPU_PERF_PSTATES.
# not
# not \retval NVAPI_OK      Completed request
# not \retval NVAPI_ERROR     Miscellaneous error occurred.
# not \retval NVAPI_HANDLE_INVALIDATED   Handle passed has been
# invalidated (see user guide).
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE Handle passed is not a
# physical GPU handle.
# not \retval NVAPI_NOT_SUPPORTED   P-States is not supported on this
# setup.
# not
# not \ingroup gpupstate
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetCurrentPstate = hDll.GPU_GetCurrentPstate
NvAPI_GPU_GetCurrentPstate.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetCurrentPstate(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_PERF_PSTATE_ID *pCurrentPstate);


# not \ingroup gpupstate
NVAPI_MAX_GPU_UTILIZATIONS = 8


# not \ingroup gpupstate
# not Used in NvAPI_GPU_GetDynamicPstatesInfoEx().
class utilization(ctypes.Structure):
    pass


utilization._fields_ = [
    # not < Set if this utilization domain is present on this GPU
    ('bIsPresent', NvU32, 1),
    # not < Percentage of time where the domain is considered busy in the
    # last 1 second interval
    ('percentage', NvU32),
]
NV_GPU_DYNAMIC_PSTATES_INFO_EX.utilization = utilization

NV_GPU_DYNAMIC_PSTATES_INFO_EX._fields_ = [
    # not < Structure version
    ('version', NvU32),
    # not < bit 0 indicates if the dynamic Pstate is enabled or not
    ('flags', NvU32),
    ('utilization', NV_GPU_DYNAMIC_PSTATES_INFO_EX.utilization * NVAPI_MAX_GPU_UTILIZATIONS),
]

# not \ingroup gpupstate
# not Macro for constructing the version field of
# NV_GPU_DYNAMIC_PSTATES_INFO_EX
NV_GPU_DYNAMIC_PSTATES_INFO_EX_VER = (
    MAKE_NVAPI_VERSION(NV_GPU_DYNAMIC_PSTATES_INFO_EX, 1)
)

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetDynamicPstatesInfoEx
# not DESCRIPTION: This API retrieves the NV_GPU_DYNAMIC_PSTATES_INFO_EX
# structure for the specified physical GPU.
# not    Each domain's info is indexed in the array. For example:
# not    -
# pDynamicPstatesInfo.utilization[NVAPI_GPU_UTILIZATION_DOMAIN_GPU] holds
# the info for the GPU domain. \p
# not    There are currently 4 domains for which GPU utilization and
# dynamic P-State thresholds can be retrieved:
# not    graphic engine (GPU), frame buffer (FB), video engine (VID), and
# bus interface (BUS).
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not
# not TCC_SUPPORTED
# not \since Release: 185
# not
# not \retval ::NVAPI_OK
# not \retval ::NVAPI_ERROR
# not \retval ::NVAPI_INVALID_ARGUMENT pDynamicPstatesInfo is NULL
# not \retval ::NVAPI_HANDLE_INVALIDATED
# not \retval ::NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE
# not \retval ::NVAPI_INCOMPATIBLE_STRUCT_VERSION The version of the INFO
# struct is not supported
# not
# not \ingroup gpupstate
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetDynamicPstatesInfoEx = hDll.GPU_GetDynamicPstatesInfoEx
NvAPI_GPU_GetDynamicPstatesInfoEx.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetDynamicPstatesInfoEx(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_DYNAMIC_PSTATES_INFO_EX *pDynamicPstatesInfoEx);


# ///////////////////////////////////////////////////////////////////////////
# Thermal API
# Provides ability to get temperature levels from the various thermal
# sensors associated with the GPU
# not \ingroup gputhermal
NVAPI_MAX_THERMAL_SENSORS_PER_GPU = 3


# not \ingroup gputhermal
# not Used in NV_GPU_THERMAL_SETTINGS
class NV_THERMAL_TARGET(ENUM):
    NVAPI_THERMAL_TARGET_NONE = 0
    NVAPI_THERMAL_TARGET_GPU = 1
    NVAPI_THERMAL_TARGET_MEMORY = 2
    NVAPI_THERMAL_TARGET_POWER_SUPPLY = 4
    NVAPI_THERMAL_TARGET_BOARD = 8

    # not < Visual Computing Device Board temperature requires
    # NvVisualComputingDeviceHandle
    NVAPI_THERMAL_TARGET_VCD_BOARD = 9

    # not < Visual Computing Device Inlet temperature requires
    # NvVisualComputingDeviceHandle
    NVAPI_THERMAL_TARGET_VCD_INLET = 10

    # not < Visual Computing Device Outlet temperature requires
    # NvVisualComputingDeviceHandle
    NVAPI_THERMAL_TARGET_VCD_OUTLET = 11
    NVAPI_THERMAL_TARGET_ALL = 15
    NVAPI_THERMAL_TARGET_UNKNOWN = - 1


NVAPI_THERMAL_TARGET_NONE = NV_THERMAL_TARGET.NVAPI_THERMAL_TARGET_NONE
NVAPI_THERMAL_TARGET_GPU = NV_THERMAL_TARGET.NVAPI_THERMAL_TARGET_GPU
NVAPI_THERMAL_TARGET_MEMORY = NV_THERMAL_TARGET.NVAPI_THERMAL_TARGET_MEMORY
NVAPI_THERMAL_TARGET_POWER_SUPPLY = NV_THERMAL_TARGET.NVAPI_THERMAL_TARGET_POWER_SUPPLY
NVAPI_THERMAL_TARGET_BOARD = NV_THERMAL_TARGET.NVAPI_THERMAL_TARGET_BOARD
NVAPI_THERMAL_TARGET_VCD_BOARD = NV_THERMAL_TARGET.NVAPI_THERMAL_TARGET_VCD_BOARD
NVAPI_THERMAL_TARGET_VCD_INLET = NV_THERMAL_TARGET.NVAPI_THERMAL_TARGET_VCD_INLET
NVAPI_THERMAL_TARGET_VCD_OUTLET = NV_THERMAL_TARGET.NVAPI_THERMAL_TARGET_VCD_OUTLET
NVAPI_THERMAL_TARGET_ALL = NV_THERMAL_TARGET.NVAPI_THERMAL_TARGET_ALL
NVAPI_THERMAL_TARGET_UNKNOWN = NV_THERMAL_TARGET.NVAPI_THERMAL_TARGET_UNKNOWN


# not \ingroup gputhermal
# not Used in NV_GPU_THERMAL_SETTINGS
class NV_THERMAL_CONTROLLER(ENUM):
    NVAPI_THERMAL_CONTROLLER_NONE = 0
    NVAPI_THERMAL_CONTROLLER_GPU_INTERNAL = 1
    NVAPI_THERMAL_CONTROLLER_ADM1032 = 2
    NVAPI_THERMAL_CONTROLLER_MAX6649 = 3
    NVAPI_THERMAL_CONTROLLER_MAX1617 = 4
    NVAPI_THERMAL_CONTROLLER_LM99 = 5
    NVAPI_THERMAL_CONTROLLER_LM89 = 6
    NVAPI_THERMAL_CONTROLLER_LM64 = 7
    NVAPI_THERMAL_CONTROLLER_ADT7473 = 8
    NVAPI_THERMAL_CONTROLLER_SBMAX6649 = 9
    NVAPI_THERMAL_CONTROLLER_VBIOSEVT = 10
    NVAPI_THERMAL_CONTROLLER_OS = 11
    NVAPI_THERMAL_CONTROLLER_UNKNOWN = - 1


NVAPI_THERMAL_CONTROLLER_NONE = NV_THERMAL_CONTROLLER.NVAPI_THERMAL_CONTROLLER_NONE
NVAPI_THERMAL_CONTROLLER_GPU_INTERNAL = NV_THERMAL_CONTROLLER.NVAPI_THERMAL_CONTROLLER_GPU_INTERNAL
NVAPI_THERMAL_CONTROLLER_ADM1032 = NV_THERMAL_CONTROLLER.NVAPI_THERMAL_CONTROLLER_ADM1032
NVAPI_THERMAL_CONTROLLER_MAX6649 = NV_THERMAL_CONTROLLER.NVAPI_THERMAL_CONTROLLER_MAX6649
NVAPI_THERMAL_CONTROLLER_MAX1617 = NV_THERMAL_CONTROLLER.NVAPI_THERMAL_CONTROLLER_MAX1617
NVAPI_THERMAL_CONTROLLER_LM99 = NV_THERMAL_CONTROLLER.NVAPI_THERMAL_CONTROLLER_LM99
NVAPI_THERMAL_CONTROLLER_LM89 = NV_THERMAL_CONTROLLER.NVAPI_THERMAL_CONTROLLER_LM89
NVAPI_THERMAL_CONTROLLER_LM64 = NV_THERMAL_CONTROLLER.NVAPI_THERMAL_CONTROLLER_LM64
NVAPI_THERMAL_CONTROLLER_ADT7473 = NV_THERMAL_CONTROLLER.NVAPI_THERMAL_CONTROLLER_ADT7473
NVAPI_THERMAL_CONTROLLER_SBMAX6649 = NV_THERMAL_CONTROLLER.NVAPI_THERMAL_CONTROLLER_SBMAX6649
NVAPI_THERMAL_CONTROLLER_VBIOSEVT = NV_THERMAL_CONTROLLER.NVAPI_THERMAL_CONTROLLER_VBIOSEVT
NVAPI_THERMAL_CONTROLLER_OS = NV_THERMAL_CONTROLLER.NVAPI_THERMAL_CONTROLLER_OS
NVAPI_THERMAL_CONTROLLER_UNKNOWN = NV_THERMAL_CONTROLLER.NVAPI_THERMAL_CONTROLLER_UNKNOWN


# not \ingroup gputhermal
# not Used in NvAPI_GPU_GetThermalSettings()
class sensor(ctypes.Structure):
    pass


sensor._fields_ = [
    # not < internal, ADM1032, MAX6649...
    ('controller', NV_THERMAL_CONTROLLER),
    # not < The min default temperature value of the thermal sensor in
    # degree Celsius
    ('defaultMinTemp', NvU32),
    # not < The max default temperature value of the thermal sensor in
    # degree Celsius
    ('defaultMaxTemp', NvU32),
    # not < The current temperature value of the thermal sensor in degree
    # Celsius
    ('currentTemp', NvU32),
    # not < Thermal sensor targeted @ GPU, memory, chipset, powersupply,
    # Visual Computing Device, etc.
    ('target', NV_THERMAL_TARGET),
]
NV_GPU_THERMAL_SETTINGS_V1.sensor = sensor

NV_GPU_THERMAL_SETTINGS_V1._fields_ = [
    # not < structure version
    ('version', NvU32),
    # not < number of associated thermal sensors
    ('count', NvU32),
    ('sensor', NV_GPU_THERMAL_SETTINGS_V1.sensor * NVAPI_MAX_THERMAL_SENSORS_PER_GPU),
]


# not \ingroup gputhermal
class sensor(ctypes.Structure):
    pass


sensor._fields_ = [
    # not < internal, ADM1032, MAX6649...
    ('controller', NV_THERMAL_CONTROLLER),
    # not < Minimum default temperature value of the thermal sensor in
    # degree Celsius
    ('defaultMinTemp', NvS32),
    # not < Maximum default temperature value of the thermal sensor in
    # degree Celsius
    ('defaultMaxTemp', NvS32),
    # not < Current temperature value of the thermal sensor in degree
    # Celsius
    ('currentTemp', NvS32),
    # not < Thermal sensor targeted - GPU, memory, chipset, powersupply,
    # Visual Computing Device, etc
    ('target', NV_THERMAL_TARGET),
]
NV_GPU_THERMAL_SETTINGS_V2.sensor = sensor

NV_GPU_THERMAL_SETTINGS_V2._fields_ = [
    # not < structure version
    ('version', NvU32),
    # not < number of associated thermal sensors
    ('count', NvU32),
    ('sensor', NV_GPU_THERMAL_SETTINGS_V2.sensor * NVAPI_MAX_THERMAL_SENSORS_PER_GPU),
]

NV_GPU_THERMAL_SETTINGS = NV_GPU_THERMAL_SETTINGS_V2
# not \ingroup gputhermal
# not @{
# not Macro for constructing the version field of
# NV_GPU_THERMAL_SETTINGS_V1
NV_GPU_THERMAL_SETTINGS_VER_1 = (
    MAKE_NVAPI_VERSION(NV_GPU_THERMAL_SETTINGS_V1, 1)
)
# not Macro for constructing the version field of
# NV_GPU_THERMAL_SETTINGS_V2
NV_GPU_THERMAL_SETTINGS_VER_2 = (
    MAKE_NVAPI_VERSION(NV_GPU_THERMAL_SETTINGS_V2, 2)
)
# not Macro for constructing the version field of NV_GPU_THERMAL_SETTINGS
NV_GPU_THERMAL_SETTINGS_VER = NV_GPU_THERMAL_SETTINGS_VER_2
# not @}
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetThermalSettings
# not This function retrieves the thermal information of all thermal
# sensors or specific thermal sensor associated with the selected GPU.
# not Thermal sensors are indexed 0 to NVAPI_MAX_THERMAL_SENSORS_PER_GPU-1.
# not
# not - To retrieve specific thermal sensor info, set the sensorIndex to
# the required thermal sensor index.
# not - To retrieve info for all sensors, set sensorIndex to
# NVAPI_THERMAL_TARGET_ALL.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 85
# not
# not \param [in] hPhysicalGPU GPU selection.
# not \param [in] sensorIndex  Explicit thermal sensor index selection.
# not \param [out] pThermalSettings Array of thermal settings.
# not
# not \retval NVAPI_OK     Completed request
# not \retval NVAPI_ERROR    Miscellaneous error occurred.
# not \retval NVAPI_INVALID_ARGUMENT   pThermalInfo is NULL.
# not \retval NVAPI_HANDLE_INVALIDATED   Handle passed has been
# invalidated (see user guide).
# not \retval NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE Handle passed is not a
# physical GPU handle.
# not \retval NVAPI_INCOMPATIBLE_STRUCT_VERSION The version of the INFO
# struct is not supported.
# not \ingroup gputhermal
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetThermalSettings = hDll.GPU_GetThermalSettings
NvAPI_GPU_GetThermalSettings.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GPU_GetThermalSettings(NvPhysicalGpuHandle hPhysicalGpu, NvU32 sensorIndex, NV_GPU_THERMAL_SETTINGS *pThermalSettings);


# not \ingroup gpuclock
# not Used in NvAPI_GPU_GetAllClockFrequencies()
class domain(ctypes.Structure):
    pass


domain._fields_ = [
    # not < Set if this domain is present on this GPU
    ('bIsPresent', NvU32, 1),
    # not < These bits are reserved for future use.
    ('reserved', NvU32, 31),
    # not < Clock frequency (kHz)
    ('frequency', NvU32),
]
NV_GPU_CLOCK_FREQUENCIES_V1.domain = domain

NV_GPU_CLOCK_FREQUENCIES_V1._fields_ = [
    # not < Structure version
    ('version', NvU32),
    # not < These bits are reserved for future use.
    ('reserved', NvU32),
    ('domain', NV_GPU_CLOCK_FREQUENCIES_V1.domain * NVAPI_MAX_GPU_PUBLIC_CLOCKS),
]

NV_GPU_MAX_CLOCK_FREQUENCIES = 3


# END IF


# not \ingroup gpuclock
# not Used in NvAPI_GPU_GetAllClockFrequencies()
class NV_GPU_CLOCK_FREQUENCIES_CLOCK_TYPE(ENUM):
    NV_GPU_CLOCK_FREQUENCIES_CURRENT_FREQ = 0
    NV_GPU_CLOCK_FREQUENCIES_BASE_CLOCK = 1
    NV_GPU_CLOCK_FREQUENCIES_BOOST_CLOCK = 2
    NV_GPU_CLOCK_FREQUENCIES_CLOCK_TYPE_NUM = NV_GPU_MAX_CLOCK_FREQUENCIES


NV_GPU_CLOCK_FREQUENCIES_CURRENT_FREQ = NV_GPU_CLOCK_FREQUENCIES_CLOCK_TYPE.NV_GPU_CLOCK_FREQUENCIES_CURRENT_FREQ
NV_GPU_CLOCK_FREQUENCIES_BASE_CLOCK = NV_GPU_CLOCK_FREQUENCIES_CLOCK_TYPE.NV_GPU_CLOCK_FREQUENCIES_BASE_CLOCK
NV_GPU_CLOCK_FREQUENCIES_BOOST_CLOCK = NV_GPU_CLOCK_FREQUENCIES_CLOCK_TYPE.NV_GPU_CLOCK_FREQUENCIES_BOOST_CLOCK
NV_GPU_CLOCK_FREQUENCIES_CLOCK_TYPE_NUM = NV_GPU_CLOCK_FREQUENCIES_CLOCK_TYPE.NV_GPU_CLOCK_FREQUENCIES_CLOCK_TYPE_NUM


# not \ingroup gpuclock
# not Used in NvAPI_GPU_GetAllClockFrequencies()
class domain(ctypes.Structure):
    pass


domain._fields_ = [
    # not < Set if this domain is present on this GPU
    ('bIsPresent', NvU32, 1),
    # not < These bits are reserved for future use.
    ('reserved', NvU32, 31),
    # not < Clock frequency (kHz)
    ('frequency', NvU32),
]
NV_GPU_CLOCK_FREQUENCIES_V2.domain = domain

NV_GPU_CLOCK_FREQUENCIES_V2._fields_ = [
    # not < Structure version
    ('version', NvU32),
    # not < One of NV_GPU_CLOCK_FREQUENCIES_CLOCK_TYPE. Used to specify
    # the type of clock to be returned.
    ('ClockType', NvU32, 4),
    # not < These bits are reserved for future use. Must be set to 0.
    ('reserved', NvU32, 20),
    # not < These bits are reserved.
    ('reserved1', NvU32, 8),
    ('domain', NV_GPU_CLOCK_FREQUENCIES_V2.domain * NVAPI_MAX_GPU_PUBLIC_CLOCKS),
]

# not \ingroup gpuclock
# not Used in NvAPI_GPU_GetAllClockFrequencies()
NV_GPU_CLOCK_FREQUENCIES = NV_GPU_CLOCK_FREQUENCIES_V2

# not \addtogroup gpuclock
# not @{
NV_GPU_CLOCK_FREQUENCIES_VER_1 = (
    MAKE_NVAPI_VERSION(NV_GPU_CLOCK_FREQUENCIES_V1, 1)
)
NV_GPU_CLOCK_FREQUENCIES_VER_2 = (
    MAKE_NVAPI_VERSION(NV_GPU_CLOCK_FREQUENCIES_V2, 2)
)
NV_GPU_CLOCK_FREQUENCIES_VER_3 = (
    MAKE_NVAPI_VERSION(NV_GPU_CLOCK_FREQUENCIES_V2, 3)
)
NV_GPU_CLOCK_FREQUENCIES_VER = NV_GPU_CLOCK_FREQUENCIES_VER_3
# not @}
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetAllClockFrequencies
# not This function retrieves the NV_GPU_CLOCK_FREQUENCIES structure for
# the specified physical GPU.
# not
# not For each clock domain:
# not  - bIsPresent is set for each domain that is present on the GPU
# not  - frequency is the domain's clock freq in kHz
# not
# not Each domain's info is indexed in the array. For example:
# not clkFreqs.domain[NVAPI_GPU_PUBLIC_CLOCK_MEMORY] holds the info for
# the MEMORY domain.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 295
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   If there are return error codes with specific meaning for this API,
# not   they are listed below.
# not \retval NVAPI_INVALID_ARGUMENT  pClkFreqs is NULL.
# not \ingroup gpuclock
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_GetAllClockFrequencies = hDll.GPU_GetAllClockFrequencies
NvAPI_GPU_GetAllClockFrequencies.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GPU_GetAllClockFrequencies(__in NvPhysicalGpuHandle hPhysicalGPU, __inout NV_GPU_CLOCK_FREQUENCIES *pClkFreqs);


# ///////////////////////////////////////////////////////////////////////
# not
# not FUNCTION NAME: NvAPI_GPU_QueryIlluminationSupport
# not
# not \fn
# NvAPI_GPU_QueryIlluminationSupport(__inout NV_GPU_QUERY_ILLUMINATION_SUPPORT_PARM *pIlluminationSupportInfo)
#
# not DESCRIPTION: This function reports if the specified illumination
# attribute is supported.
# not
# not \note Only a single GPU can manage an given attribute on a given HW
# element,
# not  regardless of how many are attatched. I.E. only one GPU will be
# used to control
# not  the brightness of the LED on an SLI bridge, regardless of how many
# are physicaly attached.
# not  You should enumerate thru the GPUs with this call to determine
# which GPU is managing the attribute.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 300.05
# not
# not \param [in] hPhysicalGpu  Physical GPU handle
# not \param  Attribute   An enumeration value specifying the Illumination
# attribute to be querried
# not \param [out] pSupported  A BOOLEAN indicating if the attribute is
# supported.
# not
# not \return See \ref nvapistatus for the list of possible return values.
# //////////////////////////////////////////////////////////////////////
# not \ingroup gpu
class _NV_GPU_ILLUMINATION_ATTRIB(ENUM):
    NV_GPU_IA_LOGO_BRIGHTNESS = 0
    NV_GPU_IA_SLI_BRIGHTNESS = 1


NV_GPU_ILLUMINATION_ATTRIB = _NV_GPU_ILLUMINATION_ATTRIB

# not \ingroup gpu
_NV_GPU_QUERY_ILLUMINATION_SUPPORT_PARM_V1._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < The handle of the GPU that you are checking for the specified
    # attribute.
    ('hPhysicalGpu', NvPhysicalGpuHandle),
    # not < An enumeration value specifying the Illumination attribute to
    # be querried.
    ('Attribute', NV_GPU_ILLUMINATION_ATTRIB),
    # not < A BOOLEAN indicating if the attribute is supported.
    ('bSupported', NvU32),
]

# not \ingroup gpu
NV_GPU_QUERY_ILLUMINATION_SUPPORT_PARM = NV_GPU_QUERY_ILLUMINATION_SUPPORT_PARM_V1
# not \ingroup gpu
NV_GPU_QUERY_ILLUMINATION_SUPPORT_PARM_VER_1 = (
    MAKE_NVAPI_VERSION(NV_GPU_QUERY_ILLUMINATION_SUPPORT_PARM_V1, 1)
)

# not \ingroup gpu
NV_GPU_QUERY_ILLUMINATION_SUPPORT_PARM_VER = (
    NV_GPU_QUERY_ILLUMINATION_SUPPORT_PARM_VER_1
)

# not \ingroup gpu
NvAPI_GPU_QueryIlluminationSupport = hDll.GPU_QueryIlluminationSupport
NvAPI_GPU_QueryIlluminationSupport.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_QueryIlluminationSupport(__inout NV_GPU_QUERY_ILLUMINATION_SUPPORT_PARM *pIlluminationSupportInfo);


# ///////////////////////////////////////////////////////////////////////
# not
# not FUNCTION NAME: NvAPI_GPU_GetIllumination
# not
# not \fn
# NvAPI_GPU_GetIllumination(NV_GPU_GET_ILLUMINATION_PARM *pIlluminationInfo)
#
# not DESCRIPTION: This function reports value of the specified
# illumination attribute.
# not
# not \note Only a single GPU can manage an given attribute on a given HW
# element,
# not  regardless of how many are attatched. I.E. only one GPU will be
# used to control
# not  the brightness of the LED on an SLI bridge, regardless of how many
# are physicaly attached.
# not  You should enumerate thru the GPUs with the \ref
# NvAPI_GPU_QueryIlluminationSupport call to
# not  determine which GPU is managing the attribute.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 300.05
# not
# not \param [in] hPhysicalGpu  Physical GPU handle
# not \param  Attribute   An enumeration value specifying the Illumination
# attribute to be querried
# not \param [out] Value   A DWORD containing the current value for the
# specified attribute.
# not       This is specified as a percentage of the full range of the
# attribute
# not       (0-100; 0 = off, 100 = full brightness)
# not
# not \return See \ref nvapistatus for the list of possible return values.
# Return values of special interest are:
# not   NVAPI_INVALID_ARGUMENT The specified attibute is not known to the
# driver.
# not   NVAPI_NOT_SUPPORTED: The specified attribute is not supported on
# the specified GPU
# //////////////////////////////////////////////////////////////////////
# not \ingroup gpu
_NV_GPU_GET_ILLUMINATION_PARM_V1._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < The handle of the GPU that you are checking for the specified
    # attribute.
    ('hPhysicalGpu', NvPhysicalGpuHandle),
    # not < An enumeration value specifying the Illumination attribute to
    # be querried.
    ('Attribute', NV_GPU_ILLUMINATION_ATTRIB),
    # not < A DWORD that will contain the current value of the specified
    # attribute.
    ('Value', NvU32),
]

# not \ingroup gpu
NV_GPU_GET_ILLUMINATION_PARM = NV_GPU_GET_ILLUMINATION_PARM_V1
# not \ingroup gpu
NV_GPU_GET_ILLUMINATION_PARM_VER_1 = (
    MAKE_NVAPI_VERSION(NV_GPU_GET_ILLUMINATION_PARM_V1, 1)
)

# not \ingroup gpu
NV_GPU_GET_ILLUMINATION_PARM_VER = NV_GPU_GET_ILLUMINATION_PARM_VER_1

# not \ingroup gpu
NvAPI_GPU_GetIllumination = hDll.GPU_GetIllumination
NvAPI_GPU_GetIllumination.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetIllumination(NV_GPU_GET_ILLUMINATION_PARM *pIlluminationInfo);


# ///////////////////////////////////////////////////////////////////////
# not
# not FUNCTION NAME: NvAPI_GPU_SetIllumination
# not
# not \fn
# NvAPI_GPU_SetIllumination(NV_GPU_SET_ILLUMINATION_PARM *pIlluminationInfo)
#
# not DESCRIPTION: This function sets the value of the specified
# illumination attribute.
# not
# not \note Only a single GPU can manage an given attribute on a given HW
# element,
# not  regardless of how many are attatched. I.E. only one GPU will be
# used to control
# not  the brightness of the LED on an SLI bridge, regardless of how many
# are physicaly attached.
# not  You should enumerate thru the GPUs with the \ref
# NvAPI_GPU_QueryIlluminationSupport call to
# not  determine which GPU is managing the attribute.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 300.05
# not
# not \param [in] hPhysicalGpu  Physical GPU handle
# not \param  Attribute   An enumeration value specifying the Illumination
# attribute to be set
# not \param  Value   The new value for the specified attribute.
# not       This should be specified as a percentage of the full range of
# the attribute
# not       (0-100; 0 = off, 100 = full brightness)
# not       If a value is specified outside this range,
# NVAPI_INVALID_ARGUMENT will be returned.
# not
# not \return See \ref nvapistatus for the list of possible return values.
# Return values of special interest are:
# not   NVAPI_INVALID_ARGUMENT The specified attibute is not known to the
# driver, or the specified value is out of range.
# not   NVAPI_NOT_SUPPORTED  The specified attribute is not supported on
# the specified GPU.
# ///////////////////////////////////////////////////////////////////////
# not \ingroup gpu
_NV_GPU_SET_ILLUMINATION_PARM_V1._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < The handle of the GPU that you are checking for the specified
    # attribute.
    ('hPhysicalGpu', NvPhysicalGpuHandle),
    # not < An enumeration value specifying the Illumination attribute to
    # be querried.
    ('Attribute', NV_GPU_ILLUMINATION_ATTRIB),
    # not < A DWORD containing the new value for the specified attribute.
    ('Value', NvU32),
]

# not \ingroup gpu
NV_GPU_SET_ILLUMINATION_PARM = NV_GPU_SET_ILLUMINATION_PARM_V1
# not \ingroup gpu
NV_GPU_SET_ILLUMINATION_PARM_VER_1 = (
    MAKE_NVAPI_VERSION(NV_GPU_SET_ILLUMINATION_PARM_V1, 1)
)

# not \ingroup gpu
NV_GPU_SET_ILLUMINATION_PARM_VER = NV_GPU_SET_ILLUMINATION_PARM_VER_1

# not \ingroup gpu
NvAPI_GPU_SetIllumination = hDll.GPU_SetIllumination
NvAPI_GPU_SetIllumination.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GPU_SetIllumination(NV_GPU_SET_ILLUMINATION_PARM *pIlluminationInfo);


# /*not Enumeration of control modes that can be applied to Illumination
# Zones.
class NV_GPU_CLIENT_ILLUM_CTRL_MODE(ENUM):
    NV_GPU_CLIENT_ILLUM_CTRL_MODE_MANUAL_RGB = 0
    NV_GPU_CLIENT_ILLUM_CTRL_MODE_PIECEWISE_LINEAR_RGB = 1
    NV_GPU_CLIENT_ILLUM_CTRL_MODE_INVALID = 0xFF


NV_GPU_CLIENT_ILLUM_CTRL_MODE_MANUAL_RGB = NV_GPU_CLIENT_ILLUM_CTRL_MODE.NV_GPU_CLIENT_ILLUM_CTRL_MODE_MANUAL_RGB
NV_GPU_CLIENT_ILLUM_CTRL_MODE_PIECEWISE_LINEAR_RGB = NV_GPU_CLIENT_ILLUM_CTRL_MODE.NV_GPU_CLIENT_ILLUM_CTRL_MODE_PIECEWISE_LINEAR_RGB
NV_GPU_CLIENT_ILLUM_CTRL_MODE_INVALID = NV_GPU_CLIENT_ILLUM_CTRL_MODE.NV_GPU_CLIENT_ILLUM_CTRL_MODE_INVALID


# /*not Enumeration of locations where an Illumination Zone might be
# present. Encoding used - 1:0 - Number specifier (0) 4:2 - Location (TOP)
# 7:5 - Type (GPU/SLI)
class NV_GPU_CLIENT_ILLUM_ZONE_LOCATION(ENUM):
    NV_GPU_CLIENT_ILLUM_ZONE_LOCATION_GPU_TOP_0 = 0x00
    NV_GPU_CLIENT_ILLUM_ZONE_LOCATION_SLI_TOP_0 = 0x20
    NV_GPU_CLIENT_ILLUM_ZONE_LOCATION_INVALID = 0xFFFFFFFF


NV_GPU_CLIENT_ILLUM_ZONE_LOCATION_GPU_TOP_0 = NV_GPU_CLIENT_ILLUM_ZONE_LOCATION.NV_GPU_CLIENT_ILLUM_ZONE_LOCATION_GPU_TOP_0
NV_GPU_CLIENT_ILLUM_ZONE_LOCATION_SLI_TOP_0 = NV_GPU_CLIENT_ILLUM_ZONE_LOCATION.NV_GPU_CLIENT_ILLUM_ZONE_LOCATION_SLI_TOP_0
NV_GPU_CLIENT_ILLUM_ZONE_LOCATION_INVALID = NV_GPU_CLIENT_ILLUM_ZONE_LOCATION.NV_GPU_CLIENT_ILLUM_ZONE_LOCATION_INVALID


# /*not Enumeration of ILLUM_DEVICEs.
class NV_GPU_CLIENT_ILLUM_DEVICE_TYPE(ENUM):
    NV_GPU_CLIENT_ILLUM_DEVICE_TYPE_INVALID = 0
    NV_GPU_CLIENT_ILLUM_DEVICE_TYPE_MCUV10 = 1


NV_GPU_CLIENT_ILLUM_DEVICE_TYPE_INVALID = NV_GPU_CLIENT_ILLUM_DEVICE_TYPE.NV_GPU_CLIENT_ILLUM_DEVICE_TYPE_INVALID
NV_GPU_CLIENT_ILLUM_DEVICE_TYPE_MCUV10 = NV_GPU_CLIENT_ILLUM_DEVICE_TYPE.NV_GPU_CLIENT_ILLUM_DEVICE_TYPE_MCUV10


# /*not Enumeration of ILLUM_ZONEs.
class NV_GPU_CLIENT_ILLUM_ZONE_TYPE(ENUM):
    NV_GPU_CLIENT_ILLUM_ZONE_TYPE_INVALID = 0
    NV_GPU_CLIENT_ILLUM_ZONE_TYPE_RGB = 1
    NV_GPU_CLIENT_ILLUM_ZONE_TYPE_COLOR_FIXED = 2


NV_GPU_CLIENT_ILLUM_ZONE_TYPE_INVALID = NV_GPU_CLIENT_ILLUM_ZONE_TYPE.NV_GPU_CLIENT_ILLUM_ZONE_TYPE_INVALID
NV_GPU_CLIENT_ILLUM_ZONE_TYPE_RGB = NV_GPU_CLIENT_ILLUM_ZONE_TYPE.NV_GPU_CLIENT_ILLUM_ZONE_TYPE_RGB
NV_GPU_CLIENT_ILLUM_ZONE_TYPE_COLOR_FIXED = NV_GPU_CLIENT_ILLUM_ZONE_TYPE.NV_GPU_CLIENT_ILLUM_ZONE_TYPE_COLOR_FIXED

# /*not Number of color points for the piecewise linear control mode.
NV_GPU_CLIENT_ILLUM_CTRL_MODE_PIECEWISE_LINEAR_COLOR_ENDPOINTS = 2


# /*not Enumeration of Cycle types for piecewise linear control mode.
class NV_GPU_CLIENT_ILLUM_PIECEWISE_LINEAR_CYCLE_TYPE(ENUM):
    NV_GPU_CLIENT_ILLUM_PIECEWISE_LINEAR_CYCLE_HALF_HALT = 0
    NV_GPU_CLIENT_ILLUM_PIECEWISE_LINEAR_CYCLE_FULL_HALT = 1
    NV_GPU_CLIENT_ILLUM_PIECEWISE_LINEAR_CYCLE_FULL_REPEAT = 2
    NV_GPU_CLIENT_ILLUM_PIECEWISE_LINEAR_CYCLE_INVALID = 0xFF


NV_GPU_CLIENT_ILLUM_PIECEWISE_LINEAR_CYCLE_HALF_HALT = NV_GPU_CLIENT_ILLUM_PIECEWISE_LINEAR_CYCLE_TYPE.NV_GPU_CLIENT_ILLUM_PIECEWISE_LINEAR_CYCLE_HALF_HALT
NV_GPU_CLIENT_ILLUM_PIECEWISE_LINEAR_CYCLE_FULL_HALT = NV_GPU_CLIENT_ILLUM_PIECEWISE_LINEAR_CYCLE_TYPE.NV_GPU_CLIENT_ILLUM_PIECEWISE_LINEAR_CYCLE_FULL_HALT
NV_GPU_CLIENT_ILLUM_PIECEWISE_LINEAR_CYCLE_FULL_REPEAT = NV_GPU_CLIENT_ILLUM_PIECEWISE_LINEAR_CYCLE_TYPE.NV_GPU_CLIENT_ILLUM_PIECEWISE_LINEAR_CYCLE_FULL_REPEAT
NV_GPU_CLIENT_ILLUM_PIECEWISE_LINEAR_CYCLE_INVALID = NV_GPU_CLIENT_ILLUM_PIECEWISE_LINEAR_CYCLE_TYPE.NV_GPU_CLIENT_ILLUM_PIECEWISE_LINEAR_CYCLE_INVALID
NV_GPU_CLIENT_ILLUM_DEVICE_NUM_DEVICES_MAX = 32

# /*not Used in \ref NV_GPU_CLIENT_ILLUM_DEVICE_INFO_V1 Describes the
# static information of illumination device type MCUV10.
_NV_GPU_CLIENT_ILLUM_DEVICE_INFO_DATA_MCUV10._fields_ = [
    ('i2cDevIdx', NvU8)  # I2C Device Index Pointing to the illumination device in I2C Devices Table.
]


# /*not
class data(ctypes.Union):
    pass


data._fields_ = [
    ('mcuv10', NV_GPU_CLIENT_ILLUM_DEVICE_INFO_DATA_MCUV10),
    ('rsvd', NvU8 * 64),
]
_NV_GPU_CLIENT_ILLUM_DEVICE_INFO_V1.data = data

_NV_GPU_CLIENT_ILLUM_DEVICE_INFO_V1._fields_ = [
    ('type', NV_GPU_CLIENT_ILLUM_DEVICE_TYPE),
    ('ctrlModeMask', NvU32),
    ('data', _NV_GPU_CLIENT_ILLUM_DEVICE_INFO_V1.data),
    ('rsvd', NvU8 * 64),
]

# /*not
_NV_GPU_CLIENT_ILLUM_DEVICE_INFO_PARAMS_V1._fields_ = [
    # Version of structure. Must always be first member.
    ('version', NvU32),
    # Number of illumination devices present.
    ('numIllumDevices', NvU32),
    # Reserved bytes for possible future extension of this struct.
    ('rsvd', NvU8 * 64),
    ('devices', NV_GPU_CLIENT_ILLUM_DEVICE_INFO_V1 * NV_GPU_CLIENT_ILLUM_DEVICE_NUM_DEVICES_MAX),
]
NV_GPU_CLIENT_ILLUM_DEVICE_INFO_PARAMS_VER_1 = (
    MAKE_NVAPI_VERSION(NV_GPU_CLIENT_ILLUM_DEVICE_INFO_PARAMS_V1, 1)
)
NV_GPU_CLIENT_ILLUM_DEVICE_INFO_PARAMS_VER = (
    NV_GPU_CLIENT_ILLUM_DEVICE_INFO_PARAMS_VER_1
)
NV_GPU_CLIENT_ILLUM_DEVICE_INFO_PARAMS = NV_GPU_CLIENT_ILLUM_DEVICE_INFO_PARAMS_V1
# ///////////////////////////////////////////////////////////////////////
# not
# not FUNCTION NAME: NvAPI_GPU_ClientIllumDevicesGetInfo
# not
# not DESCRIPTION: This API returns static information about illumination
# devices on the
# not    given GPU.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 400
# not \param [in] hPhysicalGpu  The physical GPU handle
# not \param [out] pIllumDevicesInfo Pointer to structure containing static
# not      information about illumination devices.
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   If there are return error codes with specific meaning for this API,
# not   they are listed below.
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_ClientIllumDevicesGetInfo = hDll.GPU_ClientIllumDevicesGetInfo
NvAPI_GPU_ClientIllumDevicesGetInfo.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_ClientIllumDevicesGetInfo(__in NvPhysicalGpuHandle hPhysicalGpu, __inout NV_GPU_CLIENT_ILLUM_DEVICE_INFO_PARAMS *pIllumDevicesInfo);


# /*not Structure representing the data required for synchronization.
NV_GPU_CLIENT_ILLUM_DEVICE_SYNC_V1._fields_ = [
    # Boolean representing the need for synchronization.
    ('bSync', NvBool),
    # Time stamp value required for synchronization.
    ('timeStampms', NvU64),
    # Reserved for future.
    ('rsvd', NvU8 * 64),
]

# /*not Structure representing the device control parameters of each
# ILLUM_DEVICE.
NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_V1._fields_ = [
    # Type of the illum device.
    ('type', NV_GPU_CLIENT_ILLUM_DEVICE_TYPE),
    # Structure containing the synchronization data for the illumination device.
    ('syncData', NV_GPU_CLIENT_ILLUM_DEVICE_SYNC_V1),
    # Reserved for future.
    ('rsvd', NvU8 * 64),
]
NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL = NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_V1
# /*not Structure representing the control parameters of ILLUM_DEVICE-s.
NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_PARAMS_V1._fields_ = [
    # Version of structure. Must always be first member.
    ('version', NvU32),
    # Number of illumination devices present.
    ('numIllumDevices', NvU32),
    # Reserved bytes for possible future extension of this struct.
    ('rsvd', NvU8 * 64),
    ('devices', NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_V1 * NV_GPU_CLIENT_ILLUM_DEVICE_NUM_DEVICES_MAX),
]
NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_PARAMS_VER_1 = (
    MAKE_NVAPI_VERSION(NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_PARAMS_V1, 1)
)
NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_PARAMS_VER = (
    NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_PARAMS_VER_1
)
NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_PARAMS = NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_PARAMS_V1
# ///////////////////////////////////////////////////////////////////////
# not
# not FUNCTION NAME: NvAPI_GPU_ClientIllumDevicesGetControl
# not
# not DESCRIPTION: This API gets control parameters about illumination
# devices on the
# not    given GPU.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 400
# not \param [in] hPhysicalGpu  The physical GPU handle
# not \param [inout] pIllumDevicesControl Pointer to structure containing
# control
# not      information about illum devices.
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   If there are return error codes with specific meaning for this API,
# not   they are listed below.
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_ClientIllumDevicesGetControl = hDll.GPU_ClientIllumDevicesGetControl
NvAPI_GPU_ClientIllumDevicesGetControl.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_ClientIllumDevicesGetControl(__in NvPhysicalGpuHandle hPhysicalGpu, __inout NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_PARAMS *pClientIllumDevicesControl);


# ///////////////////////////////////////////////////////////////////////
# not
# not FUNCTION NAME: NvAPI_GPU_ClientIllumDevicesSetControl
# not
# not DESCRIPTION: This API sets control parameters about illumination
# devices on the
# not    given GPU.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 400
# not \param [in] hPhysicalGpu  The physical GPU handle
# not \param [inout] pClientIllumDevicesControl Pointer to structure
# containing control
# not      information about illum devices.
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   If there are return error codes with specific meaning for this API,
# not   they are listed below.
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_ClientIllumDevicesSetControl = hDll.GPU_ClientIllumDevicesSetControl
NvAPI_GPU_ClientIllumDevicesSetControl.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_ClientIllumDevicesSetControl(__in NvPhysicalGpuHandle hPhysicalGpu, __inout NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_PARAMS *pClientIllumDevicesControl);


NV_GPU_CLIENT_ILLUM_ZONE_NUM_ZONES_MAX = 32

_NV_GPU_CLIENT_ILLUM_ZONE_INFO_DATA_RGB._fields_ = [
    ('rsvd', NvU8),
]


class data(ctypes.Union):
    pass


data._fields_ = [
    # exceeds (ctypes.sizeof(rsvd) then rsvd has failed its purpose.
    ('rgb', NV_GPU_CLIENT_ILLUM_ZONE_INFO_DATA_RGB),
    # Reserved bytes for possible future extension of this struct.
    ('rsvd', NvU8 * 64),
]
_NV_GPU_CLIENT_ILLUM_ZONE_INFO_V1.data = data
_NV_GPU_CLIENT_ILLUM_ZONE_INFO_V1._fields_ = [
    ('type', NV_GPU_CLIENT_ILLUM_ZONE_TYPE),
    # Index pointing to an Illumination Device that controls this zone.
    ('illumDeviceIdx', NvU8),
    # Provider index for representing logical to physical zone mapping.
    ('provIdx', NvU8),
    # Location of the zone on the board.
    ('zoneLocation', NV_GPU_CLIENT_ILLUM_ZONE_LOCATION),
    ('data', _NV_GPU_CLIENT_ILLUM_ZONE_INFO_V1.data),
    ('rsvd', NvU8 * 64),
]
_NV_GPU_CLIENT_ILLUM_ZONE_INFO_PARAMS_V1._fields_ = [
    # Version of structure. Must always be first member.
    ('version', NvU32),
    # Number of illumination zones present.
    ('numIllumZones', NvU32),
    # Reserved bytes for possible future extension of this struct.
    ('rsvd', NvU8 * 64),
    ('zones', NV_GPU_CLIENT_ILLUM_ZONE_INFO_V1 * NV_GPU_CLIENT_ILLUM_ZONE_NUM_ZONES_MAX),
]
NV_GPU_CLIENT_ILLUM_ZONE_INFO_PARAMS_VER_1 = (
    MAKE_NVAPI_VERSION(NV_GPU_CLIENT_ILLUM_ZONE_INFO_PARAMS_V1, 1)
)
NV_GPU_CLIENT_ILLUM_ZONE_INFO_PARAMS_VER = (
    NV_GPU_CLIENT_ILLUM_ZONE_INFO_PARAMS_VER_1
)
NV_GPU_CLIENT_ILLUM_ZONE_INFO_PARAMS = NV_GPU_CLIENT_ILLUM_ZONE_INFO_PARAMS_V1
# ///////////////////////////////////////////////////////////////////////
# not
# not FUNCTION NAME: NvAPI_GPU_ClientIllumZonesGetInfo
# not
# not DESCRIPTION: This API returns static information about illumination
# zones on the
# not    given GPU.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 400
# not \param [in] hPhysicalGpu  The physical GPU handle
# not \param [out] pIllumZonesInfo Pointer to structure containing static
# not      information about illumination devices.
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   If there are return error codes with specific meaning for this API,
# not   they are listed below.
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_ClientIllumZonesGetInfo = hDll.GPU_ClientIllumZonesGetInfo
NvAPI_GPU_ClientIllumZonesGetInfo.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_ClientIllumZonesGetInfo(__in NvPhysicalGpuHandle hPhysicalGpu, __inout NV_GPU_CLIENT_ILLUM_ZONE_INFO_PARAMS *pIllumZonesInfo);


# /*not Used in \ref NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_RGB
# Parameters required to represent control mode of type \ref
# NV_GPU_CLIENT_ILLUM_CTRL_MODE_MANUAL_RGB.
_NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_RGB_PARAMS._fields_ = [
    # Red compenent of color applied to the zone.
    ('colorR', NvU8),
    # Green compenent of color applied to the zone.
    ('colorG', NvU8),
    # Blue compenent of color applied to the zone.
    ('colorB', NvU8),
    # Brightness perecentage value of the zone.
    ('brightnessPct', NvU8),
]
# /*not Used in \ref NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_RGB Data
# required to represent control mode of type \ref
# NV_GPU_CLIENT_ILLUM_CTRL_MODE_MANUAL_RGB.
_NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_RGB._fields_ = [
    # Parameters required to represent control mode of type * \ref NV_GPU_CLIENT_ILLUM_CTRL_MODE_MANUAL_RGB.
    ('rgbParams', NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_RGB_PARAMS),
]
# /*not Used in \ref NV_GPU_ILLUM_ZONE_CONTROL_DATA_PIECEWISE_LINEAR_RGB
# Data required to represent control mode of type \ref
# NV_GPU_ILLUM_CTRL_MODE_PIECEWISE_LINEAR_RGB.
_NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_PIECEWISE_LINEAR._fields_ = [
    # Type of cycle effect to apply.
    ('cycleType', NV_GPU_CLIENT_ILLUM_PIECEWISE_LINEAR_CYCLE_TYPE),
    # Number of times to repeat function within group period.
    ('grpCount', NvU8),
    # Time in ms to transition from color A to color B.
    ('riseTimems', NvU16),
    # Time in ms to transition from color B to color A.
    ('fallTimems', NvU16),
    # Time in ms to remain at color A before color A to color B transition.
    ('ATimems', NvU16),
    # Time in ms to remain at color B before color B to color A transition.
    ('BTimems', NvU16),
    # Time in ms to remain idle before next group of repeated function cycles.
    ('grpIdleTimems', NvU16),
    # Time in ms to offset the cycle relative to other zones.
    ('phaseOffsetms', NvU16),
]
# /*not Used in \ref NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_RGB Data
# required to represent control mode of type \ref
# NV_GPU_CLIENT_ILLUM_CTRL_MODE_PIECEWISE_LINEAR_RGB.
_NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_PIECEWISE_LINEAR_RGB._fields_ = [
    # Parameters required to represent control mode of type * \ref NV_GPU_CLIENT_ILLUM_CTRL_MODE_PIECEWISE_LINEAR_RGB.
    ('rgbParams',
     NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_RGB_PARAMS * NV_GPU_CLIENT_ILLUM_CTRL_MODE_PIECEWISE_LINEAR_COLOR_ENDPOINTS),
    ('piecewiseLinearData', NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_PIECEWISE_LINEAR),
]


# /*not Used in \ref NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_V1 Describes the
# control data for illumination zone of type \ref
# NV_GPU_CLIENT_ILLUM_ZONE_TYPE_RGB.
class data(ctypes.Union):
    pass


data._fields_ = [
    # exceeds (ctypes.sizeof(rsvd) then rsvd has failed its purpose.
    ('manualRGB', NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_RGB),
    ('piecewiseLinearRGB', NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_PIECEWISE_LINEAR_RGB),
    # Reserved bytes for possible future extension of this struct.
    ('rsvd', NvU8 * 64),
]
_NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_RGB.data = data
_NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_RGB._fields_ = [
    ('data', _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_RGB.data),
    # Union of illumination zone control data for zone of type NV_GPU_CLIENT_ILLUM_ZONE_TYPE_RGB.
    # * Interpreted as per ctrlMode. * Reserved for future.
    ('rsvd', NvU8 * 64),
]
# /*not Used in \ref NV_GPU_ILLUM_ZONE_CONTROL_DATA_MANUAL_COLOR_FIXED
# Parameters required to represent control mode of type \ref
# NV_GPU_ILLUM_CTRL_MODE_MANUAL_RGB.
_NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_COLOR_FIXED_PARAMS._fields_ = [
    # Brightness percentage value of the zone.
    ('brightnessPct', NvU8),
]
# /*not Used in \ref NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_COLOR_FIXED
# Data required to represent control mode of type \ref
# NV_GPU_CLIENT_ILLUM_CTRL_MODE_MANUAL_RGB.
_NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_COLOR_FIXED._fields_ = [
    # Parameters required to represent control mode of type * \ref NV_GPU_CLIENT_ILLUM_CTRL_MODE_MANUAL_RGB.
    ('colorFixedParams', NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_COLOR_FIXED_PARAMS),
]
# /*not Used in \ref NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_COLOR_FIXED
# Data required to represent control mode of type \ref
# NV_GPU_CLIENT_ILLUM_CTRL_MODE_PIECEWISE_LINEAR_RGB.
_NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_PIECEWISE_LINEAR_COLOR_FIXED._fields_ = [
    # Parameters required to represent control mode of type * \ref NV_GPU_CLIENT_ILLUM_CTRL_MODE_PIECEWISE_LINEAR_RGB.
    ('colorFixedParams',
     NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_COLOR_FIXED_PARAMS * NV_GPU_CLIENT_ILLUM_CTRL_MODE_PIECEWISE_LINEAR_COLOR_ENDPOINTS),
    ('piecewiseLinearData', NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_PIECEWISE_LINEAR),
]


# /*not Used in \ref NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_V1 Describes the
# control data for illum zone of type \ref
# NV_GPU_CLIENT_ILLUM_ZONE_TYPE_COLOR_FIXED.
class data(ctypes.Union):
    pass


data._fields_ = [
    # exceeds (ctypes.sizeof(rsvd) then rsvd has failed its purpose.
    ('manualColorFixed', NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_MANUAL_COLOR_FIXED),
    ('piecewiseLinearColorFixed', NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_PIECEWISE_LINEAR_COLOR_FIXED),
    # Reserved bytes for possible future extension of this struct.
    ('rsvd', NvU8 * 64),
]
_NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_COLOR_FIXED.data = data
_NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_COLOR_FIXED._fields_ = [
    ('data', _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_COLOR_FIXED.data),
    # Union of illum zone control data for zone of type NV_GPU_CLIENT_ILLUM_ZONE_TYPE_COLOR_FIXED.
    # * Interpreted as per ctrlMode. * Reserved for future.
    ('rsvd', NvU8 * 64),
]


class data(ctypes.Union):
    pass


data._fields_ = [
    ('rgb', NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_RGB),
    ('colorFixed', NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_DATA_COLOR_FIXED),
    ('rsvd', NvU8 * 64),
]
_NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_V1.data = data

_NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_V1._fields_ = [
    ('type', NV_GPU_CLIENT_ILLUM_ZONE_TYPE),
    ('ctrlMode', NV_GPU_CLIENT_ILLUM_CTRL_MODE),
    ('data', _NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_V1.data),
    ('rsvd', NvU8 * 64),
]

_NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_PARAMS_V1._fields_ = [
    ('version', NvU32),
    # Bit field specifying the set of values to retrieve or set * - default (NV_TRUE) * - currently active (NV_FALSE).
    ('bDefault', NvU32, 1),
    ('rsvdField', NvU32, 31),
    # Number of illumination zones present.
    ('numIllumZonesControl', NvU32),
    # Reserved bytes for possible future extension of this struct.
    ('rsvd', NvU8 * 64),
    ('zones', NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_V1 * NV_GPU_CLIENT_ILLUM_ZONE_NUM_ZONES_MAX),
]
NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_PARAMS_VER_1 = (
    MAKE_NVAPI_VERSION(NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_PARAMS_V1, 1)
)
NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_PARAMS_VER = (
    NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_PARAMS_VER_1
)
NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_PARAMS = NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_PARAMS_V1
# ///////////////////////////////////////////////////////////////////////
# not
# not FUNCTION NAME: NvAPI_GPU_ClientIllumZonesGetControl
# not
# not DESCRIPTION: Accessor for control information about illumination
# zones on the
# not   given GPU.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 400
# not \param [in] hPhysicalGpu  The physical GPU handle
# not \param [out] pIllumZonesControl Pointer to structure containing
# control
# not       information about illumination zones.
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   If there are return error codes with specific meaning for this API,
# not   they are listed below.
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_ClientIllumZonesGetControl = hDll.GPU_ClientIllumZonesGetControl
NvAPI_GPU_ClientIllumZonesGetControl.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_ClientIllumZonesGetControl(__in NvPhysicalGpuHandle hPhysicalGpu, __inout NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_PARAMS *pIllumZonesControl);


# ///////////////////////////////////////////////////////////////////////
# not
# not FUNCTION NAME: NvAPI_GPU_ClientIllumZonesSetControl
# not
# not DESCRIPTION: Mutator for control information about illumination
# zones on the
# not    given GPU.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 400
# not \param [in] hPhysicalGpu  The physical GPU handle
# not \param [out] pIllumZonesControl Pointer to structure containing
# control
# not       information about illumination zones.
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   If there are return error codes with specific meaning for this API,
# not   they are listed below.
# ///////////////////////////////////////////////////////////////////////
NvAPI_GPU_ClientIllumZonesSetControl = hDll.GPU_ClientIllumZonesSetControl
NvAPI_GPU_ClientIllumZonesSetControl.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_ClientIllumZonesSetControl(__in NvPhysicalGpuHandle hPhysicalGpu, __inout NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_PARAMS *pIllumZonesControl);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_EnumNvidiaDisplayHandle
# not This function returns the handle of the NVIDIA display specified by
# the enum
# not    index (thisEnum). The client should keep enumerating until it
# not    returns error.
# not
# not    Note: Display handles can get invalidated on a modeset, so the
# calling applications need to
# not    renum the handles after every modeset.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 80
# not
# not \param [in] thisEnum The index of the NVIDIA display.
# not \param [out] pNvDispHandle Pointer to the NVIDIA display handle.
# not
# not \retval NVAPI_INVALID_ARGUMENT  Either the handle pointer is NULL or
# enum index too big
# not \retval NVAPI_OK    Return a valid NvDisplayHandle based on the enum
# index
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND No NVIDIA device found in the
# system
# not \retval NVAPI_END_ENUMERATION  No more display device to enumerate
# not \ingroup disphandle
# ///////////////////////////////////////////////////////////////////////
NvAPI_EnumNvidiaDisplayHandle = hDll.EnumNvidiaDisplayHandle
NvAPI_EnumNvidiaDisplayHandle.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_EnumNvidiaDisplayHandle(NvU32 thisEnum, NvDisplayHandle *pNvDispHandle);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_EnumNvidiaUnAttachedDisplayHandle
# not This function returns the handle of the NVIDIA unattached display
# specified by the enum
# not    index (thisEnum). The client should keep enumerating until it
# not    returns error.
# not    Note: Display handles can get invalidated on a modeset, so the
# calling applications need to
# not    renum the handles after every modeset.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 80
# not
# not \param [in] thisEnum   The index of the NVIDIA display.
# not \param [out] pNvUnAttachedDispHandle Pointer to the NVIDIA display
# handle of the unattached display.
# not
# not \retval NVAPI_INVALID_ARGUMENT  Either the handle pointer is NULL or
# enum index too big
# not \retval NVAPI_OK     Return a valid NvDisplayHandle based on the
# enum index
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND No NVIDIA device found in the
# system
# not \retval NVAPI_END_ENUMERATION  No more display device to enumerate.
# not \ingroup disphandle
# ///////////////////////////////////////////////////////////////////////
NvAPI_EnumNvidiaUnAttachedDisplayHandle = hDll.EnumNvidiaUnAttachedDisplayHandle
NvAPI_EnumNvidiaUnAttachedDisplayHandle.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_EnumNvidiaUnAttachedDisplayHandle(NvU32 thisEnum, NvUnAttachedDisplayHandle *pNvUnAttachedDispHandle);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_CreateDisplayFromUnAttachedDisplay
# not This function converts the unattached display handle to an active
# attached display handle.
# not
# not At least one GPU must be present in the system and running an NVIDIA
# display driver.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 80
# not
# not \retval NVAPI_INVALID_ARGUMENT  hNvUnAttachedDisp is not valid or
# pNvDisplay is NULL.
# not \retval NVAPI_OK     One or more handles were returned
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND No NVIDIA GPU driving a
# display was found
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_CreateDisplayFromUnAttachedDisplay = hDll.CreateDisplayFromUnAttachedDisplay
NvAPI_CreateDisplayFromUnAttachedDisplay.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_CreateDisplayFromUnAttachedDisplay(NvUnAttachedDisplayHandle hNvUnAttachedDisp, NvDisplayHandle *pNvDisplay);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetAssociatedNVidiaDisplayHandle
# not This function returns the handle of the NVIDIA display that is
# associated
# not with the given display "name" (such as "\\.\DISPLAY1").
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 80
# not
# not \retval NVAPI_INVALID_ARGUMENT  Either argument is NULL
# not \retval NVAPI_OK    *pNvDispHandle is now valid
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND No NVIDIA device maps to that
# display name
# not \ingroup disphandle
# ///////////////////////////////////////////////////////////////////////
NvAPI_GetAssociatedNvidiaDisplayHandle = hDll.GetAssociatedNvidiaDisplayHandle
NvAPI_GetAssociatedNvidiaDisplayHandle.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GetAssociatedNvidiaDisplayHandle(const char *szDisplayName, NvDisplayHandle *pNvDispHandle);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DISP_GetAssociatedUnAttachedNvidiaDisplayHandle
# not DESCRIPTION: This function returns the handle of an unattached
# NVIDIA display that is
# not    associated with the given display name (such as "\\DISPLAY1").
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 185
# not
# not \retval ::NVAPI_INVALID_ARGUMENT  Either argument is NULL.
# not \retval ::NVAPI_OK     *pNvUnAttachedDispHandle is now valid.
# not \retval ::NVAPI_NVIDIA_DEVICE_NOT_FOUND No NVIDIA device maps to
# that display name.
# not
# not \ingroup disphandle
# ///////////////////////////////////////////////////////////////////////
NvAPI_DISP_GetAssociatedUnAttachedNvidiaDisplayHandle = hDll.DISP_GetAssociatedUnAttachedNvidiaDisplayHandle
NvAPI_DISP_GetAssociatedUnAttachedNvidiaDisplayHandle.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DISP_GetAssociatedUnAttachedNvidiaDisplayHandle(const char *szDisplayName, NvUnAttachedDisplayHandle *pNvUnAttachedDispHandle);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetAssociatedNVidiaDisplayName
# not For a given NVIDIA display handle, this function returns a string
# (such as "\\.\DISPLAY1") to identify the display.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 80
# not
# not \retval NVAPI_INVALID_ARGUMENT  Either argument is NULL
# not \retval NVAPI_OK     *pNvDispHandle is now valid
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND No NVIDIA device maps to that
# display name
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_GetAssociatedNvidiaDisplayName = hDll.GetAssociatedNvidiaDisplayName
NvAPI_GetAssociatedNvidiaDisplayName.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GetAssociatedNvidiaDisplayName(NvDisplayHandle NvDispHandle, NvAPI_ShortString szDisplayName);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetUnAttachedAssociatedDisplayName
# not This function returns the display name given, for example,
# "\\DISPLAY1", using the unattached NVIDIA display handle
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 95
# not
# not \retval NVAPI_INVALID_ARGUMENT  Either argument is NULL
# not \retval NVAPI_OK     *pNvDispHandle is now valid
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND No NVIDIA device maps to that
# display name
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_GetUnAttachedAssociatedDisplayName = hDll.GetUnAttachedAssociatedDisplayName
NvAPI_GetUnAttachedAssociatedDisplayName.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GetUnAttachedAssociatedDisplayName(NvUnAttachedDisplayHandle hNvUnAttachedDisp, NvAPI_ShortString szDisplayName);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_EnableHWCursor
# not This function enables hardware cursor support
# not
# not SUPPORTED OS: Windows XP
# not
# not
# not
# not \since Release: 80
# not
# not \return NVAPI_ERROR or NVAPI_OK
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_EnableHWCursor = hDll.EnableHWCursor
NvAPI_EnableHWCursor.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_EnableHWCursor(NvDisplayHandle hNvDisplay);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DisableHWCursor
# not This function disables hardware cursor support
# not
# not SUPPORTED OS: Windows XP
# not
# not
# not \since Release: 80
# not
# not \return NVAPI_ERROR or NVAPI_OK
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_DisableHWCursor = hDll.DisableHWCursor
NvAPI_DisableHWCursor.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DisableHWCursor(NvDisplayHandle hNvDisplay);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetVBlankCounter
# not This function gets the V-blank counter
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 80
# not
# not \return NVAPI_ERROR or NVAPI_OK
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_GetVBlankCounter = hDll.GetVBlankCounter
NvAPI_GetVBlankCounter.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GetVBlankCounter(NvDisplayHandle hNvDisplay, NvU32 *pCounter);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_SetRefreshRateOverride
# not This function overrides the refresh rate on the given
# display/outputsMask.
# not The new refresh rate can be applied right away in this API call or
# deferred to be applied with the
# not next OS modeset. The override is good for only one modeset
# (regardless whether it's deferred or immediate).
# not
# not
# not SUPPORTED OS: Windows XP
# not
# not
# not \since Release: 80
# not
# not \param [in] hNvDisplay The NVIDIA display handle. It can be
# NVAPI_DEFAULT_HANDLE or a handle
# not     enumerated from NvAPI_EnumNVidiaDisplayHandle().
# not \param [in] outputsMask A set of bits that identify all target
# outputs which are associated with the NVIDIA
# not     display handle to apply the refresh rate override. When SLI is
# enabled, the
# not     outputsMask only applies to the GPU that is driving the display
# output.
# not \param [in] refreshRate The override value. "0.0" means cancel the
# override.
# not \param [in] bSetDeferred
# not   - "0": Apply the refresh rate override immediately in this API
# call.\p
# not   - "1": Apply refresh rate at the next OS modeset.
# not
# not \retval NVAPI_INVALID_ARGUMENT hNvDisplay or outputsMask is invalid
# not \retval NVAPI_OK   The refresh rate override is correct set
# not \retval NVAPI_ERROR  The operation failed
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_SetRefreshRateOverride = hDll.SetRefreshRateOverride
NvAPI_SetRefreshRateOverride.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_SetRefreshRateOverride(NvDisplayHandle hNvDisplay, NvU32 outputsMask, float refreshRate, NvU32 bSetDeferred);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetAssociatedDisplayOutputId
# not This function gets the active outputId associated with the display
# handle.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 90
# not
# not \param [in] hNvDisplay NVIDIA Display selection. It can be
# NVAPI_DEFAULT_HANDLE or a handle enumerated from
# NvAPI_EnumNVidiaDisplayHandle().
# not \param [out] outputId The active display output ID associated with
# the selected display handle hNvDisplay.
# not     The outputid will have only one bit set. In the case of Clone or
# Span mode, this will indicate the
# not     display outputId of the primary display that the GPU is driving.
# See \ref handles.
# not
# not \retval NVAPI_OK    Call successful.
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND No NVIDIA GPU driving a
# display was found.
# not \retval NVAPI_EXPECTED_DISPLAY_HANDLE hNvDisplay is not a valid
# display handle.
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_GetAssociatedDisplayOutputId = hDll.GetAssociatedDisplayOutputId
NvAPI_GetAssociatedDisplayOutputId.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GetAssociatedDisplayOutputId(NvDisplayHandle hNvDisplay, NvU32 *pOutputId);


# not \ingroup dispcontrol
# not Used in NvAPI_GetDisplayPortInfo().
_NV_DISPLAY_PORT_INFO_V1._fields_ = [
    # not < Structure version
    ('version', NvU32),
    # not < DPCD version of the monitor
    ('dpcd_ver', NvU32),
    # not < Maximum supported link rate
    ('maxLinkRate', NV_DP_LINK_RATE),
    # not < Maximum supported lane count
    ('maxLaneCount', NV_DP_LANE_COUNT),
    # not < Current link rate
    ('curLinkRate', NV_DP_LINK_RATE),
    # not < Current lane count
    ('curLaneCount', NV_DP_LANE_COUNT),
    # not < Current color format
    ('colorFormat', NV_DP_COLOR_FORMAT),
    # not < Dynamic range
    ('dynamicRange', NV_DP_DYNAMIC_RANGE),
    # not < Ignored in RGB space
    ('colorimetry', NV_DP_COLORIMETRY),
    # not < Current bit-per-component
    ('bpc', NV_DP_BPC),
    # not < If the monitor is driven by a DisplayPort
    ('isDp', NvU32, 1),
    # not < If the monitor is driven by an NV Dp transmitter
    ('isInternalDp', NvU32, 1),
    # not < If the color format change is supported
    ('isColorCtrlSupported', NvU32, 1),
    # not < If 6 bpc is supported
    ('is6BPCSupported', NvU32, 1),
    # not < If 8 bpc is supported
    ('is8BPCSupported', NvU32, 1),
    # not < If 10 bpc is supported
    ('is10BPCSupported', NvU32, 1),
    # not < If 12 bpc is supported
    ('is12BPCSupported', NvU32, 1),
    # not < If 16 bpc is supported
    ('is16BPCSupported', NvU32, 1),
    # not < If YCrCb420 is supported
    ('isYCrCb420Supported', NvU32, 1),
    # not < If YCrCb422 is supported
    ('isYCrCb422Supported', NvU32, 1),
    # not < If YCrCb444 is supported
    ('isYCrCb444Supported', NvU32, 1),
    # not < If Rgb444 is supported on the current mode
    ('isRgb444SupportedOnCurrentMode', NvU32, 1),
    # not < If YCbCr444 is supported on the current mode
    ('isYCbCr444SupportedOnCurrentMode', NvU32, 1),
    # not < If YCbCr422 is supported on the current mode
    ('isYCbCr422SupportedOnCurrentMode', NvU32, 1),
    # not < If YCbCr420 is supported on the current mode
    ('isYCbCr420SupportedOnCurrentMode', NvU32, 1),
    # if 6 bpc is supported On Current Mode
    ('is6BPCSupportedOnCurrentMode', NvU32, 1),
    # if 8 bpc is supported On Current Mode
    ('is8BPCSupportedOnCurrentMode', NvU32, 1),
    # if 10 bpc is supported On Current Mode
    ('is10BPCSupportedOnCurrentMode', NvU32, 1),
    # if 12 bpc is supported On Current Mode
    ('is12BPCSupportedOnCurrentMode', NvU32, 1),
    # if 16 bpc is supported On Current Mode
    ('is16BPCSupportedOnCurrentMode', NvU32, 1),
    # if xvYCC 601 extended colorimetry is supported
    ('isMonxvYCC601Capable', NvU32, 1),
    # if xvYCC 709 extended colorimetry is supported
    ('isMonxvYCC709Capable', NvU32, 1),
    # if sYCC601 extended colorimetry is supported
    ('isMonsYCC601Capable', NvU32, 1),
    # if AdobeYCC601 extended colorimetry is supported
    ('isMonAdobeYCC601Capable', NvU32, 1),
    # if AdobeRGB extended colorimetry is supported
    ('isMonAdobeRGBCapable', NvU32, 1),
    # if BT2020 RGB extended colorimetry is supported
    ('isMonBT2020RGBCapable', NvU32, 1),
    # if BT2020 Y'CbCr extended colorimetry is supported
    ('isMonBT2020YCCCapable', NvU32, 1),
    # if BT2020 cYCbCr (ant luminance) extended colorimetry is supported
    ('isMonBT2020cYCCCapable', NvU32, 1),
    # not < reserved
    ('reserved', NvU32, 4),
]
NV_DISPLAY_PORT_INFO = NV_DISPLAY_PORT_INFO_V1

# not Macro for constructing the version field of NV_DISPLAY_PORT_INFO.
NV_DISPLAY_PORT_INFO_VER1 = MAKE_NVAPI_VERSION(NV_DISPLAY_PORT_INFO, 1)
NV_DISPLAY_PORT_INFO_VER2 = MAKE_NVAPI_VERSION(NV_DISPLAY_PORT_INFO, 2)
NV_DISPLAY_PORT_INFO_VER = NV_DISPLAY_PORT_INFO_VER2

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetDisplayPortInfo
# not \fn
# NvAPI_GetDisplayPortInfo(__in_opt NvDisplayHandle hNvDisplay, __in NvU32 outputId, __inout NV_DISPLAY_PORT_INFO *pInfo)
#
# not DESCRIPTION:  This function returns the current DisplayPort-related
# information on the specified device (monitor).
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 165
# not
# not \param [in]  hvDisplay  NVIDIA Display selection. It can be
# NVAPI_DEFAULT_HANDLE or a handle enumerated from
# NvAPI_EnumNVidiaDisplayHandle().
# not      This parameter is ignored when the outputId is a NvAPI
# displayId.
# not \param [in]  outputId This can either be the connection bit mask or
# the NvAPI displayId. When the legacy connection bit mask is passed,
# not      it should have exactly 1 bit set to indicate a single display.
# If it's "0" then the default outputId from
# not      NvAPI_GetAssociatedDisplayOutputId() will be used. See \ref
# handles.
# not \param [out] pInfo  The DisplayPort information
# not
# not \retval  NVAPI_OK   Completed request
# not \retval  NVAPI_ERROR   Miscellaneous error occurred
# not \retval  NVAPI_INVALID_ARGUMENT Invalid input parameter.
# ///////////////////////////////////////////////////////////////////////
# not \ingroup  dispcontrol
NvAPI_GetDisplayPortInfo = hDll.GetDisplayPortInfo
NvAPI_GetDisplayPortInfo.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GetDisplayPortInfo(__in_opt NvDisplayHandle hNvDisplay, __in NvU32 outputId, __inout NV_DISPLAY_PORT_INFO *pInfo);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_SetDisplayPort
# not \fn
# NvAPI_SetDisplayPort(NvDisplayHandle hNvDisplay, NvU32 outputId, NV_DISPLAY_PORT_CONFIG *pCfg)
#
# not DESCRIPTION:  This function sets up DisplayPort-related
# configurations.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 165
# not
# not \param [in]  hNvDisplay NVIDIA display handle. It can be
# NVAPI_DEFAULT_HANDLE or a handle enumerated from
# not      NvAPI_EnumNVidiaDisplayHandle().
# not \param [in]  outputId This display output ID, when it's "0" it means
# the default outputId generated from the return of
# not      NvAPI_GetAssociatedDisplayOutputId(). See \ref handles.
# not \param [in]  pCfg  The display port config structure. If pCfg is
# NULL, it means to use the driver's default value to setup.
# not
# not \retval   NVAPI_OK   Completed request
# not \retval   NVAPI_ERROR   Miscellaneous error occurred
# not \retval   NVAPI_INVALID_ARGUMENT Invalid input parameter
# ///////////////////////////////////////////////////////////////////////
# not \ingroup dispcontrol
# not DisplayPort configuration settings - used in NvAPI_SetDisplayPort().
NV_DISPLAY_PORT_CONFIG._fields_ = [
    # not < Structure version - 2 is the latest
    ('version', NvU32),
    # not < Link rate
    ('linkRate', NV_DP_LINK_RATE),
    # not < Lane count
    ('laneCount', NV_DP_LANE_COUNT),
    # not < Color format to set
    ('colorFormat', NV_DP_COLOR_FORMAT),
    # not < Dynamic range
    ('dynamicRange', NV_DP_DYNAMIC_RANGE),
    # not < Ignored in RGB space
    ('colorimetry', NV_DP_COLORIMETRY),
    # not < Bit-per-component
    ('bpc', NV_DP_BPC),
    # not < If the control panel is making this call due to HPD
    ('isHPD', NvU32, 1),
    # not < Requires an OS modeset to finalize the setup if set
    ('isSetDeferred', NvU32, 1),
    # not < Force the chroma low_pass_filter to be off
    ('isChromaLpfOff', NvU32, 1),
    # not < Force to turn off dither
    ('isDitherOff', NvU32, 1),
    # not < If testing mode, skip validation
    ('testLinkTrain', NvU32, 1),
    # not < If testing mode, skip validation
    ('testColorChange', NvU32, 1),
]

# not \addtogroup dispcontrol
# not @{
# not Macro for constructing the version field of NV_DISPLAY_PORT_CONFIG
NV_DISPLAY_PORT_CONFIG_VER = (
    MAKE_NVAPI_VERSION(NV_DISPLAY_PORT_CONFIG, 2)
)
# not Macro for constructing the version field of NV_DISPLAY_PORT_CONFIG
NV_DISPLAY_PORT_CONFIG_VER_1 = (
    MAKE_NVAPI_VERSION(NV_DISPLAY_PORT_CONFIG, 1)
)
# not Macro for constructing the version field of NV_DISPLAY_PORT_CONFIG
NV_DISPLAY_PORT_CONFIG_VER_2 = (
    MAKE_NVAPI_VERSION(NV_DISPLAY_PORT_CONFIG, 2)
)
# not @}
# not \ingroup  dispcontrol
NvAPI_SetDisplayPort = hDll.SetDisplayPort
NvAPI_SetDisplayPort.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_SetDisplayPort(NvDisplayHandle hNvDisplay, NvU32 outputId, NV_DISPLAY_PORT_CONFIG *pCfg);


# not \ingroup dispcontrol
# not Used in NvAPI_GetHDMISupportInfo().
_NV_HDMI_SUPPORT_INFO_V1._fields_ = [
    # not < Structure version
    ('version', NvU32),
    # not < If the GPU can handle HDMI
    ('isGpuHDMICapable', NvU32, 1),
    # not < If the monitor supports underscan
    ('isMonUnderscanCapable', NvU32, 1),
    # not < If the monitor supports basic audio
    ('isMonBasicAudioCapable', NvU32, 1),
    # not < If YCbCr 4:4:4 is supported
    ('isMonYCbCr444Capable', NvU32, 1),
    # not < If YCbCr 4:2:2 is supported
    ('isMonYCbCr422Capable', NvU32, 1),
    # not < If xvYCC 601 is supported
    ('isMonxvYCC601Capable', NvU32, 1),
    # not < If xvYCC 709 is supported
    ('isMonxvYCC709Capable', NvU32, 1),
    # not < If the monitor is HDMI (with IEEE's HDMI registry ID)
    ('isMonHDMI', NvU32, 1),
    # not < Reserved.
    ('reserved', NvU32, 24),
    # not < Revision number of the EDID 861 extension
    ('EDID861ExtRev', NvU32),
]

_NV_HDMI_SUPPORT_INFO_V2._fields_ = [
    # not < Structure version
    ('version', NvU32),
    # not < If the GPU can handle HDMI
    ('isGpuHDMICapable', NvU32, 1),
    # not < If the monitor supports underscan
    ('isMonUnderscanCapable', NvU32, 1),
    # not < If the monitor supports basic audio
    ('isMonBasicAudioCapable', NvU32, 1),
    # not < If YCbCr 4:4:4 is supported
    ('isMonYCbCr444Capable', NvU32, 1),
    # not < If YCbCr 4:2:2 is supported
    ('isMonYCbCr422Capable', NvU32, 1),
    # not < If xvYCC extended colorimetry 601 is supported
    ('isMonxvYCC601Capable', NvU32, 1),
    # not < If xvYCC extended colorimetry 709 is supported
    ('isMonxvYCC709Capable', NvU32, 1),
    # not < If the monitor is HDMI (with IEEE's HDMI registry ID)
    ('isMonHDMI', NvU32, 1),
    # not < if sYCC601 extended colorimetry is supported
    ('isMonsYCC601Capable', NvU32, 1),
    # not < if AdobeYCC601 extended colorimetry is supported
    ('isMonAdobeYCC601Capable', NvU32, 1),
    # not < if AdobeRGB extended colorimetry is supported
    ('isMonAdobeRGBCapable', NvU32, 1),
    # not < Reserved.
    ('reserved', NvU32, 21),
    # not < Revision number of the EDID 861 extension
    ('EDID861ExtRev', NvU32),
]
NV_HDMI_SUPPORT_INFO_VER1 = (
    MAKE_NVAPI_VERSION(NV_HDMI_SUPPORT_INFO_V1, 1)
)
NV_HDMI_SUPPORT_INFO_VER2 = (
    MAKE_NVAPI_VERSION(NV_HDMI_SUPPORT_INFO_V2, 2)
)

NV_HDMI_SUPPORT_INFO = NV_HDMI_SUPPORT_INFO_V2
NV_HDMI_SUPPORT_INFO_VER = NV_HDMI_SUPPORT_INFO_VER2

# not SUPPORTED OS: Windows 7 and higher
# not
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetHDMISupportInfo
# not \fn
# NvAPI_GetHDMISupportInfo(__in_opt NvDisplayHandle hNvDisplay, __in NvU32 outputId, __inout NV_HDMI_SUPPORT_INFO *pInfo)
#
# not This API returns the current infoframe data on the specified
# device(monitor).
# not
# not \since Release: 95
# not
# not \param [in] hvDisplay NVIDIA Display selection. It can be
# NVAPI_DEFAULT_HANDLE or a handle enumerated from
# NvAPI_EnumNVidiaDisplayHandle().
# not     This parameter is ignored when the outputId is a NvAPI displayId.
# not \param [in] outputId This can either be the connection bit mask or
# the NvAPI displayId. When the legacy connection bit mask is passed,
# not     it should have exactly 1 bit set to indicate a single display.
# If it's "0" then the default outputId from
# not     NvAPI_GetAssociatedDisplayOutputId() will be used. See \ref
# handles.
# not \param [out] pInfo The monitor and GPU's HDMI support info
# not
# not \retval NVAPI_OK   Completed request
# not \retval NVAPI_ERROR   Miscellaneous error occurred
# not \retval NVAPI_INVALID_ARGUMENT Invalid input parameter.
# ///////////////////////////////////////////////////////////////////////
# not \ingroup dispcontrol
NvAPI_GetHDMISupportInfo = hDll.GetHDMISupportInfo
NvAPI_GetHDMISupportInfo.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GetHDMISupportInfo(__in_opt NvDisplayHandle hNvDisplay, __in NvU32 outputId, __inout NV_HDMI_SUPPORT_INFO *pInfo);


# not \ingroup dispcontrol
class NV_INFOFRAME_CMD(ENUM):
    # not < Returns the fields in the infoframe with values set by the
    # manufacturer - NVIDIA/OEM.
    NV_INFOFRAME_CMD_GET_DEFAULT = 0

    # not < Sets the fields in the infoframe to auto, and infoframe to the
    # default infoframe for use in a set.
    NV_INFOFRAME_CMD_RESET = 1
    NV_INFOFRAME_CMD_GET = 2

    # not < Set the current infoframe state (flushed to the monitor), the
    # values are one time and do not persist.
    NV_INFOFRAME_CMD_SET = 3

    # not < Get the override infoframe state, non-override fields will be
    # set to value = AUTO, overridden fields will have the current
    # override values.
    NV_INFOFRAME_CMD_GET_OVERRIDE = 4

    # not < Set the override infoframe state, non-override fields will be
    # set to value = AUTO, other values indicate override; persist across
    # modeset/reboot
    NV_INFOFRAME_CMD_SET_OVERRIDE = 5

    # not < get properties associated with infoframe
    # (each of the infoframe type will have properties)
    NV_INFOFRAME_CMD_GET_PROPERTY = 6
    NV_INFOFRAME_CMD_SET_PROPERTY = 7


NV_INFOFRAME_CMD_GET_DEFAULT = NV_INFOFRAME_CMD.NV_INFOFRAME_CMD_GET_DEFAULT
NV_INFOFRAME_CMD_RESET = NV_INFOFRAME_CMD.NV_INFOFRAME_CMD_RESET
NV_INFOFRAME_CMD_GET = NV_INFOFRAME_CMD.NV_INFOFRAME_CMD_GET
NV_INFOFRAME_CMD_SET = NV_INFOFRAME_CMD.NV_INFOFRAME_CMD_SET
NV_INFOFRAME_CMD_GET_OVERRIDE = NV_INFOFRAME_CMD.NV_INFOFRAME_CMD_GET_OVERRIDE
NV_INFOFRAME_CMD_SET_OVERRIDE = NV_INFOFRAME_CMD.NV_INFOFRAME_CMD_SET_OVERRIDE
NV_INFOFRAME_CMD_GET_PROPERTY = NV_INFOFRAME_CMD.NV_INFOFRAME_CMD_GET_PROPERTY
NV_INFOFRAME_CMD_SET_PROPERTY = NV_INFOFRAME_CMD.NV_INFOFRAME_CMD_SET_PROPERTY


class NV_INFOFRAME_PROPERTY_MODE(ENUM):
    NV_INFOFRAME_PROPERTY_MODE_AUTO = 0
    NV_INFOFRAME_PROPERTY_MODE_ENABLE = 1
    NV_INFOFRAME_PROPERTY_MODE_DISABLE = 2

    # not < Driver only sends infoframe when client requests it via
    # infoframe escape call.
    NV_INFOFRAME_PROPERTY_MODE_ALLOW_OVERRIDE = 3


NV_INFOFRAME_PROPERTY_MODE_AUTO = NV_INFOFRAME_PROPERTY_MODE.NV_INFOFRAME_PROPERTY_MODE_AUTO
NV_INFOFRAME_PROPERTY_MODE_ENABLE = NV_INFOFRAME_PROPERTY_MODE.NV_INFOFRAME_PROPERTY_MODE_ENABLE
NV_INFOFRAME_PROPERTY_MODE_DISABLE = NV_INFOFRAME_PROPERTY_MODE.NV_INFOFRAME_PROPERTY_MODE_DISABLE
NV_INFOFRAME_PROPERTY_MODE_ALLOW_OVERRIDE = NV_INFOFRAME_PROPERTY_MODE.NV_INFOFRAME_PROPERTY_MODE_ALLOW_OVERRIDE


# not Returns whether the current monitor is in blacklist or force this
# monitor to be in blacklist.
class NV_INFOFRAME_PROPERTY_BLACKLIST(ENUM):
    NV_INFOFRAME_PROPERTY_BLACKLIST_FALSE = 0
    NV_INFOFRAME_PROPERTY_BLACKLIST_TRUE = 1


NV_INFOFRAME_PROPERTY_BLACKLIST_FALSE = NV_INFOFRAME_PROPERTY_BLACKLIST.NV_INFOFRAME_PROPERTY_BLACKLIST_FALSE
NV_INFOFRAME_PROPERTY_BLACKLIST_TRUE = NV_INFOFRAME_PROPERTY_BLACKLIST.NV_INFOFRAME_PROPERTY_BLACKLIST_TRUE

NV_INFOFRAME_PROPERTY._fields_ = [
    ('mode', NvU32, 4),
    ('blackList', NvU32, 2),
    ('reserved', NvU32, 10),
    ('version', NvU32, 8),
    ('length', NvU32, 8),
]


# not Byte1 related
class NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO_NODATA = 0
    NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO_OVERSCAN = 1
    NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO_UNDERSCAN = 2
    NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO_FUTURE = 3
    NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO_AUTO = 7


NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO_NODATA = NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO.NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO_NODATA
NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO_OVERSCAN = NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO.NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO_OVERSCAN
NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO_UNDERSCAN = NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO.NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO_UNDERSCAN
NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO_FUTURE = NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO.NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO_FUTURE
NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO_AUTO = NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO.NV_INFOFRAME_FIELD_VALUE_AVI_SCANINFO_AUTO


class NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA_NOT_PRESENT = 0
    NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA_VERTICAL_PRESENT = 1
    NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA_HORIZONTAL_PRESENT = 2
    NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA_BOTH_PRESENT = 3
    NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA_AUTO = 7


NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA_NOT_PRESENT = NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA.NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA_NOT_PRESENT
NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA_VERTICAL_PRESENT = NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA.NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA_VERTICAL_PRESENT
NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA_HORIZONTAL_PRESENT = NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA.NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA_HORIZONTAL_PRESENT
NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA_BOTH_PRESENT = NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA.NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA_BOTH_PRESENT
NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA_AUTO = NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA.NV_INFOFRAME_FIELD_VALUE_AVI_BARDATA_AUTO


class NV_INFOFRAME_FIELD_VALUE_AVI_ACTIVEFORMATINFO(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AVI_AFI_ABSENT = 0
    NV_INFOFRAME_FIELD_VALUE_AVI_AFI_PRESENT = 1
    NV_INFOFRAME_FIELD_VALUE_AVI_AFI_AUTO = 3


NV_INFOFRAME_FIELD_VALUE_AVI_AFI_ABSENT = NV_INFOFRAME_FIELD_VALUE_AVI_ACTIVEFORMATINFO.NV_INFOFRAME_FIELD_VALUE_AVI_AFI_ABSENT
NV_INFOFRAME_FIELD_VALUE_AVI_AFI_PRESENT = NV_INFOFRAME_FIELD_VALUE_AVI_ACTIVEFORMATINFO.NV_INFOFRAME_FIELD_VALUE_AVI_AFI_PRESENT
NV_INFOFRAME_FIELD_VALUE_AVI_AFI_AUTO = NV_INFOFRAME_FIELD_VALUE_AVI_ACTIVEFORMATINFO.NV_INFOFRAME_FIELD_VALUE_AVI_AFI_AUTO


class NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT_RGB = 0
    NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT_YCbCr422 = 1
    NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT_YCbCr444 = 2
    NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT_FUTURE = 3
    NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT_AUTO = 7


NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT_RGB = NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT.NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT_RGB
NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT_YCbCr422 = NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT.NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT_YCbCr422
NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT_YCbCr444 = NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT.NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT_YCbCr444
NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT_FUTURE = NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT.NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT_FUTURE
NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT_AUTO = NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT.NV_INFOFRAME_FIELD_VALUE_AVI_COLORFORMAT_AUTO


class NV_INFOFRAME_FIELD_VALUE_AVI_F17(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AVI_F17_FALSE = 0
    NV_INFOFRAME_FIELD_VALUE_AVI_F17_TRUE = 1
    NV_INFOFRAME_FIELD_VALUE_AVI_F17_AUTO = 3


NV_INFOFRAME_FIELD_VALUE_AVI_F17_FALSE = NV_INFOFRAME_FIELD_VALUE_AVI_F17.NV_INFOFRAME_FIELD_VALUE_AVI_F17_FALSE
NV_INFOFRAME_FIELD_VALUE_AVI_F17_TRUE = NV_INFOFRAME_FIELD_VALUE_AVI_F17.NV_INFOFRAME_FIELD_VALUE_AVI_F17_TRUE
NV_INFOFRAME_FIELD_VALUE_AVI_F17_AUTO = NV_INFOFRAME_FIELD_VALUE_AVI_F17.NV_INFOFRAME_FIELD_VALUE_AVI_F17_AUTO


# not Byte2 related
class NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_NO_AFD = 0
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE01 = 1
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE02 = 2
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE03 = 3
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_LETTERBOX_GT16x9 = (
        4
    )
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE05 = 5
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE06 = 6
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE07 = 7
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_EQUAL_CODEDFRAME = (
        8
    )
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_CENTER_4x3 = 9
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_CENTER_16x9 = 10
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_CENTER_14x9 = 11
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE12 = 12
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_4x3_ON_14x9 = 13
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_16x9_ON_14x9 = 14
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_16x9_ON_4x3 = 15
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_AUTO = 31


NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_NO_AFD = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_NO_AFD
NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE01 = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE01
NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE02 = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE02
NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE03 = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE03
NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_LETTERBOX_GT16x9 = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_LETTERBOX_GT16x9
NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE05 = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE05
NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE06 = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE06
NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE07 = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE07
NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_EQUAL_CODEDFRAME = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_EQUAL_CODEDFRAME
NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_CENTER_4x3 = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_CENTER_4x3
NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_CENTER_16x9 = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_CENTER_16x9
NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_CENTER_14x9 = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_CENTER_14x9
NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE12 = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_RESERVE12
NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_4x3_ON_14x9 = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_4x3_ON_14x9
NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_16x9_ON_14x9 = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_16x9_ON_14x9
NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_16x9_ON_4x3 = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_16x9_ON_4x3
NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_AUTO = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOACTIVEPORTION_AUTO


class NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME_NO_DATA = 0
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME_4x3 = 1
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME_16x9 = 2
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME_FUTURE = 3
    NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME_AUTO = 7


NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME_NO_DATA = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME_NO_DATA
NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME_4x3 = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME_4x3
NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME_16x9 = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME_16x9
NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME_FUTURE = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME_FUTURE
NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME_AUTO = NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME.NV_INFOFRAME_FIELD_VALUE_AVI_ASPECTRATIOCODEDFRAME_AUTO


class NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY_NO_DATA = 0
    NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY_SMPTE_170M = 1
    NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY_ITUR_BT709 = 2
    NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY_USE_EXTENDED_COLORIMETRY = 3
    NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY_AUTO = 7


NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY_NO_DATA = NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY.NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY_NO_DATA
NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY_SMPTE_170M = NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY.NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY_SMPTE_170M
NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY_ITUR_BT709 = NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY.NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY_ITUR_BT709
NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY_USE_EXTENDED_COLORIMETRY = NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY.NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY_USE_EXTENDED_COLORIMETRY
NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY_AUTO = NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY.NV_INFOFRAME_FIELD_VALUE_AVI_COLORIMETRY_AUTO


# not Byte 3 related
class NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING_NO_DATA = 0
    NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING_HORIZONTAL = 1
    NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING_VERTICAL = 2
    NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING_BOTH = 3
    NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING_AUTO = 7


NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING_NO_DATA = NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING.NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING_NO_DATA
NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING_HORIZONTAL = NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING.NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING_HORIZONTAL
NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING_VERTICAL = NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING.NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING_VERTICAL
NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING_BOTH = NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING.NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING_BOTH
NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING_AUTO = NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING.NV_INFOFRAME_FIELD_VALUE_AVI_NONUNIFORMPICTURESCALING_AUTO


class NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION_DEFAULT = 0
    NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION_LIMITED_RANGE = 1
    NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION_FULL_RANGE = 2
    NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION_RESERVED = 3
    NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION_AUTO = 7


NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION_DEFAULT = NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION.NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION_DEFAULT
NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION_LIMITED_RANGE = NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION.NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION_LIMITED_RANGE
NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION_FULL_RANGE = NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION.NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION_FULL_RANGE
NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION_RESERVED = NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION.NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION_RESERVED
NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION_AUTO = NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION.NV_INFOFRAME_FIELD_VALUE_AVI_RGBQUANTIZATION_AUTO


class NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_XVYCC601 = 0
    NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_XVYCC709 = 1
    NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_SYCC601 = 2
    NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_ADOBEYCC601 = 3
    NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_ADOBERGB = 4
    NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_RESERVED05 = 5
    NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_RESERVED06 = 6
    NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_RESERVED07 = 7
    NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_AUTO = 15


NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_XVYCC601 = NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY.NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_XVYCC601
NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_XVYCC709 = NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY.NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_XVYCC709
NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_SYCC601 = NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY.NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_SYCC601
NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_ADOBEYCC601 = NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY.NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_ADOBEYCC601
NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_ADOBERGB = NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY.NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_ADOBERGB
NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_RESERVED05 = NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY.NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_RESERVED05
NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_RESERVED06 = NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY.NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_RESERVED06
NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_RESERVED07 = NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY.NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_RESERVED07
NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_AUTO = NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY.NV_INFOFRAME_FIELD_VALUE_AVI_EXTENDEDCOLORIMETRY_AUTO


class NV_INFOFRAME_FIELD_VALUE_AVI_ITC(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AVI_ITC_VIDEO_CONTENT = 0
    NV_INFOFRAME_FIELD_VALUE_AVI_ITC_ITCONTENT = 1
    NV_INFOFRAME_FIELD_VALUE_AVI_ITC_AUTO = 3


NV_INFOFRAME_FIELD_VALUE_AVI_ITC_VIDEO_CONTENT = NV_INFOFRAME_FIELD_VALUE_AVI_ITC.NV_INFOFRAME_FIELD_VALUE_AVI_ITC_VIDEO_CONTENT
NV_INFOFRAME_FIELD_VALUE_AVI_ITC_ITCONTENT = NV_INFOFRAME_FIELD_VALUE_AVI_ITC.NV_INFOFRAME_FIELD_VALUE_AVI_ITC_ITCONTENT
NV_INFOFRAME_FIELD_VALUE_AVI_ITC_AUTO = NV_INFOFRAME_FIELD_VALUE_AVI_ITC.NV_INFOFRAME_FIELD_VALUE_AVI_ITC_AUTO


# not Byte 4 related
class NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_NONE = 0
    NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X02 = 1
    NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X03 = 2
    NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X04 = 3
    NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X05 = 4
    NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X06 = 5
    NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X07 = 6
    NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X08 = 7
    NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X09 = 8
    NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X10 = 9
    NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_RESERVED10 = 10
    NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_RESERVED11 = 11
    NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_RESERVED12 = 12
    NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_RESERVED13 = 13
    NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_RESERVED14 = 14
    NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_RESERVED15 = 15
    NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_AUTO = 31


NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_NONE = NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION.NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_NONE
NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X02 = NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION.NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X02
NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X03 = NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION.NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X03
NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X04 = NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION.NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X04
NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X05 = NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION.NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X05
NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X06 = NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION.NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X06
NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X07 = NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION.NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X07
NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X08 = NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION.NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X08
NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X09 = NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION.NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X09
NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X10 = NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION.NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_X10
NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_RESERVED10 = NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION.NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_RESERVED10
NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_RESERVED11 = NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION.NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_RESERVED11
NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_RESERVED12 = NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION.NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_RESERVED12
NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_RESERVED13 = NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION.NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_RESERVED13
NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_RESERVED14 = NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION.NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_RESERVED14
NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_RESERVED15 = NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION.NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_RESERVED15
NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_AUTO = NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION.NV_INFOFRAME_FIELD_VALUE_AVI_PIXELREPETITION_AUTO


class NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE_GRAPHICS = 0
    NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE_PHOTO = 1
    NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE_CINEMA = 2
    NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE_GAME = 3
    NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE_AUTO = 7


NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE_GRAPHICS = NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE.NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE_GRAPHICS
NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE_PHOTO = NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE.NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE_PHOTO
NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE_CINEMA = NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE.NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE_CINEMA
NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE_GAME = NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE.NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE_GAME
NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE_AUTO = NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE.NV_INFOFRAME_FIELD_VALUE_AVI_CONTENTTYPE_AUTO


class NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION_LIMITED_RANGE = 0
    NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION_FULL_RANGE = 1
    NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION_RESERVED02 = 2
    NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION_RESERVED03 = 3
    NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION_AUTO = 7


NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION_LIMITED_RANGE = NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION.NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION_LIMITED_RANGE
NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION_FULL_RANGE = NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION.NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION_FULL_RANGE
NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION_RESERVED02 = NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION.NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION_RESERVED02
NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION_RESERVED03 = NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION.NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION_RESERVED03
NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION_AUTO = NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION.NV_INFOFRAME_FIELD_VALUE_AVI_YCCQUANTIZATION_AUTO

# not Adding an Auto bit to each field
NV_INFOFRAME_VIDEO._fields_ = [
    ('vic', NvU32, 8),
    ('pixelRepeat', NvU32, 5),
    ('colorSpace', NvU32, 3),
    ('colorimetry', NvU32, 3),
    ('extendedColorimetry', NvU32, 4),
    ('rgbQuantizationRange', NvU32, 3),
    ('yccQuantizationRange', NvU32, 3),
    ('itContent', NvU32, 2),
    ('contentTypes', NvU32, 3),
    ('scanInfo', NvU32, 3),
    ('activeFormatInfoPresent', NvU32, 2),
    ('activeFormatAspectRatio', NvU32, 5),
    ('picAspectRatio', NvU32, 3),
    ('nonuniformScaling', NvU32, 3),
    ('barInfo', NvU32, 3),
    ('top_bar', NvU32, 17),
    ('bottom_bar', NvU32, 17),
    ('left_bar', NvU32, 17),
    ('right_bar', NvU32, 17),
    ('Future17', NvU32, 2),
    ('Future47', NvU32, 2),
]


# not Byte 1 related
class NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_IN_HEADER = 0
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_2 = 1
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_3 = 2
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_4 = 3
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_5 = 4
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_6 = 5
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_7 = 6
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_8 = 7
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_AUTO = 15


NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_IN_HEADER = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_IN_HEADER
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_2 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_2
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_3 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_3
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_4 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_4
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_5 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_5
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_6 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_6
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_7 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_7
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_8 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_8
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_AUTO = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELCOUNT_AUTO


class NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_IN_HEADER = 0
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_PCM = 1
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_AC3 = 2
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_MPEG1 = 3
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_MP3 = 4
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_MPEG2 = 5
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_AACLC = 6
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_DTS = 7
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_ATRAC = 8
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_DSD = 9
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_EAC3 = 10
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_DTSHD = 11
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_MLP = 12
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_DST = 13
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_WMAPRO = 14
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_USE_CODING_EXTENSION_TYPE = (
        15
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_AUTO = 31


NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_IN_HEADER = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_IN_HEADER
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_PCM = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_PCM
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_AC3 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_AC3
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_MPEG1 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_MPEG1
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_MP3 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_MP3
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_MPEG2 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_MPEG2
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_AACLC = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_AACLC
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_DTS = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_DTS
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_ATRAC = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_ATRAC
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_DSD = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_DSD
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_EAC3 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_EAC3
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_DTSHD = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_DTSHD
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_MLP = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_MLP
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_DST = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_DST
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_WMAPRO = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_WMAPRO
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_USE_CODING_EXTENSION_TYPE = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_USE_CODING_EXTENSION_TYPE
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_AUTO = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGTYPE_AUTO


# not Byte 2 related
class NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE_IN_HEADER = 0
    NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE_16BITS = 1
    NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE_20BITS = 2
    NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE_24BITS = 3
    NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE_AUTO = 7


NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE_IN_HEADER = NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE.NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE_IN_HEADER
NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE_16BITS = NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE.NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE_16BITS
NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE_20BITS = NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE.NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE_20BITS
NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE_24BITS = NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE.NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE_24BITS
NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE_AUTO = NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE.NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLESIZE_AUTO


class NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_IN_HEADER = 0
    NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_32000HZ = 1
    NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_44100HZ = 2
    NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_48000HZ = 3
    NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_88200KHZ = 4
    NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_96000KHZ = 5
    NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_176400KHZ = 6
    NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_192000KHZ = 7
    NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_AUTO = 15


NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_IN_HEADER = NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY.NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_IN_HEADER
NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_32000HZ = NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY.NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_32000HZ
NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_44100HZ = NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY.NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_44100HZ
NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_48000HZ = NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY.NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_48000HZ
NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_88200KHZ = NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY.NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_88200KHZ
NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_96000KHZ = NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY.NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_96000KHZ
NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_176400KHZ = NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY.NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_176400KHZ
NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_192000KHZ = NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY.NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_192000KHZ
NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_AUTO = NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY.NV_INFOFRAME_FIELD_VALUE_AUDIO_SAMPLEFREQUENCY_AUTO


# not Byte 3 related
class NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_USE_CODING_TYPE = 0
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_HEAAC = 1
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_HEAACV2 = 2
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_MPEGSURROUND = 3
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE04 = 4
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE05 = 5
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE06 = 6
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE07 = 7
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE08 = 8
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE09 = 9
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE10 = 10
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE11 = 11
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE12 = 12
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE13 = 13
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE14 = 14
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE15 = 15
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE16 = 16
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE17 = 17
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE18 = 18
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE19 = 19
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE20 = 20
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE21 = 21
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE22 = 22
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE23 = 23
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE24 = 24
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE25 = 25
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE26 = 26
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE27 = 27
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE28 = 28
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE29 = 29
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE30 = 30
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE31 = 31
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_AUTO = 63


NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_USE_CODING_TYPE = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_USE_CODING_TYPE
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_HEAAC = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_HEAAC
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_HEAACV2 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_HEAACV2
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_MPEGSURROUND = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_MPEGSURROUND
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE04 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE04
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE05 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE05
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE06 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE06
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE07 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE07
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE08 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE08
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE09 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE09
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE10 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE10
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE11 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE11
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE12 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE12
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE13 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE13
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE14 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE14
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE15 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE15
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE16 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE16
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE17 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE17
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE18 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE18
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE19 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE19
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE20 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE20
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE21 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE21
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE22 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE22
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE23 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE23
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE24 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE24
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE25 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE25
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE26 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE26
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE27 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE27
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE28 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE28
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE29 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE29
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE30 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE30
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE31 = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_RESERVE31
NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_AUTO = NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE.NV_INFOFRAME_FIELD_VALUE_AUDIO_CODINGEXTENSIONTYPE_AUTO


# not Byte 4 related
class NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_X_X_X_FR_FL = 0
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_X_X_LFE_FR_FL = (
        1
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_X_FC_X_FR_FL = 2
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_X_FC_LFE_FR_FL = (
        3
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_RC_X_X_FR_FL = 4
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_RC_X_LFE_FR_FL = (
        5
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_RC_FC_X_FR_FL = (
        6
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_RC_FC_LFE_FR_FL = (
        7
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_RR_RL_X_X_FR_FL = (
        8
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_RR_RL_X_LFE_FR_FL = (
        9
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_RR_RL_FC_X_FR_FL = (
        10
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_RR_RL_FC_LFE_FR_FL = (
        11
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_RC_RR_RL_X_X_FR_FL = (
        12
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_RC_RR_RL_X_LFE_FR_FL = (
        13
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_RC_RR_RL_FC_X_FR_FL = (
        14
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_RC_RR_RL_FC_LFE_FR_FL = (
        15
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_RRC_RLC_RR_RL_X_X_FR_FL = (
        16
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_RRC_RLC_RR_RL_X_LFE_FR_FL = (
        17
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_RRC_RLC_RR_RL_FC_X_FR_FL = (
        18
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_RRC_RLC_RR_RL_FC_LFE_FR_FL = (
        19
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_X_X_X_FR_FL = (
        20
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_X_X_LFE_FR_FL = (
        21
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_X_FC_X_FR_FL = (
        22
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_X_FC_LFE_FR_FL = (
        23
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_RC_X_X_FR_FL = (
        24
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_RC_X_LFE_FR_FL = (
        25
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_RC_FC_X_FR_FL = (
        26
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_RC_FC_LFE_FR_FL = (
        27
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_RR_RL_X_X_FR_FL = (
        28
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_RR_RL_X_LFE_FR_FL = (
        29
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_RR_RL_FC_X_FR_FL = (
        30
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_RR_RL_FC_LFE_FR_FL = (
        31
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_FCH_RR_RL_FC_X_FR_FL = (
        32
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_FCH_RR_RL_FC_LFE_FR_FL = (
        33
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_TC_X_RR_RL_FC_X_FR_FL = (
        34
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_TC_X_RR_RL_FC_LFE_FR_FL = (
        35
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRH_FLH_RR_RL_X_X_FR_FL = (
        36
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRH_FLH_RR_RL_X_LFE_FR_FL = (
        37
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRW_FLW_RR_RL_X_X_FR_FL = (
        38
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRW_FLW_RR_RL_X_LFE_FR_FL = (
        39
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_TC_RC_RR_RL_FC_X_FR_FL = (
        40
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_TC_RC_RR_RL_FC_LFE_FR_FL = (
        41
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FCH_RC_RR_RL_FC_X_FR_FL = (
        42
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FCH_RC_RR_RL_FC_LFE_FR_FL = (
        43
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_TC_FCH_RR_RL_FC_X_FR_FL = (
        44
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_TC_FCH_RR_RL_FC_LFE_FR_FL = (
        45
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRH_FLH_RR_RL_FC_X_FR_FL = (
        46
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRH_FLH_RR_RL_FC_LFE_FR_FL = (
        47
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRW_FLW_RR_RL_FC_X_FR_FL = (
        48
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRW_FLW_RR_RL_FC_LFE_FR_FL = (
        0x31
    )
    NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_AUTO = 0x1FF


NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_X_X_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_X_X_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_X_X_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_X_X_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_X_FC_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_X_FC_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_X_FC_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_X_FC_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_RC_X_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_RC_X_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_RC_X_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_RC_X_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_RC_FC_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_RC_FC_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_RC_FC_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_X_RC_FC_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_RR_RL_X_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_RR_RL_X_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_RR_RL_X_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_RR_RL_X_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_RR_RL_FC_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_RR_RL_FC_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_RR_RL_FC_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_X_RR_RL_FC_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_RC_RR_RL_X_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_RC_RR_RL_X_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_RC_RR_RL_X_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_RC_RR_RL_X_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_RC_RR_RL_FC_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_RC_RR_RL_FC_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_RC_RR_RL_FC_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_RC_RR_RL_FC_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_RRC_RLC_RR_RL_X_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_RRC_RLC_RR_RL_X_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_RRC_RLC_RR_RL_X_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_RRC_RLC_RR_RL_X_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_RRC_RLC_RR_RL_FC_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_RRC_RLC_RR_RL_FC_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_RRC_RLC_RR_RL_FC_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_RRC_RLC_RR_RL_FC_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_X_X_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_X_X_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_X_X_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_X_X_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_X_FC_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_X_FC_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_X_FC_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_X_FC_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_RC_X_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_RC_X_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_RC_X_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_RC_X_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_RC_FC_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_RC_FC_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_RC_FC_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_X_RC_FC_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_RR_RL_X_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_RR_RL_X_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_RR_RL_X_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_RR_RL_X_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_RR_RL_FC_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_RR_RL_FC_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_RR_RL_FC_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRC_FLC_RR_RL_FC_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_FCH_RR_RL_FC_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_FCH_RR_RL_FC_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_FCH_RR_RL_FC_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_X_FCH_RR_RL_FC_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_TC_X_RR_RL_FC_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_TC_X_RR_RL_FC_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_TC_X_RR_RL_FC_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_TC_X_RR_RL_FC_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRH_FLH_RR_RL_X_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRH_FLH_RR_RL_X_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRH_FLH_RR_RL_X_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRH_FLH_RR_RL_X_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRW_FLW_RR_RL_X_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRW_FLW_RR_RL_X_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRW_FLW_RR_RL_X_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRW_FLW_RR_RL_X_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_TC_RC_RR_RL_FC_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_TC_RC_RR_RL_FC_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_TC_RC_RR_RL_FC_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_TC_RC_RR_RL_FC_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FCH_RC_RR_RL_FC_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FCH_RC_RR_RL_FC_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FCH_RC_RR_RL_FC_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FCH_RC_RR_RL_FC_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_TC_FCH_RR_RL_FC_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_TC_FCH_RR_RL_FC_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_TC_FCH_RR_RL_FC_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_TC_FCH_RR_RL_FC_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRH_FLH_RR_RL_FC_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRH_FLH_RR_RL_FC_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRH_FLH_RR_RL_FC_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRH_FLH_RR_RL_FC_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRW_FLW_RR_RL_FC_X_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRW_FLW_RR_RL_FC_X_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRW_FLW_RR_RL_FC_LFE_FR_FL = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_FRW_FLW_RR_RL_FC_LFE_FR_FL
NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_AUTO = NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION.NV_INFOFRAME_FIELD_VALUE_AUDIO_CHANNELALLOCATION_AUTO


# not Byte 5 related
class NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL_NO_DATA = 0
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL_0DB = 1
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL_PLUS10DB = 2
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL_RESERVED03 = 3
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL_AUTO = 7


NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL_NO_DATA = NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL.NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL_NO_DATA
NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL_0DB = NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL.NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL_0DB
NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL_PLUS10DB = NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL.NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL_PLUS10DB
NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL_RESERVED03 = NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL.NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL_RESERVED03
NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL_AUTO = NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL.NV_INFOFRAME_FIELD_VALUE_AUDIO_LFEPLAYBACKLEVEL_AUTO


class NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_0DB = 0
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_1DB = 1
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_2DB = 2
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_3DB = 3
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_4DB = 4
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_5DB = 5
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_6DB = 6
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_7DB = 7
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_8DB = 8
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_9DB = 9
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_10DB = 10
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_11DB = 11
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_12DB = 12
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_13DB = 13
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_14DB = 14
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_15DB = 15
    NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_AUTO = 31


NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_0DB = NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES.NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_0DB
NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_1DB = NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES.NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_1DB
NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_2DB = NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES.NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_2DB
NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_3DB = NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES.NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_3DB
NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_4DB = NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES.NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_4DB
NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_5DB = NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES.NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_5DB
NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_6DB = NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES.NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_6DB
NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_7DB = NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES.NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_7DB
NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_8DB = NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES.NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_8DB
NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_9DB = NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES.NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_9DB
NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_10DB = NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES.NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_10DB
NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_11DB = NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES.NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_11DB
NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_12DB = NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES.NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_12DB
NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_13DB = NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES.NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_13DB
NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_14DB = NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES.NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_14DB
NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_15DB = NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES.NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_15DB
NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_AUTO = NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES.NV_INFOFRAME_FIELD_VALUE_AUDIO_LEVELSHIFTVALUES_AUTO


class NV_INFOFRAME_FIELD_VALUE_AUDIO_DOWNMIX(ENUM):
    NV_INFOFRAME_FIELD_VALUE_AUDIO_DOWNMIX_PERMITTED = 0
    NV_INFOFRAME_FIELD_VALUE_AUDIO_DOWNMIX_PROHIBITED = 1
    NV_INFOFRAME_FIELD_VALUE_AUDIO_DOWNMIX_AUTO = 3


NV_INFOFRAME_FIELD_VALUE_AUDIO_DOWNMIX_PERMITTED = NV_INFOFRAME_FIELD_VALUE_AUDIO_DOWNMIX.NV_INFOFRAME_FIELD_VALUE_AUDIO_DOWNMIX_PERMITTED
NV_INFOFRAME_FIELD_VALUE_AUDIO_DOWNMIX_PROHIBITED = NV_INFOFRAME_FIELD_VALUE_AUDIO_DOWNMIX.NV_INFOFRAME_FIELD_VALUE_AUDIO_DOWNMIX_PROHIBITED
NV_INFOFRAME_FIELD_VALUE_AUDIO_DOWNMIX_AUTO = NV_INFOFRAME_FIELD_VALUE_AUDIO_DOWNMIX.NV_INFOFRAME_FIELD_VALUE_AUDIO_DOWNMIX_AUTO

NV_INFOFRAME_AUDIO._fields_ = [
    ('codingType', NvU32, 5),
    ('codingExtensionType', NvU32, 6),
    ('sampleSize', NvU32, 3),
    ('sampleRate', NvU32, 4),
    ('channelCount', NvU32, 4),
    ('speakerPlacement', NvU32, 9),
    ('downmixInhibit', NvU32, 2),
    ('lfePlaybackLevel', NvU32, 3),
    ('levelShift', NvU32, 5),
    ('Future12', NvU32, 2),
    ('Future2x', NvU32, 4),
    ('Future3x', NvU32, 4),
    ('Future52', NvU32, 2),
    ('Future6', NvU32, 9),
    ('Future7', NvU32, 9),
    ('Future8', NvU32, 9),
    ('Future9', NvU32, 9),
    ('Future10', NvU32, 9),
]


class infoframe(ctypes.Union):
    pass


infoframe._fields_ = [
    # not < This is NVIDIA-specific and corresponds to the property cmds
    # and associated infoframe.
    ('property', NV_INFOFRAME_PROPERTY),
    ('audio', NV_INFOFRAME_AUDIO),
    ('video', NV_INFOFRAME_VIDEO),
]
NV_INFOFRAME_DATA.infoframe = infoframe

NV_INFOFRAME_DATA._fields_ = [
    # not < version of this structure
    ('version', NvU32),
    # not < size of this structure
    ('size', NvU16),
    # not < The actions to perform from NV_INFOFRAME_CMD
    ('cmd', NvU8),
    # not < type of infoframe
    ('type', NvU8),
    ('infoframe', NV_INFOFRAME_DATA.infoframe),
]

# not Macro for constructing the version field of ::NV_INFOFRAME_DATA
NV_INFOFRAME_DATA_VER = MAKE_NVAPI_VERSION(NV_INFOFRAME_DATA, 1)

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Disp_InfoFrameControl
# not DESCRIPTION:  This API controls the InfoFrame values.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  displayId  Monitor Identifier
# not \param [in,out] pInfoframeData Contains data corresponding to
# InfoFrame
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not   specific meaning for this API, they are listed below.
# not
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_Disp_InfoFrameControl = hDll.Disp_InfoFrameControl
NvAPI_Disp_InfoFrameControl.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_Disp_InfoFrameControl(__in NvU32 displayId, __inout NV_INFOFRAME_DATA *pInfoframeData);


# not \ingroup dispcontrol
# not @{
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Disp_ColorControl
# not \fn
# NvAPI_Disp_ColorControl(NvU32 displayId, NV_COLOR_DATA *pColorData)
# not DESCRIPTION: This API controls the Color values.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  displayId  Monitor Identifier
# not \param [in,out] pColorData  Contains data corresponding to color
# information
# not
# not \return RETURN STATUS:
# not ::NVAPI_OK,
# not ::NVAPI_ERROR,
# not ::NVAPI_INVALID_ARGUMENT
# ///////////////////////////////////////////////////////////////////////
class NV_COLOR_CMD(ENUM):
    NV_COLOR_CMD_GET = 1
    NV_COLOR_CMD_SET = 2
    NV_COLOR_CMD_IS_SUPPORTED_COLOR = 3
    NV_COLOR_CMD_GET_DEFAULT = 4


NV_COLOR_CMD_GET = NV_COLOR_CMD.NV_COLOR_CMD_GET
NV_COLOR_CMD_SET = NV_COLOR_CMD.NV_COLOR_CMD_SET
NV_COLOR_CMD_IS_SUPPORTED_COLOR = NV_COLOR_CMD.NV_COLOR_CMD_IS_SUPPORTED_COLOR
NV_COLOR_CMD_GET_DEFAULT = NV_COLOR_CMD.NV_COLOR_CMD_GET_DEFAULT


# not See Table 14 of CEA-861E. Not all of this is supported by the GPU.
class NV_COLOR_FORMAT(ENUM):
    NV_COLOR_FORMAT_RGB = 0
    NV_COLOR_FORMAT_YUV422 = 1
    NV_COLOR_FORMAT_YUV444 = 2
    NV_COLOR_FORMAT_YUV420 = 3
    NV_COLOR_FORMAT_DEFAULT = 0xFE
    NV_COLOR_FORMAT_AUTO = 0xFF


NV_COLOR_FORMAT_RGB = NV_COLOR_FORMAT.NV_COLOR_FORMAT_RGB
NV_COLOR_FORMAT_YUV422 = NV_COLOR_FORMAT.NV_COLOR_FORMAT_YUV422
NV_COLOR_FORMAT_YUV444 = NV_COLOR_FORMAT.NV_COLOR_FORMAT_YUV444
NV_COLOR_FORMAT_YUV420 = NV_COLOR_FORMAT.NV_COLOR_FORMAT_YUV420
NV_COLOR_FORMAT_DEFAULT = NV_COLOR_FORMAT.NV_COLOR_FORMAT_DEFAULT
NV_COLOR_FORMAT_AUTO = NV_COLOR_FORMAT.NV_COLOR_FORMAT_AUTO


class NV_COLOR_COLORIMETRY(ENUM):
    NV_COLOR_COLORIMETRY_RGB = 0
    NV_COLOR_COLORIMETRY_YCC601 = 1
    NV_COLOR_COLORIMETRY_YCC709 = 2
    NV_COLOR_COLORIMETRY_XVYCC601 = 3
    NV_COLOR_COLORIMETRY_XVYCC709 = 4
    NV_COLOR_COLORIMETRY_SYCC601 = 5
    NV_COLOR_COLORIMETRY_ADOBEYCC601 = 6
    NV_COLOR_COLORIMETRY_ADOBERGB = 7
    NV_COLOR_COLORIMETRY_BT2020RGB = 8
    NV_COLOR_COLORIMETRY_BT2020YCC = 9
    NV_COLOR_COLORIMETRY_BT2020cYCC = 10
    NV_COLOR_COLORIMETRY_DEFAULT = 0xFE
    NV_COLOR_COLORIMETRY_AUTO = 0xFF


NV_COLOR_COLORIMETRY_RGB = NV_COLOR_COLORIMETRY.NV_COLOR_COLORIMETRY_RGB
NV_COLOR_COLORIMETRY_YCC601 = NV_COLOR_COLORIMETRY.NV_COLOR_COLORIMETRY_YCC601
NV_COLOR_COLORIMETRY_YCC709 = NV_COLOR_COLORIMETRY.NV_COLOR_COLORIMETRY_YCC709
NV_COLOR_COLORIMETRY_XVYCC601 = NV_COLOR_COLORIMETRY.NV_COLOR_COLORIMETRY_XVYCC601
NV_COLOR_COLORIMETRY_XVYCC709 = NV_COLOR_COLORIMETRY.NV_COLOR_COLORIMETRY_XVYCC709
NV_COLOR_COLORIMETRY_SYCC601 = NV_COLOR_COLORIMETRY.NV_COLOR_COLORIMETRY_SYCC601
NV_COLOR_COLORIMETRY_ADOBEYCC601 = NV_COLOR_COLORIMETRY.NV_COLOR_COLORIMETRY_ADOBEYCC601
NV_COLOR_COLORIMETRY_ADOBERGB = NV_COLOR_COLORIMETRY.NV_COLOR_COLORIMETRY_ADOBERGB
NV_COLOR_COLORIMETRY_BT2020RGB = NV_COLOR_COLORIMETRY.NV_COLOR_COLORIMETRY_BT2020RGB
NV_COLOR_COLORIMETRY_BT2020YCC = NV_COLOR_COLORIMETRY.NV_COLOR_COLORIMETRY_BT2020YCC
NV_COLOR_COLORIMETRY_BT2020cYCC = NV_COLOR_COLORIMETRY.NV_COLOR_COLORIMETRY_BT2020cYCC
NV_COLOR_COLORIMETRY_DEFAULT = NV_COLOR_COLORIMETRY.NV_COLOR_COLORIMETRY_DEFAULT
NV_COLOR_COLORIMETRY_AUTO = NV_COLOR_COLORIMETRY.NV_COLOR_COLORIMETRY_AUTO


class _NV_DYNAMIC_RANGE(ENUM):
    NV_DYNAMIC_RANGE_VESA = 0x0
    NV_DYNAMIC_RANGE_CEA = 0x1
    NV_DYNAMIC_RANGE_AUTO = 0xFF


NV_DYNAMIC_RANGE = _NV_DYNAMIC_RANGE


class _NV_BPC(ENUM):
    NV_BPC_DEFAULT = 0
    NV_BPC_6 = 1
    NV_BPC_8 = 2
    NV_BPC_10 = 3
    NV_BPC_12 = 4
    NV_BPC_16 = 5


NV_BPC = _NV_BPC


class _NV_COLOR_SELECTION_POLICY(ENUM):
    NV_COLOR_SELECTION_POLICY_USER = 0
    NV_COLOR_SELECTION_POLICY_BEST_QUALITY = 1
    NV_COLOR_SELECTION_POLICY_DEFAULT = (
        NV_COLOR_SELECTION_POLICY_BEST_QUALITY
    )
    NV_COLOR_SELECTION_POLICY_UNKNOWN = 0xFF


NV_COLOR_SELECTION_POLICY = _NV_COLOR_SELECTION_POLICY


class _NV_DESKTOP_COLOR_DEPTH(ENUM):
    NV_DESKTOP_COLOR_DEPTH_DEFAULT = 0x0
    NV_DESKTOP_COLOR_DEPTH_8BPC = 0x1
    NV_DESKTOP_COLOR_DEPTH_10BPC = 0x2
    NV_DESKTOP_COLOR_DEPTH_16BPC_FLOAT = 0x3

    # 16 bit FLOAT per color component (16 bit FLOAT alpha) wide color
    # gamut
    NV_DESKTOP_COLOR_DEPTH_16BPC_FLOAT_WCG = 0x4
    NV_DESKTOP_COLOR_DEPTH_16BPC_FLOAT_HDR = 0x5
    NV_DESKTOP_COLOR_DEPTH_MAX_VALUE = (
        NV_DESKTOP_COLOR_DEPTH_16BPC_FLOAT_HDR
    )


NV_DESKTOP_COLOR_DEPTH = _NV_DESKTOP_COLOR_DEPTH


class data(ctypes.Structure):
    pass


data._fields_ = [
    # not < One of NV_COLOR_FORMAT enum values.
    ('colorFormat', NvU8),
    # not < One of NV_COLOR_COLORIMETRY enum values.
    ('colorimetry', NvU8),
]
_NV_COLOR_DATA_V1.data = data

_NV_COLOR_DATA_V1._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < Size of this structure
    ('size', NvU16),
    ('cmd', NvU8),
    ('data', _NV_COLOR_DATA_V1.data),
]


class data(ctypes.Structure):
    pass


data._fields_ = [
    # not < One of NV_COLOR_FORMAT enum values.
    ('colorFormat', NvU8),
    # not < One of NV_COLOR_COLORIMETRY enum values.
    ('colorimetry', NvU8),
    # not < One of NV_DYNAMIC_RANGE enum values.
    ('dynamicRange', NvU8),
]
_NV_COLOR_DATA_V2.data = data

_NV_COLOR_DATA_V2._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < Size of this structure
    ('size', NvU16),
    ('cmd', NvU8),
    ('data', _NV_COLOR_DATA_V2.data),
]


class data(ctypes.Structure):
    pass


data._fields_ = [
    # not < One of NV_COLOR_FORMAT enum values.
    ('colorFormat', NvU8),
    # not < One of NV_COLOR_COLORIMETRY enum values.
    ('colorimetry', NvU8),
    # not < One of NV_DYNAMIC_RANGE enum values.
    ('dynamicRange', NvU8),
    # not < One of NV_BPC enum values.
    ('bpc', NV_BPC),
]
_NV_COLOR_DATA_V3.data = data

_NV_COLOR_DATA_V3._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < Size of this structure
    ('size', NvU16),
    ('cmd', NvU8),
    ('data', _NV_COLOR_DATA_V3.data),
]


class data(ctypes.Structure):
    pass


data._fields_ = [
    # not < One of NV_COLOR_FORMAT enum values.
    ('colorFormat', NvU8),
    # not < One of NV_COLOR_COLORIMETRY enum values.
    ('colorimetry', NvU8),
    # not < One of NV_DYNAMIC_RANGE enum values.
    ('dynamicRange', NvU8),
    # not < One of NV_BPC enum values.
    ('bpc', NV_BPC),
    # not < One of the color selection policy
    ('colorSelectionPolicy', NV_COLOR_SELECTION_POLICY),
]
_NV_COLOR_DATA_V4.data = data

_NV_COLOR_DATA_V4._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < Size of this structure
    ('size', NvU16),
    ('cmd', NvU8),
    ('data', _NV_COLOR_DATA_V4.data),
]


class data(ctypes.Structure):
    pass


data._fields_ = [
    # not < One of NV_COLOR_FORMAT enum values.
    ('colorFormat', NvU8),
    # not < One of NV_COLOR_COLORIMETRY enum values.
    ('colorimetry', NvU8),
    # not < One of NV_DYNAMIC_RANGE enum values.
    ('dynamicRange', NvU8),
    # not < One of NV_BPC enum values.
    ('bpc', NV_BPC),
    # not < One of the color selection policy
    ('colorSelectionPolicy', NV_COLOR_SELECTION_POLICY),
    # not < One of NV_DESKTOP_COLOR_DEPTH enum values.
    ('depth', NV_DESKTOP_COLOR_DEPTH),
]
_NV_COLOR_DATA_V5.data = data

_NV_COLOR_DATA_V5._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < Size of this structure
    ('size', NvU16),
    ('cmd', NvU8),
    ('data', _NV_COLOR_DATA_V5.data),
]

NV_COLOR_DATA = NV_COLOR_DATA_V5
NV_COLOR_DATA_VER1 = MAKE_NVAPI_VERSION(NV_COLOR_DATA_V1, 1)
NV_COLOR_DATA_VER2 = MAKE_NVAPI_VERSION(NV_COLOR_DATA_V2, 2)
NV_COLOR_DATA_VER3 = MAKE_NVAPI_VERSION(NV_COLOR_DATA_V3, 3)
NV_COLOR_DATA_VER4 = MAKE_NVAPI_VERSION(NV_COLOR_DATA_V4, 4)
NV_COLOR_DATA_VER5 = MAKE_NVAPI_VERSION(NV_COLOR_DATA_V5, 5)
NV_COLOR_DATA_VER = NV_COLOR_DATA_VER5

NvAPI_Disp_ColorControl = hDll.Disp_ColorControl
NvAPI_Disp_ColorControl.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_Disp_ColorControl(NvU32 displayId, NV_COLOR_DATA *pColorData);


# not @}
class NV_STATIC_METADATA_DESCRIPTOR_ID(ENUM):
    # not < Tells the type of structure used to define the Static Metadata
    # Descriptor block.
    NV_STATIC_METADATA_TYPE_1 = 0


NV_STATIC_METADATA_TYPE_1 = NV_STATIC_METADATA_DESCRIPTOR_ID.NV_STATIC_METADATA_TYPE_1


class display_data(ctypes.Structure):
    pass


display_data._fields_ = [
    # not < x coordinate of color primary 0 (e.g. Red) of the display
    # ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_x0', NvU16),
    # not < y coordinate of color primary 0 (e.g. Red) of the display
    # ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_y0', NvU16),
    # not < x coordinate of color primary 1 (e.g. Green) of the display
    # ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_x1', NvU16),
    # not < y coordinate of color primary 1 (e.g. Green) of the display
    # ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_y1', NvU16),
    # not < x coordinate of color primary 2 (e.g. Blue) of the display
    # ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_x2', NvU16),
    # not < y coordinate of color primary 2 (e.g. Blue) of the display
    # ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_y2', NvU16),
    # not < x coordinate of white point of the display
    # ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayWhitePoint_x', NvU16),
    # not < y coordinate of white point of the display
    # ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayWhitePoint_y', NvU16),
    # not < Maximum display luminance = desired max luminance of HDR
    # content ([0x0001-0xFFFF] = [1.0 - 65535.0] cd/m^2)
    ('desired_content_max_luminance', NvU16),
    # not < Minimum display luminance = desired min luminance of HDR
    # content ([0x0001-0xFFFF] = [1.0 - 6.55350] cd/m^2)
    ('desired_content_min_luminance', NvU16),
    # not < Desired maximum Frame-Average Light Level (MaxFALL) of HDR
    # content ([0x0001-0xFFFF] = [1.0 - 65535.0] cd/m^2)
    ('desired_content_max_frame_average_luminance', NvU16),
]
_NV_HDR_CAPABILITIES_V1.display_data = display_data

_NV_HDR_CAPABILITIES_V1._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < HDMI2.0a UHDA HDR with ST2084 EOTF (CEA861.3). Boolean: 0 =
    # not supported, 1 = supported;
    ('isST2084EotfSupported', NvU32, 1),
    # not < HDMI2.0a traditional HDR gamma (CEA861.3). Boolean: 0 = not
    # supported, 1 = supported;
    ('isTraditionalHdrGammaSupported', NvU32, 1),
    # not < Extended Dynamic Range on SDR displays. Boolean: 0 = not
    # supported, 1 = supported;
    ('isEdrSupported', NvU32, 1),
    # not < If set, driver will expand default (=zero) HDR capabilities
    # parameters contained in display's EDID.
    ('driverExpandDefaultHdrParameters', NvU32, 1),
    # not < HDMI2.0a traditional SDR gamma (CEA861.3). Boolean: 0 = not
    # supported, 1 = supported;
    ('isTraditionalSdrGammaSupported', NvU32, 1),
    ('reserved', NvU32, 27),
    # not < Static Metadata Descriptor Id (0 for static metadata type 1)
    ('static_metadata_descriptor_id', NV_STATIC_METADATA_DESCRIPTOR_ID),
    # not < Static Metadata Descriptor Type 1, CEA-861.3, SMPTE ST2086
    ('display_data', _NV_HDR_CAPABILITIES_V1.display_data),
]


class display_data(ctypes.Structure):
    pass


display_data._fields_ = [
    # not < x coordinate of color primary 0 (e.g. Red) of the display
    # ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_x0', NvU16),
    # not < y coordinate of color primary 0 (e.g. Red) of the display
    # ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_y0', NvU16),
    # not < x coordinate of color primary 1 (e.g. Green) of the display
    # ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_x1', NvU16),
    # not < y coordinate of color primary 1 (e.g. Green) of the display
    # ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_y1', NvU16),
    # not < x coordinate of color primary 2 (e.g. Blue) of the display
    # ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_x2', NvU16),
    # not < y coordinate of color primary 2 (e.g. Blue) of the display
    # ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_y2', NvU16),
    # not < x coordinate of white point of the display
    # ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayWhitePoint_x', NvU16),
    # not < y coordinate of white point of the display
    # ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayWhitePoint_y', NvU16),
    # not < Maximum display luminance = desired max luminance of HDR
    # content ([0x0001-0xFFFF] = [1.0 - 65535.0] cd/m^2)
    ('desired_content_max_luminance', NvU16),
    # not < Minimum display luminance = desired min luminance of HDR
    # content ([0x0001-0xFFFF] = [1.0 - 6.55350] cd/m^2)
    ('desired_content_min_luminance', NvU16),
    # not < Desired maximum Frame-Average Light Level (MaxFALL) of HDR
    # content ([0x0001-0xFFFF] = [1.0 - 65535.0] cd/m^2)
    ('desired_content_max_frame_average_luminance', NvU16),
]
_NV_HDR_CAPABILITIES_V2.display_data = display_data


class dv_static_metadata(ctypes.Structure):
    pass


dv_static_metadata._fields_ = [
    # not < Version of Vendor Data block,Version 0: 25 bytes Version 1: 14
    # bytes
    ('VSVDB_version', NvU32, 3),
    # not < Upper Nibble represents major version of Display
    # Management(DM) while lower represents minor version of DM
    ('dm_version', NvU32, 8),
    # not < If set sink is capable of 4kx2k @ 60hz
    ('supports_2160p60hz', NvU32, 1),
    # not < If set, sink is capable of YUV422-12 bit
    ('supports_YUV422_12bit', NvU32, 1),
    # not < Indicates if sink supports global dimming
    ('supports_global_dimming', NvU32, 1),
    # not < If set indicates sink supports DCI P3 colorimetry, REc709
    # otherwise
    ('colorimetry', NvU32, 1),
    # not < This is set when sink is using lowlatency interface and can
    # control its backlight.
    ('supports_backlight_control', NvU32, 2),
    # not < It is the level for Backlt min luminance value.
    ('backlt_min_luma', NvU32, 2),
    # not < Indicates the interface (standard or low latency) supported by
    # the sink.
    ('interface_supported_by_sink', NvU32, 2),
    # not < It is set when interface supported is low latency, it tells
    # whether it supports 10 bit or 12 bit RGB 4:4:4 or YCbCr 4:4:4 or
    # both.
    ('supports_10b_12b_444', NvU32, 2),
    # not < Should be set to zero
    ('reserved', NvU32, 9),
    # not < Represents min luminance level of Sink
    ('target_min_luminance', NvU16),
    # not < Represents max luminance level of sink
    ('target_max_luminance', NvU16),
    # not < Red primary chromaticity coordinate x
    ('cc_red_x', NvU16),
    # not < Red primary chromaticity coordinate y
    ('cc_red_y', NvU16),
    # not < Green primary chromaticity coordinate x
    ('cc_green_x', NvU16),
    # not < Green primary chromaticity coordinate Y
    ('cc_green_y', NvU16),
    # not < Blue primary chromaticity coordinate x
    ('cc_blue_x', NvU16),
    # not < Blue primary chromaticity coordinate y
    ('cc_blue_y', NvU16),
    # not < White primary chromaticity coordinate x
    ('cc_white_x', NvU16),
    # not < White primary chromaticity coordinate y
    ('cc_white_y', NvU16),
]
_NV_HDR_CAPABILITIES_V2.dv_static_metadata = dv_static_metadata

_NV_HDR_CAPABILITIES_V2._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < HDMI2.0a UHDA HDR with ST2084 EOTF (CEA861.3). Boolean: 0 =
    # not supported, 1 = supported;
    ('isST2084EotfSupported', NvU32, 1),
    # not < HDMI2.0a traditional HDR gamma (CEA861.3). Boolean: 0 = not
    # supported, 1 = supported;
    ('isTraditionalHdrGammaSupported', NvU32, 1),
    # not < Extended Dynamic Range on SDR displays. Boolean: 0 = not
    # supported, 1 = supported;
    ('isEdrSupported', NvU32, 1),
    # not < If set, driver will expand default (=zero) HDR capabilities
    # parameters contained in display's EDID.
    ('driverExpandDefaultHdrParameters', NvU32, 1),
    # not < HDMI2.0a traditional SDR gamma (CEA861.3). Boolean: 0 = not
    # supported, 1 = supported;
    ('isTraditionalSdrGammaSupported', NvU32, 1),
    # not < Dolby Vision Support. Boolean: 0 = not supported, 1 =
    # supported;
    ('isDolbyVisionSupported', NvU32, 1),
    ('reserved', NvU32, 26),
    # not < Static Metadata Descriptor Id (0 for static metadata type 1)
    ('static_metadata_descriptor_id', NV_STATIC_METADATA_DESCRIPTOR_ID),
    # not < Static Metadata Descriptor Type 1, CEA-861.3, SMPTE ST2086
    ('display_data', _NV_HDR_CAPABILITIES_V2.display_data),
    ('dv_static_metadata', _NV_HDR_CAPABILITIES_V2.dv_static_metadata),
]
NV_HDR_CAPABILITIES_VER1 = MAKE_NVAPI_VERSION(NV_HDR_CAPABILITIES_V1, 1)
NV_HDR_CAPABILITIES_VER2 = MAKE_NVAPI_VERSION(NV_HDR_CAPABILITIES_V2, 2)
NV_HDR_CAPABILITIES_VER = NV_HDR_CAPABILITIES_VER2
NV_HDR_CAPABILITIES = NV_HDR_CAPABILITIES_V2
# not \ingroup dispcontrol
# not @{
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Disp_GetHdrCapabilities
# not \fn
# NvAPI_Disp_GetHdrCapabilities(NvU32 displayId, NV_HDR_CAPABILITIES *pHdrCapabilities)
#
# not DESCRIPTION: This API gets High Dynamic Range (HDR) capabilities of
# the display.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  displayId   Monitor Identifier
# not \param [in,out] pHdrCapabilities display's HDR capabilities
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not   specific meaning for this API, they are listed below.
# ///////////////////////////////////////////////////////////////////////
NvAPI_Disp_GetHdrCapabilities = hDll.Disp_GetHdrCapabilities
NvAPI_Disp_GetHdrCapabilities.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_Disp_GetHdrCapabilities(__in NvU32 displayId, __inout NV_HDR_CAPABILITIES *pHdrCapabilities);


# not @}
class NV_HDR_CMD(ENUM):
    NV_HDR_CMD_GET = 0
    NV_HDR_CMD_SET = 1


NV_HDR_CMD_GET = NV_HDR_CMD.NV_HDR_CMD_GET
NV_HDR_CMD_SET = NV_HDR_CMD.NV_HDR_CMD_SET


class NV_HDR_MODE(ENUM):
    NV_HDR_MODE_OFF = 0

    # not < Source: CCCS [a.k.a FP16 scRGB, linear, sRGB primaries,
    # [-65504,0, 65504] range, RGB(1,1,1) = 80nits] Output : UHDA HDR
    # [a.k.a HDR10, RGB/YCC 10/12bpc ST2084(PQ) EOTF RGB(1,1,1) = 10000
    # nits, Rec2020 color primaries, ST2086 static HDR metadata]. This is
    # the only supported production HDR mode.
    NV_HDR_MODE_UHDA = 2

    # not < Experimental mode only, not for productionnot Source: HDR10
    # RGB 10bpc Output: HDR10 RGB 10 bpc - signal UHDA HDR mode
    # (PQ + Rec2020) to the sink but send source pixel values unmodified
    # (no PQ or Rec2020 conversions) - assumes source is already in HDR10
    # format.
    NV_HDR_MODE_UHDA_PASSTHROUGH = 5

    # not < Experimental mode only, not for productionnot Source: RGB8
    # Dolby Vision encoded (12 bpc YCbCr422 packed into RGB8) Output:
    # Dolby Vision encoded : Application is to encoded frames in DV format
    # and embed DV dynamic metadata as described in Dolby Vision
    # specification.
    NV_HDR_MODE_DOLBY_VISION = 7

    # not < Do not usenot Internal test mode only, to be removed. Source:
    # CCCS (a.k.a FP16 scRGB) Output : EDR (Extended Dynamic Range) - HDR
    # content is tonemapped and gamut mapped to output on regular SDR
    # display set to max luminance ( ~300 nits ).
    NV_HDR_MODE_EDR = 3

    # not < Do not usenot Internal test mode only, to be removed. Source:
    # any Output: SDR (Standard Dynamic Range), we continuously send SDR
    # EOTF InfoFrame signaling, HDMI compliance testing.
    NV_HDR_MODE_SDR = 4

    # not < Do not usenot Internal test mode only, to be removed. Source:
    # CCCS (a.k.a FP16 scRGB) Output : notebook HDR
    NV_HDR_MODE_UHDA_NB = 6

    # not < Do not usenot Obsolete, to be removed. NV_HDR_MODE_UHDBD ==
    # NV_HDR_MODE_UHDA, reflects obsolete pre-UHDA naming convention.
    NV_HDR_MODE_UHDBD = 2


NV_HDR_MODE_OFF = NV_HDR_MODE.NV_HDR_MODE_OFF
NV_HDR_MODE_UHDA = NV_HDR_MODE.NV_HDR_MODE_UHDA
NV_HDR_MODE_UHDA_PASSTHROUGH = NV_HDR_MODE.NV_HDR_MODE_UHDA_PASSTHROUGH
NV_HDR_MODE_DOLBY_VISION = NV_HDR_MODE.NV_HDR_MODE_DOLBY_VISION
NV_HDR_MODE_EDR = NV_HDR_MODE.NV_HDR_MODE_EDR
NV_HDR_MODE_SDR = NV_HDR_MODE.NV_HDR_MODE_SDR
NV_HDR_MODE_UHDA_NB = NV_HDR_MODE.NV_HDR_MODE_UHDA_NB
NV_HDR_MODE_UHDBD = NV_HDR_MODE.NV_HDR_MODE_UHDBD


class mastering_display_data(ctypes.Structure):
    pass


mastering_display_data._fields_ = [
    # not < x coordinate of color primary 0 (e.g. Red) of mastering
    # display ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_x0', NvU16),
    # not < y coordinate of color primary 0 (e.g. Red) of mastering
    # display ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_y0', NvU16),
    # not < x coordinate of color primary 1 (e.g. Green) of mastering
    # display ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_x1', NvU16),
    # not < y coordinate of color primary 1 (e.g. Green) of mastering
    # display ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_y1', NvU16),
    # not < x coordinate of color primary 2 (e.g. Blue) of mastering
    # display ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_x2', NvU16),
    # not < y coordinate of color primary 2 (e.g. Blue) of mastering
    # display ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_y2', NvU16),
    # not < x coordinate of white point of mastering display
    # ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayWhitePoint_x', NvU16),
    # not < y coordinate of white point of mastering display
    # ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayWhitePoint_y', NvU16),
    # not < Maximum display mastering luminance
    # ([0x0001-0xFFFF] = [1.0 - 65535.0] cd/m^2)
    ('max_display_mastering_luminance', NvU16),
    # not < Minimum display mastering luminance
    # ([0x0001-0xFFFF] = [1.0 - 6.55350] cd/m^2)
    ('min_display_mastering_luminance', NvU16),
    # not < Maximum Content Light level (MaxCLL)
    # ([0x0001-0xFFFF] = [1.0 - 65535.0] cd/m^2)
    ('max_content_light_level', NvU16),
    # not < Maximum Frame-Average Light Level (MaxFALL)
    # ([0x0001-0xFFFF] = [1.0 - 65535.0] cd/m^2)
    ('max_frame_average_light_level', NvU16),
]
_NV_HDR_COLOR_DATA_V1.mastering_display_data = mastering_display_data

_NV_HDR_COLOR_DATA_V1._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < Command get/set
    ('cmd', NV_HDR_CMD),
    # not < HDR mode
    ('hdrMode', NV_HDR_MODE),
    # not < Static Metadata Descriptor Id (0 for static metadata type 1)
    ('static_metadata_descriptor_id', NV_STATIC_METADATA_DESCRIPTOR_ID),
    # not < Static Metadata Descriptor Type 1, CEA-861.3, SMPTE ST2086
    ('mastering_display_data', _NV_HDR_COLOR_DATA_V1.mastering_display_data),
]


class mastering_display_data(ctypes.Structure):
    pass


mastering_display_data._fields_ = [
    # not < x coordinate of color primary 0 (e.g. Red) of mastering
    # display ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_x0', NvU16),
    # not < y coordinate of color primary 0 (e.g. Red) of mastering
    # display ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_y0', NvU16),
    # not < x coordinate of color primary 1 (e.g. Green) of mastering
    # display ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_x1', NvU16),
    # not < y coordinate of color primary 1 (e.g. Green) of mastering
    # display ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_y1', NvU16),
    # not < x coordinate of color primary 2 (e.g. Blue) of mastering
    # display ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_x2', NvU16),
    # not < y coordinate of color primary 2 (e.g. Blue) of mastering
    # display ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayPrimary_y2', NvU16),
    # not < x coordinate of white point of mastering display
    # ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayWhitePoint_x', NvU16),
    # not < y coordinate of white point of mastering display
    # ([0x0000-0xC350] = [0.0 - 1.0])
    ('displayWhitePoint_y', NvU16),
    # not < Maximum display mastering luminance
    # ([0x0001-0xFFFF] = [1.0 - 65535.0] cd/m^2)
    ('max_display_mastering_luminance', NvU16),
    # not < Minimum display mastering luminance
    # ([0x0001-0xFFFF] = [1.0 - 6.55350] cd/m^2)
    ('min_display_mastering_luminance', NvU16),
    # not < Maximum Content Light level (MaxCLL)
    # ([0x0001-0xFFFF] = [1.0 - 65535.0] cd/m^2)
    ('max_content_light_level', NvU16),
    # not < Maximum Frame-Average Light Level (MaxFALL)
    # ([0x0001-0xFFFF] = [1.0 - 65535.0] cd/m^2)
    ('max_frame_average_light_level', NvU16),
]
_NV_HDR_COLOR_DATA_V2.mastering_display_data = mastering_display_data

_NV_HDR_COLOR_DATA_V2._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < Command get/set
    ('cmd', NV_HDR_CMD),
    # not < HDR mode
    ('hdrMode', NV_HDR_MODE),
    # not < Static Metadata Descriptor Id (0 for static metadata type 1)
    ('static_metadata_descriptor_id', NV_STATIC_METADATA_DESCRIPTOR_ID),
    # not < Static Metadata Descriptor Type 1, CEA-861.3, SMPTE ST2086
    ('mastering_display_data', _NV_HDR_COLOR_DATA_V2.mastering_display_data),
    # not < Optional, One of NV_COLOR_FORMAT enum values, if set it will
    # apply requested color format for HDR session
    ('hdrColorFormat', NV_COLOR_FORMAT),
    # not < Optional, One of NV_DYNAMIC_RANGE enum values, if set it will
    # apply requested dynamic range for HDR session
    ('hdrDynamicRange', NV_DYNAMIC_RANGE),
    # not < Optional, One of NV_BPC enum values, if set it will apply
    # requested color depth
    ('hdrBpc', NV_BPC),
]
NV_HDR_COLOR_DATA_VER1 = MAKE_NVAPI_VERSION(NV_HDR_COLOR_DATA_V1, 1)
NV_HDR_COLOR_DATA_VER2 = MAKE_NVAPI_VERSION(NV_HDR_COLOR_DATA_V2, 2)
NV_HDR_COLOR_DATA_VER = NV_HDR_COLOR_DATA_VER2
NV_HDR_COLOR_DATA = NV_HDR_COLOR_DATA_V2
# not \ingroup dispcontrol
# not @{
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Disp_HdrColorControl
# not \fn
# NvAPI_Disp_HdrColorControl(NvU32 displayId, NV_HDR_COLOR_DATA *pHdrColorData)
#
# not DESCRIPTION: This API configures High Dynamic Range (HDR) and
# Extended Dynamic Range (EDR) output.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  displayId  Monitor Identifier
# not \param [in,out] pHdrColorData  HDR configuration data
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not   specific meaning for this API, they are listed below.
# ///////////////////////////////////////////////////////////////////////
NvAPI_Disp_HdrColorControl = hDll.Disp_HdrColorControl
NvAPI_Disp_HdrColorControl.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_Disp_HdrColorControl(__in NvU32 displayId, __inout NV_HDR_COLOR_DATA *pHdrColorData);


# not @}
# not \ingroup dispcontrol
# not Used in NvAPI_DISP_GetTiming().
class _Union_2(ctypes.Union):
    pass


_Union_2._fields_ = [
    # not < The actual analog HD/SDTV format. Used when the timing type is
    ('tvFormat', NvU32, 8),
    # not < The EIA/CEA 861B/D predefined SHORT timing descriptor ID.
    ('ceaId', NvU32, 8),
    # not < The NV predefined PsF format Id.
    ('nvPsfId', NvU32, 8),
]
NV_TIMING_FLAG._Union_2 = _Union_2

NV_TIMING_FLAG._anonymous_ = (
    '_Union_2',
)

NV_TIMING_FLAG._fields_ = [
    # not < To retrieve interlaced/progressive timing
    ('isInterlaced', NvU32, 4),
    ('reserved0', NvU32, 12),
    ('_Union_2', NV_TIMING_FLAG._Union_2),
    # not < Define preferred scaling
    ('scaling', NvU32, 8),
]

# not \ingroup dispcontrol
# not Used in NvAPI_DISP_GetTiming().
_NV_TIMING_INPUT._fields_ = [
    # not < (IN) structure version
    ('version', NvU32),
    # not < Visible horizontal size
    ('width', NvU32),
    # not < Visible vertical size
    ('height', NvU32),
    # not < Timing refresh rate
    ('rr', FLOAT),
    # not < Flag containing additional info for timing calculation.
    ('flag', NV_TIMING_FLAG),
    # not < Timing type(formula) to use for calculating the timing
    ('type', NV_TIMING_OVERRIDE),
]
NV_TIMING_INPUT_VER = MAKE_NVAPI_VERSION(NV_TIMING_INPUT, 1)

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DISP_GetTiming
# not DESCRIPTION: This function calculates the timing from the visible
# width/height/refresh-rate and timing type info.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 313
# not
# not
# not \param [in] displayId  Display ID of the display.
# not \param [in] timingInput Inputs used for calculating the timing.
# not \param [out] pTiming  Pointer to the NV_TIMING structure.
# not
# not \return  This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not    specific meaning for this API, they are listed below.
# not
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_DISP_GetTiming = hDll.DISP_GetTiming
NvAPI_DISP_GetTiming.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_DISP_GetTiming( __in NvU32 displayId,__in NV_TIMING_INPUT *timingInput, __out NV_TIMING *pTiming);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DISP_GetMonitorCapabilities
# not \fn
# NvAPI_DISP_GetMonitorCapabilities(NvU32 displayId, NV_MONITOR_CAPABILITIES *pMonitorCapabilities)
#
# not DESCRIPTION:  This API returns the Monitor capabilities
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] displayId   Monitor Identifier
# not \param [out]  pMonitorCapabilities  The monitor support info
# not
# not \return ::NVAPI_OK,
# not  ::NVAPI_ERROR,
# not  ::NVAPI_INVALID_ARGUMENT
# ///////////////////////////////////////////////////////////////////////
# not \ingroup dispcontrol
# not @{
# not HDMI-related and extended CAPs
class NV_MONITOR_CAPS_TYPE(ENUM):
    NV_MONITOR_CAPS_TYPE_HDMI_VSDB = 0x1000
    NV_MONITOR_CAPS_TYPE_HDMI_VCDB = 0x1001


NV_MONITOR_CAPS_TYPE_HDMI_VSDB = NV_MONITOR_CAPS_TYPE.NV_MONITOR_CAPS_TYPE_HDMI_VSDB
NV_MONITOR_CAPS_TYPE_HDMI_VCDB = NV_MONITOR_CAPS_TYPE.NV_MONITOR_CAPS_TYPE_HDMI_VCDB

_NV_MONITOR_CAPS_VCDB._fields_ = [
    ('quantizationRangeYcc', NvU8, 1),
    ('quantizationRangeRgb', NvU8, 1),
    ('scanInfoPreferredVideoFormat', NvU8, 2),
    ('scanInfoITVideoFormats', NvU8, 2),
    ('scanInfoCEVideoFormats', NvU8, 2),
]

# not See NvAPI_DISP_GetMonitorCapabilities().
_NV_MONITOR_CAPS_VSDB._fields_ = [
    # not < Byte 1
    ('sourcePhysicalAddressB', NvU8, 4),
    # not < Byte 1
    ('sourcePhysicalAddressA', NvU8, 4),
    # not < Byte 2
    ('sourcePhysicalAddressD', NvU8, 4),
    # not < Byte 2
    ('sourcePhysicalAddressC', NvU8, 4),
    # not < Byte 3
    ('supportDualDviOperation', NvU8, 1),
    # not < Byte 3
    ('reserved6', NvU8, 2),
    # not < Byte 3
    ('supportDeepColorYCbCr444', NvU8, 1),
    # not < Byte 3
    ('supportDeepColor30bits', NvU8, 1),
    # not < Byte 3
    ('supportDeepColor36bits', NvU8, 1),
    # not < Byte 3
    ('supportDeepColor48bits', NvU8, 1),
    # not < Byte 3
    ('supportAI', NvU8, 1),
    # not < Bye 4
    ('maxTmdsClock', NvU8),
    # not < Byte 5
    ('cnc0SupportGraphicsTextContent', NvU8, 1),
    # not < Byte 5
    ('cnc1SupportPhotoContent', NvU8, 1),
    # not < Byte 5
    ('cnc2SupportCinemaContent', NvU8, 1),
    # not < Byte 5
    ('cnc3SupportGameContent', NvU8, 1),
    # not < Byte 5
    ('reserved8', NvU8, 1),
    # not < Byte 5
    ('hasVicEntries', NvU8, 1),
    # not < Byte 5
    ('hasInterlacedLatencyField', NvU8, 1),
    # not < Byte 5
    ('hasLatencyField', NvU8, 1),
    # not < Byte 6
    ('videoLatency', NvU8),
    # not < Byte 7
    ('audioLatency', NvU8),
    # not < Byte 8
    ('interlacedVideoLatency', NvU8),
    # not < Byte 9
    ('interlacedAudioLatency', NvU8),
    # not < Byte 10
    ('reserved13', NvU8, 7),
    # not < Byte 10
    ('has3dEntries', NvU8, 1),
    # not < Byte 11
    ('hdmi3dLength', NvU8, 5),
    # not < Byte 11
    ('hdmiVicLength', NvU8, 3),
    # not < Keeping maximum length for 3 bits
    ('hdmi_vic', NvU8 * 7),
    # not < Keeping maximum length for 5 bits
    ('hdmi_3d', NvU8 * 31),
]


# not See NvAPI_DISP_GetMonitorCapabilities().
class data(ctypes.Union):
    pass


data._fields_ = [
    ('vsdb', NV_MONITOR_CAPS_VSDB),
    ('vcdb', NV_MONITOR_CAPS_VCDB),
]
_NV_MONITOR_CAPABILITIES_V1.data = data

_NV_MONITOR_CAPABILITIES_V1._fields_ = [
    ('version', NvU32),
    ('size', NvU16),
    ('infoType', NvU32),
    # not < Out: VGA, TV, DVI, HDMI, DP
    ('connectorType', NvU32),
    # not < Boolean : Returns invalid if requested info is not present
    # such as VCDB not present
    ('bIsValidInfo', NvU8, 1),
    ('data', _NV_MONITOR_CAPABILITIES_V1.data),
]
NV_MONITOR_CAPABILITIES = NV_MONITOR_CAPABILITIES_V1

# not Macro for constructing the version field of
# ::NV_MONITOR_CAPABILITIES_V1
NV_MONITOR_CAPABILITIES_VER1 = (
    MAKE_NVAPI_VERSION(NV_MONITOR_CAPABILITIES_V1, 1)
)
NV_MONITOR_CAPABILITIES_VER = NV_MONITOR_CAPABILITIES_VER1

# not @}
# not SUPPORTED OS: Windows 7 and higher
# not
# not \ingroup dispcontrol
NvAPI_DISP_GetMonitorCapabilities = hDll.DISP_GetMonitorCapabilities
NvAPI_DISP_GetMonitorCapabilities.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DISP_GetMonitorCapabilities(__in NvU32 displayId, __inout NV_MONITOR_CAPABILITIES *pMonitorCapabilities);

# not \ingroup dispcontrol
_NV_MONITOR_COLOR_DATA._fields_ = [
    ('version', NvU32),

    # not < One of the supported color formats
    ('colorFormat', NV_DP_COLOR_FORMAT),

    # not < One of the supported bit depths
    ('backendBitDepths', NV_DP_BPC),
]
NV_MONITOR_COLOR_CAPS = NV_MONITOR_COLOR_CAPS_V1
# not \ingroup dispcontrol
NV_MONITOR_COLOR_CAPS_VER1 = (
    MAKE_NVAPI_VERSION(NV_MONITOR_COLOR_CAPS_V1, 1)

)
NV_MONITOR_COLOR_CAPS_VER = NV_MONITOR_COLOR_CAPS_VER1
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DISP_GetMonitorColorCapabilities
# not DESCRIPTION: This API returns all the color formats and bit depth
# values supported by a given DP monitor.
# not
# not USAGE:  Sequence of calls which caller should make to get the
# information.
# not    1. First call NvAPI_DISP_GetMonitorColorCapabilities() with
# pMonitorColorCapabilities as NULL to get the count.
# not    2. Allocate memory for color caps(NV_MONITOR_COLOR_CAPS) array.
# not    3. Call NvAPI_DISP_GetMonitorColorCapabilities() again with the
# pointer to the memory allocated to get all the
# not    color capabilities.
# not
# not    Note :
# not    1. pColorCapsCount should never be NULL, else the API will fail
# with NVAPI_INVALID_ARGUMENT.
# not    2. *pColorCapsCount returned from the API will always be the
# actual count in any/every call.
# not    3. Memory size to be allocated should be
# (*pColorCapsCount * (ctypes.sizeof(NV_MONITOR_COLOR_CAPS)).
# not    4. If the memory allocated is less than what is required to
# return all the timings, this API will return the
# not    amount of information which can fit in user provided buffer and
# API will return NVAPI_INSUFFICIENT_BUFFER.
# not    5. If the caller specifies a greater value for *pColorCapsCount
# in second call to NvAPI_DISP_GetMonitorColorCapabilities()
# not    than what was returned from first call, the API will return only
# the actual number of elements in the color
# not    capabilities array and the extra buffer will remain unused.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] displayId   Monitor Identifier
# not \param [in, out] pMonitorColorCapabilities The monitor color
# capabilities information
# not \param [in, out] pColorCapsCount  - During input, the number of
# elements allocated for the pMonitorColorCapabilities pointer
# not        - During output, the actual number of color data elements the
# monitor supports
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not   specific meaning for this API, they are listed below.
# not
# not \retval  NVAPI_INSUFFICIENT_BUFFER The input buffer size is not
# sufficient to hold the total contents. In this case
# not        *pColorCapsCount will hold the required amount of elements.
# not \retval  NVAPI_INVALID_DISPLAY_ID The input monitor is either not
# connected or is not a DP panel.
# not
# not \ingroup dispcontrol
# not
# ///////////////////////////////////////////////////////////////////////
NvAPI_DISP_GetMonitorColorCapabilities = hDll.DISP_GetMonitorColorCapabilities
NvAPI_DISP_GetMonitorColorCapabilities.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DISP_GetMonitorColorCapabilities(__in NvU32 displayId, __inout_ecount_part_opt(*pColorCapsCount, *pColorCapsCount) NV_MONITOR_COLOR_CAPS *pMonitorColorCapabilities, __inout NvU32 *pColorCapsCount);

# not \ingroup dispcontrol
# not Used in NvAPI_DISP_EnumCustomDisplay() and
# NvAPI_DISP_TryCustomDisplay().
NV_CUSTOM_DISPLAY._fields_ = [
    ('version', NvU32),
    # not < Source surface(source mode) width
    ('width', NvU32),
    # not < Source surface(source mode) height
    ('height', NvU32),
    # not < Source surface color depth."0" means all 8/16/32bpp
    ('depth', NvU32),
    # not < Color format (optional)
    ('colorFormat', NV_FORMAT),
    # not < For multimon support, should be set to (0,0,1.0,1.0) for now.
    ('srcPartition', NV_VIEWPORTF),
    # not < Horizontal scaling ratio
    ('xRatio', FLOAT),
    # not < Vertical scaling ratio
    ('yRatio', FLOAT),
    # not < Timing used to program TMDS/DAC/LVDS/HDMI/TVEncoder, etc.
    ('timing', NV_TIMING),
    # not < If set, it means a hardware modeset without OS update
    ('hwModeSetOnly', NvU32, 1),
]

# not \ingroup dispcontrol
# not Used in NV_CUSTOM_DISPLAY.
NV_CUSTOM_DISPLAY_VER = MAKE_NVAPI_VERSION(NV_CUSTOM_DISPLAY, 1)

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DISP_EnumCustomDisplay
# not DESCRIPTION: This API enumerates the custom timing specified by the
# enum index.
# not   The client should keep enumerating until it returns
# NVAPI_END_ENUMERATION.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 313
# not
# not \param [in]  displayId Dispaly ID of the display.
# not \param [in]  index  Enum index
# not \param [inout] pCustDisp Pointer to the NV_CUSTOM_DISPLAY structure
# not
# not \return  This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not    specific meaning for this API, they are listed below.
# not \retval  NVAPI_INVALID_DISPLAY_ID: Custom Timing is not supported on
# the Display, whose display id is passed
# not
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_DISP_EnumCustomDisplay = hDll.DISP_EnumCustomDisplay
NvAPI_DISP_EnumCustomDisplay.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DISP_EnumCustomDisplay( __in NvU32 displayId, __in NvU32 index, __inout NV_CUSTOM_DISPLAY *pCustDisp);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DISP_TryCustomDisplay
# not DESCRIPTION: This API is used to set up a custom display without
# saving the configuration on multiple displays.
# not
# not \note
# not All the members of srcPartition, present in NV_CUSTOM_DISPLAY
# structure, should have their range in (0.0,1.0).
# not In clone mode the timings can applied to both the target monitors
# but only one target at a time. \n
# not For the secondary target the applied timings works under the
# following conditions:
# not - If the secondary monitor EDID supports the selected timing, OR
# not - If the selected custom timings can be scaled by the secondary
# monitor for the selected source resolution on the primary, OR
# not - If the selected custom timings matches the existing source
# resolution on the primary.
# not Setting up a custom display on non-active but connected monitors is
# supported only for Win7 and above.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 313
# not
# not
# not \param [in] pDisplayIds Array of the target display Dispaly IDs -
# See \ref handles.
# not \param [in] count  Total number of the incoming Display IDs and
# corresponding NV_CUSTOM_DISPLAY structure. This is for the multi-head
# support.
# not \param [in] pCustDisp Pointer to the NV_CUSTOM_DISPLAY structure
# array.
# not
# not \return  This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not    specific meaning for this API, they are listed below.
# not \retval  NVAPI_INVALID_DISPLAY_ID: Custom Timing is not supported on
# the Display, whose display id is passed
# not
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_DISP_TryCustomDisplay = hDll.DISP_TryCustomDisplay
NvAPI_DISP_TryCustomDisplay.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DISP_TryCustomDisplay( __in_ecount(count) NvU32 *pDisplayIds, __in NvU32 count, __in_ecount(count) NV_CUSTOM_DISPLAY *pCustDisp);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DISP_DeleteCustomDisplay
# not DESCRIPTION: This function deletes the custom display configuration,
# specified from the registry for all the displays whose display IDs are
# passed.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 313
# not
# not
# not \param [in]  pDisplayIds  Array of Dispaly IDs on which custom
# display configuration is to be saved.
# not \param [in]  count   Total number of the incoming Dispaly IDs. This
# is for the multi-head support.
# not \param [in]  pCustDisp  Pointer to the NV_CUSTOM_DISPLAY structure
# not
# not \return  This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not    specific meaning for this API, they are listed below.
# not \retval  NVAPI_INVALID_DISPLAY_ID: Custom Timing is not supported on
# the Display, whose display id is passed
# not
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_DISP_DeleteCustomDisplay = hDll.DISP_DeleteCustomDisplay
NvAPI_DISP_DeleteCustomDisplay.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DISP_DeleteCustomDisplay( __in_ecount(count) NvU32 *pDisplayIds, __in NvU32 count, __in NV_CUSTOM_DISPLAY *pCustDisp);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DISP_SaveCustomDisplay
# not DESCRIPTION: This function saves the current hardware display
# configuration on the specified Display IDs as a custom display
# configuration.
# not   This function should be called right after
# NvAPI_DISP_TryCustomDisplay() to save the custom display from the current
# not   hardware context. This function will not do anything if the custom
# display configuration is not tested on the hardware.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 313
# not
# not
# not \param [in]  pDisplayIds  Array of Dispaly IDs on which custom
# display configuration is to be saved.
# not \param [in]  count   Total number of the incoming Dispaly IDs. This
# is for the multi-head support.
# not \param [in]  isThisOutputIdOnly If set, the saved custom display
# will only be applied on the monitor with the same outputId
# (see \ref handles).
# not \param [in]  isThisMonitorIdOnly If set, the saved custom display
# will only be applied on the monitor with the same EDID ID or
# not       the same TV connector in case of analog TV.
# not
# not \return  This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not    specific meaning for this API, they are listed below.
# not \retval  NVAPI_INVALID_DISPLAY_ID: Custom Timing is not supported on
# the Display, whose display id is passed
# not
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_DISP_SaveCustomDisplay = hDll.DISP_SaveCustomDisplay
NvAPI_DISP_SaveCustomDisplay.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DISP_SaveCustomDisplay( __in_ecount(count) NvU32 *pDisplayIds, __in NvU32 count, __in NvU32 isThisOutputIdOnly, __in NvU32 isThisMonitorIdOnly);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DISP_RevertCustomDisplayTrial
# not DESCRIPTION: This API is used to restore the display configuration,
# that was changed by calling NvAPI_DISP_TryCustomDisplay(). This function
# not   must be called only after a custom display configuration is tested
# on the hardware, using NvAPI_DISP_TryCustomDisplay(),
# not   otherwise no action is taken. On Vista,
# NvAPI_DISP_RevertCustomDisplayTrial should be called with an active
# display that
# not   was affected during the NvAPI_DISP_TryCustomDisplay() call, per
# GPU.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 313
# not
# not
# not \param [in] pDisplayIds Pointer to display Id, of an active display.
# not \param [in] count  Total number of incoming Display IDs. For future
# use only. Currently it is expected to be passed as 1.
# not
# not \return  This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not    specific meaning for this API, they are listed below.
# not
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_DISP_RevertCustomDisplayTrial = hDll.DISP_RevertCustomDisplayTrial
NvAPI_DISP_RevertCustomDisplayTrial.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DISP_RevertCustomDisplayTrial( __in_ecount(count) NvU32* pDisplayIds, __in NvU32 count);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetView
# not This API lets caller retrieve the target display arrangement for
# selected source display handle.
# not \note Display PATH with this API is limited to single GPU. DUALVIEW
# across GPUs will be returned as STANDARD VIEW.
# not  Use NvAPI_SYS_GetDisplayTopologies() to query views across GPUs.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_DISP_GetDisplayConfig.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 85
# not
# not \param [in]  hNvDisplay   NVIDIA Display selection. It can be
# NVAPI_DEFAULT_HANDLE or a handle enumerated from
# not       NvAPI_EnumNVidiaDisplayHandle().
# not \param [out] pTargets   User allocated storage to retrieve an array
# of NV_VIEW_TARGET_INFO. Can be NULL to retrieve
# not       the targetCount.
# not \param [in,out] targetMaskCount  Count of target device mask
# specified in pTargetMask.
# not \param [out] targetView   Target view selected from
# NV_TARGET_VIEW_MODE.
# not
# not \retval  NVAPI_OK   Completed request
# not \retval  NVAPI_ERROR  Miscellaneous error occurred
# not \retval  NVAPI_INVALID_ARGUMENT Invalid input parameter.
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_GetView = hDll.GetView
NvAPI_GetView.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GetView(NvDisplayHandle hNvDisplay, NV_VIEW_TARGET_INFO *pTargets, NvU32 *pTargetMaskCount, NV_TARGET_VIEW_MODE *pTargetView);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetViewEx
# not DESCRIPTION: This API lets caller retrieve the target display
# arrangement for selected source display handle.
# not   \note Display PATH with this API is limited to single GPU.
# DUALVIEW across GPUs will be returned as STANDARD VIEW.
# not    Use NvAPI_SYS_GetDisplayTopologies() to query views across GPUs.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_DISP_GetDisplayConfig.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 165
# not
# not \param [in]  hNvDisplay  NVIDIA Display selection.
# NVAPI_DEFAULT_HANDLE is not allowed, it has to be a handle enumerated
# with
# not       NvAPI_EnumNVidiaDisplayHandle().
# not \param [in,out] pPathInfo  Count field should be set to
# NVAPI_MAX_DISPLAY_PATH. Can be NULL to retrieve just the pathCount.
# not \param [in,out] pPathCount  Number of elements in array
# pPathInfo.path.
# not \param [out] pTargetViewMode Display view selected from
# NV_TARGET_VIEW_MODE.
# not
# not \retval  NVAPI_OK    Completed request
# not \retval  NVAPI_API_NOT_INTIALIZED NVAPI not initialized
# not \retval  NVAPI_ERROR    Miscellaneous error occurred
# not \retval  NVAPI_INVALID_ARGUMENT  Invalid input parameter.
# not \retval  NVAPI_EXPECTED_DISPLAY_HANDLE hNvDisplay is not a valid
# display handle.
# not
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_GetViewEx = hDll.GetViewEx
NvAPI_GetViewEx.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GetViewEx(NvDisplayHandle hNvDisplay, NV_DISPLAY_PATH_INFO *pPathInfo, NvU32 *pPathCount, NV_TARGET_VIEW_MODE *pTargetViewMode);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetSupportedViews
# not This API lets caller enumerate all the supported NVIDIA display
# views - nView and Dualview modes.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 85
# not
# not \param [in]  hNvDisplay   NVIDIA Display selection. It can be
# NVAPI_DEFAULT_HANDLE or a handle enumerated from
# not       NvAPI_EnumNVidiaDisplayHandle().
# not \param [out] pTargetViews   Array of supported views. Can be NULL to
# retrieve the pViewCount first.
# not \param [in,out] pViewCount   Count of supported views.
# not
# not \retval  NVAPI_OK   Completed request
# not \retval  NVAPI_ERROR  Miscellaneous error occurred
# not \retval  NVAPI_INVALID_ARGUMENT Invalid input parameter.
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_GetSupportedViews = hDll.GetSupportedViews
NvAPI_GetSupportedViews.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GetSupportedViews(NvDisplayHandle hNvDisplay, NV_TARGET_VIEW_MODE *pTargetViews, NvU32 *pViewCount);


# not SUPPORTED OS: Windows 7 and higher
# not
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DISP_GetDisplayIdByDisplayName
# not DESCRIPTION:  This API retrieves the Display Id of a given display by
# not    display name. The display must be active to retrieve the
# not    displayId. In the case of clone mode or Surround gaming,
# not    the primary or top-left display will be returned.
# not
# not \param [in]  displayName Name of display (Eg: "\\DISPLAY1" to
# not      retrieve the displayId for.
# not \param [out] displayId Display ID of the requested display.
# not
# not retval ::NVAPI_OK:     Capabilties have been returned.
# not retval ::NVAPI_INVALID_ARGUMENT:  One or more args passed in are
# invalid.
# not retval ::NVAPI_API_NOT_INTIALIZED:  The NvAPI API needs to be
# initialized first
# not retval ::NVAPI_NO_IMPLEMENTATION:   This entrypoint not available
# not retval ::NVAPI_ERROR:     Miscellaneous error occurred
# not
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_DISP_GetDisplayIdByDisplayName = hDll.DISP_GetDisplayIdByDisplayName
NvAPI_DISP_GetDisplayIdByDisplayName.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DISP_GetDisplayIdByDisplayName(const char *displayName, NvU32* displayId);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DISP_GetDisplayConfig
# not DESCRIPTION:  This API lets caller retrieve the current global
# display
# not    configuration.
# not  USAGE:  The caller might have to call this three times to fetch all
# the required configuration details as follows:
# not    First Pass: Caller should Call NvAPI_DISP_GetDisplayConfig() with
# pathInfo set to NULL to fetch pathInfoCount.
# not    Second Pass: Allocate memory for pathInfo with respect to the
# number of pathInfoCount(from First Pass) to fetch
# not      targetInfoCount. If sourceModeInfo is needed allocate memory or
# it can be initialized to NULL.
# not   Third
# Pass(Optional, only required if target information is required):
# Allocate memory for targetInfo with respect
# not      to number of targetInfoCount(from Second Pass).
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in,out] pathInfoCount Number of elements in pathInfo array,
# returns number of valid topologies, this cannot be null.
# not \param [in,out] pathInfo  Array of path information
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status. If there are return error codes with
# not   specific meaning for this API, they are listed below.
# not
# not \retval NVAPI_INVALID_ARGUMENT - Invalid input parameter. Following
# can be the reason for this return value:
# not        - pathInfoCount is NULL.
# not        - *pathInfoCount is 0 and pathInfo is not NULL.
# not        - *pathInfoCount is not 0 and pathInfo is NULL.
# not \retval NVAPI_DEVICE_BUSY  - ModeSet has not yet completed. Please
# wait and call it again.
# not
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_DISP_GetDisplayConfig = hDll.DISP_GetDisplayConfig
NvAPI_DISP_GetDisplayConfig.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DISP_GetDisplayConfig(__inout NvU32 *pathInfoCount, __out_ecount_full_opt(*pathInfoCount) NV_DISPLAYCONFIG_PATH_INFO *pathInfo);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DISP_SetDisplayConfig
# not DESCRIPTION:  This API lets caller apply a global display
# configuration
# not    across multiple GPUs.
# not
# not    If all sourceIds are zero, then NvAPI will pick up sourceId's
# based on the following criteria :
# not    - If user provides sourceModeInfo then we are trying to assign
# 0th sourceId always to GDIPrimary.
# not    This is needed since active windows always moves along with 0th
# sourceId.
# not    - For rest of the paths, we are incrementally assigning the
# sourceId per adapter basis.
# not    - If user doesn't provide sourceModeInfo then NVAPI just picks up
# some default sourceId's in incremental order.
# not    Note : NVAPI will not intelligently choose the sourceIDs for any
# configs that does not need a modeset.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] pathInfoCount Number of supplied elements in pathInfo
# not \param [in] pathInfo  Array of path information
# not \param [in] flags   Flags for applying settings
# not
# not \retval ::NVAPI_OK - completed request
# not \retval ::NVAPI_API_NOT_INTIALIZED - NVAPI not initialized
# not \retval ::NVAPI_ERROR - miscellaneous error occurred
# not \retval ::NVAPI_INVALID_ARGUMENT - Invalid input parameter.
# not
# not \ingroup dispcontrol
# ///////////////////////////////////////////////////////////////////////
NvAPI_DISP_SetDisplayConfig = hDll.DISP_SetDisplayConfig
NvAPI_DISP_SetDisplayConfig.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DISP_SetDisplayConfig(__in NvU32 pathInfoCount, __in_ecount(pathInfoCount) NV_DISPLAYCONFIG_PATH_INFO* pathInfo, __in NvU32 flags);

# ////////////////////////////////////////////////////////////////////////////////
# MOSAIC allows a multi display target output scanout on a single source.
# SAMPLE of MOSAIC 1x4 topo with 8 pixel horizontal overlap
# + ------------------------- + + ------------------------- + +
# ------------------------- + + ------------------------- +
# |     or     or     or     |
# |     or     or     or     |
# |     or     or     or     |
# |  DVI1   or   DVI2  or  DVI3  or  DVI4  |
# |     or     or     or     |
# |     or     or     or     |
# |     or     or     or     |
# |     or     or     or     |
# + ------------------------- + + ------------------------- + +
# ------------------------- + + ------------------------- +
# not \addtogroup mosaicapi
# not @{
NVAPI_MAX_MOSAIC_DISPLAY_ROWS = 8
NVAPI_MAX_MOSAIC_DISPLAY_COLUMNS = 8
# These bits are used to describe the validity of a topo.
# not < The topology is valid
NV_MOSAIC_TOPO_VALIDITY_VALID = 0x00000000
# not < Not enough SLI GPUs were found to fill the entire
NV_MOSAIC_TOPO_VALIDITY_MISSING_GPU = 0x00000001
# not topology. hPhysicalGPU will be 0 for these.
# not < Not enough displays were found to fill the entire
NV_MOSAIC_TOPO_VALIDITY_MISSING_DISPLAY = 0x00000002
# not topology. displayOutputId will be 0 for these.
# not < The topoogy is only possible with displays of the same
NV_MOSAIC_TOPO_VALIDITY_MIXED_DISPLAY_TYPES = 0x00000004


# not NV_GPU_OUTPUT_TYPE. Check displayOutputIds to make
# not sure they are all CRTs, or all DFPs.
# not This structure defines the topology details.
class gpuLayout(ctypes.Structure):
    pass


gpuLayout._fields_ = [
    # not < Physical GPU to be used in the topology (0 if GPU missing)
    ('hPhysicalGPU', NvPhysicalGpuHandle),
    # not < Connected display target (0 if no display connected)
    ('displayOutputId', NvU32),
    # not < Pixels of overlap on left of target: ( + overlap, -gap)
    ('overlapX', NvS32),
    # not < Pixels of overlap on top of target: ( + overlap, -gap)
    ('overlapY', NvS32),
]
NV_MOSAIC_TOPO_DETAILS.gpuLayout = gpuLayout

NV_MOSAIC_TOPO_DETAILS._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < Logical GPU for this topology
    ('hLogicalGPU', NvLogicalGpuHandle),
    # not < 0 means topology is valid with the current hardware.
    ('validityMask', NvU32),
    # not < Number of displays in a row
    ('rowCount', NvU32),
    # not < Number of displays in a column
    ('colCount', NvU32),
    ('gpuLayout', (NV_MOSAIC_TOPO_DETAILS.gpuLayout * NVAPI_MAX_MOSAIC_DISPLAY_ROWS) * NVAPI_MAX_MOSAIC_DISPLAY_COLUMNS),
]
# not Macro for constructing te vesion field of NV_MOSAIC_TOPO_DETAILS
NVAPI_MOSAIC_TOPO_DETAILS_VER = (
    MAKE_NVAPI_VERSION(NV_MOSAIC_TOPO_DETAILS, 1)
)
# not These values refer to the different types of Mosaic topologies that
# are possible. When
# not getting the supported Mosaic topologies, you can specify one of
# these types to narrow down
# not the returned list to only those that match the given type.


class NV_MOSAIC_TOPO_TYPE(ENUM):
    NV_MOSAIC_TOPO_TYPE_ALL = 1
    NV_MOSAIC_TOPO_TYPE_BASIC = 2
    NV_MOSAIC_TOPO_TYPE_PASSIVE_STEREO = 3
    NV_MOSAIC_TOPO_TYPE_SCALED_CLONE = 4
    NV_MOSAIC_TOPO_TYPE_PASSIVE_STEREO_SCALED_CLONE = 5
    NV_MOSAIC_TOPO_TYPE_MAX = 6


NV_MOSAIC_TOPO_TYPE_ALL = NV_MOSAIC_TOPO_TYPE.NV_MOSAIC_TOPO_TYPE_ALL
NV_MOSAIC_TOPO_TYPE_BASIC = NV_MOSAIC_TOPO_TYPE.NV_MOSAIC_TOPO_TYPE_BASIC
NV_MOSAIC_TOPO_TYPE_PASSIVE_STEREO = NV_MOSAIC_TOPO_TYPE.NV_MOSAIC_TOPO_TYPE_PASSIVE_STEREO
NV_MOSAIC_TOPO_TYPE_SCALED_CLONE = NV_MOSAIC_TOPO_TYPE.NV_MOSAIC_TOPO_TYPE_SCALED_CLONE
NV_MOSAIC_TOPO_TYPE_PASSIVE_STEREO_SCALED_CLONE = NV_MOSAIC_TOPO_TYPE.NV_MOSAIC_TOPO_TYPE_PASSIVE_STEREO_SCALED_CLONE
NV_MOSAIC_TOPO_TYPE_MAX = NV_MOSAIC_TOPO_TYPE.NV_MOSAIC_TOPO_TYPE_MAX


# not This is a complete list of supported Mosaic topologies.
# not
# not Using a "Basic" topology combines multiple monitors to create a
# single desktop.
# not
# not Using a "Passive" topology combines multiples monitors to create a
# passive stereo desktop.
# not In passive stereo, two identical topologies combine - one topology
# is used for the right eye and the other identical //not topology
# (targeting different displays) is used for the left eye. \n
# not NOTE: common\inc\nvEscDef.h shadows a couple PASSIVE_STEREO enums.
# If this
# not  enum list changes and effects the value of
# NV_MOSAIC_TOPO_BEGIN_PASSIVE_STEREO
# not  please update the corresponding value in nvEscDef.h
class NV_MOSAIC_TOPO(ENUM):
    NV_MOSAIC_TOPO_NONE = 1
    NV_MOSAIC_TOPO_BEGIN_BASIC = 2
    NV_MOSAIC_TOPO_1x2_BASIC = NV_MOSAIC_TOPO_BEGIN_BASIC
    NV_MOSAIC_TOPO_2x1_BASIC = 3
    NV_MOSAIC_TOPO_1x3_BASIC = 4
    NV_MOSAIC_TOPO_3x1_BASIC = 5
    NV_MOSAIC_TOPO_1x4_BASIC = 6
    NV_MOSAIC_TOPO_4x1_BASIC = 7
    NV_MOSAIC_TOPO_2x2_BASIC = 8
    NV_MOSAIC_TOPO_2x3_BASIC = 9
    NV_MOSAIC_TOPO_2x4_BASIC = 10
    NV_MOSAIC_TOPO_3x2_BASIC = 11
    NV_MOSAIC_TOPO_4x2_BASIC = 12
    NV_MOSAIC_TOPO_1x5_BASIC = 13
    NV_MOSAIC_TOPO_1x6_BASIC = 14
    NV_MOSAIC_TOPO_7x1_BASIC = 15
    NV_MOSAIC_TOPO_END_BASIC = NV_MOSAIC_TOPO_7x1_BASIC + 9
    NV_MOSAIC_TOPO_BEGIN_PASSIVE_STEREO = 25
    NV_MOSAIC_TOPO_1x2_PASSIVE_STEREO = NV_MOSAIC_TOPO_BEGIN_PASSIVE_STEREO
    NV_MOSAIC_TOPO_2x1_PASSIVE_STEREO = 26
    NV_MOSAIC_TOPO_1x3_PASSIVE_STEREO = 27
    NV_MOSAIC_TOPO_3x1_PASSIVE_STEREO = 28
    NV_MOSAIC_TOPO_1x4_PASSIVE_STEREO = 29
    NV_MOSAIC_TOPO_4x1_PASSIVE_STEREO = 30
    NV_MOSAIC_TOPO_2x2_PASSIVE_STEREO = 31
    NV_MOSAIC_TOPO_END_PASSIVE_STEREO = (
            NV_MOSAIC_TOPO_2x2_PASSIVE_STEREO + 4
    )
    NV_MOSAIC_TOPO_MAX = 36


NV_MOSAIC_TOPO_NONE = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_NONE
NV_MOSAIC_TOPO_BEGIN_BASIC = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_BEGIN_BASIC
NV_MOSAIC_TOPO_1x2_BASIC = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_1x2_BASIC
NV_MOSAIC_TOPO_2x1_BASIC = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_2x1_BASIC
NV_MOSAIC_TOPO_1x3_BASIC = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_1x3_BASIC
NV_MOSAIC_TOPO_3x1_BASIC = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_3x1_BASIC
NV_MOSAIC_TOPO_1x4_BASIC = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_1x4_BASIC
NV_MOSAIC_TOPO_4x1_BASIC = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_4x1_BASIC
NV_MOSAIC_TOPO_2x2_BASIC = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_2x2_BASIC
NV_MOSAIC_TOPO_2x3_BASIC = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_2x3_BASIC
NV_MOSAIC_TOPO_2x4_BASIC = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_2x4_BASIC
NV_MOSAIC_TOPO_3x2_BASIC = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_3x2_BASIC
NV_MOSAIC_TOPO_4x2_BASIC = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_4x2_BASIC
NV_MOSAIC_TOPO_1x5_BASIC = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_1x5_BASIC
NV_MOSAIC_TOPO_1x6_BASIC = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_1x6_BASIC
NV_MOSAIC_TOPO_7x1_BASIC = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_7x1_BASIC
NV_MOSAIC_TOPO_END_BASIC = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_END_BASIC
NV_MOSAIC_TOPO_BEGIN_PASSIVE_STEREO = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_BEGIN_PASSIVE_STEREO
NV_MOSAIC_TOPO_1x2_PASSIVE_STEREO = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_1x2_PASSIVE_STEREO
NV_MOSAIC_TOPO_2x1_PASSIVE_STEREO = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_2x1_PASSIVE_STEREO
NV_MOSAIC_TOPO_1x3_PASSIVE_STEREO = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_1x3_PASSIVE_STEREO
NV_MOSAIC_TOPO_3x1_PASSIVE_STEREO = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_3x1_PASSIVE_STEREO
NV_MOSAIC_TOPO_1x4_PASSIVE_STEREO = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_1x4_PASSIVE_STEREO
NV_MOSAIC_TOPO_4x1_PASSIVE_STEREO = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_4x1_PASSIVE_STEREO
NV_MOSAIC_TOPO_2x2_PASSIVE_STEREO = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_2x2_PASSIVE_STEREO
NV_MOSAIC_TOPO_END_PASSIVE_STEREO = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_END_PASSIVE_STEREO
NV_MOSAIC_TOPO_MAX = NV_MOSAIC_TOPO.NV_MOSAIC_TOPO_MAX

# not This is a "topology brief" structure. It tells you what you need to
# know about
# not a topology at a high level. A list of these is returned when you
# query for the
# not supported Mosaic information.
# not
# not If you need more detailed information about the topology, call
# not NvAPI_Mosaic_GetTopoGroup() with the topology value from this
# structure.
NV_MOSAIC_TOPO_BRIEF._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < The topology
    ('topo', NV_MOSAIC_TOPO),
    # not < 1 if topo is enabled, else 0
    ('enabled', NvU32),
    # not < 1 if topo *can* be enabled, else 0
    ('isPossible', NvU32),
]

# not Macro for constructing the version field of NV_MOSAIC_TOPO_BRIEF
NVAPI_MOSAIC_TOPO_BRIEF_VER = MAKE_NVAPI_VERSION(NV_MOSAIC_TOPO_BRIEF, 1)

# not Basic per-display settings that are used in setting/getting the
# Mosaic mode
_NV_MOSAIC_DISPLAY_SETTING_V1._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < Per-display width
    ('width', NvU32),
    # not < Per-display height
    ('height', NvU32),
    # not < Bits per pixel
    ('bpp', NvU32),
    # not < Display frequency
    ('freq', NvU32),
]

NV_MOSAIC_DISPLAY_SETTING_V2._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < Per-display width
    ('width', NvU32),
    # not < Per-display height
    ('height', NvU32),
    # not < Bits per pixel
    ('bpp', NvU32),
    # not < Display frequency
    ('freq', NvU32),
    # not < Display frequency in x1k
    ('rrx1k', NvU32),
]
NV_MOSAIC_DISPLAY_SETTING = NV_MOSAIC_DISPLAY_SETTING_V2

# not Macro for constructing the version field of NV_MOSAIC_DISPLAY_SETTING
NVAPI_MOSAIC_DISPLAY_SETTING_VER1 = (
    MAKE_NVAPI_VERSION(NV_MOSAIC_DISPLAY_SETTING_V1, 1)
)
NVAPI_MOSAIC_DISPLAY_SETTING_VER2 = (
    MAKE_NVAPI_VERSION(NV_MOSAIC_DISPLAY_SETTING_V2, 2)
)
NVAPI_MOSAIC_DISPLAY_SETTING_VER = NVAPI_MOSAIC_DISPLAY_SETTING_VER2

# Set a reasonable max number of display settings to support
# so arrays are bound.
# not < Set a reasonable maximum number of display settings to support
NV_MOSAIC_DISPLAY_SETTINGS_MAX = 40

# not so arrays are bound.
# not This structure is used to contain a list of supported Mosaic
# topologies
# not along with the display settings that can be used.
_NV_MOSAIC_SUPPORTED_TOPO_INFO_V1._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < Number of topologies in below array
    ('topoBriefsCount', NvU32),
    # not < List of supported topologies with only brief details
    ('topoBriefs', NV_MOSAIC_TOPO_BRIEF * NV_MOSAIC_TOPO_MAX),
    # not < Number of display settings in below array
    ('displaySettingsCount', NvU32),
    # not < List of per display settings possible
    ('displaySettings', NV_MOSAIC_DISPLAY_SETTING_V1 * NV_MOSAIC_DISPLAY_SETTINGS_MAX),
]

_NV_MOSAIC_SUPPORTED_TOPO_INFO_V2._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < Number of topologies in below array
    ('topoBriefsCount', NvU32),
    # not < List of supported topologies with only brief details
    ('topoBriefs', NV_MOSAIC_TOPO_BRIEF * NV_MOSAIC_TOPO_MAX),
    # not < Number of display settings in below array
    ('displaySettingsCount', NvU32),
    # not < List of per display settings possible
    ('displaySettings', NV_MOSAIC_DISPLAY_SETTING_V2 * NV_MOSAIC_DISPLAY_SETTINGS_MAX),
]
NV_MOSAIC_SUPPORTED_TOPO_INFO = NV_MOSAIC_SUPPORTED_TOPO_INFO_V2

# not Macro forconstructing the version field of
# NV_MOSAIC_SUPPORTED_TOPO_INFO
NVAPI_MOSAIC_SUPPORTED_TOPO_INFO_VER1 = (
    MAKE_NVAPI_VERSION(NV_MOSAIC_SUPPORTED_TOPO_INFO_V1, 1)
)
NVAPI_MOSAIC_SUPPORTED_TOPO_INFO_VER2 = (
    MAKE_NVAPI_VERSION(NV_MOSAIC_SUPPORTED_TOPO_INFO_V2, 2)
)
NVAPI_MOSAIC_SUPPORTED_TOPO_INFO_VER = (
    NVAPI_MOSAIC_SUPPORTED_TOPO_INFO_VER2
)

# Indices to use to access the topos array within the mosaic topology
NV_MOSAIC_TOPO_IDX_DEFAULT = 0
NV_MOSAIC_TOPO_IDX_LEFT_EYE = 0
NV_MOSAIC_TOPO_IDX_RIGHT_EYE = 1
NV_MOSAIC_TOPO_NUM_EYES = 2

# not This defines the maximum number of topos that can be in a topo group.
# not At this time, it is set to 2 because our largest topo group (passive
# not stereo) only needs 2 topos (left eye and right eye).
# not
# not If a new topo group with more than 2 topos is added above, then this
# not number will also have to be incremented.
NV_MOSAIC_MAX_TOPO_PER_TOPO_GROUP = 2

# not This structure defines a group of topologies that work together to
# create one
# not overall layout. All of the supported topologies are represented with
# this
# not structure.
# not
# not For example, a 'Passive Stereo' topology would be represented with
# this
# not structure, and would have separate topology details for the left and
# right eyes.
# not The count would be 2. A 'Basic' topology is also represented by this
# structure,
# not with a count of 1.
# not
# not The structure is primarily used internally, but is exposed to
# applications in a
# not read-only fashion because there are some details in it that might be
# useful
# not (like the number of rows/cols, or connected display information). A
# user can
# not get the filled-in structure by calling NvAPI_Mosaic_GetTopoGroup().
# not
# not You can then look at the detailed values within the structure. There
# are no
# not entrypoints which take this structure as input
# (effectively making it read-only).
NV_MOSAIC_TOPO_GROUP._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < The brief details of this topo
    ('brief', NV_MOSAIC_TOPO_BRIEF),
    # not < Number of topos in array below
    ('count', NvU32),
    ('topos', NV_MOSAIC_TOPO_DETAILS * NV_MOSAIC_MAX_TOPO_PER_TOPO_GROUP),
]

# not Macro for constructing the version field of NV_MOSAIC_TOPO_GROUP
NVAPI_MOSAIC_TOPO_GROUP_VER = MAKE_NVAPI_VERSION(NV_MOSAIC_TOPO_GROUP, 1)

# not @}
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Mosaic_GetSupportedTopoInfo
# not DESCRIPTION:  This API returns information on the topologies and
# display resolutions
# not    supported by Mosaic mode.
# not
# not    NOTE: Not all topologies returned can be set immediately.
# not     See 'OUT' Notes below.
# not
# not    Once you get the list of supported topologies, you can call
# not    NvAPI_Mosaic_GetTopoGroup() with one of the Mosaic topologies if
# you need
# not    more information about it.
# not
# not  < b > 'IN' Notes: < /b > pSupportedTopoInfo.version must be set
# before calling this function.
# not    If the specified version is not supported by this implementation,
# not    an error will be returned (NVAPI_INCOMPATIBLE_STRUCT_VERSION).
# not
# not  < b > 'OUT' Notes: < /b > Some of the topologies returned might not
# be valid for one reason or
# not    another. It could be due to mismatched or missing displays. It
# not    could also be because the required number of GPUs is not found.
# not    At a high level, you can see if the topology is valid and can be
# enabled
# not    by looking at the pSupportedTopoInfo.topoBriefs[xxx].isPossible
# flag.
# not    If this is true, the topology can be enabled. If it
# not    is false, you can find out why it cannot be enabled by getting the
# not    details of the topology via NvAPI_Mosaic_GetTopoGroup(). From
# there,
# not    look at the validityMask of the individual topologies. The bits
# can
# not    be tested against the NV_MOSAIC_TOPO_VALIDITY_* bits.
# not
# not    It is possible for this function to return NVAPI_OK with no
# topologies
# not    listed in the return structure. If this is the case, it means that
# not    the current hardware DOES support Mosaic, but with the given
# configuration
# not    no valid topologies were found. This most likely means that SLI
# was not
# not    enabled for the hardware. Once enabled, you should see valid
# topologies
# not    returned from this function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 185
# not
# not
# not \param [in,out] pSupportedTopoInfo Information about what topologies
# and display resolutions
# not       are supported for Mosaic.
# not \param [in] type   The type of topologies the caller is interested in
# not       getting. See NV_MOSAIC_TOPO_TYPE for possible values.
# not
# not \retval ::NVAPI_OK     No errors in returning supported topologies.
# not \retval ::NVAPI_NOT_SUPPORTED   Mosaic is not supported with the
# existing hardware.
# not \retval ::NVAPI_INVALID_ARGUMENT  One or more arguments passed in
# are invalid.
# not \retval ::NVAPI_API_NOT_INTIALIZED  The NvAPI API needs to be
# initialized first.
# not \retval ::NVAPI_NO_IMPLEMENTATION   This entrypoint not available.
# not \retval ::NVAPI_INCOMPATIBLE_STRUCT_VERSION The version of the
# structure passed in is not
# compatible with this entry point.
# not \retval ::NVAPI_ERROR:    Miscellaneous error occurred.
# not
# not \ingroup mosaicapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Mosaic_GetSupportedTopoInfo = hDll.Mosaic_GetSupportedTopoInfo
NvAPI_Mosaic_GetSupportedTopoInfo.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Mosaic_GetSupportedTopoInfo(NV_MOSAIC_SUPPORTED_TOPO_INFO *pSupportedTopoInfo, NV_MOSAIC_TOPO_TYPE type);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Mosaic_GetTopoGroup
# not DESCRIPTION:  This API returns a structure filled with the details
# not    of the specified Mosaic topology.
# not
# not    If the pTopoBrief passed in matches the current topology,
# not    then information in the brief and group structures
# not    will reflect what is current. Thus the brief would have
# not    the current 'enable' status, and the group would have the
# not    current overlap values. If there is no match, then the
# not    returned brief has an 'enable' status of FALSE (since it
# not    is obviously not enabled), and the overlap values will be 0.
# not
# not  < b > 'IN' Notes: < /b > pTopoGroup.version must be set before
# calling this function.
# not    If the specified version is not supported by this implementation,
# not    an error will be returned (NVAPI_INCOMPATIBLE_STRUCT_VERSION).
# not
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 185
# not
# not \param [in]  pTopoBrief  The topology for getting the details
# not      This must be one of the topology briefs
# not      returned from NvAPI_Mosaic_GetSupportedTopoInfo().
# not \param [in,out] pTopoGroup  The topology details matching the brief
# not
# not \retval ::NVAPI_OK     Details were retrieved successfully.
# not \retval ::NVAPI_NOT_SUPPORTED   Mosaic is not supported with the
# existing hardware.
# not \retval ::NVAPI_INVALID_ARGUMENT  One or more argumentss passed in
# are invalid.
# not \retval ::NVAPI_API_NOT_INTIALIZED  The NvAPI API needs to be
# initialized first.
# not \retval ::NVAPI_NO_IMPLEMENTATION   This entrypoint not available.
# not \retval ::NVAPI_INCOMPATIBLE_STRUCT_VERSION The version of the
# structure passed in is not
# compatible with this entry point.
# not \retval ::NVAPI_ERROR:    Miscellaneous error occurred.
# not
# not \ingroup mosaicapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Mosaic_GetTopoGroup = hDll.Mosaic_GetTopoGroup
NvAPI_Mosaic_GetTopoGroup.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Mosaic_GetTopoGroup(NV_MOSAIC_TOPO_BRIEF *pTopoBrief, NV_MOSAIC_TOPO_GROUP *pTopoGroup);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Mosaic_GetOverlapLimits
# not DESCRIPTION:  This API returns the X and Y overlap limits required if
# not    the given Mosaic topology and display settings are to be used.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 185
# not
# not \param [in] pTopoBrief  The topology for getting limits
# not      This must be one of the topo briefs
# not      returned from NvAPI_Mosaic_GetSupportedTopoInfo().
# not \param [in] pDisplaySetting  The display settings for getting the
# limits.
# not      This must be one of the settings
# not      returned from NvAPI_Mosaic_GetSupportedTopoInfo().
# not \param [out] pMinOverlapX  X overlap minimum
# not \param [out] pMaxOverlapX  X overlap maximum
# not \param [out] pMinOverlapY  Y overlap minimum
# not \param [out] pMaxOverlapY  Y overlap maximum
# not
# not \retval ::NVAPI_OK     Details were retrieved successfully.
# not \retval ::NVAPI_NOT_SUPPORTED   Mosaic is not supported with the
# existing hardware.
# not \retval ::NVAPI_INVALID_ARGUMENT  One or more argumentss passed in
# are invalid.
# not \retval ::NVAPI_API_NOT_INTIALIZED  The NvAPI API needs to be
# initialized first.
# not \retval ::NVAPI_NO_IMPLEMENTATION   This entrypoint not available.
# not \retval ::NVAPI_INCOMPATIBLE_STRUCT_VERSION The version of the
# structure passed in is not
# not        compatible with this entry point.
# not \retval ::NVAPI_ERROR     Miscellaneous error occurred.
# not
# not \ingroup mosaicapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Mosaic_GetOverlapLimits = hDll.Mosaic_GetOverlapLimits
NvAPI_Mosaic_GetOverlapLimits.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Mosaic_GetOverlapLimits(NV_MOSAIC_TOPO_BRIEF *pTopoBrief, NV_MOSAIC_DISPLAY_SETTING *pDisplaySetting, NvS32 *pMinOverlapX, NvS32 *pMaxOverlapX, NvS32 *pMinOverlapY, NvS32 *pMaxOverlapY);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Mosaic_SetCurrentTopo
# not DESCRIPTION:  This API sets the Mosaic topology and performs a mode
# switch
# not    using the given display settings.
# not
# not    If NVAPI_OK is returned, the current Mosaic topology was set
# not    correctly. Any other status returned means the
# not    topology was not set, and remains what it was before this
# not    function was called.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 185
# not
# not \param [in]  pTopoBrief  The topology to set. This must be one of
# the topologies returned from
# not      NvAPI_Mosaic_GetSupportedTopoInfo(), and it must have an
# isPossible value of 1.
# not \param [in]  pDisplaySetting The per display settings to be used in
# the Mosaic mode. This must be one of the
# not      settings returned from NvAPI_Mosaic_GetSupportedTopoInfo().
# not \param [in]  overlapX  The pixel overlap to use between horizontal
# displays (use positive a number for
# not      overlap, or a negative number to create a
# gap.) If the overlap is out of bounds
# not      for what is possible given the topo and display setting, the
# overlap will be clamped.
# not \param [in]  overlapY  The pixel overlap to use between vertical
# displays (use positive a number for
# not      overlap, or a negative number to create a
# gap.) If the overlap is out of bounds for
# not      what is possible given the topo and display setting, the
# overlap will be clamped.
# not \param [in]  enable  If 1, the topology being set will also be
# enabled, meaning that the mode set will
# not      occur. \n
# not      If 0, you don't want to be in Mosaic mode right now, but want
# to set the current
# not      Mosaic topology so you can enable it later with
# NvAPI_Mosaic_EnableCurrentTopo().
# not
# not \retval ::NVAPI_OK     The Mosaic topology was set.
# not \retval ::NVAPI_NOT_SUPPORTED   Mosaic is not supported with the
# existing hardware.
# not \retval ::NVAPI_INVALID_ARGUMENT  One or more argumentss passed in
# are invalid.
# not \retval ::NVAPI_TOPO_NOT_POSSIBLE   The topology passed in is not
# currently possible.
# not \retval ::NVAPI_API_NOT_INTIALIZED  The NvAPI API needs to be
# initialized first.
# not \retval ::NVAPI_NO_IMPLEMENTATION   This entrypoint not available.
# not \retval ::NVAPI_INCOMPATIBLE_STRUCT_VERSION The version of the
# structure passed in is not
# not         compatible with this entrypoint.
# not \retval ::NVAPI_MODE_CHANGE_FAILED  There was an error changing the
# display mode.
# not \retval ::NVAPI_ERROR     Miscellaneous error occurred.
# not
# not \ingroup mosaicapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Mosaic_SetCurrentTopo = hDll.Mosaic_SetCurrentTopo
NvAPI_Mosaic_SetCurrentTopo.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Mosaic_SetCurrentTopo(NV_MOSAIC_TOPO_BRIEF *pTopoBrief, NV_MOSAIC_DISPLAY_SETTING *pDisplaySetting, NvS32 overlapX, NvS32 overlapY, NvU32 enable);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Mosaic_GetCurrentTopo
# not DESCRIPTION:  This API returns information for the current Mosaic
# topology.
# not    This includes topology, display settings, and overlap values.
# not
# not    You can call NvAPI_Mosaic_GetTopoGroup() with the topology
# not    if you require more information.
# not
# not    If there isn't a current topology, then pTopoBrief.topo will
# not    be NV_MOSAIC_TOPO_NONE.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 185
# not
# not \param [out]  pTopoBrief  The current Mosaic topology
# not \param [out]  pDisplaySetting The current per-display settings
# not \param [out]  pOverlapX  The pixel overlap between horizontal
# displays
# not \param [out]  pOverlapY  The pixel overlap between vertical displays
# not
# not \retval ::NVAPI_OK     Success getting current info.
# not \retval ::NVAPI_NOT_SUPPORTED   Mosaic is not supported with the
# existing hardware.
# not \retval ::NVAPI_INVALID_ARGUMENT  One or more argumentss passed in
# are invalid.
# not \retval ::NVAPI_API_NOT_INTIALIZED  The NvAPI API needs to be
# initialized first.
# not \retval ::NVAPI_NO_IMPLEMENTATION   This entry point not available.
# not \retval ::NVAPI_ERROR     Miscellaneous error occurred.
# not
# not \ingroup mosaicapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Mosaic_GetCurrentTopo = hDll.Mosaic_GetCurrentTopo
NvAPI_Mosaic_GetCurrentTopo.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Mosaic_GetCurrentTopo(NV_MOSAIC_TOPO_BRIEF *pTopoBrief, NV_MOSAIC_DISPLAY_SETTING *pDisplaySetting, NvS32 *pOverlapX, NvS32 *pOverlapY);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Mosaic_EnableCurrentTopo
# not DESCRIPTION:  This API enables or disables the current Mosaic
# topology
# not    based on the setting of the incoming 'enable' parameter.
# not
# not    An "enable" setting enables the current (previously set) Mosaic
# topology.
# not    Note that when the current Mosaic topology is retrieved, it must
# have an isPossible value of 1 or
# not    an error will occur.
# not
# not    A "disable" setting disables the current Mosaic topology.
# not    The topology information will persist, even across reboots.
# not    To re-enable the Mosaic topology, call this function
# not    again with the enable parameter set to 1.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 185
# not
# not \param [in] enable   1 to enable the current Mosaic topo, 0 to
# disable it.
# not
# not \retval ::NVAPI_OK    The Mosaic topo was enabled/disabled.
# not \retval ::NVAPI_NOT_SUPPORTED Mosaic is not supported with the
# existing hardware.
# not \retval ::NVAPI_INVALID_ARGUMENT One or more arguments passed in are
# invalid.
# not \retval ::NVAPI_TOPO_NOT_POSSIBLE The current topology is not
# currently possible.
# not \retval ::NVAPI_MODE_CHANGE_FAILED There was an error changing the
# display mode.
# not \retval ::NVAPI_ERROR:   Miscellaneous error occurred.
# not
# not \ingroup mosaicapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Mosaic_EnableCurrentTopo = hDll.Mosaic_EnableCurrentTopo
NvAPI_Mosaic_EnableCurrentTopo.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Mosaic_EnableCurrentTopo(NvU32 enable);

# not \ingroup mosaicapi
# not @{
_NV_MOSAIC_GRID_TOPO_DISPLAY_V1._fields_ = [
    # not < DisplayID of the display
    ('displayId', NvU32),
    # not < ( + overlap, -gap)
    ('overlapX', NvS32),
    # not < ( + overlap, -gap)
    ('overlapY', NvS32),
    # not < Rotation of display
    ('rotation', NV_ROTATE),
    # not < Reserved, must be 0
    ('cloneGroup', NvU32),
]


class _NV_PIXEL_SHIFT_TYPE(ENUM):
    NV_PIXEL_SHIFT_TYPE_NO_PIXEL_SHIFT = 0

    # not < This display will be used to scanout top left pixels in 2x2
    # PixelShift configuration
    NV_PIXEL_SHIFT_TYPE_2x2_TOP_LEFT_PIXELS = 1

    # not < This display will be used to scanout bottom right pixels in
    # 2x2 PixelShift configuration
    NV_PIXEL_SHIFT_TYPE_2x2_BOTTOM_RIGHT_PIXELS = 2

    # not < This display will be used to scanout top right pixels in 2x2
    # PixelShift configuration
    NV_PIXEL_SHIFT_TYPE_2x2_TOP_RIGHT_PIXELS = 4

    # not < This display will be used to scanout bottom left pixels in 2x2
    # PixelShift configuration
    NV_PIXEL_SHIFT_TYPE_2x2_BOTTOM_LEFT_PIXELS = 8


NV_PIXEL_SHIFT_TYPE = _NV_PIXEL_SHIFT_TYPE

_NV_MOSAIC_GRID_TOPO_DISPLAY_V2._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < DisplayID of the display
    ('displayId', NvU32),
    # not < ( + overlap, -gap)
    ('overlapX', NvS32),
    # not < ( + overlap, -gap)
    ('overlapY', NvS32),
    # not < Rotation of display
    ('rotation', NV_ROTATE),
    # not < Reserved, must be 0
    ('cloneGroup', NvU32),
    # not < Type of the pixel shift enabled display
    ('pixelShiftType', NV_PIXEL_SHIFT_TYPE),
]

NV_MOSAIC_GRID_TOPO_DISPLAY = NV_MOSAIC_GRID_TOPO_DISPLAY_V1

_NV_MOSAIC_GRID_TOPO_V1._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < Number of rows
    ('rows', NvU32),
    # not < Number of columns
    ('columns', NvU32),
    # not < Number of display details
    ('displayCount', NvU32),
    # not < When enabling and doing the modeset, do we switch to the
    # bezel-corrected resolution
    ('applyWithBezelCorrect', NvU32, 1),
    # not < Enable as immersive gaming instead of Mosaic SLI
    # (for Quadro-boards only)
    ('immersiveGaming', NvU32, 1),
    # not < Enable as Base Mosaic (Panoramic) instead of Mosaic SLI
    # (for NVS and Quadro-boards only)
    ('baseMosaic', NvU32, 1),
    # not < If necessary, reloading the driver is permitted
    # (for Vista and above only). Will not be persisted. Value undefined
    # on get.
    ('driverReloadAllowed', NvU32, 1),
    # not < Enable SLI acceleration on the primary display while in
    # single-wide mode (For Immersive Gaming only). Will not be persisted.
    # Value undefined on get.
    ('acceleratePrimaryDisplay', NvU32, 1),
    # not < Reserved, must be 0
    ('reserved', NvU32, 27),
    # not < Displays are done as [(row * columns) + column]
    ('displays', NV_MOSAIC_GRID_TOPO_DISPLAY_V1 * NV_MOSAIC_MAX_DISPLAYS),
    # not < Display settings
    ('displaySettings', NV_MOSAIC_DISPLAY_SETTING_V1),
]

_NV_MOSAIC_GRID_TOPO_V2._fields_ = [
    # not < Version of this structure
    ('version', NvU32),
    # not < Number of rows
    ('rows', NvU32),
    # not < Number of columns
    ('columns', NvU32),
    # not < Number of display details
    ('displayCount', NvU32),
    # not < When enabling and doing the modeset, do we switch to the
    # bezel-corrected resolution
    ('applyWithBezelCorrect', NvU32, 1),
    # not < Enable as immersive gaming instead of Mosaic SLI
    # (for Quadro-boards only)
    ('immersiveGaming', NvU32, 1),
    # not < Enable as Base Mosaic (Panoramic) instead of Mosaic SLI
    # (for NVS and Quadro-boards only)
    ('baseMosaic', NvU32, 1),
    # not < If necessary, reloading the driver is permitted
    # (for Vista and above only). Will not be persisted. Value undefined
    # on get.
    ('driverReloadAllowed', NvU32, 1),
    # not < Enable SLI acceleration on the primary display while in
    # single-wide mode (For Immersive Gaming only). Will not be persisted.
    # Value undefined on get.
    ('acceleratePrimaryDisplay', NvU32, 1),
    # not < Enable Pixel shift
    ('pixelShift', NvU32, 1),
    # not < Reserved, must be 0
    ('reserved', NvU32, 26),
    # not < Displays are done as [(row * columns) + column]
    ('displays', NV_MOSAIC_GRID_TOPO_DISPLAY_V2 * NV_MOSAIC_MAX_DISPLAYS),
    # not < Display settings
    ('displaySettings', NV_MOSAIC_DISPLAY_SETTING_V1),
]

# not Macro for constructing the version field of ::NV_MOSAIC_GRID_TOPO
NV_MOSAIC_GRID_TOPO_VER1 = MAKE_NVAPI_VERSION(NV_MOSAIC_GRID_TOPO_V1, 1)
NV_MOSAIC_GRID_TOPO_VER2 = MAKE_NVAPI_VERSION(NV_MOSAIC_GRID_TOPO_V2, 2)
NV_MOSAIC_GRID_TOPO = NV_MOSAIC_GRID_TOPO_V2
# not Macro for constructing the version field of ::NV_MOSAIC_GRID_TOPO
NV_MOSAIC_GRID_TOPO_VER = NV_MOSAIC_GRID_TOPO_VER2

# not @}
# not since Release R290
NV_MOSAIC_DISPLAYCAPS_PROBLEM_DISPLAY_ON_INVALID_GPU = NV_BIT(0)
NV_MOSAIC_DISPLAYCAPS_PROBLEM_DISPLAY_ON_WRONG_CONNECTOR = NV_BIT(1)
NV_MOSAIC_DISPLAYCAPS_PROBLEM_NO_COMMON_TIMINGS = NV_BIT(2)
NV_MOSAIC_DISPLAYCAPS_PROBLEM_NO_EDID_AVAILABLE = NV_BIT(3)
NV_MOSAIC_DISPLAYCAPS_PROBLEM_MISMATCHED_OUTPUT_TYPE = NV_BIT(4)
NV_MOSAIC_DISPLAYCAPS_PROBLEM_NO_DISPLAY_CONNECTED = NV_BIT(5)
NV_MOSAIC_DISPLAYCAPS_PROBLEM_NO_GPU_TOPOLOGY = NV_BIT(6)
NV_MOSAIC_DISPLAYCAPS_PROBLEM_NOT_SUPPORTED = NV_BIT(7)
NV_MOSAIC_DISPLAYCAPS_PROBLEM_NO_SLI_BRIDGE = NV_BIT(8)
NV_MOSAIC_DISPLAYCAPS_PROBLEM_ECC_ENABLED = NV_BIT(9)
NV_MOSAIC_DISPLAYCAPS_PROBLEM_GPU_TOPOLOGY_NOT_SUPPORTED = NV_BIT(10)
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Mosaic_SetDisplayGrids
# not DESCRIPTION:  Sets a new display topology, replacing any existing
# topologies
# not    that use the same displays.
# not
# not    This function will look for an SLI configuration that will
# not    allow the display topology to work.
# not
# not    To revert to a single display, specify that display as a 1x1
# not    grid.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] pGridTopologies The topology details to set.
# not \param [in] gridCount  The number of elements in the pGridTopologies
# array.
# not \param [in] setTopoFlags  Zero or more of the
# NVAPI_MOSAIC_SETDISPLAYTOPO_FLAG_*
# not       flags.
# not
# not
# not \retval ::NVAPI_OK     Capabilities have been returned.
# not \retval ::NVAPI_INVALID_ARGUMENT  One or more args passed in are
# invalid.
# not \retval ::NVAPI_API_NOT_INTIALIZED  The NvAPI API needs to be
# initialized first
# not \retval ::NVAPI_NO_IMPLEMENTATION   This entrypoint not available
# not \retval ::NVAPI_NO_ACTIVE_SLI_TOPOLOGY No matching GPU topologies
# could be found.
# not \retval ::NVAPI_TOPO_NOT_POSSIBLE   One or more of the display grids
# are not valid.
# not \retval ::NVAPI_ERROR     Miscellaneous error occurred
# not \ingroup mosaicapi
# ///////////////////////////////////////////////////////////////////////
# not Do not change the current GPU topology. If the NO_DRIVER_RELOAD bit
# is not
# not specified, then it may still require a driver reload.
NV_MOSAIC_SETDISPLAYTOPO_FLAG_CURRENT_GPU_TOPOLOGY = NV_BIT(0)
# not Do not allow a driver reload. That is, stick with the same master
# GPU as well as the
# not same SLI configuration.
NV_MOSAIC_SETDISPLAYTOPO_FLAG_NO_DRIVER_RELOAD = NV_BIT(1)
# not When choosing a GPU topology, choose the topology with the best
# performance.
# not Without this flag, it will choose the topology that uses the
# smallest number
# not of GPU's.
NV_MOSAIC_SETDISPLAYTOPO_FLAG_MAXIMIZE_PERFORMANCE = NV_BIT(2)
# not Do not return an error if no configuration will work with all of the
# grids.
NV_MOSAIC_SETDISPLAYTOPO_FLAG_ALLOW_INVALID = NV_BIT(3)

NvAPI_Mosaic_SetDisplayGrids = hDll.Mosaic_SetDisplayGrids
NvAPI_Mosaic_SetDisplayGrids.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Mosaic_SetDisplayGrids(__in_ecount(gridCount) NV_MOSAIC_GRID_TOPO *pGridTopologies, __in NvU32 gridCount, __in NvU32 setTopoFlags);

# not \ingroup mosaicapi
# not Indicates that a display's position in the grid is sub-optimal.
NV_MOSAIC_DISPLAYTOPO_WARNING_DISPLAY_POSITION = NV_BIT(0)
# not \ingroup mosaicapi
# not Indicates that SetDisplaySettings would need to perform a driver
# reload.
NV_MOSAIC_DISPLAYTOPO_WARNING_DRIVER_RELOAD_REQUIRED = NV_BIT(1)


# not \ingroup mosaicapi
class displays(ctypes.Structure):
    pass


displays._fields_ = [
    # not < (OUT) The DisplayID of this display.
    ('displayId', NvU32),
    # not < (OUT) Any of the NV_MOSAIC_DISPLAYCAPS_PROBLEM_* flags.
    ('errorFlags', NvU32),
    # not < (OUT) Any of the NV_MOSAIC_DISPLAYTOPO_WARNING_* flags.
    ('warningFlags', NvU32),
    # not < (OUT) This display can be rotated
    ('supportsRotation', NvU32, 1),
    # not < (OUT) reserved
    ('reserved', NvU32, 31),
]
NV_MOSAIC_DISPLAY_TOPO_STATUS.displays = displays

NV_MOSAIC_DISPLAY_TOPO_STATUS._fields_ = [
    ('version', NvU32),
    # not < (OUT) Any of the NV_MOSAIC_DISPLAYTOPO_ERROR_* flags.
    ('errorFlags', NvU32),
    # not < (OUT) Any of the NV_MOSAIC_DISPLAYTOPO_WARNING_* flags.
    ('warningFlags', NvU32),
    # not < (OUT) The number of valid entries in the displays array.
    ('displayCount', NvU32),
    ('displays', NV_MOSAIC_DISPLAY_TOPO_STATUS.displays * NVAPI_MAX_DISPLAYS),
]

# not \ingroup mosaicapi
NV_MOSAIC_DISPLAY_TOPO_STATUS_VER = (
    MAKE_NVAPI_VERSION(NV_MOSAIC_DISPLAY_TOPO_STATUS, 1)
)

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Mosaic_ValidateDisplayGrids
# not DESCRIPTION:  Determines if a list of grid topologies is valid. It
# will choose an SLI
# not    configuration in the same way that NvAPI_Mosaic_SetDisplayGrids()
# does.
# not
# not    On return, each element in the pTopoStatus array will contain any
# errors or
# not    warnings about each grid topology. If any error flags are set,
# then the topology
# not    is not valid. If any warning flags are set, then the topology is
# valid, but
# not    sub-optimal.
# not
# not    If the ALLOW_INVALID flag is set, then it will continue to
# validate the grids
# not    even if no SLI configuration will allow all of the grids. In this
# case, a grid
# not    grid with no matching GPU topology will have the error
# not    flags NO_GPU_TOPOLOGY or NOT_SUPPORTED set.
# not
# not    If the ALLOW_INVALID flag is not set and no matching SLI
# configuration is
# not    found, then it will skip the rest of the validation and return
# not    NVAPI_NO_ACTIVE_SLI_TOPOLOGY.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] setTopoFlags  Zero or more of the
# NVAPI_MOSAIC_SETDISPLAYTOPO_FLAG_*
# not       flags.
# not \param [in] pGridTopologies The array of grid topologies to verify.
# not \param [in,out] pTopoStatus  The array of problems and warnings with
# each grid topology.
# not \param [in] gridCount  The number of elements in the pGridTopologies
# and
# not       pTopoStatus arrays.
# not
# not
# not \retval ::NVAPI_OK:     Capabilities have been returned.
# not \retval ::NVAPI_INVALID_ARGUMENT:  One or more args passed in are
# invalid.
# not \retval ::NVAPI_API_NOT_INTIALIZED:  The NvAPI API needs to be
# initialized first
# not \retval ::NVAPI_NO_IMPLEMENTATION:   This entrypoint not available
# not \retval ::NVAPI_NO_ACTIVE_SLI_TOPOLOGY: No matching GPU topologies
# could be found.
# not \retval ::NVAPI_ERROR:     Miscellaneous error occurred
# not
# not \ingroup mosaicapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Mosaic_ValidateDisplayGrids = hDll.Mosaic_ValidateDisplayGrids
NvAPI_Mosaic_ValidateDisplayGrids.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Mosaic_ValidateDisplayGrids(__in NvU32 setTopoFlags,
#        __in_ecount(gridCount) NV_MOSAIC_GRID_TOPO *pGridTopologies,
#        __inout_ecount_full(gridCount) NV_MOSAIC_DISPLAY_TOPO_STATUS *pTopoStatus,
#        __in NvU32 gridCount);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Mosaic_EnumDisplayModes
# not DESCRIPTION:  Determines the set of available display modes for a
# given grid topology.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] pGridTopology  The grid topology to use.
# not \param [in,out] pDisplaySettings A pointer to an array of display
# settings to populate,
# not        or NULL to find out the total number of available modes.
# not \param [in,out] pDisplayCount  If pDisplaySettings is not NULL, then
# pDisplayCount
# not        should point to the number of elements in the
# not        pDisplaySettings array. On return, it will contain the
# not        number of modes that were actually returned. If
# not        pDisplaySettings is NULL, then pDisplayCount will receive
# not        the total number of modes that are available.
# not
# not
# not \retval ::NVAPI_OK     Capabilities have been returned.
# not \retval ::NVAPI_INVALID_ARGUMENT  One or more args passed in are
# invalid.
# not \retval ::NVAPI_API_NOT_INTIALIZED  The NvAPI API needs to be
# initialized first
# not \retval ::NVAPI_NO_IMPLEMENTATION   This entrypoint not available
# not \retval ::NVAPI_ERROR     Miscellaneous error occurred
# not
# not \ingroup mosaciapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Mosaic_EnumDisplayModes = hDll.Mosaic_EnumDisplayModes
NvAPI_Mosaic_EnumDisplayModes.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Mosaic_EnumDisplayModes(__in NV_MOSAIC_GRID_TOPO *pGridTopology,
#        __inout_ecount_part_opt(*pDisplayCount, *pDisplayCount) NV_MOSAIC_DISPLAY_SETTING *pDisplaySettings,
#        __inout NvU32 *pDisplayCount);


# not SUPPORTED OS: Windows 7 and higher
# not
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Mosaic_EnumDisplayGrids
# not DESCRIPTION:  Enumerates the current active grid topologies. This
# includes Mosaic, IG, and
# not    Panoramic topologies, as well as single displays.
# not
# not    If pGridTopologies is NULL, then pGridCount will be set to the
# number of active
# not    grid topologies.
# not
# not    If pGridTopologies is not NULL, then pGridCount contains the
# maximum number of
# not    grid topologies to return. On return, pGridCount will be set to
# the number of
# not    grid topologies that were returned.
# not
# not \param [out]  pGridTopologies The list of active grid topologies.
# not \param [in,out] pGridCount  A pointer to the number of grid
# topologies returned.
# not
# not \retval ::NVAPI_OK     Capabilties have been returned.
# not \retval ::NVAPI_END_ENUMERATION   There are no more topologies to
# return.
# not \retval ::NVAPI_INVALID_ARGUMENT  One or more args passed in are
# invalid.
# not \retval ::NVAPI_API_NOT_INTIALIZED  The NvAPI API needs to be
# initialized first
# not \retval ::NVAPI_NO_IMPLEMENTATION   This entrypoint not available
# not \retval ::NVAPI_ERROR     Miscellaneous error occurred
# not
# not \ingroup mosaicapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Mosaic_EnumDisplayGrids = hDll.Mosaic_EnumDisplayGrids
NvAPI_Mosaic_EnumDisplayGrids.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Mosaic_EnumDisplayGrids(__inout_ecount_part_opt(*pGridCount, *pGridCount) NV_MOSAIC_GRID_TOPO *pGridTopologies,
#        __inout NvU32 *pGridCount);

# ////////////////////////////////////////////////////////////////////////////////
#
# DELME_RUSS - DELME_RUSS - DELME_RUSS - DELME_RUSS - DELME_RUSS -
# DELME_RUSS
# Below is the Phase 1 Mosaic stuff, the Phase 2 stuff above is what will
# remain
# once Phase 2 is complete. For a small amount of time, the two will
# co-exist. As
# soon as apps (nvapichk, NvAPITestMosaic, and CPL) are updated to use the
# Phase 2
# entrypoints, the code below will be deleted.
# DELME_RUSS - DELME_RUSS - DELME_RUSS - DELME_RUSS - DELME_RUSS -
# DELME_RUSS
#
# Supported topos 1x4, 4x1 and 2x2 to start with.
# Selected scan out targets can be one per GPU or more than one on the
# same GPU.
# SAMPLE of MOSAIC 1x4 SCAN OUT TOPO with 8 pixel horizontal overlap
# + ------------------------- + + ------------------------- + +
# ------------------------- + + ------------------------- +
# |     or     or     or     |
# |     or     or     or     |
# |     or     or     or     |
# |  DVI1   or   DVI2  or  DVI3  or  DVI4  |
# |     or     or     or     |
# |     or     or     or     |
# |     or     or     or     |
# |     or     or     or     |
# + ------------------------- + + ------------------------- + +
# ------------------------- + + ------------------------- +
# not \addtogroup mosaicapi
# not @{
# not Used in NV_MOSAIC_TOPOLOGY.
NVAPI_MAX_MOSAIC_DISPLAY_ROWS = 8
# not Used in NV_MOSAIC_TOPOLOGY.
NVAPI_MAX_MOSAIC_DISPLAY_COLUMNS = 8
# not Used in NV_MOSAIC_TOPOLOGY.
NVAPI_MAX_MOSAIC_TOPOS = 16


# not Used in NvAPI_GetCurrentMosaicTopology() and
# NvAPI_SetCurrentMosaicTopology().
class gpuLayout(ctypes.Structure):
    pass


gpuLayout._fields_ = [
    # not < Physical GPU to be used in the topology
    ('hPhysicalGPU', NvPhysicalGpuHandle),
    # not < Connected display target
    ('displayOutputId', NvU32),
    # not < Pixels of overlap on the left of target: ( + overlap, -gap)
    ('overlapX', NvS32),
    # not < Pixels of overlap on the top of target: ( + overlap, -gap)
    ('overlapY', NvS32),
]
NV_MOSAIC_TOPOLOGY.gpuLayout = gpuLayout

NV_MOSAIC_TOPOLOGY._fields_ = [
    # not < Version number of the mosaic topology
    ('version', NvU32),
    # not < Horizontal display count
    ('rowCount', NvU32),
    # not < Vertical display count
    ('colCount', NvU32),
    ('gpuLayout', (NV_MOSAIC_TOPOLOGY.gpuLayout * NVAPI_MAX_MOSAIC_DISPLAY_ROWS) * NVAPI_MAX_MOSAIC_DISPLAY_COLUMNS),
]
# not Used in NV_MOSAIC_TOPOLOGY.
NVAPI_MOSAIC_TOPOLOGY_VER = MAKE_NVAPI_VERSION(NV_MOSAIC_TOPOLOGY, 1)
# not Used in NvAPI_GetSupportedMosaicTopologies().
NV_MOSAIC_SUPPORTED_TOPOLOGIES._fields_ = [
    ('version', NvU32),
    # not < Count of valid topologies
    ('totalCount', NvU32),
    # not < Maximum number of topologies
    ('topos', NV_MOSAIC_TOPOLOGY * NVAPI_MAX_MOSAIC_TOPOS),
]
# not Used in NV_MOSAIC_SUPPORTED_TOPOLOGIES.
NVAPI_MOSAIC_SUPPORTED_TOPOLOGIES_VER = (
    MAKE_NVAPI_VERSION(NV_MOSAIC_SUPPORTED_TOPOLOGIES, 1)
)
# not @}
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetSupportedMosaicTopologies
# not DESCRIPTION:  This API returns all valid Mosaic topologies.
# not
# not SUPPORTED OS: Windows XP
# not
# not
# not \since Release: 177
# not
# not \param [out] pMosaicTopos    An array of valid Mosaic topologies.
# not
# not \retval NVAPI_OK     Call succeeded; 1 or more topologies were
# returned
# not \retval NVAPI_INVALID_ARGUMENT  One or more arguments are invalid
# not \retval NVAPI_MIXED_TARGET_TYPES  Mosaic topology is only possible
# with all targets of the same NV_GPU_OUTPUT_TYPE.
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND No NVIDIA GPU driving a
# display was found
# not \retval NVAPI_NOT_SUPPORTED  Mosaic is not supported with GPUs on
# this system.
# not \retval NVAPI_NO_ACTIVE_SLI_TOPOLOGY SLI is not enabled, yet needs
# to be, in order for this function to succeed.
# not
# not \ingroup  mosaicapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_GetSupportedMosaicTopologies = hDll.GetSupportedMosaicTopologies
NvAPI_GetSupportedMosaicTopologies.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GetSupportedMosaicTopologies(NV_MOSAIC_SUPPORTED_TOPOLOGIES *pMosaicTopos);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetCurrentMosaicTopology
# not DESCRIPTION:  This API gets the current Mosaic topology.
# not
# not SUPPORTED OS: Windows XP
# not
# not
# not \since Release: 177
# not
# not \param [out] pMosaicTopo    The current Mosaic topology
# not \param [out] pEnabled     TRUE if returned topology is currently
# enabled, else FALSE
# not
# not \retval NVAPI_OK     Call succeeded
# not \retval NVAPI_INVALID_ARGUMENT  One or more arguments are invalid
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND No NVIDIA GPU driving a
# display was found
# not \retval NVAPI_NOT_SUPPORTED  Mosaic is not supported with GPUs on
# this system.
# not \retval NVAPI_NO_ACTIVE_SLI_TOPOLOGY SLI is not enabled, yet needs
# to be, in order for this function to succeed.
# not
# not \ingroup  mosaicapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_GetCurrentMosaicTopology = hDll.GetCurrentMosaicTopology
NvAPI_GetCurrentMosaicTopology.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GetCurrentMosaicTopology(NV_MOSAIC_TOPOLOGY *pMosaicTopo, NvU32 *pEnabled);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_SetCurrentMosaicTopology
# not DESCRIPTION:  This API sets the Mosaic topology, and enables it so
# that the
# not    Mosaic display settings are enumerated upon request.
# not
# not SUPPORTED OS: Windows XP
# not
# not
# not \since Release: 177
# not
# not \param [in] pMosaicTopo    A valid Mosaic topology
# not
# not \retval NVAPI_OK     Call succeeded
# not \retval NVAPI_INVALID_ARGUMENT  One or more arguments are invalid
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND No NVIDIA GPU driving a
# display was found
# not \retval NVAPI_NOT_SUPPORTED  Mosaic is not supported with GPUs on
# this system.
# not \retval NVAPI_NO_ACTIVE_SLI_TOPOLOGY SLI is not enabled, yet needs
# to be, in order for this function to succeed.
# not
# not \ingroup  mosaicapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_SetCurrentMosaicTopology = hDll.SetCurrentMosaicTopology
NvAPI_SetCurrentMosaicTopology.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_SetCurrentMosaicTopology(NV_MOSAIC_TOPOLOGY *pMosaicTopo);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_EnableCurrentMosaicTopology
# not DESCRIPTION: This API enables or disables the current Mosaic
# topology.
# not   When enabling, the last Mosaic topology will be set.
# not
# not    - If enabled, enumeration of display settings will include valid
# Mosaic resolutions.
# not    - If disabled, enumeration of display settings will not include
# Mosaic resolutions.
# not
# not SUPPORTED OS: Windows XP
# not
# not
# not \since Release: 177
# not
# not \param [in] enable     TRUE to enable the Mosaic Topology, FALSE to
# disable it.
# not
# not \retval NVAPI_OK     Call succeeded
# not \retval NVAPI_INVALID_ARGUMENT  One or more arguments are invalid
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND No NVIDIA GPU driving a
# display was found
# not \retval NVAPI_NOT_SUPPORTED  Mosaic is not supported with GPUs on
# this system.
# not \retval NVAPI_NO_ACTIVE_SLI_TOPOLOGY SLI is not enabled, yet needs
# to be, in order for this function to succeed.
# not
# not \ingroup  mosaicapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_EnableCurrentMosaicTopology = hDll.EnableCurrentMosaicTopology
NvAPI_EnableCurrentMosaicTopology.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_EnableCurrentMosaicTopology(NvU32 enable);


NVAPI_MAX_GSYNC_DEVICES = 4

# Sync Display APIs
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GSync_EnumSyncDevices
# not DESCRIPTION: This API returns an array of Sync device handles. A
# Sync device handle represents a
# not    single Sync device on the system.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 313
# not
# not \param [out] nvGSyncHandles- The caller provides an array of
# handles, which must contain at least
# not      NVAPI_MAX_GSYNC_DEVICES elements. The API will zero out the
# entire array and then fill in one
# not      or more handles. If an error occurs, the array is invalid.
# not \param [out] *gsyncCount-  The caller provides the storage space.
# NvAPI_GSync_EnumSyncDevices
# not      sets *gsyncCount to indicate how many of the elements in the
# nvGSyncHandles[] array are valid.
# not      If an error occurs, *gsyncCount will be set to zero.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   If there are return error codes with specific meaning for this
# API, they are listed below.
# not \retval ::NVAPI_INVALID_ARGUMENT  nvGSyncHandles or gsyncCount is
# NULL.
# not \retval ::NVAPI_NVIDIA_DEVICE_NOT_FOUND The queried Graphics system
# does not have any Sync Device.
# not
# not \ingroup gsyncapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_GSync_EnumSyncDevices = hDll.GSync_EnumSyncDevices
NvAPI_GSync_EnumSyncDevices.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GSync_EnumSyncDevices(__out NvGSyncDeviceHandle nvGSyncHandles[NVAPI_MAX_GSYNC_DEVICES], __out NvU32 *gsyncCount);

# GSync boardId values
# not < GSync board ID 0x358, see NV_GSYNC_CAPABILITIES
NVAPI_GSYNC_BOARD_ID_P358 = 856

# not < GSync board ID 0x2060, see NV_GSYNC_CAPABILITIES
NVAPI_GSYNC_BOARD_ID_P2060 = 8288

# not \since Release: 375
# not < GSync board ID 0x2061, see NV_GSYNC_CAPABILITIES
NVAPI_GSYNC_BOARD_ID_P2061 = 8289

# not Used in NvAPI_GSync_QueryCapabilities().
_NV_GSYNC_CAPABILITIES_V1._fields_ = [
    # not < Version of the structure
    ('version', NvU32),
    # not < Board ID
    ('boardId', NvU32),
    # not < FPGA Revision
    ('revision', NvU32),
    # not < Capabilities of the Sync board. Reserved for future use
    ('capFlags', NvU32),
]

_NV_GSYNC_CAPABILITIES_V2._fields_ = [
    # not < Version of the structure
    ('version', NvU32),
    # not < Board ID
    ('boardId', NvU32),
    # not < FPGA major revision
    ('revision', NvU32),
    # not < Capabilities of the Sync board. Reserved for future use
    ('capFlags', NvU32),
    # not < FPGA minor revision
    ('extendedRevision', NvU32),
]
NV_GSYNC_CAPABILITIES = NV_GSYNC_CAPABILITIES_V2

# not \ingroup gsyncapi
# not Macro for constructing the version field of NV_GSYNC_CAPABILITIES.
NV_GSYNC_CAPABILITIES_VER1 = (
    MAKE_NVAPI_VERSION(NV_GSYNC_CAPABILITIES_V1, 1)
)
NV_GSYNC_CAPABILITIES_VER2 = (
    MAKE_NVAPI_VERSION(NV_GSYNC_CAPABILITIES_V2, 2)
)
NV_GSYNC_CAPABILITIES_VER = NV_GSYNC_CAPABILITIES_VER2

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GSync_QueryCapabilities
# not DESCRIPTION: This API returns the capabilities of the Sync device.
# not
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 313
# not
# not \param [in] hNvGSyncDevice-  The handle for a Sync device for which
# the capabilities will be queried.
# not \param [inout] *pNvGSyncCapabilities- The caller provides the
# storage space. NvAPI_GSync_QueryCapabilities() sets
# not       *pNvGSyncCapabilities to the version and capabilities details
# of the Sync device
# not       If an error occurs, *pNvGSyncCapabilities will be set to NULL.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   If there are return error codes with specific meaning for this
# API, they are listed below.
# not \retval ::NVAPI_INVALID_ARGUMENT  hNvGSyncDevice is NULL.
# not \retval ::NVAPI_NVIDIA_DEVICE_NOT_FOUND The queried Graphics system
# does not have any Sync Device.
# not
# not \ingroup gsyncapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_GSync_QueryCapabilities = hDll.GSync_QueryCapabilities
NvAPI_GSync_QueryCapabilities.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GSync_QueryCapabilities(__in NvGSyncDeviceHandle hNvGSyncDevice, __inout NV_GSYNC_CAPABILITIES *pNvGSyncCapabilities);

# not Connector values for a GPU. Used in NV_GSYNC_GPU.


class _NVAPI_GSYNC_GPU_TOPOLOGY_CONNECTOR(ENUM):
    NVAPI_GSYNC_GPU_TOPOLOGY_CONNECTOR_NONE = 0
    NVAPI_GSYNC_GPU_TOPOLOGY_CONNECTOR_PRIMARY = 1
    NVAPI_GSYNC_GPU_TOPOLOGY_CONNECTOR_SECONDARY = 2
    NVAPI_GSYNC_GPU_TOPOLOGY_CONNECTOR_TERTIARY = 3
    NVAPI_GSYNC_GPU_TOPOLOGY_CONNECTOR_QUARTERNARY = 4


NVAPI_GSYNC_GPU_TOPOLOGY_CONNECTOR = _NVAPI_GSYNC_GPU_TOPOLOGY_CONNECTOR


# not Display sync states. Used in NV_GSYNC_DISPLAY.
class _NVAPI_GSYNC_DISPLAY_SYNC_STATE(ENUM):
    NVAPI_GSYNC_DISPLAY_SYNC_STATE_UNSYNCED = 0
    NVAPI_GSYNC_DISPLAY_SYNC_STATE_SLAVE = 1
    NVAPI_GSYNC_DISPLAY_SYNC_STATE_MASTER = 2


NVAPI_GSYNC_DISPLAY_SYNC_STATE = _NVAPI_GSYNC_DISPLAY_SYNC_STATE

_NV_GSYNC_GPU._fields_ = [
    # not < Version of the structure
    ('version', NvU32),
    # not < GPU handle
    ('hPhysicalGpu', NvPhysicalGpuHandle),
    # not < Indicates which connector on the device the GPU is connected
    # to.
    ('connector', NVAPI_GSYNC_GPU_TOPOLOGY_CONNECTOR),
    # not < GPU through which hPhysicalGpu is connected to the Sync device
    # (if not directly connected)
    ('hProxyPhysicalGpu', NvPhysicalGpuHandle),
    # not < Whether this GPU is sync'd or not.
    ('isSynced', NvU32, 1),
    # not < Should be set to ZERO
    ('reserved', NvU32, 31),
]

_NV_GSYNC_DISPLAY._fields_ = [
    # not < Version of the structure
    ('version', NvU32),
    # not < display identifier for displays.The GPU to which it is
    # connected, can be retireved from
    # NvAPI_SYS_GetPhysicalGpuFromDisplayId
    ('displayId', NvU32),
    # not < Can this display be the master? (Read only)
    ('isMasterable', NvU32, 1),
    # not < Should be set to ZERO
    ('reserved', NvU32, 31),
    # not < Is this display slave/master
    ('syncState', NVAPI_GSYNC_DISPLAY_SYNC_STATE),
]
NV_GSYNC_DISPLAY_VER = MAKE_NVAPI_VERSION(NV_GSYNC_DISPLAY, 1)
NV_GSYNC_GPU_VER = MAKE_NVAPI_VERSION(NV_GSYNC_GPU, 1)

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GSync_GetTopology
# not DESCRIPTION: This API returns the topology for the specified Sync
# device.
# not
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 313
# not
# not \param [in]  hNvGSyncDevice-  The caller provides the handle for a
# Sync device for which the topology will be queried.
# not \param [in, out] gsyncGpuCount- It returns number of GPUs connected
# to Sync device
# not \param [in, out] gsyncGPUs-  It returns info about GPUs connected to
# Sync device
# not \param [in, out] gsyncDisplayCount- It returns number of active
# displays that belongs to Sync device
# not \param [in, out] gsyncDisplays- It returns info about all active
# displays that belongs to Sync device
# not
# not HOW TO USE:
# 1) make a call to get the number of GPUs connected OR displays synced through Sync device
#
# not    by passing the gsyncGPUs OR gsyncDisplays as NULL respectively.
# Both gsyncGpuCount and gsyncDisplayCount can be retrieved in same call
# by passing
# not    both gsyncGPUs and gsyncDisplays as NULL
# not    On call success:
# not   2) Allocate memory based on gsyncGpuCount(for
# gsyncGPUs) and/or gsyncDisplayCount(for
# gsyncDisplays) then make a call to populate gsyncGPUs and/or gsyncDisplays respectively.
#
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   If there are return error codes with specific meaning for this
# API, they are listed below.
# not \retval ::NVAPI_INVALID_ARGUMENT   hNvGSyncDevice is NULL.
# not \retval ::NVAPI_NVIDIA_DEVICE_NOT_FOUND  The queried Graphics system
# does not have any Sync Device.
# not \retval ::NVAPI_INSUFFICIENT_BUFFER  When the actual number of
# GPUs/displays in the topology exceed the number of elements allocated
# for SyncGPUs/SyncDisplays respectively.
# not
# not \ingroup gsyncapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_GSync_GetTopology = hDll.GSync_GetTopology
NvAPI_GSync_GetTopology.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GSync_GetTopology(__in NvGSyncDeviceHandle hNvGSyncDevice, __inout_opt NvU32 *gsyncGpuCount,  __inout_ecount_part_opt(*gsyncGpuCount, *gsyncGpuCount) NV_GSYNC_GPU *gsyncGPUs,
#                                        __inout_opt NvU32 *gsyncDisplayCount, __inout_ecount_part_opt(*gsyncDisplayCount, *gsyncDisplayCount) NV_GSYNC_DISPLAY *gsyncDisplays);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GSync_SetSyncStateSettings
# not DESCRIPTION: Sets a new sync state for the displays in system.
# not
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 313
# not
# not \param [in] gsyncDisplayCount-  The number of displays in
# gsyncDisplays.
# not \param [in] pGsyncDisplays-  The caller provides the structure
# containing all displays that need to be synchronized in the system.
# not        The displays that are not part of pGsyncDisplays, will be
# un-synchronized.
# not \param [in] flags-    Reserved for future use.
# not
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   If there are return error codes with specific meaning for this
# API, they are listed below.
# not
# not \retval ::NVAPI_INVALID_ARGUMENT  If the display topology or count
# not valid.
# not \retval ::NVAPI_NVIDIA_DEVICE_NOT_FOUND  The queried Graphics system
# does not have any Sync Device.
# not \retval ::NVAPI_INVALID_SYNC_TOPOLOGY  1.If any mosaic grid is
# partial.
# not        2.If timing(HVisible/VVisible/refreshRate) applied of any
# display is different.
# not        3.If There is a across GPU mosaic grid in system and that is
# not a part of pGsyncDisplays.
# not
# not \ingroup gsyncapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_GSync_SetSyncStateSettings = hDll.GSync_SetSyncStateSettings
NvAPI_GSync_SetSyncStateSettings.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GSync_SetSyncStateSettings(__in NvU32 gsyncDisplayCount, __in_ecount(gsyncDisplayCount) NV_GSYNC_DISPLAY *pGsyncDisplays, __in NvU32 flags);

# not \ingroup gsyncapi
# not Source signal edge to be used for output pulse. See
# NV_GSYNC_CONTROL_PARAMS.
class _NVAPI_GSYNC_POLARITY(ENUM):
    NVAPI_GSYNC_POLARITY_RISING_EDGE = 0
    NVAPI_GSYNC_POLARITY_FALLING_EDGE = 1
    NVAPI_GSYNC_POLARITY_BOTH_EDGES = 2


NVAPI_GSYNC_POLARITY = _NVAPI_GSYNC_POLARITY


# not Used in NV_GSYNC_CONTROL_PARAMS.
class _NVAPI_GSYNC_VIDEO_MODE(ENUM):
    NVAPI_GSYNC_VIDEO_MODE_NONE = 0
    NVAPI_GSYNC_VIDEO_MODE_TTL = 1
    NVAPI_GSYNC_VIDEO_MODE_NTSCPALSECAM = 2
    NVAPI_GSYNC_VIDEO_MODE_HDTV = 3
    NVAPI_GSYNC_VIDEO_MODE_COMPOSITE = 4


NVAPI_GSYNC_VIDEO_MODE = _NVAPI_GSYNC_VIDEO_MODE


# not Used in NV_GSYNC_CONTROL_PARAMS.
class _NVAPI_GSYNC_SYNC_SOURCE(ENUM):
    NVAPI_GSYNC_SYNC_SOURCE_VSYNC = 0
    NVAPI_GSYNC_SYNC_SOURCE_HOUSESYNC = 1


NVAPI_GSYNC_SYNC_SOURCE = _NVAPI_GSYNC_SYNC_SOURCE

# not Used in NV_GSYNC_CONTROL_PARAMS.
_NV_GSYNC_DELAY._fields_ = [
    # not < Version of the structure
    ('version', NvU32),
    # not < delay to be induced in number of horizontal lines.
    ('numLines', NvU32),
    # not < delay to be induced in number of pixels.
    ('numPixels', NvU32),
    # not < maximum number of lines supported at current display mode to
    # induce delay. Updated by NvAPI_GSync_GetControlParameters(). Read
    # only.
    ('maxLines', NvU32),
    # not < minimum number of pixels required at current display mode to
    # induce delay. Updated by NvAPI_GSync_GetControlParameters(). Read
    # only.
    ('minPixels', NvU32),
]
NV_GSYNC_DELAY_VER = MAKE_NVAPI_VERSION(NV_GSYNC_DELAY, 1)

# not Used in NvAPI_GSync_GetControlParameters() and
# NvAPI_GSync_SetControlParameters().
_NV_GSYNC_CONTROL_PARAMS._fields_ = [
    # not < Version of the structure
    ('version', NvU32),
    # not < Leading edge / Falling edge / both
    ('polarity', NVAPI_GSYNC_POLARITY),
    # not < None, TTL, NTSCPALSECAM, HDTV
    ('vmode', NVAPI_GSYNC_VIDEO_MODE),
    # not < Number of pulses to wait between framelock signal generation
    ('interval', NvU32),
    # not < VSync/House sync
    ('source', NVAPI_GSYNC_SYNC_SOURCE),
    # not < interlace mode for a Sync device
    ('interlaceMode', NvU32, 1),
    # not < Set this to make house sync as an output; valid only when
    # NV_GSYNC_CONTROL_PARAMS::source is NVAPI_GSYNC_SYNC_SOURCE_VSYNC on
    # P2061 boards.
    ('syncSourceIsOutput', NvU32, 1),
    # not < should be set zero
    ('reserved', NvU32, 30),
    # not < The time delay between the frame sync signal and the GPUs
    # signal.
    ('syncSkew', NV_GSYNC_DELAY),
    # not < Sync start delay for master.
    ('startupDelay', NV_GSYNC_DELAY),
]
NV_GSYNC_CONTROL_PARAMS_VER = (
    MAKE_NVAPI_VERSION(NV_GSYNC_CONTROL_PARAMS, 1)
)

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GSync_GetControlParameters
# not DESCRIPTION: This API queries for sync control parameters as defined
# in NV_GSYNC_CONTROL_PARAMS.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 313
# not
# not \param [in] hNvGSyncDevice- The caller provides the handle of the
# Sync device for which to get parameters
# not \param [inout] *pGsyncControls- The caller provides the storage
# space. NvAPI_GSync_GetControlParameters() populates *pGsyncControls with
# values.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   If there are return error codes with specific meaning for this
# API, they are listed below.
# not \retval ::NVAPI_INVALID_ARGUMENT  hNvGSyncDevice is NULL.
# not \retval ::NVAPI_NVIDIA_DEVICE_NOT_FOUND The queried Graphics system
# does not have any Sync Device.
# not
# not \ingroup gsyncapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_GSync_GetControlParameters = hDll.GSync_GetControlParameters
NvAPI_GSync_GetControlParameters.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GSync_GetControlParameters(__in NvGSyncDeviceHandle hNvGSyncDevice, __inout NV_GSYNC_CONTROL_PARAMS *pGsyncControls);

# //////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GSync_SetControlParameters
# not DESCRIPTION: This API sets control parameters as defined in
# NV_SYNC_CONTROL_PARAMS.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 313
# not
# not \param [in] hNvGSyncDevice- The caller provides the handle of the
# Sync device for which to get parameters
# not \param [inout] *pGsyncControls- The caller provides
# NV_GSYNC_CONTROL_PARAMS. skew and startDelay will be updated to the
# applied values.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   If there are return error codes with specific meaning for this
# API, they are listed below.
# not \retval ::NVAPI_INVALID_ARGUMENT  hNvGSyncDevice is NULL.
# not \retval ::NVAPI_NVIDIA_DEVICE_NOT_FOUND The queried Graphics system
# does not have any Sync Device.
# not \retval ::NVAPI_SYNC_MASTER_NOT_FOUND  Control Parameters can only
# be set if there is a Sync Master enabled on the Gsync card.
# not
# not \ingroup gsyncapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_GSync_SetControlParameters = hDll.GSync_SetControlParameters
NvAPI_GSync_SetControlParameters.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_GSync_SetControlParameters(__in NvGSyncDeviceHandle hNvGSyncDevice, __inout NV_GSYNC_CONTROL_PARAMS *pGsyncControls);


# not Used in NvAPI_GSync_AdjustSyncDelay()
class _NVAPI_GSYNC_DELAY_TYPE(ENUM):
    NVAPI_GSYNC_DELAY_TYPE_UNKNOWN = 0
    NVAPI_GSYNC_DELAY_TYPE_SYNC_SKEW = 1
    NVAPI_GSYNC_DELAY_TYPE_STARTUP = 2


NVAPI_GSYNC_DELAY_TYPE = _NVAPI_GSYNC_DELAY_TYPE

# //////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GSync_AdjustSyncDelay
# not DESCRIPTION: This API adjusts the skew and startDelay to the closest
# possible values. Use this API before calling
# NvAPI_GSync_SetControlParameters for skew or startDelay.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 319
# not
# not \param [in] hNvGSyncDevice-  The caller provides the handle of the
# Sync device for which to get parameters
# not \param [in] delayType-   Specifies whether the delay is syncSkew or
# startupDelay.
# not \param [inout] *pGsyncDelay- The caller provides NV_GSYNC_DELAY.
# skew and startDelay will be adjusted and updated to the closest values.
# not \param [out] *syncSteps-  This parameter is optional. It returns the
# sync delay in unit steps. If 0, it means either the
# NV_GSYNC_DELAY::numPixels is less than NV_GSYNC_DELAY::minPixels or
# NV_GSYNC_DELAY::numOfLines exceeds the NV_GSYNC_DELAY::maxLines.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   If there are return error codes with specific meaning for this
# API, they are listed below.
# not
# not \ingroup gsyncapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_GSync_AdjustSyncDelay = hDll.GSync_AdjustSyncDelay
NvAPI_GSync_AdjustSyncDelay.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GSync_AdjustSyncDelay(__in NvGSyncDeviceHandle hNvGSyncDevice, __in NVAPI_GSYNC_DELAY_TYPE delayType, __inout NV_GSYNC_DELAY *pGsyncDelay, __out_opt NvU32* syncSteps);


# not Used in NvAPI_GSync_GetSyncStatus().
_NV_GSYNC_STATUS._fields_ = [
    # not < Version of the structure
    ('version', NvU32),
    # not < Is timing in sync?
    ('bIsSynced', NvU32),
    # not < Does the phase of the timing signal from the GPU = the phase
    # of the master sync signal?
    ('bIsStereoSynced', NvU32),
    # not < Is the sync signal available?
    ('bIsSyncSignalAvailable', NvU32),
]

# not Macro for constructing the version field for NV_GSYNC_STATUS.
NV_GSYNC_STATUS_VER = MAKE_NVAPI_VERSION(NV_GSYNC_STATUS, 1)

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GSync_GetSyncStatus
# not DESCRIPTION: This API queries the sync status of a GPU - timing,
# stereosync and sync signal availability.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 313
# not
# not \param [in] hNvGSyncDevice-  Handle of the Sync device
# not \param [in] hPhysicalGpu-  GPU to be queried for sync status.
# not \param [out] *status-  The caller provides the storage space.
# NvAPI_GSync_GetSyncStatus() populates *status with
# not       values - timing, stereosync and signal availability. On error,
# *status is set to NULL.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   If there are return error codes with specific meaning for this
# API, they are listed below.
# not \retval ::NVAPI_INVALID_ARGUMENT  hNvGSyncDevice is NULL /
# SyncTarget is NULL.
# not \retval ::NVAPI_NVIDIA_DEVICE_NOT_FOUND The queried Graphics system
# does not have any G-Sync Device.
# not
# not \ingroup gsyncapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_GSync_GetSyncStatus = hDll.GSync_GetSyncStatus
NvAPI_GSync_GetSyncStatus.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GSync_GetSyncStatus(__in NvGSyncDeviceHandle hNvGSyncDevice, __in NvPhysicalGpuHandle hPhysicalGpu, __inout NV_GSYNC_STATUS *status);


# not \ingroup gsyncapi
NVAPI_MAX_RJ45_PER_GSYNC = 2


# not Used in NV_GSYNC_STATUS_PARAMS.
class _NVAPI_GSYNC_RJ45_IO(ENUM):
    NVAPI_GSYNC_RJ45_OUTPUT = 0
    NVAPI_GSYNC_RJ45_INPUT = 1

    # not < This field is used to notify that the framelock is not
    # actually present.
    NVAPI_GSYNC_RJ45_UNUSED = 2


NVAPI_GSYNC_RJ45_IO = _NVAPI_GSYNC_RJ45_IO

# not \ingroup gsyncapi
# not Used in NvAPI_GSync_GetStatusParameters().
_NV_GSYNC_STATUS_PARAMS_V1._fields_ = [
    ('version', NvU32),
    # not < The refresh rate
    ('refreshRate', NvU32),
    # not < Configured as input / output
    ('RJ45_IO', NVAPI_GSYNC_RJ45_IO * NVAPI_MAX_RJ45_PER_GSYNC),
    # not < Connected to ethernet hub? [ERRONEOUSLY CONNECTEDnot ]
    ('RJ45_Ethernet', NvU32 * NVAPI_MAX_RJ45_PER_GSYNC),
    # not < Incoming house sync frequency in Hz
    ('houseSyncIncoming', NvU32),
    # not < Is house sync connected?
    ('bHouseSync', NvU32),
]

_NV_GSYNC_STATUS_PARAMS_V2._fields_ = [
    ('version', NvU32),
    # not < The refresh rate
    ('refreshRate', NvU32),
    # not < Configured as input / output
    ('RJ45_IO', NVAPI_GSYNC_RJ45_IO * NVAPI_MAX_RJ45_PER_GSYNC),
    # not < Connected to ethernet hub? [ERRONEOUSLY CONNECTEDnot ]
    ('RJ45_Ethernet', NvU32 * NVAPI_MAX_RJ45_PER_GSYNC),
    # not < Incoming house sync frequency in Hz
    ('houseSyncIncoming', NvU32),
    # not < Is house sync connected?
    ('bHouseSync', NvU32),
    # not < Valid only for P2061 board.
    ('bInternalSlave', NvU32, 1),
    # not < Reserved for future use.
    ('reserved', NvU32, 31),
]
NV_GSYNC_STATUS_PARAMS = NV_GSYNC_STATUS_PARAMS_V2

# not \ingroup gsyncapi
# not Macro for constructing the version field of NV_GSYNC_STATUS_PARAMS
NV_GSYNC_STATUS_PARAMS_VER1 = (
    MAKE_NVAPI_VERSION(NV_GSYNC_STATUS_PARAMS_V1, 1)
)
NV_GSYNC_STATUS_PARAMS_VER2 = (
    MAKE_NVAPI_VERSION(NV_GSYNC_STATUS_PARAMS_V2, 2)
)
NV_GSYNC_STATUS_PARAMS_VER = NV_GSYNC_STATUS_PARAMS_VER2

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GSync_GetStatusParameters
# not DESCRIPTION: This API queries for sync status parameters as defined
# in NV_GSYNC_STATUS_PARAMS.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 313
# not
# not \param [in] hNvGSyncDevice The caller provides the handle of the
# GSync device for which to get parameters
# not \param [out] *pStatusParams The caller provides the storage space.
# NvAPI_GSync_GetStatusParameters populates *pStatusParams with
# not      values.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   If there are return error codes with specific meaning for this
# API, they are listed below.
# not \retval ::NVAPI_INVALID_ARGUMENT  hNvGSyncDevice is NULL /
# pStatusParams is NULL.
# not \retval ::NVAPI_NVIDIA_DEVICE_NOT_FOUND  The queried Graphics system
# does not have any GSync Device.
# not
# not \ingroup gsyncapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_GSync_GetStatusParameters = hDll.GSync_GetStatusParameters
NvAPI_GSync_GetStatusParameters.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GSync_GetStatusParameters(NvGSyncDeviceHandle hNvGSyncDevice, NV_GSYNC_STATUS_PARAMS *pStatusParams);


# not @}
# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D9_RegisterResource
# not DESCRIPTION: This API binds a resource (surface/texture) so that
# it can be retrieved
# not   internally by NVAPI.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not \param [in]  pResource surface/texture
# not
# not \return ::NVAPI_OK, ::NVAPI_ERROR
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D9_RegisterResource = hDll.D3D9_RegisterResource
NvAPI_D3D9_RegisterResource.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D9_RegisterResource(IDirect3DResource9* pResource);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D9_UnregisterResource
# not DESCRIPTION:  This API unbinds a resource (surface/texture)
# after use.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  pResource surface/texture
# not
# not \return ::NVAPI_OK, ::NVAPI_ERROR
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D9_UnregisterResource = hDll.D3D9_UnregisterResource
NvAPI_D3D9_UnregisterResource.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_D3D9_UnregisterResource(IDirect3DResource9* pResource);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D9_AliasSurfaceAsTexture
# not \fn NvAPI_D3D9_AliasSurfaceAsTexture(IDirect3DDevice9* pDev,
# not         IDirect3DSurface9* pSurface,
# not         IDirect3DTexture9 **ppTexture,
# not         DWORD dwFlag);
# not DESCRIPTION: Create a texture that is an alias of a surface
# registered with NvAPI. The
# not    new texture can be bound with IDirect3DDevice9::SetTexture().
# Note that the texture must
# not    be unbound before drawing to the surface again.
# not    Unless the USE_SUPER flag is passed, MSAA surfaces will be
# resolved before
# not    being used as a texture. MSAA depth buffers are resolved with
# a point filter,
# not    and non-depth MSAA surfaces are resolved with a linear filter.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] pDev  The D3D device that owns the objects
# not \param [in] pSurface  Pointer to a surface that has been
# registered with NvAPI
# not     to which a texture alias is to be provided
# not \param [out] ppTexture Fill with the texture created
# not \param [in] dwFlag  NVAPI_ALIAS_SURFACE_FLAG to describe how to
# handle the texture
# not
# not \retval ::NVAPI_OK   completed request
# not \retval ::NVAPI_INVALID_POINTER  A null pointer was passed as an
# argument
# not \retval ::NVAPI_INVALID_ARGUMENT One of the arguments was
# invalid, probably dwFlag.
# not \retval ::NVAPI_UNREGISTERED_RESOURCE pSurface has not been
# registered with NvAPI
# not \retval ::NVAPI_ERROR   error occurred
# ///////////////////////////////////////////////////////////////////
# not \ingroup dx
# not See NvAPI_D3D9_AliasSurfaceAsTexture().
class NVAPI_ALIAS_SURFACE_FLAG(ENUM):
    NVAPI_ALIAS_SURFACE_FLAG_NONE = 0x00000000

    # not < Use the surface's msaa buffer directly as a texture,
    # rather than resolving.
    # (This is much slower, but potentially has higher quality.)
    NVAPI_ALIAS_SURFACE_FLAG_USE_SUPER = 0x00000001
    NVAPI_ALIAS_SURFACE_FLAG_MASK = 0x00000001


NVAPI_ALIAS_SURFACE_FLAG_NONE = NVAPI_ALIAS_SURFACE_FLAG.NVAPI_ALIAS_SURFACE_FLAG_NONE
NVAPI_ALIAS_SURFACE_FLAG_USE_SUPER = NVAPI_ALIAS_SURFACE_FLAG.NVAPI_ALIAS_SURFACE_FLAG_USE_SUPER
NVAPI_ALIAS_SURFACE_FLAG_MASK = NVAPI_ALIAS_SURFACE_FLAG.NVAPI_ALIAS_SURFACE_FLAG_MASK

NvAPI_D3D9_AliasSurfaceAsTexture = hDll.D3D9_AliasSurfaceAsTexture
NvAPI_D3D9_AliasSurfaceAsTexture.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D9_AliasSurfaceAsTexture(IDirect3DDevice9* pDev,
#                                                 IDirect3DSurface9* pSurface,
#                                                 IDirect3DTexture9 **ppTexture,
#                                                 DWORD dwFlag);

# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D9_StretchRectEx
# not DESCRIPTION:  This API copies the contents of the source
# resource to the destination
# not    resource. This function can convert
# not    between a wider range of surfaces than
# not    IDirect3DDevice9::StretchRect. For example, it can copy
# not    from a depth/stencil surface to a texture.
# not
# not    The source and destination resources *must* be registered
# not    with NvAPI before being used with NvAPI_D3D9_StretchRectEx().
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  pDevice   The D3D device that owns the objects.
# not \param [in]  pSourceResource  Pointer to the source resource.
# not \param [in]  pSrcRect  Defines the rectangle on the source to
# copy from. If NULL, copy from the entire resource.
# not \param [in]  pDestResource  Pointer to the destination resource.
# not \param [in]  pDstRect  Defines the rectangle on the destination
# to copy to. If NULL, copy to the entire resource.
# not \param [in]  Filter   Choose a filtering method: D3DTEXF_NONE,
# D3DTEXF_POINT, D3DTEXF_LINEAR.
# not
# not \retval ::NVAPI_OK     completed request
# not \retval ::NVAPI_INVALID_POINTER  An invalid pointer was passed
# as an argument (probably NULL)
# not \retval ::NVAPI_INVALID_ARGUMENT  One of the arguments was
# invalid
# not \retval ::NVAPI_UNREGISTERED_RESOURCE a resource was passed in
# without being registered
# not \retval ::NVAPI_ERROR    error occurred
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D9_StretchRectEx = hDll.D3D9_StretchRectEx
NvAPI_D3D9_StretchRectEx.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D9_StretchRectEx(IDirect3DDevice9 * pDevice,
#                                         IDirect3DResource9 * pSourceResource,
#                                         CONST RECT * pSourceRect,
#                                         IDirect3DResource9 * pDestResource,
#                                         CONST RECT * pDestRect,
#                                         D3DTEXTUREFILTERTYPE Filter);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D9_ClearRT
# not DESCRIPTION:  This API Clears the currently bound render
# target(s) with the
# not    given color
# not
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  pDevice   The D3D device that owns the objects.
# not \param [in]  dwNumRects  The no of rectangles to clear. If 0,
# clear the entire surface (clipped to viewport)
# not \param [in]  pRects   Defines the rectangles to clear. Should be
# NULL if dwNumRects == 0
# not \param [in]  r    red component of the clear color
# not \param [in]  g    green component of the clear color
# not \param [in]  b    blue component of the clear color
# not \param [in]  a    alpha component of the clear color
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D9_ClearRT = hDll.D3D9_ClearRT
NvAPI_D3D9_ClearRT.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D9_ClearRT(IDirect3DDevice9 * pDevice,
#                                    NvU32 dwNumRects,
#                                    CONST RECT * pRects,
#                                    float r, float g, float b, float a);

# not SUPPORTED OS: Windows 7 and higher
# not
# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D9_GetSurfaceHandle
# not This function gets the handle of a given surface. This handle
# uniquely
# not identifies the surface through all NvAPI entries.
# not
# not
# not \since Release: 313
# not
# not \param [in]  pSurface Surface to be identified
# not \param [out] pHandle Will be filled by the return handle
# not
# not \return An INT which could be an NvAPI status or DX HRESULT code
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D9_GetSurfaceHandle = hDll.D3D9_GetSurfaceHandle
NvAPI_D3D9_GetSurfaceHandle.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_D3D9_GetSurfaceHandle(IDirect3DSurface9 *pSurface,
#                                        NVDX_ObjectHandle *pHandle);

# not SUPPORTED OS: Windows 7 and higher
# not
# not \addtogroup dxvidcontrol
# not @{
# ///////////////////////////////////////////////////////////////////
# FUNCTION_NAME: NvAPI_D3D9_VideoSetStereoInfo
# not \fn NvAPI_D3D9_VideoSetStereoInfo(IDirect3DDevice9 *pDev,
# not        NV_DX_VIDEO_STEREO_INFO *pStereoInfo);
# not \code
# not DESCRIPTION: This api specifies the stereo format of a surface,
# so that the
# not    surface could be used for stereo video processing or
# compositing.
# not    In particular, this api could be used to link the left and
# right
# not    views of a decoded picture.
# not
# not \since Release: 313
# not
# not  INPUT: pDev  - The device on which the stereo surface will be
# used
# not    pStereoInfo - The stereo format of the surface
# not
# not RETURN STATUS: an INT which could be an NvAPI status or DX
# HRESULT code
# not \endcode
# ///////////////////////////////////////////////////////////////////


class _NV_STEREO_VIDEO_FORMAT(ENUM):
    NV_STEREO_VIDEO_FORMAT_NOT_STEREO = 0
    NV_STEREO_VIDEO_FORMAT_SIDE_BY_SIDE_LR = 1
    NV_STEREO_VIDEO_FORMAT_SIDE_BY_SIDE_RL = 2
    NV_STEREO_VIDEO_FORMAT_TOP_BOTTOM_LR = 3
    NV_STEREO_VIDEO_FORMAT_TOP_BOTTOM_RL = 4
    NV_STEREO_VIDEO_FORMAT_ROW_INTERLEAVE_LR = 5
    NV_STEREO_VIDEO_FORMAT_ROW_INTERLEAVE_RL = 6
    NV_STEREO_VIDEO_FORMAT_TWO_FRAMES_LR = 7
    NV_STEREO_VIDEO_FORMAT_MONO_PLUS_OFFSET = 8
    NV_STEREO_VIDEO_FORMAT_LAST = 9


NV_STEREO_VIDEO_FORMAT = _NV_STEREO_VIDEO_FORMAT

# not < Must be NV_DX_VIDEO_STEREO_INFO_VER
_NV_DX_VIDEO_STEREO_INFO._fields_ = [
    ('dwVersion', NvU32),
    # not < The surface whose stereo format is to be set
    ('hSurface', NVDX_ObjectHandle),
    # not < The linked surface
    # (must be valid when eFormat == NV_STEREO_VIDEO_FORMAT_TWO_FRAMES_LR)
    #
    ('hLinkedSurface', NVDX_ObjectHandle),
    # not < Stereo format of the surface
    ('eFormat', NV_STEREO_VIDEO_FORMAT),
    # not < Signed offset of each view
    # (positive offset indicating left view is shifted left)
    ('sViewOffset', NvS32),
    # not < Whether stereo rendering should be enabled
    # (if FALSE, only left view will be used)
    ('bStereoEnable', BOOL),
]

# not Macro for constructing the version field of
# ::NV_DX_VIDEO_STEREO_INFO
NV_DX_VIDEO_STEREO_INFO_VER = (
    MAKE_NVAPI_VERSION(NV_DX_VIDEO_STEREO_INFO, 1)
)

NvAPI_D3D9_VideoSetStereoInfo = hDll.D3D9_VideoSetStereoInfo
NvAPI_D3D9_VideoSetStereoInfo.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D9_VideoSetStereoInfo(IDirect3DDevice9 *pDev,
#                                              NV_DX_VIDEO_STEREO_INFO *pStereoInfo);


# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D10_SetDepthBoundsTest
# not DESCRIPTION: This function enables/disables the depth bounds
# test.
# not
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] pDev  The device to set the depth bounds test
# not \param [in] bEnable Enable(non-zero)/disable(zero) the depth
# bounds test
# not \param [in] fMinDepth The minimum depth for the depth bounds test
# not \param [in] fMaxDepth The maximum depth for the depth bounds
# test \n
# not     The valid values for fMinDepth and fMaxDepth
# not     are such that 0 <= fMinDepth <= fMaxDepth <= 1
# not
# not \return NVAPI_OK if the depth bounds test was correctly enabled
# or disabled
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D10_SetDepthBoundsTest = hDll.D3D10_SetDepthBoundsTest
NvAPI_D3D10_SetDepthBoundsTest.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D10_SetDepthBoundsTest(ID3D10Device *pDev,
#                                               NvU32 bEnable,
#                                               float fMinDepth,
#                                               float fMaxDepth);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_IsNvShaderExtnOpCodeSupported
# not DESCRIPTION: This function checks if a nv HLSL shader extension
# opcode is
# not    supported on current hardware. List of opcodes is in
# nvShaderExtnEnums.h
# not    To use Nvidia HLSL extensions the application must include
# nvHLSLExtns.h
# not    in the hlsl shader code. See nvHLSLExtns.h for more details
# on supported opcodes.
# not
# not    This function can be called from a different thread than the
# one calling immediate device setstate functions.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  pDev  The device on which to query for support,
# not      should be a ID3D11Device+ device
# not \param [in]  opCode  the opcode to check
# not \param [out]  pSupported true if supported, false otherwise
# not
# not RETURN STATUS:  This API can return any of the error codes
# enumerated in NvAPI_Status.
# not    If there are return error codes with specific meaning for
# this API, they are listed below.
# not \retval ::  NVAPI_OK if the call succeeded
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_IsNvShaderExtnOpCodeSupported = hDll.D3D11_IsNvShaderExtnOpCodeSupported
NvAPI_D3D11_IsNvShaderExtnOpCodeSupported.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_IsNvShaderExtnOpCodeSupported(__in  IUnknown *pDev,
#                                                           __in  NvU32 opCode,
#                                                           __out bool *pSupported);


# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_SetNvShaderExtnSlot
# not DESCRIPTION: This function sets the fake UAV slot that is used
# by Nvidia HLSL
# not    shader extensions globally. All createShader calls made to
# the driver after
# not    setting this slot would treat writes/reads to this UAV in a
# not    different way. Applications are expected to bind null UAV to
# this slot.
# not    The same slot is used for all shader stages.
# not    To disable shader extensions the app need to set this uav
# slot to 0xFFFFFFFF.
# not    To use Nvidia HLSL extensions the application must include
# nvHLSLExtns.h
# not    in the hlsl shader code. See nvHLSLExtns.h for more details.
# not
# not    This function can be called from a different thread than the
# one calling immediate device setstate functions.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  pDev  The device for which to set the extension slot
# not      should be a ID3D11Device+ device
# not \param [in]  uavSlot the uav slot to use
# not
# not RETURN STATUS:  This API can return any of the error codes
# enumerated in NvAPI_Status.
# not    If there are return error codes with specific meaning for
# this API, they are listed below.
# not \retval ::  NVAPI_OK : success, the uavSlot was set sucessfully
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_SetNvShaderExtnSlot = hDll.D3D11_SetNvShaderExtnSlot
NvAPI_D3D11_SetNvShaderExtnSlot.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_SetNvShaderExtnSlot(__in IUnknown *pDev,
#                                                __in NvU32 uavSlot);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_SetNvShaderExtnSlotSpace
# not DESCRIPTION: This function is specifically created for ray
# tracing since we do not
# not    currently support PSOs with DXR.
# not    This function sets the device's fake UAV slot and space that
# is used by Nvidia HLSL
# not    shader extensions globally. All state objects created by the
# driver after
# not    setting this slot would treat writes/reads to this UAV in a
# not    different way. Applications are expected to bind null UAV to
# this slot.
# not    The same slot is used for all shader stages.
# not    To disable shader extensions the app need to set this uav
# slot to 0xFFFFFFFF.
# not    To use Nvidia HLSL extensions the application must include
# nvHLSLExtns.h
# not    in the hlsl shader code. See nvHLSLExtns.h for more details.
# not
# not    This function can be called from a different thread than the
# one calling immediate device setstate functions.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  pDev  The device for which to set the extension slot
# not      should be a ID3D12Device+ device
# not \param [in]  uavSlot The uav slot to use
# not \param [in]  uavSpace  The uav space to use
# not
# not RETURN STATUS:  This API can return any of the error codes
# enumerated in NvAPI_Status.
# not    If there are return error codes with specific meaning for
# this API, they are listed below.
# not \retval ::  NVAPI_OK : success, the uavSlot and uavSpace were
# set sucessfully
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D12_SetNvShaderExtnSlotSpace = hDll.D3D12_SetNvShaderExtnSlotSpace
NvAPI_D3D12_SetNvShaderExtnSlotSpace.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_SetNvShaderExtnSlotSpace(__in IUnknown *pDev,
#                                                __in NvU32 uavSlot,
#                                                __in NvU32 uavSpace);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_SetNvShaderExtnSlotSpaceLocalThread
# not DESCRIPTION: This function is specifically created for ray
# tracing shaders since we do not
# not    currently support PSOs with DXR.
# not    This function sets the device's fake UAV slot that is used by
# Nvidia HLSL
# not    shader extensions on local thread. All state objects created
# by the driver
# not    on the same thread that call this function after setting this
# slot would treat writes/reads
# not    to this UAV in a different way.
# not    Applications are expected to bind null UAV to this slot.
# not    The same slot is used for all shader stages for the device.
# not    To disable shader extensions the app may set this uav slot to
# 0xFFFFFFFF.
# not    To use Nvidia HLSL extensions the application must include
# nvHLSLExtns.h
# not    in the hlsl shader code. See nvHLSLExtns.h for more details.
# not
# not    This function can be called from a different thread than the
# one calling immediate device setstate functions.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not
# not \since Release: 387
# not
# not \param [in]  pDev  The device for which to set the extension slot
# not      should be a ID3D12Device+ device
# not \param [in]  uavSlot the uav slot to use
# not \param [in]  uavSpace  the uav space to use
# not
# not RETURN STATUS:  This API can return any of the error codes
# enumerated in NvAPI_Status.
# not    If there are return error codes with specific meaning for
# this API, they are listed below.
# not \retval ::  NVAPI_OK : success, the uavSlot and uavSpace were
# set sucessfully
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D12_SetNvShaderExtnSlotSpaceLocalThread = hDll.D3D12_SetNvShaderExtnSlotSpaceLocalThread
NvAPI_D3D12_SetNvShaderExtnSlotSpaceLocalThread.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_SetNvShaderExtnSlotSpaceLocalThread(__in IUnknown *pDev,
#                                                                 __in NvU32 uavSlot,
#                                                                 __in NvU32 uavSpace);


# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_SetNvShaderExtnSlotLocalThread
# not DESCRIPTION: This function sets the fake UAV slot that is used
# by Nvidia HLSL
# not    shader extensions on local thread. All createShader calls on
# the same thread
# not    that calls this function after setting this slot would treat
# writes/reads
# not    to this UAV in a different way.
# not    Applications are expected to bind null UAV to this slot.
# not    The same slot is used for all shader stages.
# not    To disable shader extensions the app may set this uav slot to
# 0xFFFFFFFF.
# not    To use Nvidia HLSL extensions the application must include
# nvHLSLExtns.h
# not    in the hlsl shader code. See nvHLSLExtns.h for more details.
# not
# not    This function can be called from a different thread than the
# one calling immediate device setstate functions.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 387
# not
# not \param [in]  pDev  The device for which to set the extension slot
# not      should be a ID3D11Device+ device
# not \param [in]  uavSlot the uav slot to use
# not
# not RETURN STATUS:  This API can return any of the error codes
# enumerated in NvAPI_Status.
# not    If there are return error codes with specific meaning for
# this API, they are listed below.
# not \retval ::  NVAPI_OK : success, the uavSlot was set sucessfully
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_SetNvShaderExtnSlotLocalThread = hDll.D3D11_SetNvShaderExtnSlotLocalThread
NvAPI_D3D11_SetNvShaderExtnSlotLocalThread.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_D3D11_SetNvShaderExtnSlotLocalThread(__in IUnknown *pDev,
#                                                           __in NvU32 uavSlot);
#

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_BeginUAVOverlapEx
# not DESCRIPTION: Causes the driver to skip synchronization that is
# normally needed when accessing UAVs.
# not    Applications must use this with caution otherwise this might
# cause data hazards when
# not    multiple draw calls/compute shader launches are accessing
# same memory locations
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  *pDeviceOrContext  pointer to D3D11 device, or
# D3D11 device context
# not \param [in]  insertWFIFlags  bit fields to indicate which WFI
# would be inserted (gfx / compute / both).
# not
# not RETURN STATUS:  This API can return any of the error codes
# enumerated in NvAPI_Status.
# not    If there are return error codes with specific meaning for
# this API, they are listed below.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
class _NVAPI_D3D11_INSERTWFI_FLAG(ENUM):
    NVAPI_D3D_BEGIN_UAV_OVERLAP_NO_WFI = 0x00000000
    NVAPI_D3D_BEGIN_UAV_OVERLAP_GFX_WFI = 0x00000001
    NVAPI_D3D_BEGIN_UAV_OVERLAP_COMP_WFI = 0x00000002


NVAPI_D3D11_INSERTWFI_FLAG = _NVAPI_D3D11_INSERTWFI_FLAG

NvAPI_D3D11_BeginUAVOverlapEx = hDll.D3D11_BeginUAVOverlapEx
NvAPI_D3D11_BeginUAVOverlapEx.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_BeginUAVOverlapEx(__in  IUnknown *pDeviceOrContext, __in NvU32 insertWFIFlags);


# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_BeginUAVOverlap
# not DESCRIPTION: Causes the driver to skip synchronization that is
# normally needed when accessing UAVs.
# not    Applications must use this with caution otherwise this might
# cause data hazards when
# not    multiple draw calls/compute shader launches are accessing
# same memory locations
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  *pDeviceOrContext  pointer to D3D11 device, or
# D3D11 device context
# not
# not RETURN STATUS:  This API can return any of the error codes
# enumerated in NvAPI_Status.
# not    If there are return error codes with specific meaning for
# this API, they are listed below.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_BeginUAVOverlap = hDll.D3D11_BeginUAVOverlap
NvAPI_D3D11_BeginUAVOverlap.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_BeginUAVOverlap(__in  IUnknown *pDeviceOrContext);


# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_EndUAVOverlap
# not DESCRIPTION: Re-enables driver synchronization between calls
# that access same UAVs
# not    See NvAPI_D3D_BeginUAVOverlap for more details.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  *pDeviceOrContext  pointer to D3D11 device, or
# D3D11 device context
# not
# not RETURN STATUS:  This API can return any of the error codes
# enumerated in NvAPI_Status.
# not    If there are return error codes with specific meaning for
# this API, they are listed below.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_EndUAVOverlap = hDll.D3D11_EndUAVOverlap
NvAPI_D3D11_EndUAVOverlap.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_EndUAVOverlap(__in  IUnknown *pDeviceOrContext);


# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_SetFPSIndicatorState
# not DESCRIPTION: Display an overlay that tracks the number of times
# the app presents per second, or,
# not  the number of frames-per-second (FPS)
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] BOOL Whether or not to enable the fps indicator.
# not
# not \return ::NVAPI_OK,
# not  ::NVAPI_ERROR
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D_SetFPSIndicatorState = hDll.D3D_SetFPSIndicatorState
NvAPI_D3D_SetFPSIndicatorState.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D_SetFPSIndicatorState(IUnknown *pDev, NvU8 doEnable);


# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D9_Present
# not DESCRIPTION: This API presents the contents of the next buffer
# in the sequence of back buffers
# not   owned by a IDirect3DDevice9 device.
# not   This Present operation supports using a SwapGroup and
# SwapBarrier on the SwapChain
# not   that owns the back buffer to be presented.
# not
# not   NOTE: NvAPI_D3D9_Present is a wrapper of the method
# IDirect3DDevice9::Present which
# not    additionally notifies the D3D driver of the SwapChain used by
# the runtime for
# not    presentation, thus allowing the D3D driver to apply SwapGroup
# and SwapBarrier
# not    functionality to that SwapChain.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] pDevice  The IDirect3DDevice9 interface that is used
# to issue the Present,
# not    using the following IDirect3DDevice9::Present input parameters
# not \param [in] pSwapChain Optional pointer to a IDirect3DSwapChain9
# interface. If provided, the presentation is executed
# not     using this interface (i.e. pSwapChain.Present()) for the
# given swapchain only.
# not     If NULL, the presentation is executed on the device for all
# swapchains as in pDevice.Present()
# not \param [in] pSourceRect A pointer to a RECT structure containing
# the source rectangle.
# not     If NULL, the entire source surface is presented.
# not \param [in] pDestRect A pointer to a RECT structure containing
# the destination rectangle, in window client coordinates.
# not    If NULL, the entire client area is filled.
# not \param [in] hDestWindowOverride A pointer to a destination
# window whose client area is taken as the target for this
# presentation.
# not       If this value is NULL, then the hWndDeviceWindow member of
# D3DPRESENT_PARAMTERS is taken.
# not \param [in] pDirtyRegion (IN) A pointer to a region to be
# presented. It must be NULL unless the swap chain was reated with
# not       D3DSWAPEFFECT_COPY. If this value is non-NULL, the
# contained region is expressed in back buffer coordinates.
# not
# not \retval ::NVAPI_OK    the Present operation was successfully
# executed
# not \retval ::NVAPI_D3D_DEVICE_LOST D3D device status is
# D3DERR_DEVICELOST or D3DERR_DEVICENOTRESET, the caller has to reset
# device
# not \retval ::NVAPI_DEVICE_BUSY  the Present operation failed with
# an error other than D3DERR_DEVICELOST or D3DERR_DEVICENOTRESET
# not \retval ::NVAPI_ERROR   the communication with the D3D driver
# failed, SwapGroup/SwapBarrier may not be possible.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI was not yet
# initialized.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D9_Present = hDll.D3D9_Present
NvAPI_D3D9_Present.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D9_Present(IDirect3DDevice9 *pDevice,
#                                    IDirect3DSwapChain9 *pSwapChain,
#                                    const RECT *pSourceRect,
#                                    const RECT *pDestRect,
#                                    HWND hDestWindowOverride,
#                                    const RGNDATA *pDirtyRegion);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D9_QueryFrameCount
# not DESCRIPTION: This API queries the universal framecounter of the
# Quadro-Sync master device.
# not
# not \param [in] pDevice  The caller provides the DX9 device that has
# access to the Quadro-Sync device
# not \param [out] pFrameCount  The caller provides the storage space
# where the framecount is stored.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \retval ::NVAPI_OK   *pFrameCount populated with framecount
# value.
# not \retval ::NVAPI_ERROR   The operation failed.
# not \retval ::NVAPI_INVALID_ARGUMENT One or more args passed in are
# invalid.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI was not yet
# initialized.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D9_QueryFrameCount = hDll.D3D9_QueryFrameCount
NvAPI_D3D9_QueryFrameCount.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D9_QueryFrameCount(IDirect3DDevice9 *pDevice,
#                                            NvU32 *pFrameCount);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D9_ResetFrameCount
# not DESCRIPTION: This API resets the universal framecounter on the
# Quadro-Sync master device.
# not
# not \param [in] pDevice  The caller provides the DX9 device that has
# access to the Quadro-Sync device
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \retval ::NVAPI_OK    framecounter has been reset
# not \retval ::NVAPI_ERROR   The operation failed.
# not \retval ::NVAPI_INVALID_ARGUMENT  One or more args passed in are
# invalid.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI was not yet
# initialized.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D9_ResetFrameCount = hDll.D3D9_ResetFrameCount
NvAPI_D3D9_ResetFrameCount.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D9_ResetFrameCount(IDirect3DDevice9 *pDevice);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D9_QueryMaxSwapGroup
# not DESCRIPTION: This API queries the number of supported SwapGroups
# and SwapBarriers in the graphics system.
# not
# not \param [in] pDevice   The caller provides the DirectX 9 device
# that is used as a swapgroup client
# not \param [out] pMaxGroups   The caller provides the storage space
# where the number of available SwapGroups is stored.
# not \param [out] pMaxBarriers  The caller provides the storage space
# where the number of available SwapBarriers is stored.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \retval ::NVAPI_OK    the number of SwapGroups and SwapBarriers
# has been stored
# not \retval ::NVAPI_ERROR   The operation failed.
# not \retval ::NVAPI_INVALID_ARGUMENT  One or more args passed in are
# invalid.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI was not yet
# initialized.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D9_QueryMaxSwapGroup = hDll.D3D9_QueryMaxSwapGroup
NvAPI_D3D9_QueryMaxSwapGroup.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D9_QueryMaxSwapGroup(IDirect3DDevice9 *pDevice,
#                                             NvU32 *pMaxGroups,
#                                             NvU32 *pMaxBarriers);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D9_QuerySwapGroup
# not DESCRIPTION: This API queries the current SwapGroup and
# SwapBarrier that a SwapChain of a specific client device is bound to.
# not
# not \param [in] pDevice  The caller provides the DirectX 9 device
# that is used as a swapgroup client
# not \param [in] pSwapChain  The caller provides the
# IDirect3DSwapChain9 interface as a handle to the SwapChain
# not       that belongs to the swapgroup client device
# not \param [out] pSwapGroup  The caller provides the storage space
# where the current SwapGroup is stored.
# not \param [out] pSwapBarrier  The caller provides the storage space
# where the current SwapBarrier is stored.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \retval ::NVAPI_OK    the current SwapGroup and SwapBarrier has
# been stored
# not \retval ::NVAPI_ERROR   The operation failed.
# not \retval ::NVAPI_INVALID_ARGUMENT  One or more args passed in are
# invalid.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI was not yet
# initialized.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D9_QuerySwapGroup = hDll.D3D9_QuerySwapGroup
NvAPI_D3D9_QuerySwapGroup.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D9_QuerySwapGroup(IDirect3DDevice9 *pDevice,
#                                          IDirect3DSwapChain9 *pSwapChain,
#                                          NvU32 *pSwapGroup,
#                                          NvU32 *pSwapBarrier);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D9_JoinSwapGroup
# not DESCRIPTION: This API causes the SwapChain of a SwapGroup client
# to join or leave the specified SwapGroup.
# not
# not \param [in] pDevice   The caller provides the DirectX 9 device
# that is used as a swapgroup client
# not \param [in] pSwapChain  The caller provides the
# IDirect3DSwapChain9 interface as a handle to the SwapChain
# not       that belongs to the swapgroup client device
# not \param [in] group    The caller specifies the SwapGroup which
# the SwapChain should join.
# not       - If the value of group is zero, the SwapChain leaves the
# SwapGroup.
# not       - The SwapChain joins a SwapGroup if the SwapGroup number
# is a positive integer less than or
# not        equal to the maximum number of SwapGroups queried by
# NvAPI_SwapGroup_QueryMaxSwapGroup.
# not \param [in] blocking   The caller specifies that a presentation
# of this SwapChain should return immediately or block
# not       until all members of the SwapGroup are ready and the
# presentation was actually executed.
# not       A BOOLEAN value of false means the Present operation
# returns immediately and a value of true
# not       means the Present operation is blocking.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \retval ::NVAPI_OK    the SwapChain joined/left the SwapGroup
# accordingly
# not \retval ::NVAPI_ERROR   The operation failed.
# not \retval ::NVAPI_INVALID_ARGUMENT  One or more args passed in are
# invalid.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI was not yet
# initialized.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D9_JoinSwapGroup = hDll.D3D9_JoinSwapGroup
NvAPI_D3D9_JoinSwapGroup.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D9_JoinSwapGroup(IDirect3DDevice9 *pDevice,
#                                         IDirect3DSwapChain9 *pSwapChain,
#                                         NvU32 group,
#                                         BOOL blocking);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D9_BindSwapBarrier
# not DESCRIPTION: This API causes a SwapGroup to be bound to or
# released from the specified SwapBarrier.
# not
# not \param [in] pDevice The caller provides the DirectX 9 device
# that is used as a swapgroup client
# not \param [in] group The caller specifies the SwapGroup to be bound
# to the SwapBarrier.
# not \param [in] barrier The caller specifies the SwapBarrier that
# the SwapGroup should be bound to.
# not      - If the value of barrier is zero, the SwapGroup will be
# released from the SwapBarrier.
# not      - The SwapGroup will be bound to the SwapBarrier if the
# value of barrier is a positive
# not      integer less than or equal to the maximum number of
# SwapBarriers queried by NvAPI_SwapGroup_QueryMaxSwapGroup.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \retval ::NVAPI_OK   the SwapGroup is bound to or released from
# the specified SwapBarrier
# not \retval ::NVAPI_ERROR   The operation failed.
# not \retval ::NVAPI_INVALID_ARGUMENT One or more args passed in are
# invalid.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI was not yet
# initialized.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D9_BindSwapBarrier = hDll.D3D9_BindSwapBarrier
NvAPI_D3D9_BindSwapBarrier.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D9_BindSwapBarrier(IDirect3DDevice9 *pDevice,
#                                           NvU32 group,
#                                           NvU32 barrier);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D1x_Present
# not DESCRIPTION: Presents the contents of the next buffer in the
# sequence of back buffers
# not   owned by a D3D device.
# not   This Present operation supports using a SwapGroup and
# SwapBarrier on the SwapChain
# not   that owns the back buffer to be presented.
# not
# not   NOTE: NvAPI_D3D1x_Present is a wrapper of the method
# IDXGISwapChain::Present which
# not    additionally notifies the D3D driver of the SwapChain used by
# the runtime for
# not    presentation, thus allowing the D3D driver to apply SwapGroup
# and SwapBarrier
# not    functionality to that SwapChain.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  pDevice  The D3D device interface that is used to
# issue the Present operation,
# not      using the following IDirect3DDevice9::Present input
# parameters.
# not       pDevice can be either ID3D10Device or ID3D10Device1 or
# ID3D11Device or ID3D12Device.
# not \param [in]  pSwapChain  The IDXGISwapChain interface that is
# intended to present
# not \param [in]  SyncInterval  An integer that specifies the how to
# synchronize presentation of a frame with the vertical blank.
# not        Values are:
# not        - 0: The presentation occurs immediately, there is no
# synchronization.
# not        - 1,2,3,4 : Synchronize presentation after the n'th
# vertical blank.
# not \param [in]  Flags  An integer value that contains swap-chain
# presentation options as defined in DXGI_PRESENT.
# not
# not \retval ::NVAPI_OK    the Present operation was successfully
# executed
# not \retval ::NVAPI_DEVICE_BUSY  the Present operation failed with
# an error DXGI_ERROR_DEVICE_RESET or DXGI_ERROR_DEVICE_REMOVED,
# DXGI_STATUS_OCCLUDED, or D3DDDIERR_DEVICEREMOVED.
# not \retval ::NVAPI_ERROR   the communication with the D3D driver
# failed, SwapGroup/SwapBarrier may not be possible.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI was not yet
# initialized.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D1x_Present = hDll.D3D1x_Present
NvAPI_D3D1x_Present.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D1x_Present(IUnknown *pDevice,
#                                    IDXGISwapChain *pSwapChain,
#                                    UINT SyncInterval,
#                                    UINT Flags);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D1x_QueryFrameCount
# not DESCRIPTION: This API queries the universal framecounter of the
# Quadro-Sync master device.
# not
# not \param [in] pDevice   The caller provides the D3D device that
# has access to the Quadro-Sync device,
# not       pDevice can be either ID3D10Device or ID3D10Device1 or
# ID3D11Device or ID3D12Device.
# not \param [out] pFrameCount  The caller provides the storage space
# where the framecount is stored.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \retval ::NVAPI_OK    *pFrameCount populated with framecount
# value.
# not \retval ::NVAPI_ERROR   The operation failed.
# not \retval ::NVAPI_INVALID_ARGUMENT  One or more args passed in are
# invalid.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI was not yet
# initialized.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D1x_QueryFrameCount = hDll.D3D1x_QueryFrameCount
NvAPI_D3D1x_QueryFrameCount.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D1x_QueryFrameCount(IUnknown *pDevice,
#                                            NvU32 *pFrameCount);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D1x_ResetFrameCount
# not DESCRIPTION: This API resets the universal framecounter on the
# Quadro-Sync master device.
# not
# not \param [in] pDevice  The caller provides the D3D device that has
# access to the Quadro-Sync device,
# not      pDevice can be either ID3D10Device or ID3D10Device1 or
# ID3D11Device or ID3D12Device.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \retval ::NVAPI_OK    framecounter has been reset
# not \retval ::NVAPI_ERROR   The operation failed.
# not \retval ::NVAPI_INVALID_ARGUMENT  pDevice arg passed in is
# invalid.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI was not yet
# initialized.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D1x_ResetFrameCount = hDll.D3D1x_ResetFrameCount
NvAPI_D3D1x_ResetFrameCount.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D1x_ResetFrameCount(IUnknown *pDevice);


# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D1x_QueryMaxSwapGroup
# not DESCRIPTION: This API queries the number of supported SwapGroups
# and SwapBarriers in the graphics system.
# not
# not \param [in] pDevice  The caller provides the D3D device that is
# intended to use SwapGroup functionality.
# not      pDevice can be either ID3D10Device or ID3D10Device1 or
# ID3D11Device or ID3D12Device.
# not \param [out] pMaxGroups  The caller provides the storage space
# where the number of available SwapGroups is stored.
# not \param [out] pMaxBarriers The caller provides the storage space
# where the number of available SwapBarriers is stored.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \retval ::NVAPI_OK   the number of SwapGroups and SwapBarriers
# has been stored
# not \retval ::NVAPI_ERROR   The operation failed.
# not \retval ::NVAPI_INVALID_ARGUMENT One or more args passed in are
# invalid.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI was not yet
# initialized.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D1x_QueryMaxSwapGroup = hDll.D3D1x_QueryMaxSwapGroup
NvAPI_D3D1x_QueryMaxSwapGroup.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D1x_QueryMaxSwapGroup(IUnknown *pDevice,
#                                              NvU32 *pMaxGroups,
#                                              NvU32 *pMaxBarriers);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D1x_QuerySwapGroup
# not DESCRIPTION: This API queries the current SwapGroup and
# SwapBarrier that a SwapChain of a specific client device is bound to.
# not
# not \param [in] pDevice  The caller provides the D3D device that
# owns the SwapChain used as a SwapGroup client.
# not      pDevice can be either ID3D10Device or ID3D10Device1 or
# ID3D11Device or ID3D12Device.
# not \param [in] pSwapChain  The IDXGISwapChain interface that is
# used as the SwapGroup client.
# not
# not \param [out] pSwapGroup  The caller provides the storage space
# where the current SwapGroup is stored.
# not \param [out] pSwapBarrier  The caller provides the storage space
# where the current SwapBarrier is stored.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \retval ::NVAPI_OK    the current SwapGroup and SwapBarrier has
# been stored
# not \retval ::NVAPI_ERROR   The operation failed.
# not \retval ::NVAPI_INVALID_ARGUMENT  One or more args passed in are
# invalid.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI was not yet
# initialized.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D1x_QuerySwapGroup = hDll.D3D1x_QuerySwapGroup
NvAPI_D3D1x_QuerySwapGroup.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D1x_QuerySwapGroup(IUnknown *pDevice,
#                                           IDXGISwapChain  *pSwapChain,
#                                           NvU32 *pSwapGroup,
#                                           NvU32 *pSwapBarrier);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D1x_JoinSwapGroup
# not DESCRIPTION: This API causes the SwapChain of a SwapGroup client
# to join or leave the specified SwapGroup.
# not
# not \param [in] pDevice  The caller provides the D3D device that
# owns the SwapChain used as a SwapGroup client.
# not       pDevice can be either ID3D10Device or ID3D10Device1 or
# ID3D11Device or ID3D12Device.
# not \param [in] pSwapChain  The IDXGISwapChain interface that is
# used as the SwapGroup client.
# not \param [in] group   The caller specifies the SwapGroup which the
# SwapChain should join.
# not       - If the value of group is zero, the SwapChain leaves the
# SwapGroup.
# not       - The SwapChain joins a SwapGroup if the SwapGroup number
# is a positive integer less than or
# not        equal to the maximum number of SwapGroups queried by
# NvAPI_SwapGroup_QueryMaxSwapGroup.
# not \param [in] blocking   The caller specifies that a presentation
# of this SwapChain should return immediately or block
# not       until all members of the SwapGroup are ready and the
# presentation was actually executed.
# not       A BOOLEAN value of false means the Present operation
# returns immediately and a value of true
# not       means the Present operation is blocking.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \retval ::NVAPI_OK    the SwapChain joined/left the SwapGroup
# accordingly
# not \retval ::NVAPI_ERROR   The operation failed.
# not \retval ::NVAPI_INVALID_ARGUMENT  One or more args passed in are
# invalid.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI was not yet
# initialized.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D1x_JoinSwapGroup = hDll.D3D1x_JoinSwapGroup
NvAPI_D3D1x_JoinSwapGroup.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D1x_JoinSwapGroup(IUnknown *pDevice,
#                                          IDXGISwapChain  *pSwapChain,
#                                          NvU32 group,
#                                          BOOL blocking);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D1x_BindSwapBarrier
# not DESCRIPTION: This API causes a SwapGroup to be bound to or
# released from the specified SwapBarrier.
# not
# not \param [in] pDevice  The caller provides the D3D device that
# owns the SwapChain used as a SwapGroup client.
# not       pDevice can be either ID3D10Device or ID3D10Device1 or
# ID3D11Device or ID3D12Device.
# not \param [in] group   The caller specifies the SwapGroup to be
# bound to the SwapBarrier.
# not \param [in] barrier  The caller specifies the SwapBarrier that
# the SwapGroup should be bound to.
# not       - If the value of barrier is zero, the SwapGroup releases
# the SwapBarrier.
# not       - The SwapGroup will be bound to the SwapBarrier if the
# value of barrier is a positive
# not        integer less than or equal to the maximum number of
# SwapBarriers queried by NvAPI_D3D1x_QueryMaxSwapGroup.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \retval ::NVAPI_OK   the SwapGroup is bound to the specified
# SwapBarrier
# not \retval ::NVAPI_ERROR   The operation failed.
# not \retval ::NVAPI_INVALID_ARGUMENT  One or more args passed in are
# invalid.
# not \retval ::NVAPI_API_NOT_INITIALIZED NvAPI was not yet
# initialized.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////

NvAPI_D3D1x_BindSwapBarrier = hDll.D3D1x_BindSwapBarrier
NvAPI_D3D1x_BindSwapBarrier.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_D3D1x_BindSwapBarrier(IUnknown *pDevice,
#                                            NvU32 group,
#                                            NvU32 barrier);

# not SUPPORTED OS: Windows 7 and higher
# not
class NVAPI_QUAD_FILLMODE(ENUM):
    NVAPI_QUAD_FILLMODE_DISABLED = 0
    NVAPI_QUAD_FILLMODE_BBOX = 1
    NVAPI_QUAD_FILLMODE_FULL_VIEWPORT = 2


NVAPI_QUAD_FILLMODE_DISABLED = NVAPI_QUAD_FILLMODE.NVAPI_QUAD_FILLMODE_DISABLED
NVAPI_QUAD_FILLMODE_BBOX = NVAPI_QUAD_FILLMODE.NVAPI_QUAD_FILLMODE_BBOX
NVAPI_QUAD_FILLMODE_FULL_VIEWPORT = NVAPI_QUAD_FILLMODE.NVAPI_QUAD_FILLMODE_FULL_VIEWPORT

# not SUPPORTED OS: Windows 7 and higher
# not

D3D11_FILL_MODE = VOID
D3D11_CULL_MODE = VOID

NvAPI_D3D11_RASTERIZER_DESC_EX._fields_ = [
    # D3D11_RASTERIZER_DESC member variables
    ('FillMode', D3D11_FILL_MODE),
    ('CullMode', D3D11_CULL_MODE),
    ('FrontCounterClockwise', BOOL),
    ('DepthBias', INT),
    ('DepthBiasClamp', FLOAT),
    ('SlopeScaledDepthBias', FLOAT),
    ('DepthClipEnable', BOOL),
    ('ScissorEnable', BOOL),
    ('MultisampleEnable', BOOL),
    ('AntialiasedLineEnable', BOOL),
    # < not Added DX 11.1, part of _DESC1 version of this struct.
    ('ForcedSampleCount', NvU32),
    # < not enable Programmable Samples feature
    ('ProgrammableSamplePositionsEnable', BOOL),
    # < not when jitter is enabled, an app need to fill the whole
    # arrays below, otherwise only as much entries as samples
    ('InterleavedSamplingEnable', BOOL),
    # < not number of samples. In TIR N.1 it needs to match N, in
    # non-TIR it needs to match RT sample count. Ignored if
    # ForcePerSampleInterlock is set
    ('SampleCount', NvU8),
    # < not x positions in API sample order
    ('SamplePositionsX', NvU8 * 16),
    # < not y positions in API sample order
    ('SamplePositionsY', NvU8 * 16),
    # < not rasterize all pixels a primitive touches in any way
    # instead of just those with the centroid covered.
    ('ConservativeRasterEnable', BOOL),
    # < not Fill a triangle outside its bounds as a screen-aligned
    # quad, matching the tri's bounding-box or filling the full
    # viewport.
    ('QuadFillMode', NVAPI_QUAD_FILLMODE),
    # < not Enable pixel-shader input SV_COVERAGE to account for
    # z-test in early-z mode.
    ('PostZCoverageEnable', BOOL),
    # < not Enable output of coverage to a color render-target.
    ('CoverageToColorEnable', BOOL),
    # < not Index of RT for coverage-to-color.
    ('CoverageToColorRTIndex', NvU8),
    # < not TargetIndepentRasterWithDepth = TRUE enables rasterezation
    # mode where sample count of both raster and depth-stencil buffer
    # are equal and do not match RT sample count.
    ('TargetIndepentRasterWithDepth', BOOL),
    # < not reserved for expansion, set to zero.
    ('reserved', NvU8 * 63),
]

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_CreateRasterizerState
# not \code
# not DESCRIPTION: This function is an extension of
# ID3D11Device::CreateRasterizerState with additional raster states
# not
# not    If programmable sample positions is used, to decompress the
# surface using the currently bound
# not    programmable sample positions, use function
# NvAPI_D3D11_DecompressView.
# not
# not    This function is free-threaded create compatible i.e. it can
# be called from a different thread
# not    than the one calling immediate device setstate functions.
# not
# not  \param [in]  pDevice   current d3d device
# not  \param [in]  pRasterizerDesc  Rasterizer state description of
# type NVAPI_D3D11_RASTERIZER_DESC_EX
# not  \param [out]  ppRasterizerState ID3D11RasterizerState
# not
# not
# not \return ::NVAPI_OK  if the call succeeds.
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_CreateRasterizerState = hDll.D3D11_CreateRasterizerState
NvAPI_D3D11_CreateRasterizerState.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_D3D11_CreateRasterizerState(__in ID3D11Device *pDevice,
#                                                  __in const NvAPI_D3D11_RASTERIZER_DESC_EX *pRasterizerDesc,
#                                                  __out ID3D11RasterizerState **ppRasterizerState);

# not SUPPORTED OS: Windows 7 and higher
# not

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_ConfigureAnsel
# not \code
# not DESCRIPTION: This function configure the setting of AnselShim,
# including hotkey.
# not
# not  \param [in]  pDevice   current d3d device
# (should be ID3D11Device, ID3D10Device, or ID3D12Device)
# not  \param [in]  pAnselConfig  configuration of Ansel to be set,
# including hotkey setting
# not
# not
# not \return ::NVAPI_OK  if the call succeeds.
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
class _NVAPI_ANSEL_FEATURE(ENUM):
    NVAPI_ANSEL_FEATURE_UNKNOWN = 0
    NVAPI_ANSEL_FEATURE_BLACK_AND_WHITE = 1
    NVAPI_ANSEL_FEATURE_HUDLESS = 2


NVAPI_ANSEL_FEATURE = _NVAPI_ANSEL_FEATURE


class _NVAPI_ANSEL_FEATURE_STATE(ENUM):
    NVAPI_ANSEL_FEATURE_STATE_UNKNOWN = 0
    NVAPI_ANSEL_FEATURE_STATE_ENABLE = 1
    NVAPI_ANSEL_FEATURE_STATE_DISABLE = 2


NVAPI_ANSEL_FEATURE_STATE = _NVAPI_ANSEL_FEATURE_STATE


class _NVAPI_ANSEL_HOTKEY_MODIFIER(ENUM):
    NVAPI_ANSEL_HOTKEY_MODIFIER_UNKNOWN = 0
    NVAPI_ANSEL_HOTKEY_MODIFIER_CTRL = 1
    NVAPI_ANSEL_HOTKEY_MODIFIER_SHIFT = 2
    NVAPI_ANSEL_HOTKEY_MODIFIER_ALT = 3


NVAPI_ANSEL_HOTKEY_MODIFIER = _NVAPI_ANSEL_HOTKEY_MODIFIER

# not < Id of the feature
NVAPI_ANSEL_FEATURE_CONFIGURATION_STRUCT._fields_ = [
    ('featureId', NVAPI_ANSEL_FEATURE),
    # not < Whether the feature is enabled or not
    ('featureState', NVAPI_ANSEL_FEATURE_STATE),
    # not < An optional virtual key associated with this feature
    ('hotkey', UINT),
]

# not < Structure version
NVAPI_ANSEL_CONFIGURATION_STRUCT_V1._fields_ = [
    ('version', NvU32),
    # not < Modifier key to use in hotkey combination
    ('hotkeyModifier', NVAPI_ANSEL_HOTKEY_MODIFIER),
    # not < VKEY to enable/disable Ansel
    ('keyEnable', UINT),
    # not < Number of features in pAnselFeatures
    ('numAnselFeatures', UINT),
    # not < Array of features configurations
    ('pAnselFeatures', POINTER(NVAPI_ANSEL_FEATURE_CONFIGURATION_STRUCT)),
]
NVAPI_ANSEL_CONFIGURATION_STRUCT = NVAPI_ANSEL_CONFIGURATION_STRUCT_V1
NVAPI_ANSEL_CONFIGURATION_STRUCT_VER1 = (
    MAKE_NVAPI_VERSION(NVAPI_ANSEL_CONFIGURATION_STRUCT_V1, 1)
)
NVAPI_ANSEL_CONFIGURATION_STRUCT_VER = (
    NVAPI_ANSEL_CONFIGURATION_STRUCT_VER1
)

NvAPI_D3D_ConfigureAnsel = hDll.D3D_ConfigureAnsel
NvAPI_D3D_ConfigureAnsel.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D_ConfigureAnsel(__in IUnknown *pDevice,
#                                         __in NVAPI_ANSEL_CONFIGURATION_STRUCT *pNLSConfig);

# not SUPPORTED OS: Windows 8 and higher
# not

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_CreateTiledTexture2DArray
# not \since Release: 375
# not \code
# not DESCRIPTION: Tiled resource is supported for Texture2D Array,
# however, but only when mip packing is not triggered.
# not    So any mip level cannot be smaller than a single tile
# size(64KB).
# not    This set of API is an extension of D3D11 support for tiled
# resource to allow a tiled texture2D array with mip packing.
# not    If any of API from this set is used, using all of them is
# highly recommended.
# not    It includes NvAPI_D3D11_CreateTiledTexture2DArray,
# NvAPI_D3D11_TiledTexture2DArrayGetDesc,
# not    NvAPI_D3D11_UpdateTileMappings, NvAPI_D3D11_CopyTileMappings,
# NvAPI_D3D11_TiledResourceBarrier.
# not    Reminder: all API in this set other than
# NvAPI_D3D11_CreateTiledTexture2DArray won't has D3D Debug Layer
# information.
# not
# not    NvAPI_D3D11_CreateTiledTexture2DArray is an extension of
# ID3D11Device::CreateTexutre2D.
# not    Use this function to create a tiled Texture2D array with mip
# packing.
# not    Runtime doesn't know the created resource is actually a tiled
# resource.
# not    Any other D3D11 API where runtime will check whether resource
# is tiled or not has a corresponding NVAPI version and they should be
# used.
# not    Different from DX12 implementation, this API should only be
# called when creating a tiled texture2D array with mip packing.
# not    Other normal tiled resource following D3D spec must use the
# standard ID3D11Device::CreateTexutre2D to create.
# not
# not  \param [in]  pDevice   current d3d device
# not  \param [in]  pDesc   The Texture2D Array descriptor, ArraySize
# > 1 and (pDesc.MiscFlags & D3D11_RESOURCE_MISC_TILED)
# not  \param [in]  pInitialData  A pointer to an array of
# D3D11_SUBRESOURCE_DATA structures that describe subresources for the
# 2D texture resource.
# not  \param [out]  ppTexture2D  A pointer to a buffer that receives
# a pointer to a ID3D11Texture2D interface for the created texture.
# not
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# not
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_CreateTiledTexture2DArray = hDll.D3D11_CreateTiledTexture2DArray
NvAPI_D3D11_CreateTiledTexture2DArray.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_D3D11_CreateTiledTexture2DArray(__in       ID3D11Device           *pDevice,
#                                                      __in const D3D11_TEXTURE2D_DESC   *pDesc,
#                                                      __in const D3D11_SUBRESOURCE_DATA *pInitialData,
#                                                      __out      ID3D11Texture2D        **ppTexture2D);

# not SUPPORTED OS: Windows 10 and higher
# not

class _NV_D3D11_FEATURE(ENUM):
    NV_D3D11_FEATURE_RASTERIZER = 1


NV_D3D11_FEATURE = _NV_D3D11_FEATURE

_NV_D3D11_FEATURE_DATA_RASTERIZER_SUPPORT._fields_ = [
    ('TargetIndependentRasterWithDepth', BOOL),
    ('ProgrammableSamplePositions', BOOL),
    ('InterleavedSampling', BOOL),
    ('ConservativeRaster', BOOL),
    ('PostZCoverage', BOOL),
    ('CoverageToColor', BOOL),
]

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_CheckFeatureSupport
# not DESCRIPTION: This function gets information about the features
# that are supported by the current graphics driver.
# not
# not
# not
# not \param [in]  pDevice    The device on which to query for support.
# not \param [in]  Feature    A member of the NvAPI_D3D11_FEATURE
# enumerated type that describes which feature to query for suppor.
# not \param [in]  pFeatureSupportData  Upon completion of the method,
# the passed structure is filled with data that describes the feature
# support.
# not \param [out]  FeatureSupportDataSize The size of the structure
# passed to the pFeatureSupportData parameter.
# not
# not \since Release: 410
# not
# not RETURN STATUS:  This API can return any of the error codes
# enumerated in NvAPI_Status.
# not \retval ::  Returns NVAPI_OK if successful; returns
# NVAPI_INVALID_ARGUMENT if an unsupported data type is passed to the
# pFeatureSupportData parameter
# not    or a size mismatch is detected for the FeatureSupportDataSize
# parameter;
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_CheckFeatureSupport = hDll.D3D11_CheckFeatureSupport
NvAPI_D3D11_CheckFeatureSupport.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_CheckFeatureSupport(__in  ID3D11Device        *pDevice,
#                                                __in  NV_D3D11_FEATURE    Feature,
#                                                __out VOID                *pFeatureSupportData,
#                                                __in  UINT                FeatureSupportDataSize);

# not SUPPORTED OS: Windows 10 and higher
# not

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_CreateImplicitMSAATexture2D
# not \since Release: 410
# not \code
# not DESCRIPTION: NvAPI_D3D11_CreateImplicitMSAATexture2D is a simple
# wrapper of ID3D11Device::CreateTexture2D
# not    which allows to create multisampled 2D texture that is
# exposed to DX runtime as non-multisampled texture.
# not
# not  \param [in]  pDevice Current d3d device
# not  \param [in]  pDesc  A pointer to a D3D11_TEXTURE2D_DESC
# structure that describes a 2D texture resource.
# not        To create a typeless resource that can be interpreted at
# runtime into different,
# not        compatible formats, specify a typeless format in the
# texture description.
# not        To generatemipmap levels automatically, set the number of
# mipmap levels to 0.
# not        SampleDesc.SampleCount specifies actual resource sample
# count, while D3D runtime object
# not        sees resource as non-multisampled.
# not
# not  \param [out] ppTexture2D A pointer to a buffer that receives a
# pointer to a ID3D11Texture2D interface for the
# not        created texture.
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. See MSDN for the API specific error codes.
# not
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_CreateImplicitMSAATexture2D = hDll.D3D11_CreateImplicitMSAATexture2D
NvAPI_D3D11_CreateImplicitMSAATexture2D.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_CreateImplicitMSAATexture2D(__in  ID3D11Device                 *pDevice,
#                                                        __in  const D3D11_TEXTURE2D_DESC   *pDesc,
#                                                        __out ID3D11Texture2D              **ppTexture2D);
# not SUPPORTED OS: Windows 10 and higher
# not

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_CreateImplicitMSAATexture2D
# not \since Release: 410
# not \code
# not DESCRIPTION: NvAPI_D3D12_CreateCommittedImplicitMSAATexture2D is
# a simple wrapper of ID3D12Device::CreateCommittedResource
# not    which allows to create multisampled 2D texture that is
# exposed to DX runtime as non-multisampled texture.
# not
# not  \param [in]  pDevice Current d3d device
# not  \param [in]  pDesc  A pointer to a D3D12_RESOURCE_DESC
# structure that describes a 2D texture resource.
# not        To create a typeless resource that can be interpreted at
# runtime into different,
# not        compatible formats, specify a typeless format in the
# texture description.
# not        To generatemipmap levels automatically, set the number of
# mipmap levels to 0.
# not        SampleDesc.SampleCount specifies actual resource sample
# count, while D3D runtime object
# not        sees resource as non-multisampled.
# not  \param [in]  pHeapProperties, HeapFlags, InitialResourceState,
# pOptimizedClearValue, riidResource See D3D12 docs
# not
# not  \param [out] ppResource Same
# ID3D12Device::CreateCommittedResource
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. See MSDN for the API specific error codes.
# not
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D12_CreateCommittedImplicitMSAATexture2D = hDll.D3D12_CreateCommittedImplicitMSAATexture2D
NvAPI_D3D12_CreateCommittedImplicitMSAATexture2D.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_D3D12_CreateCommittedImplicitMSAATexture2D(
#        __in  ID3D12Device* pDevice,
#        __in  const D3D12_HEAP_PROPERTIES *pHeapProperties,
#        D3D12_HEAP_FLAGS HeapFlags,
#        __in  const D3D12_RESOURCE_DESC *pDesc,
#        D3D12_RESOURCE_STATES InitialResourceState,
#        __in_opt  const D3D12_CLEAR_VALUE *pOptimizedClearValue,
#        REFIID riidResource,
#        __out VOID **ppvResource);

# not SUPPORTED OS: Windows 10 and higher
# not
# not \ingroup dx
# not Valid modes for NvAPI_D3D11_ResolveSubresourceRegion() and
# NvAPI_D3D12_ResolveSubresourceRegion

class _NV_RESOLVE_MODE(ENUM):
    NV_RESOLVE_MODE_SAMPLE_0 = 1


NV_RESOLVE_MODE = _NV_RESOLVE_MODE

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_ResolveSubresourceRegion
# not \since Release: 410
# not \code
# not DESCRIPTION: NvAPI_D3D11_ResolveSubresourceRegion is D3D11 an
# analog of D3D12 ResolveSubresourceRegion.
# not
# not  \param [in]  pDstResource Destination resource. Must be a
# created with the D3D11_USAGE_DEFAULT flag and be single-sampled.
# not  \param [in]  DstSubresource A zero-based index, that identifies
# the destination subresource. Use D3D11CalcSubresource to calculate
# the index.
# not  \param [in]  DstX  The X coordinate of the left-most edge of
# the destination region.
# not        The width of the destination region is the same as the
# width of the source rect.
# not
# not  \param [in]  DstY  The Y coordinate of the top-most edge of the
# destination region.
# not        The height of the destination region is the same as the
# height of the source rect.
# not
# not  \param [in]  pSrcResource Source resource. Must be multisampled.
# not  \param [in]  SrcSubresource The source subresource of the
# source resource.
# not  \param [in]  pSrcRect  Specifies the rectangular region of the
# source resource to be resolved.
# not        Passing NULL for pSrcRect specifies that the entire
# subresource is to be resolved.
# not
# not  \param [in]  Format  A DXGI_FORMAT that indicates how the
# multisampled resource will be resolved to a single-sampled resource.
# not  \param [in]  ResolveMode  Specifies the operation used to
# resolve the source samples. NV_RESOLVE_MODE_SAMPLE_0 is the only
# supported mode.
# not        NV_RESOLVE_MODE_SAMPLE_0 outputs sample 0 and discards
# all other samples.
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. See MSDN for the API specific error codes.
# not
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_ResolveSubresourceRegion = hDll.D3D11_ResolveSubresourceRegion
NvAPI_D3D11_ResolveSubresourceRegion.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_ResolveSubresourceRegion(
#     __in  ID3D11Device     *pDevice,
#     __in  ID3D11Texture2D  *pDstResource,
#     __in  UINT              DstSubresource,
#     __in  UINT              DstX,
#     __in  UINT              DstY,
#     __in  ID3D11Texture2D  *pSrcResource,
#     __in  UINT              SrcSubresource,
#     __in_opt const RECT    *pSrcRect,
#     __in  DXGI_FORMAT       Format,
#     __in  NV_RESOLVE_MODE   ResolveMode);


# not SUPPORTED OS: Windows 10 and higher
# not

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_ResolveSubresourceRegion
# not \since Release: 410
# not \code
# not DESCRIPTION: NvAPI_D3D12_ResolveSubresourceRegion is D3D11 an
# analog of D3D12 ResolveSubresourceRegion.
# not
# not  \param [in]  pDstResource Destination resource. Must be a
# created with the D3D11_USAGE_DEFAULT flag and be single-sampled.
# not  \param [in]  DstSubresource A zero-based index, that identifies
# the destination subresource. Use D3D11CalcSubresource to calculate
# the index.
# not  \param [in]  DstX  The X coordinate of the left-most edge of
# the destination region.
# not        The width of the destination region is the same as the
# width of the source rect.
# not
# not  \param [in]  DstY  The Y coordinate of the top-most edge of the
# destination region.
# not        The height of the destination region is the same as the
# height of the source rect.
# not
# not  \param [in]  pSrcResource Source resource. Must be multisampled.
# not  \param [in]  SrcSubresource The source subresource of the
# source resource.
# not  \param [in]  pSrcRect  Specifies the rectangular region of the
# source resource to be resolved.
# not        Passing NULL for pSrcRect specifies that the entire
# subresource is to be resolved.
# not
# not  \param [in]  Format  A DXGI_FORMAT that indicates how the
# multisampled resource will be resolved to a single-sampled resource.
# not  \param [in]  ResolveMode  Specifies the operation used to
# resolve the source samples. NV_RESOLVE_MODE_SAMPLE_0 is the only
# supported mode.
# not        NV_RESOLVE_MODE_SAMPLE_0 outputs sample 0 and discards
# all other samples.
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. See MSDN for the API specific error codes.
# not
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D12_ResolveSubresourceRegion = hDll.D3D12_ResolveSubresourceRegion
NvAPI_D3D12_ResolveSubresourceRegion.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_ResolveSubresourceRegion(
#     __in     ID3D12GraphicsCommandList1*pCommandList,
#     __in     ID3D12Resource            *pDstResource,
#     __in     UINT                       DstSubresource,
#     __in     UINT                       DstX,
#     __in     UINT                       DstY,
#     __in     ID3D12Resource            *pSrcResource,
#     __in     UINT                       SrcSubresource,
#     __in_opt RECT                      *pSrcRect,
#     __in     DXGI_FORMAT                Format,
#     __in     NV_RESOLVE_MODE            ResolveMode);


# not SUPPORTED OS: Windows 8 and higher
# not

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_TiledTexture2DArrayGetDesc
# not \since Release: 375
# not \code
# not DESCRIPTION: NvAPI_D3D11_TiledTexture2DArrayGetDesc is an simple
# wrapper of ID3D11Texture2D::GetDesc
# not    when pTiledTexture2DArray is created with
# NvAPI_D3D11_CreateTiledTexture2DArray.
# not    Runtime doesn't know the created resource is actually a tiled
# resource.
# not    So calling ID3D11Texture2D::GetDesc will get a desc without
# D3D11_RESOURCE_MISC_TILED in MiscFlags.
# not    This wrapper API just adds D3D11_RESOURCE_MISC_TILED back.
# not
# not  \param [in]  pTiledTexture2DArray Pointer of tiled texture2D
# array to get resource desc from.
# not  \param [out]  pDesc    Pointer to a resource description.
# not
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# not
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_TiledTexture2DArrayGetDesc = hDll.D3D11_TiledTexture2DArrayGetDesc
NvAPI_D3D11_TiledTexture2DArrayGetDesc.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_TiledTexture2DArrayGetDesc(__in  ID3D11Texture2D      *pTiledTexture2DArray,
#                                                        __out D3D11_TEXTURE2D_DESC *pDesc);

# not SUPPORTED OS: Windows 8 and higher
# not

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_UpdateTileMappings
# not \since Release: 375
# not \code
# not DESCRIPTION: NvAPI_D3D11_UpdateTileMappings is an extension of
# ID3D11DeviceContext2::UpdateTileMappings.
# not    It allows pTiledResource to be a resource created with
# NvAPI_D3D11_CreateTiledTexture2DArray, and should be used only in
# such case.
# not
# not  \param [in]  pDeviceContext     Must be Immediate DeviceContext.
# not  \param [in]  pTiledResource     A pointer to the tiled texture
# 2D array resource created by NvAPI_D3D11_CreateTiledTexture2DArray.
# not  \param [in]  NumTiledResourceRegions   The number of tiled
# resource regions.
# not  \param [in]  pTiledResourceRegionStartCoordinates An array of
# D3D11_TILED_RESOURCE_COORDINATE structures that describe the
# starting coordinates of the tiled resource regions. Cannot be NULL.
# not  \param [in]  pTiledResourceRegionSizes  An array of
# D3D11_TILE_REGION_SIZE structures that describe the sizes of the
# tiled resource regions. Cannot be NULL.
# not  \param [in]  pTilePool     A pointer to the tile pool. This
# resource should be created by standard API.
# not  \param [in]  NumRanges     The number of tile-pool ranges.
# not  \param [in]  pRangeFlags     An array of D3D11_TILE_RANGE_FLAG
# values that describe each tile-pool range.
# not  \param [in]  pTilePoolStartOffsets   An array of offsets into
# the tile pool. These are 0-based tile offsets, counting in tiles
# (not bytes).
# not  \param [in]  pRangeTileCounts    An array of values that
# specify the number of tiles in each tile-pool range.
# not  \param [in]  Flags      A combination of
# D3D11_TILE_MAPPING_FLAGS values that are combined by using a bitwise
# OR operation.
# not
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# not
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////

NvAPI_D3D11_UpdateTileMappings = hDll.D3D11_UpdateTileMappings
NvAPI_D3D11_UpdateTileMappings.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_UpdateTileMappings(
#     __in       ID3D11DeviceContext2            *pDeviceContext,
#     __in       ID3D11Resource                  *pTiledResource,
#     __in       UINT                             NumTiledResourceRegions,
#     __in const D3D11_TILED_RESOURCE_COORDINATE *pTiledResourceRegionStartCoordinates,
#     __in const D3D11_TILE_REGION_SIZE          *pTiledResourceRegionSizes,
#     __in       ID3D11Buffer                    *pTilePool,
#     __in       UINT                             NumRanges,
#     __in const UINT                            *pRangeFlags,
#     __in const UINT                            *pTilePoolStartOffsets,
#     __in const UINT                            *pRangeTileCounts,
#     __in       UINT                             Flags);


# not SUPPORTED OS: Windows 8 and higher
# not

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_CopyTileMappings
# not \since Release: 375
# not \code
# not DESCRIPTION: NvAPI_D3D11_CopyTileMappings is an extension of
# ID3D11DeviceContext2::CopyTileMappings
# not    It allows pDestTiledResource or pSourceTiledResource or both
# to be created with NvAPI_D3D11_CreateTiledTexture2DArray.
# not    It should be used only in such case.
# not
# not  \param [in]  pDeviceContext     Must be Immediate DeviceContext.
# not  \param [in]  pDestTiledResource    Tiled resource created by
# NvAPI_D3D11_CreateTiledTexture2DArray to copy tile mappings into.
# not  \param [in]  pDestRegionStartCoordinate   A pointer to a
# D3D11_TILED_RESOURCE_COORDINATE structure that describes the
# starting coordinates of the destination tiled resource.
# not  \param [in]  pSourceTiledResource    Tiled resource created by
# NvAPI_D3D11_CreateTiledTexture2DArray to copy tile mappings from.
# not  \param [in]  pSourceRegionStartCoordinate  A pointer to a
# D3D11_TILED_RESOURCE_COORDINATE structure that describes the
# starting coordinates of the source tiled resource.
# not  \param [in]  pTileRegionSize    A pointer to a
# D3D11_TILE_REGION_SIZE structure that describes the size of the
# tiled region.
# not  \param [in]  Flags      A combination of
# D3D11_TILE_MAPPING_FLAGS values that are combined by using a bitwise
# OR operation.
# not
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# not
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_CopyTileMappings = hDll.D3D11_CopyTileMappings
NvAPI_D3D11_CopyTileMappings.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_CopyTileMappings(
# __in ID3D11DeviceContext * pDeviceContext,
# __in ID3D11Resource * pDestTiledResource,
# __in const D3D11_TILED_RESOURCE_COORDINATE * pDestRegionStartCoordinate,
# __in ID3D11Resource * pSourceTiledResource,
# __in const D3D11_TILED_RESOURCE_COORDINATE * pSourceRegionStartCoordinate,
# __in const D3D11_TILE_REGION_SIZE * pTileRegionSize,
# __in UINT Flags);


# not SUPPORTED OS: Windows 8 and higher
# not

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_TiledResourceBarrier
# not \since Release: 375
# not \code
# not DESCRIPTION: NvAPI_D3D11_TiledResourceBarrier is an extension of
# ID3D11DeviceContext2::TiledResourceBarrier, but only works on
# ID3D11Resource(no support for ID3D11View).
# not    If pTiledResourceAccessBeforeBarrier or
# pTiledResourceAccessAfterBarrier or both are created by
# NvAPI_D3D11_CreateTiledTexture2DArray,
# not    NvAPI_D3D11_TiledResourceBarrier must be used instead of
# ID3D11DeviceContext2::TiledResourceBarrier.
# not
# not  \param [in]  pDeviceContext     Must be Immediate DeviceContext.
# not  \param [in]  pTiledResourceAccessBeforeBarrier  Access
# operations on this resource must complete before the access
# operations on the object that pTiledResourceAccessAfterBarrier
# specifies.
# not  \param [in]  pTiledResourceAccessAfterBarrier  Access
# operations on this resource must begin after the access operations
# on the object that pTiledResourceAccessBeforeBarrier specifies.
# not
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# not
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////

NvAPI_D3D11_TiledResourceBarrier = hDll.D3D11_TiledResourceBarrier
NvAPI_D3D11_TiledResourceBarrier.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_TiledResourceBarrier(
#     __in       ID3D11DeviceContext             *pDeviceContext,
#     __in       ID3D11Resource                  *pTiledResourceAccessBeforeBarrier,
#     __in       ID3D11Resource                  *pTiledResourceAccessAfterBarrier);


# not SUPPORTED OS: Windows 7 and higher
# not

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_AliasMSAATexture2DAsNonMSAA
# not \code
# not DESCRIPTION: This function allows creating (aliasing) a non-MSAA
# Texture2D object using the same memory as the given multi-sampled
# not    texture (pInputTex). The surface created would be bloated in
# width and height but it will have SampleCount = 1
# not    For 2X MSAA: OutTex.Width = InputTex.Width * 2, outTex.Height
# = InputTex.Height
# not    For 4X MSAA: OutTex.Width = InputTex.Width * 2, outTex.Height
# = InputTex.Height * 2
# not    For 8X MSAA: OutTex.Width = InputTex.Width * 4, outTex.Height
# = InputTex.Height * 2
# not    Only textures SampleQuality = 0 can be aliased as Non MSAA
# not    The app should ensure that original texture is released only
# after the aliased copy is released.
# not
# not    This function is free-threaded create compatible i.e. it can
# be called from a different thread
# not    than the one calling immediate device setstate functions.
# not
# not  \param [in]  pDevice   current d3d device
# not  \param [in]  pInputTex   The MultiSampled Texture2D resource
# that is being aliased
# not  \param [out]  ppOutTex  The aliased non AA copy MultiSampled
# Texture2D resource
# not
# not
# not \return :: NVAPI_OK    if the call succeeds.
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////

NvAPI_D3D11_AliasMSAATexture2DAsNonMSAA = hDll.D3D11_AliasMSAATexture2DAsNonMSAA
NvAPI_D3D11_AliasMSAATexture2DAsNonMSAA.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_AliasMSAATexture2DAsNonMSAA(__in ID3D11Device *pDevice,
#                                                         __in ID3D11Texture2D *pInputTex,
#                                                         __out ID3D11Texture2D **ppOutTex);


NvAPI_D3D11_SWIZZLE_MODE = UINT


class _NV_SWIZZLE_MODE(ENUM):
    NV_SWIZZLE_POS_X = 0
    NV_SWIZZLE_NEG_X = 1
    NV_SWIZZLE_POS_Y = 2
    NV_SWIZZLE_NEG_Y = 3
    NV_SWIZZLE_POS_Z = 4
    NV_SWIZZLE_NEG_Z = 5
    NV_SWIZZLE_POS_W = 6
    NV_SWIZZLE_NEG_W = 7


NV_SWIZZLE_MODE = _NV_SWIZZLE_MODE


class _NV_SWIZZLE_OFFSET(ENUM):
    NV_SWIZZLE_OFFSET_X = 0
    NV_SWIZZLE_OFFSET_Y = 4
    NV_SWIZZLE_OFFSET_Z = 8
    NV_SWIZZLE_OFFSET_W = 12


NV_SWIZZLE_OFFSET = _NV_SWIZZLE_OFFSET

# not SUPPORTED OS: Windows 7 and higher
# not

NV_CUSTOM_SEMANTIC_MAX_LIMIT = 32


class NV_CUSTOM_SEMANTIC_TYPE(ENUM):
    NV_NONE_SEMANTIC = 0
    NV_X_RIGHT_SEMANTIC = 1
    NV_VIEWPORT_MASK_SEMANTIC = 2
    NV_XYZW_RIGHT_SEMANTIC = 3
    NV_VIEWPORT_MASK_2_SEMANTIC = 4
    NV_POSITION_SEMANTIC = 5

    # MultiView can accept upto two vec4 values. So the application
    # should not use
    NV_CLIP_DISTANCE_0_SEMANTIC = 6

    # more than 2 of the below Clip / Cull semantics in a single
    # shader.
    NV_CLIP_DISTANCE_1_SEMANTIC = 7
    NV_CULL_DISTANCE_0_SEMANTIC = 8
    NV_CULL_DISTANCE_1_SEMANTIC = 9
    NV_GENERIC_ATTRIBUTE_SEMANTIC = 10
    NV_PACKED_EYE_INDEX_SEMANTIC = 17
    NV_CUSTOM_SEMANTIC_MAX = NV_CUSTOM_SEMANTIC_MAX_LIMIT


_NV_CUSTOM_SEMANTIC._fields_ = [
    # NV_CUSTOM_SEMANTIC_VERSION
    ('version', UINT),
    # type of custom semantic (NV_CUSTOM_SEMANTIC_TYPE)
    ('NVCustomSemanticType', NV_CUSTOM_SEMANTIC_TYPE),
    # name of custom semantic e.g. "NV_X_RIGHT", "NV_VIEWPORT_MASK"
    ('NVCustomSemanticNameString', NvAPI_LongString),
    # (optional) set to TRUE to explicitly provide register number and
    # mask as below
    ('RegisterSpecified', BOOL),
    # (optional) output register which has the custom semantic.
    ('RegisterNum', NvU32),
    # (optional) output register component mask which has the custom
    # semantic (X:1, Y:2, Z:4)
    ('RegisterMask', NvU32),
    # reserved
    ('Reserved', NvU32),
]
NV_CUSTOM_SEMANTIC_VERSION = (
    MAKE_NVAPI_VERSION(NV_CUSTOM_SEMANTIC, 1)
)

NvAPI_D3D11_CREATE_GEOMETRY_SHADER_EX_V5._fields_ = [
    ('version', UINT),
    ('UseViewportMask', BOOL),
    ('OffsetRtIndexByVpIndex', BOOL),
    ('ForceFastGS', BOOL),
    ('DontUseViewportOrder', BOOL),
    ('UseAttributeSkipMask', BOOL),
    ('UseCoordinateSwizzle', BOOL),
    ('pCoordinateSwizzling', POINTER(NvAPI_D3D11_SWIZZLE_MODE)),
    # Number of custom semantics elements
    # (upto NV_CUSTOM_SEMANTIC_MAX) provided in array pointer
    # pCustomSemantics
    ('NumCustomSemantics', NvU32),
    # pointer to array of NV_CUSTOM_SEMANTIC
    ('pCustomSemantics', POINTER(NV_CUSTOM_SEMANTIC)),
    # reserved
    ('ConvertToFastGS', BOOL),
    # TRUE if creating minimal specific shaders with nvapi shader
    # extensions
    ('UseSpecificShaderExt', BOOL),
]
NvAPI_D3D11_CREATE_GEOMETRY_SHADER_EX = NvAPI_D3D11_CREATE_GEOMETRY_SHADER_EX_V5
NVAPI_D3D11_CREATEGEOMETRYSHADEREX_2_VER_5 = (
    MAKE_NVAPI_VERSION(NvAPI_D3D11_CREATE_GEOMETRY_SHADER_EX_V5, 5)
)
NVAPI_D3D11_CREATEGEOMETRYSHADEREX_2_VERSION = (
    NVAPI_D3D11_CREATEGEOMETRYSHADEREX_2_VER_5
)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_CreateGeometryShaderEx
# not \fn NvAPI_D3D11_CreateGeometryShaderEx
# not
# not DESCRIPTION: This function allows us to extend the creation of
# geometry shaders with extra bits
# not    of functionality.
# not
# not    The first parameters are identical to
# ID3D11Device::CreateGeometryShader()
# not    so please refer to its documentation for their usage.
# not
# not    The new parameter is UseViewportMask which is to tell the
# driver to create a shader
# not    that outputs a viewport mask instead when a viewport index is
# indicated.
# not    Outputting a viewport mask allows a single primitive to land
# on many different viewports
# not    as specified by the bits set in the mask, rather than to rely
# on a single number that tells it
# not    which unique viewport it would be drawn on.
# not    This can be used for example in conjunction with the setting
# of coordinates swizzling (see XXX_NVAPI function)
# not    to generates multiple adjacent views of the same primitive in
# a more efficient fashion
# not    (outputting the primitive only once).
# not
# not    This function is free-threaded create compatible i.e. it can
# be called from a different
# not    thread than the one calling immediate device setstate
# functions.
# not
# not \since Release:
# not
# not \param [in] pDevice   The device pointer
# not \param [in] pShaderBytecode  A pointer to the compiled shader.
# not \param [in] BytecodeLength  Size of the compiled geometry shader.
# not \param [in] pClassLinkage  A pointer to a class linkage
# interface. Can be NULL.
# not \param [in] UseViewportMask  Set to FALSE for custom semantic
# shaders. Tell the driver to create a shader that outputs the
# viewport mask in lieu of the viewport index. See above description.
# not \param [in] OffsetRtIndexByVpIndex Set to FALSE for custom
# semantic shaders. The Rendertarget index is offset by the viewport
# index
# not \param [in] ForceFastGS   If TRUE, GS must be written with
# maxvertexcount(1) and must pass-through input vertex 0 to the output
# without modification
# not \param [in] DontUseViewportOrder Default FALSE for Primitives
# batched per viewport to improve performance. Set TRUE for API order
# (slow).
# not \param [in] UseAttributeSkipMask reserved
# not \param [in] UseCoordinateSwizzle reserved
# not \param [in] pCoordinateSwizzling reserved
# not \param [in] NumCustomSemantics Number of custom semantics
# elements (upto NV_CUSTOM_SEMANTIC_MAX) provided in array pointer
# pCustomSemantics
# not \param [in] pCustomSemantics pointer to array of
# NV_CUSTOM_SEMANTIC
# not \param [in] ConvertToFastGS  reserved
# not \param [in] UseSpecificShaderExt TRUE if creating minimal
# specific shaders with nvapi shader extensions
# not \param [out] ppGeometryShader Address of a pointer to a
# ID3D11GeometryShader interface.
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# ///////////////////////////////////////////////////////////////////

NvAPI_D3D11_CreateGeometryShaderEx_2 = hDll.D3D11_CreateGeometryShaderEx_2
NvAPI_D3D11_CreateGeometryShaderEx_2.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_CreateGeometryShaderEx_2(__in ID3D11Device *pDevice, __in const VOID *pShaderBytecode,
#                                                      __in SIZE_T BytecodeLength, __in_opt ID3D11ClassLinkage *pClassLinkage,
#                                                      __in const NvAPI_D3D11_CREATE_GEOMETRY_SHADER_EX *pCreateGeometryShaderExArgs,
#                                                     __out ID3D11GeometryShader **ppGeometryShader);


# not SUPPORTED OS: Windows 7 and higher
# not

NvAPI_D3D11_CREATE_VERTEX_SHADER_EX_V1._fields_ = [
    ('version', UINT),
    # Number of custom semantics elements
    # (upto NV_CUSTOM_SEMANTIC_MAX) provided in array pointer
    # pCustomSemantics
    ('NumCustomSemantics', NvU32),
    # pointer to array of NV_CUSTOM_SEMANTIC
    ('pCustomSemantics', POINTER(NV_CUSTOM_SEMANTIC)),
]

NvAPI_D3D11_CREATE_VERTEX_SHADER_EX_V2._fields_ = [
    ('version', UINT),
    # Number of custom semantics elements
    # (upto NV_CUSTOM_SEMANTIC_MAX) provided in array pointer
    # pCustomSemantics
    ('NumCustomSemantics', NvU32),
    # pointer to array of NV_CUSTOM_SEMANTIC
    ('pCustomSemantics', POINTER(NV_CUSTOM_SEMANTIC)),
    # reserved
    ('UseWithFastGS', BOOL),
]

NvAPI_D3D11_CREATE_VERTEX_SHADER_EX_V3._fields_ = [
    ('version', UINT),
    # Number of custom semantics elements
    # (upto NV_CUSTOM_SEMANTIC_MAX) provided in array pointer
    # pCustomSemantics
    ('NumCustomSemantics', NvU32),
    # pointer to array of NV_CUSTOM_SEMANTIC
    ('pCustomSemantics', POINTER(NV_CUSTOM_SEMANTIC)),
    # reserved
    ('UseWithFastGS', BOOL),
    # TRUE if creating minimal specific shaders with nvapi shader
    # extensions
    ('UseSpecificShaderExt', BOOL),
]
NvAPI_D3D11_CREATE_VERTEX_SHADER_EX = NvAPI_D3D11_CREATE_VERTEX_SHADER_EX_V3
NVAPI_D3D11_CREATEVERTEXSHADEREX_VER_1 = (
    MAKE_NVAPI_VERSION(NvAPI_D3D11_CREATE_VERTEX_SHADER_EX_V1, 1)
)
NVAPI_D3D11_CREATEVERTEXSHADEREX_VER_2 = (
    MAKE_NVAPI_VERSION(NvAPI_D3D11_CREATE_VERTEX_SHADER_EX_V2, 2)
)
NVAPI_D3D11_CREATEVERTEXSHADEREX_VER_3 = (
    MAKE_NVAPI_VERSION(NvAPI_D3D11_CREATE_VERTEX_SHADER_EX_V2, 3)
)
NVAPI_D3D11_CREATEVERTEXSHADEREX_VERSION = (
    NVAPI_D3D11_CREATEVERTEXSHADEREX_VER_3
)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_CreateVertexShaderEx
# not \fn NvAPI_D3D11_CreateVertexShaderEx
# not
# not DESCRIPTION: This function allows us to extend the creation of
# vertex shaders with extra bits
# not    of functionality.
# not
# not    The first parameters are identical to
# ID3D11Device::CreateVertexShader()
# not    so please refer to its documentation for their usage.
# not
# not    The new parameter are custom semantics which allow setting of
# custom semantic variables
# not    in the shader
# not
# not    This function is free-threaded create compatible i.e. it can
# be called from a different thread
# not    than the one calling immediate device setstate functions.
# not
# not \since Release:
# not
# not \param [in] pDevice   The device pointer
# not \param [in] pShaderBytecode  A pointer to the compiled shader.
# not \param [in] BytecodeLength  Size of the compiled vertex shader.
# not \param [in] pClassLinkage  A pointer to a class linkage
# interface. Can be NULL.
# not \param [in] NumCustomSemantics Number of custom semantics
# elements (upto NV_CUSTOM_SEMANTIC_MAX) provided in array pointer
# pCustomSemantics
# not \param [in] pCustomSemantics pointer to array of
# NV_CUSTOM_SEMANTIC
# not \param [in] UseWithFastGS  reserved
# not \param [in] UseSpecificShaderExt TRUE if creating minimal
# specific shaders with nvapi shader extensions
# not \param [out] ppVertexShader  Address of a pointer to a
# ID3D11VertexShader interface.
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_CreateVertexShaderEx = hDll.D3D11_CreateVertexShaderEx
NvAPI_D3D11_CreateVertexShaderEx.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_CreateVertexShaderEx(__in ID3D11Device *pDevice, __in const VOID *pShaderBytecode,
#                                                  __in SIZE_T BytecodeLength, __in_opt ID3D11ClassLinkage *pClassLinkage,
#                                                  __in const NvAPI_D3D11_CREATE_VERTEX_SHADER_EX *pCreateVertexShaderExArgs,
#                                                  __out ID3D11VertexShader **ppVertexShader);

# not SUPPORTED OS: Windows 7 and higher
# not

NvAPI_D3D11_CREATE_HULL_SHADER_EX_V1._fields_ = [
    ('version', UINT),
    # Number of custom semantics elements
    # (upto NV_CUSTOM_SEMANTIC_MAX) provided in array pointer
    # pCustomSemantics
    ('NumCustomSemantics', NvU32),
    # pointer to array of NV_CUSTOM_SEMANTIC
    ('pCustomSemantics', POINTER(NV_CUSTOM_SEMANTIC)),
    # reserved
    ('UseWithFastGS', BOOL),
]

NvAPI_D3D11_CREATE_HULL_SHADER_EX_V2._fields_ = [
    ('version', UINT),
    # Number of custom semantics elements
    # (upto NV_CUSTOM_SEMANTIC_MAX) provided in array pointer
    # pCustomSemantics
    ('NumCustomSemantics', NvU32),
    # pointer to array of NV_CUSTOM_SEMANTIC
    ('pCustomSemantics', POINTER(NV_CUSTOM_SEMANTIC)),
    # reserved
    ('UseWithFastGS', BOOL),
    # TRUE if creating minimal specific shaders with nvapi shader
    # extensions
    ('UseSpecificShaderExt', BOOL),
]
NvAPI_D3D11_CREATE_HULL_SHADER_EX = NvAPI_D3D11_CREATE_HULL_SHADER_EX_V2
NVAPI_D3D11_CREATEHULLSHADEREX_VER_1 = (
    MAKE_NVAPI_VERSION(NvAPI_D3D11_CREATE_HULL_SHADER_EX_V1, 1)
)
NVAPI_D3D11_CREATEHULLSHADEREX_VER_2 = (
    MAKE_NVAPI_VERSION(NvAPI_D3D11_CREATE_HULL_SHADER_EX_V1, 2)
)
NVAPI_D3D11_CREATEHULLSHADEREX_VERSION = (
    NVAPI_D3D11_CREATEHULLSHADEREX_VER_2
)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_CreateHullShaderEx
# not \fn NvAPI_D3D11_CreateHullShaderEx
# not
# not DESCRIPTION: This function allows us to extend the creation of
# hull shaders with extra bits
# not    of functionality.
# not
# not    The first parameters are identical to
# ID3D11Device::CreateHullShader()
# not    so please refer to its documentation for their usage.
# not
# not    The new parameter are custom semantics which allow setting of
# custom semantic variables
# not    in the shader
# not
# not    This function is free-threaded create compatible i.e. it can
# be called from a different thread
# not    than the one calling immediate device setstate functions.
# not
# not \since Release:
# not
# not \param [in] pDevice   The device pointer
# not \param [in] pShaderBytecode  A pointer to the compiled shader.
# not \param [in] BytecodeLength  Size of the compiled hull shader.
# not \param [in] pClassLinkage  A pointer to a class linkage
# interface. Can be NULL.
# not \param [in] NumCustomSemantics Number of custom semantics
# elements (upto NV_CUSTOM_SEMANTIC_MAX) provided in array pointer
# pCustomSemantics
# not \param [in] pCustomSemantics pointer to array of
# NV_CUSTOM_SEMANTIC
# not \param [in] UseWithFastGS  reserved
# not \param [in] UseSpecificShaderExt TRUE if creating minimal
# specific shaders with nvapi shader extensions
# not \param [out] ppHullShader  Address of a pointer to a
# ID3D11HullShader interface.
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# ///////////////////////////////////////////////////////////////////

NvAPI_D3D11_CreateHullShaderEx = hDll.D3D11_CreateHullShaderEx
NvAPI_D3D11_CreateHullShaderEx.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_CreateHullShaderEx(__in ID3D11Device *pDevice, __in const VOID *pShaderBytecode,
#                                                __in SIZE_T BytecodeLength, __in_opt ID3D11ClassLinkage *pClassLinkage,
#                                                __in const NvAPI_D3D11_CREATE_HULL_SHADER_EX *pCreateHullShaderExArgs,
#                                                __out ID3D11HullShader **ppHullShader);


# not SUPPORTED OS: Windows 7 and higher
# not

NvAPI_D3D11_CREATE_DOMAIN_SHADER_EX_V1._fields_ = [
    ('version', UINT),
    # Number of custom semantics elements
    # (upto NV_CUSTOM_SEMANTIC_MAX) provided in array pointer
    # pCustomSemantics
    ('NumCustomSemantics', NvU32),
    # pointer to array of NV_CUSTOM_SEMANTIC
    ('pCustomSemantics', POINTER(NV_CUSTOM_SEMANTIC)),
]

NvAPI_D3D11_CREATE_DOMAIN_SHADER_EX_V2._fields_ = [
    ('version', UINT),
    # Number of custom semantics elements
    # (upto NV_CUSTOM_SEMANTIC_MAX) provided in array pointer
    # pCustomSemantics
    ('NumCustomSemantics', NvU32),
    # pointer to array of NV_CUSTOM_SEMANTIC
    ('pCustomSemantics', POINTER(NV_CUSTOM_SEMANTIC)),
    # reserved
    ('UseWithFastGS', BOOL),
]

NvAPI_D3D11_CREATE_DOMAIN_SHADER_EX_V3._fields_ = [
    ('version', UINT),
    # Number of custom semantics elements
    # (upto NV_CUSTOM_SEMANTIC_MAX) provided in array pointer
    # pCustomSemantics
    ('NumCustomSemantics', NvU32),
    # pointer to array of NV_CUSTOM_SEMANTIC
    ('pCustomSemantics', POINTER(NV_CUSTOM_SEMANTIC)),
    # reserved
    ('UseWithFastGS', BOOL),
    # TRUE if creating minimal specific shaders with nvapi shader
    # extensions
    ('UseSpecificShaderExt', BOOL),
]
NvAPI_D3D11_CREATE_DOMAIN_SHADER_EX = NvAPI_D3D11_CREATE_DOMAIN_SHADER_EX_V3
NVAPI_D3D11_CREATEDOMAINSHADEREX_VER_1 = (
    MAKE_NVAPI_VERSION(NvAPI_D3D11_CREATE_DOMAIN_SHADER_EX_V1, 1)
)
NVAPI_D3D11_CREATEDOMAINSHADEREX_VER_2 = (
    MAKE_NVAPI_VERSION(NvAPI_D3D11_CREATE_DOMAIN_SHADER_EX_V2, 2)
)
NVAPI_D3D11_CREATEDOMAINSHADEREX_VER_3 = (
    MAKE_NVAPI_VERSION(NvAPI_D3D11_CREATE_DOMAIN_SHADER_EX_V3, 3)
)
NVAPI_D3D11_CREATEDOMAINSHADEREX_VERSION = (
    NVAPI_D3D11_CREATEDOMAINSHADEREX_VER_3
)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_CreateDomainShaderEx
# not \fn NvAPI_D3D11_CreateDomainShaderEx
# not
# not DESCRIPTION: This function allows us to extend the creation of
# domain shaders with extra bits
# not    of functionality.
# not
# not    The first parameters are identical to
# ID3D11Device::CreateDomainShader()
# not    so please refer to its documentation for their usage.
# not
# not    The new parameter are custom semantics which allow setting of
# custom semantic variables
# not    in the shader
# not
# not    This function is free-threaded create compatible i.e. it can
# be called from a different thread
# not    than the one calling immediate device setstate functions.
# not
# not \since Release:
# not
# not \param [in] pDevice   The device pointer
# not \param [in] pShaderBytecode  A pointer to the compiled shader.
# not \param [in] BytecodeLength  Size of the compiled domain shader.
# not \param [in] pClassLinkage  A pointer to a class linkage
# interface. Can be NULL.
# not \param [in] NumCustomSemantics Number of custom semantics
# elements (upto NV_CUSTOM_SEMANTIC_MAX) provided in array pointer
# pCustomSemantics
# not \param [in] pCustomSemantics pointer to array of
# NV_CUSTOM_SEMANTIC
# not \param [in] UseWithFastGS  reserved
# not \param [in] UseSpecificShaderExt TRUE if creating minimal
# specific shaders with nvapi shader extensions
# not \param [out] ppDomainShader  Address of a pointer to a
# ID3D11DomainShader interface.
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# ///////////////////////////////////////////////////////////////////

NvAPI_D3D11_CreateDomainShaderEx = hDll.D3D11_CreateDomainShaderEx
NvAPI_D3D11_CreateDomainShaderEx.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_CreateDomainShaderEx(__in ID3D11Device *pDevice, __in const VOID *pShaderBytecode,
#                                                  __in SIZE_T BytecodeLength, __in_opt ID3D11ClassLinkage *pClassLinkage,
#                                                  __in const NvAPI_D3D11_CREATE_DOMAIN_SHADER_EX *pCreateDomainShaderExArgs,
#                                                  __out ID3D11DomainShader **ppDomainShader);


# not SUPPORTED OS: Windows 7 and higher
# not

NvAPI_D3D11_CREATE_PIXEL_SHADER_EX_V1._fields_ = [
    ('version', UINT),
    # Number of custom semantics elements
    # (upto NV_CUSTOM_SEMANTIC_MAX) provided in array pointer
    # pCustomSemantics
    ('NumCustomSemantics', NvU32),
    # pointer to array of NV_CUSTOM_SEMANTIC
    ('pCustomSemantics', POINTER(NV_CUSTOM_SEMANTIC)),
]
NVAPI_D3D11_CREATEPIXELSHADEREX_VER_1 = (
    MAKE_NVAPI_VERSION(NvAPI_D3D11_CREATE_PIXEL_SHADER_EX_V1, 1)
)

NvAPI_D3D11_CREATE_PIXEL_SHADER_EX_V2._fields_ = [
    # Always use NVAPI_D3D11_CREATEPIXELSHADEREX_VERSION
    ('version', UINT),
    # Number of custom semantics elements
    # (upto NV_CUSTOM_SEMANTIC_MAX) provided in array pointer
    # pCustomSemantics
    ('NumCustomSemantics', NvU32),
    # pointer to array of NV_CUSTOM_SEMANTIC
    ('pCustomSemantics', POINTER(NV_CUSTOM_SEMANTIC)),
    # This enables sampling within a pixel for SuperSampling mode of
    # Variable Rate Shading for relevant attributes tagged with
    # "sample" modifier
    ('bEnableSuperSamplingPredicationForVRS', NvU32, 1),
    # This enables sampling within a pixel for SuperSampling mode of
    # Variable Rate Shading for all relevant attributes
    ('bEnableSuperSamplingPredicationForVRSAllAttributes', NvU32, 1),
    # Reserved for further use
    ('reserved', NvU32, 30),
]
NvAPI_D3D11_CREATE_PIXEL_SHADER_EX = NvAPI_D3D11_CREATE_PIXEL_SHADER_EX_V2
NVAPI_D3D11_CREATEPIXELSHADEREX_VER_2 = (
    MAKE_NVAPI_VERSION(NvAPI_D3D11_CREATE_PIXEL_SHADER_EX_V2, 2)
)
NVAPI_D3D11_CREATEPIXELSHADEREX_VERSION = (
    NVAPI_D3D11_CREATEPIXELSHADEREX_VER_2
)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_CreatePixelShaderEx_2
# not \fn NvAPI_D3D11_CreatePixelShaderEx_2
# not
# not DESCRIPTION: This function allows us to extend the creation of
# pixel shaders with extra bits
# not    of functionality.
# not
# not    The first parameters are identical to
# ID3D11Device::CreatePixelShader()
# not    so please refer to its documentation for their usage.
# not
# not    The new parameter are custom semantics which allow setting of
# custom semantic variables
# not    in the shader
# not
# not    This function is free-threaded create compatible i.e. it can
# be called from a different thread
# not    than the one calling immediate device setstate functions.
# not
# not \since Release: 410
# not
# not \param [in] pDevice   The device pointer
# not \param [in] pShaderBytecode  A pointer to the compiled shader.
# not \param [in] BytecodeLength  Size of the compiled domain shader.
# not \param [in] pClassLinkage  A pointer to a class linkage
# interface. Can be NULL.
# not \param [in] NumCustomSemantics Number of custom semantics
# elements (upto NV_CUSTOM_SEMANTIC_MAX) provided in array pointer
# pCustomSemantics
# not \param [in] pCustomSemantics pointer to array of
# NV_CUSTOM_SEMANTIC
# not \param [out] ppPixelShader  Address of a pointer to a
# ID3D11PixelShader interface.
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
#
NvAPI_D3D11_CreatePixelShaderEx_2 = hDll.D3D11_CreatePixelShaderEx_2
NvAPI_D3D11_CreatePixelShaderEx_2.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_D3D11_CreatePixelShaderEx_2(__in ID3D11Device *pDevice, __in const VOID *pShaderBytecode,
#                                                  __in SIZE_T BytecodeLength, __in_opt ID3D11ClassLinkage *pClassLinkage,
#                                                  __in const NvAPI_D3D11_CREATE_PIXEL_SHADER_EX *pCreatePixelShaderExArgs,
#                                                  __out ID3D11PixelShader **ppPixelShader);


# not SUPPORTED OS: Windows 7 and higher
# not
class _NV_FASTGS_FLAGS(ENUM):
    # Causes SV_ViewportArrayIndex value to be interpreted as a
    # bitmask of viewports to broadcast to.
    NV_FASTGS_USE_VIEWPORT_MASK = 0x01

    # Causes SV_RenderTargetArrayIndex value to be offset by the
    # viewport index when broadcasting.
    NV_FASTGS_OFFSET_RT_INDEX_BY_VP_INDEX = 0x02

    # Causes broadcast primitives to be rendered strictly in API order
    # (slow).
    NV_FASTGS_STRICT_API_ORDER = 0x04


NV_FASTGS_FLAGS = _NV_FASTGS_FLAGS

NvAPI_D3D11_CREATE_FASTGS_EXPLICIT_DESC_V1._fields_ = [
    # ALWAYS == NVAPI_D3D11_CREATEFASTGSEXPLICIT_VER
    ('version', NvU32),
    # A combination of flags from NV_FASTGS_FLAGS
    ('flags', NvU32),
    # [optional] Array of 16 coordinate swizzle modes, one per
    # viewport. NULL if not used.
    ('pCoordinateSwizzling', POINTER(NvAPI_D3D11_SWIZZLE_MODE)),
]

NVAPI_D3D11_CREATEFASTGSEXPLICIT_VER1 = (
    MAKE_NVAPI_VERSION(NvAPI_D3D11_CREATE_FASTGS_EXPLICIT_DESC_V1, 1)
)
NVAPI_D3D11_CREATEFASTGSEXPLICIT_VER = (
    NVAPI_D3D11_CREATEFASTGSEXPLICIT_VER1
)
NvAPI_D3D11_CREATE_FASTGS_EXPLICIT_DESC = NvAPI_D3D11_CREATE_FASTGS_EXPLICIT_DESC_V1

# ////////////////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_CreateFastGeometryShaderExplicit
# not \fn NvAPI_D3D11_CreateFastGeometryShaderExplicit
# not
# not DESCRIPTION: This function will create a fast geometry shader
# written using an "explicit"
# not    coding style, rather than converting a standard GS. For the
# explicit coding
# not    style, the GS must be written with maxvertexcount(1), and
# must pass-through
# not    input vertex 0 to the output without modification.
# not
# not    Additional per-primitive outputs may also be computed and
# written to the single
# not    output vertex. If these outputs are read by the pixel shader,
# they must be
# not    declared with the "nointerpolation" attribute in the PS input
# signature;
# not    otherwise, visual corruption may occur. Also, unlike D3D API,
# there is no guarantee
# not    that pixel shader will get the default value of an attribute
# if that attribute is not written
# not    by the earlier shader stage in the pipeline.
# not
# not    The first four parameters are identical to
# ID3D11Device::CreateGeometryShader(),
# not    so please refer to its documentation for their usage.
# not
# not    This function is free-threaded create compatible i.e. it can
# be called from a different thread
# not    than the one calling immediate device setstate functions.
# not
# not \since Release:
# not
# not \param [in] pDevice   The device pointer
# not \param [in] pShaderBytecode  A pointer to the compiled shader.
# not \param [in] BytecodeLength  Size of the compiled geometry shader.
# not \param [in] pClassLinkage  A pointer to a class linkage
# interface. Can be NULL.
# not \param [in] pCreateFastGSArgs  A pointer to a
# NvAPI_D3D11_CREATE_FASTGS_EXPLICIT struct.
# not \param [out] ppGeometryShader Address of a pointer to a
# ID3D11GeometryShader interface.
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# ////////////////////////////////////////////////////////////////////////////////////////

NvAPI_D3D11_CreateFastGeometryShaderExplicit = hDll.D3D11_CreateFastGeometryShaderExplicit
NvAPI_D3D11_CreateFastGeometryShaderExplicit.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_CreateFastGeometryShaderExplicit(__in ID3D11Device *pDevice, __in const VOID *pShaderBytecode,
#                                                              __in SIZE_T BytecodeLength, __in_opt ID3D11ClassLinkage *pClassLinkage,
#                                                              __in const NvAPI_D3D11_CREATE_FASTGS_EXPLICIT_DESC *pCreateFastGSArgs,
#                                                              __out ID3D11GeometryShader **ppGeometryShader);


# not SUPPORTED OS: Windows 7 and higher
# not

# //////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_CreateFastGeometryShader
# not \fn NvAPI_D3D11_CreateFastGeometryShader
# not
# not DESCRIPTION: This function will convert a regular geometry
# shader into a fast GS variant if possible.
# not    It will not do any validation regarding the compatibility of
# the resulting fast GS with any
# not    Pixel shader. The validation has to be done by the
# application manually.
# not
# not    The parameters are identical to
# ID3D11Device::CreateGeometryShader()
# not    so please refer to its documentation for their usage.
# not
# not    If the shader is too complex or is not in adequate form to be
# converted to fast GS
# not    this function will simply fail. You should then call
# ID3D11Device::CreateGeometryShader()
# not    to create the regular geometry shader.
# not
# not    This function is free-threaded create compatible i.e. it can
# be called from a different thread
# not    than the one calling immediate device setstate functions.
# not
# not \since Release:
# not
# not \param [in] pDevice   The device pointer
# not \param [in] pShaderBytecode  A pointer to the compiled shader.
# not \param [in] BytecodeLength  Size of the compiled geometry shader.
# not \param [in] pClassLinkage  A pointer to a class linkage
# interface. Can be NULL.
# not \param [out] ppGeometryShader Address of a pointer to a
# ID3D11GeometryShader interface.
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# ///////////////////////////////////////////////////////////////////


NvAPI_D3D11_CreateFastGeometryShader = hDll.D3D11_CreateFastGeometryShader
NvAPI_D3D11_CreateFastGeometryShader.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_CreateFastGeometryShader(__in ID3D11Device *pDevice, __in const VOID *pShaderBytecode,
#                                                      __in SIZE_T BytecodeLength, __in_opt ID3D11ClassLinkage *pClassLinkage,
#                                                      __out ID3D11GeometryShader **ppGeometryShader);


# not SUPPORTED OS: Windows 7 and higher
# not
# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_DecompressView
# not \code
# not DESCRIPTION: This function is used to decompress a surface using
# the currently bound programmable sample positions.
# not
# not    This is needed:
# not    - When writing to a surface in a region previously rendered
# by different sample positions and no clear was done.
# not    - When reading a surface in a shader that was rendered using
# non-standard sample positions.
# not    - When copying from a surface that was rendered using
# non-standard sample positions.
# not
# not  \param [in]  pDevice   Current d3d11 device
# not  \param [in]  pDeviceContext Current d3d11 device context
# not  \param [in]  pView   Current view to decompress
# not
# not
# not \return ::NVAPI_OK  if the call succeeds.
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////

NvAPI_D3D11_DecompressView = hDll.D3D11_DecompressView
NvAPI_D3D11_DecompressView.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_D3D11_DecompressView(__in ID3D11Device* pDevice, __in ID3D11DeviceContext *pDeviceContext, __in ID3D11View* pView);


# not Enum for CreatePSO extensions.
# not \ingroup dx
class _NV_PSO_EXTENSION(ENUM):
    NV_PSO_RASTER_EXTENSION = 0
    NV_PSO_REQUEST_FASTGS_EXTENSION = 1
    NV_PSO_GEOMETRY_SHADER_EXTENSION = 2
    NV_PSO_ENABLE_DEPTH_BOUND_TEST_EXTENSION = 3
    NV_PSO_EXPLICIT_FASTGS_EXTENSION = 4
    NV_PSO_SET_SHADER_EXTNENSION_SLOT_AND_SPACE = 5
    NV_PSO_VERTEX_SHADER_EXTENSION = 6
    NV_PSO_DOMAIN_SHADER_EXTENSION = 7
    NV_PSO_HULL_SHADER_EXTENSION = 9


NV_PSO_EXTENSION = _NV_PSO_EXTENSION

NVAPI_D3D12_PSO_EXTENSION_DESC_V1._fields_ = [
    # < not Always use NV_PSO_EXTENSION_DESC_VER
    ('baseVersion', NvU32),
    ('psoExtension', NV_PSO_EXTENSION),
]
NV_PSO_EXTENSION_DESC_VER_1 = (
    MAKE_NVAPI_VERSION(NVAPI_D3D12_PSO_EXTENSION_DESC_V1, 1)
)
NV_PSO_EXTENSION_DESC_VER = NV_PSO_EXTENSION_DESC_VER_1
NVAPI_D3D12_PSO_EXTENSION_DESC = NVAPI_D3D12_PSO_EXTENSION_DESC_V1


class NVAPI_D3D12_PSO_RASTERIZER_STATE_DESC_V1(ctypes.Structure):
    pass


class NVAPI_D3D12_PSO_CREATE_FASTGS_EXPLICIT_DESC_V1(ctypes.Structure):
    pass


class NVAPI_D3D12_PSO_REQUEST_FAST_GEOMETRY_SHADER_DESC_V1(ctypes.Structure):
    pass


class NVAPI_D3D12_PSO_GEOMETRY_SHADER_DESC_V5(ctypes.Structure):
    pass


class NVAPI_D3D12_PSO_VERTEX_SHADER_DESC_V1(ctypes.Structure):
    pass


class NVAPI_D3D12_PSO_VERTEX_SHADER_DESC_V2(ctypes.Structure):
    pass


class NVAPI_D3D12_PSO_VERTEX_SHADER_DESC_V3(ctypes.Structure):
    pass


class NVAPI_D3D12_PSO_HULL_SHADER_DESC_V1(ctypes.Structure):
    pass


class NVAPI_D3D12_PSO_HULL_SHADER_DESC_V2(ctypes.Structure):
    pass


class NVAPI_D3D12_PSO_DOMAIN_SHADER_DESC_V1(ctypes.Structure):
    pass


class NVAPI_D3D12_PSO_DOMAIN_SHADER_DESC_V2(ctypes.Structure):
    pass


class NVAPI_D3D12_PSO_DOMAIN_SHADER_DESC_V3(ctypes.Structure):
    pass


class NVAPI_D3D12_PSO_ENABLE_DEPTH_BOUND_TEST_DESC_V1(ctypes.Structure):
    pass


class NVAPI_D3D12_PSO_SET_SHADER_EXTENSION_SLOT_DESC_V1(ctypes.Structure):
    pass


NVAPI_D3D12_PSO_RASTERIZER_STATE_DESC_V1._fields_ = NVAPI_D3D12_PSO_EXTENSION_DESC._fields_ + [
    ('version', NvU32),  # <! Always use NV_RASTERIZER_PSO_EXTENSION_DESC_VER
    # These are additional parameters on the top of D3D12_RASTERIZER_DESC
    ('ProgrammableSamplePositionsEnable', BOOL),  # <! enable Programmable Samples feature
    ('InterleavedSamplingEnable', BOOL),  # <! when jitter is enabled, an app need to fill the whole arrays below, otherwise only as much entries as samples
    ('SampleCount', NvU8),  # <! number of samples. In TIR N->1 it needs to match N, in non-TIR it needs to match RT sample count. Ignored if ForcePerSampleInterlock is set
    ('SamplePositionsX', NvU8 * 16),  # <! x positions in API sample order
    ('SamplePositionsY', NvU8 * 16),  # <! y positions in API sample order
    ('QuadFillMode', NVAPI_QUAD_FILLMODE),  # <! Fill a triangle outside its bounds as a screen-aligned quad, matching the tri's bounding-box or filling the full viewport.
    ('PostZCoverageEnable', BOOL),  # <! Enable pixel-shader input SV_COVERAGE to account for z-test in early-z mode.
    ('CoverageToColorEnable', BOOL),  # <! Enable output of coverage to a color render-target.
    ('CoverageToColorRTIndex', NvU8),  # <! Index of RT for coverage-to-color.
    # Added with NV_RASTERIZER_PSO_EXTENSION_DESC_VER_2
    ('TargetIndepentRasterWithDepth', BOOL),  # <! TargetIndepentRasterWithDepth = TRUE enables rasterezation mode where sample count of both raster and depth-stencil buffer are equal and do not match RT sample count.
    ('ForcedSampleCount', NvU8),  # <! Must be set when TargetIndepentRasterWithDepth is true - refers to SampleDesc.Count for the DSV
    # Reserved
    ('reserved', NvU8 * 62),  # <! reserved for expansion, set to zero.
]


NV_RASTERIZER_PSO_EXTENSION_DESC_VER_1 = (
    MAKE_NVAPI_VERSION(NVAPI_D3D12_PSO_RASTERIZER_STATE_DESC_V1, 1)
)
NV_RASTERIZER_PSO_EXTENSION_DESC_VER_2 = (
    MAKE_NVAPI_VERSION(NVAPI_D3D12_PSO_RASTERIZER_STATE_DESC_V1, 2)
)
NV_RASTERIZER_PSO_EXTENSION_DESC_VER = (
    NV_RASTERIZER_PSO_EXTENSION_DESC_VER_2
)
NVAPI_D3D12_PSO_RASTERIZER_STATE_DESC = NVAPI_D3D12_PSO_RASTERIZER_STATE_DESC_V1


NVAPI_D3D12_PSO_CREATE_FASTGS_EXPLICIT_DESC_V1._fields_ = NVAPI_D3D12_PSO_EXTENSION_DESC._fields_ + [
    ('version', NvU32),  #  ALWAYS == NV_FASTGS_EXPLICIT_PSO_EXTENSION_VER
    ('flags', NvU32),#  A combination of flags from NV_FASTGS_FLAGS
    ('pCoordinateSwizzling', POINTER(NvAPI_D3D11_SWIZZLE_MODE)),  # [optional] Array of 16 coordinate swizzle modes, one per viewport. NULL if not used.
                                                     # The output x, y, z, and w coordinates of all vertices can be set to any of the coordinates or their
                                                     # operation occurs i.e. before frustum clipping, scaling, and viewport clipping. And after
                                                     # last of vertex/tesselation/geometry shader stage, stream-out and viewport broadcast expansion (see NV_FASTGS_USE_VIEWPORT_MASK)
                                                     # pCoordinateSwizzling[i] sets the swizzle-mode of each component for viewport i.
                                                     # See NV_SWIZZLE_MODE for values of allowed swizzle modes.
                                                     # See NV_SWIZZLE_OFFSET for bit offset from where NV_SWIZZLE_MODE to be set for each component.
                                                     # For example :
                                                     # 1. To set swizzle for viewport 0 such that -  w and z are unchanged and values of x and y are swapped :
                                                     # pCoordinateSwizzling[0] = (NV_SWIZZLE_POS_W << NV_SWIZZLE_OFFSET_W) |
                                                     #                            (NV_SWIZZLE_POS_Z << NV_SWIZZLE_OFFSET_Z) |
                                                     #                            (NV_SWIZZLE_POS_X << NV_SWIZZLE_OFFSET_Y) |
                                                     #                            (NV_SWIZZLE_POS_Y << NV_SWIZZLE_OFFSET_X)
                                                     #  2. To set swizzle for viewport 0 such that -  w, z and y are unchanged and value of x is negated :
                                                     #  pCoordinateSwizzling[0] = (NV_SWIZZLE_POS_W << NV_SWIZZLE_OFFSET_W) |
                                                     #                            (NV_SWIZZLE_POS_Z << NV_SWIZZLE_OFFSET_Z) |
                                                     #                            (NV_SWIZZLE_POS_Y << NV_SWIZZLE_OFFSET_Y) |
                                                     #                            (NV_SWIZZLE_NEG_X << NV_SWIZZLE_OFFSET_X)
                                                     #  Need to set some valid combination of swizzle-modes for all viewports, irrespective of whether that viewport is set.
                                                     #  Invalid swizzle-mode for any viewport (even if that viewport is not set) may result in removal of device.

]

NV_FASTGS_EXPLICIT_PSO_EXTENSION_VER_1 = (
    MAKE_NVAPI_VERSION(NVAPI_D3D12_PSO_CREATE_FASTGS_EXPLICIT_DESC_V1, 1)
)
NV_FASTGS_EXPLICIT_PSO_EXTENSION_VER = (
    NV_FASTGS_EXPLICIT_PSO_EXTENSION_VER_1
)
NVAPI_D3D12_PSO_CREATE_FASTGS_EXPLICIT_DESC = NVAPI_D3D12_PSO_CREATE_FASTGS_EXPLICIT_DESC_V1


NVAPI_D3D12_PSO_REQUEST_FAST_GEOMETRY_SHADER_DESC_V1._fields_ = NVAPI_D3D12_PSO_EXTENSION_DESC._fields_ + [
    ('version', NvU32),  # <! Always use NV_FAST_GEOMETRY_SHADER_PSO_EXTENSION_VER

]

NV_FAST_GEOMETRY_SHADER_PSO_EXTENSION_VER_1 = (
    MAKE_NVAPI_VERSION(NVAPI_D3D12_PSO_REQUEST_FAST_GEOMETRY_SHADER_DESC_V1, 1)
)
NV_FAST_GEOMETRY_SHADER_PSO_EXTENSION_VER = (
    NV_FAST_GEOMETRY_SHADER_PSO_EXTENSION_VER_1
)
NVAPI_D3D12_PSO_REQUEST_FAST_GEOMETRY_SHADER_DESC = NVAPI_D3D12_PSO_REQUEST_FAST_GEOMETRY_SHADER_DESC_V1


NVAPI_D3D12_PSO_GEOMETRY_SHADER_DESC_V5._fields_ = NVAPI_D3D12_PSO_EXTENSION_DESC._fields_ + [
    ('version', NvU32),  # <! Always use NV_GEOMETRY_SHADER_PSO_EXTENSION_DESC_VER
    ('UseViewportMask', BOOL),
    # Set to FALSE for custom semantic shaders. Tell the driver to create a shader that outputs the viewport mask in lieu of the viewport index. See above description.
    ('OffsetRtIndexByVpIndex', BOOL),
    # Set to FALSE for custom semantic shaders. The Rendertarget index is offset by the viewport index
    ('ForceFastGS', BOOL),
    # If TRUE, GS must be written with maxvertexcount(1) and must pass-through input vertex 0 to the output without modification
    ('DontUseViewportOrder', BOOL),
    # Default FALSE for Primitives batched per viewport to improve performance. Set TRUE for API order (slow).
    ('UseAttributeSkipMask', BOOL),  # Reserved
    ('UseCoordinateSwizzle', BOOL),  # Reserved
    ('pCoordinateSwizzling', POINTER(NvAPI_D3D11_SWIZZLE_MODE)),  # Reserved
    ('NumCustomSemantics', NvU32),
    # Number of custom semantics elements (upto NV_CUSTOM_SEMANTIC_MAX) provided in array pointer pCustomSemantics
    ('pCustomSemantics', POINTER(NV_CUSTOM_SEMANTIC)),  # pointer to array of NV_CUSTOM_SEMANTIC
    ('ConvertToFastGS', BOOL),  # Tell the driver to attempt to create a fast geometry shader
    ('UseSpecificShaderExt', BOOL),  # TRUE if creating minimal specific shaders with nvapi shader extensions

]


NV_GEOMETRY_SHADER_PSO_EXTENSION_DESC_VER_5 = (
    MAKE_NVAPI_VERSION(NVAPI_D3D12_PSO_GEOMETRY_SHADER_DESC_V5, 5)
)
NV_GEOMETRY_SHADER_PSO_EXTENSION_DESC_VER = (
    NV_GEOMETRY_SHADER_PSO_EXTENSION_DESC_VER_5
)
NVAPI_D3D12_PSO_GEOMETRY_SHADER_DESC = NVAPI_D3D12_PSO_GEOMETRY_SHADER_DESC_V5


NVAPI_D3D12_PSO_VERTEX_SHADER_DESC_V1._fields_ = NVAPI_D3D12_PSO_EXTENSION_DESC._fields_ + [
    ('version', NvU32),  # <! Always use NV_VERTEX_SHADER_PSO_EXTENSION_DESC_VER
    ('NumCustomSemantics', NvU32),  #  Number of custom semantics elements (upto NV_CUSTOM_SEMANTIC_MAX) provided in array pointer pCustomSemantics
    ('pCustomSemantics', POINTER(NV_CUSTOM_SEMANTIC)),  #  Pointer to array of NV_CUSTOM_SEMANTIC

]

NVAPI_D3D12_PSO_VERTEX_SHADER_DESC_V2._fields_ = NVAPI_D3D12_PSO_VERTEX_SHADER_DESC_V1._fields_ + [
    ('UseWithFastGS', BOOL),  #  Reserved
]


NVAPI_D3D12_PSO_VERTEX_SHADER_DESC_V3._fields_ = NVAPI_D3D12_PSO_VERTEX_SHADER_DESC_V2._fields_ + [
    ('UseSpecificShaderExt', BOOL),  #  TRUE if creating minimal specific shaders with NvAPI shader extensions
]


NV_VERTEX_SHADER_PSO_EXTENSION_DESC_VER_1 = (
    MAKE_NVAPI_VERSION(NVAPI_D3D12_PSO_VERTEX_SHADER_DESC_V1, 1)
)
NV_VERTEX_SHADER_PSO_EXTENSION_DESC_VER_2 = (
    MAKE_NVAPI_VERSION(NVAPI_D3D12_PSO_VERTEX_SHADER_DESC_V2, 2)
)
NV_VERTEX_SHADER_PSO_EXTENSION_DESC_VER_3 = (
    MAKE_NVAPI_VERSION(NVAPI_D3D12_PSO_VERTEX_SHADER_DESC_V3, 3)
)
NV_VERTEX_SHADER_PSO_EXTENSION_DESC_VER = (
    NV_VERTEX_SHADER_PSO_EXTENSION_DESC_VER_3
)
NVAPI_D3D12_PSO_VERTEX_SHADER_DESC = NVAPI_D3D12_PSO_VERTEX_SHADER_DESC_V3


NVAPI_D3D12_PSO_HULL_SHADER_DESC_V1._fields_ = NVAPI_D3D12_PSO_EXTENSION_DESC._fields_ + [
    ('version', NvU32),  # <! Always use NV_HULL_SHADER_PSO_EXTENSION_DESC_VER
    ('NumCustomSemantics', NvU32),  # Number of custom semantics elements (upto NV_CUSTOM_SEMANTIC_MAX) provided in array pointer pCustomSemantics
    ('pCustomSemantics', POINTER(NV_CUSTOM_SEMANTIC)),  # Pointer to array of NV_CUSTOM_SEMANTIC
    ('UseWithFastGS', BOOL),  # Reserved

]


NVAPI_D3D12_PSO_HULL_SHADER_DESC_V2._fields_ = NVAPI_D3D12_PSO_HULL_SHADER_DESC_V1._fields_ + [
    ('UseSpecificShaderExt', BOOL),  # TRUE if creating minimal specific shaders with nvapi shader extensions
]


NV_HULL_SHADER_PSO_EXTENSION_DESC_VER_1 = (
    MAKE_NVAPI_VERSION(NVAPI_D3D12_PSO_HULL_SHADER_DESC_V1, 1)
)
NV_HULL_SHADER_PSO_EXTENSION_DESC_VER_2 = (
    MAKE_NVAPI_VERSION(NVAPI_D3D12_PSO_HULL_SHADER_DESC_V2, 2)
)
NV_HULL_SHADER_PSO_EXTENSION_DESC_VER = (
    NV_HULL_SHADER_PSO_EXTENSION_DESC_VER_2
)
NVAPI_D3D12_PSO_HULL_SHADER_DESC = NVAPI_D3D12_PSO_HULL_SHADER_DESC_V2


NVAPI_D3D12_PSO_DOMAIN_SHADER_DESC_V1._fields_ = NVAPI_D3D12_PSO_EXTENSION_DESC._fields_ + [
    ('version', NvU32),  # <! Always use NV_DOMAIN_SHADER_PSO_EXTENSION_DESC_VER
    ('NumCustomSemantics', NvU32),  #  Number of custom semantics elements (upto NV_CUSTOM_SEMANTIC_MAX) provided in array pointer pCustomSemantics
    ('pCustomSemantics', POINTER(NV_CUSTOM_SEMANTIC)),  #  Pointer to array of NV_CUSTOM_SEMANTIC

]

NVAPI_D3D12_PSO_DOMAIN_SHADER_DESC_V2._fields_ = NVAPI_D3D12_PSO_DOMAIN_SHADER_DESC_V1._fields_ + [
    ('UseWithFastGS', BOOL),  #  Reserved
]


NVAPI_D3D12_PSO_DOMAIN_SHADER_DESC_V3._fields_ = NVAPI_D3D12_PSO_DOMAIN_SHADER_DESC_V2._fields_ + [
    ('UseSpecificShaderExt', BOOL),  #  TRUE if creating minimal specific shaders with NvAPI shader extensions
]


NV_DOMAIN_SHADER_PSO_EXTENSION_DESC_VER_1 = (
    MAKE_NVAPI_VERSION(NVAPI_D3D12_PSO_DOMAIN_SHADER_DESC_V1, 1)
)
NV_DOMAIN_SHADER_PSO_EXTENSION_DESC_VER_2 = (
    MAKE_NVAPI_VERSION(NVAPI_D3D12_PSO_DOMAIN_SHADER_DESC_V2, 2)
)
NV_DOMAIN_SHADER_PSO_EXTENSION_DESC_VER_3 = (
    MAKE_NVAPI_VERSION(NVAPI_D3D12_PSO_DOMAIN_SHADER_DESC_V3, 3)
)
NV_DOMAIN_SHADER_PSO_EXTENSION_DESC_VER = (
    NV_DOMAIN_SHADER_PSO_EXTENSION_DESC_VER_3
)
NVAPI_D3D12_PSO_DOMAIN_SHADER_DESC = NVAPI_D3D12_PSO_DOMAIN_SHADER_DESC_V3


NVAPI_D3D12_PSO_ENABLE_DEPTH_BOUND_TEST_DESC_V1._fields_ = NVAPI_D3D12_PSO_EXTENSION_DESC._fields_ + [
    ('version', NvU32),  # <! Always use NV_ENABLE_DEPTH_BOUND_TEST_PSO_EXTENSION_DESC_VER
    ('EnableDBT', BOOL),

]


NV_ENABLE_DEPTH_BOUND_TEST_PSO_EXTENSION_DESC_VER_1 = (
    MAKE_NVAPI_VERSION(NVAPI_D3D12_PSO_ENABLE_DEPTH_BOUND_TEST_DESC_V1, 1)
)
NV_ENABLE_DEPTH_BOUND_TEST_PSO_EXTENSION_DESC_VER = (
    NV_ENABLE_DEPTH_BOUND_TEST_PSO_EXTENSION_DESC_VER_1
)
NVAPI_D3D12_PSO_ENABLE_DEPTH_BOUND_TEST_DESC = NVAPI_D3D12_PSO_ENABLE_DEPTH_BOUND_TEST_DESC_V1


NVAPI_D3D12_PSO_SET_SHADER_EXTENSION_SLOT_DESC_V1._fields_ = NVAPI_D3D12_PSO_EXTENSION_DESC._fields_ + [
    ('version', NvU32),  # <! Always use NV_SET_SHADER_EXTENSION_SLOT_DESC_VER
    ('uavSlot', NvU32),
    ('registerSpace', NvU32)
]

NV_SET_SHADER_EXTENSION_SLOT_DESC_VER_1 = (
    MAKE_NVAPI_VERSION(NVAPI_D3D12_PSO_SET_SHADER_EXTENSION_SLOT_DESC_V1, 1)
)
NV_SET_SHADER_EXTENSION_SLOT_DESC_VER = (
    NV_SET_SHADER_EXTENSION_SLOT_DESC_VER_1
)
NVAPI_D3D12_PSO_SET_SHADER_EXTENSION_SLOT_DESC = NVAPI_D3D12_PSO_SET_SHADER_EXTENSION_SLOT_DESC_V1


# not \ingroup dx
# not Enum for compute shader derivative modes
class _NV_COMPUTE_SHADER_DERIVATIVES(ENUM):
    NV_COMPUTE_SHADER_DERIVATIVE_NONE = 0

    # Compute derivatives supported. Quads are defined as groups of
    # four threads with linear thread IDs of the form 4N..4N + 3
    NV_COMPUTE_SHADER_DERIVATIVE_GROUP_LINEAR = 1

    # Compute derivatives supported. Quads are defined as group of 2x2
    # thread IDs in a 2D (or 3D) CTA. In this mode
    NV_COMPUTE_SHADER_DERIVATIVE_GROUP_QUADS = 2


NV_COMPUTE_SHADER_DERIVATIVES = _NV_COMPUTE_SHADER_DERIVATIVES

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_CreateGraphicsPipelineState
# not \code
# not DESCRIPTION: This function will create PSO with provided
# extensions
# not
# not \note Note that "Cached PSO" functionality is not supported with
# the Pipeline State Object created using
# not  this NvAPI. GetCachedBlob() should not be called with such a
# PSO.
# not
# not  \param [in]  pDevice   Current d3d device
# not  \param [in]  pPSODesc   PSO description of type
# D3D12_GRAPHICS_PIPELINE_STATE_DESC
# not  \param [in]  numExtensions  Number of extensions
# not  \param [in]  ppExtensions  Array of PSO extensions
# (see NV_PSO_EXTENSION for possible extensions)
# not  \param [out]  ppPSO   Output PSO object of type
# ID3D12PipelineState
# not
# not SUPPORTED OS: Windows 10
# not
# not \return ::NVAPI_OK  if the call succeeds.
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////

NvAPI_D3D12_CreateGraphicsPipelineState = hDll.D3D12_CreateGraphicsPipelineState
NvAPI_D3D12_CreateGraphicsPipelineState.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_CreateGraphicsPipelineState(__in ID3D12Device *pDevice,
#                                                         __in const D3D12_GRAPHICS_PIPELINE_STATE_DESC *pPSODesc,
#                                                           NvU32 numExtensions,
#                                                         __in const NVAPI_D3D12_PSO_EXTENSION_DESC** ppExtensions,
#                                                         __out ID3D12PipelineState **ppPSO);


# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_CreateComputePipelineState
# not \code
# not DESCRIPTION: This function will create PSO with provided
# extensions
# not
# not  \param [in]  pDevice   Current d3d device
# not  \param [in]  pPSODesc   PSO description of type
# D3D12_COMPUTE_PIPELINE_STATE_DESC
# not  \param [in]  numExtensions  Number of extensions
# not  \param [in]  ppExtensions  Array of PSO extensions
# (see NV_PSO_EXTENSION for possible extensions)
# not  \param [out]  ppPSO   Output PSO object of type
# ID3D12PipelineState
# not
# not \since Release: 364
# not
# not SUPPORTED OS: Windows 10
# not
# not \return ::NVAPI_OK  if the call succeeds.
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////

NvAPI_D3D12_CreateComputePipelineState = hDll.D3D12_CreateComputePipelineState
NvAPI_D3D12_CreateComputePipelineState.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_CreateComputePipelineState(__in ID3D12Device *pDevice,
#                                                        __in const D3D12_COMPUTE_PIPELINE_STATE_DESC *pPSODesc,
#                                                          NvU32 numExtensions,
#                                                        __in const NVAPI_D3D12_PSO_EXTENSION_DESC** ppExtensions,
#                                                        __out ID3D12PipelineState **ppPSO);


# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_SetDepthBoundsTestValues
# not \code
# not DESCRIPTION: This function will set the minDepth and maxDepth
# values for depth bounds test
# not    To enable/ disable depth bounds test use PSO extension
# NV_PSO_ENABLE_DEPTH_BOUND_TEST_EXTENSION
# not    in the nvapi NvAPI_D3D12_CreateGraphicsPipelineState
# not
# not  \param [in]  pCommandList  Command List to set depth bounds test
# not  \param [in]  minDepth   min value for depth bound test
# not  \param [in]  maxDepth   max value for depth bound test
# not
# not The valid values for minDepth and maxDepth are such that 0 <=
# minDepth <= maxDepth <= 1
# not
# not SUPPORTED OS: Windows 10
# not
# not \return ::NVAPI_OK  if the call succeeds.
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////

NvAPI_D3D12_SetDepthBoundsTestValues = hDll.D3D12_SetDepthBoundsTestValues
NvAPI_D3D12_SetDepthBoundsTestValues.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_SetDepthBoundsTestValues(__in ID3D12GraphicsCommandList *pCommandList,
#                                                      __in const float minDepth,
#                                                      __in const float maxDepth);


# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_CreateReservedResource
# not \since Release: 375
# not \code
# not DESCRIPTION: Tiled resource is supported for Texture2D Array,
# however, but only when mip packing is not triggered.
# not    So any mip level cannot be smaller than a single tile
# size(64KB).
# not    This set of API is an extension of D3D12 support for tiled
# resource to allow a tiled texture2D array with mip packing.
# not    If any of API from this set is used, using all of them is
# highly recommended.
# not    It includes NvAPI_D3D12_CreateReservedResource,
# NvAPI_D3D12_CreateHeap, NvAPI_D3D12_ReservedResourceGetDesc,
# not    NvAPI_D3D12_UpdateTileMappings, NvAPI_D3D12_CopyTileMappings,
# NvAPI_D3D12_ResourceAliasingBarrier.
# not    Reminder: all API in this set other than
# NvAPI_D3D12_CreateReservedResource won't has D3D Debug Layer
# information.
# not
# not    NvAPI_D3D12_CreateReservedResource is an extension of
# ID3D12Device::CreateReservedResource.
# not    Use this function to create a tiled Texture2D array with mip
# packing.
# not    Runtime doesn't know the created resource is actually a tiled
# resource.
# not    Any other D3D12 API where runtime will check whether resource
# is tiled or not, has a corresponding NVAPI version and they should
# be used.
# not    Different from DX11 implementation, we highly recommend
# replace all ID3D12Device::CreateReservedResource with
# NvAPI_D3D12_CreateReservedResource,
# not    and use bTexture2DArrayMipPack to control which creation to
# use.
# not    Otherwise, NvAPI_D3D12_ResourceAliasingBarrier will fail if
# any resource is not created by NvAPI_D3D12_CreateReservedResource.
# not    DX11 implementation doesn't have this restriction and
# resource created by NVAPI and D3D API can be used together.
# not    pHeap is necessary when bTexture2DArrayMipPack is true. pHeap
# can be any heap and this API doens't change anything to it.
# not
# not  \param [in]  pDevice   A pointer to D3D12 device.
# not  \param [in]  pDesc   A pointer to a D3D12_RESOURCE_DESC
# structure that describes the resource.
# not  \param [in]  InitialState   The initial state of the resource,
# as a bitwise-OR'd combination of D3D12_RESOURCE_STATES enumeration
# constants.
# not  \param [in]  pOptimizedClearValue Specifies a D3D12_CLEAR_VALUE
# that describes the default value for a clear color.
# not  \param [in]  riid    The globally unique identifier (GUID) for
# the resource interface.
# not  \param [out]  ppvResource  A pointer to a memory block that
# receives a pointer to the resource. Cannot be NULL.
# not  \param [in]  bTexture2DArrayMipPack Whether pDesc indicates
# it's a texture2D array resource with mip packing.
# not         TRUE: Use NVAPI to create. Will check pHeap to be not
# NULL.
# not         FALSE: Standard D3D12 API will be used, use DebugDevice
# to check any runtime ERROR. Won't check pHeap
# not  \param [in]  pHeap   A pointer to ID3D12Heap. Cannot be NULL
# when bTexture2DArrayMipPack is true.
# not
# not SUPPORTED OS: Windows 10
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# not
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////

NvAPI_D3D12_CreateReservedResource = hDll.D3D12_CreateReservedResource
NvAPI_D3D12_CreateReservedResource.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_CreateReservedResource(__in       ID3D12Device           *pDevice,
#                                                    __in const D3D12_RESOURCE_DESC    *pDesc,
#                                                    __in       D3D12_RESOURCE_STATES   InitialState,
#                                                    __in const D3D12_CLEAR_VALUE      *pOptimizedClearValue,
#                                                    __in       REFIID                  riid,
#                                                    __out      VOID                  **ppvResource,
#                                                    __in       bool                    bTexture2DArrayMipPack,
#                                                    __in       ID3D12Heap             *pHeap);


# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_CreateHeap
# not \since Release: 375
# not \code
# not DESCRIPTION: NvAPI_D3D12_CreateHeap is a safe replacement of
# ID3D12Device::CreateHeap with no functionality change and overhead.
# not    In NvAPI_D3D12_UpdateTileMappings, pTilePool must be created
# with NvAPI_D3D12_CreateHeap and otherwise
# NvAPI_D3D12_UpdateTileMappings will fail.
# not    In other word, any tile pool used in
# NvAPI_D3D12_UpdateTileMappings must be created by
# NvAPI_D3D12_CreateHeap.
# not
# not  \param [in]  pDevice   A pointer to D3D12 device.
# not  \param [in]  pDesc   A pointer to a D3D12_HEAP_DESC structure
# that describes the heap.
# not  \param [in]  riid    The globally unique identifier (GUID) for
# the resource interface.
# not  \param [out]  ppvHeap   A pointer to a memory block that
# receives a pointer to the heap. Cannot be NULL.
# not
# not SUPPORTED OS: Windows 10
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# not
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////

NvAPI_D3D12_CreateHeap = hDll.D3D12_CreateHeap
NvAPI_D3D12_CreateHeap.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_CreateHeap(__in       ID3D12Device     *pDevice,
#                                        __in const D3D12_HEAP_DESC  *pDesc,
#                                        __in       REFIID            riid,
#                                        __out      VOID            **ppvHeap);


# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_ReservedResourceGetDesc
# not \since Release: 375
# not \code
# not DESCRIPTION: NvAPI_D3D12_ReservedResourceGetDesc is an simple
# wrapper of ID3D12Resource::GetDesc when pReservedResource is created
# by NvAPI_D3D12_CreateReservedResource.
# not    Runtime doesn't know the created resource is actually a tiled
# resource if bTexture2DArrayMipPack = true in
# NvAPI_D3D12_CreateReservedResource.
# not    So calling ID3D12Resource::GetDesc on such resource will get
# a desc with D3D12_TEXTURE_LAYOUT_UNKNOWN in Layout instead of
# D3D12_TEXTURE_LAYOUT_64KB_UNDEFINED_SWIZZLE.
# not    This wrapper API just set Layout to
# D3D12_TEXTURE_LAYOUT_64KB_UNDEFINED_SWIZZLE if Layout is
# D3D12_TEXTURE_LAYOUT_UNKNOWN.
# not
# not  \param [in]  pReservedResource Pointer of reserved resource to
# get resource desc from.
# not  \param [out]  pDesc   Pointer to a resource description.
# not SUPPORTED OS: Windows 10
# not
# not
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# not
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D12_ReservedResourceGetDesc = hDll.D3D12_ReservedResourceGetDesc
NvAPI_D3D12_ReservedResourceGetDesc.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_ReservedResourceGetDesc(__in  ID3D12Resource      *pReservedResource,
#                                                     __out D3D12_RESOURCE_DESC *pDesc);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_UpdateTileMappings
# not \since Release: 375
# not \code
# not DESCRIPTION: NvAPI_D3D12_UpdateTileMappings is an extension of
# ID3D12CommandQueue::UpdateTileMappings.
# not    pTiledResource must be created by
# NvAPI_D3D12_CreateReservedResource.
# not    pTilePool must be created by NvAPI_D3D12_CreateHeap.
# not
# not  \param [in]  pCommandQueue    A pointer to ID3D12CommandQueue.
# not  \param [in]  pTiledResource     A pointer to the tiled resource
# created by NvAPI_D3D12_CreateReservedResource.
# not  \param [in]  NumTiledResourceRegions   The number of tiled
# resource regions.
# not  \param [in]  pTiledResourceRegionStartCoordinates An array of
# D3D12_TILED_RESOURCE_COORDINATE structures that describe the
# starting coordinates of the tiled resource regions. Cannot be NULL.
# not  \param [in]  pTiledResourceRegionSizes  An array of
# D3D12_TILE_REGION_SIZE structures that describe the sizes of the
# tiled resource regions. Cannot be NULL.
# not  \param [in]  pTilePool     A pointer to the resource heap
# created by NvAPI_D3D12_CreateHeap.
# not  \param [in]  NumRanges     The number of tile-pool ranges.
# not  \param [in]  pRangeFlags     A pointer to an array of
# D3D12_TILE_RANGE_FLAGS values that describes each tile range.
# not  \param [in]  pTilePoolStartOffsets   An array of offsets into
# the tile pool. These are 0-based tile offsets, counting in tiles
# (not bytes).
# not  \param [in]  pRangeTileCounts    An array of values that
# specify the number of tiles in each tile-pool range.
# not  \param [in]  Flags      A combination of
# D3D12_TILE_MAPPING_FLAGS values that are combined by using a bitwise
# OR operation.
# not SUPPORTED OS: Windows 10
# not
# not
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# not
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D12_UpdateTileMappings = hDll.D3D12_UpdateTileMappings
NvAPI_D3D12_UpdateTileMappings.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_UpdateTileMappings(
#     __in       ID3D12CommandQueue              *pCommandQueue,
#     __in       ID3D12Resource                  *pResource,
#     __in       UINT                             NumResourceRegions,
#     __in const D3D12_TILED_RESOURCE_COORDINATE *pResourceRegionStartCoordinates,
#     __in const D3D12_TILE_REGION_SIZE          *pResourceRegionSizes,
#     __in       ID3D12Heap                      *pHeap,
#     __in       UINT                             NumRanges,
#     __in const D3D12_TILE_RANGE_FLAGS          *pRangeFlags,
#     __in const UINT                            *pHeapRangeStartOffsets,
#     __in const UINT                            *pRangeTileCounts,
#     __in       D3D12_TILE_MAPPING_FLAGS         Flags);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_CopyTileMappings
# not \since Release: 375
# not \code
# not DESCRIPTION: NvAPI_D3D12_CopyTileMappings is an extension of
# ID3D12CommandQueue::CopyTileMappings
# not    pDstResource and pSrcResource must be created by
# NvAPI_D3D12_CreateReservedResource.
# not
# not  \param [in]  pCommandQueue    A pointer to ID3D12CommandQueue.
# not  \param [in]  pDstResource     Tiled resource created by
# NvAPI_D3D12_CreateReservedResource to copy tile mappings into.
# not  \param [in]  pDstRegionStartCoordinate  A pointer to a
# D3D12_TILED_RESOURCE_COORDINATE structure that describes the
# starting coordinates of the destination reserved resource.
# not  \param [in]  pSrcResource     Tiled resource created by
# NvAPI_D3D12_CreateReservedResource to copy tile mappings from.
# not  \param [in]  pSourceRegionStartCoordinate  A pointer to a
# D3D12_TILED_RESOURCE_COORDINATE structure that describes the
# starting coordinates of the source reserved resource.
# not  \param [in]  pTileRegionSize    A pointer to a
# D3D12_TILE_REGION_SIZE structure that describes the size of the
# reserved region.
# not  \param [in]  Flags      One member of D3D12_TILE_MAPPING_FLAGS.
# not SUPPORTED OS: Windows 10
# not
# not
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# not
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D12_CopyTileMappings = hDll.D3D12_CopyTileMappings
NvAPI_D3D12_CopyTileMappings.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_CopyTileMappings(
#     __in       ID3D12CommandQueue              *pCommandQueue,
#     __in       ID3D12Resource                  *pDstResource,
#     __in const D3D12_TILED_RESOURCE_COORDINATE *pDstRegionStartCoordinate,
#     __in       ID3D12Resource                  *pSrcResource,
#     __in const D3D12_TILED_RESOURCE_COORDINATE *pSrcRegionStartCoordinate,
#     __in const D3D12_TILE_REGION_SIZE          *pRegionSize,
#     __in       D3D12_TILE_MAPPING_FLAGS         Flags);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_ResourceAliasingBarrier
# not \since Release: 375
# not \code
# not DESCRIPTION: NvAPI_D3D12_ResourceAliasingBarrier is an extension
# of ID3D12GraphicsCommandList::ResourceBarrier, but only for
# D3D12_RESOURCE_ALIASING_BARRIER.
# not    Both resource in pBarriers must be created by
# NvAPI_D3D12_CreateReservedTexture2DArray.
# not
# not  \param [in]  pCommandList     A pointer to
# ID3D12GraphicsCommandList.
# not  \param [in]  NumBarriers      The number of submitted barrier
# descriptions.
# not  \param [in]  pBarriers      Pointer to an array of barrier
# descriptions with D3D12_RESOURCE_ALIASING_BARRIER type only.
# not SUPPORTED OS: Windows 10
# not
# not
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# not
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D12_ResourceAliasingBarrier = hDll.D3D12_ResourceAliasingBarrier
NvAPI_D3D12_ResourceAliasingBarrier.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_D3D12_ResourceAliasingBarrier(
#     __in       ID3D12GraphicsCommandList *pCommandList,
#     __in       UINT                       NumBarriers,
#     __in const D3D12_RESOURCE_BARRIER    *pBarriers);

# ///////////////////////////////////////////////////////////////////
# MetaCommands common defines
# not \since Release: 400
# ///////////////////////////////////////////////////////////////////
class NV_D3D_GRAPHICS_STATES(ENUM):
    NV_D3D_GRAPHICS_STATE_NONE = 0
    NV_D3D_GRAPHICS_STATE_IA_VERTEX_BUFFERS = 1 << 0
    NV_D3D_GRAPHICS_STATE_IA_INDEX_BUFFER = 1 << 1
    NV_D3D_GRAPHICS_STATE_IA_PRIMITIVE_TOPOLOGY = 1 << 2
    NV_D3D_GRAPHICS_STATE_DESCRIPTOR_HEAP = 1 << 3
    NV_D3D_GRAPHICS_STATE_GRAPHICS_ROOT_SIGNATURE = 1 << 4
    NV_D3D_GRAPHICS_STATE_COMPUTE_ROOT_SIGNATURE = 1 << 5
    NV_D3D_GRAPHICS_STATE_RS_VIEWPORTS = 1 << 6
    NV_D3D_GRAPHICS_STATE_RS_SCISSOR_RECTS = 1 << 7
    NV_D3D_GRAPHICS_STATE_PREDICATION = 1 << 8
    NV_D3D_GRAPHICS_STATE_OM_RENDER_TARGETS = 1 << 9
    NV_D3D_GRAPHICS_STATE_OM_STENCIL_REF = 1 << 10
    NV_D3D_GRAPHICS_STATE_OM_BLEND_FACTOR = 1 << 11
    NV_D3D_GRAPHICS_STATE_PIPELINE_STATE = 1 << 12
    NV_D3D_GRAPHICS_STATE_SO_TARGETS = 1 << 13
    NV_D3D_GRAPHICS_STATE_OM_DEPTH_BOUNDS = 1 << 14
    NV_D3D_GRAPHICS_STATE_SAMPLE_POSITIONS = 1 << 15
    NV_D3D_GRAPHICS_STATE_VIEW_INSTANCE_MASK = 1 << 16


NV_D3D_GRAPHICS_STATE_NONE = NV_D3D_GRAPHICS_STATES.NV_D3D_GRAPHICS_STATE_NONE
NV_D3D_GRAPHICS_STATE_IA_VERTEX_BUFFERS = NV_D3D_GRAPHICS_STATES.NV_D3D_GRAPHICS_STATE_IA_VERTEX_BUFFERS
NV_D3D_GRAPHICS_STATE_IA_INDEX_BUFFER = NV_D3D_GRAPHICS_STATES.NV_D3D_GRAPHICS_STATE_IA_INDEX_BUFFER
NV_D3D_GRAPHICS_STATE_IA_PRIMITIVE_TOPOLOGY = NV_D3D_GRAPHICS_STATES.NV_D3D_GRAPHICS_STATE_IA_PRIMITIVE_TOPOLOGY
NV_D3D_GRAPHICS_STATE_DESCRIPTOR_HEAP = NV_D3D_GRAPHICS_STATES.NV_D3D_GRAPHICS_STATE_DESCRIPTOR_HEAP
NV_D3D_GRAPHICS_STATE_GRAPHICS_ROOT_SIGNATURE = NV_D3D_GRAPHICS_STATES.NV_D3D_GRAPHICS_STATE_GRAPHICS_ROOT_SIGNATURE
NV_D3D_GRAPHICS_STATE_COMPUTE_ROOT_SIGNATURE = NV_D3D_GRAPHICS_STATES.NV_D3D_GRAPHICS_STATE_COMPUTE_ROOT_SIGNATURE
NV_D3D_GRAPHICS_STATE_RS_VIEWPORTS = NV_D3D_GRAPHICS_STATES.NV_D3D_GRAPHICS_STATE_RS_VIEWPORTS
NV_D3D_GRAPHICS_STATE_RS_SCISSOR_RECTS = NV_D3D_GRAPHICS_STATES.NV_D3D_GRAPHICS_STATE_RS_SCISSOR_RECTS
NV_D3D_GRAPHICS_STATE_PREDICATION = NV_D3D_GRAPHICS_STATES.NV_D3D_GRAPHICS_STATE_PREDICATION
NV_D3D_GRAPHICS_STATE_OM_RENDER_TARGETS = NV_D3D_GRAPHICS_STATES.NV_D3D_GRAPHICS_STATE_OM_RENDER_TARGETS
NV_D3D_GRAPHICS_STATE_OM_STENCIL_REF = NV_D3D_GRAPHICS_STATES.NV_D3D_GRAPHICS_STATE_OM_STENCIL_REF
NV_D3D_GRAPHICS_STATE_OM_BLEND_FACTOR = NV_D3D_GRAPHICS_STATES.NV_D3D_GRAPHICS_STATE_OM_BLEND_FACTOR
NV_D3D_GRAPHICS_STATE_PIPELINE_STATE = NV_D3D_GRAPHICS_STATES.NV_D3D_GRAPHICS_STATE_PIPELINE_STATE
NV_D3D_GRAPHICS_STATE_SO_TARGETS = NV_D3D_GRAPHICS_STATES.NV_D3D_GRAPHICS_STATE_SO_TARGETS
NV_D3D_GRAPHICS_STATE_OM_DEPTH_BOUNDS = NV_D3D_GRAPHICS_STATES.NV_D3D_GRAPHICS_STATE_OM_DEPTH_BOUNDS
NV_D3D_GRAPHICS_STATE_SAMPLE_POSITIONS = NV_D3D_GRAPHICS_STATES.NV_D3D_GRAPHICS_STATE_SAMPLE_POSITIONS
NV_D3D_GRAPHICS_STATE_VIEW_INSTANCE_MASK = NV_D3D_GRAPHICS_STATES.NV_D3D_GRAPHICS_STATE_VIEW_INSTANCE_MASK

NVAPI_META_COMMAND_DESC._fields_ = [
    ('Id', GUID),
    ('Name', LPCWSTR),
    # states that the initialization and execution of the metacommand
    # will dirty
    ('InitializationDirtyState', NV_D3D_GRAPHICS_STATES),
    ('ExecutionDirtyState', NV_D3D_GRAPHICS_STATES),
]
NV_META_COMMAND_BOOL = NvU64
NV_META_COMMAND_MAX_TENSOR_DIM = 5

# dimensions (Size and Stride) are always indexed this way,
# irrespective of NV_META_COMMAND_LAYOUT
# For DimensionCount = 5: N, C, D, H, W
# For DimensionCount = 4: N, C, H, W
NV_META_COMMAND_ACTIVATION_MAX_PARAMS = 2


def compile_time_assert(b):
    pass


class NV_META_COMMAND_TENSOR_DATA_TYPE(ENUM):
    NV_META_COMMAND_TENSOR_DATA_TYPE_FLOAT32 = 1
    NV_META_COMMAND_TENSOR_DATA_TYPE_FLOAT16 = 2
    NV_META_COMMAND_TENSOR_DATA_TYPE_UINT32 = 3
    NV_META_COMMAND_TENSOR_DATA_TYPE_COUNT = 4


NV_META_COMMAND_TENSOR_DATA_TYPE_FLOAT32 = NV_META_COMMAND_TENSOR_DATA_TYPE.NV_META_COMMAND_TENSOR_DATA_TYPE_FLOAT32
NV_META_COMMAND_TENSOR_DATA_TYPE_FLOAT16 = NV_META_COMMAND_TENSOR_DATA_TYPE.NV_META_COMMAND_TENSOR_DATA_TYPE_FLOAT16
NV_META_COMMAND_TENSOR_DATA_TYPE_UINT32 = NV_META_COMMAND_TENSOR_DATA_TYPE.NV_META_COMMAND_TENSOR_DATA_TYPE_UINT32
NV_META_COMMAND_TENSOR_DATA_TYPE_COUNT = NV_META_COMMAND_TENSOR_DATA_TYPE.NV_META_COMMAND_TENSOR_DATA_TYPE_COUNT


class NV_META_COMMAND_TENSOR_LAYOUT(ENUM):
    NV_META_COMMAND_TENSOR_LAYOUT_UNKNOWN = 1

    # NCDHW - planar / row major layout
    # (width is inner-most dimension, batch-size N is the outermost)
    #
    NV_META_COMMAND_TENSOR_LAYOUT_STANDARD = 2
    NV_META_COMMAND_TENSOR_LAYOUT_COUNT = 3


NV_META_COMMAND_TENSOR_LAYOUT_UNKNOWN = NV_META_COMMAND_TENSOR_LAYOUT.NV_META_COMMAND_TENSOR_LAYOUT_UNKNOWN
NV_META_COMMAND_TENSOR_LAYOUT_STANDARD = NV_META_COMMAND_TENSOR_LAYOUT.NV_META_COMMAND_TENSOR_LAYOUT_STANDARD
NV_META_COMMAND_TENSOR_LAYOUT_COUNT = NV_META_COMMAND_TENSOR_LAYOUT.NV_META_COMMAND_TENSOR_LAYOUT_COUNT


class NV_META_COMMAND_TENSOR_FLAGS(ENUM):
    NV_META_COMMAND_TENSOR_FLAG_NONE = 0

    # data pointed by the tensor is static
    # (i.e, won't be modified after command list recording)
    NV_META_COMMAND_TENSOR_FLAG_DATA_STATIC = 0x1


NV_META_COMMAND_TENSOR_FLAG_NONE = NV_META_COMMAND_TENSOR_FLAGS.NV_META_COMMAND_TENSOR_FLAG_NONE
NV_META_COMMAND_TENSOR_FLAG_DATA_STATIC = NV_META_COMMAND_TENSOR_FLAGS.NV_META_COMMAND_TENSOR_FLAG_DATA_STATIC


class NV_META_COMMAND_PRECISION(ENUM):
    NV_META_COMMAND_PRECISION_FLOAT32 = 1
    NV_META_COMMAND_PRECISION_FLOAT16 = 2
    NV_META_COMMAND_PRECISION_MUL_FLOAT16_ADD_FLOAT32 = 3
    NV_META_COMMAND_PRECISION_COUNT = 4


NV_META_COMMAND_PRECISION_FLOAT32 = NV_META_COMMAND_PRECISION.NV_META_COMMAND_PRECISION_FLOAT32
NV_META_COMMAND_PRECISION_FLOAT16 = NV_META_COMMAND_PRECISION.NV_META_COMMAND_PRECISION_FLOAT16
NV_META_COMMAND_PRECISION_MUL_FLOAT16_ADD_FLOAT32 = NV_META_COMMAND_PRECISION.NV_META_COMMAND_PRECISION_MUL_FLOAT16_ADD_FLOAT32
NV_META_COMMAND_PRECISION_COUNT = NV_META_COMMAND_PRECISION.NV_META_COMMAND_PRECISION_COUNT

NV_META_COMMAND_TENSOR_DESC._fields_ = [
    # NV_META_COMMAND_TENSOR_DATA_TYPE
    ('DataType', NvU64),
    # NV_META_COMMAND_TENSOR_LAYOUT
    ('Layout', NvU64),
    # NV_META_COMMAND_TENSOR_FLAGS
    ('Flags', NvU64),
    # 4 or 5
    ('DimensionCount', NvU64),
    ('Size', NvU64 * NV_META_COMMAND_MAX_TENSOR_DIM),
    # only used with NV_META_COMMAND_TENSOR_LAYOUT_STANDARD
    ('Stride', NvU64 * NV_META_COMMAND_MAX_TENSOR_DIM),
]


class NV_META_COMMAND_ACTIVATION_FUNCTION(ENUM):
    NV_META_COMMAND_ACTIVATION_FUNCTION_ELU = 1
    NV_META_COMMAND_ACTIVATION_FUNCTION_HARDMAX = 2
    NV_META_COMMAND_ACTIVATION_FUNCTION_HARD_SIGMOID = 3
    NV_META_COMMAND_ACTIVATION_FUNCTION_IDENTITY = 4
    NV_META_COMMAND_ACTIVATION_FUNCTION_LEAKY_RELU = 5
    NV_META_COMMAND_ACTIVATION_FUNCTION_LINEAR = 6
    NV_META_COMMAND_ACTIVATION_FUNCTION_LOG_SOFTMAX = 7
    NV_META_COMMAND_ACTIVATION_FUNCTION_PARAMETERIZED_RELU = 8
    NV_META_COMMAND_ACTIVATION_FUNCTION_PARAMETRIC_SOFTPLUS = 9
    NV_META_COMMAND_ACTIVATION_FUNCTION_RELU = 10
    NV_META_COMMAND_ACTIVATION_FUNCTION_SCALED_ELU = 11
    NV_META_COMMAND_ACTIVATION_FUNCTION_SCALED_TANH = 12
    NV_META_COMMAND_ACTIVATION_FUNCTION_SIGMOID = 13
    NV_META_COMMAND_ACTIVATION_FUNCTION_SOFTMAX = 14
    NV_META_COMMAND_ACTIVATION_FUNCTION_SOFTPLUS = 15
    NV_META_COMMAND_ACTIVATION_FUNCTION_SOFTSIGN = 16
    NV_META_COMMAND_ACTIVATION_FUNCTION_TANH = 17
    NV_META_COMMAND_ACTIVATION_FUNCTION_THRESHOLDED_RELU = 18
    NV_META_COMMAND_ACTIVATION_FUNCTION_COUNT = 19


NV_META_COMMAND_ACTIVATION_FUNCTION_ELU = NV_META_COMMAND_ACTIVATION_FUNCTION.NV_META_COMMAND_ACTIVATION_FUNCTION_ELU
NV_META_COMMAND_ACTIVATION_FUNCTION_HARDMAX = NV_META_COMMAND_ACTIVATION_FUNCTION.NV_META_COMMAND_ACTIVATION_FUNCTION_HARDMAX
NV_META_COMMAND_ACTIVATION_FUNCTION_HARD_SIGMOID = NV_META_COMMAND_ACTIVATION_FUNCTION.NV_META_COMMAND_ACTIVATION_FUNCTION_HARD_SIGMOID
NV_META_COMMAND_ACTIVATION_FUNCTION_IDENTITY = NV_META_COMMAND_ACTIVATION_FUNCTION.NV_META_COMMAND_ACTIVATION_FUNCTION_IDENTITY
NV_META_COMMAND_ACTIVATION_FUNCTION_LEAKY_RELU = NV_META_COMMAND_ACTIVATION_FUNCTION.NV_META_COMMAND_ACTIVATION_FUNCTION_LEAKY_RELU
NV_META_COMMAND_ACTIVATION_FUNCTION_LINEAR = NV_META_COMMAND_ACTIVATION_FUNCTION.NV_META_COMMAND_ACTIVATION_FUNCTION_LINEAR
NV_META_COMMAND_ACTIVATION_FUNCTION_LOG_SOFTMAX = NV_META_COMMAND_ACTIVATION_FUNCTION.NV_META_COMMAND_ACTIVATION_FUNCTION_LOG_SOFTMAX
NV_META_COMMAND_ACTIVATION_FUNCTION_PARAMETERIZED_RELU = NV_META_COMMAND_ACTIVATION_FUNCTION.NV_META_COMMAND_ACTIVATION_FUNCTION_PARAMETERIZED_RELU
NV_META_COMMAND_ACTIVATION_FUNCTION_PARAMETRIC_SOFTPLUS = NV_META_COMMAND_ACTIVATION_FUNCTION.NV_META_COMMAND_ACTIVATION_FUNCTION_PARAMETRIC_SOFTPLUS
NV_META_COMMAND_ACTIVATION_FUNCTION_RELU = NV_META_COMMAND_ACTIVATION_FUNCTION.NV_META_COMMAND_ACTIVATION_FUNCTION_RELU
NV_META_COMMAND_ACTIVATION_FUNCTION_SCALED_ELU = NV_META_COMMAND_ACTIVATION_FUNCTION.NV_META_COMMAND_ACTIVATION_FUNCTION_SCALED_ELU
NV_META_COMMAND_ACTIVATION_FUNCTION_SCALED_TANH = NV_META_COMMAND_ACTIVATION_FUNCTION.NV_META_COMMAND_ACTIVATION_FUNCTION_SCALED_TANH
NV_META_COMMAND_ACTIVATION_FUNCTION_SIGMOID = NV_META_COMMAND_ACTIVATION_FUNCTION.NV_META_COMMAND_ACTIVATION_FUNCTION_SIGMOID
NV_META_COMMAND_ACTIVATION_FUNCTION_SOFTMAX = NV_META_COMMAND_ACTIVATION_FUNCTION.NV_META_COMMAND_ACTIVATION_FUNCTION_SOFTMAX
NV_META_COMMAND_ACTIVATION_FUNCTION_SOFTPLUS = NV_META_COMMAND_ACTIVATION_FUNCTION.NV_META_COMMAND_ACTIVATION_FUNCTION_SOFTPLUS
NV_META_COMMAND_ACTIVATION_FUNCTION_SOFTSIGN = NV_META_COMMAND_ACTIVATION_FUNCTION.NV_META_COMMAND_ACTIVATION_FUNCTION_SOFTSIGN
NV_META_COMMAND_ACTIVATION_FUNCTION_TANH = NV_META_COMMAND_ACTIVATION_FUNCTION.NV_META_COMMAND_ACTIVATION_FUNCTION_TANH
NV_META_COMMAND_ACTIVATION_FUNCTION_THRESHOLDED_RELU = NV_META_COMMAND_ACTIVATION_FUNCTION.NV_META_COMMAND_ACTIVATION_FUNCTION_THRESHOLDED_RELU
NV_META_COMMAND_ACTIVATION_FUNCTION_COUNT = NV_META_COMMAND_ACTIVATION_FUNCTION.NV_META_COMMAND_ACTIVATION_FUNCTION_COUNT

NV_META_COMMAND_ACTIVATION_DESC._fields_ = [
    # NV_META_COMMAND_ACTIVATION_FUNCTION
    ('Function', NvU64),
    ('Params', FLOAT * NV_META_COMMAND_ACTIVATION_MAX_PARAMS),
]
# END IF


class NV_META_COMMAND_PADDING_MODE(ENUM):
    NV_META_COMMAND_PADDING_ZEROS = 1
    NV_META_COMMAND_PADDING_MIRROR = 2
    NV_META_COMMAND_PADDING_CLAMP = 3
    NV_META_COMMAND_PADDING_CONSTANT = 4
    NV_META_COMMAND_PADDING_COUNT = 5


NV_META_COMMAND_PADDING_ZEROS = NV_META_COMMAND_PADDING_MODE.NV_META_COMMAND_PADDING_ZEROS
NV_META_COMMAND_PADDING_MIRROR = NV_META_COMMAND_PADDING_MODE.NV_META_COMMAND_PADDING_MIRROR
NV_META_COMMAND_PADDING_CLAMP = NV_META_COMMAND_PADDING_MODE.NV_META_COMMAND_PADDING_CLAMP
NV_META_COMMAND_PADDING_CONSTANT = NV_META_COMMAND_PADDING_MODE.NV_META_COMMAND_PADDING_CONSTANT
NV_META_COMMAND_PADDING_COUNT = NV_META_COMMAND_PADDING_MODE.NV_META_COMMAND_PADDING_COUNT

NV_META_COMMAND_PADDING_DESC._fields_ = [
    ('Mode', NV_META_COMMAND_PADDING_MODE),
    # used with NV_META_COMMAND_PADDING_CONSTANT
    ('ConstantPadVal', FLOAT),
]


# use this enum to query resource sizes using
# GetRequiredParameterResourceSize() call
class NV_META_COMMAND_RESOURCE_TYPE(ENUM):
    NV_META_COMMAND_RESOURCE_TYPE_INPUT = 0
    NV_META_COMMAND_RESOURCE_TYPE_OUTPUT = 1
    NV_META_COMMAND_RESOURCE_TYPE_FILTER = 2
    NV_META_COMMAND_RESOURCE_TYPE_WEIGHT = 2
    NV_META_COMMAND_RESOURCE_TYPE_BIAS = 3
    NV_META_COMMAND_RESOURCE_TYPE_MATRIX_A = 0
    NV_META_COMMAND_RESOURCE_TYPE_MATRIX_B = 2
    NV_META_COMMAND_RESOURCE_TYPE_MATRIX_C = 3
    NV_META_COMMAND_RESOURCE_TYPE_PERSISTENT = 4
    NV_META_COMMAND_RESOURCE_TYPE_TEMPORARY = 5


NV_META_COMMAND_RESOURCE_TYPE_INPUT = NV_META_COMMAND_RESOURCE_TYPE.NV_META_COMMAND_RESOURCE_TYPE_INPUT
NV_META_COMMAND_RESOURCE_TYPE_OUTPUT = NV_META_COMMAND_RESOURCE_TYPE.NV_META_COMMAND_RESOURCE_TYPE_OUTPUT
NV_META_COMMAND_RESOURCE_TYPE_FILTER = NV_META_COMMAND_RESOURCE_TYPE.NV_META_COMMAND_RESOURCE_TYPE_FILTER
NV_META_COMMAND_RESOURCE_TYPE_WEIGHT = NV_META_COMMAND_RESOURCE_TYPE.NV_META_COMMAND_RESOURCE_TYPE_WEIGHT
NV_META_COMMAND_RESOURCE_TYPE_BIAS = NV_META_COMMAND_RESOURCE_TYPE.NV_META_COMMAND_RESOURCE_TYPE_BIAS
NV_META_COMMAND_RESOURCE_TYPE_MATRIX_A = NV_META_COMMAND_RESOURCE_TYPE.NV_META_COMMAND_RESOURCE_TYPE_MATRIX_A
NV_META_COMMAND_RESOURCE_TYPE_MATRIX_B = NV_META_COMMAND_RESOURCE_TYPE.NV_META_COMMAND_RESOURCE_TYPE_MATRIX_B
NV_META_COMMAND_RESOURCE_TYPE_MATRIX_C = NV_META_COMMAND_RESOURCE_TYPE.NV_META_COMMAND_RESOURCE_TYPE_MATRIX_C
NV_META_COMMAND_RESOURCE_TYPE_PERSISTENT = NV_META_COMMAND_RESOURCE_TYPE.NV_META_COMMAND_RESOURCE_TYPE_PERSISTENT
NV_META_COMMAND_RESOURCE_TYPE_TEMPORARY = NV_META_COMMAND_RESOURCE_TYPE.NV_META_COMMAND_RESOURCE_TYPE_TEMPORARY

# Extended version of convolution operation that performs:
# y = act ( alpha1 * conv(x) + alpha2 * z + bias )
# alpha1 and alpha2 are either scalars or if PerChannelScaling is
# TRUE, they are vectors of
# same dimension as the bias tensor
# (vector of size equal to number of output channels)
# z (SkipConnectionResource) has same dimension as output tensor y
# (OutputResource).
NV_META_COMMAND_NUM_SPATIAL_DIM = 3


# D, H, W when DimensionCount is 3
# H, W when DimensionCount is 2

class NV_META_COMMAND_CONVOLUTION_DIRECTION(ENUM):
    NV_META_COMMAND_CONVOLUTION_DIRECTION_FORWARD = 1
    NV_META_COMMAND_CONVOLUTION_DIRECTION_BACKWARD = 2
    NV_META_COMMAND_CONVOLUTION_DIRECTION_COUNT = 3


NV_META_COMMAND_CONVOLUTION_DIRECTION_FORWARD = NV_META_COMMAND_CONVOLUTION_DIRECTION.NV_META_COMMAND_CONVOLUTION_DIRECTION_FORWARD
NV_META_COMMAND_CONVOLUTION_DIRECTION_BACKWARD = NV_META_COMMAND_CONVOLUTION_DIRECTION.NV_META_COMMAND_CONVOLUTION_DIRECTION_BACKWARD
NV_META_COMMAND_CONVOLUTION_DIRECTION_COUNT = NV_META_COMMAND_CONVOLUTION_DIRECTION.NV_META_COMMAND_CONVOLUTION_DIRECTION_COUNT


class NV_META_COMMAND_CONVOLUTION_MODE(ENUM):
    NV_META_COMMAND_CONVOLUTION_MODE_CONVOLUTION = 1
    NV_META_COMMAND_CONVOLUTION_MODE_CROSS_CORRELATION = 2
    NV_META_COMMAND_CONVOLUTION_MODE_COUNT = 3


NV_META_COMMAND_CONVOLUTION_MODE_CONVOLUTION = NV_META_COMMAND_CONVOLUTION_MODE.NV_META_COMMAND_CONVOLUTION_MODE_CONVOLUTION
NV_META_COMMAND_CONVOLUTION_MODE_CROSS_CORRELATION = NV_META_COMMAND_CONVOLUTION_MODE.NV_META_COMMAND_CONVOLUTION_MODE_CROSS_CORRELATION
NV_META_COMMAND_CONVOLUTION_MODE_COUNT = NV_META_COMMAND_CONVOLUTION_MODE.NV_META_COMMAND_CONVOLUTION_MODE_COUNT


class NV_META_COMMAND_OPTIONAL_TENSOR_DESC(ctypes.Structure):
    _fields_ = NV_META_COMMAND_TENSOR_DESC._fields_ + [
        # true when the tensor isn't needed (e.g, bias is optional)
        ('IsNull', NV_META_COMMAND_BOOL)
    ]


class NV_META_COMMAND_OPTIONAL_ACTIVATION_DESC(ctypes.Structure):
    _fields_ = NV_META_COMMAND_ACTIVATION_DESC._fields_ + [
        # true when activation isn't needed
        ('IsNull', NV_META_COMMAND_BOOL)
    ]


NV_META_COMMAND_CREATE_CONVOLUTION_EX_DESC._fields_ = [
    # Descriptor of the input tensor
    ('DescIn', NV_META_COMMAND_TENSOR_DESC),
    # Descriptor of the tensor acting as the filter kernel
    ('DescFilter', NV_META_COMMAND_TENSOR_DESC),
    # Descriptor of the optional bias tensor
    ('DescBias', NV_META_COMMAND_OPTIONAL_TENSOR_DESC),
    # Descriptor of the output tensor
    ('DescOut', NV_META_COMMAND_TENSOR_DESC),
    # Convolution mode (CROSS_CORRELATION or CONVOLUTION)
    ('Mode', NV_META_COMMAND_CONVOLUTION_MODE),
    # Convolution direction (FORWARD or BACKWARD)
    ('Direction', NV_META_COMMAND_CONVOLUTION_DIRECTION),
    # Precision at which convolution is done
    ('Precision', NV_META_COMMAND_PRECISION),
    # Optional activation function
    ('Activation', NV_META_COMMAND_OPTIONAL_ACTIVATION_DESC),
    # Padding mode (only used when output tensor dimensions are different from input tensor dimensions)
    ('Padding', NV_META_COMMAND_PADDING_DESC),
    # instead of Alpha1 and Alpha2 below
    ('PerChannelScaling', NV_META_COMMAND_BOOL),
    # that don't need scaling or skip connection
    ('Alpha1', FLOAT),
    ('Alpha2', FLOAT),
    # Strides for the filter kernel position
    ('Stride', NvU64 * NV_META_COMMAND_NUM_SPATIAL_DIM),
    # The distance per dimension between elements that are
    # multiplied
    ('Dilation', NvU64 * NV_META_COMMAND_NUM_SPATIAL_DIM),
    # Padding at the start of each dimension
    ('StartPadding', NvU64 * NV_META_COMMAND_NUM_SPATIAL_DIM),
    # Padding at the end of each dimension
    ('EndPadding', NvU64 * NV_META_COMMAND_NUM_SPATIAL_DIM),
    # Number of dimensions to which convolution occurs (2 or 3)
    ('DimensionCount', NvU64),
    # Number of channel groups convolved independently
    ('GroupCount', NvU64),
]

# Fused Convolution variants
# supported combinations right now are:
# - Convolution + Max Pooling (also optionally outputs pre-pool data)
# - 2x2 upsample + (optional) residual add + Convolution
# other combinations may be exposed in future

MetaCommand_ConvolutionExFused = GUID('{e1b112eb-decd-4ff6-85bb-1f0e3ab00414}')


class NV_META_COMMAND_CONVOLUTION_POOL_MODE(ENUM):
    NV_META_COMMAND_CONVOLUTION_POOL_MODE_NONE = 1
    NV_META_COMMAND_CONVOLUTION_POOL_MODE_REDUCTION_MAX = 2
    NV_META_COMMAND_CONVOLUTION_POOL_MODE_REDUCTION_AVG = 3
    NV_META_COMMAND_CONVOLUTION_POOL_MODE_REDUCTION_MIN = 4
    NV_META_COMMAND_CONVOLUTION_POOL_MODE_COUNT = 5


NV_META_COMMAND_CONVOLUTION_POOL_MODE_NONE = NV_META_COMMAND_CONVOLUTION_POOL_MODE.NV_META_COMMAND_CONVOLUTION_POOL_MODE_NONE
NV_META_COMMAND_CONVOLUTION_POOL_MODE_REDUCTION_MAX = NV_META_COMMAND_CONVOLUTION_POOL_MODE.NV_META_COMMAND_CONVOLUTION_POOL_MODE_REDUCTION_MAX
NV_META_COMMAND_CONVOLUTION_POOL_MODE_REDUCTION_AVG = NV_META_COMMAND_CONVOLUTION_POOL_MODE.NV_META_COMMAND_CONVOLUTION_POOL_MODE_REDUCTION_AVG
NV_META_COMMAND_CONVOLUTION_POOL_MODE_REDUCTION_MIN = NV_META_COMMAND_CONVOLUTION_POOL_MODE.NV_META_COMMAND_CONVOLUTION_POOL_MODE_REDUCTION_MIN
NV_META_COMMAND_CONVOLUTION_POOL_MODE_COUNT = NV_META_COMMAND_CONVOLUTION_POOL_MODE.NV_META_COMMAND_CONVOLUTION_POOL_MODE_COUNT


class NV_META_COMMAND_CONVOLUTION_UPSAMPLE_MODE(ENUM):
    NV_META_COMMAND_CONVOLUTION_UPSAMPLE_MODE_NONE = 1
    NV_META_COMMAND_CONVOLUTION_UPSAMPLE_MODE_REPLICATE = 2
    NV_META_COMMAND_CONVOLUTION_UPSAMPLE_MODE_BILINEAR = 3
    NV_META_COMMAND_CONVOLUTION_UPSAMPLE_MODE_COUNT = 4


NV_META_COMMAND_CONVOLUTION_UPSAMPLE_MODE_NONE = NV_META_COMMAND_CONVOLUTION_UPSAMPLE_MODE.NV_META_COMMAND_CONVOLUTION_UPSAMPLE_MODE_NONE
NV_META_COMMAND_CONVOLUTION_UPSAMPLE_MODE_REPLICATE = NV_META_COMMAND_CONVOLUTION_UPSAMPLE_MODE.NV_META_COMMAND_CONVOLUTION_UPSAMPLE_MODE_REPLICATE
NV_META_COMMAND_CONVOLUTION_UPSAMPLE_MODE_BILINEAR = NV_META_COMMAND_CONVOLUTION_UPSAMPLE_MODE.NV_META_COMMAND_CONVOLUTION_UPSAMPLE_MODE_BILINEAR
NV_META_COMMAND_CONVOLUTION_UPSAMPLE_MODE_COUNT = NV_META_COMMAND_CONVOLUTION_UPSAMPLE_MODE.NV_META_COMMAND_CONVOLUTION_UPSAMPLE_MODE_COUNT


class NV_META_COMMAND_CONVOLUTION_SKIP_MODE(ENUM):
    NV_META_COMMAND_CONVOLUTION_SKIP_MODE_NONE = 1
    NV_META_COMMAND_CONVOLUTION_SKIP_MODE_ADD = 2
    NV_META_COMMAND_CONVOLUTION_SKIP_MODE_CONCAT = 3
    NV_META_COMMAND_CONVOLUTION_SKIP_MODE_COUNT = 4


NV_META_COMMAND_CONVOLUTION_SKIP_MODE_NONE = NV_META_COMMAND_CONVOLUTION_SKIP_MODE.NV_META_COMMAND_CONVOLUTION_SKIP_MODE_NONE
NV_META_COMMAND_CONVOLUTION_SKIP_MODE_ADD = NV_META_COMMAND_CONVOLUTION_SKIP_MODE.NV_META_COMMAND_CONVOLUTION_SKIP_MODE_ADD
NV_META_COMMAND_CONVOLUTION_SKIP_MODE_CONCAT = NV_META_COMMAND_CONVOLUTION_SKIP_MODE.NV_META_COMMAND_CONVOLUTION_SKIP_MODE_CONCAT
NV_META_COMMAND_CONVOLUTION_SKIP_MODE_COUNT = NV_META_COMMAND_CONVOLUTION_SKIP_MODE.NV_META_COMMAND_CONVOLUTION_SKIP_MODE_COUNT

NV_META_COMMAND_CONVOLUTION_FUSE_DESC._fields_ = [
    ('PoolMode', NV_META_COMMAND_CONVOLUTION_POOL_MODE),
    ('UpsampleMode', NV_META_COMMAND_CONVOLUTION_UPSAMPLE_MODE),
    ('SkipMode', NV_META_COMMAND_CONVOLUTION_SKIP_MODE),
    # used with NV_META_COMMAND_CONVOLUTION_POOL_MODE
    ('OutputPrepool', NV_META_COMMAND_BOOL),
]

# uses same structures for init and execute descriptors
# SkipConnectionResource is used to specify the resource for pre-pool
# data or residual add

class NV_META_COMMAND_CREATE_CONVOLUTION_EX_FUSED_DESC(ctypes.Structure):
    _fields_ = NV_META_COMMAND_CREATE_CONVOLUTION_EX_DESC._fields_ + [
        ('FuseDesc', NV_META_COMMAND_CONVOLUTION_FUSE_DESC),
    ]

MetaCommand_Gemm = GUID('{8f9ff059-fe72-488e-a066-b14e7948ec08}')


# make sure structure sizes match what the driver assumes
# GEMM (General matrix multiply)
# Y = alpha * t(A) * t(B) + beta * C,
# where t is a matrix transform option
# If C is null, and beta is non-zero, the output
# matrix is used as C matrix. i.e, the operation performed is:
# Y = alpha * t(A) * t(B) + beta * Y

class NV_META_COMMAND_MATRIX_TRANSFORM(ENUM):
    NV_META_COMMAND_MATRIX_TRANSFORM_NONE = 1
    NV_META_COMMAND_MATRIX_TRANSFORM_TRANSPOSE = 2
    NV_META_COMMAND_MATRIX_TRANSFORM_COUNT = 3


NV_META_COMMAND_MATRIX_TRANSFORM_NONE = NV_META_COMMAND_MATRIX_TRANSFORM.NV_META_COMMAND_MATRIX_TRANSFORM_NONE
NV_META_COMMAND_MATRIX_TRANSFORM_TRANSPOSE = NV_META_COMMAND_MATRIX_TRANSFORM.NV_META_COMMAND_MATRIX_TRANSFORM_TRANSPOSE
NV_META_COMMAND_MATRIX_TRANSFORM_COUNT = NV_META_COMMAND_MATRIX_TRANSFORM.NV_META_COMMAND_MATRIX_TRANSFORM_COUNT

NV_META_COMMAND_CREATE_GEMM_DESC._fields_ = [
    ('DescA', NV_META_COMMAND_TENSOR_DESC),
    ('DescB', NV_META_COMMAND_TENSOR_DESC),
    ('DescOut', NV_META_COMMAND_TENSOR_DESC),
    ('Precision', NV_META_COMMAND_PRECISION),
    ('TransA', NV_META_COMMAND_MATRIX_TRANSFORM),
    ('TransB', NV_META_COMMAND_MATRIX_TRANSFORM),
    ('Alpha', FLOAT),
    ('Beta', FLOAT),
]

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_EnumerateMetaCommands
# not \since Release: 400
# not \code
# not DESCRIPTION: Enumerates MetaCommands supported on the system
# not
# not  \param [in]  pDevice   A pointer to D3D11 device.
# not  \param [in/out] pNumMetaCommands  Should be non-null. When the
# value pointed by pNumMetaCommands is 0 (or when pDescs is NULL), the
# function returns number of metacommands supported.
# not         When the value pointed is non-zero, the value indicates
# number of Metacommand descriptions to be populated in pDescs array.
# not  \param [out]  pDescs    Pointer to array where Metacommand
# descriptions will be returned. Can be null to indicate that the app
# is querying the number of supported metacommands.
# not         Otherwise should have enough space to hold
# *pNumMetaCommands descriptors
# not SUPPORTED OS: Windows 10
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_EnumerateMetaCommands = hDll.D3D11_EnumerateMetaCommands
NvAPI_D3D11_EnumerateMetaCommands.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_D3D11_EnumerateMetaCommands(__in                                  ID3D11Device                    *pDevice,
#                                                   __inout                               NvU32                           *pNumMetaCommands,
#                                                   __out_ecount_opt(*pNumMetaCommands)   NVAPI_META_COMMAND_DESC         *pDescs);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_CreateMetaCommand
# not \since Release: 400
# not \code
# not DESCRIPTION: Creates a MetaCommand object which can be used to
# execute optimized operations exposed by driver like convolutions.
# not
# not  \param [in]  pDevice    A pointer to D3D11 device.
# not  \param [in]  CommandId    GUID of the operations to perform
# not  \param [in]  pCreationParametersData structure containing all
# creation parameters for the requested Metacommand
# not  \param [in]  CreationParametersDataSize size of parameter data
# structure
# not  \param [out]  ppMetaCommand   A pointer to memory that receives
# the pointer to the created MetaCommand object.
# not SUPPORTED OS: Windows 10
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# not
# not   DXGI_ERROR_NOT_SUPPORTED - The requested Metacommand is not
# supported.
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
class _Union_3(ctypes.Union):
    pass


_Union_3._fields_ = [
    # NVAPI handle of a buffer resource
    # (use NvAPI_D3D11_GetResourceHandle to get this handle)
    ('ResourceHandle', NVDX_ObjectHandle),
    # to get correct sturcutre size on 32 bit builds
    ('unused', NvU64),
]
NV_D3D11_META_COMMAND_RESOURCE._Union_3 = _Union_3

NV_D3D11_META_COMMAND_RESOURCE._anonymous_ = (
    '_Union_3',
)

NV_D3D11_META_COMMAND_RESOURCE._fields_ = [
    ('_Union_3', NV_D3D11_META_COMMAND_RESOURCE._Union_3),
    # offset within the resource in bytes
    ('Offset', NvU64),
]

NV_D3D11_META_COMMAND_INITIALIZE_CONVOLUTION_EX_DESC._fields_ = [
    # use GetRequiredParameterResourceSize to query its size
    ('PersistentResource', NV_D3D11_META_COMMAND_RESOURCE),
]

NV_D3D11_META_COMMAND_EXECUTE_CONVOLUTION_EX_DESC._fields_ = [
    ('InputResource', NV_D3D11_META_COMMAND_RESOURCE),
    ('FilterResource', NV_D3D11_META_COMMAND_RESOURCE),
    # optional
    ('BiasResource', NV_D3D11_META_COMMAND_RESOURCE),
    ('OutputResource', NV_D3D11_META_COMMAND_RESOURCE),
    # should have same dimension as bias
    ('Alpha1Resource', NV_D3D11_META_COMMAND_RESOURCE),
    ('Alpha2Resource', NV_D3D11_META_COMMAND_RESOURCE),
    # optional, same dimension/descriptor as output
    ('SkipConnectionResource', NV_D3D11_META_COMMAND_RESOURCE),
    # should point to same memory that was specified at time of init
    ('PersistentResource', NV_D3D11_META_COMMAND_RESOURCE),
    # use GetRequiredParameterResourceSize to query its size
    ('TemporaryResource', NV_D3D11_META_COMMAND_RESOURCE),
]

# make sure structure sizes match what the driver assumes
NV_D3D11_META_COMMAND_INITIALIZE_GEMM_DESC._fields_ = [
    ('PersistentResource', NV_D3D11_META_COMMAND_RESOURCE),
]

NV_D3D11_META_COMMAND_EXECUTE_GEMM_DESC._fields_ = [
    ('AResource', NV_D3D11_META_COMMAND_RESOURCE),
    ('BResource', NV_D3D11_META_COMMAND_RESOURCE),
    ('CResource', NV_D3D11_META_COMMAND_RESOURCE),
    ('OutputResource', NV_D3D11_META_COMMAND_RESOURCE),
    ('PersistentResource', NV_D3D11_META_COMMAND_RESOURCE),
    ('TemporaryResource', NV_D3D11_META_COMMAND_RESOURCE),
]

# make sure structure sizes match what the driver assumes
IID_ID3D11NvMetaCommand_V1 = GUID('{00BF193A-117B-42BC-BBCD-E964A0EA4F2B}')


class ID3D11NvMetaCommand_V1(comtypes.IUnknown):
    _iid_ = IID_ID3D11NvMetaCommand_V1
    _methods_ = [
        #  *** IUnknown methods ***
        #  ** ID3D11NvMetaCommand methods ***
        #  Return size of parameter
        comtypes.STDMETHOD(
            VOID,
            'GetRequiredParameterResourceSize',
            (NV_META_COMMAND_RESOURCE_TYPE, POINTER(NvU64))
        ),
    ]


ID3D11NvMetaCommand = ID3D11NvMetaCommand_V1
ID3D11NvMetaCommand_VER1 = (
    MAKE_NVAPI_VERSION(ID3D11NvMetaCommand_V1, 1)
)
ID3D11NvMetaCommand_VER = ID3D11NvMetaCommand_VER1

NvAPI_D3D11_CreateMetaCommand = hDll.D3D11_CreateMetaCommand
NvAPI_D3D11_CreateMetaCommand.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_CreateMetaCommand(__in                                     ID3D11Device            *pDevice,
#                                               __in                                     REFGUID                  CommandId,
#                                               __in_bcount(CreationParametersDataSize)  const VOID              *pCreationParametersData,
#                                               __in                                     NvU32                    CreationParametersDataSize,
#                                               __out                                    ID3D11NvMetaCommand    **ppMetaCommand);


# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_InitializeMetaCommand
# not \since Release: 400
# not \code
# not DESCRIPTION: Initializes the given MetaCommand with the
# parameters passed in
# not
# not  \param [in]  pDeviceContext    A pointer to the d3d11 device
# context
# not  \param [in]  pMetaCommand    the MetaCommand to initialize
# not  \param [in]  pInitializationParametersData Structure containing
# parameters
# not  \param [in]  InitializationParametersDataSize Size of the
# parameter structure in bytes
# not SUPPORTED OS: Windows 10
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////

NvAPI_D3D11_InitializeMetaCommand = hDll.D3D11_InitializeMetaCommand
NvAPI_D3D11_InitializeMetaCommand.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_InitializeMetaCommand(__in                                          ID3D11DeviceContext       *pDeviceContext,
#                                                   __in                                          ID3D11NvMetaCommand       *pMetaCommand,
#                                                   __in_bcount(InitializationParametersDataSize) const VOID                *pInitializationParametersData,
#                                                   __in                                          NvU32                      InitializationParametersDataSize);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_ExecuteMetaCommand
# not \since Release: 400
# not \code
# not DESCRIPTION: Executes the given MetaCommand with the parameters
# passed in
# not
# not  \param [in]  pDeviceContext    A pointer to the d3d11 device
# context
# not  \param [in]  pMetaCommand    the MetaCommand to execute
# not  \param [in]  pExecutionParametersData  Structure containing
# parameters
# not  \param [in]  ExecutionParametersDataSize Size of the parameter
# structure in bytes
# not SUPPORTED OS: Windows 10
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////

NvAPI_D3D11_ExecuteMetaCommand = hDll.D3D11_ExecuteMetaCommand
NvAPI_D3D11_ExecuteMetaCommand.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_ExecuteMetaCommand(__in                                          ID3D11DeviceContext       *pDeviceContext,
#                                                __in                                          ID3D11NvMetaCommand       *pMetaCommand,
#                                                __in_bcount(ExecutionParametersDataSize)      const VOID                *pExecutionParametersData,
#                                                __in                                          NvU32                      ExecutionParametersDataSize);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_EnumerateMetaCommands
# not \since Release: 400
# not \code
# not DESCRIPTION: Enumerates MetaCommands supported on the system
# not
# not  \param [in]  pDevice   A pointer to D3D12 device.
# not  \param [in/out] pNumMetaCommands  Should be non-null. When the
# value pointed by pNumMetaCommands is 0 or when pDescs is NULL, the
# function returns number of metacommands supported.
# not         When the value pointed is non-zero, the value indicates
# number of Metacommand descriptions to be populated in pDescs array.
# not  \param [out]  pDescs    Pointer to array where Metacommand
# descriptions will be returned. Can be null to indicate that the app
# is querying the number of supported metacommands.
# not         Otherwise should have enough space to hold
# *pNumMetaCommands descriptors
# not SUPPORTED OS: Windows 10
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////

NvAPI_D3D12_EnumerateMetaCommands = hDll.D3D12_EnumerateMetaCommands
NvAPI_D3D12_EnumerateMetaCommands.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_EnumerateMetaCommands(__in                                  ID3D12Device                    *pDevice,
#                                                   __inout                               NvU32                           *pNumMetaCommands,
#                                                   __out_ecount_opt(*pNumMetaCommands)   NVAPI_META_COMMAND_DESC         *pDescs);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_CreateMetaCommand
# not \since Release: 400
# not \code
# not DESCRIPTION: Creates a MetaCommand object which can be used to
# execute optimized operations exposed by driver like convolutions.
# not
# not  \param [in]  pDevice    A pointer to D3D12 device.
# not  \param [in]  CommandId    GUID of the operations to perform
# not  \param [in]  NodeMask    GPU mask for which metacommand is to
# be created. Set it to 0 for single GPU systems
# not  \param [in]  pCreationParametersData structure containing all
# creation parameters for the requested Metacommand
# not  \param [in]  CreationParametersDataSize size of parameter data
# structure
# not  \param [out]  ppMetaCommand   A pointer to memory that receives
# the pointer to the created MetaCommand object.
# not SUPPORTED OS: Windows 10
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# not
# not   DXGI_ERROR_NOT_SUPPORTED - The requested Metacommand is not
# supported.
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NV_D3D12_META_COMMAND_INITIALIZE_CONVOLUTION_EX_DESC._fields_ = [
    # use GetRequiredParameterResourceSize to query its size
    ('PersistentResource', D3D12_GPU_VIRTUAL_ADDRESS),
]

NV_D3D12_META_COMMAND_EXECUTE_CONVOLUTION_EX_DESC._fields_ = [
    ('InputResource', D3D12_GPU_VIRTUAL_ADDRESS),
    ('FilterResource', D3D12_GPU_VIRTUAL_ADDRESS),
    # optional
    ('BiasResource', D3D12_GPU_VIRTUAL_ADDRESS),
    ('OutputResource', D3D12_GPU_VIRTUAL_ADDRESS),
    # should have same dimension as bias
    ('Alpha1Resource', D3D12_GPU_VIRTUAL_ADDRESS),
    ('Alpha2Resource', D3D12_GPU_VIRTUAL_ADDRESS),
    # optional, same dimension/descriptor as output
    ('SkipConnectionResource', D3D12_GPU_VIRTUAL_ADDRESS),
    # should point to same memory that was specified at time of init
    ('PersistentResource', D3D12_GPU_VIRTUAL_ADDRESS),
    # use GetRequiredParameterResourceSize to query its size
    ('TemporaryResource', D3D12_GPU_VIRTUAL_ADDRESS),
]

# make sure structure sizes match what the driver assumes
NV_D3D12_META_COMMAND_INITIALIZE_GEMM_DESC._fields_ = [
    ('PersistentResource', NvU64),
]

NV_D3D12_META_COMMAND_EXECUTE_GEMM_DESC._fields_ = [
    ('AResource', NvU64),
    ('BResource', NvU64),
    ('CResource', NvU64),
    ('OutputResource', NvU64),
    ('PersistentResource', NvU64),
    ('TemporaryResource', NvU64),
]

# make sure structure sizes match what the driver assumes
# uuid("00BF193A-117B-42BC-BBCD-E964A0EA4F2B")


IID_ID3D12NvMetaCommand_V1 = GUID('{00BF193A-117B-42BC-BBCD-E964A0EA4F2B}')


class ID3D12NvMetaCommand_V1(comtypes.IUnknown):
    _iid_ = IID_ID3D12NvMetaCommand_V1
    _methods_ = [
        #  *** IUnknown methods ***
        #  ** ID3D12NvMetaCommand methods ***
        #  Return size of parameter
        comtypes.STDMETHOD(
            VOID,
            'GetRequiredParameterResourceSize',
            (NV_META_COMMAND_RESOURCE_TYPE, POINTER(NvU64))
        ),
    ]


ID3D12NvMetaCommand = ID3D12NvMetaCommand_V1
ID3D12NvMetaCommand_VER1 = (
    MAKE_NVAPI_VERSION(ID3D12NvMetaCommand_V1, 1)
)
ID3D12NvMetaCommand_VER = ID3D12NvMetaCommand_VER1

NvAPI_D3D12_CreateMetaCommand = hDll.D3D12_CreateMetaCommand
NvAPI_D3D12_CreateMetaCommand.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_CreateMetaCommand(__in                                     ID3D12Device            *pDevice,
#                                               __in                                     REFGUID                  CommandId,
#                                               __in                                     NvU32                    NodeMask,
#                                               __in_bcount(CreationParametersDataSize)  const VOID              *pCreationParametersData,
#                                               __in                                     NvU32                    CreationParametersDataSize,
#                                               __out                                    ID3D12NvMetaCommand    **ppMetaCommand);


# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_InitializeMetaCommand
# not \since Release: 400
# not \code
# not DESCRIPTION: Initializes the given MetaCommand with the
# parameters passed in
# not
# not  \param [in]  pCommandList    A pointer to D3D12 command list.
# not  \param [in]  pMetaCommand    the MetaCommand to initialize
# not  \param [in]  pInitializationParametersData Structure containing
# parameters
# not  \param [in]  InitializationParametersDataSize Size of the
# parameter structure in bytes
# not SUPPORTED OS: Windows 10
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////

NvAPI_D3D12_InitializeMetaCommand = hDll.D3D12_InitializeMetaCommand
NvAPI_D3D12_InitializeMetaCommand.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_InitializeMetaCommand(__in                                          ID3D12GraphicsCommandList *pCommandlist,
#                                                   __in                                          ID3D12NvMetaCommand       *pMetaCommand,
#                                                   __in_bcount(InitializationParametersDataSize) const VOID                *pInitializationParametersData,
#                                                   __in                                          NvU32                      InitializationParametersDataSize);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_ExecuteMetaCommand
# not \since Release: 400
# not \code
# not DESCRIPTION: Executes the given MetaCommand with the parameters
# passed in
# not
# not  \param [in]  pCommandList    A pointer to D3D12 command list.
# not  \param [in]  pMetaCommand    the MetaCommand to execute
# not  \param [in]  pExecutionParametersData  Structure containing
# parameters
# not  \param [in]  ExecutionParametersDataSize Size of the parameter
# structure in bytes
# not SUPPORTED OS: Windows 10
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////

NvAPI_D3D12_ExecuteMetaCommand = hDll.D3D12_ExecuteMetaCommand
NvAPI_D3D12_ExecuteMetaCommand.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_ExecuteMetaCommand(__in                                          ID3D12GraphicsCommandList *pCommandlist,
#                                                __in                                          ID3D12NvMetaCommand       *pMetaCommand,
#                                                __in_bcount(ExecutionParametersDataSize)      const VOID                *pExecutionParametersData,
#                                                __in                                          NvU32                      ExecutionParametersDataSize);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_IsNvShaderExtnOpCodeSupported
# not DESCRIPTION: This function checks if a nv HLSL shader extension
# opcode is
# not    supported on current hardware. List of opcodes is in
# nvShaderExtnEnums.h
# not    To use Nvidia HLSL extensions the application must include
# nvHLSLExtns.h
# not    in the hlsl shader code. See nvHLSLExtns.h for more details
# on supported opcodes.
# not
# not \since Release: 364
# not
# not SUPPORTED OS: Windows 10
# not
# not
# not \param [in]  pDev  The device on which to query for support
# not \param [in]  opCode  the opcode to check
# not \param [out]  pSupported true if supported, false otherwise
# not
# not RETURN STATUS:  This API can return any of the error codes
# enumerated in NvAPI_Status.
# not \retval ::  NVAPI_OK if the call succeeded
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D12_IsNvShaderExtnOpCodeSupported = hDll.D3D12_IsNvShaderExtnOpCodeSupported
NvAPI_D3D12_IsNvShaderExtnOpCodeSupported.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_IsNvShaderExtnOpCodeSupported(__in  ID3D12Device *pDevice,
#                                                           __in  NvU32 opCode,
#                                                           __out bool *pSupported);

# ///////////////////////////////////////////////////////////////////
# not
# not FUNCTION NAME: NvAPI_D3D_IsGSyncCapable
# not DESCRIPTION: This API gets G-Sync capability for the given
# device context.
# not    This is only reliable after the first present call has
# completed.
# not \param [in] pDeviceOrContext The D3D9, D3D10, D3D11 device, or
# D3D11 device context
# not \param [in] NVDX_ObjectHandle The handle of primary surface
# not \param [out] pIsGsyncCapable  if G-Sync can be enabled,
# *pIsGsyncCapable is true.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not RETURN STATUS: This API can return any of the error codes
# enumerated in NvAPI_Status.
# not    If there are return error codes with specific meaning for
# this API, they are listed below.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D_IsGSyncCapable = hDll.D3D_IsGSyncCapable
NvAPI_D3D_IsGSyncCapable.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D_IsGSyncCapable(__in IUnknown *pDeviceOrContext, __in NVDX_ObjectHandle primarySurface, __out BOOL *pIsGsyncCapable);

# ///////////////////////////////////////////////////////////////////
# not
# not FUNCTION NAME: NvAPI_D3D_IsGSyncActive
# not DESCRIPTION: This API get the G-Sync state for the given device
# context.
# not    This is only reliable after the first present call has
# completed.
# not    As it is a bit time consuming, It should not be called per
# frame.
# not \param [in] pDeviceOrContext The D3D9, D3D10, D3D11 device, or
# D3D11 device context
# not \param [in] NVDX_ObjectHandle The handle of primary surface
# not \param [out] pIsGsyncActive if G-Sync is active, *pisGsyncActive
# is true.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not RETURN STATUS: This API can return any of the error codes
# enumerated in NvAPI_Status.
# not    If there are return error codes with specific meaning for
# this API, they are listed below.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D_IsGSyncActive = hDll.D3D_IsGSyncActive
NvAPI_D3D_IsGSyncActive.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D_IsGSyncActive(__in IUnknown *pDeviceOrContext, __in NVDX_ObjectHandle primarySurface, __out BOOL *pIsGsyncActive);


# not SUPPORTED OS: Windows 7 and higher
# not

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D1x_DisableShaderDiskCache
# not DESCRIPTION: Disables driver managed caching of shader
# compilations to disk
# not
# not \param [in] pDevice   Device to disabled the shader disk cache on
# not
# not
# not \retval ::NVAPI_OK    Shader disk cache was disabled
# not \retval ::NVAPI_ERROR   The operation failed.
# not \retval ::NVAPI_INVALID_ARGUMENT  Argument passed in is invalid.
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D1x_DisableShaderDiskCache = hDll.D3D1x_DisableShaderDiskCache
NvAPI_D3D1x_DisableShaderDiskCache.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D1x_DisableShaderDiskCache(IUnknown *pDevice);

# not SUPPORTED OS: Windows 7 and higher
# not

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_MultiGPU_GetCaps
# not DESCRIPTION: Request to get multi GPU extension caps.
# not
# not \param [in/out] pMultiGPUCaps  Pointer to a structure returning
# multi GPU caps
# not \retval ::NVAPI_OK    Call succeeded.
# not \retval ::NVAPI_ERROR   Call failed.
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
# not \ingroup dx
_NV_MULTIGPU_CAPS_V1._fields_ = [
    ('multiGPUVersion', NvU32),
    ('reserved', NvU32),
    ('nTotalGPUs', NvU32),
    ('nSLIGPUs', NvU32),
    ('videoBridgePresent', NvU32),
]


# not SUPPORTED OS: Windows 7 and higher
# not

class _Union_4(ctypes.Union):
    pass


_Union_4._fields_ = [
    ('reserved', NvU32),
    # not < The version of the structure
    ('version', NvU32),
]
_NV_MULTIGPU_CAPS_V2._Union_4 = _Union_4

_NV_MULTIGPU_CAPS_V2._anonymous_ = (
    '_Union_4',
)

_NV_MULTIGPU_CAPS_V2._fields_ = [
    ('multiGPUVersion', NvU32),
    ('_Union_4', _NV_MULTIGPU_CAPS_V2._Union_4),
    ('nTotalGPUs', NvU32),
    ('nSLIGPUs', NvU32),
    ('videoBridgePresent', NvU32),
    ('NvLinkPresent', NvU32),
    ('fastNvLinkReads', NvU32),
]
NV_MULTIGPU_CAPS_VER1 = MAKE_NVAPI_VERSION(NV_MULTIGPU_CAPS_V1, 1)
NV_MULTIGPU_CAPS_VER2 = MAKE_NVAPI_VERSION(NV_MULTIGPU_CAPS_V2, 2)
NV_MULTIGPU_CAPS_VER = NV_MULTIGPU_CAPS_VER2
NV_MULTIGPU_CAPS = NV_MULTIGPU_CAPS_V2
PNV_MULTIGPU_CAPS = PNV_MULTIGPU_CAPS_V2
# not SUPPORTED OS: Windows 7 and higher
# not

# not \ingroup dx
NV_MULTIGPU_CAPS = NV_MULTIGPU_CAPS_V1
PNV_MULTIGPU_CAPS = PNV_MULTIGPU_CAPS_V1

NvAPI_D3D11_MultiGPU_GetCaps = hDll.D3D11_MultiGPU_GetCaps
NvAPI_D3D11_MultiGPU_GetCaps.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_MultiGPU_GetCaps(__inout PNV_MULTIGPU_CAPS pMultiGPUCaps);

# not SUPPORTED OS: Windows 7 and higher
# not

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_MultiGPU_Init
# not DESCRIPTION: Request to enable/disable multi GPU extension. Also
# if enabled automatically disables auto stereo.
# not
# not \param [in] bEnable   if true enables the extension for all
# subsequently created devices. Otherwise disables it
# not \retval ::NVAPI_OK    Call succeeded.
# not \retval ::NVAPI_ERROR   Call failed.
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_MultiGPU_Init = hDll.D3D11_MultiGPU_Init
NvAPI_D3D11_MultiGPU_Init.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_MultiGPU_Init(__in bool bEnable);

# not SUPPORTED OS: Windows 7 and higher
# not

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_CreateMultiGPUDevice
# not \code
# not DESCRIPTION: This function returns ID3D11MultiGPUDevice used for
# multi GPU VR support
# not
# not  \param [in]  pDevice   current d3d device
# not  \param [in]  version   version of requested
# ID3D11MultiGPUDevice.
# not  \param [out]  currentVersion   pointer to returned current
# version of ID3D11MultiGPUDevice.
# not  \param [out]  ppD3D11MultiGPUDevice pointer to returned
# ID3D11MultiGPUDevice.
# not  \param [in]  maxGpus   max number of gpus this
# ID3D11MultiGPUDevice is allowed to use
# not
# not
# not \return ::NVAPI_OK     if the call succeeds.
# not  NVAPI_INVALID_ARGUMENT  if NvAPI_D3D11_MultiGPU_Init() was not
# enabled prior to the creation of the D3D11 device,
# not        or if maxGpus is greater than the number of GPUs in the
# SLI group.
# not  NVAPI_NO_ACTIVE_SLI_TOPOLOGY on single-GPU systems, or
# not        if SLI has not been enabled in the NVIDIA control panel.
# not  NVAPI_INVALID_CALL   if there is already an
# ID3D11MultiGPUDevice created for the specified ID3D11Device.
# not  NVAPI_INCOMPATIBLE_STRUCT_VERSION if requested interface
# version is greater than the one that is supported by installed.
# not        driver. In this case currentVersion will contain version
# supported by installed driver.
# not \endcode
# ///////////////////////////////////////////////////////////////////
# not \ingroup dx
NVAPI_COPY_ASYNCHRONOUSLY = 1

# not SUPPORTED OS: Windows 7 and higher
# not
NVAPI_COPY_P2P_READ = 2

# not SUPPORTED OS: Windows 7 and higher
# not
NVAPI_CPU_RESOURCE = 0xFFFFFFFF

from .dx.d3d11_h import *


class ID3D11MultiGPUDevice_V1(comtypes.IUnknown):
    _iid_ = GUID()
    _methods_ = [
        # ////////////////////////////   VER1 methods //////////////////////////////////////////
        comtypes.STDMETHOD(
            VOID,
            'Destroy',
            ()
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'SetGPUMask',
            (POINTER(ID3D11DeviceContext), UINT,)
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'CopySubresourceRegion',
            (
                POINTER(ID3D11DeviceContext),
                POINTER(ID3D11Resource),
                UINT,
                UINT,
                UINT,
                UINT,
                UINT,
                POINTER(ID3D11Resource),
                UINT,
                UINT,
                POINTER(D3D11_BOX),
                UINT
            )
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'CopySubresourceRegion1',
            (
                POINTER(ID3D11DeviceContext),
                POINTER(ID3D11Resource),
                UINT,
                UINT,
                UINT,
                UINT,
                UINT,
                POINTER(ID3D11Resource),
                UINT,
                UINT,
                POINTER(D3D11_BOX),
                UINT,
                UINT
            )
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'UpdateSubresource',
            (
                POINTER(ID3D11DeviceContext),
                POINTER(ID3D11Resource),
                UINT,
                UINT,
                POINTER(D3D11_BOX),
                POINTER(VOID),
                UINT,
                UINT
            )
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'VSSetConstantBuffers',
            (
                POINTER(ID3D11DeviceContext),
                UINT,
                UINT,
                UINT,
                POINTER(ID3D11Buffer),
                POINTER(UINT),
                POINTER(UINT)
            )
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'PSSetConstantBuffers',
            (
                UINT,
                UINT,
                UINT,
                POINTER(ID3D11Buffer),
                POINTER(UINT),
                POINTER(UINT)
            )
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'GSSetConstantBuffers',
            (
                POINTER(ID3D11DeviceContext),
                UINT,
                UINT,
                UINT,
                POINTER(ID3D11Buffer),
                POINTER(UINT),
                POINTER(UINT)
            )
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'DSSetConstantBuffers',
            (
                POINTER(ID3D11DeviceContext),
                UINT,
                UINT,
                UINT,
                POINTER(ID3D11Buffer),
                POINTER(UINT),
                POINTER(UINT)
            )
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'HSSetConstantBuffers',
            (
                POINTER(ID3D11DeviceContext),
                UINT,
                UINT,
                UINT,
                POINTER(ID3D11Buffer),
                POINTER(UINT),
                POINTER(UINT)
            )
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'CSSetConstantBuffers',
            (
                POINTER(ID3D11DeviceContext),
                UINT,
                UINT,
                UINT,
                POINTER(ID3D11Buffer),
                POINTER(UINT),
                POINTER(UINT)
            )
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'SetViewports',
            (
                POINTER(ID3D11DeviceContext),
                UINT,
                UINT,
                POINTER(D3D11_VIEWPORT)
            )
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'SetScissorRects',
            (
                POINTER(ID3D11DeviceContext),
                UINT,
                UINT,
                POINTER(D3D11_RECT)
            )
        ),
        comtypes.STDMETHOD(
            HRESULT,
            'GetData',
            (
                POINTER(ID3D11DeviceContext),
                POINTER(ID3D11Asynchronous),
                UINT,
                POINTER(VOID),
                UINT,
                UINT
            )
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'UpdateTiles',
            (
                POINTER(VOID),
                POINTER(ID3D11Resource),
                UINT,
                POINTER(VOID),
                POINTER(VOID),
                POINTER(VOID),
                UINT
            )
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'CreateFences',
            (
                UINT,
                POINTER(POINTER(VOID))
            )
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'SetFence',
            (UINT, POINTER(VOID), UINT64)
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'WaitForFence',
            (UINT, POINTER(VOID), UINT64)
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'FreeFences',
            (UINT, POINTER(POINTER(VOID)))
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'PresentCompositingConfig',
            (POINTER(comtypes.IUnknown), UINT, POINTER(D3D11_RECT), UINT)
        ),
        # ////////////////////////////   end of VER1 methods   //////////////////////////////////////////
        # ////////////////////////////   Methods added in VER2 //////////////////////////////////////////
        comtypes.STDMETHOD(
            NvAPI_Status,
            'SetContextGPUMask',
            (POINTER(ID3D11DeviceContext), UINT)
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'GetVideoBridgeStatus',
            (POINTER(comtypes.IUnknown), POINTER(UINT))
        ),
        # ////////////////////////////   end of VER2 methods   //////////////////////////////////////////
        # ////////////////////////////   Methods added in VER3 //////////////////////////////////////////
        comtypes.STDMETHOD(
            NvAPI_Status,
            'CreateMultiGPUConstantBuffer',
            (POINTER(D3D11_BUFFER_DESC), POINTER(POINTER(D3D11_SUBRESOURCE_DATA)), POINTER(POINTER(ID3D11Buffer)))
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'ReleaseMultiGPUConstantBuffer',
            (POINTER(ID3D11Buffer),)
        ),
        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////
        #  Following XXSetMGPUConstantBuffers work the same way as DX XXSetConstantBuffers
        #  The difference is that
        #  1. They are setting constant buffers on GPUs that are defined by
        #  current GPU mask that is set via SetGPUMask.
        #  2. For constant buffer created via CreateMultiGPUConstantBuffer these calls set GPU specific constant buffer.
        #  3. For regular constant buffers these calls set the same constant buffer on all GPUs defined by 1.
        #  4. If these functions are called in deferred context then GPUs are defined as GlobalGPUmask & LocalGPUMask
        #  where GlobalGPUmask is GPUMask set before CL execution
        #  and  LocalGPUMask is current GPUMask set in  CL.
        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////
        comtypes.STDMETHOD(
            NvAPI_Status,
            'VSSetMGPUConstantBuffers',
            (POINTER(ID3D11DeviceContext), UINT, UINT, POINTER(ID3D11Buffer))
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'PSSetMGPUConstantBuffers',
            (POINTER(ID3D11DeviceContext), UINT, UINT, POINTER(ID3D11Buffer))
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'GSSetMGPUConstantBuffers',
            (POINTER(ID3D11DeviceContext), UINT, UINT, POINTER(ID3D11Buffer))
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'DSSetMGPUConstantBuffers',
            (POINTER(ID3D11DeviceContext), UINT, UINT, POINTER(ID3D11Buffer))
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'HSSetMGPUConstantBuffers',
            (POINTER(ID3D11DeviceContext), UINT, UINT, POINTER(ID3D11Buffer))
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'CSSetMGPUConstantBuffers',
            (POINTER(ID3D11DeviceContext), UINT, UINT, POINTER(ID3D11Buffer))
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'UpdateConstantBuffer',
            (POINTER(ID3D11DeviceContext), POINTER(ID3D11Buffer), POINTER(VOID), UINT)
        )
        # ////////////////////////////   end of VER3 methods   //////////////////////////////////////////
    ]


# not Synchronization macros based on fences.
def FENCE_SYNCHRONIZATION_START(pMultiGPUDevice, hFence, Value, srcGpu, dstGpu):
    pMultiGPUDevice.SetFence(dstGpu, hFence, Value)
    pMultiGPUDevice.WaitForFence(1 << srcGpu, hFence, Value)
    return Value + 1


def FENCE_SYNCHRONIZATION_END(pMultiGPUDevice, hFence, Value, srcGpu, dstGpu):
    pMultiGPUDevice.SetFence(srcGpu, hFence, Value)
    pMultiGPUDevice.WaitForFence(1 << dstGpu, hFence, Value)
    return Value + 1


# not PresentCompositingConfig method flags.
NVAPI_PRESENT_COMPOSITING_CONFIG_FLAG_USE_VIDEO_BRIDGE = 0x01
NVAPI_PRESENT_COMPOSITING_CONFIG_FLAG_CLEAR_OUTBANDS = 0x02
NVAPI_PRESENT_COMPOSITING_CONFIG_FLAG_GET_VIDEO_BRIDGE_STATUS = (
    0x80000000
)
NVAPI_VIDEO_BRIDGE_STATUS_AVAILABLE = 0
NVAPI_VIDEO_BRIDGE_STATUS_NOT_AVAILABLE = 1
NVAPI_VIDEO_BRIDGE_STATUS_FAILED_ACCESS = 2
NVAPI_VIDEO_BRIDGE_STATUS_UNKNOWN = 3
NVAPI_ALL_GPUS = 0
ID3D11MultiGPUDevice = ID3D11MultiGPUDevice_V1
ID3D11MultiGPUDevice_VER1 = (
    MAKE_NVAPI_VERSION(ID3D11MultiGPUDevice_V1, 1)
)
ID3D11MultiGPUDevice_VER2 = (
    MAKE_NVAPI_VERSION(ID3D11MultiGPUDevice_V1, 2)
)
ID3D11MultiGPUDevice_VER3 = (
    MAKE_NVAPI_VERSION(ID3D11MultiGPUDevice_V1, 3)
)
ID3D11MultiGPUDevice_VER = ID3D11MultiGPUDevice_VER3
ALL_GPUS = 0

# not \ingroup dx
NvAPI_D3D11_CreateMultiGPUDevice = hDll.D3D11_CreateMultiGPUDevice
NvAPI_D3D11_CreateMultiGPUDevice.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_CreateMultiGPUDevice(__in ID3D11Device *pDevice, __in ULONG version, __out ULONG *currentVersion, __out ID3D11MultiGPUDevice **ppD3D11MultiGPUDevice, __in UINT maxGpus=ALL_GPUS);


# not SUPPORTED OS: Windows 7 and higher
# not
# not Used to query the support of Single Pass Stereo HW feature
# not \ingroup dx
_NV_QUERY_SINGLE_PASS_STEREO_SUPPORT_PARAMS_V1._fields_ = [
    # parameter struct version
    ('version', NvU32),
    # Single Pass Stereo supported
    ('bSinglePassStereoSupported', NvU32),
]

_NV_QUERY_SINGLE_PASS_STEREO_SUPPORT_PARAMS_V2._fields_ = [
    # _IN_ parameter struct version
    ('version', NvU32),
    # _OUT_ Single Pass Stereo supported
    ('bSinglePassStereoSupported', NvU32, 1),
    # _OUT_ Single Pass Stereo XYZW supported
    ('bSinglePassStereoXYZWSupported', NvU32, 1),
    # _INOUT_ bits reserved for future use
    ('reserved', NvU32, 30),
]

NV_QUERY_SINGLE_PASS_STEREO_SUPPORT_PARAMS_VER2 = (
    MAKE_NVAPI_VERSION(NV_QUERY_SINGLE_PASS_STEREO_SUPPORT_PARAMS_V2, 2)
)
NV_QUERY_SINGLE_PASS_STEREO_SUPPORT_PARAMS_VER = (
    NV_QUERY_SINGLE_PASS_STEREO_SUPPORT_PARAMS_VER2
)
NV_QUERY_SINGLE_PASS_STEREO_SUPPORT_PARAMS = NV_QUERY_SINGLE_PASS_STEREO_SUPPORT_PARAMS_V1
NV_QUERY_SINGLE_PASS_STEREO_SUPPORT_PARAMS_VER1 = (
    MAKE_NVAPI_VERSION(NV_QUERY_SINGLE_PASS_STEREO_SUPPORT_PARAMS_V1, 1)
)


# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_QuerySinglePassStereoSupport
# not DESCRIPTION: Queries the support of Single Pass Stereo feature
# on current setup and returns appropriate BOOLEAN value.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  pDevice      The ID3D11Device to use.
# not \param [inout] pSinglePassStereoSupportedParams  Stores value of
# whether Single Pass Stereo is supported on current setup or not.
# not
# not \retval NVAPI_OK     Call succeeded.
# not \retval NVAPI_ERROR    Call failed.
# not \retval NVAPI_INVALID_ARGUMENT   One or more arguments are
# invalid.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D_QuerySinglePassStereoSupport = hDll.D3D_QuerySinglePassStereoSupport
NvAPI_D3D_QuerySinglePassStereoSupport.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D_QuerySinglePassStereoSupport(__in IUnknown *pDevice,
#                                                 __inout NV_QUERY_SINGLE_PASS_STEREO_SUPPORT_PARAMS *pQuerySinglePassStereoSupportedParams);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_SetSinglePassStereoMode
# not DESCRIPTION: Set the Single Pass Stereo state
# not
# not \note Note that this is an asynchronous function and returns
# NVAPI_OK if all arguments are valid.
# not  Returned value NVAPI_OK does not reflect that Single Pass
# Stereo is supported or is set in hardware.
# not  One must call NvAPI_D3D_QuerySinglePassStereoSupport() to
# confirm that the current setup
# not  supports Single Pass Stereo before calling this set-function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] pDevOrContext   The ID3D11Device or
# ID3D11DeviceContext to use.
# not \param [in] numViews     Number of views to render.
# not \param [in] renderTargetIndexOffset  Offset between render
# targets of the different views.
# not \param [in] independentViewportMaskEnable Is the independent
# viewport mask enabled.
# not
# not \retval NVAPI_OK     Call succeeded.
# not \retval NVAPI_ERROR    Call failed.
# not \retval NVAPI_INVALID_ARGUMENT   One or more arguments are
# invalid.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D_SetSinglePassStereoMode = hDll.D3D_SetSinglePassStereoMode
NvAPI_D3D_SetSinglePassStereoMode.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D_SetSinglePassStereoMode(__in IUnknown *pDevOrContext, __in NvU32 numViews, __in NvU32 renderTargetIndexOffset, __in NvU8 independentViewportMaskEnable);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_QuerySinglePassStereoSupport
# not DESCRIPTION: Queries the support of Single Pass Stereo feature
# on current setup and returns appropriate BOOLEAN value.
# not
# not SUPPORTED OS: Windows 10
# not
# not
# not \param [in]  pDevice      The IDirect3DDevice12 to use.
# not \param [inout] pQuerySinglePassStereoSupportedParams Stores
# value of whether Single Pass Stereo is supported on current setup or
# not.
# not
# not \retval NVAPI_OK       Call succeeded.
# not \retval NVAPI_ERROR      Call failed.
# not \retval NVAPI_INVALID_ARGUMENT     One or more arguments are
# invalid.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D12_QuerySinglePassStereoSupport = hDll.D3D12_QuerySinglePassStereoSupport
NvAPI_D3D12_QuerySinglePassStereoSupport.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_QuerySinglePassStereoSupport(__in ID3D12Device *pDevice,
#                                                          __inout NV_QUERY_SINGLE_PASS_STEREO_SUPPORT_PARAMS *pQuerySinglePassStereoSupportedParams);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_SetSinglePassStereoMode
# not DESCRIPTION: Set the Single Pass Stereo state.
# not
# not \note Note that Single Pass Stereo state persists on a
# particular CommandList till it is closed.
# not  The state is reset to default (disabled) for every newly
# created CommandList.
# not  One must call NvAPI_D3D12_QuerySinglePassStereoSupport() to
# confirm that the current setup
# not  supports Single Pass Stereo before calling this set-function.
# not
# not SUPPORTED OS: Windows 10
# not
# not
# not \param [in] pCommandList    The command list in which we will
# add push buffer commmands for enabling Single Pass Stereo feature
# not        Note: Command list of type D3D12_COMMAND_LIST_TYPE_BUNDLE
# is not allowed for setting the state of this feature.
# not \param [in] numViews     Number of views to render.
# not \param [in] RenderTargetIndexOffset  Offset between render
# targets of the different views.
# not \param [in] IndependentViewportMaskEnable Is the independent
# viewport mask enabled.
# not
# not \retval NVAPI_OK     Call succeeded.
# not \retval NVAPI_ERROR    Call failed.
# not \retval NVAPI_INVALID_ARGUMENT   One or more arguments are
# invalid.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D12_SetSinglePassStereoMode = hDll.D3D12_SetSinglePassStereoMode
NvAPI_D3D12_SetSinglePassStereoMode.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_SetSinglePassStereoMode(__in ID3D12GraphicsCommandList* pCommandList,
#                                                     __in NvU32 numViews,
#                                                     __in NvU32 renderTargetIndexOffset,
#                                                     __in NvU8 independentViewportMaskEnable);

# not SUPPORTED OS: Windows 7 and higher
# not
# not Used to query the support of MultiView HW feature
# not \ingroup dx
_NV_QUERY_MULTIVIEW_SUPPORT_PARAMS_V1._fields_ = [
    # _IN_ parameter struct version
    ('version', NvU32),
    # _OUT_ MultiView supported (Render 4 views in a single pass)
    ('bMultiViewSupported', NvU32, 1),
    # _OUT_ StereoX supported (Render 2 views in a single pass)
    ('bSinglePassStereoSupported', NvU32, 1),
    # _OUT_ StereoXYZW supported (Render 2 views in a single pass)
    ('bSinglePassStereoXYZWSupported', NvU32, 1),
    # _INOUT_ bits reserved for future use
    ('reserved', NvU32, 29),
]
NV_QUERY_MULTIVIEW_SUPPORT_PARAMS = NV_QUERY_MULTIVIEW_SUPPORT_PARAMS_V1
NV_QUERY_MULTIVIEW_SUPPORT_PARAMS_VER1 = (
    MAKE_NVAPI_VERSION(NV_QUERY_MULTIVIEW_SUPPORT_PARAMS_V1, 1)
)
NV_QUERY_MULTIVIEW_SUPPORT_PARAMS_VER = (
    NV_QUERY_MULTIVIEW_SUPPORT_PARAMS_VER1
)
NV_MULTIVIEW_MAX_SUPPORTED_VIEWS = 4

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_QueryMultiViewSupport
# not DESCRIPTION: Queries the support of MultiView feature on current
# setup and returns appropriate BOOLEAN value.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since  Release: 410
# not
# not \param [in]  pDevice      The ID3D11Device to use.
# not \param [inout] pMultiViewSupportedParams   Stores value of
# whether MultiView is supported on current setup or not.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not  If there are return error codes with specific meaning for this
# API, they are listed below.
# not  (none)
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D_QueryMultiViewSupport = hDll.D3D_QueryMultiViewSupport
NvAPI_D3D_QueryMultiViewSupport.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D_QueryMultiViewSupport(__in IUnknown *pDevice,
#                                                 __inout NV_QUERY_MULTIVIEW_SUPPORT_PARAMS *pQueryMultiViewSupportedParams);
#

# not SUPPORTED OS: Windows 7 and higher
# not
# not Used for setting the Mode for MultiView HW Feature.
# not \ingroup dx
_NV_MULTIVIEW_PARAMS_V1._fields_ = [
    # _IN_ parameter struct version
    ('version', NvU32),
    # _IN_ Number of views to render.
    ('numViews', NvU32),
    # _IN_ Offset between render targets for each of the per views.
    ('renderTargetIndexOffset', NvU32 * NV_MULTIVIEW_MAX_SUPPORTED_VIEWS),
    # _IN_ Is the independent viewport mask enabled.
    ('independentViewportMaskEnable', NvU8),
]
NV_MULTIVIEW_PARAMS = NV_MULTIVIEW_PARAMS_V1
NV_MULTIVIEW_PARAMS_VER1 = MAKE_NVAPI_VERSION(NV_MULTIVIEW_PARAMS_V1, 1)
NV_MULTIVIEW_PARAMS_VER = NV_MULTIVIEW_PARAMS_VER1

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_SetMultiViewMode
# not DESCRIPTION: Set the MultiView state
# not
# not \note Note that this is an asynchronous function and returns
# NVAPI_OK if all arguments are valid.
# not  Returned value NVAPI_OK does not reflect that MultiView is
# supported or is set in hardware.
# not  One must call NvAPI_D3D_QueryMultiViewSupport() to confirm that
# the current setup
# not  supports MultiView before calling this set-function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since  Release: 410
# not
# not \param [in] pDevOrContext    The ID3D11Device or
# ID3D11DeviceContext to use.
# not \param [in] pMultiViewParams    MultiView Params
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not  If there are return error codes with specific meaning for this
# API, they are listed below.
# not  (none)
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D_SetMultiViewMode = hDll.D3D_SetMultiViewMode
NvAPI_D3D_SetMultiViewMode.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D_SetMultiViewMode(__in IUnknown *pDevOrContext, __in NV_MULTIVIEW_PARAMS *pMultiViewParams);

# not SUPPORTED OS: Windows 7 and higher
# not
# not Used to query the support of Lens Matched Shading HW feature
# not \ingroup dx
_NV_QUERY_MODIFIED_W_SUPPORT_PARAMS._fields_ = [
    # parameter struct version
    ('version', NvU32),
    # Modified W supported
    ('bModifiedWSupported', NvU32),
]
NV_QUERY_MODIFIED_W_SUPPORT_PARAMS = NV_QUERY_MODIFIED_W_SUPPORT_PARAMS_V1
NV_QUERY_MODIFIED_W_SUPPORT_PARAMS_VER1 = (
    MAKE_NVAPI_VERSION(NV_QUERY_MODIFIED_W_SUPPORT_PARAMS_V1, 1)
)
NV_QUERY_MODIFIED_W_SUPPORT_PARAMS_VER = (
    NV_QUERY_MODIFIED_W_SUPPORT_PARAMS_VER1
)

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_QueryModifiedWSupport
# not DESCRIPTION: Queries the support of Modified W feature on
# current setup and returns appropriate BOOLEAN value.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  pDevice      The ID3D11Device to use.
# not \param [inout] pQueryModifiedWSupportedParams Stores value of
# whether Modified W is supported on current setup or not.
# not
# not \retval NVAPI_OK     Call succeeded.
# not \retval NVAPI_ERROR    Call failed.
# not \retval NVAPI_INVALID_ARGUMENT   One or more arguments are
# invalid.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D_QueryModifiedWSupport = hDll.D3D_QueryModifiedWSupport
NvAPI_D3D_QueryModifiedWSupport.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D_QueryModifiedWSupport(__in IUnknown *pDev,
#                                             __inout NV_QUERY_MODIFIED_W_SUPPORT_PARAMS *pQueryModifiedWSupportedParams);

# not SUPPORTED OS: Windows 7 and higher
# not
NV_MODIFIED_W_MAX_VIEWPORTS = 16

_NV_MODIFIED_W_COEFFICIENTS._fields_ = [
    # A coefficient in w' = w + Ax + By
    ('fA', FLOAT),
    # B coefficient in w' = w + Ax + By
    ('fB', FLOAT),
    # reserved
    ('fAReserved', FLOAT),
    # reserved
    ('fBReserved', FLOAT),
    # reserved
    ('fReserved', FLOAT * 2),
]

_NV_MODIFIED_W_PARAMS._fields_ = [
    # parameter struct version
    ('version', NvU32),
    # number of valid NV_MODIFIED_W_COEFFICIENTS structs in array
    ('numEntries', NvU32),
    # coefficients
    ('modifiedWCoefficients', NV_MODIFIED_W_COEFFICIENTS * NV_MODIFIED_W_MAX_VIEWPORTS),
    # reserved
    ('id', NvU32),
    # reserved
    ('reserved', NvU32 * NV_MODIFIED_W_MAX_VIEWPORTS),
]
NV_MODIFIED_W_PARAMS = NV_MODIFIED_W_PARAMS_V1
NV_MODIFIED_W_PARAMS_VER1 = (
    MAKE_NVAPI_VERSION(NV_MODIFIED_W_PARAMS_V1, 1)
)
NV_MODIFIED_W_PARAMS_VER = NV_MODIFIED_W_PARAMS_VER1

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_SetModifiedWMode
# not DESCRIPTION: Set the Modified W state and A,B coefficients for
# HW support
# not
# not \note Note that this is an asynchronous function and returns
# NVAPI_OK if all arguments are valid.
# not  Returned value NVAPI_OK does not reflect that Modified-W is
# supported or is set in hardware.
# not  One must call NvAPI_D3D_QueryModifiedWSupport() to confirm that
# the current setup
# not  supports Modified-W before calling this set-function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] pDevOrContext   The ID3D11Device or
# ID3D11DeviceContext to use.
# not \param [in] psModifiedWParams   Modified W parameters.
# not
# not \retval NVAPI_OK     Call succeeded.
# not \retval NVAPI_ERROR    Call failed.
# not \retval NVAPI_INVALID_ARGUMENT   One or more arguments are
# invalid.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D_SetModifiedWMode = hDll.D3D_SetModifiedWMode
NvAPI_D3D_SetModifiedWMode.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D_SetModifiedWMode(__in IUnknown *pDevOrContext, __in NV_MODIFIED_W_PARAMS *psModifiedWParams);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_QueryModifiedWSupport
# not DESCRIPTION: Queries the support of Modified-W feature on
# current setup and returns appropriate BOOLEAN value.
# not
# not SUPPORTED OS: Windows 10
# not
# not
# not \param [in]  pDevice     The ID3D12Device Device created by
# application
# not \param [inout] pQueryModifiedWSupportedParams Stores value of
# whether Modified-W is supported on current setup or not.
# not
# not \retval NVAPI_OK      Call succeeded.
# not \retval NVAPI_ERROR     Call failed.
# not \retval NVAPI_INVALID_ARGUMENT    One or more arguments are
# invalid.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D12_QueryModifiedWSupport = hDll.D3D12_QueryModifiedWSupport
NvAPI_D3D12_QueryModifiedWSupport.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_QueryModifiedWSupport(__in ID3D12Device *pDevice,
#                                                   __inout NV_QUERY_MODIFIED_W_SUPPORT_PARAMS *pQueryModifiedWSupportedParams);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_SetModifiedWMode
# not DESCRIPTION: Set the Modified-W state and A, B coefficients for
# HW support
# not
# not \note Note that Modified-W state persists on a particular
# CommandList till it is closed.
# not  The state is reset to default (disabled) for every newly
# created CommandList.
# not  One must call NvAPI_D3D12_QueryModifiedWSupport() to confirm
# that the current setup
# not  supports Modified-W before calling this set-function.
# not
# not SUPPORTED OS: Windows 10
# not
# not
# not \param [in] pCommandList    The command list in which we will
# add push buffer commmands for enabling Modified-W feature
# not        Note: Command list of type D3D12_COMMAND_LIST_TYPE_BUNDLE
# is not allowed for setting the state of this feature.
# not \param [in] pModifiedWParams   Modified-W parameters.
# not
# not \retval NVAPI_OK     Call succeeded.
# not \retval NVAPI_ERROR    Call failed.
# not \retval NVAPI_INVALID_ARGUMENT   One or more arguments are
# invalid.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D12_SetModifiedWMode = hDll.D3D12_SetModifiedWMode
NvAPI_D3D12_SetModifiedWMode.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_D3D12_SetModifiedWMode(__in ID3D12GraphicsCommandList* pCommandList,
#                                              __in NV_MODIFIED_W_PARAMS *pModifiedWParams);

# not \ingroup dx
# not See NvAPI_D3D_CreateLateLatchObject
class ID3DLateLatchObject_V1(comtypes.IUnknown):
    _iid_ = GUID()
    _methods_ = [
        comtypes.STDMETHOD(
            UINT,
            'Release',
            ()
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'Latch',
            (POINTER(comtypes.IUnknown),)
        ),
        comtypes.STDMETHOD(
            POINTER(ID3D11Buffer),
            'GetD3D11Buffer',
            (UINT,)
        ),
        comtypes.STDMETHOD(
            UINT,
            'GetBufferCount',
            ()
        ),
        comtypes.STDMETHOD(
            NvAPI_Status,
            'UpdateData',
            (POINTER(POINTER(VOID)),)
        )
    ]


# not \ingroup dx
# not See NvAPI_D3D_CreateLateLatchObject
ID3DLateLatchObject = ID3DLateLatchObject_V1
ID3DLateLatchObject_VER1 = (
    MAKE_NVAPI_VERSION(ID3DLateLatchObject_V1, 1)
)
ID3DLateLatchObject_VER = ID3DLateLatchObject_VER1

_NV_D3D_LATELATCH_OBJECT_DESC_V1._fields_ = [
    ('version', NvU32),
    # _IN_ Number of LateLatch buffers that the app wants to create.
    ('numBuffers', NvU32),
    # _IN_ Description of buffers
    ('ppBufferDesc', POINTER(POINTER(D3D11_BUFFER_DESC))),
    # _Out_ Pointer to created interface
    ('ppD3DLateLatchObject', POINTER(POINTER(ID3DLateLatchObject))),
]
NV_D3D_LATELATCH_OBJECT_DESC = NV_D3D_LATELATCH_OBJECT_DESC_V1
NV_D3D_LATELATCH_OBJECT_DESC_VER1 = (
    MAKE_NVAPI_VERSION(NV_D3D_LATELATCH_OBJECT_DESC_V1, 1)
)
NV_D3D_LATELATCH_OBJECT_DESC_VER = NV_D3D_LATELATCH_OBJECT_DESC_VER1

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_CreateLateLatchObject
# not DESCRIPTION: Creates a Late Latch Object interface
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 384
# not
# not \param [in] pDevice    Current ID3D11Device.
# not \param [inout] pLateLatchObjectDesc Pointer to in/out structure
# for late latch object creation
# not
# not RETURN STATUS:  This API can return any of the error codes
# enumerated in NvAPI_Status.
# not    If there are return error codes with specific meaning for
# this API, they are listed below.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D_CreateLateLatchObject = hDll.D3D_CreateLateLatchObject
NvAPI_D3D_CreateLateLatchObject.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D_CreateLateLatchObject(__in IUnknown *pDevice, __inout NV_D3D_LATELATCH_OBJECT_DESC* pLateLatchObjectDesc);

# not \ingroup dx
# not See NvAPI_D3D_QueryLateLatchSupport
_NV_QUERY_LATELATCH_SUPPORT_PARAMS._fields_ = [
    # not < (IN) Parameter structure version
    ('version', NvU32),
    # not < (OUT) LateLatch supported
    ('bLateLatchSupported', NvU32),
]
NV_QUERY_LATELATCH_SUPPORT_PARAMS = NV_QUERY_LATELATCH_SUPPORT_PARAMS_V1
NV_QUERY_LATELATCH_SUPPORT_PARAMS_VER1 = (
    MAKE_NVAPI_VERSION(NV_QUERY_LATELATCH_SUPPORT_PARAMS_V1, 1)
)
NV_QUERY_LATELATCH_SUPPORT_PARAMS_VER = (
    NV_QUERY_LATELATCH_SUPPORT_PARAMS_VER1
)

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_QueryLateLatchSupport
# not DESCRIPTION: Queries the support of DX11 Late Latch feature on
# current setup.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 384
# not
# not \param [in]  pDevice      Current ID3D11Device.
# not \param [inout] pQueryLateLatchSupportParams  Stores value of
# whether Late Latch is supported on current setup or not.
# not
# not RETURN STATUS:  This API can return any of the error codes
# enumerated in NvAPI_Status.
# not    If there are return error codes with specific meaning for
# this API, they are listed below.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D_QueryLateLatchSupport = hDll.D3D_QueryLateLatchSupport
NvAPI_D3D_QueryLateLatchSupport.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D_QueryLateLatchSupport(__in IUnknown *pDevice,
#                                             __inout NV_QUERY_LATELATCH_SUPPORT_PARAMS *pQueryLateLatchSupportParams);
# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_RegisterDevice
# not DESCRIPTION: Tells NvAPI about a D3D device. This must be called
# prior to using any DX1x
# not    deferred-context calls.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] pDev     The ID3D10Device or ID3D11Device to use.
# not
# not RETURN STATUS:  This API can return any of the error codes
# enumerated in NvAPI_Status.
# not    If there are return error codes with specific meaning for
# this API, they are listed below.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D_RegisterDevice = hDll.D3D_RegisterDevice
NvAPI_D3D_RegisterDevice.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D_RegisterDevice(__in IUnknown *pDev);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_MultiDrawInstancedIndirect
# not DESCRIPTION: Extension of DrawInstancedIndirect that takes a
# draw count in. The effect of this function is to loop over
# not    that draw count and perform the DrawInstancedIndirect
# operation each time, incrementing the buffer offset
# not    by the supplied stride each time.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  *pDevContext11   Pointer to D3D11 device context
# (IC or DC)
# not \param [in]  drawCount    Do DrawInstancedIndirect operation
# this many times
# not \param [in]  *pBuffer    ID3D11Buffer that contains the command
# parameters
# not \param [in]  alignedByteOffsetForArgs  Start in pBuffer of the
# command parameters
# not \param [in]  alignedByteStrideForArgs  Stride of the command
# parameters - must be >= 4 * (ctypes.sizeof(NvU32)
# not
# not RETURN STATUS:  This API can return any of the error codes
# enumerated in NvAPI_Status.
# not    If there are return error codes with specific meaning for
# this API, they are listed below.
# not
# not \retval NVAPI_D3D_DEVICE_NOT_REGISTERED  When MultiDraw is
# called on a deferred context, and the device has not yet
# not         been registered (NvAPI_D3D_RegisterDevice), this error
# is returned.
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////

NvAPI_D3D11_MultiDrawInstancedIndirect = hDll.D3D11_MultiDrawInstancedIndirect
NvAPI_D3D11_MultiDrawInstancedIndirect.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_MultiDrawInstancedIndirect(__in ID3D11DeviceContext *pDevContext11,
#                                                        __in NvU32                drawCount,
#                                                        __in ID3D11Buffer        *pBuffer,
#                                                        __in NvU32                alignedByteOffsetForArgs,
#                                                        __in NvU32                alignedByteStrideForArgs);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_MultiDrawIndexedInstancedIndirect
# not DESCRIPTION: Extension of DrawIndexedInstancedIndirect that
# takes a draw count in. The effect of this function is to loop over
# not    that draw count and perform the DrawIndexedInstancedIndirect
# operation each time, incrementing the buffer offset
# not    by the supplied stride each time.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  *pDevContext11   Pointer to D3D11 device context
# (IC or DC)
# not \param [in]  drawCount    Do DrawIndexedInstancedIndirect
# operation this many times
# not \param [in]  *pBuffer    ID3D11Buffer that contains the command
# parameters
# not \param [in]  alignedByteOffsetForArgs  Start in pBuffer of the
# command parameters
# not \param [in]  alignedByteStrideForArgs  Stride of the command
# parameters - must be >= 5 * (ctypes.sizeof(NvU32)
# not
# not RETURN STATUS:  This API can return any of the error codes
# enumerated in NvAPI_Status.
# not    If there are return error codes with specific meaning for
# this API, they are listed below.
# not
# not \retval NVAPI_D3D_DEVICE_NOT_REGISTERED  When MultiDraw is
# called on a deferred context, and the device has not yet
# not         been registered (NvAPI_D3D_RegisterDevice), this error
# is returned.
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_MultiDrawInstancedIndirect = hDll.D3D11_MultiDrawInstancedIndirect
NvAPI_D3D11_MultiDrawInstancedIndirect.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_D3D11_MultiDrawInstancedIndirect(__in ID3D11DeviceContext *pDevContext11,
#                                                        __in NvU32                drawCount,
#                                                        __in ID3D11Buffer        *pBuffer,
#                                                        __in NvU32                alignedByteOffsetForArgs,
#                                                        __in NvU32                alignedByteStrideForArgs);

# not SUPPORTED OS: Windows 7 and higher
# not

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_ImplicitSLIControl
# not This function enables/disables the SLI rendering mode. It has to
# be called prior to D3D device creation. Once this function is called
# with DISABLE_IMPLICIT_SLI
# not parameter all subsequently created devices will be forced to run
# in a single gpu mode until the same function is called with
# ENABLE_IMPLICIT_SLI parameter. The enable
# not call will force all subsequently created devices to run in
# default implicit SLI mode being determined by an application profile
# or a global control panel SLI setting.
# not This NvAPI call is supported in all DX10+ versions of the
# driver. It is supported on all Windows versions.
# not
# not \retval NVAPI_OK      Completed request
# not \retval NVAPI_ERROR     Error occurred
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
# not \ingroup dx
class _IMPLICIT_SLI_CONTROL(ENUM):
    DISABLE_IMPLICIT_SLI = 0
    ENABLE_IMPLICIT_SLI = 1


IMPLICIT_SLI_CONTROL = _IMPLICIT_SLI_CONTROL

# not \ingroup dx
NvAPI_D3D_ImplicitSLIControl = hDll.D3D_ImplicitSLIControl
NvAPI_D3D_ImplicitSLIControl.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D_ImplicitSLIControl(__in IMPLICIT_SLI_CONTROL implicitSLIControl);


# not SUPPORTED OS: Windows 10
# not

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_UseDriverHeapPriorities
# not \code
# not DESCRIPTION: Sets the driver to override Microsoft's heap
# allocation priority values with Nvidia driver priority values. Use
# this once per process before allocating resources.
# not
# not \param [in] pDevice The IDirect3DDevice12 to use.
# not
# not \return This API can return any of the error codes enumerated in
# not   NvAPI_Status. If there are return error codes with specific
# not   meaning for this API, they are listed below.
# not
# not \since Release: 381
# not
# not \endcode
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D12_UseDriverHeapPriorities = hDll.D3D12_UseDriverHeapPriorities
NvAPI_D3D12_UseDriverHeapPriorities.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_UseDriverHeapPriorities(__in ID3D12Device *pDevice);


# not SUPPORTED OS: Windows 10 and higher
# not
#
# _NV_D3D12_MOSAIC_GETCOMPANIONALLOCATIONS._fields_ = [
#     # not < Structure version
#     ('version', POINTER(NvU32)),
#     # not < The ID3D12Device created by application.
#     ('pDevice', POINTER(ID3D12Device)),
#     # not < The ID3D12Resource part of the application swap chain that
#     # has companion allocations.
#     ('pSwapChainBuffer', POINTER(ID3D12Resource)),
#     # not < The number of ID3D12Resource pointers requested to be
#     # returned in the ppComanionResources array, which should match
#     # ID3D12Device::GetNodeCount for the complete set of companion
#     # allocations.
#     ('companionBufferCount', POINTER(NvU32)),
#     # not < An array of ID3D12Resource pointers sized to match
#     # companionBufferCount, which will receive the companion
#     # allocations.
#     ('ppCompanionResources', POINTER(POINTER(ID3D12Resource))),
# ]
# NV_D3D12_MOSAIC_GETCOMPANIONALLOCATIONS = NV_D3D12_MOSAIC_GETCOMPANIONALLOCATIONS_V1
# NV_D3D12_MOSAIC_GETCOMPANIONALLOCATIONS_VER1 = (
#     MAKE_NVAPI_VERSION(NV_D3D12_MOSAIC_GETCOMPANIONALLOCATIONS_V1, 1)
# )
# NV_D3D12_MOSAIC_GETCOMPANIONALLOCATIONS_VER = (
#     NV_D3D12_MOSAIC_GETCOMPANIONALLOCATIONS_VER1
# )

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_Mosaic_GetCompanionAllocations
# not DESCRIPTION: Queries the driver for internally created
# allocations that accompany a swap chain buffer for present-related
# operations.
# not    Surfaces returned by this interface must be destroied at the
# same time that the original swap chain buffer is destroyed. In
# general this occurs prior to a ResizeBuffers call, or when the swap
# chain is released.
# not
# not \param [inout] companionBufferCount  The parameters for this
# function.
# not
# not \retval NVAPI_OK      Call succeeded.
# not \retval NVAPI_ERROR     Call failed.
# not \retval NVAPI_INVALID_ARGUMENT    One or more arguments are
# invalid.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D12_Mosaic_GetCompanionAllocations = hDll.D3D12_Mosaic_GetCompanionAllocations
NvAPI_D3D12_Mosaic_GetCompanionAllocations.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_Mosaic_GetCompanionAllocations(__inout NV_D3D12_MOSAIC_GETCOMPANIONALLOCATIONS *params);


# not SUPPORTED OS: Windows 10 and higher
# not
#
# _NV_D3D12_MOSAIC_GETVIEWPORTANDGPUPARTITIONS._fields_ = [
#     # not < Structure version
#     ('version', POINTER(NvU32)),
#     # not < The ID3D12Device created by application.
#     ('pDevice', POINTER(ID3D12Device)),
#     # not < The ID3D12Resource part of the application swap chain.
#     ('pSwapChainBuffer', POINTER(ID3D12Resource)),
#     # not < A variable to receive the number of
#     # NV_MGPU_MOSAIC_DISPLAY_SURFACE_PARTITION elements returned or
#     # that holds the size of pPartitions when it is non-NULL.
#     ('pPartitionCount', POINTER(NvU32)),
#     # not < An optional array to hold the viewport information per
#     # partition. When this is valid pNodeMask must also be valid.
#     ('pViewport', POINTER(RECT)),
#     # not < An optional array to hold the GPU mask where this viewport
#     # must be valid per partition. When this is valid pViewport must
#     # also be valid.
#     ('pNodeMask', POINTER(NvU32)),
# ]
# NV_D3D12_MOSAIC_GETVIEWPORTANDGPUPARTITIONS = NV_D3D12_MOSAIC_GETVIEWPORTANDGPUPARTITIONS_V1
# NV_D3D12_MOSAIC_GETVIEWPORTANDGPUPARTITIONS_VER1 = (
#     MAKE_NVAPI_VERSION(NV_D3D12_MOSAIC_GETVIEWPORTANDGPUPARTITIONS_V1, 1)
# )
# NV_D3D12_MOSAIC_GETVIEWPORTANDGPUPARTITIONS_VER = (
#     NV_D3D12_MOSAIC_GETVIEWPORTANDGPUPARTITIONS_VER1
# )

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D12_Mosaic_GetViewportAndGpuPartitions
# not DESCRIPTION: Queries the driver for how a swap chain display
# surface is subdivided across devices in relation to display
# connectivity.
# not    Call this interface with NULL pPartitions in order to know
# how many subdivisions exist and allocate a proper size to hold all
# data.
# not    Call it a second time with a properly sized partitions array
# to receive all subdivisions along with GPU node masks of each
# rectangle.
# not
# not \param [inout] params     The parameters for this function.
# not
# not \retval NVAPI_OK      Call succeeded.
# not \retval NVAPI_ERROR     Call failed.
# not \retval NVAPI_INVALID_ARGUMENT    One or more arguments are
# invalid.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D12_Mosaic_GetViewportAndGpuPartitions = hDll.D3D12_Mosaic_GetViewportAndGpuPartitions
NvAPI_D3D12_Mosaic_GetViewportAndGpuPartitions.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D12_Mosaic_GetViewportAndGpuPartitions(__inout NV_D3D12_MOSAIC_GETVIEWPORTANDGPUPARTITIONS *params);


# not \ingroup dx
# not See NvAPI_D3D1x_GetGraphicsCapabilities
_NV_D3D1x_GRAPHICS_CAPS_V1._fields_ = [
    # not < (OUT) Outputs whether Exclusive Scissor Rects are
    # supported or not
    ('bExclusiveScissorRectsSupported', NvU32, 1),
    # not < (OUT) Outputs whether Variable Pixel Shading Rates are
    # supported or not
    ('bVariablePixelRateShadingSupported', NvU32, 1),
    # Reserved bits for future expansion
    ('reservedBits', NvU32, 30),
    # Reserved for future expansion
    ('reserved', NvU32 * 7),
]
NV_D3D1x_GRAPHICS_CAPS_VER1 = (
    MAKE_NVAPI_VERSION(NV_D3D1x_GRAPHICS_CAPS_V1, 1)
)

_NV_D3D1x_GRAPHICS_CAPS_V2._fields_ = [
    # not < (OUT) Outputs whether Exclusive Scissor Rects are
    # supported or not
    ('bExclusiveScissorRectsSupported', NvU32, 1),
    # not < (OUT) Outputs whether Variable Pixel Shading Rates are
    # supported or not
    ('bVariablePixelRateShadingSupported', NvU32, 1),
    # Reserved bits for future expansion
    ('reservedBits', NvU32, 30),
    # not < (OUT) Major SM version of the device
    ('majorSMVersion', NvU16),
    # not < (OUT) Minor SM version of the device
    ('minorSMVersion', NvU16),
    # Reserved for future expansion
    ('reserved', NvU32 * 14),
]
NV_D3D1x_GRAPHICS_CAPS = NV_D3D1x_GRAPHICS_CAPS_V2
NV_D3D1x_GRAPHICS_CAPS_VER2 = (
    MAKE_NVAPI_VERSION(NV_D3D1x_GRAPHICS_CAPS_V2, 2)
)
NV_D3D1x_GRAPHICS_CAPS_VER = NV_D3D1x_GRAPHICS_CAPS_VER2

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D1x_GetGraphicsCapabilities
# not DESCRIPTION: Get the graphics capabilities for current
# hardware/software setup
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 410
# not
# not \param [in]  pDevice   The ID3D11Device device to be used for
# getting the graphics capabilities.
# not \param [in]  structVersion  Version of the caps struct. Should
# be set to NV_D3D1x_GRAPHICS_CAPS_VER.
# not \param [inout]  pGraphicsCaps  Pointer to a
# NV_D3D1x_GRAPHICS_CAPS_CAPS struct created by app.
# not       Graphics capabilities will be filled in this struct by the
# driver.
# not
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not  If there are return error codes with specific meaning for this
# API, they are listed below.
# not  (none)
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D1x_GetGraphicsCapabilities = hDll.D3D1x_GetGraphicsCapabilities
NvAPI_D3D1x_GetGraphicsCapabilities.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D1x_GetGraphicsCapabilities(__in IUnknown *pDevice,
#                                                     __in NvU32 structVersion,
#                                                     __inout NV_D3D1x_GRAPHICS_CAPS *pGraphicsCaps);


NV_MAX_NUM_EXCLUSIVE_SCISSOR_RECTS = 16

# not \ingroup dx
# not See NvAPI_D3D11_RSSetExclusiveScissorRects
_NV_D3D11_EXCLUSIVE_SCISSOR_RECT_DESC_V1._fields_ = [
    # not < (IN) Control of enabling Exclusive ScissorRect per rect
    ('enableExclusiveScissorRect', BOOL),
    # not < (IN) Single rect dimensions
    ('scissorRect', D3D11_RECT),
]

_NV_D3D11_EXCLUSIVE_SCISSOR_RECTS_DESC_V1._fields_ = [
    # not < (IN) Parameter struct version
    ('version', NvU32),
    # not < (IN) Number of Exclusive Scissor Rects to be set.
    ('numRects', NvU32),
    # not < (IN) Array of NV_D3D11_EXCLUSIVE_SCISSOR_RECT_DESC with
    # number of elements equal to Exclusive Scissor Rects
    ('pRects', POINTER(NV_D3D11_EXCLUSIVE_SCISSOR_RECT_DESC_V1)),
]
NV_D3D11_EXCLUSIVE_SCISSOR_RECTS_DESC = NV_D3D11_EXCLUSIVE_SCISSOR_RECTS_DESC_V1
NV_D3D11_EXCLUSIVE_SCISSOR_RECT_DESC = NV_D3D11_EXCLUSIVE_SCISSOR_RECT_DESC_V1
NV_D3D11_EXCLUSIVE_SCISSOR_RECTS_DESC_VER1 = (
    MAKE_NVAPI_VERSION(NV_D3D11_EXCLUSIVE_SCISSOR_RECTS_DESC_V1, 1)
)
NV_D3D11_EXCLUSIVE_SCISSOR_RECTS_DESC_VER = (
    NV_D3D11_EXCLUSIVE_SCISSOR_RECTS_DESC_VER1
)

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_RSSetExclusiveScissorRects
# not DESCRIPTION: Sets Exclusive Scissor Rects. The content bounded
# within the Scissor Rects
# not   will be excluded from rendering unlike regular Scissor Rects.
# These are
# not   orthogonal with Regular Scissor Rects.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 410
# not
# not \param [in]  pContext    The device context
# (ID3D11DeviceContext) to be used for setting the Exclusive Scissor
# Rects.
# not \param [in]  pExclusiveScissorRectsDesc Description of the
# Exclusive Scissor Rects duly filled with their dimensions
# not         and control over enablement of individual ScissorRect
# not
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not  If there are return error codes with specific meaning for this
# API, they are listed below.
# not  (none)
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_RSSetExclusiveScissorRects = hDll.D3D11_RSSetExclusiveScissorRects
NvAPI_D3D11_RSSetExclusiveScissorRects.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_RSSetExclusiveScissorRects(__in IUnknown *pContext,
#                                                        __in NV_D3D11_EXCLUSIVE_SCISSOR_RECTS_DESC *pExclusiveScissorRectsDesc);


# not \ingroup dx
# not See NvAPI_D3D11_RSSetViewportsPixelShadingRates
# Currently only 12 Shading Rates are available
NV_MAX_PIXEL_SHADING_RATES = 16
NV_MAX_NUM_VIEWPORTS = 16

# Every element in Shading Rate Resource represents the shading rate
# for all pixels in the corresponding tile
# The Shading Rate Resource dimensions must be the bound render target
# size divided by the tile dimensions (width/height)
# Width of the tile, in pixels
NV_VARIABLE_PIXEL_SHADING_TILE_WIDTH = 16

# Height of the tile, in pixels
NV_VARIABLE_PIXEL_SHADING_TILE_HEIGHT = 16


class NV_PIXEL_SHADING_RATE(ENUM):
    NV_PIXEL_X0_CULL_RASTER_PIXELS = 1
    NV_PIXEL_X16_PER_RASTER_PIXEL = 2
    NV_PIXEL_X8_PER_RASTER_PIXEL = 3
    NV_PIXEL_X4_PER_RASTER_PIXEL = 4
    NV_PIXEL_X2_PER_RASTER_PIXEL = 5
    NV_PIXEL_X1_PER_RASTER_PIXEL = 6
    NV_PIXEL_X1_PER_2X1_RASTER_PIXELS = 7
    NV_PIXEL_X1_PER_1X2_RASTER_PIXELS = 8
    NV_PIXEL_X1_PER_2X2_RASTER_PIXELS = 9
    NV_PIXEL_X1_PER_4X2_RASTER_PIXELS = 10
    NV_PIXEL_X1_PER_2X4_RASTER_PIXELS = 11
    NV_PIXEL_X1_PER_4X4_RASTER_PIXELS = 12


NV_PIXEL_X0_CULL_RASTER_PIXELS = NV_PIXEL_SHADING_RATE.NV_PIXEL_X0_CULL_RASTER_PIXELS
NV_PIXEL_X16_PER_RASTER_PIXEL = NV_PIXEL_SHADING_RATE.NV_PIXEL_X16_PER_RASTER_PIXEL
NV_PIXEL_X8_PER_RASTER_PIXEL = NV_PIXEL_SHADING_RATE.NV_PIXEL_X8_PER_RASTER_PIXEL
NV_PIXEL_X4_PER_RASTER_PIXEL = NV_PIXEL_SHADING_RATE.NV_PIXEL_X4_PER_RASTER_PIXEL
NV_PIXEL_X2_PER_RASTER_PIXEL = NV_PIXEL_SHADING_RATE.NV_PIXEL_X2_PER_RASTER_PIXEL
NV_PIXEL_X1_PER_RASTER_PIXEL = NV_PIXEL_SHADING_RATE.NV_PIXEL_X1_PER_RASTER_PIXEL
NV_PIXEL_X1_PER_2X1_RASTER_PIXELS = NV_PIXEL_SHADING_RATE.NV_PIXEL_X1_PER_2X1_RASTER_PIXELS
NV_PIXEL_X1_PER_1X2_RASTER_PIXELS = NV_PIXEL_SHADING_RATE.NV_PIXEL_X1_PER_1X2_RASTER_PIXELS
NV_PIXEL_X1_PER_2X2_RASTER_PIXELS = NV_PIXEL_SHADING_RATE.NV_PIXEL_X1_PER_2X2_RASTER_PIXELS
NV_PIXEL_X1_PER_4X2_RASTER_PIXELS = NV_PIXEL_SHADING_RATE.NV_PIXEL_X1_PER_4X2_RASTER_PIXELS
NV_PIXEL_X1_PER_2X4_RASTER_PIXELS = NV_PIXEL_SHADING_RATE.NV_PIXEL_X1_PER_2X4_RASTER_PIXELS
NV_PIXEL_X1_PER_4X4_RASTER_PIXELS = NV_PIXEL_SHADING_RATE.NV_PIXEL_X1_PER_4X4_RASTER_PIXELS

_NV_D3D11_VIEWPORT_SHADING_RATE_DESC_V1._fields_ = [
    # not < (IN) Control of enabling Variable Pixel Shading Rate per
    # viewport
    ('enableVariablePixelShadingRate', BOOL),
    # not < (IN) Lookup table of converting Shading Rate Index to
    # NV_PIXEL_SHADING_RATE
    ('shadingRateTable', NV_PIXEL_SHADING_RATE * NV_MAX_PIXEL_SHADING_RATES),
]

_NV_D3D11_VIEWPORTS_SHADING_RATE_DESC_V1._fields_ = [
    # not < (IN) Struct version
    ('version', NvU32),
    # not < (IN) Number of viewports with shading rate set.
    ('numViewports', NvU32),
    # not < (IN) Array of NV_D3D11_VIEWPORT_SHADING_RATE_DESC with
    # number of elements equal to NumViewports
    ('pViewports', POINTER(NV_D3D11_VIEWPORT_SHADING_RATE_DESC_V1)),
]
NV_D3D11_VIEWPORTS_SHADING_RATE_DESC = NV_D3D11_VIEWPORTS_SHADING_RATE_DESC_V1
NV_D3D11_VIEWPORT_SHADING_RATE_DESC = NV_D3D11_VIEWPORT_SHADING_RATE_DESC_V1
NV_D3D11_VIEWPORTS_SHADING_RATE_DESC_VER1 = (
    MAKE_NVAPI_VERSION(NV_D3D11_VIEWPORTS_SHADING_RATE_DESC_V1, 1)
)
NV_D3D11_VIEWPORTS_SHADING_RATE_DESC_VER = (
    NV_D3D11_VIEWPORTS_SHADING_RATE_DESC_VER1
)

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_RSSetViewportsPixelShadingRates
# not DESCRIPTION: Sets Pixel Shading Rates and Enables/Disables
# per-viewport Variable Pixel Shading Rate feature
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 410
# not
# not \param [in]  pContext   The device context (ID3D11DeviceContext)
# to be used for setting the Viewports Shading Rates
# not \param [in]  pShadingRateDesc  Shading rate descriptor
# not
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not  If there are return error codes with specific meaning for this
# API, they are listed below.
# not  (none)
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_RSSetViewportsPixelShadingRates = hDll.D3D11_RSSetViewportsPixelShadingRates
NvAPI_D3D11_RSSetViewportsPixelShadingRates.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_D3D11_RSSetViewportsPixelShadingRates(__in IUnknown *pContext,
#                                                             __in NV_D3D11_VIEWPORTS_SHADING_RATE_DESC *pShadingRateDesc);


class _NV_SRRV_DIMENSION(ENUM):
    NV_SRRV_DIMENSION_TEXTURE2D = 4
    NV_SRRV_DIMENSION_TEXTURE2DARRAY = 5


NV_SRRV_DIMENSION = _NV_SRRV_DIMENSION

_NV_TEX2D_SRRV._fields_ = [
    ('MipSlice', UINT),
]

_NV_TEX2D_ARRAY_SRRV._fields_ = [
    ('MipSlice', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]


class _Union_5(ctypes.Union):
    pass


_Union_5._fields_ = [
    ('Texture2D', NV_TEX2D_SRRV),
    ('Texture2DArray', NV_TEX2D_ARRAY_SRRV),
]
_NV_D3D11_SHADING_RATE_RESOURCE_VIEW_DESC_V1._Union_5 = _Union_5

_NV_D3D11_SHADING_RATE_RESOURCE_VIEW_DESC_V1._anonymous_ = (
    '_Union_5',
)

_NV_D3D11_SHADING_RATE_RESOURCE_VIEW_DESC_V1._fields_ = [
    # not < (IN) Parameter struct version
    ('version', NvU32),
    # not < (IN) Format of the resource used as Shading Rate Surface.
    # Should be either DXGI_FORMAT_R8_UINT or DXGI_FORMAT_R8_TYPELESS
    ('Format', DXGI_FORMAT),
    # not < (IN) This declares whether the Shading Rate Surface is a
    # simple 2D Texture or Array of 2D Textures
    ('ViewDimension', NV_SRRV_DIMENSION),
    ('_Union_5', _NV_D3D11_SHADING_RATE_RESOURCE_VIEW_DESC_V1._Union_5),
]
NV_D3D11_SHADING_RATE_RESOURCE_VIEW_DESC = NV_D3D11_SHADING_RATE_RESOURCE_VIEW_DESC_V1
NV_D3D11_SHADING_RATE_RESOURCE_VIEW_DESC_VER1 = (
    MAKE_NVAPI_VERSION(NV_D3D11_SHADING_RATE_RESOURCE_VIEW_DESC_V1, 1)
)
NV_D3D11_SHADING_RATE_RESOURCE_VIEW_DESC_VER = (
    NV_D3D11_SHADING_RATE_RESOURCE_VIEW_DESC_VER1
)

IID_ID3D11NvShadingRateResourceView_V1 = GUID('{E14BE7F6-8FF5-4F5E-B63A-AD016EB8FBE5}')


class ID3D11NvShadingRateResourceView_V1(comtypes.IUnknown):
    _iid_ = IID_ID3D11NvShadingRateResourceView_V1
    _methods_ = [

        # uuid("E14BE7F6-8FF5-4F5E-B63A-AD016EB8FBE5")
        #  *** IUnknown methods ***
        #  **** ID3D11View method **/
        #  Get Shading Rate Resource used while creating the Shading Rate Resource View
        comtypes.STDMETHOD(
            VOID,
            'GetResource',
            (POINTER(POINTER(ID3D11Resource)),)
        ),
        #  ** ID3D11NvShadingRateResourceView methods ***
        #  The descriptor used while creating the Shading Rate Resource View
        comtypes.STDMETHOD(
            VOID,
            'GetDesc',
            (POINTER(NV_D3D11_SHADING_RATE_RESOURCE_VIEW_DESC),)
        ),
    ]


ID3D11NvShadingRateResourceView = ID3D11NvShadingRateResourceView_V1
ID3D11NvShadingRateResourceView_VER1 = (
    MAKE_NVAPI_VERSION(ID3D11NvShadingRateResourceView_V1, 1)
)
ID3D11NvShadingRateResourceView_VER = (
    ID3D11NvShadingRateResourceView_VER1
)

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_CreateShadingRateResourceView
# not DESCRIPTION: Creates Shading Rate Resource View by taking
# ID3D11Resource as an input Shading Rate Surface.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 410
# not
# not \param [in]  pDevice    The device to be used for creating the
# Shading Rate Resource View
# not \param [in]  pShadingRateResource  Shading Rate Resource on
# which the view is to be created.
# not         \note This should be of format DXGI_FORMAT_R8_UINT or
# DXGI_FORMAT_R8_TYPELESS
# not         \note This should be confined to size calculated using
# render target dimensions,
# not          NV_VARIABLE_PIXEL_SHADING_TILE_WIDTH and
# NV_VARIABLE_PIXEL_SHADING_TILE_HEIGHT
# not \param [in]  pShadingRateDesc   Shading Rate Resource View
# descriptor
# not \param [out]  ppShadingRateResourceView Address of a pointer to
# ID3D11NvShadingRateResourceView for returning the newly created
# Shading Rate Resource View
# not
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not  If there are return error codes with specific meaning for this
# API, they are listed below.
# not  (none)
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_CreateShadingRateResourceView = hDll.D3D11_CreateShadingRateResourceView
NvAPI_D3D11_CreateShadingRateResourceView.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_CreateShadingRateResourceView(__in  ID3D11Device *pDevice,
#                                                           __in  ID3D11Resource *pShadingRateResource,
#                                                           __in  NV_D3D11_SHADING_RATE_RESOURCE_VIEW_DESC *pShadingRateResourceViewDesc,
#                                                           __out ID3D11NvShadingRateResourceView **ppShadingRateResourceView);


# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_RSSetShadingRateResourceView
# not DESCRIPTION: Sets Shading Rate Resource View
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 410
# not
# not \param [in]  pContext    The device context
# (ID3D11DeviceContext) used for setting the Shading Rate Resource View
# not \param [out]  pShadingRateResourceView  Shading Rate Resource
# View to be set
# not         \note See NvAPI_D3D11_CreateShadingRateResourceView
# not         \note Passing this as null will reset Shading Rate
# Resource View to defaults
# not
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not  If there are return error codes with specific meaning for this
# API, they are listed below.
# not  (none)
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_RSSetShadingRateResourceView = hDll.D3D11_RSSetShadingRateResourceView
NvAPI_D3D11_RSSetShadingRateResourceView.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_D3D11_RSSetShadingRateResourceView(__in IUnknown *pContext,
#                                                          __in ID3D11NvShadingRateResourceView *pShadingRateResourceView);


# not \ingroup dx
# not See NvAPI_D3D11_RSGetPixelShadingRateSampleOrder
# not See NvAPI_D3D11_RSSetPixelShadingRateSampleOrder
# X, Y = sample position. S = sample number.
# The inner-most dimension is the sample number, followed by X and Y.


class NV_PIXEL_SRSO_1x2_X1(ctypes.Structure):
    _fields_ = [
        ('Y', NvU8 * 2)
    ]


class NV_PIXEL_SRSO_1x2_X2(ctypes.Structure):
    _fields_ = [
        ('YS', (NvU8 * 2) * 2)
    ]


class NV_PIXEL_SRSO_1x2_X4(ctypes.Structure):
    _fields_ = [
        ('YS', (NvU8 * 2) * 4)
    ]


class NV_PIXEL_SRSO_1x2_X8(ctypes.Structure):
    _fields_ = [
        ('YS', (NvU8 * 2) * 8)
    ]


class NV_PIXEL_SRSO_2x1_X1(ctypes.Structure):
    _fields_ = [
        ('X', NvU8 * 2)
    ]


class NV_PIXEL_SRSO_2x1_X2(ctypes.Structure):
    _fields_ = [
        ('XS', (NvU8 * 2) * 2)
    ]


class NV_PIXEL_SRSO_2x1_X4(ctypes.Structure):
    _fields_ = [
        ('XS', (NvU8 * 2) * 4)
    ]


class NV_PIXEL_SRSO_2x2_X1(ctypes.Structure):
    _fields_ = [
        ('YX', (NvU8 * 2) * 2)
    ]


class NV_PIXEL_SRSO_2x2_X2(ctypes.Structure):
    _fields_ = [
        ('YXS', ((NvU8 * 2) * 2) * 2)
    ]


class NV_PIXEL_SRSO_2x2_X4(ctypes.Structure):
    _fields_ = [
        ('YXS', ((NvU8 * 2) * 2) * 4)
    ]


class NV_PIXEL_SRSO_2x4_X1(ctypes.Structure):
    _fields_ = [
        ('YX', (NvU8 * 4) * 2)
    ]


class NV_PIXEL_SRSO_2x4_X2(ctypes.Structure):
    _fields_ = [
        ('YXS', ((NvU8 * 4) * 2) * 2)
    ]


class NV_PIXEL_SRSO_4x2_X1(ctypes.Structure):
    _fields_ = [
        ('YX', (NvU8 * 2) * 4)
    ]


class NV_PIXEL_SRSO_4x4_X1(ctypes.Structure):
    _fields_ = [
        ('YX', (NvU8 * 4) * 4)
    ]


_NV_PIXEL_SRSO_1x2._fields_ = [
    ('X1', NV_PIXEL_SRSO_1x2_X1),
    ('X2', NV_PIXEL_SRSO_1x2_X2),
    ('X4', NV_PIXEL_SRSO_1x2_X4),
    ('X8', NV_PIXEL_SRSO_1x2_X8)
]

_NV_PIXEL_SRSO_2x1._fields_ = [
    ('X1', NV_PIXEL_SRSO_2x1_X1),
    ('X2', NV_PIXEL_SRSO_2x1_X2),
    ('X4', NV_PIXEL_SRSO_2x1_X4)
]

_NV_PIXEL_SRSO_2x2._fields_ = [
    ('X1', NV_PIXEL_SRSO_2x2_X1),
    ('X2', NV_PIXEL_SRSO_2x2_X2),
    ('X4', NV_PIXEL_SRSO_2x2_X4)
]

_NV_PIXEL_SRSO_2x4._fields_ = [
    ('X1', NV_PIXEL_SRSO_2x4_X1),
    ('X2', NV_PIXEL_SRSO_2x4_X2),
]

_NV_PIXEL_SRSO_4x2._fields_ = [
    ('X1', NV_PIXEL_SRSO_4x2_X1),
]

_NV_PIXEL_SRSO_4x4._fields_ = [
    ('X1', NV_PIXEL_SRSO_4x4_X1),
]

_NV_PIXEL_SHADING_RATE_SAMPLE_ORDER_TABLE_V1._fields_ = [
    ('version', NvU32),
    ('Pixel_1x2', NV_PIXEL_SRSO_1x2),
    ('Pixel_2x1', NV_PIXEL_SRSO_2x1),
    ('Pixel_2x2', NV_PIXEL_SRSO_2x2),
    ('Pixel_2x4', NV_PIXEL_SRSO_2x4),
    ('Pixel_4x2', NV_PIXEL_SRSO_4x2),
    ('Pixel_4x4', NV_PIXEL_SRSO_4x4)
]

NV_PIXEL_SHADING_RATE_SAMPLE_ORDER_TABLE = NV_PIXEL_SHADING_RATE_SAMPLE_ORDER_TABLE_V1

NV_PIXEL_SHADING_RATE_SAMPLE_ORDER_TABLE_VER1 = (
    MAKE_NVAPI_VERSION(NV_PIXEL_SHADING_RATE_SAMPLE_ORDER_TABLE_V1, 1)
)

NV_PIXEL_SHADING_RATE_SAMPLE_ORDER_TABLE_VER = (
    NV_PIXEL_SHADING_RATE_SAMPLE_ORDER_TABLE_VER1
)

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_RSGetPixelShadingRateSampleOrder
# not DESCRIPTION: Get the Sample Order for Variable Shading Rate
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 410
# not
# not \param [in]  pContext    The device context
# (ID3D11DeviceContext) used for getting the Shading Rate Sample Order
# not \param [out]  pSampleOrderTable  A pointer to
# NV_PIXEL_SHADING_RATE_SAMPLE_ORDER_TABLE where the current Sample
# Order for Variable Pixel Rate Shading that is returned
# not
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not  If there are return error codes with specific meaning for this
# API, they are listed below.
# not  (none)
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_RSGetPixelShadingRateSampleOrder = hDll.D3D11_RSGetPixelShadingRateSampleOrder
NvAPI_D3D11_RSGetPixelShadingRateSampleOrder.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_RSGetPixelShadingRateSampleOrder(__in IUnknown *pContext,
#                                                              __out NV_PIXEL_SHADING_RATE_SAMPLE_ORDER_TABLE* pSampleOrderTable);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_RSSetPixelShadingRateSampleOrder
# not DESCRIPTION: Set the Sample Order for Variable Shading Rate
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 410
# not
# not \param [in]  pContext    The device context
# (ID3D11DeviceContext) used for setting the Shading Rate Sample Order
# not \param [out]  pSampleOrderTable  Sample Order for Variable
# Shading Rate to be set
# not
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not  If there are return error codes with specific meaning for this
# API, they are listed below.
# not  (none)
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D11_RSSetPixelShadingRateSampleOrder = hDll.D3D11_RSSetPixelShadingRateSampleOrder
NvAPI_D3D11_RSSetPixelShadingRateSampleOrder.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D11_RSSetPixelShadingRateSampleOrder(__in IUnknown *pContext,
#                                                              __in NV_PIXEL_SHADING_RATE_SAMPLE_ORDER_TABLE* pSampleOrderTable);


# not SUPPORTED OS: Windows 7 and higher
# not

_NV_VRS_HELPER_LATCH_GAZE_PARAMS_V1._fields_ = [
    # not < (IN) Struct version
    ('version', NvU32),
    # not < (IN) Reserved for future use
    ('flags', NvU32),
]
NV_VRS_HELPER_LATCH_GAZE_PARAMS = NV_VRS_HELPER_LATCH_GAZE_PARAMS_V1
NV_VRS_HELPER_LATCH_GAZE_PARAMS_VER1 = (
    MAKE_NVAPI_VERSION(NV_VRS_HELPER_LATCH_GAZE_PARAMS_V1, 1)
)
NV_VRS_HELPER_LATCH_GAZE_PARAMS_VER = (
    NV_VRS_HELPER_LATCH_GAZE_PARAMS_VER1
)


class _NV_VRS_CONTENT_TYPE(ENUM):
    NV_VRS_CONTENT_TYPE_INVALID = 0x0
    NV_VRS_CONTENT_TYPE_FOVEATED_RENDERING = 0x1
    NV_VRS_CONTENT_TYPE_MAX = NV_VRS_CONTENT_TYPE_FOVEATED_RENDERING


NV_VRS_CONTENT_TYPE = _NV_VRS_CONTENT_TYPE


class _NV_FOVEATED_RENDERING_SHADING_RATE_PRESET(ENUM):
    NV_FOVEATED_RENDERING_SHADING_RATE_PRESET_INVALID = 0
    NV_FOVEATED_RENDERING_SHADING_RATE_PRESET_HIGHEST_PERFORMANCE = 1
    NV_FOVEATED_RENDERING_SHADING_RATE_PRESET_HIGH_PERFORMANCE = 2
    NV_FOVEATED_RENDERING_SHADING_RATE_PRESET_BALANCED = 3
    NV_FOVEATED_RENDERING_SHADING_RATE_PRESET_HIGH_QUALITY = 4
    NV_FOVEATED_RENDERING_SHADING_RATE_PRESET_HIGHEST_QUALITY = 5
    NV_FOVEATED_RENDERING_SHADING_RATE_PRESET_CUSTOM = 6
    NV_FOVEATED_RENDERING_SHADING_RATE_PRESET_MAX = (
        NV_FOVEATED_RENDERING_SHADING_RATE_PRESET_CUSTOM
    )


NV_FOVEATED_RENDERING_SHADING_RATE_PRESET = _NV_FOVEATED_RENDERING_SHADING_RATE_PRESET

_NV_FOVEATED_RENDERING_CUSTOM_SHADING_RATE_PRESET_DESC_V1._fields_ = [
    ('version', NvU32),
    # not < (IN) Shading Rate for the inner-most region of the
    # foveated rendering pattern
    ('InnerMostRegionShadingRate', NV_PIXEL_SHADING_RATE),
    # not < (IN) Shading Rate for the middle region of the foveated
    # rendering pattern
    ('MiddleRegionShadingRate', NV_PIXEL_SHADING_RATE),
    # not < (IN) Shading Rate for the peripheral region of the
    # foveated rendering pattern
    ('PeripheralRegionShadingRate', NV_PIXEL_SHADING_RATE),
]
NV_FOVEATED_RENDERING_CUSTOM_SHADING_RATE_PRESET_DESC = NV_FOVEATED_RENDERING_CUSTOM_SHADING_RATE_PRESET_DESC_V1
NV_FOVEATED_RENDERING_CUSTOM_SHADING_RATE_PRESET_DESC_VER1 = (
    MAKE_NVAPI_VERSION(NV_FOVEATED_RENDERING_CUSTOM_SHADING_RATE_PRESET_DESC_V1, 1)
)
NV_FOVEATED_RENDERING_CUSTOM_SHADING_RATE_PRESET_DESC_VER = (
    NV_FOVEATED_RENDERING_CUSTOM_SHADING_RATE_PRESET_DESC_VER1
)


class _NV_FOVEATED_RENDERING_FOVEATION_PATTERN_PRESET(ENUM):
    NV_FOVEATED_RENDERING_FOVEATION_PATTERN_PRESET_INVALID = 0
    NV_FOVEATED_RENDERING_FOVEATION_PATTERN_PRESET_WIDE = 1
    NV_FOVEATED_RENDERING_FOVEATION_PATTERN_PRESET_BALANCED = 2
    NV_FOVEATED_RENDERING_FOVEATION_PATTERN_PRESET_NARROW = 3
    NV_FOVEATED_RENDERING_FOVEATION_PATTERN_PRESET_CUSTOM = 4
    NV_FOVEATED_RENDERING_FOVEATION_PATTERN_PRESET_MAX = (
        NV_FOVEATED_RENDERING_FOVEATION_PATTERN_PRESET_CUSTOM
    )


NV_FOVEATED_RENDERING_FOVEATION_PATTERN_PRESET = _NV_FOVEATED_RENDERING_FOVEATION_PATTERN_PRESET

_NV_FOVEATED_RENDERING_CUSTOM_FOVEATION_PATTERN_PRESET_DESC_V1._fields_ = [
    ('version', NvU32),
    # not < (IN) Horizontal and vertical radius for the inner-most
    # region of the foveated rendering pattern
    ('fInnermostRadii', FLOAT * 2),
    # not < (IN) Horizontal and vertical radius for the middle region
    # of the foveated rendering pattern
    ('fMiddleRadii', FLOAT * 2),
    # not < (IN) Horizontal and vertical radius for the peripheral
    # region of the foveated rendering pattern
    ('fPeripheralRadii', FLOAT * 2),
]
NV_FOVEATED_RENDERING_CUSTOM_FOVEATION_PATTERN_PRESET_DESC = NV_FOVEATED_RENDERING_CUSTOM_FOVEATION_PATTERN_PRESET_DESC_V1
NV_FOVEATED_RENDERING_CUSTOM_FOVEATION_PATTERN_PRESET_DESC_VER1 = (
    MAKE_NVAPI_VERSION(NV_FOVEATED_RENDERING_CUSTOM_FOVEATION_PATTERN_PRESET_DESC_V1, 1)
)
NV_FOVEATED_RENDERING_CUSTOM_FOVEATION_PATTERN_PRESET_DESC_VER = (
    NV_FOVEATED_RENDERING_CUSTOM_FOVEATION_PATTERN_PRESET_DESC_VER1
)

_NV_FOVEATED_RENDERING_DESC_V1._fields_ = [
    # not < (IN) Struct version
    ('version', NvU32),
    # not < (IN) Reserved for future use
    ('flags', NvU32),
    # not < (IN) Preset of the shading rate
    ('ShadingRatePreset', NV_FOVEATED_RENDERING_SHADING_RATE_PRESET),
    # not < (IN) To be provided only if ShadingRatePreset is
    # NV_FOVEATED_RENDERING_SHADING_RATE_PRESET_CUSTOM
    ('ShadingRateCustomPresetDesc', NV_FOVEATED_RENDERING_CUSTOM_SHADING_RATE_PRESET_DESC_V1),
    # not < (IN) Preset of the foveation pattern
    ('FoveationPatternPreset', NV_FOVEATED_RENDERING_FOVEATION_PATTERN_PRESET),
    # not < (IN) To be provided only if FoveationPatternPreset is
    # NV_FOVEATED_RENDERING_FOVEATION_PATTERN_PRESET_CUSTOM
    ('FoveationPatternCustomPresetDesc', NV_FOVEATED_RENDERING_CUSTOM_FOVEATION_PATTERN_PRESET_DESC_V1),
    # not < (IN) ID of the gaze data provider. Needed only for
    # supporting more than one device with eye tracking.
    ('GazeDataDeviceId', NvU32),
]
NV_FOVEATED_RENDERING_DESC = NV_FOVEATED_RENDERING_DESC_V1
NV_FOVEATED_RENDERING_DESC_VER1 = (
    MAKE_NVAPI_VERSION(NV_FOVEATED_RENDERING_DESC_V1, 1)
)
NV_FOVEATED_RENDERING_DESC_VER = NV_FOVEATED_RENDERING_DESC_VER1


class _NV_VRS_RENDER_MODE(ENUM):
    NV_VRS_RENDER_MODE_INVALID = 0
    NV_VRS_RENDER_MODE_MONO = 1

    # States Left eye rendering of a stereo pair on the entire render
    # target
    NV_VRS_RENDER_MODE_LEFT_EYE = 2

    # States Right eye rendering of a stereo pair on the entire render
    # target
    NV_VRS_RENDER_MODE_RIGHT_EYE = 3
    NV_VRS_RENDER_MODE_STEREO = 4
    NV_VRS_RENDER_MODE_MAX = NV_VRS_RENDER_MODE_STEREO


NV_VRS_RENDER_MODE = _NV_VRS_RENDER_MODE

# Maximum number of gaze data providers / devices.
MAX_NUMBER_OF_GAZE_DATA_PROVIDERS = 8

_NV_VRS_HELPER_ENABLE_PARAMS_V1._fields_ = [
    # not < (IN) Struct version
    ('version', NvU32),
    # not < (IN) Reserved for future use
    ('flags', NvU32),
    # not < (IN) This defines whether subsequent render calls are for
    # mono/stereo
    ('RenderMode', NV_VRS_RENDER_MODE),
    # not < (IN) This defines the type of content with which the VRS
    # pattern will be generated
    ('ContentType', NV_VRS_CONTENT_TYPE),
    # not < (IN) Provide this if ContentType has
    # NV_VRS_CONTENT_TYPE_FOVEATED_RENDERING flag
    ('sFoveatedRenderingDesc', NV_FOVEATED_RENDERING_DESC_V1),
]
NV_VRS_HELPER_ENABLE_PARAMS = NV_VRS_HELPER_ENABLE_PARAMS_V1
NV_VRS_HELPER_ENABLE_PARAMS_VER1 = (
    MAKE_NVAPI_VERSION(NV_VRS_HELPER_ENABLE_PARAMS_V1, 1)
)
NV_VRS_HELPER_ENABLE_PARAMS_VER = NV_VRS_HELPER_ENABLE_PARAMS_VER1

_NV_VRS_HELPER_DISABLE_PARAMS_V1._fields_ = [
    # not < (IN) Struct version
    ('version', NvU32),
    # not < (IN) Reserved for future use
    ('reserved', NvU32),
]
NV_VRS_HELPER_DISABLE_PARAMS = NV_VRS_HELPER_DISABLE_PARAMS_V1
NV_VRS_HELPER_DISABLE_PARAMS_VER1 = (
    MAKE_NVAPI_VERSION(NV_VRS_HELPER_DISABLE_PARAMS_V1, 1)
)
NV_VRS_HELPER_DISABLE_PARAMS_VER = NV_VRS_HELPER_DISABLE_PARAMS_VER1

_NV_VRS_HELPER_GET_SHADING_RATE_RESOURCE_PARAMS_V1._fields_ = [
    # not < (IN) Struct version
    ('version', NvU32),
    # not < (OUT) Pointer to 2D Texture resource with currently
    # applied shading rate pattern
    ('ppShadingRateResource', POINTER(POINTER(comtypes.IUnknown))),
    # not < (OUT) Shading Rate Table filled by the driver
    ('shadingRateTable', NV_PIXEL_SHADING_RATE * NV_MAX_PIXEL_SHADING_RATES),
]
NV_VRS_HELPER_GET_SHADING_RATE_RESOURCE_PARAMS = NV_VRS_HELPER_GET_SHADING_RATE_RESOURCE_PARAMS_V1
NV_VRS_HELPER_GET_SHADING_RATE_RESOURCE_PARAMS_VER1 = (
    MAKE_NVAPI_VERSION(NV_VRS_HELPER_GET_SHADING_RATE_RESOURCE_PARAMS_V1, 1)
)
NV_VRS_HELPER_GET_SHADING_RATE_RESOURCE_PARAMS_VER = (
    NV_VRS_HELPER_GET_SHADING_RATE_RESOURCE_PARAMS_VER1
)

_NV_VRS_HELPER_PURGE_INTERNAL_RESOURCES_PARAMS_V1._fields_ = [
    # not < (IN) Struct version
    ('version', NvU32),
    # not < (IN) Reserved for future use
    ('reserved', NvU32),
]
NV_VRS_HELPER_PURGE_INTERNAL_RESOURCES_PARAMS = NV_VRS_HELPER_PURGE_INTERNAL_RESOURCES_PARAMS_V1
NV_VRS_HELPER_PURGE_INTERNAL_RESOURCES_PARAMS_VER1 = (
    MAKE_NVAPI_VERSION(NV_VRS_HELPER_PURGE_INTERNAL_RESOURCES_PARAMS_V1, 1)
)
NV_VRS_HELPER_PURGE_INTERNAL_RESOURCES_PARAMS_VER = (
    NV_VRS_HELPER_PURGE_INTERNAL_RESOURCES_PARAMS_VER1
)


class ID3DNvVRSHelper_V1(comtypes.IUnknown):
    _iid_ = GUID()
    _methods_ = [
        #  Latches the latest gaze which will be used for subsequent foveated rendering. Recommended to be called once per frame before scene drawing begins.
        comtypes.STDMETHOD(
            NvAPI_Status,
            'LatchGaze',
            (
                POINTER(comtypes.IUnknown),
                POINTER(NV_VRS_HELPER_LATCH_GAZE_PARAMS)
            )
        ),
        #  Enables VRS with sepcified content type and preset. This can be called per draw call.
        comtypes.STDMETHOD(
            NvAPI_Status,
            'Enable',
            (
                POINTER(comtypes.IUnknown),
                POINTER(NV_VRS_HELPER_ENABLE_PARAMS)
            )
        ),
        #  Disables VRS till re-enabled.
        comtypes.STDMETHOD(
            NvAPI_Status,
            'Disable',
            (
                POINTER(comtypes.IUnknown),
                POINTER(NV_VRS_HELPER_DISABLE_PARAMS)
            )
        ),
        #  Creates a 2D texture, copies the current shading rate pattern on it and returns the pointer to this texture.
        #  It also returns an array that conveys which value in the shading rate resource corresponds to which exact pixel shading rate.
        comtypes.STDMETHOD(
            NvAPI_Status,
            'GetShadingRateResource',
            (
                POINTER(comtypes.IUnknown),
                POINTER(NV_VRS_HELPER_GET_SHADING_RATE_RESOURCE_PARAMS)
            )
        ),
        #  Destroys all internally created shading rate resources and views.
        comtypes.STDMETHOD(
            NvAPI_Status,
            'PurgeInternalShadingRateResources',
            (
                POINTER(comtypes.IUnknown),
                POINTER(NV_VRS_HELPER_PURGE_INTERNAL_RESOURCES_PARAMS)
            )
        ),
    ]


ID3DNvVRSHelper = ID3DNvVRSHelper_V1
ID3DNvVRSHelper_VER1 = MAKE_NVAPI_VERSION(ID3DNvVRSHelper_V1, 1)
ID3DNvVRSHelper_VER = ID3DNvVRSHelper_VER1

_NV_VRS_HELPER_INIT_PARAMS_V1._fields_ = [
    # not < (IN) Struct version
    ('version', NvU32),
    # not < (IN) Reserved for future use
    ('flags', NvU32),
    # not < (OUT) Interface for Shading Rate Pattern Tracker
    ('ppVRSHelper', POINTER(POINTER(ID3DNvVRSHelper_V1))),
]
NV_VRS_HELPER_INIT_PARAMS = NV_VRS_HELPER_INIT_PARAMS_V1
NV_VRS_HELPER_INIT_PARAMS_VER1 = (
    MAKE_NVAPI_VERSION(NV_VRS_HELPER_INIT_PARAMS_V1, 1)
)
NV_VRS_HELPER_INIT_PARAMS_VER = NV_VRS_HELPER_INIT_PARAMS_VER1

# not SUPPORTED OS: Windows 7 and higher
# not
# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_InitializeVRSHelper
# not DESCRIPTION: Creates an interface for updating, enabling and
# disabling internally tracked shading rate pattern for Variable Rate
# Shading
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 430
# not
# not \param [in]  pDevice     The device to be used for creating the
# VRS Handler interface
# not          \note This should be same the device used for Gaze
# Handler. See also: NvAPI_D3D_InitializeNvGazeHandler.
# not \param [in]  pInitializeVRSHelperParams   Descriptor for VRS
# Helper initialization
# not
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not  If there are return error codes with specific meaning for this
# API, they are listed below.
# not  (none)
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D_InitializeVRSHelper = hDll.D3D_InitializeVRSHelper
NvAPI_D3D_InitializeVRSHelper.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_D3D_InitializeVRSHelper(__in    IUnknown *pDevice,
#                                               __inout NV_VRS_HELPER_INIT_PARAMS *pInitializeVRSHelperParams);


class _NV_GAZE_DATA_VALIDITY_FLAGS(ENUM):
    NV_GAZE_ORIGIN_VALID = 0x1
    NV_GAZE_DIRECTION_VALID = 0x2
    NV_GAZE_LOCATION_VALID = 0x4
    NV_GAZE_VELOCITY_VALID = 0x8
    NV_GAZE_PUPIL_DIAMETER_VALID = 0x10
    NV_GAZE_EYE_OPENNESS_VALID = 0x20
    NV_GAZE_EYE_SACCADE_DATA_VALID = 0x40


NV_GAZE_DATA_VALIDITY_FLAGS = _NV_GAZE_DATA_VALIDITY_FLAGS

_NV_FOVEATED_RENDERING_GAZE_DATA_PER_EYE._fields_ = [
    # not < (IN) Version of the structure
    ('version', NvU32),
    # not < (IN) To be populated with OR'ing flags from
    # NV_GAZE_DATA_VALIDITY_FLAGS
    ('GazeDataValidityFlags', NvU32),
    # not < (IN) Use flag NV_GAZE_ORIGIN_VALID. Origin of the eye in
    # millimeters. Used mainly to detect whether Left Eye or Right Eye.
    ('fGazeOrigin_mm', FLOAT * 3),
    # not < (IN) Use flag NV_GAZE_DIRECTION_VALID. Normalized
    # direction of the gaze of the eye. Used for calculating the gaze
    # location using the FOV.
    ('fGazeDirection', FLOAT * 3),
    # not < (IN) Use flag NV_GAZE_LOCATION_VALID. Precalculated
    # normalized gaze location in limits (-1 to + 1) for X and Y.
    # Center of the screen denotes (0, 0). If this is valid, this will
    # be given higher priority than direction.
    ('fGazeNormalizedLocation', FLOAT * 2),
    # not < (IN) Use flag NV_GAZE_VELOCITY_VALID. Optional: Velocity
    # of the eye on the normalized space in each direction. Central
    # foveated region would be skewed in the direction of the velocity.
    ('fGazeVelocity', FLOAT * 2),
    # not < (IN) Use flag NV_GAZE_PUPIL_DIAMETER_VALID. Unused at the
    # moment.
    ('fPupilDiameter_mm', FLOAT),
    # not < (IN) Use flag NV_GAZE_EYE_OPENNESS_VALID. Unused at the
    # moment.
    ('fEyeOpenness', FLOAT),
    # not < (IN) Use flag NV_GAZE_EYE_SACCADE_DATA_VALID. Denotes
    # whether eye is currently in saccade movement or not.
    ('bInSaccade', BOOL),
]
NV_FOVEATED_RENDERING_GAZE_DATA_PER_EYE = NV_FOVEATED_RENDERING_GAZE_DATA_PER_EYE_V1
NV_FOVEATED_RENDERING_GAZE_DATA_PER_EYE_VER1 = (
    MAKE_NVAPI_VERSION(NV_FOVEATED_RENDERING_GAZE_DATA_PER_EYE_V1, 1)
)
NV_FOVEATED_RENDERING_GAZE_DATA_PER_EYE_VER = (
    NV_FOVEATED_RENDERING_GAZE_DATA_PER_EYE_VER1
)


class _Union_6(ctypes.Union):
    pass


class sStereoData(ctypes.Structure):
    pass


sStereoData._fields_ = [
    # not < (IN) Gaze data for Left Eye of Stereo rendering mode
    ('sLeftEye', NV_FOVEATED_RENDERING_GAZE_DATA_PER_EYE_V1),
    # not < (IN) Gaze data for Right Eye of Stereo rendering mode
    ('sRightEye', NV_FOVEATED_RENDERING_GAZE_DATA_PER_EYE_V1),
]
_Union_6.sStereoData = sStereoData

_Union_6._fields_ = [
    # not < (IN) Gaze data for Mono rendering mode
    ('sMonoData', NV_FOVEATED_RENDERING_GAZE_DATA_PER_EYE_V1),
    ('sStereoData', _Union_6.sStereoData),
]
_NV_FOVEATED_RENDERING_UPDATE_GAZE_DATA_PARAMS._Union_6 = _Union_6

_NV_FOVEATED_RENDERING_UPDATE_GAZE_DATA_PARAMS._anonymous_ = (
    '_Union_6',
)

_NV_FOVEATED_RENDERING_UPDATE_GAZE_DATA_PARAMS._fields_ = [
    # not < (IN) Struct version
    ('version', NvU32),
    # not < (IN) Reserved for future use
    ('flags', NvU32),
    # not < (IN) Timestamp at which the gaze data has been captured.
    # Should be larger than timestamp provided at previous update.
    ('Timestamp', NvU64),
    ('_Union_6', _NV_FOVEATED_RENDERING_UPDATE_GAZE_DATA_PARAMS._Union_6),
]
NV_FOVEATED_RENDERING_UPDATE_GAZE_DATA_PARAMS = NV_FOVEATED_RENDERING_UPDATE_GAZE_DATA_PARAMS_V1
NV_FOVEATED_RENDERING_UPDATE_GAZE_DATA_PARAMS_VER1 = (
    MAKE_NVAPI_VERSION(NV_FOVEATED_RENDERING_UPDATE_GAZE_DATA_PARAMS_V1, 1)
)
NV_FOVEATED_RENDERING_UPDATE_GAZE_DATA_PARAMS_VER = (
    NV_FOVEATED_RENDERING_UPDATE_GAZE_DATA_PARAMS_VER1
)


class ID3DNvGazeHandler_V1(comtypes.IUnknown):
    _iid_ = GUID()
    _methods_ = [
        #  Updates the gaze data for foveated rendering
        comtypes.STDMETHOD(
            NvAPI_Status,
            'UpdateGazeData',
            (POINTER(comtypes.IUnknown), POINTER(NV_FOVEATED_RENDERING_UPDATE_GAZE_DATA_PARAMS))
        ),
    ]


ID3DNvGazeHandler = ID3DNvGazeHandler_V1
ID3DNvGazeHandler_VER1 = MAKE_NVAPI_VERSION(ID3DNvGazeHandler_V1, 1)
ID3DNvGazeHandler_VER = ID3DNvGazeHandler_VER1


class _NV_GAZE_DATA_TYPE(ENUM):
    NV_GAZE_DATA_INVALID = 0
    NV_GAZE_DATA_MONO = 1
    NV_GAZE_DATA_STEREO = 2
    NV_GAZE_DATA_MAX = NV_GAZE_DATA_STEREO


NV_GAZE_DATA_TYPE = _NV_GAZE_DATA_TYPE

_NV_GAZE_HANDLER_INIT_PARAMS_V1._fields_ = [
    # not < (IN) Struct version
    ('version', NvU32),
    # not < (IN) ID of the gaze data provider. Needed only for
    # supporting more than one device with eye tracking.
    ('GazeDataDeviceId', NvU32),
    # not < (IN) Describes whether gaze is Mono or Stereo
    ('GazeDataType', NV_GAZE_DATA_TYPE),
    # not < (IN) Reserved for future use
    ('flags', NvU32),
    # not < (IN) Horizontal Field of View
    ('fHorizontalFOV', FLOAT),
    # not < (IN) Vertical Field of View
    ('fVericalFOV', FLOAT),
    # not < (OUT) Interface for Gaze Data Handler
    ('ppNvGazeHandler', POINTER(POINTER(ID3DNvGazeHandler_V1))),
]
NV_GAZE_HANDLER_INIT_PARAMS = NV_GAZE_HANDLER_INIT_PARAMS_V1
NV_GAZE_HANDLER_INIT_PARAMS_VER1 = (
    MAKE_NVAPI_VERSION(NV_GAZE_HANDLER_INIT_PARAMS_V1, 1)
)
NV_GAZE_HANDLER_INIT_PARAMS_VER = NV_GAZE_HANDLER_INIT_PARAMS_VER1

# not SUPPORTED OS: Windows 7 and higher
# not

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_InitializeNvGazeHandler
# not DESCRIPTION: Creates an interface for updating and managing gaze
# data
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 430
# not
# not \param [in]  pDevice     The device to be used for creating the
# Gaze Handler interface
# not         \note This should be same as the device used with VRS
# Handler. See also: NvAPI_D3D_InitializeVRSHelper.
# not \param [in]  pInitializeNvGazeHandlerParams Descriptor for Gaze
# Data Handler initialization
# not
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not  If there are return error codes with specific meaning for this
# API, they are listed below.
# not  (none)
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D_InitializeNvGazeHandler = hDll.D3D_InitializeNvGazeHandler
NvAPI_D3D_InitializeNvGazeHandler.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_D3D_InitializeNvGazeHandler(__in    IUnknown *pDevice,
#                                                   __inout NV_GAZE_HANDLER_INIT_PARAMS *pInitializeNvGazeHandlerParams);


# not SUPPORTED OS: Windows 7 and higher
# not

# not \ingroup dx
class NV_SMP_ASSIST_TYPE(ENUM):
    NV_SMP_ASSIST_NONE = 0
    NV_SMP_ASSIST_MRS = 1
    NV_SMP_ASSIST_LMS = 2
    NV_SMP_ASSIST_NUM_TYPES = 3


class NV_SMP_ASSIST_LEVEL(ENUM):
    # Full assistance. App selects a pre-baked MRS/LMS config, driver
    # handles correct setting of viewport, scissors and FastGS
    NV_SMP_ASSIST_LEVEL_FULL = 0

    # Partial assistance. App provides a custom MRS/LMS config, driver
    # handles correct setting of viewport, scissors and FastGS
    NV_SMP_ASSIST_LEVEL_PARTIAL = 1

    # Minimal assistance. App provides viewports and scissors. App
    # sets FastGS as required. App sets LMS params as required
    # (NvAPI_D3D_SetModifiedWMode). App provides SMPType as NONE.
    # Driver handles correct setting of viewports and scissors.
    NV_SMP_ASSIST_LEVEL_MINIMAL = 2
    NV_SMP_ASSIST_NUM_LEVELS = 3


class NV_MRS_CONFIG(ENUM):
    NV_MRS_CONFIG_BALANCED = 0
    NV_MRS_CONFIG_AGGRESSIVE = 1
    NV_MRS_CONFIG_OCULUSRIFT_CV1_CONSERVATIVE = 2
    NV_MRS_CONFIG_OCULUSRIFT_CV1_BALANCED = 3
    NV_MRS_CONFIG_OCULUSRIFT_CV1_AGGRESSIVE = 4
    NV_MRS_CONFIG_HTC_VIVE_CONSERVATIVE = 5
    NV_MRS_CONFIG_HTC_VIVE_BALANCED = 6
    NV_MRS_CONFIG_HTC_VIVE_AGGRESSIVE = 7
    NV_MRS_NUM_CONFIGS = 8


class NV_LMS_CONFIG(ENUM):
    NV_LMS_CONFIG_OCULUSRIFT_CV1_CONSERVATIVE = 0
    NV_LMS_CONFIG_OCULUSRIFT_CV1_BALANCED = 1
    NV_LMS_CONFIG_OCULUSRIFT_CV1_AGGRESSIVE = 2
    NV_LMS_CONFIG_HTC_VIVE_CONSERVATIVE = 3
    NV_LMS_CONFIG_HTC_VIVE_BALANCED = 4
    NV_LMS_CONFIG_HTC_VIVE_AGGRESSIVE = 5
    NV_LMS_NUM_CONFIGS = 6


NV_SMP_ASSIST_FLAGS_DEFAULT = 0x00000000
NV_SMP_ASSIST_MAX_VIEWPORTS = 16

_NV_MRS_CUSTOM_CONFIG_V1._fields_ = [
    # not < (IN) Size of the central viewport, ranging
    # (0,1], where 1 is full original viewport size
    ('centerWidth', FLOAT),
    ('centerHeight', FLOAT),
    # not < (IN) Location of the central viewport, ranging 0..1, where
    # 0.5 is the center of the screen
    ('centerX', FLOAT),
    ('centerY', FLOAT),
    # not < (IN) Pixel density scale factors: how much the linear
    # pixel density is scaled within each row and column
    # (1.0 = full density)
    ('densityScaleX', FLOAT * 3),
    ('densityScaleY', FLOAT * 3),
]
NV_MRS_CUSTOM_CONFIG = NV_MRS_CUSTOM_CONFIG_V1

# not < (OUT) MRS Instanced stereo config returned by the SMP Assist
# GetConstants API
_NV_MRS_INSTANCED_STEREO_CONFIG_V1._fields_ = [
    # not < (OUT) Size of the central viewport, ranging
    # (0,1], where 1 is full original viewport size
    ('centerWidth', FLOAT * 2),
    ('centerHeight', FLOAT),
    # not < (OUT) Location of the central viewport, ranging 0..1,
    # where 0.5 is the center of the screen
    ('centerX', FLOAT * 2),
    ('centerY', FLOAT),
    # not < (OUT) Pixel density scale factors: how much the linear
    # pixel density is scaled within each row and column
    # (1.0 = full density)
    ('densityScaleX', FLOAT * 5),
    ('densityScaleY', FLOAT * 3),
]
NV_MRS_INSTANCED_STEREO_CONFIG = NV_MRS_INSTANCED_STEREO_CONFIG_V1

_NV_LMS_CUSTOM_CONFIG_V1._fields_ = [
    # not < (IN) LMS params to control warping of the 2 left quadrants
    ('warpLeft', FLOAT),
    # not < (IN) LMS params to control warping of the 2 right quadrants
    ('warpRight', FLOAT),
    # not < (IN) LMS params to control warping of the 2 upper quadrants
    ('warpUp', FLOAT),
    # not < (IN) LMS params to control warping of the 2 lower quadrants
    ('warpDown', FLOAT),
    # not < (IN) LMS params to control the width of the 2 left
    # quandrants relative to the bounding box width
    ('relativeSizeLeft', FLOAT),
    # not < (IN) LMS params to control the width of the 2 right
    # quandrants relative to the bounding box width
    ('relativeSizeRight', FLOAT),
    # not < (IN) LMS params to control the height of the 2 upper
    # quandrants relative to the bounding box height
    ('relativeSizeUp', FLOAT),
    # not < (IN) LMS params to control the height of the 2 lower
    # quandrants relative to the bounding box height
    ('relativeSizeDown', FLOAT),
]
NV_LMS_CUSTOM_CONFIG = NV_LMS_CUSTOM_CONFIG_V1

# not < (OUT) LMS Instanced stereo config returned by the SMP Assist
# GetConstants API
_NV_LMS_INSTANCED_STEREO_CONFIG_V1._fields_ = [
    # not < (OUT) LMS config for the Left eye view
    ('sLeftConfig', NV_LMS_CUSTOM_CONFIG_V1),
    # not < (OUT) LMS config for the Right eye view
    ('sRightConfig', NV_LMS_CUSTOM_CONFIG_V1),
]
NV_LMS_INSTANCED_STEREO_CONFIG = NV_LMS_INSTANCED_STEREO_CONFIG_V1


class _NV_SMP_ASSIST_EYE_INDEX(ENUM):
    NV_SMP_ASSIST_EYE_INDEX_MONO = 0
    NV_SMP_ASSIST_EYE_INDEX_LEFT_EYE = 1
    NV_SMP_ASSIST_EYE_INDEX_RIGHT_EYE = 2
    NV_SMP_ASSIST_EYE_INDEX_INSTANCED_STEREO = 3


NV_SMP_ASSIST_EYE_INDEX = _NV_SMP_ASSIST_EYE_INDEX
NV_SMP_ASSIST_MINIMAL_LEVEL_NUM_EYE_INDICES = 4

_NV_CUSTOM_RECTS_V1._fields_ = [
    ('numViewports', NvU32 * NV_SMP_ASSIST_MINIMAL_LEVEL_NUM_EYE_INDICES),
    # not < (IN) Viewports, for each eye index, that should be set
    # when app calls Enable(eyeIndex)
    ('pViewports', POINTER(D3D11_VIEWPORT) * NV_SMP_ASSIST_MINIMAL_LEVEL_NUM_EYE_INDICES),
    # not < (IN) Scissors, for each eye index, that should be set when
    # app calls Enable(eyeIndex)
    ('pScissors', POINTER(D3D11_RECT) * NV_SMP_ASSIST_MINIMAL_LEVEL_NUM_EYE_INDICES),
]
NV_CUSTOM_RECTS = NV_CUSTOM_RECTS_V1

_NV_SMP_ASSIST_ENABLE_PARAMS_V1._fields_ = [
    # not < (IN) Structure version
    ('version', NvU32),
    # not < (IN) Rendering mode for upcoming draw calls
    # (Mono/Stereo-Left/Stereo-Right/Instanced Stereo)
    ('eEyeIndex', NV_SMP_ASSIST_EYE_INDEX),
]
NV_SMP_ASSIST_ENABLE_PARAMS = NV_SMP_ASSIST_ENABLE_PARAMS_V1
NV_SMP_ASSIST_ENABLE_PARAMS_VER1 = (
    MAKE_NVAPI_VERSION(NV_SMP_ASSIST_ENABLE_PARAMS_V1, 1)
)
NV_SMP_ASSIST_ENABLE_PARAMS_VER = NV_SMP_ASSIST_ENABLE_PARAMS_VER1

_NV_SMP_ASSIST_DISABLE_PARAMS_V1._fields_ = [
    # not < (IN) Structure version
    ('version', NvU32),
    # not < (IN) Unused.
    ('Reserved', NvU32),
]
NV_SMP_ASSIST_DISABLE_PARAMS = NV_SMP_ASSIST_DISABLE_PARAMS_V1
NV_SMP_ASSIST_DISABLE_PARAMS_VER1 = (
    MAKE_NVAPI_VERSION(NV_SMP_ASSIST_DISABLE_PARAMS_V1, 1)
)
NV_SMP_ASSIST_DISABLE_PARAMS_VER = NV_SMP_ASSIST_DISABLE_PARAMS_VER1

# FastGS constant buffer data returned by the GetConstants API.
# Refer VRWorks SDK's multiprojection_dx app (struct FastGSCBData)
_NV_SMP_ASSIST_FASTGSCBDATA_V1._fields_ = [
    # not < (OUT) FastGS constant buffer data for Multi-Res Shading/
    # Lens Matched Shading
    ('NDCSplitsX', FLOAT * 2),
    ('NDCSplitsY', FLOAT * 2),
]
NV_SMP_ASSIST_FASTGSCBDATA = NV_SMP_ASSIST_FASTGSCBDATA_V1

_NV_SMP_ASSIST_FASTGSCBDATA_MRS_INSTANCED_STEREO_V1._fields_ = [
    # not < (OUT) FastGS constant buffer data for Multi-Res Shading
    # (Instanced stereo). 2 splits for left eye followed by 2 splits
    # for right eye
    ('NDCSplitsX', FLOAT * 4),
    ('NDCSplitsY', FLOAT * 2),
]
NV_SMP_ASSIST_FASTGSCBDATA_MRS_INSTANCED_STEREO = NV_SMP_ASSIST_FASTGSCBDATA_MRS_INSTANCED_STEREO_V1

# Constant buffer data to supply the UV-remapping helper functions
# Refer VRWorks SDK's multiprojection_dx app (struct RemapCBData)
_NV_SMP_ASSIST_REMAPCBDATA_V1._fields_ = [
    # not < (OUT) Constant buffer data to supply the UV-remapping
    # helper functions
    ('ClipToWindowSplitsX', FLOAT * 2),
    ('ClipToWindowSplitsY', FLOAT * 2),
    # ClipToWindowX[i][0] is Scale and ClipToWindowX[i][1] is Bias
    ('ClipToWindowX', (FLOAT * 3) * 2),
    # ClipToWindowY[i][0] is Scale and ClipToWindowY[i][1] is Bias
    ('ClipToWindowY', (FLOAT * 3) * 2),
    # ClipToWindowZ[0] is Scale and ClipToWindowZ[1] is Bias
    ('ClipToWindowZ', FLOAT * 2),
    ('WindowToClipSplitsX', FLOAT * 2),
    ('WindowToClipSplitsY', FLOAT * 2),
    # WindowToClipX[i][0] is Scale and WindowToClipX[i][1] is Bias
    ('WindowToClipX', (FLOAT * 3) * 2),
    # WindowToClipY[i][0] is Scale and WindowToClipY[i][1] is Bias
    ('WindowToClipY', (FLOAT * 3) * 2),
    # WindowToClipZ[0] is Scale and WindowToClipZ[1] is Bias
    ('WindowToClipZ', FLOAT * 2),
    ('BoundingRectOriginX', FLOAT),
    ('BoundingRectOriginY', FLOAT),
    ('BoundingRectSizeWidth', FLOAT),
    ('BoundingRectSizeHeight', FLOAT),
    ('BoundingRectSizeInvWidth', FLOAT),
    ('BoundingRectSizeInvHeight', FLOAT),
    ('Padding', FLOAT * 2),
]
NV_SMP_ASSIST_REMAPCBDATA = NV_SMP_ASSIST_REMAPCBDATA_V1


# not SUPPORTED OS: Windows 7 and higher
# not
class _Union_7(ctypes.Union):
    pass


_Union_7._fields_ = [
    # not < (OUT) If eSMPAssistType is MRS, then MRS config will be
    # populated
    ('sMRSConfig', NV_MRS_CUSTOM_CONFIG_V1),
    # not < (OUT) If eSMPAssistType is LMS, then LMS config will be
    # populated
    ('sLMSConfig', NV_LMS_CUSTOM_CONFIG_V1),
]
_NV_SMP_ASSIST_GET_CONSTANTS_V3._Union_7 = _Union_7


class _Union_8(ctypes.Union):
    pass


_Union_8._fields_ = [
    # not < (OUT) If eSMPAssistType is MRS and eEyeIndex is
    # NV_SMP_ASSIST_EYE_INDEX_INSTANCED_STEREO then MRS Instanced
    # stereo config will be populated
    ('sMRS_ISConfig', NV_MRS_INSTANCED_STEREO_CONFIG_V1),
    # not < (OUT) If eSMPAssistType is LMS and eEyeIndex is
    # NV_SMP_ASSIST_EYE_INDEX_INSTANCED_STEREO then LMS Instanced
    # stereo config will be populated
    ('sLMS_ISConfig', NV_LMS_INSTANCED_STEREO_CONFIG_V1),
]
_NV_SMP_ASSIST_GET_CONSTANTS_V3._Union_8 = _Union_8

_NV_SMP_ASSIST_GET_CONSTANTS_V3._anonymous_ = (
    '_Union_7',
    '_Union_8',
)

_NV_SMP_ASSIST_GET_CONSTANTS_V3._fields_ = [
    # not < (IN) Structure version
    ('version', NvU32),
    # not < (IN) Viewports/scissors/constant buffer data corresponding
    # to the input eEyeIndex will be returned
    ('eEyeIndex', NV_SMP_ASSIST_EYE_INDEX),
    # not < (OUT) Number of valid viewport entries
    ('numViewports', NvU32),
    # not < (OUT) If not NULL, this will contain the viewports
    # computed by driver based on init params
    ('pViewports', POINTER(D3D11_VIEWPORT)),
    # not < (OUT) If not NULL, this will contain the scissors computed
    # by the driver based on init params
    ('pScissors', POINTER(D3D11_RECT)),
    # not < (OUT) SMP type provided in Init call
    ('eSMPAssistType', NV_SMP_ASSIST_TYPE),
    # not < (OUT) SMP Assist level provided in Init call
    ('eSMPAssistLevel', NV_SMP_ASSIST_LEVEL),
    ('_Union_7', _NV_SMP_ASSIST_GET_CONSTANTS_V3._Union_7),
    # not < (OUT) MRS/LMS projection size
    ('projectionSizeWidth', FLOAT),
    # not < (OUT)
    ('projectionSizeHeight', FLOAT),
    # not < (OUT) If not NULL, this will contain constant buffer data
    # to supply the FastGS for culling primitives per-viewport
    ('pFastGSCBData', POINTER(NV_SMP_ASSIST_FASTGSCBDATA_V1)),
    # not < (OUT) If not NULL, this will contain constant buffer data
    # to supply the UV-remapping helper functions
    ('pRemapCBData', POINTER(NV_SMP_ASSIST_REMAPCBDATA_V1)),
    # not < (OUT) If eSMPType is MRS or LMS then this will be a union
    # of the individual viewports populated in pViewports
    ('boundingViewport', D3D11_VIEWPORT),
    # not < (OUT) If eSMPType is MRS or LMS then this will be a union
    # of the individual scissor rects populated in pScissors
    ('boundingScissor', D3D11_RECT),
    ('_Union_8', _NV_SMP_ASSIST_GET_CONSTANTS_V3._Union_8),
    # not < (OUT) If non-NULL and eSMPAssistType is MRS and eEyeIndex
    # is NV_SMP_ASSIST_EYE_INDEX_INSTANCED_STEREO then MRS Instanced
    # stereo FastGS constant buffer data will be populated
    ('pFastGSCBDataMRS_IS', POINTER(NV_SMP_ASSIST_FASTGSCBDATA_MRS_INSTANCED_STEREO_V1)),
]
NV_SMP_ASSIST_GET_CONSTANTS_VER3 = (
    MAKE_NVAPI_VERSION(NV_SMP_ASSIST_GET_CONSTANTS_V3, 3)
)
NV_SMP_ASSIST_GET_CONSTANTS = NV_SMP_ASSIST_GET_CONSTANTS_V3
NV_SMP_ASSIST_GET_CONSTANTS_VER = NV_SMP_ASSIST_GET_CONSTANTS_VER3


# not SUPPORTED OS: Windows 7 and higher
# not
class _Union_9(ctypes.Union):
    pass


_Union_9._fields_ = [
    # not < (IN) If eSMPAssistType is MRS and SMP Assist Level is Full
    # then provide MRS config enum
    ('eMRSConfig', NV_MRS_CONFIG),
    # not < (IN) If eSMPAssistType is LMS and SMP Assist Level is Full
    # then provide LMS config enum
    ('eLMSConfig', NV_LMS_CONFIG),
    # not < (IN) If eSMPAssistType is MRS and SMP Assist Level is
    # Partial, then provide MRS config
    ('sMRSCustomConfig', NV_MRS_CUSTOM_CONFIG_V1),
    # not < (IN) If eSMPAssistType is LMS and SMP Assist Level is
    # Partial, then provide LMS config
    ('sLMSCustomConfig', NV_LMS_CUSTOM_CONFIG_V1),
    # not < (IN) If SMP Assist Level is Minimal, provide custom
    # viewports and scissor rects for each eye index.
    ('sCustomRects', NV_CUSTOM_RECTS_V1),
]
_NV_SMP_ASSIST_SETUP_PARAMS_V1._Union_9 = _Union_9

_NV_SMP_ASSIST_SETUP_PARAMS_V1._anonymous_ = (
    '_Union_9',
)

_NV_SMP_ASSIST_SETUP_PARAMS_V1._fields_ = [
    # not < (IN) Structure version
    ('version', NvU32),
    ('_Union_9', _NV_SMP_ASSIST_SETUP_PARAMS_V1._Union_9),
    # not < (IN) A resolution multiplier in the range [0.1, 3.0] if
    # app wants to render at higher resolution
    ('resolutionScale', FLOAT),
    # not < (IN) Rect on the rendertarget, to place the projection
    ('boundingBox', D3D11_VIEWPORT),
    # not < (IN) Default set to 0. If non-zero, MRS/LMS viewports'
    # TopLeftX and TopLeftY will be
    ('vpOffsets', FLOAT * 2),
]
NV_SMP_ASSIST_SETUP_PARAMS = NV_SMP_ASSIST_SETUP_PARAMS_V1
NV_SMP_ASSIST_SETUP_PARAMS_VER1 = (
    MAKE_NVAPI_VERSION(NV_SMP_ASSIST_SETUP_PARAMS_V1, 1)
)
NV_SMP_ASSIST_SETUP_PARAMS_VER = NV_SMP_ASSIST_SETUP_PARAMS_VER1

_NV_SMP_ASSIST_UPDATE_INSTANCEDSTEREO_DATA_PARAMS_V1._fields_ = [
    # not < (IN) Structure version
    ('version', NvU32),
    # Patch instanced stereo shaders (created with packed eye index)
    # with this SMPAssistType (NV_SMP_ASSIST_LMS only)
    ('eSMPAssistType', NV_SMP_ASSIST_TYPE),
    # Left eye: outpos.x = dotproduct(outputpos, leftCoeffs) +
    # leftConst
    ('leftCoeffs', FLOAT * 4),
    ('leftConst', FLOAT),
    # Right eye: outpos.x = dotproduct(outputpos, rightCoeffs) +
    # rightConst
    ('rightCoeffs', FLOAT * 4),
    ('rightConst', FLOAT),
]
NV_SMP_ASSIST_UPDATE_INSTANCEDSTEREO_DATA_PARAMS = NV_SMP_ASSIST_UPDATE_INSTANCEDSTEREO_DATA_PARAMS_V1
NV_SMP_ASSIST_UPDATE_INSTANCEDSTEREO_DATA_PARAMS_VER1 = (
    MAKE_NVAPI_VERSION(NV_SMP_ASSIST_UPDATE_INSTANCEDSTEREO_DATA_PARAMS_V1, 1)
)
NV_SMP_ASSIST_UPDATE_INSTANCEDSTEREO_DATA_PARAMS_VER = (
    NV_SMP_ASSIST_UPDATE_INSTANCEDSTEREO_DATA_PARAMS_VER1
)


# not SUPPORTED OS: Windows 7 and higher
# not
class ID3DNvSMPAssist_V1(comtypes.IUnknown):
    _iid_ = GUID()
    _methods_ = [
        # ////////////////////////////   VER1 methods //////////////////////////////////////////
        #  Disable SMP Assist for further Draw calls
        comtypes.STDMETHOD(
            NvAPI_Status,
            'Disable',
            (POINTER(comtypes.IUnknown), POINTER(NV_SMP_ASSIST_DISABLE_PARAMS))
        ),
        #  Enable SMP Assist for further Draw calls. App has to provide the type of rendering done in upcoming Draw calls - Mono/Left eye/Right eye/Instanced Stereo
        comtypes.STDMETHOD(
            NvAPI_Status,
            'Enable',
            (POINTER(comtypes.IUnknown), POINTER(NV_SMP_ASSIST_ENABLE_PARAMS))
        ),
        #  Get the constants used by the drivers
        comtypes.STDMETHOD(
            NvAPI_Status,
            'GetConstants',
            (POINTER(NV_SMP_ASSIST_GET_CONSTANTS),)
        ),
        #  Setup the projections (rects, constant buffer data etc.)
        comtypes.STDMETHOD(
            NvAPI_Status,
            'SetupProjections',
            (POINTER(comtypes.IUnknown), POINTER(NV_SMP_ASSIST_SETUP_PARAMS))
        ),
        #  Update instanced stereo specific data
        comtypes.STDMETHOD(
            NvAPI_Status,
            'UpdateInstancedStereoData',
            (POINTER(comtypes.IUnknown), POINTER(NV_SMP_ASSIST_UPDATE_INSTANCEDSTEREO_DATA_PARAMS))
        ),
        # ////////////////////////////   end of VER1 methods   //////////////////////////////////////////
    ]


ID3DNvSMPAssist = ID3DNvSMPAssist_V1
ID3DNVSMPASSIST_VER1 = MAKE_NVAPI_VERSION(ID3DNvSMPAssist_V1, 1)
ID3DNVSMPASSIST_VER = ID3DNVSMPASSIST_VER1

# not SUPPORTED OS: Windows 7 and higher
# not
_NV_SMP_ASSIST_INITIALIZE_PARAMS_V1._fields_ = [
    # not < (IN) Structure version
    ('version', NvU32),
    # not < (IN) None/MRS/LMS
    ('eSMPAssistType', NV_SMP_ASSIST_TYPE),
    # not < (IN) Full/Partial/Minimal
    ('eSMPAssistLevel', NV_SMP_ASSIST_LEVEL),
    # not < (IN) Flags, if any
    ('flags', NvU32),
    # not < (OUT) Interface pointer returned by the Init call. Use for
    # future Enable/Disable etc. calls
    ('ppD3DNvSMPAssist', POINTER(POINTER(ID3DNvSMPAssist))),
]
NV_SMP_ASSIST_INITIALIZE_PARAMS_VER1 = (
    MAKE_NVAPI_VERSION(NV_SMP_ASSIST_INITIALIZE_PARAMS_V1, 1)
)
NV_SMP_ASSIST_INITIALIZE_PARAMS = NV_SMP_ASSIST_INITIALIZE_PARAMS_V1
NV_SMP_ASSIST_INITIALIZE_PARAMS_VER = (
    NV_SMP_ASSIST_INITIALIZE_PARAMS_VER1
)

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_InitializeSMPAssist
# not DESCRIPTION: Initialize SMP Assist extension. Take the
# SMPAssist(MRS/LMS) params from the application.
# not   Provide the application with a interface pointer for future
# use.
# not
# not \since Release: 396
# not \param [in]  pDevice    Pointer to IUnknown
# (Currently supports ID3D11Device)
# not \param [inout] pSMPAssistInitParams SMP Assist initialization
# params
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not  If there are return error codes with specific meaning for this
# API, they are listed below.
# not \retval ::NVAPI_OK     Call succeeded.
# not \retval ::NVAPI_ERROR     Call failed.
# not \retval ::NVAPI_INVALID_ARGUMENT  One of the required input
# arguments was NULL
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D_InitializeSMPAssist = hDll.D3D_InitializeSMPAssist
NvAPI_D3D_InitializeSMPAssist.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D_InitializeSMPAssist(__in IUnknown *pDevice, __inout NV_SMP_ASSIST_INITIALIZE_PARAMS *pSMPAssistInitParams);


# not SUPPORTED OS: Windows 7 and higher
# not

# not \ingroup dx
_NV_QUERY_SMP_ASSIST_SUPPORT_PARAMS_V1._fields_ = [
    # not < (IN) Structure version
    ('version', NvU32),
    # not < (IN) None/MRS/LMS
    ('eSMPAssistType', NV_SMP_ASSIST_TYPE),
    # not < (IN) Full/Partial/Minimal
    ('eSMPAssistLevel', NV_SMP_ASSIST_LEVEL),
    # not < (OUT) SMP Assist supported or not
    ('bSMPAssistSupported', NvBool),
]
NV_QUERY_SMP_ASSIST_SUPPORT_PARAMS = NV_QUERY_SMP_ASSIST_SUPPORT_PARAMS_V1
NV_QUERY_SMP_ASSIST_SUPPORT_PARAMS_VER1 = (
    MAKE_NVAPI_VERSION(NV_QUERY_SMP_ASSIST_SUPPORT_PARAMS_V1, 1)
)
NV_QUERY_SMP_ASSIST_SUPPORT_PARAMS_VER = (
    NV_QUERY_SMP_ASSIST_SUPPORT_PARAMS_VER1
)

# not SUPPORTED OS: Windows 7 and higher
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_QuerySMPAssistSupport
# not DESCRIPTION: Query SMP assist extension support.
# not
# not \since Release: 396
# not \param [in]  pDev      Pointer to IUnknown
# (Currently supports ID3D11Device)
# not \param [out] pQuerySMPAssistSupportParams  Pointer to a
# structure returning requested SMP assist support
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not  If there are return error codes with specific meaning for this
# API, they are listed below.
# not \retval ::NVAPI_NOT_SUPPORTED     Requested SMP assist is not
# supported.
# not \retval ::NVAPI_OK      Call succeeded. Check value of
# pQuerySMPAssistSupportParams.bSMPAssistSupported
# not \retval ::NVAPI_INVALID_POINTER    pDev or
# pQuerySMPAssistSupportParams was a NULL pointer
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D_QuerySMPAssistSupport = hDll.D3D_QuerySMPAssistSupport
NvAPI_D3D_QuerySMPAssistSupport.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D_QuerySMPAssistSupport(__in IUnknown *pDev, __inout NV_QUERY_SMP_ASSIST_SUPPORT_PARAMS *pQuerySMPAssistSupportParams);


# not \ingroup vidio
# not Unique identifier for VIO owner
# (process identifier or NVVIOOWNERID_NONE)
NVVIOOWNERID = NvU32
# not \addtogroup vidio
# not @{
# not < Unregistered ownerId
NVVIOOWNERID_NONE = 0


# not Owner type for device
class _NVVIOOWNERTYPE(ENUM):
    NVVIOOWNERTYPE_NONE = 1
    NVVIOOWNERTYPE_APPLICATION = 2

    # not < Desktop transparent mode owns the device
    # (not applicable for video input)
    NVVIOOWNERTYPE_DESKTOP = 3


NVVIOOWNERTYPE = _NVVIOOWNERTYPE

# Access rights for NvAPI_VIO_Open()
# not Read access   (not applicable for video output)
NVVIO_O_READ = 0x00000000

# not Write exclusive access (not applicable for video input)
NVVIO_O_WRITE_EXCLUSIVE = 0x00010001

# not
NVVIO_VALID_ACCESSRIGHTS = NVVIO_O_READ | NVVIO_O_WRITE_EXCLUSIVE

# not VIO_DATA.ulOwnerID high-bit is set only if device has been
# initialized by VIOAPI
# not examined at NvAPI_GetCapabilities | NvAPI_VIO_Open to determine if
# settings need to be applied from registry or POR state read
NVVIO_OWNERID_INITIALIZED = 0x80000000

# not VIO_DATA.ulOwnerID next-bit is set only if device is currently in
# exclusive write access mode from NvAPI_VIO_Open()
NVVIO_OWNERID_EXCLUSIVE = 0x40000000

# not VIO_DATA.ulOwnerID lower bits are:
# not NVGVOOWNERTYPE_xxx enumerations indicating use context
# not < mask for NVVIOOWNERTYPE_xxx
NVVIO_OWNERID_TYPEMASK = 0x0FFFFFFF


# not @}
# ---------------------------------------------------------------------
# Enumerations
# ---------------------------------------------------------------------
# not \addtogroup vidio
# not @{
# not Video signal format and resolution
class _NVVIOSIGNALFORMAT(ENUM):
    NVVIOSIGNALFORMAT_NONE = 1
    NVVIOSIGNALFORMAT_487I_59_94_SMPTE259_NTSC = 2
    NVVIOSIGNALFORMAT_576I_50_00_SMPTE259_PAL = 3
    NVVIOSIGNALFORMAT_1035I_60_00_SMPTE260 = 4
    NVVIOSIGNALFORMAT_1035I_59_94_SMPTE260 = 5
    NVVIOSIGNALFORMAT_1080I_50_00_SMPTE295 = 6
    NVVIOSIGNALFORMAT_1080I_60_00_SMPTE274 = 7
    NVVIOSIGNALFORMAT_1080I_59_94_SMPTE274 = 8
    NVVIOSIGNALFORMAT_1080I_50_00_SMPTE274 = 9
    NVVIOSIGNALFORMAT_1080P_30_00_SMPTE274 = 10
    NVVIOSIGNALFORMAT_1080P_29_97_SMPTE274 = 11
    NVVIOSIGNALFORMAT_1080P_25_00_SMPTE274 = 12
    NVVIOSIGNALFORMAT_1080P_24_00_SMPTE274 = 13
    NVVIOSIGNALFORMAT_1080P_23_976_SMPTE274 = 14
    NVVIOSIGNALFORMAT_720P_60_00_SMPTE296 = 15
    NVVIOSIGNALFORMAT_720P_59_94_SMPTE296 = 16
    NVVIOSIGNALFORMAT_720P_50_00_SMPTE296 = 17
    NVVIOSIGNALFORMAT_1080I_48_00_SMPTE274 = 18
    NVVIOSIGNALFORMAT_1080I_47_96_SMPTE274 = 19
    NVVIOSIGNALFORMAT_720P_30_00_SMPTE296 = 20
    NVVIOSIGNALFORMAT_720P_29_97_SMPTE296 = 21
    NVVIOSIGNALFORMAT_720P_25_00_SMPTE296 = 22
    NVVIOSIGNALFORMAT_720P_24_00_SMPTE296 = 23
    NVVIOSIGNALFORMAT_720P_23_98_SMPTE296 = 24
    NVVIOSIGNALFORMAT_2048P_30_00_SMPTE372 = 25
    NVVIOSIGNALFORMAT_2048P_29_97_SMPTE372 = 26
    NVVIOSIGNALFORMAT_2048I_60_00_SMPTE372 = 27
    NVVIOSIGNALFORMAT_2048I_59_94_SMPTE372 = 28
    NVVIOSIGNALFORMAT_2048P_25_00_SMPTE372 = 29
    NVVIOSIGNALFORMAT_2048I_50_00_SMPTE372 = 30
    NVVIOSIGNALFORMAT_2048P_24_00_SMPTE372 = 31
    NVVIOSIGNALFORMAT_2048P_23_98_SMPTE372 = 32
    NVVIOSIGNALFORMAT_2048I_48_00_SMPTE372 = 33
    NVVIOSIGNALFORMAT_2048I_47_96_SMPTE372 = 34
    NVVIOSIGNALFORMAT_1080PSF_25_00_SMPTE274 = 35
    NVVIOSIGNALFORMAT_1080PSF_29_97_SMPTE274 = 36
    NVVIOSIGNALFORMAT_1080PSF_30_00_SMPTE274 = 37
    NVVIOSIGNALFORMAT_1080PSF_24_00_SMPTE274 = 38
    NVVIOSIGNALFORMAT_1080PSF_23_98_SMPTE274 = 39
    NVVIOSIGNALFORMAT_1080P_50_00_SMPTE274_3G_LEVEL_A = 40
    NVVIOSIGNALFORMAT_1080P_59_94_SMPTE274_3G_LEVEL_A = 41
    NVVIOSIGNALFORMAT_1080P_60_00_SMPTE274_3G_LEVEL_A = 42
    NVVIOSIGNALFORMAT_1080P_60_00_SMPTE274_3G_LEVEL_B = 43
    NVVIOSIGNALFORMAT_1080I_60_00_SMPTE274_3G_LEVEL_B = 44
    NVVIOSIGNALFORMAT_2048I_60_00_SMPTE372_3G_LEVEL_B = 45
    NVVIOSIGNALFORMAT_1080P_50_00_SMPTE274_3G_LEVEL_B = 46
    NVVIOSIGNALFORMAT_1080I_50_00_SMPTE274_3G_LEVEL_B = 47
    NVVIOSIGNALFORMAT_2048I_50_00_SMPTE372_3G_LEVEL_B = 48
    NVVIOSIGNALFORMAT_1080P_30_00_SMPTE274_3G_LEVEL_B = 49
    NVVIOSIGNALFORMAT_2048P_30_00_SMPTE372_3G_LEVEL_B = 50
    NVVIOSIGNALFORMAT_1080P_25_00_SMPTE274_3G_LEVEL_B = 51
    NVVIOSIGNALFORMAT_2048P_25_00_SMPTE372_3G_LEVEL_B = 52
    NVVIOSIGNALFORMAT_1080P_24_00_SMPTE274_3G_LEVEL_B = 53
    NVVIOSIGNALFORMAT_2048P_24_00_SMPTE372_3G_LEVEL_B = 54
    NVVIOSIGNALFORMAT_1080I_48_00_SMPTE274_3G_LEVEL_B = 55
    NVVIOSIGNALFORMAT_2048I_48_00_SMPTE372_3G_LEVEL_B = 56
    NVVIOSIGNALFORMAT_1080P_59_94_SMPTE274_3G_LEVEL_B = 57
    NVVIOSIGNALFORMAT_1080I_59_94_SMPTE274_3G_LEVEL_B = 58
    NVVIOSIGNALFORMAT_2048I_59_94_SMPTE372_3G_LEVEL_B = 59
    NVVIOSIGNALFORMAT_1080P_29_97_SMPTE274_3G_LEVEL_B = 60
    NVVIOSIGNALFORMAT_2048P_29_97_SMPTE372_3G_LEVEL_B = 61
    NVVIOSIGNALFORMAT_1080P_23_98_SMPTE274_3G_LEVEL_B = 62
    NVVIOSIGNALFORMAT_2048P_23_98_SMPTE372_3G_LEVEL_B = 63
    NVVIOSIGNALFORMAT_1080I_47_96_SMPTE274_3G_LEVEL_B = 64
    NVVIOSIGNALFORMAT_2048I_47_96_SMPTE372_3G_LEVEL_B = 65
    NVVIOSIGNALFORMAT_END = 66


NVVIOSIGNALFORMAT = _NVVIOSIGNALFORMAT


# not SMPTE standards format
class _NVVIOVIDEOSTANDARD(ENUM):
    NVVIOVIDEOSTANDARD_SMPTE259 = 1
    NVVIOVIDEOSTANDARD_SMPTE260 = 2
    NVVIOVIDEOSTANDARD_SMPTE274 = 3
    NVVIOVIDEOSTANDARD_SMPTE295 = 4
    NVVIOVIDEOSTANDARD_SMPTE296 = 5
    NVVIOVIDEOSTANDARD_SMPTE372 = 6


NVVIOVIDEOSTANDARD = _NVVIOVIDEOSTANDARD


# not HD or SD video type
class _NVVIOVIDEOTYPE(ENUM):
    NVVIOVIDEOTYPE_SD = 1
    NVVIOVIDEOTYPE_HD = 2


NVVIOVIDEOTYPE = _NVVIOVIDEOTYPE


# not Interlace mode
class _NVVIOINTERLACEMODE(ENUM):
    NVVIOINTERLACEMODE_PROGRESSIVE = 1
    NVVIOINTERLACEMODE_INTERLACE = 2
    NVVIOINTERLACEMODE_PSF = 3


NVVIOINTERLACEMODE = _NVVIOINTERLACEMODE


# not Video data format
class _NVVIODATAFORMAT(ENUM):
    NVVIODATAFORMAT_UNKNOWN = - 1
    NVVIODATAFORMAT_R8G8B8_TO_YCRCB444 = 0
    NVVIODATAFORMAT_R8G8B8A8_TO_YCRCBA4444 = 1
    NVVIODATAFORMAT_R8G8B8Z10_TO_YCRCBZ4444 = 2
    NVVIODATAFORMAT_R8G8B8_TO_YCRCB422 = 3
    NVVIODATAFORMAT_R8G8B8A8_TO_YCRCBA4224 = 4
    NVVIODATAFORMAT_R8G8B8Z10_TO_YCRCBZ4224 = 5
    NVVIODATAFORMAT_X8X8X8_444_PASSTHRU = 6
    NVVIODATAFORMAT_X8X8X8A8_4444_PASSTHRU = 7
    NVVIODATAFORMAT_X8X8X8Z10_4444_PASSTHRU = 8
    NVVIODATAFORMAT_X10X10X10_444_PASSTHRU = 9
    NVVIODATAFORMAT_X10X8X8_444_PASSTHRU = 10
    NVVIODATAFORMAT_X10X8X8A10_4444_PASSTHRU = 11
    NVVIODATAFORMAT_X10X8X8Z10_4444_PASSTHRU = 12
    NVVIODATAFORMAT_DUAL_R8G8B8_TO_DUAL_YCRCB422 = 13
    NVVIODATAFORMAT_DUAL_X8X8X8_TO_DUAL_422_PASSTHRU = 14
    NVVIODATAFORMAT_R10G10B10_TO_YCRCB422 = 15
    NVVIODATAFORMAT_R10G10B10_TO_YCRCB444 = 16
    NVVIODATAFORMAT_X12X12X12_444_PASSTHRU = 17
    NVVIODATAFORMAT_X12X12X12_422_PASSTHRU = 18
    NVVIODATAFORMAT_Y10CR10CB10_TO_YCRCB422 = 19
    NVVIODATAFORMAT_Y8CR8CB8_TO_YCRCB422 = 20
    NVVIODATAFORMAT_Y10CR8CB8A10_TO_YCRCBA4224 = 21
    NVVIODATAFORMAT_R10G10B10_TO_RGB444 = 22
    NVVIODATAFORMAT_R12G12B12_TO_YCRCB444 = 23
    NVVIODATAFORMAT_R12G12B12_TO_YCRCB422 = 24


NVVIODATAFORMAT = _NVVIODATAFORMAT


# not Video output area
class _NVVIOOUTPUTAREA(ENUM):
    NVVIOOUTPUTAREA_FULLSIZE = 1
    NVVIOOUTPUTAREA_SAFEACTION = 2
    NVVIOOUTPUTAREA_SAFETITLE = 3


NVVIOOUTPUTAREA = _NVVIOOUTPUTAREA


# not Synchronization source
class _NVVIOSYNCSOURCE(ENUM):
    NVVIOSYNCSOURCE_SDISYNC = 1
    NVVIOSYNCSOURCE_COMPSYNC = 2


NVVIOSYNCSOURCE = _NVVIOSYNCSOURCE


# not Composite synchronization type
class _NVVIOCOMPSYNCTYPE(ENUM):
    NVVIOCOMPSYNCTYPE_AUTO = 1
    NVVIOCOMPSYNCTYPE_BILEVEL = 2
    NVVIOCOMPSYNCTYPE_TRILEVEL = 3


NVVIOCOMPSYNCTYPE = _NVVIOCOMPSYNCTYPE


# not Video input output status
class _NVVIOINPUTOUTPUTSTATUS(ENUM):
    NVINPUTOUTPUTSTATUS_OFF = 1
    NVINPUTOUTPUTSTATUS_ERROR = 2
    NVINPUTOUTPUTSTATUS_SDI_SD = 3
    NVINPUTOUTPUTSTATUS_SDI_HD = 4


NVVIOINPUTOUTPUTSTATUS = _NVVIOINPUTOUTPUTSTATUS


# not Synchronization input status
class _NVVIOSYNCSTATUS(ENUM):
    NVVIOSYNCSTATUS_OFF = 1
    NVVIOSYNCSTATUS_ERROR = 2
    NVVIOSYNCSTATUS_SYNCLOSS = 3
    NVVIOSYNCSTATUS_COMPOSITE = 4
    NVVIOSYNCSTATUS_SDI_SD = 5
    NVVIOSYNCSTATUS_SDI_HD = 6


NVVIOSYNCSTATUS = _NVVIOSYNCSTATUS


# not Video Capture Status
class _NVVIOCAPTURESTATUS(ENUM):
    NVVIOSTATUS_STOPPED = 1
    NVVIOSTATUS_RUNNING = 2
    NVVIOSTATUS_ERROR = 3


NVVIOCAPTURESTATUS = _NVVIOCAPTURESTATUS


# not Video Capture Status
class _NVVIOSTATUSTYPE(ENUM):
    NVVIOSTATUSTYPE_IN = 1
    NVVIOSTATUSTYPE_OUT = 2


NVVIOSTATUSTYPE = _NVVIOSTATUSTYPE

# not Assumption, maximum 4 SDI input and 4 SDI output cards supported on
# a system
NVAPI_MAX_VIO_DEVICES = 8

# not 4 physical jacks supported on each SDI input card.
NVAPI_MAX_VIO_JACKS = 4

# not Each physical jack an on SDI input card can have
# not two "channels" in the case of "3G" VideoFormats, as specified
# not by SMPTE 425; for non-3G VideoFormats, only the first channel within
# not a physical jack is valid.
NVAPI_MAX_VIO_CHANNELS_PER_JACK = 2

# not 4 Streams, 1 per physical jack
NVAPI_MAX_VIO_STREAMS = 4
NVAPI_MIN_VIO_STREAMS = 1

# not SDI input supports a max of 2 links per stream
NVAPI_MAX_VIO_LINKS_PER_STREAM = 2
NVAPI_MAX_FRAMELOCK_MAPPING_MODES = 20

# not Min number of capture images
NVAPI_GVI_MIN_RAW_CAPTURE_IMAGES = 1

# not Max number of capture images
NVAPI_GVI_MAX_RAW_CAPTURE_IMAGES = 32

# not Default number of capture images
NVAPI_GVI_DEFAULT_RAW_CAPTURE_IMAGES = 5


# Data Signal notification events. These need a event handler in RM.
# Register/Unregister and PopEvent NVAPI's are already available.
# not Device configuration
class _NVVIOCONFIGTYPE(ENUM):
    NVVIOCONFIGTYPE_IN = 1
    NVVIOCONFIGTYPE_OUT = 2


NVVIOCONFIGTYPE = _NVVIOCONFIGTYPE


class _NVVIOCOLORSPACE(ENUM):
    NVVIOCOLORSPACE_UNKNOWN = 1
    NVVIOCOLORSPACE_YCBCR = 2
    NVVIOCOLORSPACE_YCBCRA = 3
    NVVIOCOLORSPACE_YCBCRD = 4
    NVVIOCOLORSPACE_GBR = 5
    NVVIOCOLORSPACE_GBRA = 6
    NVVIOCOLORSPACE_GBRD = 7


NVVIOCOLORSPACE = _NVVIOCOLORSPACE


# not Component sampling
class _NVVIOCOMPONENTSAMPLING(ENUM):
    NVVIOCOMPONENTSAMPLING_UNKNOWN = 1
    NVVIOCOMPONENTSAMPLING_4444 = 2
    NVVIOCOMPONENTSAMPLING_4224 = 3
    NVVIOCOMPONENTSAMPLING_444 = 4
    NVVIOCOMPONENTSAMPLING_422 = 5


NVVIOCOMPONENTSAMPLING = _NVVIOCOMPONENTSAMPLING


class _NVVIOBITSPERCOMPONENT(ENUM):
    NVVIOBITSPERCOMPONENT_UNKNOWN = 1
    NVVIOBITSPERCOMPONENT_8 = 2
    NVVIOBITSPERCOMPONENT_10 = 3
    NVVIOBITSPERCOMPONENT_12 = 4


NVVIOBITSPERCOMPONENT = _NVVIOBITSPERCOMPONENT


class _NVVIOLINKID(ENUM):
    NVVIOLINKID_UNKNOWN = 1
    NVVIOLINKID_A = 2
    NVVIOLINKID_B = 3
    NVVIOLINKID_C = 4
    NVVIOLINKID_D = 5


NVVIOLINKID = _NVVIOLINKID


class _NVVIOANCPARITYCOMPUTATION(ENUM):
    NVVIOANCPARITYCOMPUTATION_AUTO = 1
    NVVIOANCPARITYCOMPUTATION_ON = 2
    NVVIOANCPARITYCOMPUTATION_OFF = 3


NVVIOANCPARITYCOMPUTATION = _NVVIOANCPARITYCOMPUTATION

# not @}
# ---------------------------------------------------------------------
# Structures
# ---------------------------------------------------------------------
# not \addtogroup vidio
# not @{
# not Supports Serial Digital Interface (SDI) output
NVVIOCAPS_VIDOUT_SDI = 0x00000001

# not Supports Internal timing source
NVVIOCAPS_SYNC_INTERNAL = 0x00000100

# not Supports Genlock timing source
NVVIOCAPS_SYNC_GENLOCK = 0x00000200

# not Supports Serial Digital Interface (SDI) synchronization input
NVVIOCAPS_SYNCSRC_SDI = 0x00001000

# not Supports Composite synchronization input
NVVIOCAPS_SYNCSRC_COMP = 0x00002000

# not Supports Desktop transparent mode
NVVIOCAPS_OUTPUTMODE_DESKTOP = 0x00010000

# not Supports OpenGL application mode
NVVIOCAPS_OUTPUTMODE_OPENGL = 0x00020000

# not Supports Serial Digital Interface (SDI) input
NVVIOCAPS_VIDIN_SDI = 0x00100000

# not Supports Packed ANC
NVVIOCAPS_PACKED_ANC_SUPPORTED = 0x00200000

# not Supports ANC audio blanking
NVVIOCAPS_AUDIO_BLANKING_SUPPORTED = 0x00400000

# not SDI-class interface: SDI output with two genlock inputs
NVVIOCLASS_SDI = 0x00000001


# not Device capabilities
class driver(ctypes.Structure):
    pass


driver._fields_ = [
    # not < Major version. For GVI, majorVersion contains
    # MajorVersion(HIWORD) And MinorVersion(LOWORD)
    ('majorVersion', NvU32),
    # not < Minor version. For GVI, minorVersion contains Revison(HIWORD)
    # And Build(LOWORD)
    ('minorVersion', NvU32),
]
_NVVIOCAPS.driver = driver


class firmWare(ctypes.Structure):
    pass


firmWare._fields_ = [
    # not < Major version. In version 2, for both GVI and GVO,
    # majorVersion contains MajorVersion(HIWORD) And MinorVersion(LOWORD)
    ('majorVersion', NvU32),
    # not < Minor version. In version 2, for both GVI and GVO,
    # minorVersion contains Revison(HIWORD) And Build(LOWORD)
    ('minorVersion', NvU32),
]
_NVVIOCAPS.firmWare = firmWare

_NVVIOCAPS._fields_ = [
    # not < Structure version
    ('version', NvU32),
    # not < Graphics adapter name
    ('adapterName', NvAPI_String),
    # not < Graphics adapter classes (NVVIOCLASS_SDI mask)
    ('adapterClass', NvU32),
    # not < Graphics adapter capabilities (NVVIOCAPS_* mask)
    ('adapterCaps', NvU32),
    # not < On-board DIP switch settings bits
    ('dipSwitch', NvU32),
    # not < On-board DIP switch settings reserved bits
    ('dipSwitchReserved', NvU32),
    # not < Board ID
    ('boardID', NvU32),
    # not Driver version
    ('driver', _NVVIOCAPS.driver),
    # not Firmware version
    ('firmWare', _NVVIOCAPS.firmWare),
    # not < Unique identifier for owner of video output
    # (NVVIOOWNERID_INVALID if free running)
    ('ownerId', NVVIOOWNERID),
    # not < Owner type (OpenGL application or Desktop mode)
    ('ownerType', NVVIOOWNERTYPE),
]

# not Macro for constructing the version field of NVVIOCAPS
NVVIOCAPS_VER1 = MAKE_NVAPI_VERSION(NVVIOCAPS, 1)
NVVIOCAPS_VER2 = MAKE_NVAPI_VERSION(NVVIOCAPS, 2)
NVVIOCAPS_VER = NVVIOCAPS_VER2

# not Input channel status
_NVVIOCHANNELSTATUS._fields_ = [
    # not < 4-byte SMPTE 352 video payload identifier
    ('smpte352', NvU32),
    # not < Signal format
    ('signalFormat', NVVIOSIGNALFORMAT),
    # not < Bits per component
    ('bitsPerComponent', NVVIOBITSPERCOMPONENT),
    # not < Sampling format
    ('samplingFormat', NVVIOCOMPONENTSAMPLING),
    # not < Color space
    ('colorSpace', NVVIOCOLORSPACE),
    # not < Link ID
    ('linkID', NVVIOLINKID),
]

# not Input device status
_NVVIOINPUTSTATUS._fields_ = [
    # not < Video input status per channel within a jack
    ('vidIn', (NVVIOCHANNELSTATUS * NVAPI_MAX_VIO_JACKS) * NVAPI_MAX_VIO_CHANNELS_PER_JACK),
    # not < status of video capture
    ('captureStatus', NVVIOCAPTURESTATUS),
]

# not Output device status
_NVVIOOUTPUTSTATUS._fields_ = [
    # not < Video 1 output status
    ('vid1Out', NVVIOINPUTOUTPUTSTATUS),
    # not < Video 2 output status
    ('vid2Out', NVVIOINPUTOUTPUTSTATUS),
    # not < SDI sync input status
    ('sdiSyncIn', NVVIOSYNCSTATUS),
    # not < Composite sync input status
    ('compSyncIn', NVVIOSYNCSTATUS),
    # not < Sync enable (TRUE if using syncSource)
    ('syncEnable', NvU32),
    # not < Sync source
    ('syncSource', NVVIOSYNCSOURCE),
    # not < Sync format
    ('syncFormat', NVVIOSIGNALFORMAT),
    # not < Framelock enable flag
    ('frameLockEnable', NvU32),
    # not < Output locked status
    ('outputVideoLocked', NvU32),
    # not < Data integrity check error count
    ('dataIntegrityCheckErrorCount', NvU32),
    # not < Data integrity check status enabled
    ('dataIntegrityCheckEnabled', NvU32),
    # not < Data integrity check status failed
    ('dataIntegrityCheckFailed', NvU32),
    # not < genlocked to framelocked to ref signal
    ('uSyncSourceLocked', NvU32),
    # not < TRUE: indicates there is sufficient power
    ('uPowerOn', NvU32),
]


# not Video device status.
class vioStatus(ctypes.Union):
    pass


vioStatus._fields_ = [
    # not < Input device status
    ('inStatus', NVVIOINPUTSTATUS),
    # not < Output device status
    ('outStatus', NVVIOOUTPUTSTATUS),
]
_NVVIOSTATUS.vioStatus = vioStatus

_NVVIOSTATUS._fields_ = [
    # not < Structure version
    ('version', NvU32),
    # not < Input or Output status
    ('nvvioStatusType', NVVIOSTATUSTYPE),
    ('vioStatus', _NVVIOSTATUS.vioStatus),
]

# not Macro for constructingthe version field of NVVIOSTATUS
NVVIOSTATUS_VER = MAKE_NVAPI_VERSION(NVVIOSTATUS, 1)

# not Output region
_NVVIOOUTPUTREGION._fields_ = [
    # not < Horizontal origin in pixels
    ('x', NvU32),
    # not < Vertical origin in pixels
    ('y', NvU32),
    # not < Width of region in pixels
    ('width', NvU32),
    # not < Height of region in pixels
    ('height', NvU32),
]

# not Gamma ramp (8-bit index)
_NVVIOGAMMARAMP8._fields_ = [
    # not < Red channel gamma ramp (8-bit index, 16-bit values)
    ('uRed', NvU16 * 256),
    # not < Green channel gamma ramp (8-bit index, 16-bit values)
    ('uGreen', NvU16 * 256),
    # not < Blue channel gamma ramp (8-bit index, 16-bit values)
    ('uBlue', NvU16 * 256),
]

# not Gamma ramp (10-bit index)
_NVVIOGAMMARAMP10._fields_ = [
    # not < Red channel gamma ramp (10-bit index, 16-bit values)
    ('uRed', NvU16 * 1024),
    # not < Green channel gamma ramp (10-bit index, 16-bit values)
    ('uGreen', NvU16 * 1024),
    # not < Blue channel gamma ramp (10-bit index, 16-bit values)
    ('uBlue', NvU16 * 1024),
]

# not Sync delay
_NVVIOSYNCDELAY._fields_ = [
    # not < Structure version
    ('version', NvU32),
    # not < Horizontal delay in pixels
    ('horizontalDelay', NvU32),
    # not < Vertical delay in lines
    ('verticalDelay', NvU32),
]

# not Macro for constructing the version field of NVVIOSYNCDELAY
NVVIOSYNCDELAY_VER = MAKE_NVAPI_VERSION(NVVIOSYNCDELAY, 1)

# not Video mode information
_NVVIOVIDEOMODE._fields_ = [
    # not < Horizontal resolution (in pixels)
    ('horizontalPixels', NvU32),
    # not < Vertical resolution for frame (in lines)
    ('verticalLines', NvU32),
    # not < Frame rate
    ('fFrameRate', FLOAT),
    # not < Interlace mode
    ('interlaceMode', NVVIOINTERLACEMODE),
    # not < SMPTE standards format
    ('videoStandard', NVVIOVIDEOSTANDARD),
    # not < HD or SD signal classification
    ('videoType', NVVIOVIDEOTYPE),
]

# not Signal format details
_NVVIOSIGNALFORMATDETAIL._fields_ = [
    # not < Signal format enumerated value
    ('signalFormat', NVVIOSIGNALFORMAT),
    # not < Video mode for signal format
    ('videoMode', NVVIOVIDEOMODE),
]

# not R8:G8:B8
NVVIOBUFFERFORMAT_R8G8B8 = 0x00000001

# not R8:G8:B8:Z24
NVVIOBUFFERFORMAT_R8G8B8Z24 = 0x00000002

# not R8:G8:B8:A8
NVVIOBUFFERFORMAT_R8G8B8A8 = 0x00000004

# not R8:G8:B8:A8:Z24
NVVIOBUFFERFORMAT_R8G8B8A8Z24 = 0x00000008

# not R16FP:G16FP:B16FP
NVVIOBUFFERFORMAT_R16FPG16FPB16FP = 0x00000010

# not R16FP:G16FP:B16FP:Z24
NVVIOBUFFERFORMAT_R16FPG16FPB16FPZ24 = 0x00000020

# not R16FP:G16FP:B16FP:A16FP
NVVIOBUFFERFORMAT_R16FPG16FPB16FPA16FP = 0x00000040

# not R16FP:G16FP:B16FP:A16FP:Z24
NVVIOBUFFERFORMAT_R16FPG16FPB16FPA16FPZ24 = 0x00000080

# not Data format details
_NVVIODATAFORMATDETAIL._fields_ = [
    # not < Data format enumerated value
    ('dataFormat', NVVIODATAFORMAT),
    # not < Data format capabilities (NVVIOCAPS_* mask)
    ('vioCaps', NvU32),
]

# not Colorspace conversion
_NVVIOCOLORCONVERSION._fields_ = [
    # not < Structure version
    ('version', NvU32),
    # not < Output[n] =
    ('colorMatrix', (FLOAT * 3) * 3),
    # not < Input[0] * colorMatrix[n][0] +
    ('colorOffset', FLOAT * 3),
    # not < Input[1] * colorMatrix[n][1] +
    ('colorScale', FLOAT * 3),
    # not < compositeSafe constrains luminance range when using composite
    # output
    ('compositeSafe', NvU32),
]

# not macro for constructing the version field of _NVVIOCOLORCONVERSION.
NVVIOCOLORCONVERSION_VER = MAKE_NVAPI_VERSION(NVVIOCOLORCONVERSION, 1)


# not Gamma correction
class gammaRamp(ctypes.Union):
    pass


gammaRamp._fields_ = [
    # not < Gamma ramp (8-bit index, 16-bit values)
    ('gammaRamp8', NVVIOGAMMARAMP8),
    # not < Gamma ramp (10-bit index, 16-bit values)
    ('gammaRamp10', NVVIOGAMMARAMP10),
]
_NVVIOGAMMACORRECTION.gammaRamp = gammaRamp

_NVVIOGAMMACORRECTION._fields_ = [
    # not < Structure version
    ('version', NvU32),
    # not < Gamma correction type (8-bit or 10-bit)
    ('vioGammaCorrectionType', NvU32),
    # not Gamma correction:
    ('gammaRamp', _NVVIOGAMMACORRECTION.gammaRamp),
    # not < Red Gamma value within gamma ranges. 0.5 - 6.0
    ('fGammaValueR', FLOAT),
    # not < Green Gamma value within gamma ranges. 0.5 - 6.0
    ('fGammaValueG', FLOAT),
    # not < Blue Gamma value within gamma ranges. 0.5 - 6.0
    ('fGammaValueB', FLOAT),
]

# not Macro for constructing thevesion field of _NVVIOGAMMACORRECTION
NVVIOGAMMACORRECTION_VER = MAKE_NVAPI_VERSION(NVVIOGAMMACORRECTION, 1)

# not Maximum number of ranges per channel
MAX_NUM_COMPOSITE_RANGE = 2

_NVVIOCOMPOSITERANGE._fields_ = [
    ('uRange', NvU32),
    ('uEnabled', NvU32),
    ('uMin', NvU32),
    ('uMax', NvU32),
]

# Device configuration
# (fields masks indicating NVVIOCONFIG fields to use for NvAPI_VIO_GetConfig/NvAPI_VIO_SetConfig() )
#
# not < fields: signalFormat
NVVIOCONFIG_SIGNALFORMAT = 0x00000001

# not < fields: dataFormat
NVVIOCONFIG_DATAFORMAT = 0x00000002

# not < fields: outputRegion
NVVIOCONFIG_OUTPUTREGION = 0x00000004

# not < fields: outputArea
NVVIOCONFIG_OUTPUTAREA = 0x00000008

# not < fields: colorConversion
NVVIOCONFIG_COLORCONVERSION = 0x00000010

# not < fields: gammaCorrection
NVVIOCONFIG_GAMMACORRECTION = 0x00000020

# not < fields: syncSource and syncEnable
NVVIOCONFIG_SYNCSOURCEENABLE = 0x00000040

# not < fields: syncDelay
NVVIOCONFIG_SYNCDELAY = 0x00000080

# not < fields: compositeSyncType
NVVIOCONFIG_COMPOSITESYNCTYPE = 0x00000100

# not < fields: EnableFramelock
NVVIOCONFIG_FRAMELOCKENABLE = 0x00000200

# not < fields: bEnable422Filter
NVVIOCONFIG_422FILTER = 0x00000400

# not < fields: bCompositeTerminate (Not supported on Quadro FX 4000 SDI)
NVVIOCONFIG_COMPOSITETERMINATE = 0x00000800

# not < fields: bEnableDataIntegrityCheck
# (Not supported on Quadro FX 4000 SDI)
NVVIOCONFIG_DATAINTEGRITYCHECK = 0x00001000

# not < fields: colorConversion override
NVVIOCONFIG_CSCOVERRIDE = 0x00002000

# not < fields: flipqueuelength control
NVVIOCONFIG_FLIPQUEUELENGTH = 0x00004000

# not < fields: bEnableANCTimeCodeGeneration
NVVIOCONFIG_ANCTIMECODEGENERATION = 0x00008000

# not < fields: bEnableComposite
NVVIOCONFIG_COMPOSITE = 0x00010000

# not < fields: bEnableAlphaKeyComposite
NVVIOCONFIG_ALPHAKEYCOMPOSITE = 0x00020000

# not < fields: compRange
NVVIOCONFIG_COMPOSITE_Y = 0x00040000

# not < fields: compRange
NVVIOCONFIG_COMPOSITE_CR = 0x00080000

# not < fields: compRange
NVVIOCONFIG_COMPOSITE_CB = 0x00100000

# not < fields: bEnableFullColorRange
NVVIOCONFIG_FULL_COLOR_RANGE = 0x00200000

# not < fields: bEnableRGBData
NVVIOCONFIG_RGB_DATA = 0x00400000

# not < fields: bEnableSDIOutput
NVVIOCONFIG_RESERVED_SDIOUTPUTENABLE = 0x00800000

# not < fields: streams
NVVIOCONFIG_STREAMS = 0x01000000

# not < fields: ancParityComputation
NVVIOCONFIG_ANC_PARITY_COMPUTATION = 0x02000000

# not < fields: enableAudioBlanking
NVVIOCONFIG_ANC_AUDIO_REPEAT = 0x04000000

# Don't forget to update NVVIOCONFIG_VALIDFIELDS in nvapi.spec when
# NVVIOCONFIG_ALLFIELDS changes.
NVVIOCONFIG_ALLFIELDS = (
        NVVIOCONFIG_SIGNALFORMAT |
        NVVIOCONFIG_DATAFORMAT |
        NVVIOCONFIG_OUTPUTREGION |
        NVVIOCONFIG_OUTPUTAREA |
        NVVIOCONFIG_COLORCONVERSION |
        NVVIOCONFIG_GAMMACORRECTION |
        NVVIOCONFIG_SYNCSOURCEENABLE |
        NVVIOCONFIG_SYNCDELAY |
        NVVIOCONFIG_COMPOSITESYNCTYPE |
        NVVIOCONFIG_FRAMELOCKENABLE |
        NVVIOCONFIG_422FILTER |
        NVVIOCONFIG_COMPOSITETERMINATE |
        NVVIOCONFIG_DATAINTEGRITYCHECK |
        NVVIOCONFIG_CSCOVERRIDE |
        NVVIOCONFIG_FLIPQUEUELENGTH |
        NVVIOCONFIG_ANCTIMECODEGENERATION |
        NVVIOCONFIG_COMPOSITE |
        NVVIOCONFIG_ALPHAKEYCOMPOSITE |
        NVVIOCONFIG_COMPOSITE_Y |
        NVVIOCONFIG_COMPOSITE_CR |
        NVVIOCONFIG_COMPOSITE_CB |
        NVVIOCONFIG_FULL_COLOR_RANGE |
        NVVIOCONFIG_RGB_DATA |
        NVVIOCONFIG_RESERVED_SDIOUTPUTENABLE |
        NVVIOCONFIG_STREAMS |
        NVVIOCONFIG_ANC_PARITY_COMPUTATION |
        NVVIOCONFIG_ANC_AUDIO_REPEAT
)
NVVIOCONFIG_VALIDFIELDS = (
        NVVIOCONFIG_SIGNALFORMAT |
        NVVIOCONFIG_DATAFORMAT |
        NVVIOCONFIG_OUTPUTREGION |
        NVVIOCONFIG_OUTPUTAREA |
        NVVIOCONFIG_COLORCONVERSION |
        NVVIOCONFIG_GAMMACORRECTION |
        NVVIOCONFIG_SYNCSOURCEENABLE |
        NVVIOCONFIG_SYNCDELAY |
        NVVIOCONFIG_COMPOSITESYNCTYPE |
        NVVIOCONFIG_FRAMELOCKENABLE |
        NVVIOCONFIG_RESERVED_SDIOUTPUTENABLE |
        NVVIOCONFIG_422FILTER |
        NVVIOCONFIG_COMPOSITETERMINATE |
        NVVIOCONFIG_DATAINTEGRITYCHECK |
        NVVIOCONFIG_CSCOVERRIDE |
        NVVIOCONFIG_FLIPQUEUELENGTH |
        NVVIOCONFIG_ANCTIMECODEGENERATION |
        NVVIOCONFIG_COMPOSITE |
        NVVIOCONFIG_ALPHAKEYCOMPOSITE |
        NVVIOCONFIG_COMPOSITE_Y |
        NVVIOCONFIG_COMPOSITE_CR |
        NVVIOCONFIG_COMPOSITE_CB |
        NVVIOCONFIG_FULL_COLOR_RANGE |
        NVVIOCONFIG_RGB_DATA |
        NVVIOCONFIG_RESERVED_SDIOUTPUTENABLE |
        NVVIOCONFIG_STREAMS |
        NVVIOCONFIG_ANC_PARITY_COMPUTATION |
        NVVIOCONFIG_ANC_AUDIO_REPEAT
)
NVVIOCONFIG_DRIVERFIELDS = (
        NVVIOCONFIG_OUTPUTREGION |
        NVVIOCONFIG_OUTPUTAREA |
        NVVIOCONFIG_COLORCONVERSION |
        NVVIOCONFIG_FLIPQUEUELENGTH
)
NVVIOCONFIG_GAMMAFIELDS = NVVIOCONFIG_GAMMACORRECTION
NVVIOCONFIG_RMCTRLFIELDS = (
        NVVIOCONFIG_SIGNALFORMAT |
        NVVIOCONFIG_DATAFORMAT |
        NVVIOCONFIG_SYNCSOURCEENABLE |
        NVVIOCONFIG_COMPOSITESYNCTYPE |
        NVVIOCONFIG_FRAMELOCKENABLE |
        NVVIOCONFIG_422FILTER |
        NVVIOCONFIG_COMPOSITETERMINATE |
        NVVIOCONFIG_DATAINTEGRITYCHECK |
        NVVIOCONFIG_COMPOSITE |
        NVVIOCONFIG_ALPHAKEYCOMPOSITE |
        NVVIOCONFIG_COMPOSITE_Y |
        NVVIOCONFIG_COMPOSITE_CR |
        NVVIOCONFIG_COMPOSITE_CB
)
NVVIOCONFIG_RMSKEWFIELDS = NVVIOCONFIG_SYNCDELAY
NVVIOCONFIG_ALLOWSDIRUNNING_FIELDS = (
        NVVIOCONFIG_DATAINTEGRITYCHECK |
        NVVIOCONFIG_SYNCDELAY |
        NVVIOCONFIG_CSCOVERRIDE |
        NVVIOCONFIG_ANCTIMECODEGENERATION |
        NVVIOCONFIG_COMPOSITE |
        NVVIOCONFIG_ALPHAKEYCOMPOSITE |
        NVVIOCONFIG_COMPOSITE_Y |
        NVVIOCONFIG_COMPOSITE_CR |
        NVVIOCONFIG_COMPOSITE_CB |
        NVVIOCONFIG_ANC_PARITY_COMPUTATION
)
NVVIOCONFIG_RMMODESET_FIELDS = (
        NVVIOCONFIG_SIGNALFORMAT |
        NVVIOCONFIG_DATAFORMAT |
        NVVIOCONFIG_SYNCSOURCEENABLE |
        NVVIOCONFIG_FRAMELOCKENABLE |
        NVVIOCONFIG_COMPOSITESYNCTYPE |
        NVVIOCONFIG_ANC_AUDIO_REPEAT
)

# not Output device configuration
# No members can be deleted from below structure. Only add new members at
# the
# end of the structure.
_NVVIOOUTPUTCONFIG_V1._fields_ = [
    # not < Signal format for video output
    ('signalFormat', NVVIOSIGNALFORMAT),
    # not < Data format for video output
    ('dataFormat', NVVIODATAFORMAT),
    # not < Region for video output (Desktop mode)
    ('outputRegion', NVVIOOUTPUTREGION),
    # not < Usable resolution for video output (safe area)
    ('outputArea', NVVIOOUTPUTAREA),
    # not < Color conversion.
    ('colorConversion', NVVIOCOLORCONVERSION),
    ('gammaCorrection', NVVIOGAMMACORRECTION),
    # not < Sync enable (TRUE to use syncSource)
    ('syncEnable', NvU32),
    # not < Sync source
    ('syncSource', NVVIOSYNCSOURCE),
    # not < Sync delay
    ('syncDelay', NVVIOSYNCDELAY),
    # not < Composite sync type
    ('compositeSyncType', NVVIOCOMPSYNCTYPE),
    # not < Flag indicating whether framelock was on/off
    ('frameLockEnable', NvU32),
    # not < Indicates whether contained format is PSF Signal format
    ('psfSignalFormat', NvU32),
    # not < Enables/Disables 4:2:2 filter
    ('enable422Filter', NvU32),
    # not < Composite termination
    ('compositeTerminate', NvU32),
    # not < Enable data integrity check: true - enable, false - disable
    ('enableDataIntegrityCheck', NvU32),
    # not < Use provided CSC color matrix to overwrite
    ('cscOverride', NvU32),
    # not < Number of buffers used for the internal flipqueue
    ('flipQueueLength', NvU32),
    # not < Enable SDI ANC time code generation
    ('enableANCTimeCodeGeneration', NvU32),
    # not < Enable composite
    ('enableComposite', NvU32),
    # not < Enable Alpha key composite
    ('enableAlphaKeyComposite', NvU32),
    # not < Composite ranges
    ('compRange', NVVIOCOMPOSITERANGE),
    # not < Inicates last stored SDI output state TRUE-ON / FALSE-OFF
    ('reservedData', NvU8 * 256),
    # not < Flag indicating Full Color Range
    ('enableFullColorRange', NvU32),
    # not < Indicates data is in RGB format
    ('enableRGBData', NvU32),
]

_NVVIOOUTPUTCONFIG_V2._fields_ = [
    # not < Signal format for video output
    ('signalFormat', NVVIOSIGNALFORMAT),
    # not < Data format for video output
    ('dataFormat', NVVIODATAFORMAT),
    # not < Region for video output (Desktop mode)
    ('outputRegion', NVVIOOUTPUTREGION),
    # not < Usable resolution for video output (safe area)
    ('outputArea', NVVIOOUTPUTAREA),
    # not < Color conversion.
    ('colorConversion', NVVIOCOLORCONVERSION),
    ('gammaCorrection', NVVIOGAMMACORRECTION),
    # not < Sync enable (TRUE to use syncSource)
    ('syncEnable', NvU32),
    # not < Sync source
    ('syncSource', NVVIOSYNCSOURCE),
    # not < Sync delay
    ('syncDelay', NVVIOSYNCDELAY),
    # not < Composite sync type
    ('compositeSyncType', NVVIOCOMPSYNCTYPE),
    # not < Flag indicating whether framelock was on/off
    ('frameLockEnable', NvU32),
    # not < Indicates whether contained format is PSF Signal format
    ('psfSignalFormat', NvU32),
    # not < Enables/Disables 4:2:2 filter
    ('enable422Filter', NvU32),
    # not < Composite termination
    ('compositeTerminate', NvU32),
    # not < Enable data integrity check: true - enable, false - disable
    ('enableDataIntegrityCheck', NvU32),
    # not < Use provided CSC color matrix to overwrite
    ('cscOverride', NvU32),
    # not < Number of buffers used for the internal flip queue
    ('flipQueueLength', NvU32),
    # not < Enable SDI ANC time code generation
    ('enableANCTimeCodeGeneration', NvU32),
    # not < Enable composite
    ('enableComposite', NvU32),
    # not < Enable Alpha key composite
    ('enableAlphaKeyComposite', NvU32),
    # not < Composite ranges
    ('compRange', NVVIOCOMPOSITERANGE),
    # not < Indicates last stored SDI output state TRUE-ON / FALSE-OFF
    ('reservedData', NvU8 * 256),
    # not < Flag indicating Full Color Range
    ('enableFullColorRange', NvU32),
    # not < Indicates data is in RGB format
    ('enableRGBData', NvU32),
    # not < Enable HW ANC parity bit computation (auto/on/off)
    ('ancParityComputation', NVVIOANCPARITYCOMPUTATION),
]

_NVVIOOUTPUTCONFIG_V3._fields_ = [
    # not < Signal format for video output
    ('signalFormat', NVVIOSIGNALFORMAT),
    # not < Data format for video output
    ('dataFormat', NVVIODATAFORMAT),
    # not < Region for video output (Desktop mode)
    ('outputRegion', NVVIOOUTPUTREGION),
    # not < Usable resolution for video output (safe area)
    ('outputArea', NVVIOOUTPUTAREA),
    # not < Color conversion.
    ('colorConversion', NVVIOCOLORCONVERSION),
    ('gammaCorrection', NVVIOGAMMACORRECTION),
    # not < Sync enable (TRUE to use syncSource)
    ('syncEnable', NvU32),
    # not < Sync source
    ('syncSource', NVVIOSYNCSOURCE),
    # not < Sync delay
    ('syncDelay', NVVIOSYNCDELAY),
    # not < Composite sync type
    ('compositeSyncType', NVVIOCOMPSYNCTYPE),
    # not < Flag indicating whether framelock was on/off
    ('frameLockEnable', NvU32),
    # not < Indicates whether contained format is PSF Signal format
    ('psfSignalFormat', NvU32),
    # not < Enables/Disables 4:2:2 filter
    ('enable422Filter', NvU32),
    # not < Composite termination
    ('compositeTerminate', NvU32),
    # not < Enable data integrity check: true - enable, false - disable
    ('enableDataIntegrityCheck', NvU32),
    # not < Use provided CSC color matrix to overwrite
    ('cscOverride', NvU32),
    # not < Number of buffers used for the internal flip queue
    ('flipQueueLength', NvU32),
    # not < Enable SDI ANC time code generation
    ('enableANCTimeCodeGeneration', NvU32),
    # not < Enable composite
    ('enableComposite', NvU32),
    # not < Enable Alpha key composite
    ('enableAlphaKeyComposite', NvU32),
    # not < Composite ranges
    ('compRange', NVVIOCOMPOSITERANGE),
    # not < Indicates last stored SDI output state TRUE-ON / FALSE-OFF
    ('reservedData', NvU8 * 256),
    # not < Flag indicating Full Color Range
    ('enableFullColorRange', NvU32),
    # not < Indicates data is in RGB format
    ('enableRGBData', NvU32),
    # not < Enable HW ANC parity bit computation (auto/on/off)
    ('ancParityComputation', NVVIOANCPARITYCOMPUTATION),
    # not < Enable HANC audio blanking on repeat frames
    ('enableAudioBlanking', NvU32),
]


# not Stream configuration
class links(ctypes.Structure):
    pass


links._fields_ = [
    # not < This stream's link[i] will use the specified (0-based) channel
    # within the
    ('jack', NvU32),
    # not < specified (0-based) jack
    ('channel', NvU32),
]
_NVVIOSTREAM.links = links

_NVVIOSTREAM._fields_ = [
    # not < Bits per component
    ('bitsPerComponent', NvU32),
    # not < Sampling
    ('sampling', NVVIOCOMPONENTSAMPLING),
    # not < Enable/disable 4:2:2.4:4:4 expansion
    ('expansionEnable', NvU32),
    # not < Number of active links
    ('numLinks', NvU32),
    ('links', _NVVIOSTREAM.links * NVAPI_MAX_VIO_LINKS_PER_STREAM),
]

# not Input device configuration
_NVVIOINPUTCONFIG._fields_ = [
    # not < numRawCaptureImages is the number of frames to keep in the
    # capture queue.
    ('numRawCaptureImages', NvU32),
    # not < Signal format.
    ('signalFormat', NVVIOSIGNALFORMAT),
    # not < Number of active streams.
    ('numStreams', NvU32),
    # not < Stream configurations
    ('streams', NVVIOSTREAM * NVAPI_MAX_VIO_STREAMS),
    # not < This attribute controls the GVI test mode.
    ('bTestMode', NvU32),
]


class vioConfig(ctypes.Union):
    pass


vioConfig._fields_ = [
    # not < Input device configuration
    ('inConfig', NVVIOINPUTCONFIG),
    # not < Output device configuration
    ('outConfig', NVVIOOUTPUTCONFIG_V1),
]
_NVVIOCONFIG_V1.vioConfig = vioConfig

_NVVIOCONFIG_V1._fields_ = [
    # not < Structure version
    ('version', NvU32),
    # not < Caller sets to NVVIOCONFIG_* mask for fields to use
    ('fields', NvU32),
    # not < Input or Output configuration
    ('nvvioConfigType', NVVIOCONFIGTYPE),
    ('vioConfig', _NVVIOCONFIG_V1.vioConfig),
]


class vioConfig(ctypes.Union):
    pass


vioConfig._fields_ = [
    # not < Input device configuration
    ('inConfig', NVVIOINPUTCONFIG),
    # not < Output device configuration
    ('outConfig', NVVIOOUTPUTCONFIG_V2),
]
_NVVIOCONFIG_V2.vioConfig = vioConfig

_NVVIOCONFIG_V2._fields_ = [
    # not < Structure version
    ('version', NvU32),
    # not < Caller sets to NVVIOCONFIG_* mask for fields to use
    ('fields', NvU32),
    # not < Input or Output configuration
    ('nvvioConfigType', NVVIOCONFIGTYPE),
    ('vioConfig', _NVVIOCONFIG_V2.vioConfig),
]


class vioConfig(ctypes.Union):
    pass


vioConfig._fields_ = [
    # not < Input device configuration
    ('inConfig', NVVIOINPUTCONFIG),
    # not < Output device configuration
    ('outConfig', NVVIOOUTPUTCONFIG_V3),
]
_NVVIOCONFIG_V3.vioConfig = vioConfig

_NVVIOCONFIG_V3._fields_ = [
    # not < Structure version
    ('version', NvU32),
    # not < Caller sets to NVVIOCONFIG_* mask for fields to use
    ('fields', NvU32),
    # not < Input or Output configuration
    ('nvvioConfigType', NVVIOCONFIGTYPE),
    ('vioConfig', _NVVIOCONFIG_V3.vioConfig),
]
NVVIOOUTPUTCONFIG = NVVIOOUTPUTCONFIG_V3
NVVIOCONFIG = NVVIOCONFIG_V3
NVVIOCONFIG_VER1 = MAKE_NVAPI_VERSION(NVVIOCONFIG_V1, 1)
NVVIOCONFIG_VER2 = MAKE_NVAPI_VERSION(NVVIOCONFIG_V2, 2)
NVVIOCONFIG_VER3 = MAKE_NVAPI_VERSION(NVVIOCONFIG_V3, 3)
NVVIOCONFIG_VER = NVVIOCONFIG_VER3

NVVIOTOPOLOGYTARGET._fields_ = [
    # not < Handle to Physical GPU
    # (This could be NULL for GVI device if its not binded)
    ('hPhysicalGpu', NvPhysicalGpuHandle),
    # not < handle to SDI Input/Output device
    ('hVioHandle', NvVioHandle),
    # not < device Id of SDI Input/Output device
    ('vioId', NvU32),
    # not < deviceMask of the SDI display connected to GVO device.
    ('outputId', NvU32),
]

_NV_VIO_TOPOLOGY._fields_ = [
    ('version', NvU32),
    # not < How many video I/O targets are valid
    ('vioTotalDeviceCount', NvU32),
    # not < Array of video I/O targets
    ('vioTarget', NVVIOTOPOLOGYTARGET * NVAPI_MAX_VIO_DEVICES),
]

# not Macro for constructing the version field of NV_VIO_TOPOLOGY
NV_VIO_TOPOLOGY_VER = MAKE_NVAPI_VERSION(NV_VIO_TOPOLOGY, 1)

# not Macro for constructing the version field of NVVIOTOPOLOGY
NVVIOTOPOLOGY_VER = MAKE_NVAPI_VERSION(NVVIOTOPOLOGY, 1)

# not @}
# not \addtogroup vidio
# not @{
# ///////////////////////////////////////////////////////////////////////
# not
# not Function: NvAPI_VIO_GetCapabilities
# not
# not Description: This API determine the graphics adapter video I/O
# capabilities.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 396. Instead, use NvAPI_D3D_QuerySMPAssistSupport.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [in] NvVioHandle The caller provides the SDI device handle as
# input.
# not \param [out] pAdapterCaps Pointer to receive capabilities
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# ///////////////////////////////////////////////////////////////////////
NvAPI_VIO_GetCapabilities = hDll.VIO_GetCapabilities
NvAPI_VIO_GetCapabilities.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_VIO_GetCapabilities(NvVioHandle     hVioHandle,
#                                           NVVIOCAPS       *pAdapterCaps);

# ////////////////////////////////////////////////////////////////////////
# not Function: NvAPI_VIO_Open
# not
# not Description: This API opens the graphics adapter for video I/O
# operations
# not    using the OpenGL application interface. Read operations
# not    are permitted in this mode by multiple clients, but Write
# not    operations are application exclusive.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 396. Instead, use NvAPI_D3D_QuerySMPAssistSupport.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [in] NvVioHandle The caller provides the SDI output device
# handle as input.
# not \param [in] vioClass  Class interface (NVVIOCLASS_* value)
# not \param [in] ownerType  Specify NVVIOOWNERTYPE_APPLICATION or
# NVVIOOWNERTYPE_DESKTOP.
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# ///////////////////////////////////////////////////////////////////////
NvAPI_VIO_Open = hDll.VIO_Open
NvAPI_VIO_Open.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_VIO_Open(NvVioHandle       hVioHandle,
#                                NvU32             vioClass,
#                                NVVIOOWNERTYPE    ownerType);

# ///////////////////////////////////////////////////////////////////////
# not Function: NvAPI_VIO_Close
# not
# not Description: This API closes the graphics adapter for
# graphics-to-video operations
# not    using the OpenGL application interface. Closing an
# not    OpenGL handle releases the device.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 396. Instead, use NvAPI_D3D_QuerySMPAssistSupport.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [in] NvVioHandle The caller provides the SDI output device
# handle as input.
# not \param [in] bRelease BOOLEAN value to either keep or release
# ownership
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# ///////////////////////////////////////////////////////////////////////
NvAPI_VIO_Close = hDll.VIO_Close
NvAPI_VIO_Close.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_VIO_Close(NvVioHandle       hVioHandle,
#                                 NvU32             bRelease);
# ///////////////////////////////////////////////////////////////////////
# not Function: NvAPI_VIO_Status
# not
# not Description: This API gets the Video I/O LED status.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 396. Instead, use NvAPI_D3D_QuerySMPAssistSupport.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [in] NvVioHandle The caller provides the SDI device handle as
# input.
# not \param [out] pStatus  Return pointer to NVVIOSTATUS
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# ///////////////////////////////////////////////////////////////////////
NvAPI_VIO_Status = hDll.VIO_Status
NvAPI_VIO_Status.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_VIO_Status(NvVioHandle     hVioHandle,
#                                  NVVIOSTATUS     *pStatus);

# ////////////////////////////////////////////////////////////////////////
# not Function: NvAPI_VIO_SyncFormatDetect
# not
# not Description: This API detects the Video I/O incoming sync video
# format.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 396. Instead, use NvAPI_D3D_QuerySMPAssistSupport.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [in] NvVioHandle The caller provides the SDI device handle as
# input.
# not \param [out] pWait  Pointer to receive how many milliseconds will
# lapse
# not     before VIOStatus returns the detected syncFormat.
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# ///////////////////////////////////////////////////////////////////////
NvAPI_VIO_SyncFormatDetect = hDll.VIO_SyncFormatDetect
NvAPI_VIO_SyncFormatDetect.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_VIO_SyncFormatDetect(NvVioHandle hVioHandle,
#                                            NvU32       *pWait);

# ///////////////////////////////////////////////////////////////////////
# not Function: NvAPI_VIO_GetConfig
# not
# not Description: This API gets the graphics-to-video configuration.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 396. Instead, use NvAPI_D3D_QuerySMPAssistSupport.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [in] NvVioHandle The caller provides the SDI device handle as
# input.
# not \param [out] pConfig  Pointer to the graphics-to-video configuration
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# ///////////////////////////////////////////////////////////////////////
NvAPI_VIO_GetConfig = hDll.VIO_GetConfig
NvAPI_VIO_GetConfig.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_VIO_GetConfig(NvVioHandle        hVioHandle,
#                                     NVVIOCONFIG        *pConfig);

# ///////////////////////////////////////////////////////////////////////
# not Function: NvAPI_VIO_SetConfig
# not
# not Description: This API sets the graphics-to-video configuration.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 396. Instead, use NvAPI_D3D_QuerySMPAssistSupport.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [in] NvVioHandle The caller provides the SDI device handle as
# input.
# not \param [in] pConfig  Pointer to Graphics-to-Video configuration
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# ///////////////////////////////////////////////////////////////////////
NvAPI_VIO_SetConfig = hDll.VIO_SetConfig
NvAPI_VIO_SetConfig.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_VIO_SetConfig(NvVioHandle            hVioHandle,
#                                     const NVVIOCONFIG      *pConfig);

# ///////////////////////////////////////////////////////////////////////
# not Function: NvAPI_VIO_SetCSC
# not
# not Description: This API sets the colorspace conversion parameters.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_VIO_SetConfig.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [in] NvVioHandle The caller provides the SDI device handle as
# input.
# not \param [in] pCSC   Pointer to CSC parameters
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# //////////////////////////////////////////////////////////////////////////////----
NvAPI_VIO_SetCSC = hDll.VIO_SetCSC
NvAPI_VIO_SetCSC.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_VIO_SetCSC(NvVioHandle           hVioHandle,
#                                   NVVIOCOLORCONVERSION  *pCSC);
# ////////////////////////////////////////////////////////////////////////
# not Function: NvAPI_VIO_GetCSC
# not
# not Description: This API gets the colorspace conversion parameters.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_VIO_GetConfig.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [in] NvVioHandle The caller provides the SDI device handle as
# input.
# not \param [out] pCSC   Pointer to CSC parameters
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# ////////////////////////////////////////////////////////////////////////
NvAPI_VIO_GetCSC = hDll.VIO_GetCSC
NvAPI_VIO_GetCSC.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_VIO_GetCSC(NvVioHandle           hVioHandle,
#                                  NVVIOCOLORCONVERSION  *pCSC);

# ///////////////////////////////////////////////////////////////////////
# not Function: NvAPI_VIO_SetGamma
# not
# not Description: This API sets the gamma conversion parameters.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_VIO_SetConfig.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [in] NvVioHandle  The caller provides the SDI device handle
# as input.
# not \param [in] pGamma  Pointer to gamma parameters
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# ///////////////////////////////////////////////////////////////////////
NvAPI_VIO_SetGamma = hDll.VIO_SetGamma
NvAPI_VIO_SetGamma.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_VIO_SetGamma(NvVioHandle           hVioHandle,
#                                    NVVIOGAMMACORRECTION  *pGamma);


# ///////////////////////////////////////////////////////////////////////
# not Function: NvAPI_VIO_GetGamma
# not
# not Description: This API gets the gamma conversion parameters.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_VIO_GetConfig.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [in] NvVioHandle The caller provides the SDI device handle as
# input.
# not \param [out] pGamma   Pointer to gamma parameters
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# ///////////////////////////////////////////////////////////////////////
NvAPI_VIO_GetGamma = hDll.VIO_GetGamma
NvAPI_VIO_GetGamma.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_VIO_GetGamma(NvVioHandle           hVioHandle,
#                                    NVVIOGAMMACORRECTION* pGamma);

# ////////////////////////////////////////////////////////////////////////
# not Function: NvAPI_VIO_SetSyncDelay
# not
# not Description: This API sets the sync delay parameters.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_VIO_SetConfig.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [in] NvVioHandle The caller provides the SDI device handle as
# input.
# not \param [in] pSyncDelay Pointer to sync delay parameters
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# ///////////////////////////////////////////////////////////////////////
NvAPI_VIO_SetSyncDelay = hDll.VIO_SetSyncDelay
NvAPI_VIO_SetSyncDelay.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_VIO_SetSyncDelay(NvVioHandle            hVioHandle,
#                                        const NVVIOSYNCDELAY   *pSyncDelay);

# ////////////////////////////////////////////////////////////////////////
# not Function: NvAPI_VIO_GetSyncDelay
# not
# not Description: This API gets the sync delay parameters.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_VIO_GetConfig.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [in] NvVioHandle The caller provides the SDI device handle as
# input.
# not \param [out] pSyncDelay  Pointer to sync delay parameters
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# ///////////////////////////////////////////////////////////////////////
NvAPI_VIO_GetSyncDelay = hDll.VIO_GetSyncDelay
NvAPI_VIO_GetSyncDelay.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_VIO_GetSyncDelay(NvVioHandle      hVioHandle,
#                                        NVVIOSYNCDELAY   *pSyncDelay);

class _NVVIOPCILINKRATE(ENUM):
    NVVIOPCILINKRATE_UNKNOWN = 0
    NVVIOPCILINKRATE_GEN1 = 1
    NVVIOPCILINKRATE_GEN2 = 2
    NVVIOPCILINKRATE_GEN3 = 3


NVVIOPCILINKRATE = _NVVIOPCILINKRATE


class _NVVIOPCILINKWIDTH(ENUM):
    NVVIOPCILINKWIDTH_UNKNOWN = 0
    NVVIOPCILINKWIDTH_x1 = 1
    NVVIOPCILINKWIDTH_x2 = 2
    NVVIOPCILINKWIDTH_x4 = 4
    NVVIOPCILINKWIDTH_x8 = 8
    NVVIOPCILINKWIDTH_x16 = 16


NVVIOPCILINKWIDTH = _NVVIOPCILINKWIDTH

_NVVIOPCIINFO._fields_ = [
    # not < Structure version
    ('version', NvU32),
    # not < specifies the internal PCI device identifier for the GVI.
    ('pciDeviceId', NvU32),
    # not < specifies the internal PCI subsystem identifier for the GVI.
    ('pciSubSystemId', NvU32),
    # not < specifies the internal PCI device-specific revision identifier
    # for the GVI.
    ('pciRevisionId', NvU32),
    # not < specifies the PCI domain of the GVI device.
    ('pciDomain', NvU32),
    # not < specifies the PCI bus number of the GVI device.
    ('pciBus', NvU32),
    # not < specifies the PCI slot number of the GVI device.
    ('pciSlot', NvU32),
    # not < specifies the the negotiated PCIE link width.
    ('pciLinkWidth', NVVIOPCILINKWIDTH),
    # not < specifies the the negotiated PCIE link rate.
    ('pciLinkRate', NVVIOPCILINKRATE),
]
NVVIOPCIINFO = NVVIOPCIINFO_V1
NVVIOPCIINFO_VER1 = MAKE_NVAPI_VERSION(NVVIOPCIINFO_V1, 1)
NVVIOPCIINFO_VER = NVVIOPCIINFO_VER1

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_VIO_GetPCIInfo()
# DESCRIPTION: This API gets PCI information of the attached SDI(input)
# capture card.
# PARAMETERS: hVioHandle (IN) - Handle to SDI capture card.
# pVioPCIInfo (OUT) - PCI information of the attached SDI capture card.
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_VIO_GetConfig.
# not SUPPORTED OS: Windows 7 and higher
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# ///////////////////////////////////////////////////////////////////////
NvAPI_VIO_GetPCIInfo = hDll.VIO_GetPCIInfo
NvAPI_VIO_GetPCIInfo.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_VIO_GetPCIInfo(__in NvVioHandle hVioHandle,
#                                             __inout NVVIOPCIINFO* pVioPCIInfo);

# ////////////////////////////////////////////////////////////////////////
# not Function: NvAPI_VIO_IsRunning
# not
# not Description: This API determines if Video I/O is running.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_VIO_GetConfig.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [in] NvVioHandle[IN]  The caller provides the SDI device
# handle as input.
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# ///////////////////////////////////////////////////////////////////////
NvAPI_VIO_IsRunning = hDll.VIO_IsRunning
NvAPI_VIO_IsRunning.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_VIO_IsRunning(NvVioHandle   hVioHandle);

# ///////////////////////////////////////////////////////////////////////
# not Function: NvAPI_VIO_Start
# not
# not Description: This API starts Video I/O.
# not   This API should be called for NVVIOOWNERTYPE_DESKTOP only and will
# not work for OGL applications.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_VIO_GetConfig.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [in] NvVioHandle[IN]  The caller provides the SDI device
# handle as input.
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# ///////////////////////////////////////////////////////////////////////
NvAPI_VIO_Start = hDll.VIO_Start
NvAPI_VIO_Start.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_VIO_Start(NvVioHandle     hVioHandle);

# ///////////////////////////////////////////////////////////////////////
# not Function: NvAPI_VIO_Stop
# not
# not Description: This API stops Video I/O.
# not   This API should be called for NVVIOOWNERTYPE_DESKTOP only and will
# not work for OGL applications.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_VIO_GetConfig.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [in] NvVioHandle[IN]  The caller provides the SDI device
# handle as input.
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# ///////////////////////////////////////////////////////////////////////
NvAPI_VIO_Stop = hDll.VIO_Stop
NvAPI_VIO_Stop.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_VIO_Stop(NvVioHandle     hVioHandle);

# ///////////////////////////////////////////////////////////////////////
# not Function: NvAPI_VIO_IsFrameLockModeCompatible
# not
# not Description: This API checks whether modes are compatible in frame
# lock mode.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_VIO_GetConfig.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [in] NvVioHandle  The caller provides the SDI device handle
# as input.
# not \param [in] srcEnumIndex  Source Enumeration index
# not \param [in] destEnumIndex  Destination Enumeration index
# not \param [out] pbCompatible  Pointer to receive compatibility
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# ///////////////////////////////////////////////////////////////////////
NvAPI_VIO_IsFrameLockModeCompatible = hDll.VIO_IsFrameLockModeCompatible
NvAPI_VIO_IsFrameLockModeCompatible.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_VIO_IsFrameLockModeCompatible(NvVioHandle              hVioHandle,
#                                                     NvU32                    srcEnumIndex,
#                                                     NvU32                    destEnumIndex,
#                                                     NvU32*                   pbCompatible);


# ///////////////////////////////////////////////////////////////////////
# not Function: NvAPI_VIO_EnumDevices
# not
# not Description: This API enumerate all VIO devices connected to the
# system.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_VIO_GetConfig.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [out] NvVioHandle   User passes the pointer of NvVioHandle[]
# array to get handles to
# not        all the connected video I/O devices.
# not \param [out] vioDeviceCount   User gets total number of VIO devices
# connected to the system.
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# ///////////////////////////////////////////////////////////////////////
NvAPI_VIO_EnumDevices = hDll.VIO_EnumDevices
NvAPI_VIO_EnumDevices.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_VIO_EnumDevices(NvVioHandle       hVioHandle[NVAPI_MAX_VIO_DEVICES],
#                                       NvU32             *vioDeviceCount);

# ///////////////////////////////////////////////////////////////////////
# not Function: NvAPI_VIO_QueryTopology
# not
# not Description: This API queries the valid SDI topologies.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_VIO_GetConfig.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [out] pNvVIOTopology  User passes the pointer to
# NVVIOTOPOLOGY to fetch all valid SDI topologies.
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# ///////////////////////////////////////////////////////////////////////
NvAPI_VIO_QueryTopology = hDll.VIO_QueryTopology
NvAPI_VIO_QueryTopology.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_VIO_QueryTopology(NV_VIO_TOPOLOGY   *pNvVIOTopology);

# ///////////////////////////////////////////////////////////////////////
# not Function: NvAPI_VIO_EnumSignalFormats
# not
# not Description: This API enumerates signal formats supported by Video
# I/O.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_VIO_GetConfig.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [in] NvVioHandle  The caller provides the SDI device handle
# as input.
# not \param [in] enumIndex  Enumeration index
# not \param [out] pSignalFormatDetail Pointer to receive detail or NULL
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# ///////////////////////////////////////////////////////////////////////
NvAPI_VIO_EnumSignalFormats = hDll.VIO_EnumSignalFormats
NvAPI_VIO_EnumSignalFormats.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_VIO_EnumSignalFormats(NvVioHandle              hVioHandle,
#                                             NvU32                    enumIndex,
#                                             NVVIOSIGNALFORMATDETAIL  *pSignalFormatDetail);

# ///////////////////////////////////////////////////////////////////////
# not Function: NvAPI_VIO_EnumDataFormats
# not
# not Description: This API enumerates data formats supported by Video I/O.
# not
# not \deprecated Do not use this function - it is deprecated in release
# 290. Instead, use NvAPI_VIO_GetConfig.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 190
# not
# not \param [in] NvVioHandle  The caller provides the SDI device handle
# as input.
# not \param [in] enumIndex   Enumeration index
# not \param [out] pDataFormatDetail Pointer to receive detail or NULL
# not
# not \retval :: NVAPI_NOT_SUPPORTED API is not supported
# not
# ///////////////////////////////////////////////////////////////////////
NvAPI_VIO_EnumDataFormats = hDll.VIO_EnumDataFormats
NvAPI_VIO_EnumDataFormats.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_VIO_EnumDataFormats(NvVioHandle            hVioHandle,
#                                           NvU32                  enumIndex,
#                                           NVVIODATAFORMATDETAIL  *pDataFormatDetail);

# not @}
# ///////////////////////////////////////////////////////////////////////////
# CAMERA TEST API
# These APIs allows test apps to perform low level camera tests
# not \addtogroup vidio
# not @{
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_CreateConfigurationProfileRegistryKey
# not \fn
# NvAPI_Stereo_CreateConfigurationProfileRegistryKey(NV_STEREO_REGISTRY_PROFILE_TYPE registryProfileType)
#
# not
# not DESCRIPTION: Creates new configuration registry key for current
# application.
# not
# not    If there is no configuration profile prior to the function call,
# not    this API tries to create a new configuration profile registry key
# not    for a given application and fill it with the default values.
# not    If an application already has a configuration profile registry
# key, the API does nothing.
# not    The name of the key is automatically set to the name of the
# executable that calls this function.
# not    Because of this, the executable should have a distinct and unique
# name.
# not    If the application is using only one version of DirectX, then the
# default profile type will be appropriate.
# not    If the application is using more than one version of DirectX from
# the same executable,
# not    it should use the appropriate profile type for each configuration
# profile.
# not
# not HOW TO USE: When there is a need for an application to have default
# stereo parameter values,
# not    use this function to create a key to store the values.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in] registryProfileType Type of profile the application
# wants to create. It should be one of the symbolic constants defined in
# not       ::NV_STEREO_REGISTRY_PROFILE_TYPE. Any other value will cause
# function to do nothing and return
# not       ::NV_STEREO_REGISTRY_PROFILE_TYPE_NOT_SUPPORTED.
# not
# not \retval ::NVAPI_OK        Key exists in the registry.
# not \retval ::NVAPI_STEREO_REGISTRY_PROFILE_TYPE_NOT_SUPPORTED This
# profile type is not supported.
# not \retval ::NVAPI_STEREO_REGISTRY_ACCESS_FAILED   Access to registry
# failed.
# not \retval ::NVAPI_API_NOT_INTIALIZED
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED     Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR
# not
# ///////////////////////////////////////////////////////////////////////
# not \ingroup stereoapi
# not Used in NvAPI_Stereo_CreateConfigurationProfileRegistryKey()
class _NV_StereoRegistryProfileType(ENUM):
    NVAPI_STEREO_DEFAULT_REGISTRY_PROFILE = 1

    # not < Separate registry configuration profile for a DirectX 9
    # executable.
    NVAPI_STEREO_DX9_REGISTRY_PROFILE = 2

    # not < Separate registry configuration profile for a DirectX 10
    # executable.
    NVAPI_STEREO_DX10_REGISTRY_PROFILE = 3


NV_STEREO_REGISTRY_PROFILE_TYPE = _NV_StereoRegistryProfileType

# not \ingroup stereoapi
NvAPI_Stereo_CreateConfigurationProfileRegistryKey = hDll.Stereo_CreateConfigurationProfileRegistryKey
NvAPI_Stereo_CreateConfigurationProfileRegistryKey.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Stereo_CreateConfigurationProfileRegistryKey(NV_STEREO_REGISTRY_PROFILE_TYPE registryProfileType);


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_DeleteConfigurationProfileRegistryKey
# not DESCRIPTION: Removes configuration registry key for current
# application.
# not
# not    If an application already has a configuration profile prior to
# this function call,
# not    the function attempts to remove the application's configuration
# profile registry key from the registry.
# not    If there is no configuration profile registry key prior to the
# function call,
# not    the function does nothing and does not report an error.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in] registryProfileType Type of profile that the application
# wants to delete. This should be one of the symbolic
# not       constants defined in ::NV_STEREO_REGISTRY_PROFILE_TYPE. Any
# other value will cause the function
# not       to do nothing and return
# ::NV_STEREO_REGISTRY_PROFILE_TYPE_NOT_SUPPORTED.
# not
# not \retval ::NVAPI_OK        Key does not exist in the registry any
# more.
# not \retval ::NVAPI_STEREO_REGISTRY_PROFILE_TYPE_NOT_SUPPORTED This
# profile type is not supported.
# not \retval ::NVAPI_STEREO_REGISTRY_ACCESS_FAILED   Access to registry
# failed.
# not \retval ::NVAPI_API_NOT_INTIALIZED     NVAPI is not initialized.
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED     Stereo part of NVAPI is
# not initialized.
# not \retval ::NVAPI_ERROR
# not
# not \ingroup stereoapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Stereo_DeleteConfigurationProfileRegistryKey = hDll.Stereo_DeleteConfigurationProfileRegistryKey
NvAPI_Stereo_DeleteConfigurationProfileRegistryKey.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_Stereo_DeleteConfigurationProfileRegistryKey(NV_STEREO_REGISTRY_PROFILE_TYPE registryProfileType);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_SetConfigurationProfileValue
# not \fn
# NvAPI_Stereo_SetConfigurationProfileValue(NV_STEREO_REGISTRY_PROFILE_TYPE registryProfileType, NV_STEREO_REGISTRY_ID valueRegistryID, VOID *pValue)
#
# not
# not DESCRIPTION: This API sets the given parameter value under the
# application's registry key.
# not
# not    If the value does not exist under the application's registry key,
# not    the value will be created under the key.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in]  registryProfileType The type of profile the application
# wants to access. It should be one of the
# not       symbolic constants defined in
# ::NV_STEREO_REGISTRY_PROFILE_TYPE. Any other value
# not       will cause function to do nothing and return
# ::NV_STEREO_REGISTRY_PROFILE_TYPE_NOT_SUPPORTED.
# not \param [in]  valueRegistryID ID of the value that is being set. It
# should be one of the symbolic constants defined in
# not       ::NV_STEREO_REGISTRY_PROFILE_TYPE. Any other value will cause
# function to do nothing
# not       and return ::NVAPI_STEREO_REGISTRY_VALUE_NOT_SUPPORTED.
# not \param [in]  pValue   Address of the value that is being set. It
# should be either address of a DWORD or of a float,
# not       dependent on the type of the stereo parameter whose value is
# being set. The API will then cast that
# not       address to DWORD* and write whatever is in those 4 bytes as a
# DWORD to the registry.
# not
# not \retval ::NVAPI_OK        Value is written to registry.
# not \retval ::NVAPI_STEREO_REGISTRY_PROFILE_TYPE_NOT_SUPPORTED This
# profile type is not supported.
# not \retval ::NVAPI_STEREO_REGISTRY_VALUE_NOT_SUPPORTED  This value is
# not supported.
# not \retval ::NVAPI_STEREO_REGISTRY_ACCESS_FAILED   Access to registry
# failed.
# not \retval ::NVAPI_API_NOT_INTIALIZED     NVAPI is not initialized.
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED     Stereo part of NVAPI is
# not initialized.
# not \retval ::NVAPI_ERROR       Something is wrong (generic error).
# ///////////////////////////////////////////////////////////////////////
# not \ingroup stereoapi
# not Used in NvAPI_Stereo_SetConfigurationProfileValue()
class _NV_StereoRegistryID(ENUM):
    NVAPI_CONVERGENCE_ID = 1
    NVAPI_FRUSTUM_ADJUST_MODE_ID = 2


NV_STEREO_REGISTRY_ID = _NV_StereoRegistryID

# not \ingroup stereoapi
NvAPI_Stereo_SetConfigurationProfileValue = hDll.Stereo_SetConfigurationProfileValue
NvAPI_Stereo_SetConfigurationProfileValue.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Stereo_SetConfigurationProfileValue(NV_STEREO_REGISTRY_PROFILE_TYPE registryProfileType, NV_STEREO_REGISTRY_ID valueRegistryID, VOID *pValue);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_DeleteConfigurationProfileValue
# not DESCRIPTION: This API removes the given value from the application's
# configuration profile registry key.
# not    If there is no such value, the function does nothing and does not
# report an error.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in]  registryProfileType The type of profile the application
# wants to access. It should be one of the
# not       symbolic constants defined in
# ::NV_STEREO_REGISTRY_PROFILE_TYPE. Any other value will
# not       cause function to do nothing and return
# ::NV_STEREO_REGISTRY_PROFILE_TYPE_NOT_SUPPORTED.
# not \param [in]  valueRegistryID  ID of the value that is being deleted.
# It should be one of the symbolic constants defined in
# not       ::NV_STEREO_REGISTRY_PROFILE_TYPE. Any other value will cause
# function to do nothing and return
# not       ::NVAPI_STEREO_REGISTRY_VALUE_NOT_SUPPORTED.
# not
# not \retval ::NVAPI_OK        Value does not exist in registry any more.
# not \retval ::NVAPI_STEREO_REGISTRY_PROFILE_TYPE_NOT_SUPPORTED This
# profile type is not supported.
# not \retval ::NVAPI_STEREO_REGISTRY_VALUE_NOT_SUPPORTED  This value is
# not supported.
# not \retval ::NVAPI_STEREO_REGISTRY_ACCESS_FAILED   Access to registry
# failed.
# not \retval ::NVAPI_API_NOT_INTIALIZED
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED     Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR
# not
# not \ingroup stereoapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Stereo_DeleteConfigurationProfileValue = hDll.Stereo_DeleteConfigurationProfileValue
NvAPI_Stereo_DeleteConfigurationProfileValue.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Stereo_DeleteConfigurationProfileValue(NV_STEREO_REGISTRY_PROFILE_TYPE registryProfileType, NV_STEREO_REGISTRY_ID valueRegistryID);

# not \addtogroup stereoapi
# not @{
_NVAPI_STEREO_CAPS._fields_ = [
    ('version', NvU32),
    ('supportsWindowedModeOff', NvU32, 1),
    ('supportsWindowedModeAutomatic', NvU32, 1),
    ('supportsWindowedModePersistent', NvU32, 1),
    # must be 0
    ('reserved', NvU32, 29),
    # must be 0
    ('reserved2', NvU32 * 3),
]
NVAPI_STEREO_CAPS_VER1 = MAKE_NVAPI_VERSION(_NVAPI_STEREO_CAPS, 1)
NVAPI_STEREO_CAPS_VER = NVAPI_STEREO_CAPS_VER1
NVAPI_STEREO_CAPS = NVAPI_STEREO_CAPS_V1
# not @}
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_GetStereoSupport
# not DESCRIPTION: This API checks what kind of stereo support is
# currently supported on a particular display.
# not   If the the display is prohibited from showing stereo
# (e.g. secondary in a multi-mon setup), we will
# not   return 0 for all stereo modes
# (full screen exclusive, automatic windowed, persistent windowed).
# not   Otherwise, we will check which stereo mode is supported. On 120Hz
# display, this will be what
# not   the user chooses in control panel. On HDMI 1.4 display, persistent
# windowed mode is always assumed to be
# not   supported. Note that this function does not check if the CURRENT
# RESOLUTION/REFRESH RATE can support
# not   stereo. For HDMI 1.4, it is the app's responsibility to change the
# resolution/refresh rate to one that is
# not   3D compatible. For 120Hz, the driver will ALWAYS force 120Hz
# anyway.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 304
# not
# not \param [in]  hMonitor handle to monitor that app is going to run on
# not \param [out] pCaps Address where the result of the inquiry will be
# placed.
# not     *pCaps is defined in NVAPI_STEREO_CAPS.
# not \return  This API can return any of the following error codes
# enumerated in NvAPI_Status
# not \retval ::NVAPI_OK
# not
# not \ingroup stereoapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Stereo_GetStereoSupport = hDll.Stereo_GetStereoSupport
NvAPI_Stereo_GetStereoSupport.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Stereo_GetStereoSupport(__in NvMonitorHandle hMonitor, __out NVAPI_STEREO_CAPS *pCaps);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_DecreaseSeparation
# not DESCRIPTION: This API decreases separation for the given device
# interface (just like the Ctrl + F3 hotkey).
# not
# not WHEN TO USE: After the stereo handle for device interface is created
# via successfull call to the appropriate NvAPI_Stereo_CreateHandleFrom()
# function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in] stereoHandle Stereo handle that corresponds to the
# device interface.
# not
# not \retval ::NVAPI_OK - Decrease of separation percentage was
# successfull.
# not \retval ::NVAPI_STEREO_INVALID_DEVICE_INTERFACE - Device interface
# is not valid. Create again, then attach again.
# not \retval ::NVAPI_API_NOT_INTIALIZED - NVAPI not initialized.
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED - Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR - Something is wrong (generic error).
# not
# not \ingroup stereoapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Stereo_DecreaseSeparation = hDll.Stereo_DecreaseSeparation
NvAPI_Stereo_DecreaseSeparation.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Stereo_DecreaseSeparation(StereoHandle stereoHandle);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_IncreaseSeparation
# not DESCRIPTION: This API increases separation for the given device
# interface (just like the Ctrl + F4 hotkey).
# not
# not WHEN TO USE: After the stereo handle for the device interface is
# created via successfull call to the appropriate
# NvAPI_Stereo_CreateHandleFrom() function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in] stereoHandle Stereo handle that corresponds to the
# device interface.
# not
# not \retval ::NVAPI_OK      Increase of separation percentage was
# successfull.
# not \retval ::NVAPI_STEREO_INVALID_DEVICE_INTERFACE Device interface is
# not valid. Create again, then attach again.
# not \retval ::NVAPI_API_NOT_INTIALIZED   NVAPI not initialized.
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED   Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR     Something is wrong (generic error).
# not
# not \ingroup stereoapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Stereo_IncreaseSeparation = hDll.Stereo_IncreaseSeparation
NvAPI_Stereo_IncreaseSeparation.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Stereo_IncreaseSeparation(StereoHandle stereoHandle);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_DecreaseConvergence
# not DESCRIPTION: This API decreases convergence for the given device
# interface (just like the Ctrl + F5 hotkey).
# not
# not WHEN TO USE: After the stereo handle for the device interface is
# created via successfull call to the appropriate
# NvAPI_Stereo_CreateHandleFrom() function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in]  stereoHandle Stereo handle that corresponds to the
# device interface.
# not
# not \retval ::NVAPI_OK - Decrease of convergence was successfull.
# not \retval ::NVAPI_STEREO_INVALID_DEVICE_INTERFACE - Device interface
# is not valid. Create again, then attach again.
# not \retval ::NVAPI_API_NOT_INTIALIZED - NVAPI not initialized.
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED - Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR - Something is wrong (generic error).
# not
# not \ingroup stereoapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Stereo_DecreaseConvergence = hDll.Stereo_DecreaseConvergence
NvAPI_Stereo_DecreaseConvergence.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Stereo_DecreaseConvergence(StereoHandle stereoHandle);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_IncreaseConvergence
# not DESCRIPTION: This API increases convergence for given the device
# interface (just like the Ctrl + F5 hotkey).
# not
# not WHEN TO USE: After the stereo handle for the device interface is
# created via successfull call to the appropriate
# NvAPI_Stereo_CreateHandleFrom() function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in] stereoHandle Stereo handle that corresponds to the
# device interface.
# not
# not \retval ::NVAPI_OK      Increase of convergence was successfull.
# not \retval ::NVAPI_STEREO_INVALID_DEVICE_INTERFACE Device interface is
# not valid. Create again, then attach again.
# not \retval ::NVAPI_API_NOT_INTIALIZED
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED   Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR
# not
# not \ingroup stereoapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Stereo_IncreaseConvergence = hDll.Stereo_IncreaseConvergence
NvAPI_Stereo_IncreaseConvergence.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_Stereo_IncreaseConvergence(StereoHandle stereoHandle);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_GetFrustumAdjustMode
# not \fn
# NvAPI_Stereo_GetFrustumAdjustMode(StereoHandle stereoHandle, NV_FRUSTUM_ADJUST_MODE *pFrustumAdjustMode)
#
# not DESCRIPTION: This API gets the current frustum adjust mode value.
# not
# not WHEN TO USE: After the stereo handle for the device interface is
# created via successfull call to the appropriate
# NvAPI_Stereo_CreateHandleFrom() function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in]  stereoHandle  Stereo handle that corresponds to the
# device interface.
# not \param [out] pFrustumAdjustMode Address of the
# NV_FRUSTUM_ADJUST_MODE type variable to store current frustum value in.
# not
# not \retval ::NVAPI_OK - Retrieval of frustum adjust mode was
# successfull.
# not \retval ::NVAPI_STEREO_INVALID_DEVICE_INTERFACE - Device interface
# is not valid. Create again, then attach again.
# not \retval ::NVAPI_API_NOT_INTIALIZED - NVAPI not initialized.
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED - Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR - Something is wrong (generic error).
# not
# ///////////////////////////////////////////////////////////////////////
# not \ingroup stereoapi
# not Used in NvAPI_Stereo_GetFrustumAdjustMode().
class _NV_FrustumAdjustMode(ENUM):
    NVAPI_NO_FRUSTUM_ADJUST = 1
    NVAPI_FRUSTUM_STRETCH = 2
    NVAPI_FRUSTUM_CLEAR_EDGES = 3


NV_FRUSTUM_ADJUST_MODE = _NV_FrustumAdjustMode

# not \ingroup stereoapi
NvAPI_Stereo_GetFrustumAdjustMode = hDll.Stereo_GetFrustumAdjustMode
NvAPI_Stereo_GetFrustumAdjustMode.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Stereo_GetFrustumAdjustMode(StereoHandle stereoHandle, NV_FRUSTUM_ADJUST_MODE *pFrustumAdjustMode);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_SetFrustumAdjustMode
# not DESCRIPTION: This API sets the current frustum adjust mode value.
# not
# not WHEN TO USE: After the stereo handle for the device interface is
# created via successfull call to the appropriate
# NvAPI_Stereo_CreateHandleFrom() function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in]  stereoHandle   Stereo handle that corresponds to the
# device interface.
# not \param [in]  newFrustumAdjustModeValue New value for frustum adjust
# mode. It should be one of the symbolic constants defined in
# not        ::NV_FRUSTUM_ADJUST_MODE. Any other value will cause function
# to do nothing and return
# not        ::NVAPI_STEREO_FRUSTUM_ADJUST_MODE_NOT_SUPPORTED.
# not
# not \retval ::NVAPI_OK        Retrieval of frustum adjust mode was
# successfull.
# not \retval ::NVAPI_STEREO_INVALID_DEVICE_INTERFACE  Device interface is
# not valid. Create again, then attach again.
# not \retval ::NVAPI_API_NOT_INTIALIZED
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED    Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_STEREO_FRUSTUM_ADJUST_MODE_NOT_SUPPORTED Given
# frustum adjust mode is not supported.
# not \retval ::NVAPI_ERROR
# not
# not \ingroup stereoapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Stereo_SetFrustumAdjustMode = hDll.Stereo_SetFrustumAdjustMode
NvAPI_Stereo_SetFrustumAdjustMode.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Stereo_SetFrustumAdjustMode(StereoHandle stereoHandle, NV_FRUSTUM_ADJUST_MODE newFrustumAdjustModeValue);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_CaptureJpegImage
# not DESCRIPTION: This API captures the current stereo image in JPEG
# stereo format with the given quality.
# not    Only the last capture call per flip will be effective.
# not
# not WHEN TO USE: After the stereo handle for the device interface is
# created via successfull call to the appropriate
# NvAPI_Stereo_CreateHandleFrom() function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in]  stereoHandle Stereo handle that corresponds to the
# device interface.
# not \param [in]  quality  Quality of the JPEG image to be captured.
# Integer value betweeen 0 and 100.
# not
# not \retval ::NVAPI_OK     Image captured.
# not \retval ::NVAPI_STEREO_INVALID_DEVICE_INTERFACE Device interface is
# not valid. Create again, then attach again.
# not \retval ::NVAPI_API_NOT_INTIALIZED
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED
# not \retval ::NVAPI_STEREO_PARAMETER_OUT_OF_RANGE Given quality is out
# of [0..100] range.
# not \retval ::NVAPI_ERROR
# not
# not \ingroup stereoapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Stereo_CaptureJpegImage = hDll.Stereo_CaptureJpegImage
NvAPI_Stereo_CaptureJpegImage.restype = NVAPI_INTERFACE


# NVAPI_INTERFACE NvAPI_Stereo_CaptureJpegImage(StereoHandle stereoHandle, NvU32 quality);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_InitActivation
# not DESCRIPTION: This API allows an application to enable stereo
# viewing, without the need of a GUID/Key pair
# not    This API cannot be used to enable stereo viewing on 3DTV.
# not
# not HOW TO USE: Call this function immediately after device creation,
# then follow with a reset. \n
# not    Very generically:
# not    Create Device.Create Stereo Handle.InitActivation.Reset Device
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not \since Release: 302
# not
# not \param [in] stereoHandle  Stereo handle corresponding to the device
# interface.
# not \param [in] bDelayed   Use delayed activation
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not  If there are return error codes with specific meaning for this API,
# not  they are listed below.
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED - Stereo part of NVAPI not
# initialized.
# not
# not \ingroup stereoapi
# ///////////////////////////////////////////////////////////////////////
# not \addtogroup stereoapi
# not @{
# not InitActivation Flags
class _NVAPI_STEREO_INIT_ACTIVATION_FLAGS(ENUM):
    NVAPI_STEREO_INIT_ACTIVATION_IMMEDIATE = 0x00
    NVAPI_STEREO_INIT_ACTIVATION_DELAYED = 0x01


NVAPI_STEREO_INIT_ACTIVATION_FLAGS = _NVAPI_STEREO_INIT_ACTIVATION_FLAGS

NvAPI_Stereo_InitActivation = hDll.Stereo_InitActivation
NvAPI_Stereo_InitActivation.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Stereo_InitActivation(__in StereoHandle hStereoHandle, __in NVAPI_STEREO_INIT_ACTIVATION_FLAGS flags);

# not @}
# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_Trigger_Activation
# not DESCRIPTION: This API allows an application to trigger creation of a
# stereo desktop,
# not    in case the creation was stopped on application launch.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not \since Release: 302
# not
# not \param [in] stereoHandle Stereo handle that corresponds to the
# device interface.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not  If there are return error codes with specific meaning for this API,
# not  they are listed below.
# not \retval ::NVAPI_STEREO_INIT_ACTIVATION_NOT_DONE - Stereo
# InitActivation not called.
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED - Stereo part of NVAPI not
# initialized.
# not
# not \ingroup stereoapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Stereo_Trigger_Activation = hDll.Stereo_Trigger_Activation
NvAPI_Stereo_Trigger_Activation.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Stereo_Trigger_Activation(__in StereoHandle hStereoHandle);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_CapturePngImage
# not DESCRIPTION: This API captures the current stereo image in PNG
# stereo format.
# not    Only the last capture call per flip will be effective.
# not
# not WHEN TO USE: After the stereo handle for the device interface is
# created via successfull call to the appropriate
# NvAPI_Stereo_CreateHandleFrom() function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in]  stereoHandle Stereo handle corresponding to the device
# interface.
# not
# not \retval ::NVAPI_OK      Image captured.
# not \retval ::NVAPI_STEREO_INVALID_DEVICE_INTERFACE Device interface is
# not valid. Create again, then attach again.
# not \retval ::NVAPI_API_NOT_INTIALIZED
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED   Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR
# not
# not \ingroup stereoapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Stereo_CapturePngImage = hDll.Stereo_CapturePngImage
NvAPI_Stereo_CapturePngImage.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Stereo_CapturePngImage(StereoHandle stereoHandle);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_ReverseStereoBlitControl
# not DESCRIPTION: This API turns on/off reverse stereo blit.
# not
# not HOW TO USE: Use after the stereo handle for the device interface is
# created via successfull call to the appropriate
# not    NvAPI_Stereo_CreateHandleFrom() function.
# not    After reversed stereo blit control is turned on, blits from the
# stereo surface will
# not    produce the right-eye image in the left side of the destination
# surface and the left-eye
# not    image in the right side of the destination surface.
# not
# not    In DirectX 9, the destination surface must be created as the
# render target, and StretchRect must be used.
# not    Conditions:
# not    - DstWidth == 2*SrcWidth
# not    - DstHeight == SrcHeight
# not    - Src surface is the stereo surface.
# not    - SrcRect must be {0,0,SrcWidth,SrcHeight}
# not    - DstRect must be {0,0,DstWidth,DstHeight}
# not
# not    In DirectX 10, ResourceCopyRegion must be used.
# not    Conditions:
# not    - DstWidth == 2*SrcWidth
# not    - DstHeight == SrcHeight
# not    - dstX == 0,
# not    - dstY == 0,
# not    - dstZ == 0,
# not    - SrcBox: left=top=front == 0; right == SrcWidth; bottom ==
# SrcHeight; back == 1;
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 185
# not
# not \param [in] stereoHandle Stereo handle corresponding to the device
# interface.
# not \param [in] TurnOn  != 0 : Turns on \n
# not      == 0 : Turns off
# not
# not
# not \retval ::NVAPI_OK      Retrieval of frustum adjust mode was
# successfull.
# not \retval ::NVAPI_STEREO_INVALID_DEVICE_INTERFACE Device interface is
# not valid. Create again, then attach again.
# not \retval ::NVAPI_API_NOT_INTIALIZED
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED  Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR
# not
# not \ingroup stereoapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Stereo_ReverseStereoBlitControl = hDll.Stereo_ReverseStereoBlitControl
NvAPI_Stereo_ReverseStereoBlitControl.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Stereo_ReverseStereoBlitControl(StereoHandle hStereoHandle, NvU8 TurnOn);

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_SetNotificationMessage
# not DESCRIPTION: This API is a Setup notification message that the
# stereo driver uses to notify the application
# not    when the user changes the stereo driver state.
# not
# not    When the user changes the stereo state
# (Activated or Deactivated, separation or conversion)
# not    the stereo driver posts a defined message with the following
# parameters:
# not
# not    lParam is the current conversion.
# (Actual conversion is *(FLOAT*) & lParam )
# not
# not    wParam == MAKEWPARAM(l, h) where
# not    - l == 0 if stereo is deactivated
# not    - l == 1 if stereo is deactivated
# not    - h is the current separation.
# (Actual separation is float(h*100.f/0xFFFF)
# not
# not    Call this API with NULL hWnd to prohibit notification.
# not
# not WHEN TO USE: Use after the stereo handle for device interface is
# created via successful call to appropriate
# not    NvAPI_Stereo_CreateHandleFrom() function.
# not
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not
# not \param [in]  stereoHandle Stereo handle corresponding to the device
# interface.
# not \param [in]  hWnd  Window HWND that will be notified when the user
# changes the stereo driver state.
# not      Actual HWND must be cast to an NvU64.
# not \param [in]  messageID  MessageID of the message that will be posted
# to hWnd
# not
# not \retval ::NVAPI_OK      Notification set.
# not \retval ::NVAPI_STEREO_INVALID_DEVICE_INTERFACE Device interface is
# not valid. Create again, then attach again.
# not \retval ::NVAPI_API_NOT_INTIALIZED
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED  Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR
# not
# not \ingroup stereoapi
# ///////////////////////////////////////////////////////////////////////
NvAPI_Stereo_SetNotificationMessage = hDll.Stereo_SetNotificationMessage
NvAPI_Stereo_SetNotificationMessage.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_Stereo_SetNotificationMessage(StereoHandle hStereoHandle, NvU64 hWnd,NvU64 messageID);

# not \ingroup stereoapi
NVAPI_STEREO_QUADBUFFERED_API_VERSION = 0x2


# not \ingroup stereoapi
class _NV_StereoSwapChainMode(ENUM):
    NVAPI_STEREO_SWAPCHAIN_DEFAULT = 0
    NVAPI_STEREO_SWAPCHAIN_STEREO = 1
    NVAPI_STEREO_SWAPCHAIN_MONO = 2


NV_STEREO_SWAPCHAIN_MODE = _NV_StereoSwapChainMode

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D1x_CreateSwapChain
# not DESCRIPTION: This API allows the user to create a mono or a
# stereo swap chain.
# not
# not   NOTE: NvAPI_D3D1x_CreateSwapChain is a wrapper of the method
# IDXGIFactory::CreateSwapChain which
# not    additionally notifies the D3D driver of the mode in which
# stereo mode the swap chain is to be
# not    created.
# not
# not \since Release: 285
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  hStereoHandle Stereo handle that corresponds to the
# device interface.
# not      A pointer to the device that will write 2D images to the
# swap chain.
# not \param [in]  pDesc   A pointer to the swap-chain description
# (DXGI_SWAP_CHAIN_DESC). This parameter cannot be NULL.
# not \param [out] ppSwapChain  A pointer to the swap chain created.
# not \param [in]  mode   The stereo mode fot the swap chain.
# not      NVAPI_STEREO_SWAPCHAIN_DEFAULT
# not      NVAPI_STEREO_SWAPCHAIN_STEREO
# not      NVAPI_STEREO_SWAPCHAIN_MONO
# not
# not \retval ::NVAPI_OK    The swap chain was created successfully.
# not \retval ::NVAPI_ERROR   The operation failed.
# not
# not \ingroup stereoapi
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D1x_CreateSwapChain = hDll.D3D1x_CreateSwapChain
NvAPI_D3D1x_CreateSwapChain.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D1x_CreateSwapChain(StereoHandle hStereoHandle,
#                                             DXGI_SWAP_CHAIN_DESC* pDesc,
#                                             IDXGISwapChain** ppSwapChain,
#                                             NV_STEREO_SWAPCHAIN_MODE mode);


# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D9_CreateSwapChain
# not DESCRIPTION: This API allows the user to create a mono or a
# stereo swap chain.
# not
# not   NOTE: NvAPI_D3D9_CreateSwapChain is a wrapper of the method
# IDirect3DDevice9::CreateAdditionalSwapChain which
# not    additionally notifies the D3D driver if the swap chain
# creation mode must be stereo or mono.
# not
# not
# not \since Release: 285
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hStereoHandle  Stereo handle that corresponds to the
# device interface.
# not \param [in, out] pPresentationParameters A pointer to the
# swap-chain description (DXGI). This parameter cannot be NULL.
# not \param [out]  ppSwapChain   A pointer to the swap chain created.
# not \param [in] mode    The stereo mode for the swap chain.
# not        NVAPI_STEREO_SWAPCHAIN_DEFAULT
# not        NVAPI_STEREO_SWAPCHAIN_STEREO
# not        NVAPI_STEREO_SWAPCHAIN_MONO
# not
# not \retval ::NVAPI_OK    The swap chain creation was successful
# not \retval ::NVAPI_ERROR    The operation failed.
# not
# not \ingroup stereoapi
# ///////////////////////////////////////////////////////////////////
NvAPI_D3D9_CreateSwapChain = hDll.D3D9_CreateSwapChain
NvAPI_D3D9_CreateSwapChain.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_D3D9_CreateSwapChain(StereoHandle hStereoHandle,
#                                            D3DPRESENT_PARAMETERS *pPresentationParameters,
#                                            IDirect3DSwapChain9 **ppSwapChain,
#                                            NV_STEREO_SWAPCHAIN_MODE mode);

# ndif //if defined(_D3D9_H_) //NvAPI_D3D9_CreateSwapChain
# not \addtogroup drsapi
# not @{
# GPU Profile APIs

NvDRSSessionHandle = NV_DECLARE_HANDLE('NvDRSSessionHandle')
NvDRSProfileHandle = NV_DECLARE_HANDLE('NvDRSProfileHandle')

NVAPI_DRS_GLOBAL_PROFILE = NvDRSProfileHandle(-1)
NVAPI_SETTING_MAX_VALUES = 100


class _NVDRS_SETTING_TYPE(ENUM):
    NVDRS_DWORD_TYPE = 1
    NVDRS_BINARY_TYPE = 2
    NVDRS_STRING_TYPE = 3
    NVDRS_WSTRING_TYPE = 4


NVDRS_SETTING_TYPE = _NVDRS_SETTING_TYPE


class _NVDRS_SETTING_LOCATION(ENUM):
    NVDRS_CURRENT_PROFILE_LOCATION = 1
    NVDRS_GLOBAL_PROFILE_LOCATION = 2
    NVDRS_BASE_PROFILE_LOCATION = 3
    NVDRS_DEFAULT_PROFILE_LOCATION = 4


NVDRS_SETTING_LOCATION = _NVDRS_SETTING_LOCATION

_NVDRS_GPU_SUPPORT._fields_ = [
    ('geforce', NvU32, 1),
    ('quadro', NvU32, 1),
    ('nvs', NvU32, 1),
    ('reserved4', NvU32, 1),
    ('reserved5', NvU32, 1),
    ('reserved6', NvU32, 1),
    ('reserved7', NvU32, 1),
    ('reserved8', NvU32, 1),
    ('reserved9', NvU32, 1),
    ('reserved10', NvU32, 1),
    ('reserved11', NvU32, 1),
    ('reserved12', NvU32, 1),
    ('reserved13', NvU32, 1),
    ('reserved14', NvU32, 1),
    ('reserved15', NvU32, 1),
    ('reserved16', NvU32, 1),
    ('reserved17', NvU32, 1),
    ('reserved18', NvU32, 1),
    ('reserved19', NvU32, 1),
    ('reserved20', NvU32, 1),
    ('reserved21', NvU32, 1),
    ('reserved22', NvU32, 1),
    ('reserved23', NvU32, 1),
    ('reserved24', NvU32, 1),
    ('reserved25', NvU32, 1),
    ('reserved26', NvU32, 1),
    ('reserved27', NvU32, 1),
    ('reserved28', NvU32, 1),
    ('reserved29', NvU32, 1),
    ('reserved30', NvU32, 1),
    ('reserved31', NvU32, 1),
    ('reserved32', NvU32, 1),
]

# not Enum to decide on the datatype of setting value.
_NVDRS_BINARY_SETTING._fields_ = [
    # not < valueLength should always be in number of bytes.
    ('valueLength', NvU32),
    ('valueData', NvU8 * NVAPI_BINARY_DATA_MAX),
]


class _Union_10(ctypes.Union):
    pass


_Union_10._fields_ = [
    # not < Accessing default DWORD value of this setting.
    ('u32DefaultValue', NvU32),
    # not < Accessing default Binary value of this setting.
    ('binaryDefaultValue', NVDRS_BINARY_SETTING),
    # not < Accessing default unicode string value of this setting.
    ('wszDefaultValue', NvAPI_UnicodeString),
]
_NVDRS_SETTING_VALUES._Union_10 = _Union_10


# not < NOT mixed types.
class settingValues(ctypes.Union):
    pass


settingValues._fields_ = [
    # not < All possible DWORD values for a setting
    ('u32Value', NvU32),
    # not < All possible Binary values for a setting
    ('binaryValue', NVDRS_BINARY_SETTING),
    # not < Accessing current unicode string value of this setting.
    ('wszValue', NvAPI_UnicodeString),
]
_NVDRS_SETTING_VALUES.settingValues = settingValues

_NVDRS_SETTING_VALUES._anonymous_ = (
    '_Union_10',
)

_NVDRS_SETTING_VALUES._fields_ = [
    # not < Structure Version
    ('version', NvU32),
    # not < Total number of values available in a setting.
    ('numSettingValues', NvU32),
    # not < Type of setting value.
    ('settingType', NVDRS_SETTING_TYPE),
    # not < Setting can hold either DWORD or Binary value or string.
    # Not mixed types.
    ('_Union_10', _NVDRS_SETTING_VALUES._Union_10),
    # not < Setting values can be of either DWORD, Binary values or
    # String type,
    ('settingValues', _NVDRS_SETTING_VALUES.settingValues * NVAPI_SETTING_MAX_VALUES),
]

# not Macro for constructing the version field of
# ::_NVDRS_SETTING_VALUES
NVDRS_SETTING_VALUES_VER = (
    MAKE_NVAPI_VERSION(NVDRS_SETTING_VALUES, 1)
)


class _Union_11(ctypes.Union):
    pass


_Union_11._fields_ = [
    # not < Accessing default DWORD value of this setting.
    ('u32PredefinedValue', NvU32),
    # not < Accessing default Binary value of this setting.
    ('binaryPredefinedValue', NVDRS_BINARY_SETTING),
    # not < Accessing default unicode string value of this setting.
    ('wszPredefinedValue', NvAPI_UnicodeString),
]
_NVDRS_SETTING_V1._Union_11 = _Union_11


class _Union_12(ctypes.Union):
    pass


_Union_12._fields_ = [
    # not < Accessing current DWORD value of this setting.
    ('u32CurrentValue', NvU32),
    # not < Accessing current Binary value of this setting.
    ('binaryCurrentValue', NVDRS_BINARY_SETTING),
    # not < Accessing current unicode string value of this setting.
    ('wszCurrentValue', NvAPI_UnicodeString),
]
_NVDRS_SETTING_V1._Union_12 = _Union_12

_NVDRS_SETTING_V1._anonymous_ = (
    '_Union_11',
    '_Union_12',
)

_NVDRS_SETTING_V1._fields_ = [
    # not < Structure Version
    ('version', NvU32),
    # not < String name of setting
    ('settingName', NvAPI_UnicodeString),
    # not < 32 bit setting Id
    ('settingId', NvU32),
    # not < Type of setting value.
    ('settingType', NVDRS_SETTING_TYPE),
    # not < Describes where the value in CurrentValue comes from.
    ('settingLocation', NVDRS_SETTING_LOCATION),
    # not < It is different than 0 if the currentValue is a predefined
    # Value,
    ('isCurrentPredefined', NvU32),
    # not < It is different than 0 if the PredefinedValue union
    # contains a valid value.
    ('isPredefinedValid', NvU32),
    # not < Setting can hold either DWORD or Binary value or string.
    # Not mixed types.
    ('_Union_11', _NVDRS_SETTING_V1._Union_11),
    # not < Setting can hold either DWORD or Binary value or string.
    # Not mixed types.
    ('_Union_12', _NVDRS_SETTING_V1._Union_12),
]

# not Macro for constructing the version field of ::_NVDRS_SETTING
NVDRS_SETTING_VER1 = MAKE_NVAPI_VERSION(NVDRS_SETTING_V1, 1)
NVDRS_SETTING = NVDRS_SETTING_V1
NVDRS_SETTING_VER = NVDRS_SETTING_VER1

_NVDRS_APPLICATION_V1._fields_ = [
    # not < Structure Version
    ('version', NvU32),
    # not < Is the application userdefined/predefined
    ('isPredefined', NvU32),
    # not < String name of the Application
    ('appName', NvAPI_UnicodeString),
    # not < UserFriendly name of the Application
    ('userFriendlyName', NvAPI_UnicodeString),
    # not < Indicates the name (if any) of the launcher that starts
    # the application
    ('launcher', NvAPI_UnicodeString),
]

_NVDRS_APPLICATION_V2._fields_ = [
    # not < Structure Version
    ('version', NvU32),
    # not < Is the application userdefined/predefined
    ('isPredefined', NvU32),
    # not < String name of the Application
    ('appName', NvAPI_UnicodeString),
    # not < UserFriendly name of the Application
    ('userFriendlyName', NvAPI_UnicodeString),
    # not < Indicates the name (if any) of the launcher that starts
    # the Application
    ('launcher', NvAPI_UnicodeString),
    # not < Select this application only if this file is found.
    ('fileInFolder', NvAPI_UnicodeString),
]

_NVDRS_APPLICATION_V3._fields_ = [
    # not < Structure Version
    ('version', NvU32),
    # not < Is the application userdefined/predefined
    ('isPredefined', NvU32),
    # not < String name of the Application
    ('appName', NvAPI_UnicodeString),
    # not < UserFriendly name of the Application
    ('userFriendlyName', NvAPI_UnicodeString),
    # not < Indicates the name (if any) of the launcher that starts
    # the Application
    ('launcher', NvAPI_UnicodeString),
    # not < Select this application only if this file is found.
    ('fileInFolder', NvAPI_UnicodeString),
    # not < Windows 8 style app
    ('isMetro', NvU32, 1),
    # not < Command line parsing for the application name
    ('isCommandLine', NvU32, 1),
    # not < Reserved. Should be 0.
    ('reserved', NvU32, 30),
]

_NVDRS_APPLICATION_V4._fields_ = [
    # not < Structure Version
    ('version', NvU32),
    # not < Is the application userdefined/predefined
    ('isPredefined', NvU32),
    # not < String name of the Application
    ('appName', NvAPI_UnicodeString),
    # not < UserFriendly name of the Application
    ('userFriendlyName', NvAPI_UnicodeString),
    # not < Indicates the name (if any) of the launcher that starts
    # the Application
    ('launcher', NvAPI_UnicodeString),
    # not < Select this application only if this file is found.
    ('fileInFolder', NvAPI_UnicodeString),
    # not < Windows 8 style app
    ('isMetro', NvU32, 1),
    # not < Command line parsing for the application name
    ('isCommandLine', NvU32, 1),
    # not < Reserved. Should be 0.
    ('reserved', NvU32, 30),
    # not < If isCommandLine is set to 0 this must be an empty. If
    # isCommandLine is set to 1
    ('commandLine', NvAPI_UnicodeString),
]
NVDRS_APPLICATION_VER_V1 = (
    MAKE_NVAPI_VERSION(NVDRS_APPLICATION_V1, 1)
)
NVDRS_APPLICATION_VER_V2 = (
    MAKE_NVAPI_VERSION(NVDRS_APPLICATION_V2, 2)
)
NVDRS_APPLICATION_VER_V3 = (
    MAKE_NVAPI_VERSION(NVDRS_APPLICATION_V3, 3)
)
NVDRS_APPLICATION_VER_V4 = (
    MAKE_NVAPI_VERSION(NVDRS_APPLICATION_V4, 4)
)
NVDRS_APPLICATION = NVDRS_APPLICATION_V4
NVDRS_APPLICATION_VER = NVDRS_APPLICATION_VER_V4

_NVDRS_PROFILE_V1._fields_ = [
    # not < Structure Version
    ('version', NvU32),
    # not < String name of the Profile
    ('profileName', NvAPI_UnicodeString),
    # not < This read-only flag indicates the profile support on either
    ('gpuSupport', NVDRS_GPU_SUPPORT),
    # not < Is the Profile user-defined, or predefined
    ('isPredefined', NvU32),
    # not < Total number of applications that belong to this profile.
    # Read-only
    ('numOfApps', NvU32),
    # not < Total number of settings applied for this Profile.
    # Read-only
    ('numOfSettings', NvU32),
]
NVDRS_PROFILE = NVDRS_PROFILE_V1
# not Macro for constructing the version field of ::NVDRS_PROFILE
NVDRS_PROFILE_VER1 = MAKE_NVAPI_VERSION(NVDRS_PROFILE_V1, 1)
NVDRS_PROFILE_VER = NVDRS_PROFILE_VER1

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_CreateSession
# not DESCRIPTION: This API allocates memory and initializes the
# session.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [out] *phSession Return pointer to the session handle.
# not
# not \retval ::NVAPI_OK SUCCESS
# not \retval ::NVAPI_ERROR: For miscellaneous errors.
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_CreateSession = hDll.DRS_CreateSession
NvAPI_DRS_CreateSession.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_CreateSession(NvDRSSessionHandle *phSession);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_DestroySession
# not DESCRIPTION: This API frees the allocation: cleanup of
# NvDrsSession.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession Input to the session handle.
# not
# not \retval ::NVAPI_OK SUCCESS
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_DestroySession = hDll.DRS_DestroySession
NvAPI_DRS_DestroySession.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_DestroySession(NvDRSSessionHandle hSession);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_LoadSettings
# not DESCRIPTION: This API loads and parses the settings data.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession Input to the session handle.
# not
# not \retval ::NVAPI_OK  SUCCESS
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_LoadSettings = hDll.DRS_LoadSettings
NvAPI_DRS_LoadSettings.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_LoadSettings(NvDRSSessionHandle hSession);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_SaveSettings
# not DESCRIPTION: This API saves the settings data to the system.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession Input to the session handle.
# not
# not \retval ::NVAPI_OK SUCCESS
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_SaveSettings = hDll.DRS_SaveSettings
NvAPI_DRS_SaveSettings.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_SaveSettings(NvDRSSessionHandle hSession);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_LoadSettingsFromFile
# not DESCRIPTION: This API loads settings from the given file path.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession Input to the session handle
# not \param [in] fileName Binary File Name/Path
# not
# not \retval ::NVAPI_OK  SUCCESS
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_LoadSettingsFromFile = hDll.DRS_LoadSettingsFromFile
NvAPI_DRS_LoadSettingsFromFile.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_LoadSettingsFromFile(NvDRSSessionHandle hSession, NvAPI_UnicodeString fileName);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_SaveSettingsToFile
# not DESCRIPTION: This API saves settings to the given file path.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession Input to the session handle.
# not \param [in] fileName Binary File Name/Path
# not
# not \retval ::NVAPI_OK  SUCCESS
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_SaveSettingsToFile = hDll.DRS_SaveSettingsToFile
NvAPI_DRS_SaveSettingsToFile.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_SaveSettingsToFile(NvDRSSessionHandle hSession, NvAPI_UnicodeString fileName);

# not @}
# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_CreateProfile
# not DESCRIPTION: This API creates an empty profile.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession  Input to the session handle.
# not \param [in] *pProfileInfo Input pointer to NVDRS_PROFILE.
# not \param [in] *phProfile Returns pointer to profile handle.
# not
# not \retval ::NVAPI_OK  SUCCESS
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_CreateProfile = hDll.DRS_CreateProfile
NvAPI_DRS_CreateProfile.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_CreateProfile(NvDRSSessionHandle hSession, NVDRS_PROFILE *pProfileInfo, NvDRSProfileHandle *phProfile);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_DeleteProfile
# not DESCRIPTION: This API deletes a profile or sets it back to a
# predefined value.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession Input to the session handle.
# not \param [in] hProfile Input profile handle.
# not
# not \retval ::NVAPI_OK  SUCCESS if the profile is found
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_DeleteProfile = hDll.DRS_DeleteProfile
NvAPI_DRS_DeleteProfile.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_DeleteProfile(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_SetCurrentGlobalProfile
# not DESCRIPTION: This API sets the current global profile in the
# driver.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession   Input to the session handle.
# not \param [in] wszGlobalProfileName Input current Global profile
# name.
# not
# not \retval ::NVAPI_OK  SUCCESS
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_SetCurrentGlobalProfile = hDll.DRS_SetCurrentGlobalProfile
NvAPI_DRS_SetCurrentGlobalProfile.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_SetCurrentGlobalProfile(NvDRSSessionHandle hSession, NvAPI_UnicodeString wszGlobalProfileName);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_GetCurrentGlobalProfile
# not DESCRIPTION: This API returns the handle to the current global
# profile.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession  Input to the session handle.
# not \param [out] *phProfile Returns current Global profile handle.
# not
# not \retval ::NVAPI_OK  SUCCESS
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_GetCurrentGlobalProfile = hDll.DRS_GetCurrentGlobalProfile
NvAPI_DRS_GetCurrentGlobalProfile.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_GetCurrentGlobalProfile(NvDRSSessionHandle hSession, NvDRSProfileHandle *phProfile);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_GetProfileInfo
# not DESCRIPTION: This API gets information about the given profile.
# User needs to specify the name of the Profile.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession  Input to the session handle.
# not \param [in] hProfile  Input profile handle.
# not \param [out] *pProfileInfo Return the profile info.
# not
# not \retval ::NVAPI_OK  SUCCESS
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_GetProfileInfo = hDll.DRS_GetProfileInfo
NvAPI_DRS_GetProfileInfo.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_GetProfileInfo(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NVDRS_PROFILE *pProfileInfo);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_SetProfileInfo
# not DESCRIPTION: Specifies flags for a given profile. Currently only
# the NVDRS_GPU_SUPPORT is
# not    used to update the profile. Neither the name, number of
# settings or applications
# not    or other profile information can be changed with this
# function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession  Input to the session handle.
# not \param [in] hProfile  Input profile handle.
# not \param [in] *pProfileInfo Input the new profile info.
# not
# not \retval ::NVAPI_OK  SUCCESS
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_SetProfileInfo = hDll.DRS_SetProfileInfo
NvAPI_DRS_SetProfileInfo.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_SetProfileInfo(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NVDRS_PROFILE *pProfileInfo);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_FindProfileByName
# not DESCRIPTION: This API finds a profile in the current session.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession Input to the session handle.
# not \param [in] profileName Input profileName.
# not \param [out] phProfile  Input profile handle.
# not
# not \retval ::NVAPI_OK   SUCCESS if the profile is found
# not \retval ::NVAPI_PROFILE_NOT_FOUND if profile is not found
# not \retval ::NVAPI_ERROR   For miscellaneous errors.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_FindProfileByName = hDll.DRS_FindProfileByName
NvAPI_DRS_FindProfileByName.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_FindProfileByName(NvDRSSessionHandle hSession, NvAPI_UnicodeString profileName, NvDRSProfileHandle* phProfile);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_EnumProfiles
# not DESCRIPTION: This API enumerates through all the profiles in the
# session.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession  Input to the session handle.
# not \param [in] index   Input the index for enumeration.
# not \param [out] *phProfile Returns profile handle.
# not
# not RETURN STATUS: NVAPI_OK: SUCCESS if the profile is found
# not    NVAPI_ERROR: For miscellaneous errors.
# not    NVAPI_END_ENUMERATION: index exceeds the total number of
# available Profiles in DB.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_EnumProfiles = hDll.DRS_EnumProfiles
NvAPI_DRS_EnumProfiles.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_EnumProfiles(NvDRSSessionHandle hSession, NvU32 index, NvDRSProfileHandle *phProfile);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_GetNumProfiles
# not DESCRIPTION: This API obtains the number of profiles in the
# current session object.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession  Input to the session handle.
# not \param out] *numProfiles Returns count of profiles in the
# current hSession.
# not
# not \retval ::NVAPI_OK   SUCCESS
# not \retval ::NVAPI_API_NOT_INTIALIZED Failed to initialize.
# not \retval ::NVAPI_INVALID_ARGUMENT Invalid Arguments.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_GetNumProfiles = hDll.DRS_GetNumProfiles
NvAPI_DRS_GetNumProfiles.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_GetNumProfiles(NvDRSSessionHandle hSession, NvU32 *numProfiles);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_CreateApplication
# not DESCRIPTION: This API adds an executable name to a profile.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession  Input to the session handle.
# not \param [in] hProfile  Input profile handle.
# not \param [in] *pApplication Input NVDRS_APPLICATION struct with
# the executable name to be added.
# not
# not \retval ::NVAPI_OK  SUCCESS
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_CreateApplication = hDll.DRS_CreateApplication
NvAPI_DRS_CreateApplication.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_CreateApplication(NvDRSSessionHandle hSession, NvDRSProfileHandle  hProfile, NVDRS_APPLICATION *pApplication);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_DeleteApplicationEx
# not DESCRIPTION: This API removes an executable from a profile.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession - Input to the session handle.
# not \param [in] hProfile - Input profile handle.
# not \param [in] *pApp  - Input all the information about the
# application to be removed.
# not
# not \retval ::NVAPI_OK SUCCESS
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# not \retval ::NVAPI_EXECUTABLE_PATH_IS_AMBIGUOUS If the path
# provided could refer to two different executables,
# not         this error will be returned.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_DeleteApplicationEx = hDll.DRS_DeleteApplicationEx
NvAPI_DRS_DeleteApplicationEx.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_DeleteApplicationEx(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NVDRS_APPLICATION *pApp);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_DeleteApplication
# not DESCRIPTION: This API removes an executable name from a profile.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSessionPARAMETERS Input to the session handle.
# not \param [in] hProfile   Input profile handle.
# not \param [in] appName   Input the executable name to be removed.
# not
# not \retval ::NVAPI_OK  SUCCESS
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# not \retval ::NVAPI_EXECUTABLE_PATH_IS_AMBIGUOUS If the path
# provided could refer to two different executables,
# not         this error will be returned
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_DeleteApplication = hDll.DRS_DeleteApplication
NvAPI_DRS_DeleteApplication.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_DeleteApplication(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NvAPI_UnicodeString appName);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_GetApplicationInfo
# not DESCRIPTION: This API gets information about the given
# application. The input application name
# not    must match exactly what the Profile has stored for the
# application.
# not    This function is better used to retrieve application
# information from a previous
# not    enumeration.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession  Input to the session handle.
# not \param [in] hProfile  Input profile handle.
# not \param [in] appName  Input application name.
# not \param [out] *pApplication Returns NVDRS_APPLICATION struct with
# all the attributes.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   If there are return error codes with specific meaning for this
# API,
# not   they are listed below.
# not \retval ::NVAPI_EXECUTABLE_PATH_IS_AMBIGUOUS The application
# name could not
# single out only one executable.
# not \retval ::NVAPI_EXECUTABLE_NOT_FOUND   No application with that
# name is found on the profile.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_GetApplicationInfo = hDll.DRS_GetApplicationInfo
NvAPI_DRS_GetApplicationInfo.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_GetApplicationInfo(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NvAPI_UnicodeString appName, NVDRS_APPLICATION *pApplication);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_EnumApplications
# not DESCRIPTION: This API enumerates all the applications in a given
# profile from the starting index to the maximum length.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession  Input to the session handle.
# not \param [in] hProfile  Input profile handle.
# not \param [in] startIndex  Indicates starting index for enumeration.
# not \param [in,out] *appCount  Input maximum length of the passed in
# arrays. Returns the actual length.
# not \param [out]  *pApplication Returns NVDRS_APPLICATION struct
# with all the attributes.
# not
# not \retval ::NVAPI_OK   SUCCESS
# not \retval ::NVAPI_ERROR  For miscellaneous errors.
# not \retval ::NVAPI_END_ENUMERATION startIndex exceeds the total
# appCount.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_EnumApplications = hDll.DRS_EnumApplications
NvAPI_DRS_EnumApplications.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_EnumApplications(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NvU32 startIndex, NvU32 *appCount, NVDRS_APPLICATION *pApplication);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_FindApplicationByName
# not DESCRIPTION: This API searches the application and the
# associated profile for the given application name.
# not    If a fully qualified path is provided, this function will
# always return the profile
# not    the driver will apply upon running the application
# (on the path provided).
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession  Input to the hSession handle
# not \param [in] appName  Input appName. For best results, provide a
# fully qualified path of the type
# not      c:/Folder1/Folder2/App.exe
# not \param [out]  *phProfile  Returns profile handle.
# not \param [in,out] *pApplication Returns NVDRS_APPLICATION struct
# pointer.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not    If there are return error codes with specific meaning for
# this API,
# not    they are listed below:
# not \retval ::NVAPI_APPLICATION_NOT_FOUND  If App not found
# not \retval ::NVAPI_EXECUTABLE_PATH_IS_AMBIGUOUS If the input
# appName was not fully qualified, this error might return in the case
# of multiple matches
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_FindApplicationByName = hDll.DRS_FindApplicationByName
NvAPI_DRS_FindApplicationByName.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_FindApplicationByName(__in NvDRSSessionHandle hSession, __in NvAPI_UnicodeString appName, __out NvDRSProfileHandle *phProfile, __inout NVDRS_APPLICATION *pApplication);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_SetSetting
# not DESCRIPTION: This API adds/modifies a setting to a profile.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession  Input to the session handle.
# not \param [in] hProfile  Input profile handle.
# not \param [in] *pSetting Input NVDRS_SETTING struct pointer.
# not
# not \retval ::NVAPI_OK  SUCCESS
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_SetSetting = hDll.DRS_SetSetting
NvAPI_DRS_SetSetting.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_SetSetting(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NVDRS_SETTING *pSetting);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_GetSetting
# not DESCRIPTION: This API gets information about the given setting.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession Input to the session handle.
# not \param [in] hProfile Input profile handle.
# not \param [in] settingId Input settingId.
# not \param [out] *pSetting Returns all the setting info
# not
# not \retval ::NVAPI_OK  SUCCESS
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_GetSetting = hDll.DRS_GetSetting
NvAPI_DRS_GetSetting.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_GetSetting(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NvU32 settingId, NVDRS_SETTING *pSetting);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_EnumSettings
# not DESCRIPTION: This API enumerates all the settings of a given
# profile from startIndex to the maximum length.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession  Input to the session handle.
# not \param [in] hProfile  Input profile handle.
# not \param [in] startIndex Indicates starting index for enumeration.
# not \param [in,out] *settingsCount Input max length of the passed in
# arrays, Returns the actual length.
# not \param [out]  *pSetting  Returns all the settings info.
# not
# not \retval ::NVAPI_OK   SUCCESS
# not \retval ::NVAPI_ERROR   For miscellaneous errors.
# not \retval ::NVAPI_END_ENUMERATION startIndex exceeds the total
# appCount.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_EnumSettings = hDll.DRS_EnumSettings
NvAPI_DRS_EnumSettings.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_EnumSettings(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NvU32 startIndex, NvU32 *settingsCount, NVDRS_SETTING *pSetting);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_EnumAvailableSettingIds
# not DESCRIPTION: This API enumerates all the Ids of all the settings
# recognized by NVAPI.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [out] pSettingIds  User-provided array of length
# *pMaxCount that NVAPI will fill with IDs.
# not \param [in,out] pMaxCount  Input max length of the passed in
# array, Returns the actual length.
# not
# not \retval ::NVAPI_OK  SUCCESS
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# not    NVAPI_END_ENUMERATION: the provided pMaxCount is not enough
# to hold all settingIds.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_EnumAvailableSettingIds = hDll.DRS_EnumAvailableSettingIds
NvAPI_DRS_EnumAvailableSettingIds.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_EnumAvailableSettingIds(NvU32 *pSettingIds, NvU32 *pMaxCount);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_EnumAvailableSettingValues
# not DESCRIPTION: This API enumerates all available setting values
# for a given setting.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] settingId  Input settingId.
# not \param [in,out] pMaxNumValues Input max length of the passed in
# arrays, Returns the actual length.
# not \param [out]  *pSettingValues Returns all available setting
# values and its count.
# not
# not \retval ::NVAPI_OK  SUCCESS
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_EnumAvailableSettingValues = hDll.DRS_EnumAvailableSettingValues
NvAPI_DRS_EnumAvailableSettingValues.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_EnumAvailableSettingValues(NvU32 settingId, NvU32 *pMaxNumValues, NVDRS_SETTING_VALUES *pSettingValues);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_GetSettingIdFromName
# not DESCRIPTION: This API gets the binary ID of a setting given the
# setting name.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] settingName Input Unicode settingName.
# not \param [out] *pSettingId Returns corresponding settingId.
# not
# not \retval ::NVAPI_OK    SUCCESS if the profile is found
# not \retval ::NVAPI_PROFILE_NOT_FOUND if profile is not found
# not \retval ::NVAPI_SETTING_NOT_FOUND if setting is not found
# not \retval ::NVAPI_ERROR   For miscellaneous errors.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_GetSettingIdFromName = hDll.DRS_GetSettingIdFromName
NvAPI_DRS_GetSettingIdFromName.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_GetSettingIdFromName(NvAPI_UnicodeString settingName, NvU32 *pSettingId);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_GetSettingNameFromId
# not DESCRIPTION: This API gets the setting name given the binary ID.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] settingId  Input settingId.
# not \param [in] *pSettingName Returns corresponding Unicode
# settingName.
# not
# not \retval ::NVAPI_OK    SUCCESS if the profile is found
# not \retval ::NVAPI_PROFILE_NOT_FOUND if profile is not found
# not \retval ::NVAPI_SETTING_NOT_FOUND if setting is not found
# not \retval ::NVAPI_ERROR   For miscellaneous errors.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_GetSettingNameFromId = hDll.DRS_GetSettingNameFromId
NvAPI_DRS_GetSettingNameFromId.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_GetSettingNameFromId(NvU32 settingId, NvAPI_UnicodeString *pSettingName);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_DeleteProfileSetting
# not DESCRIPTION: This API deletes a setting or sets it back to
# predefined value.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession  Input to the session handle.
# not \param [in] hProfile  Input profile handle.
# not \param [in] settingId   Input settingId to be deleted.
# not
# not \retval ::NVAPI_OK  SUCCESS if the profile is found
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_DeleteProfileSetting = hDll.DRS_DeleteProfileSetting
NvAPI_DRS_DeleteProfileSetting.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_DeleteProfileSetting(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NvU32 settingId);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_RestoreAllDefaults
# not DESCRIPTION: This API restores the whole system to
# predefined(default) values.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession Input to the session handle.
# not
# not \retval ::NVAPI_OK  SUCCESS if the profile is found
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_RestoreAllDefaults = hDll.DRS_RestoreAllDefaults
NvAPI_DRS_RestoreAllDefaults.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_RestoreAllDefaults(NvDRSSessionHandle hSession);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_RestoreProfileDefault
# not DESCRIPTION: This API restores the given profile to
# predefined(default) values.
# not    Any and all user specified modifications will be removed.
# not    If the whole profile was set by the user, the profile will be
# removed.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession Input to the session handle.
# not \param [in] hProfile Input profile handle.
# not
# not \retval ::NVAPI_OK   SUCCESS if the profile is found
# not \retval ::NVAPI_ERROR   For miscellaneous errors.
# not \retval ::NVAPI_PROFILE_REMOVED SUCCESS, and the hProfile is no
# longer valid.
# not \retval ::NVAPI_ERROR   For miscellaneous errors.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_RestoreProfileDefault = hDll.DRS_RestoreProfileDefault
NvAPI_DRS_RestoreProfileDefault.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_RestoreProfileDefault(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_RestoreProfileDefaultSetting
# not DESCRIPTION: This API restores the given profile setting to
# predefined(default) values.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession Input to the session handle.
# not \param [in] hProfile Input profile handle.
# not \param [in] settingId Input settingId.
# not
# not \retval ::NVAPI_OK  SUCCESS if the profile is found
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_RestoreProfileDefaultSetting = hDll.DRS_RestoreProfileDefaultSetting
NvAPI_DRS_RestoreProfileDefaultSetting.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_RestoreProfileDefaultSetting(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NvU32 settingId);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DRS_GetBaseProfile
# not DESCRIPTION: Returns the handle to the current global profile.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] hSession Input to the session handle.
# not \param [in] *phProfile Returns Base profile handle.
# not
# not \retval ::NVAPI_OK  SUCCESS if the profile is found
# not \retval ::NVAPI_ERROR For miscellaneous errors.
# not
# not \ingroup drsapi
# ///////////////////////////////////////////////////////////////////
NvAPI_DRS_GetBaseProfile = hDll.DRS_GetBaseProfile
NvAPI_DRS_GetBaseProfile.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_DRS_GetBaseProfile(NvDRSSessionHandle hSession, NvDRSProfileHandle *phProfile);


# not \addtogroup sysgeneral
# not @{
NV_CHIPSET_INFO_v4._fields_ = [

    # not < structure version
    ('version', NvU32),

    # not < Chipset vendor identification
    ('vendorId', NvU32),

    # not < Chipset device identification
    ('deviceId', NvU32),

    # not < Chipset vendor Name
    ('szVendorName', NvAPI_ShortString),

    # not < Chipset device Name
    ('szChipsetName', NvAPI_ShortString),

    # not < Chipset info flags - obsolete
    ('flags', NvU32),

    # not < Chipset subsystem vendor identification
    ('subSysVendorId', NvU32),

    # not < Chipset subsystem device identification
    ('subSysDeviceId', NvU32),

    # not < subsystem vendor Name
    ('szSubSysVendorName', NvAPI_ShortString),

    # not < Host bridge vendor identification
    ('HBvendorId', NvU32),

    # not < Host bridge device identification
    ('HBdeviceId', NvU32),

    # not < Host bridge subsystem vendor identification
    ('HBsubSysVendorId', NvU32),

    # not < Host bridge subsystem device identification
    ('HBsubSysDeviceId', NvU32),
]
NV_CHIPSET_INFO_v3._fields_ = [

    # not < structure version
    ('version', NvU32),

    # not < vendor ID
    ('vendorId', NvU32),

    # not < device ID
    ('deviceId', NvU32),

    # not < vendor Name
    ('szVendorName', NvAPI_ShortString),

    # not < device Name
    ('szChipsetName', NvAPI_ShortString),

    # not < Chipset info flags - obsolete
    ('flags', NvU32),

    # not < subsystem vendor ID
    ('subSysVendorId', NvU32),

    # not < subsystem device ID
    ('subSysDeviceId', NvU32),

    # not < subsystem vendor Name
    ('szSubSysVendorName', NvAPI_ShortString),
]


class NV_CHIPSET_INFO_FLAGS(ENUM):
    NV_CHIPSET_INFO_HYBRID = 0x00000001


NV_CHIPSET_INFO_HYBRID = NV_CHIPSET_INFO_FLAGS.NV_CHIPSET_INFO_HYBRID

NV_CHIPSET_INFO_v2._fields_ = [
    # not < structure version
    ('version', NvU32),
    # not < vendor ID
    ('vendorId', NvU32),
    # not < device ID
    ('deviceId', NvU32),
    # not < vendor Name
    ('szVendorName', NvAPI_ShortString),
    # not < device Name
    ('szChipsetName', NvAPI_ShortString),
    # not < Chipset info flags
    ('flags', NvU32),
]

NV_CHIPSET_INFO_v1._fields_ = [
    # structure version
    ('version', NvU32),
    # vendor ID
    ('vendorId', NvU32),
    # device ID
    ('deviceId', NvU32),
    # vendor Name
    ('szVendorName', NvAPI_ShortString),
    # device Name
    ('szChipsetName', NvAPI_ShortString),
]
NV_CHIPSET_INFO_VER_1 = MAKE_NVAPI_VERSION(NV_CHIPSET_INFO_v1, 1)
NV_CHIPSET_INFO_VER_2 = MAKE_NVAPI_VERSION(NV_CHIPSET_INFO_v2, 2)
NV_CHIPSET_INFO_VER_3 = MAKE_NVAPI_VERSION(NV_CHIPSET_INFO_v3, 3)
NV_CHIPSET_INFO_VER_4 = MAKE_NVAPI_VERSION(NV_CHIPSET_INFO_v4, 4)
NV_CHIPSET_INFO = NV_CHIPSET_INFO_v4
NV_CHIPSET_INFO_VER = NV_CHIPSET_INFO_VER_4

# not @}
# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_SYS_GetChipSetInfo
# not This function returns information about the system's chipset.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 95
# not
# not \retval NVAPI_INVALID_ARGUMENT   pChipSetInfo is NULL.
# not \retval NVAPI_OK     *pChipSetInfo is now set.
# not \retval NVAPI_INCOMPATIBLE_STRUCT_VERSION NV_CHIPSET_INFO
# version not compatible with driver.
# not \ingroup sysgeneral
# ///////////////////////////////////////////////////////////////////
NvAPI_SYS_GetChipSetInfo = hDll.SYS_GetChipSetInfo
NvAPI_SYS_GetChipSetInfo.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_SYS_GetChipSetInfo(NV_CHIPSET_INFO *pChipSetInfo);

# not \ingroup sysgeneral
# not Lid and dock information - used in NvAPI_GetLidDockInfo()
NV_LID_DOCK_PARAMS._fields_ = [

    # not Structure version, constructed from the macro
    # NV_LID_DOCK_PARAMS_VER
    ('version', NvU32),
    ('currentLidState', NvU32),
    ('currentDockState', NvU32),
    ('currentLidPolicy', NvU32),
    ('currentDockPolicy', NvU32),
    ('forcedLidMechanismPresent', NvU32),
    ('forcedDockMechanismPresent', NvU32),
]
# not ingroup sysgeneral
NV_LID_DOCK_PARAMS_VER = MAKE_NVAPI_VERSION(NV_LID_DOCK_PARAMS, 1)
# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GetLidDockInfo
# not DESCRIPTION: This function returns the current lid and dock
# information.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 177
# not
# not \retval ::NVAPI_OK
# not \retval ::NVAPI_ERROR
# not \retval ::NVAPI_NOT_SUPPORTED
# not \retval ::NVAPI_HANDLE_INVALIDATED
# not \retval ::NVAPI_API_NOT_INTIALIZED
# not
# not \ingroup sysgeneral
# ///////////////////////////////////////////////////////////////////
NvAPI_SYS_GetLidAndDockInfo = hDll.SYS_GetLidAndDockInfo
NvAPI_SYS_GetLidAndDockInfo.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_SYS_GetLidAndDockInfo(NV_LID_DOCK_PARAMS *pLidAndDock);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_SYS_GetDisplayIdFromGpuAndOutputId
# not DESCRIPTION:  This API converts a Physical GPU handle and output
# ID to a
# not    display ID.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  hPhysicalGpu Handle to the physical GPU
# not \param [in]  outputId  Connected display output ID on the
# not      target GPU - must only have one bit set
# not \param [out] displayId Pointer to an NvU32 which contains
# not      the display ID
# not
# not \retval ::NVAPI_OK - completed request
# not \retval ::NVAPI_API_NOT_INTIALIZED - NVAPI not initialized
# not \retval ::NVAPI_ERROR - miscellaneous error occurred
# not \retval ::NVAPI_INVALID_ARGUMENT - Invalid input parameter.
# not
# not \ingroup sysgeneral
# ///////////////////////////////////////////////////////////////////
NvAPI_SYS_GetDisplayIdFromGpuAndOutputId = hDll.SYS_GetDisplayIdFromGpuAndOutputId
NvAPI_SYS_GetDisplayIdFromGpuAndOutputId.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_SYS_GetDisplayIdFromGpuAndOutputId(NvPhysicalGpuHandle hPhysicalGpu, NvU32 outputId, NvU32* displayId);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_SYS_GetGpuAndOutputIdFromDisplayId
# not DESCRIPTION:  This API converts a display ID to a Physical GPU
# handle and output ID.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  displayId  Display ID of display to retrieve
# not      GPU and outputId for
# not \param [out] hPhysicalGpu Handle to the physical GPU
# not \param [out] outputId ) Connected display output ID on the
# not      target GPU will only have one bit set.
# not
# not \retval ::NVAPI_OK
# not \retval ::NVAPI_API_NOT_INTIALIZED
# not \retval ::NVAPI_ID_OUT_OF_RANGE The DisplayId corresponds to a
# not       display which is not within the
# not       normal outputId range.
# not \retval ::NVAPI_ERROR
# not \retval ::NVAPI_INVALID_ARGUMENT
# not
# not \ingroup sysgeneral
# ///////////////////////////////////////////////////////////////////
NvAPI_SYS_GetGpuAndOutputIdFromDisplayId = hDll.SYS_GetGpuAndOutputIdFromDisplayId
NvAPI_SYS_GetGpuAndOutputIdFromDisplayId.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_SYS_GetGpuAndOutputIdFromDisplayId(NvU32 displayId, NvPhysicalGpuHandle *hPhysicalGpu, NvU32 *outputId);

# ///////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_SYS_GetPhysicalGpuFromDisplayId
# not \code
# not DESCRIPTION:  This API retrieves the Physical GPU handle of the
# connected display
# not
# not \since Release: 313
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not PARAMETERS: displayId(IN)  - Display ID of display to retrieve
# not       GPU handle
# not    hPhysicalGpu(OUT) - Handle to the physical GPU
# not
# not RETURN STATUS:
# not    NVAPI_OK - completed request
# not    NVAPI_API_NOT_INTIALIZED - NVAPI not initialized
# not    NVAPI_ERROR - miscellaneous error occurred
# not    NVAPI_INVALID_ARGUMENT - Invalid input parameter.
# not \endcode
# not \ingroup sysgeneral
# ///////////////////////////////////////////////////////////////////
NvAPI_SYS_GetPhysicalGpuFromDisplayId = hDll.SYS_GetPhysicalGpuFromDisplayId
NvAPI_SYS_GetPhysicalGpuFromDisplayId.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_SYS_GetPhysicalGpuFromDisplayId(NvU32 displayId, NvPhysicalGpuHandle *hPhysicalGpu);
