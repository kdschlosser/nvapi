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
    
    def __init__(self, gpu, display_id):
        
        self.gpu = gpu
        self.display_id = display_id
        
    @property
    def __display_data(self):
        displayIdCount = NvU32(16)
        flags = NvU32(0)
        displayIdArray = (NV_GPU_DISPLAYIDS * 16)()
        displayIdArray[0].version = NV_GPU_DISPLAYIDS_VER

        nvStatus = NvAPI_GPU_GetConnectedDisplayIds(
            self.gpu.gpu_handle,
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


class GPU(object):
    
    def __init__(self, gpu_index, gpu_handle):
        self.gpu_index = gpu_index
        self.gpu_handle = gpu_handle
        
    def __iter__(self):
        displayIdCount = NvU32(16)
        flags = NvU32(0)
        displayIdArray = (NV_GPU_DISPLAYIDS * 16)()
        displayIdArray[0].version = NV_GPU_DISPLAYIDS_VER

        nvStatus = NvAPI_GPU_GetConnectedDisplayIds(
            self.gpu_handle,
            displayIdArray, 
            ctypes.byref(displayIdCount), 
            flags
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
    
    def __init__(self):
        InitNV()
    
    def __iter__(self):
        hNvDisplay = NvDisplayHandle()
        
        nvStatus = NvAPI_EnumNvidiaDisplayHandle(0, ctypes.byref(hNvDisplay))
        if nvStatus != NvAPI_Status.NVAPI_OK:
            raise RuntimeError("NvAPI_EnumNvidiaDisplayHandle returned error code %d" % (nvStatus,))

        gpuCount = NvU32()
        ahGPU = (NvPhysicalGpuHandle * NVAPI_MAX_PHYSICAL_GPUS)()
        # get the list of displays connected, populate the dynamic components
        nvStatus = NvAPI_EnumPhysicalGPUs(ahGPU, ctypes.byref(gpuCount))

        if NvAPI_Status.NVAPI_OK != nvStatus:
            raise RuntimeError("NvAPI_EnumPhysicalGPUs returned error code %d" % (nvStatus,))
        
        for i in range(gpuCount.value):
            yield GPU(i, ahGPU[i])
