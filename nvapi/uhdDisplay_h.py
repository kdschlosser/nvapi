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

# Walk all the monitors and apply the requested HDR settings

from .nvapi_h import *

first = True

# Walk all the monitors and apply the requested HDR settings
def SetHdrMonitorMode(enableHDR):
    global first

    if first:
        NvAPI_Initialize()
        first = False

    hNvDisplay = NvDisplayHandle()

    # get first display handle which should work for all NVAPI calls for all GPUs
    nvStatus = NvAPI_EnumNvidiaDisplayHandle(0, ctypes.byref(hNvDisplay))
    if nvStatus != NvAPI_Status.NVAPI_OK:
        print("NvAPI_EnumNvidiaDisplayHandle returned error code %d\r\n" % (nvStatus,))
        return

    gpuCount = NvU32()
    ahGPU = (NvPhysicalGpuHandle * NVAPI_MAX_PHYSICAL_GPUS)()

    # get the list of displays connected, populate the dynamic components
    nvStatus = NvAPI_EnumPhysicalGPUs(ahGPU, ctypes.byref(gpuCount))

    if NvAPI_Status.NVAPI_OK != nvStatus:
        print("NvAPI_EnumPhysicalGPUs returned error code %d\r\n" % (nvStatus,))
        return

    for i in range(gpuCount.value):
        displayIdCount = NvU32(16)
        flags = NvU32(0)
        displayIdArray = (NV_GPU_DISPLAYIDS * 16)
        displayIdArray[0].version = NV_GPU_DISPLAYIDS_VER

        nvStatus = NvAPI_GPU_GetConnectedDisplayIds(ahGPU[i], displayIdArray, ctypes.byref(displayIdCount), flags)

        if NvAPI_Status.NVAPI_OK != nvStatus:
            szDesc = NvAPI_ShortString()
            NvAPI_GetErrorMessage(nvStatus, szDesc)
            print("NvAPI_GPU_GetConnectedDisplayIds returned %s (%d)\r\n" % (szDesc, nvStatus))


        print("Display count %d\r\n" % (displayIdCount.value,))

        for maxDisplayIndex in range(displayIdCount.value):
            print("Display tested %d\r\n" % (maxDisplayIndex,))

            hdrCapabilities = NV_HDR_CAPABILITIES()

            hdrCapabilities.version = NV_HDR_CAPABILITIES_VER

            if NvAPI_Status.NVAPI_OK != NvAPI_Disp_GetHdrCapabilities(
                displayIdArray[maxDisplayIndex].displayId, ctypes.byref(hdrCapabilities)
            ):
                szDesc = NvAPI_ShortString()
                NvAPI_GetErrorMessage(nvStatus, szDesc)
                print("NvAPI_Disp_GetHdrCapabilities returned %s (%s)\r\n" % (szDesc, nvStatus))
                continue

            if not hdrCapabilities.isST2084EotfSupported:
                continue

            print("Display %d supports ST2084 EOTF\r\n" % (maxDisplayIndex,))

            hdrColorData = NV_HDR_COLOR_DATA()

            hdrColorData.version = NV_HDR_COLOR_DATA_VER
            hdrColorData.cmd = NV_HDR_CMD_SET
            hdrColorData.static_metadata_descriptor_id = NV_STATIC_METADATA_TYPE_1

            hdrColorData.hdrMode = NV_HDR_MODE_UHDBD if enableHDR else NV_HDR_MODE_OFF

            nvStatus = NvAPI_Disp_HdrColorControl(
                displayIdArray[maxDisplayIndex].displayId,
                ctypes.byref(hdrColorData)
            )

            if NvAPI_Status.NVAPI_OK == nvStatus:
                print("NvAPI_Disp_SethdrColorData call has succeeded: ")
            else:
                szDesc = NvAPI_ShortString()
                NvAPI_GetErrorMessage(nvStatus, szDesc)
                print("NvAPI_Disp_HdrColorControl returned %s (%s)\r\n" % (szDesc, nvStatus))