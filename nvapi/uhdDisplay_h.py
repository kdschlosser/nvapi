import ctypes


class Chromaticities(ctypes.Structure):
    pass


# Copyright(c) 2016, NVIDIA CORPORATION.All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met :
# * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and / or other materials provided with the distribution.
# * Neither the name of NVIDIA CORPORATION nor the names of its
# contributors may be used to endorse or promote products derived
# from this software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES(INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
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


# Copyright(c) 2016, NVIDIA CORPORATION.All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met :
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and / or other materials provided with the distribution.
#  * Neither the name of NVIDIA CORPORATION nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES(INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


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