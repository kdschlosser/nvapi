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
import ctypes
import six
from collections import namedtuple


class Chromaticities(ctypes.Structure):
    pass


# Interface for setting UHD metadata
Chromaticities._fields_ = [
    ('red_x', float),
    ('red_y', float),
    ('green_x', float),
    ('green_y', float),
    ('blue_x', float),
    ('blue_y', float),
    ('wp_x', float),
    ('wp_y', float),
]


ColorCoordinates = namedtuple('ColorCoordinates', ['red', 'green', 'blue', 'white'])
RedCoordinate = namedtuple('RedCoordinate', ['x', 'y'])
GreenCoordinate = namedtuple('RedCoordinate', ['x', 'y'])
BlueCoordinate = namedtuple('RedCoordinate', ['x', 'y'])
WhiteCoordinate = namedtuple('RedCoordinate', ['x', 'y'])


class Display(object):
    # NvAPI_GPU_GetEDID(NvPhysicalGpuHandle hPhysicalGpu, NvU32 displayOutputId, NV_EDID *pEDID);
    # NvAPI_GPU_SetEDID(NvPhysicalGpuHandle hPhysicalGpu, NvU32 displayOutputId, NV_EDID *pEDID);

    # NvAPI_GPU_GetScanoutConfiguration(NvU32 displayId, NvSBox* desktopRect, NvSBox* scanoutRect);
    # NvAPI_GPU_GetScanoutCompositionParameter(__in NvU32 displayId, __in NV_GPU_SCANOUT_COMPOSITION_PARAMETER parameter, __out NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE *parameterData, __out float *pContainer);
    # NvAPI_GPU_GetScanoutConfigurationEx(__in NvU32 displayId, __inout NV_SCANOUT_INFORMATION *pScanoutInformation);
    # NvAPI_GPU_SetScanoutIntensity(NvU32 displayId, NV_SCANOUT_INTENSITY_DATA* scanoutIntensityData, int *pbSticky);
    # NvAPI_GPU_GetScanoutIntensityState(__in NvU32 displayId, __inout NV_SCANOUT_INTENSITY_STATE_DATA* scanoutIntensityStateData);
    # NvAPI_GPU_SetScanoutWarping(NvU32 displayId, NV_SCANOUT_WARPING_DATA* scanoutWarpingData, int* piMaxNumVertices, int* pbSticky);
    # NvAPI_GPU_GetScanoutWarpingState(__in NvU32 displayId, __inout NV_SCANOUT_WARPING_STATE_DATA* scanoutWarpingStateData);
    # NvAPI_GPU_SetScanoutCompositionParameter(NvU32 displayId, NV_GPU_SCANOUT_COMPOSITION_PARAMETER parameter,NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE parameterValue, float *pContainer);

    # NvAPI_Disp_InfoFrameControl(__in NvU32 displayId, __inout NV_INFOFRAME_DATA *pInfoframeData);
    # NvAPI_Disp_ColorControl(NvU32 displayId, NV_COLOR_DATA *pColorData);
    # NvAPI_Disp_GetHdrCapabilities(__in NvU32 displayId, __inout NV_HDR_CAPABILITIES *pHdrCapabilities);
    # NvAPI_Disp_HdrColorControl(__in NvU32 displayId, __inout NV_HDR_COLOR_DATA *pHdrColorData);
    # NvAPI_DISP_GetTiming( __in NvU32 displayId,__in NV_TIMING_INPUT *timingInput, __out NV_TIMING *pTiming);
    # NvAPI_DISP_GetMonitorCapabilities(__in NvU32 displayId, __inout NV_MONITOR_CAPABILITIES *pMonitorCapabilities);
    # NvAPI_DISP_GetMonitorColorCapabilities(__in NvU32 displayId, __inout_ecount_part_opt(*pColorCapsCount, *pColorCapsCount) NV_MONITOR_COLOR_CAPS *pMonitorColorCapabilities, __inout NvU32 *pColorCapsCount);
    # NvAPI_DISP_EnumCustomDisplay( __in NvU32 displayId, __in NvU32 index, __inout NV_CUSTOM_DISPLAY *pCustDisp);
    # NvAPI_DISP_TryCustomDisplay( __in_ecount(count) NvU32 *pDisplayIds, __in NvU32 count, __in_ecount(count) NV_CUSTOM_DISPLAY *pCustDisp);
    # NvAPI_DISP_DeleteCustomDisplay( __in_ecount(count) NvU32 *pDisplayIds, __in NvU32 count, __in NV_CUSTOM_DISPLAY *pCustDisp);
    # NvAPI_DISP_SaveCustomDisplay( __in_ecount(count) NvU32 *pDisplayIds, __in NvU32 count, __in NvU32 isThisOutputIdOnly, __in NvU32 isThisMonitorIdOnly);
    # NvAPI_DISP_RevertCustomDisplayTrial( __in_ecount(count) NvU32* pDisplayIds, __in NvU32 count);



    # NvAPI_EnumNvidiaDisplayHandle(NvU32 thisEnum, NvDisplayHandle *pNvDispHandle);
    # NvAPI_EnumNvidiaUnAttachedDisplayHandle(NvU32 thisEnum, NvUnAttachedDisplayHandle *pNvUnAttachedDispHandle);
    # NvAPI_CreateDisplayFromUnAttachedDisplay(NvUnAttachedDisplayHandle hNvUnAttachedDisp, NvDisplayHandle *pNvDisplay);
    # NvAPI_GetAssociatedNvidiaDisplayHandle(const char *szDisplayName, NvDisplayHandle *pNvDispHandle);
    # NvAPI_DISP_GetAssociatedUnAttachedNvidiaDisplayHandle(const char *szDisplayName, NvUnAttachedDisplayHandle *pNvUnAttachedDispHandle);
    # NvAPI_GetAssociatedNvidiaDisplayName(NvDisplayHandle NvDispHandle, NvAPI_ShortString szDisplayName);
    # NvAPI_GetUnAttachedAssociatedDisplayName(NvUnAttachedDisplayHandle hNvUnAttachedDisp, NvAPI_ShortString szDisplayName);
    # NvAPI_EnableHWCursor(NvDisplayHandle hNvDisplay);
    # NvAPI_DisableHWCursor(NvDisplayHandle hNvDisplay);
    # NvAPI_GetVBlankCounter(NvDisplayHandle hNvDisplay, NvU32 *pCounter);
    # NvAPI_SetRefreshRateOverride(NvDisplayHandle hNvDisplay, NvU32 outputsMask, float refreshRate, NvU32 bSetDeferred);
    # NvAPI_GetAssociatedDisplayOutputId(NvDisplayHandle hNvDisplay, NvU32 *pOutputId);
    # NvAPI_GetDisplayPortInfo(__in_opt NvDisplayHandle hNvDisplay, __in NvU32 outputId, __inout NV_DISPLAY_PORT_INFO *pInfo);
    # NvAPI_SetDisplayPort(NvDisplayHandle hNvDisplay, NvU32 outputId, NV_DISPLAY_PORT_CONFIG *pCfg);
    # NvAPI_GetHDMISupportInfo(__in_opt NvDisplayHandle hNvDisplay, __in NvU32 outputId, __inout NV_HDMI_SUPPORT_INFO *pInfo);

    # NvAPI_DISP_GetDisplayConfig(__inout NvU32 *pathInfoCount, __out_ecount_full_opt(*pathInfoCount) NV_DISPLAYCONFIG_PATH_INFO *pathInfo);
    # NvAPI_DISP_SetDisplayConfig(__in NvU32 pathInfoCount, __in_ecount(pathInfoCount) NV_DISPLAYCONFIG_PATH_INFO* pathInfo, __in NvU32 flags);
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
            raise RuntimeError("NvAPI_DISP_GetGDIPrimaryDisplayId returned %s (%d)" % (szDesc, nvStatus))

        return self.display_id.value == displayId.value

    @property
    def _hPhysicalGpu(self):
        hPhysicalGpu = NvPhysicalGpuHandle()
        nvStatus = NvAPI_SYS_GetPhysicalGpuFromDisplayId(self.display_id, ctypes.byref(hPhysicalGpu))

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_SYS_GetPhysicalGpuFromDisplayId returned %s (%d)" % (szDesc, nvStatus))

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
            raise RuntimeError("NvAPI_GPU_GetConnectedDisplayIds returned %s (%d)" % (szDesc, nvStatus))

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
            raise RuntimeError("NvAPI_Disp_GetHdrCapabilities returned %s (%d)" % (szDesc, nvStatus))

        return hdrCapabilities

    def enable_hdr(self, flag):
        if self.is_hdr_supported:
            hdrColorData = NV_HDR_COLOR_DATA()

            hdrColorData.version = NV_HDR_COLOR_DATA_VER
            hdrColorData.cmd = NV_HDR_CMD_SET
            hdrColorData.static_metadata_descriptor_id = NV_STATIC_METADATA_TYPE_1

            if flag:
                hdrColorData.hdrMode = NV_HDR_MODE_UHDBD
            else:
                hdrColorData.hdrMode = NV_HDR_MODE_OFF

            nvStatus = NvAPI_Disp_HdrColorControl(
                self.display_id,
                ctypes.byref(hdrColorData)
            )

            if NvAPI_Status.NVAPI_OK != nvStatus:
                szDesc = NvAPI_ShortString()
                NvAPI_GetErrorMessage(nvStatus, szDesc)
                raise RuntimeError("NvAPI_Disp_HdrColorControl returned %s (%d)" % (szDesc, nvStatus))

    @property
    def connector_type(self):
        dd = self.__display_data
        
        connector_mapping = {
            NV_MONITOR_CONN_TYPE_UNINITIALIZED: 'Uninitilized', 
            NV_MONITOR_CONN_TYPE_VGA: 'VGA',
            NV_MONITOR_CONN_TYPE_COMPONENT: 'Component',
            NV_MONITOR_CONN_TYPE_SVIDEO: 'SVideo',
            NV_MONITOR_CONN_TYPE_HDMI: 'HDMI',
            NV_MONITOR_CONN_TYPE_DVI: 'DVI',
            NV_MONITOR_CONN_TYPE_LVDS: 'LVDS (Laptop)',
            NV_MONITOR_CONN_TYPE_DP: 'DisplayPort',
            NV_MONITOR_CONN_TYPE_COMPOSITE: 'Composite',
            NV_MONITOR_CONN_TYPE_UNKNOWN: 'Unknown'
        }
        return connector_mapping[dd.connectorType]
    
    @property
    def is_dynamic(self):
        dd = self.__display_data
        return bool(dd.isDynamic)    
    
    @property
    def is_multi_stream_root_node(self):
        dd = self.__display_data
        return bool(dd.isMultiStreamRootNode)
        
    @property
    def is_active(self):
        dd = self.__display_data
        return bool(dd.isActive)

    @property
    def is_cluster(self):
        dd = self.__display_data
        return bool(dd.isCluster)
    
    @property
    def is_visible(self):
        dd = self.__display_data
        return bool(dd.isOSVisible)
    
    @property
    def is_wireless_display(self):
        dd = self.__display_data
        return bool(dd.isWFD)
    
    @property
    def is_connected(self):
        dd = self.__display_data
        return bool(dd.isConnected)

    @property
    def is_physically_connected(self):
        dd = self.__display_data
        return bool(dd.isConnected) and bool(dd.isPhysicallyConnected)

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
    def primary_color_coordinates(self):
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

    @property
    def maximum_hdr_luminance(self):
        # Maximum display luminance = desired max luminance of HDR
        # content ([0x0001-0xFFFF] = [1.0 - 65535.0] cd/m^2)
        dd = self.__hdr_data.display_data
        return dd.desired_content_max_luminance

    @property
    def minimum_hdr_luminance(self):
        # Minimum display luminance = desired min luminance of HDR
        # content ([0x0001-0xFFFF] = [1.0 - 6.55350] cd/m^2)
        dd = self.__hdr_data.display_data
        return dd.desired_content_min_luminance

    @property
    def maximum_frame_average_hdr_luminance(self):
        # Desired maximum Frame-Average Light Level (MaxFALL) of HDR
        # content ([0x0001-0xFFFF] = [1.0 - 65535.0] cd/m^2)
        dd = self.__hdr_data.display_data
        return dd.desired_content_max_frame_average_luminance

    @property
    def supports_2160p60hz(self):
        # If set sink is capable of 4kx2k @ 60hz
        dvsm = self.__hdr_data.dv_static_metadata
        return bool(dvsm.supports_2160p60hz)

    @property
    def supports_yuv422_12bit(self):
        # If set, sink is capable of YUV422-12 bit
        dvsm = self.__hdr_data.dv_static_metadata
        return bool(dvsm.supports_YUV422_12bit)

    @property
    def supports_global_dimming(self):
        # Indicates if sink supports global dimming
        dvsm = self.__hdr_data.dv_static_metadata
        return bool(dvsm.supports_global_dimming)

    @property
    def colorimetry(self):
        # If set indicates sink supports DCI P3 colorimetry, REc709 otherwise
        dvsm = self.__hdr_data.dv_static_metadata
        if bool(dvsm.colorimetry):
            return 'DCI P3'
        else:
            return 'REc709'

    @property
    def supports_backlight_control(self):
        # This is set when sink is using lowlatency interface and can control its backlight.
        dvsm = self.__hdr_data.dv_static_metadata
        return bool(dvsm.supports_backlight_control)

    @property
    def backlight_minimum(self):
        # It is the level for Backlt min luminance value.
        dvsm = self.__hdr_data.dv_static_metadata
        return dvsm.backlt_min_luma

    @property
    def interface_supported_by_sink(self):
        # Indicates the interface (standard or low latency) supported by the sink.
        dvsm = self.__hdr_data.dv_static_metadata
        return dvsm.interface_supported_by_sink

    @property
    def supports_10b_12b_444(self):
        # It is set when interface supported is low latency,
        # it tells whether it supports 10 bit or 12 bit RGB 4:4:4 or YCbCr 4:4:4 or both.
        dvsm = self.__hdr_data.dv_static_metadata
        return dvsm.supports_10b_12b_444

    @property
    def minimum_sink_luminance(self):
        # Represents min luminance level of Sink
        dvsm = self.__hdr_data.dv_static_metadata
        return dvsm.target_min_luminance

    @property
    def maximum_sink_luminance(self):
        # Represents max luminance level of sink
        dvsm = self.__hdr_data.dv_static_metadata
        return dvsm.target_max_luminance

    @property
    def primary_chromaticity_coordinates(self):
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


