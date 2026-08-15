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
    # NvAPI_DISP_GetTiming( __in NvU32 displayId,__in NV_TIMING_INPUT *timingInput, __out NV_TIMING *pTiming);

    # NvAPI_DISP_GetMonitorCapabilities(__in NvU32 displayId, __inout NV_MONITOR_CAPABILITIES *pMonitorCapabilities);


    # NvAPI_DISP_GetMonitorColorCapabilities(__in NvU32 displayId, __inout_ecount_part_opt(*pColorCapsCount, *pColorCapsCount) NV_MONITOR_COLOR_CAPS *pMonitorColorCapabilities, __inout NvU32 *pColorCapsCount);
    # NvAPI_DISP_EnumCustomDisplay( __in NvU32 displayId, __in NvU32 index, __inout NV_CUSTOM_DISPLAY *pCustDisp);
    # NvAPI_DISP_TryCustomDisplay( __in_ecount(count) NvU32 *pDisplayIds, __in NvU32 count, __in_ecount(count) NV_CUSTOM_DISPLAY *pCustDisp);
    # NvAPI_DISP_DeleteCustomDisplay( __in_ecount(count) NvU32 *pDisplayIds, __in NvU32 count, __in NV_CUSTOM_DISPLAY *pCustDisp);
    # NvAPI_DISP_SaveCustomDisplay( __in_ecount(count) NvU32 *pDisplayIds, __in NvU32 count, __in NvU32 isThisOutputIdOnly, __in NvU32 isThisMonitorIdOnly);
    # NvAPI_DISP_RevertCustomDisplayTrial( __in_ecount(count) NvU32* pDisplayIds, __in NvU32 count);



    # NvAPI_EnumNvidiaDisplayHandle(NvU32 thisEnum, NvDisplayHandle *pNvDispHandle);

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

    def set_source_hdr_metadata(self, metadata):
        # metadata: HdrMetadata namedtuple (or anything with the same
        # attribute names, e.g. a plain object)
        pMetadata = NV_HDR_METADATA()
        pMetadata.version = NV_HDR_METADATA_VER
        pMetadata.displayPrimary_x0 = metadata.display_primary_0.x
        pMetadata.displayPrimary_y0 = metadata.display_primary_0.y
        pMetadata.displayPrimary_x1 = metadata.display_primary_1.x
        pMetadata.displayPrimary_y1 = metadata.display_primary_1.y
        pMetadata.displayPrimary_x2 = metadata.display_primary_2.x
        pMetadata.displayPrimary_y2 = metadata.display_primary_2.y
        pMetadata.displayWhitePoint_x = metadata.white_point.x
        pMetadata.displayWhitePoint_y = metadata.white_point.y
        pMetadata.max_display_mastering_luminance = metadata.max_display_mastering_luminance
        pMetadata.min_display_mastering_luminance = metadata.min_display_mastering_luminance
        pMetadata.max_content_light_level = metadata.max_content_light_level
        pMetadata.max_frame_average_light_level = metadata.max_frame_average_light_level

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

    def set_adaptive_sync_data(self, max_frame_interval_ns=0, disable_adaptive_sync=False, disable_frame_splitting=False):
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

    def set_virtual_refresh_rate_data(self, frame_interval_us=0, refresh_rate_x1000=0, is_gaming_vrr=False):
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

    def set_dedicated_display_metadata(self, position_x=None, position_y=None, name=None):
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

    def validate_output_combination(self, outputs_mask):
        nvStatus = NvAPI_GPU_ValidateOutputCombination(self._hPhysicalGpu, NvU32(outputs_mask))
        if nvStatus == NvAPI_Status.NVAPI_INVALID_COMBINATION:
            return False
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_ValidateOutputCombination returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

        return True

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

        res = ''

        for i in range(16):
            res += chr(pBoardInfo.BoardNum[i])

        return res

    @property
    def tach_reading(self):
        pValue = NvU32()
        nvStatus = NvAPI_GPU_GetTachReading(self._hPhysicalGpu,  ctypes.byref(pValue))
        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            raise RuntimeError("NvAPI_GPU_GetTachReading returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

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

    # NvAPI_GPU_GetCurrentPstate(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_PERF_PSTATE_ID *pCurrentPstate);

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
            res += [
                {
                    'controller': NV_THERMAL_CONTROLLER.get(sensr.controller),
                    'default_minimum_temp': sensr.defaultMinTemp,
                    'default_maximum_temp': sensr.defaultMaxTemp,
                    'current_temp': sensr.currentTemp,
                    'target': NV_THERMAL_TARGET.get(sensr.target)
                }
            ]

    @property
    def clock_frequencies(self):
        # ClockType is an INPUT selector on the outer struct (one query
        # per call picks Current/Base/Boost) -- it is not a per-domain
        # output field, so getting all three means three separate calls,
        # not reading pClkFreqs.domain[i].ClockType (which doesn't exist;
        # only bIsPresent/frequency are on the per-domain struct).
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

            domains = []
            for i in range(NVAPI_MAX_GPU_PUBLIC_CLOCKS):
                domain = pClkFreqs.domain[i]
                domains += [domain.frequency if domain.bIsPresent else None]

            res[type_name] = domains

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

        return ArchitectureInfo(
            architecture=pArchInfo.architecture,
            implementation=pArchInfo.implementation,
            revision=pArchInfo.revision,
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
        # not KB, and it adds eviction/promotion accounting the older call
        # doesn't have
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
            caps_table=pCaps.capsTbl,
            lowest_nvlink_version=pCaps.lowestNvlinkVersion,
            highest_nvlink_version=pCaps.highestNvlinkVersion,
            lowest_nci_version=pCaps.lowestNciVersion,
            highest_nci_version=pCaps.highestNciVersion,
            link_mask=pCaps.linkMask,
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
                nvlink_version=info.nvlinkVersion,
                nci_version=info.nciVersion,
                nvlink_common_clock_speed_mhz=info.nvlinkCommonClockSpeedMhz,
                nvlink_link_clock_mhz=info.nvlinkLinkClockMhz,
                remote_device_uuid=bytes(info.remoteDeviceInfo.deviceUUID).hex(),
            )]

        return NVLinkStatus(
            link_mask=pStatus.linkMask,
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
        logical_gpu_info = self._logical_gpu_info
        for i in range(logical_gpu_info.physicalGpuCount):
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
                raise RuntimeError("NvAPI_GPU_GetConnectedDisplayIds returned %s (%d)" % (szDesc.value.decode('ascii', 'replace'), nvStatus))

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