def _get_bit(byteval, idx):
    return byteval & (1 << idx) != 0


class PhysicalGPU(object):
    @property
    def _hdcp_support_status(self):
        pGetHDCPSupportStatus = NV_GPU_GET_HDCP_SUPPORT_STATUS()
        nvStatus = NvAPI_GPU_GetHDCPSupportStatus(self._hPhysicalGpu,  ctypes.byref(pGetHDCPSupportStatus))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetHDCPSupportStatus returned %s (%d)" % (szDesc, nvStatus))

        return pGetHDCPSupportStatus

    @property
    def hdcp_fuse_state(self):
        state_mapping = {
            NV_GPU_HDCP_FUSE_STATE.NV_GPU_HDCP_FUSE_STATE_DISABLED: 'Disabled',
            NV_GPU_HDCP_FUSE_STATE.NV_GPU_HDCP_FUSE_STATE_ENABLED: 'Enabled',
            NV_GPU_HDCP_FUSE_STATE.NV_GPU_HDCP_FUSE_STATE_UNKNOWN: 'Unknown'
        }
        return state_mapping[self._hdcp_support_status.hdcpFuseState]

    @property
    def hdcp_key_source(self):
        source_mapping = {
            NV_GPU_HDCP_KEY_SOURCE.NV_GPU_HDCP_KEY_SOURCE_CRYPTO_ROM: 'Crypto Rom',
            NV_GPU_HDCP_KEY_SOURCE.NV_GPU_HDCP_KEY_SOURCE_FUSES: 'Fuses',
            NV_GPU_HDCP_KEY_SOURCE.NV_GPU_HDCP_KEY_SOURCE_I2C_ROM: 'I2C Rom',
            NV_GPU_HDCP_KEY_SOURCE.NV_GPU_HDCP_KEY_SOURCE_NONE: 'None',
            NV_GPU_HDCP_KEY_SOURCE.NV_GPU_HDCP_KEY_SOURCE_SBIOS: 'SBios',
            NV_GPU_HDCP_KEY_SOURCE.NV_GPU_HDCP_KEY_SOURCE_UNKNOWN: 'Unknown'
        }
        return source_mapping[self._hdcp_support_status.hdcpKeySource]

    @property
    def hdcp_key_source_state(self):
        state_mapping = {
            NV_GPU_HDCP_KEY_SOURCE_STATE.NV_GPU_HDCP_KEY_SOURCE_STATE_PRESENT: 'Present',
            NV_GPU_HDCP_KEY_SOURCE_STATE.NV_GPU_HDCP_KEY_SOURCE_STATE_ABSENT: 'Absent',
            NV_GPU_HDCP_KEY_SOURCE_STATE.NV_GPU_HDCP_KEY_SOURCE_STATE_UNKNOWN: 'Unknown'
        }
        return state_mapping[self._hdcp_support_status.hdcpKeySourceState]

    @property
    def shader_sub_pipe_count(self):
        hPhysicalGpu = self._hPhysicalGpu
        pCount = NvU32()
        nvStatus = NvAPI_GPU_GetShaderSubPipeCount(hPhysicalGpu, ctypes.byref(pCount))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetShaderSubPipeCount returned %s (%d)" % (szDesc, nvStatus))

        return pCount.value

    @property
    def core_count(self):
        hPhysicalGpu = self._hPhysicalGpu
        pCount = NvU32()
        nvStatus = NvAPI_GPU_GetGpuCoreCount(hPhysicalGpu, ctypes.byref(pCount))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetGpuCoreCount returned %s (%d)" % (szDesc, nvStatus))

        return pCount.value

    # NvAPI_GPU_GetAllOutputs(NvPhysicalGpuHandle hPhysicalGpu,NvU32 *pOutputsMask);
    # NvAPI_GPU_GetConnectedOutputs(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pOutputsMask);
    # NvAPI_GPU_GetConnectedSLIOutputs(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pOutputsMask);
    # NvAPI_GPU_GetConnectedOutputsWithLidState(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pOutputsMask);
    # NvAPI_GPU_GetConnectedSLIOutputsWithLidState(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pOutputsMask);

    @property
    def system_type(self):
        system_mapping = {
            NV_SYSTEM_TYPE.NV_SYSTEM_TYPE_DESKTOP: 'Desktop',
            NV_SYSTEM_TYPE.NV_SYSTEM_TYPE_LAPTOP: 'Laptop',
            NV_SYSTEM_TYPE.NV_SYSTEM_TYPE_UNKNOWN: 'Unknown'
        }

        pSystemType = NV_SYSTEM_TYPE()
        nvStatus = NvAPI_GPU_GetSystemType(self._hPhysicalGpu,  ctypes.byref(pSystemType))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetConnectedDisplayIds returned %s (%d)" % (szDesc, nvStatus))

        return system_mapping[pSystemType]

    # NvAPI_GPU_GetActiveOutputs(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pOutputsMask);
    # NvAPI_GPU_GetOutputType(NvPhysicalGpuHandle hPhysicalGpu, NvU32 outputId, NV_GPU_OUTPUT_TYPE *pOutputType);
    # NvAPI_GPU_ValidateOutputCombination(NvPhysicalGpuHandle hPhysicalGpu, NvU32 outputsMask);
    # NvAPI_GPU_GetFullName(NvPhysicalGpuHandle hPhysicalGpu, NvAPI_ShortString szName);

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
            raise RuntimeError("NvAPI_GPU_GetPCIIdentifiers returned %s (%d)" % (szDesc, nvStatus))

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
            raise RuntimeError("NvAPI_GPU_GetGPUType returned %s (%d)" % (szDesc, nvStatus))

        gpu_mapping = {
            NV_GPU_TYPE.NV_SYSTEM_TYPE_DGPU: 'DGPU',
            NV_GPU_TYPE.NV_SYSTEM_TYPE_GPU_UNKNOWN: 'Unknown',
            NV_GPU_TYPE.NV_SYSTEM_TYPE_IGPU: 'IGPU'
        }

        return gpu_mapping[pGpuType]

    @property
    def bus_type(self):
        pBusType = NV_GPU_BUS_TYPE()
        nvStatus = NvAPI_GPU_GetBusType(self._hPhysicalGpu, ctypes.byref(pBusType))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetBusType returned %s (%d)" % (szDesc, nvStatus))

        bus_type_mapping = {
            NV_GPU_BUS_TYPE.NVAPI_GPU_BUS_TYPE_UNDEFINED: 'Undefined',
            NV_GPU_BUS_TYPE.NVAPI_GPU_BUS_TYPE_PCI: 'PCI',
            NV_GPU_BUS_TYPE.NVAPI_GPU_BUS_TYPE_AGP: 'AGP',
            NV_GPU_BUS_TYPE.NVAPI_GPU_BUS_TYPE_PCI_EXPRESS: 'PCIe',
            NV_GPU_BUS_TYPE.NVAPI_GPU_BUS_TYPE_FPCI: 'FPCI',
            NV_GPU_BUS_TYPE.NVAPI_GPU_BUS_TYPE_AXI: 'AXI'
        }
        return bus_type_mapping[pBusType]

    @property
    def bus_id(self):
        pBusId = NvU32()
        nvStatus = NvAPI_GPU_GetBusId(self._hPhysicalGpu, ctypes.byref(pBusId))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetBusId returned %s (%d)" % (szDesc, nvStatus))

        return pBusId.value

    @property
    def bus_slot_id(self):
        pBusSlotId = NvU32()
        nvStatus = NvAPI_GPU_GetTachReading(self._hPhysicalGpu, ctypes.byref(pBusSlotId))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetTachReading returned %s (%d)" % (szDesc, nvStatus))

        return pBusSlotId.value

    @property
    def irq(self):
        pIRQ = NvU32()
        nvStatus = NvAPI_GPU_GetIRQ(self._hPhysicalGpu, ctypes.byref(pIRQ))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetIRQ returned %s (%d)" % (szDesc, nvStatus))

        return pIRQ.value

    @property
    def vbios_revision(self):
        pBiosRevision = NvU32()
        nvStatus = NvAPI_GPU_GetVbiosRevision(self._hPhysicalGpu, ctypes.byref(pBiosRevision))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetVbiosRevision returned %s (%d)" % (szDesc, nvStatus))
        return pBiosRevision.value

    @property
    def oem_vbios_revision(self):
        # (NvPhysicalGpuHandle hPhysicalGpu,NvU32 *);
        pBiosRevision = NvU32()
        nvStatus = NvAPI_GPU_GetVbiosOEMRevision(self._hPhysicalGpu, ctypes.byref(pBiosRevision))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetVbiosOEMRevision returned %s (%d)" % (szDesc, nvStatus))

        return pBiosRevision.value

    @property
    def vbios_version(self):
        szBiosRevision = NvAPI_ShortString()
        nvStatus = NvAPI_GPU_GetVbiosVersionString(self._hPhysicalGpu, szBiosRevision)

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetVbiosVersionString returned %s (%d)" % (szDesc, nvStatus))

        return szBiosRevision.value

    @property
    def agp_aperture(self):
        # (NvPhysicalGpuHandle hPhysicalGpu,NvU32 *);
        pSize = NvU32()
        nvStatus = NvAPI_GPU_GetAGPAperture(self._hPhysicalGpu, ctypes.byref(pSize))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetAGPAperture returned %s (%d)" % (szDesc, nvStatus))

        return pSize.value

    @property
    def current_agp_rate(self):
        pRate = NvU32()
        nvStatus = NvAPI_GPU_GetCurrentAGPRate(self._hPhysicalGpu, ctypes.byref(pRate))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetCurrentAGPRate returned %s (%d)" % (szDesc, nvStatus))

        return pRate.value

    @property
    def current_pcie_downstream_width(self):
        pWidth = NvU32()
        nvStatus = NvAPI_GPU_GetCurrentPCIEDownstreamWidth(self._hPhysicalGpu, ctypes.byref(pWidth))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetCurrentPCIEDownstreamWidth returned %s (%d)" % (szDesc, nvStatus))

        return pWidth.value

    @property
    def physical_frame_buffer_size(self):
        pSize = NvU32()
        nvStatus = NvAPI_GPU_GetPhysicalFrameBufferSize(self._hPhysicalGpu, ctypes.byref(pSize))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetPhysicalFrameBufferSize returned %s (%d)" % (szDesc, nvStatus))

        return pSize.value

    @property
    def virtual_frame_buffer_size(self):
        pSize = NvU32()
        nvStatus = NvAPI_GPU_GetVirtualFrameBufferSize(self._hPhysicalGpu, ctypes.byref(pSize))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetVirtualFrameBufferSize returned %s (%d)" % (szDesc, nvStatus))

        return pSize.value

    @property
    def quadro_status(self):
        pStatus = NvU32()
        nvStatus = NvAPI_GPU_GetQuadroStatus(self._hPhysicalGPU, ctypes.byref(pStatus))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetQuadroStatus returned %s (%d)" % (szDesc, nvStatus))

        return 'Quadro' if pStatus.value else 'GeForce'

    @property
    def serial_number(self):
        pBoardInfo = NV_BOARD_INFO()
        nvStatus = NvAPI_GPU_GetBoardInfo(self._hPhysicalGpu, ctypes.byref(pBoardInfo))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetBoardInfo returned %s (%d)" % (szDesc, nvStatus))

        res = ''

        for i in range(16):
            res += chr(pBoardInfo.BoardNum[i].value)

        return res

    @property
    def tach_reading(self):
        pValue = NvU32()
        nvStatus = NvAPI_GPU_GetTachReading(self._hPhysicalGpu,  ctypes.byref(pValue))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetTachReading returned %s (%d)" % (szDesc, nvStatus))

        return pValue.value

    # NvAPI_I2CRead(NvPhysicalGpuHandle hPhysicalGpu, NV_I2C_INFO *pI2cInfo);
    # NvAPI_I2CWrite(NvPhysicalGpuHandle hPhysicalGpu, NV_I2C_INFO *pI2cInfo);

    # NvAPI_GPU_WorkstationFeatureSetup(__in NvPhysicalGpuHandle hPhysicalGpu, __in NvU32 featureEnableMask, __in NvU32 featureDisableMask);
    # NvAPI_GPU_WorkstationFeatureQuery(__in NvPhysicalGpuHandle hPhysicalGpu, __out_opt NvU32 *pConfiguredFeatureMask, __out_opt NvU32 *pConsistentFeatureMask);
    # NvAPI_GPU_GetECCStatusInfo(NvPhysicalGpuHandle hPhysicalGpu,NV_GPU_ECC_STATUS_INFO *pECCStatusInfo);
    # NvAPI_GPU_GetECCErrorInfo(NvPhysicalGpuHandle hPhysicalGpu,NV_GPU_ECC_ERROR_INFO *pECCErrorInfo);
    # NvAPI_GPU_ResetECCErrorInfo(NvPhysicalGpuHandle hPhysicalGpu, NvU8 bResetCurrent,NvU8 bResetAggregate);
    # NvAPI_GPU_GetECCConfigurationInfo(NvPhysicalGpuHandle hPhysicalGpu,NV_GPU_ECC_CONFIGURATION_INFO *pECCConfigurationInfo);
    # NvAPI_GPU_SetECCConfiguration(NvPhysicalGpuHandle hPhysicalGpu, NvU8 bEnable,NvU8 bEnableImmediately);
    # NvAPI_GPU_QueryWorkstationFeatureSupport(NvPhysicalGpuHandle physicalGpu, NV_GPU_WORKSTATION_FEATURE_TYPE gpuWorkstationFeature);
    # NvAPI_GPU_GetPerfDecreaseInfo(__in NvPhysicalGpuHandle hPhysicalGpu, __inout NvU32 *pPerfDecrInfo);

    @property
    def performance_monitor(self):
        pPerfPstatesInfo = NV_GPU_PERF_PSTATES_INFO()
        inputFlags = NvU32()
        nvStatus = NvAPI_GPU_GetPstatesInfoEx(self._hPhysicalGpu,  ctypes.byref(pPerfPstatesInfo),  inputFlags)
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetPstatesInfoEx returned %s (%d)" % (szDesc, nvStatus))

        pPstatesInfo = NV_GPU_PERF_PSTATES20_INFO()
        NvAPI_GPU_GetPstates20(self._hPhysicalGpu, ctypes.byref(pPstatesInfo))

        res = {}

        if _get_bit(pPerfPstatesInfo.flags.value, 0):

            for i in range(pPerfPstatesInfo.numPstates.value):
                pstate = pPerfPstatesInfo.pstates[i]
                state_info = pPstatesInfo.pstates[i]

                ps = {'clocks': [], 'voltages': []}
                res[pstate.pstateId] = ps

                if _get_bit(pstate.flags, 0):
                    ps['pcie_limit'] = 'GEN2'
                else:
                    ps['pcie_limit'] = 'GEN1'

                for j in range(pPerfPstatesInfo.numClocks.value):
                    clock = pstate.clocks[j]
                    state_info_clock = state_info.clocks[j]
                    clock_type_mapping = {
                        NVAPI_GPU_PERF_PSTATE20_CLOCK_TYPE_SINGLE: 'Single',
                        NVAPI_GPU_PERF_PSTATE20_CLOCK_TYPE_RANGE: 'Range'
                    }

                    type_id = clock_type_mapping[clock.typeId]


                    clock_id_mapping = {
                        NV_GPU_PUBLIC_CLOCK_ID.NVAPI_GPU_PUBLIC_CLOCK_GRAPHICS: 'Graphics',
                        NV_GPU_PUBLIC_CLOCK_ID.NVAPI_GPU_PUBLIC_CLOCK_MEMORY: 'Memory',
                        NV_GPU_PUBLIC_CLOCK_ID.NVAPI_GPU_PUBLIC_CLOCK_PROCESSOR: 'Processor',
                        NV_GPU_PUBLIC_CLOCK_ID.NVAPI_GPU_PUBLIC_CLOCK_VIDEO: 'Video',
                        NV_GPU_PUBLIC_CLOCK_ID.NVAPI_GPU_PUBLIC_CLOCK_UNDEFINED: 'Undefined'
                    }

                    data = {
                        'type': clock_id_mapping[clock.domainId],
                        'info_type': type_id,
                        'freq_delta_khz': state_info_clock.freqDelta_kHz.value.value,
                        'freq_delta_maximum_khz': state_info_clock.freqDelta_kHz.valueRange.max.value,
                        'freq_delta_minimum_khz': state_info_clock.freqDelta_kHz.valueRange.min.value,
                        'can_overclock': _get_bit(clock.flags.value, 0),
                        'freq_khz': clock.freq.value
                    }

                    if type_id == 'Single':
                        data['freq_khz'] = state_info_clock.data.single.freq_kHz.value
                    else:
                        data['minimum_freq_khz'] = state_info_clock.data.range.minFreq_kHz.value
                        data['maximum_freq_khz'] = state_info_clock.data.range.maxFreq_kHz.value
                        data['minimum_voltage'] = state_info_clock.data.range.minVoltage_uV.value
                        data['maximum_voltage'] = state_info_clock.data.range.maxVoltage_uV.value

                    ps['clocks'] += [data]

                for j in range(pPerfPstatesInfo.numVoltages.value):
                    voltage = pstate.voltages[j]
                    base_voltage = state_info.baseVoltages[j]

                    voltage_id_mapping = {
                        NV_GPU_PERF_VOLTAGE_INFO_DOMAIN_ID.NVAPI_GPU_PERF_VOLTAGE_INFO_DOMAIN_CORE: 'Core',
                        NV_GPU_PERF_VOLTAGE_INFO_DOMAIN_ID.NVAPI_GPU_PERF_VOLTAGE_INFO_DOMAIN_UNDEFINED: 'Undefined'
                    }

                    ps['voltages'] += [
                        {
                            'type': voltage_id_mapping[voltage.domainId],
                            'mvolt': voltage.mvolt.value,
                            'volt': base_voltage.volt_uV.value,
                            'volt_delta': base_voltage.voltDelta_uV.value.value,
                            'volt_delta_maximum': base_voltage.voltDelta_uV.valueRange.max.value,
                            'volt_delta_minimum': base_voltage.voltDelta_uV.valueRange.min.value
                        }
                    ]

            pDynamicPstatesInfoEx = NV_GPU_DYNAMIC_PSTATES_INFO_EX()
            NvAPI_GPU_GetDynamicPstatesInfoEx(self._hPhysicalGpu,  ctypes.byref(pDynamicPstatesInfoEx))
            res['utilization'] = []
            if _get_bit(pDynamicPstatesInfoEx.flags.value, 0):
                for i in range(NVAPI_MAX_GPU_UTILIZATIONS):
                    util = pDynamicPstatesInfoEx.utilization[i]
                    if util.bIsPresent.value:
                        res['utilization'] += [util.percentage.value]
                    else:
                        res['utilization'] += [None]

        # TODO: pPstatesInfo.ov

        return res

    # NvAPI_GPU_GetCurrentPstate(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_PERF_PSTATE_ID *pCurrentPstate);

    @property
    def thermal_sensors(self):
        sensorIndex = NvU32(NVAPI_THERMAL_TARGET_ALL)
        pThermalSettings = NV_GPU_THERMAL_SETTINGS()
        nvStatus = NvAPI_GPU_GetThermalSettings(self._hPhysicalGpu, sensorIndex,  ctypes.byref(pThermalSettings))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetThermalSettings returned %s (%d)" % (szDesc, nvStatus))

        res = []

        target_mapping = {
            NVAPI_THERMAL_TARGET_NONE: 'None',
            NVAPI_THERMAL_TARGET_GPU: 'GPU',
            NVAPI_THERMAL_TARGET_MEMORY: 'Memory',
            NVAPI_THERMAL_TARGET_POWER_SUPPLY: 'Power Supply',
            NVAPI_THERMAL_TARGET_BOARD: 'Board',
            NVAPI_THERMAL_TARGET_VCD_BOARD: 'VCD Board',
            NVAPI_THERMAL_TARGET_VCD_INLET: 'VCD Inlet',
            NVAPI_THERMAL_TARGET_VCD_OUTLET: 'VCD Outlet',
            NVAPI_THERMAL_TARGET_ALL: 'All',
            NVAPI_THERMAL_TARGET_UNKNOWN: 'Unknown'
        }

        controller_mapping = {
            NVAPI_THERMAL_CONTROLLER_NONE: 'None',
            NVAPI_THERMAL_CONTROLLER_GPU_INTERNAL: 'GPU Internal',
            NVAPI_THERMAL_CONTROLLER_ADM1032: 'ADM1032',
            NVAPI_THERMAL_CONTROLLER_MAX6649: 'MAX6649',
            NVAPI_THERMAL_CONTROLLER_MAX1617: 'MAX1617',
            NVAPI_THERMAL_CONTROLLER_LM99: 'LM99',
            NVAPI_THERMAL_CONTROLLER_LM89: 'LM89',
            NVAPI_THERMAL_CONTROLLER_LM64: 'LM64',
            NVAPI_THERMAL_CONTROLLER_ADT7473: 'ADT7473',
            NVAPI_THERMAL_CONTROLLER_SBMAX6649: 'SBMAX6649',
            NVAPI_THERMAL_CONTROLLER_VBIOSEVT: 'VBIOSEVT',
            NVAPI_THERMAL_CONTROLLER_OS: 'OS',
            NVAPI_THERMAL_CONTROLLER_UNKNOWN: 'Unknown'
        }

        for i in range(pThermalSettings.count.value):
            sensr = pThermalSettings.sensor[i]
            res += [
                {
                    'controller': controller_mapping[sensr.controller],
                    'default_minimum_temp': sensr.defaultMinTemp.value,
                    'default_maximum_temp': sensr.defaultMaxTemp.value,
                    'current_temp': sensr.currentTemp.value,
                    'target': target_mapping[sensr.target]
                }
            ]

    @property
    def clock_frequencies(self):
        pClkFreqs = NV_GPU_CLOCK_FREQUENCIES()
        nvStatus = NvAPI_GPU_GetAllClockFrequencies(self._hPhysicalGPU,  ctypes.byref(pClkFreqs))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetThermalSettings returned %s (%d)" % (szDesc, nvStatus))

        res = []

        clock_type_mapping = {
            NV_GPU_CLOCK_FREQUENCIES_CURRENT_FREQ: 'Current',
            NV_GPU_CLOCK_FREQUENCIES_BASE_CLOCK: 'Base',
            NV_GPU_CLOCK_FREQUENCIES_BOOST_CLOCK:'Boost',
            NV_GPU_CLOCK_FREQUENCIES_CLOCK_TYPE_NUM: 'Num'
        }

        for i in range(NVAPI_MAX_GPU_PUBLIC_CLOCKS):
            dmain = pClkFreqs.domain[i]

            if dmain.bIsPresent.value:
                freq = dmain.frequency.value
            else:
                freq = None

            res += [
                {
                    'frequency': freq,
                    'type': clock_type_mapping[domain.ClockType.value]
                }
            ]

        return res

    # NvAPI_GPU_ClientIllumDevicesGetInfo(__in NvPhysicalGpuHandle hPhysicalGpu, __inout NV_GPU_CLIENT_ILLUM_DEVICE_INFO_PARAMS *pIllumDevicesInfo);
    # NvAPI_GPU_ClientIllumDevicesGetControl(__in NvPhysicalGpuHandle hPhysicalGpu, __inout NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_PARAMS *pClientIllumDevicesControl);
    # NvAPI_GPU_ClientIllumDevicesSetControl(__in NvPhysicalGpuHandle hPhysicalGpu, __inout NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_PARAMS *pClientIllumDevicesControl);
    # NvAPI_GPU_ClientIllumZonesGetInfo(__in NvPhysicalGpuHandle hPhysicalGpu, __inout NV_GPU_CLIENT_ILLUM_ZONE_INFO_PARAMS *pIllumZonesInfo);
    # NvAPI_GPU_ClientIllumZonesGetControl(__in NvPhysicalGpuHandle hPhysicalGpu, __inout NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_PARAMS *pIllumZonesControl);
    # NvAPI_GPU_ClientIllumZonesSetControl(__in NvPhysicalGpuHandle hPhysicalGpu, __inout NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_PARAMS *pIllumZonesControl);

    def __init__(self, logical_gpu, physical_gpu_index):
        self.logical_gpu = logical_gpu
        self.physical_gpu_index = physical_gpu_index

    @property
    def dedicated_memory(self):
        # Size(in kb) of the physical framebuffer.
        return self._memory_info.dedicatedVideoMemory.value

    @property
    def available_dedicated_memory(self):
        # Size(in kb) of the available physical framebuffer for allocating
        # video memory surfaces.
        return self._memory_info.availableDedicatedVideoMemory.value

    @property
    def system_memory(self):
        # Size(in kb) of system memory the driver allocates at load time.
        return self._memory_info.systemVideoMemory.value

    @property
    def shared_system_memory(self):
        # Size(in kb) of shared system memory that driver is allowed to
        # commit for surfaces across all allocations.
        return self._memory_info.sharedSystemMemory.value

    @property
    def current_available_dedicated_memory(self):
        # Size(in kb) of the current available physical framebuffer for
        # allocating video memory surfaces.
        return self._memory_info.curAvailableDedicatedVideoMemory.value

    @property
    def dedicated_memory_eviction_size(self):
        # Size(in kb) of the total size of memory released as a result of
        # the evictions.
        return self._memory_info.dedicatedVideoMemoryEvictionsSize.value

    @property
    def dedicated_memory_eviction_count(self):
        # Indicates the number of eviction events that caused an allocation
        # to be removed from dedicated video memory to free GPU
        return self._memory_info.dedicatedVideoMemoryEvictionCount.value

    @property
    def _hPhysicalGpu(self):
        return self.logical_gpu._logical_gpu_info.physicalGpuHandles[self.physical_gpu_index]

    @property
    def _memory_info(self):
        hPhysicalGpu = self._hPhysicalGpu
        pMemoryInfo = NV_DISPLAY_DRIVER_MEMORY_INFO()

        nvStatus = NvAPI_GPU_GetMemoryInfo(hPhysicalGpu, ctypes.byref(pMemoryInfo))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetMemoryInfo returned %s (%d)" % (szDesc, nvStatus))


class LogicalGPU(object):

    @property
    def _pLogicalGPU(self):
        thisEnum = NvU32(self.gpu_index)
        hNvDisplay = NvDisplayHandle()
        nvStatus = NvAPI_EnumNvidiaDisplayHandle(thisEnum, ctypes.byref(hNvDisplay))

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_EnumNvidiaDisplayHandle returned %s (%d)" % (szDesc, nvStatus))

        pLogicalGPU = NvLogicalGpuHandle()

        nvStatus = NvAPI_GetLogicalGPUFromDisplay(
            hNvDisplay,
            ctypes.byref(pLogicalGPU)
        )

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GetLogicalGPUFromDisplay returned %s (%d)" % (szDesc, nvStatus))

        return pLogicalGPU

    def __len__(self):
        return

    @property
    def physical_gpus(self):
        for i in range(self._logical_gpu_info.physicalGpuCount.value):
            yield PhysicalGPU(self, i)

    @property
    def _logical_gpu_info(self):
        pLogicalGpuData = NV_LOGICAL_GPU_DATA()
        nvStatus = NvAPI_GPU_GetLogicalGpuInfo(
            self._pLogicalGPU,
            ctypes.byref(pLogicalGpuData)
        )

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetLogicalGpuInfo returned %s (%d)" % (szDesc, nvStatus))

        return pLogicalGpuData

    @property
    def os_adpater_id(self):
        return self._logical_gpu_info.pOSAdapterId.value

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
        logical_gpu_info = self._logical_gpu_info
        for i in range(logical_gpu_info.physicalGpuCount.value):
            hPhysicalGpu = logical_gpu_info.physicalGpuHandles[i]

            displayIdCount = NvU32(16)
            displayIdArray = (NV_GPU_DISPLAYIDS * 16)()
            displayIdArray[0].version = NV_GPU_DISPLAYIDS_VER

            nvStatus = NvAPI_GPU_GetAllDisplayIds(
                hPhysicalGpu,
                displayIdArray,
                ctypes.byref(displayIdCount),
            )

            if NvAPI_Status.NVAPI_OK != nvStatus:
                szDesc = NvAPI_ShortString()
                NvAPI_GetErrorMessage(nvStatus, szDesc)
                raise RuntimeError("NvAPI_GPU_GetConnectedDisplayIds returned %s (%d)" % (szDesc, nvStatus))

            for i in range(displayIdCount.value):
                yield Display(self, displayIdArray[i].displayId)


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
    # NvAPI_GetInterfaceVersionString(NvAPI_ShortString szDesc);
    # NvAPI_SYS_GetChipSetInfo(NV_CHIPSET_INFO *pChipSetInfo);
    # NvAPI_SYS_GetLidAndDockInfo(NV_LID_DOCK_PARAMS *pLidAndDock);

    # NvAPI_GPU_QueryIlluminationSupport(__inout NV_GPU_QUERY_ILLUMINATION_SUPPORT_PARM *pIlluminationSupportInfo);
    # NvAPI_GPU_GetIllumination(NV_GPU_GET_ILLUMINATION_PARM *pIlluminationInfo);
    # NvAPI_GPU_SetIllumination(NV_GPU_SET_ILLUMINATION_PARM *pIlluminationInfo);


    # NvAPI_Stereo_Enable(void);
    # NvAPI_Stereo_Disable(void);
    # NvAPI_Stereo_IsEnabled(NvU8 *pIsStereoEnabled);

    # NvAPI_Stereo_IsWindowedModeSupported(NvU8* bSupported);
    # NvAPI_Stereo_SetDriverMode( NV_STEREO_DRIVER_MODE mode );
    def __init__(self):
        InitNV()
    
    def __iter__(self):
        count = 0
        hNvDisplay = NvDisplayHandle()
        nvStatus = NvAPI_EnumNvidiaDisplayHandle(NvU32(count), ctypes.byref(hNvDisplay))

        while nvStatus == NvAPI_Status.NVAPI_OK:
            pLogicalGPU = NvLogicalGpuHandle()
            if NvAPI_GetLogicalGPUFromDisplay(
                    hNvDisplay,
                    ctypes.byref(pLogicalGPU)
            ) == NvAPI_Status.NVAPI_OK:

                yield LogicalGPU(count)

            count += 1
            nvStatus = NvAPI_EnumNvidiaDisplayHandle(NvU32(count), ctypes.byref(hNvDisplay))

        if nvStatus != NvAPI_Status.NVAPI_END_ENUMERATION:
            raise RuntimeError("NvAPI_EnumNvidiaDisplayHandle returned error code %d" % (nvStatus,))