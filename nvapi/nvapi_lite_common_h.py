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

import ctypes.util
import ctypes
from ctypes import POINTER
import sys

from ctypes.wintypes import BOOL, CHAR, INT,  UINT

from .utils import *


VOID = ctypes.c_void_p
NULL = None


if ctypes.sizeof(ctypes.c_void_p) == 8:
    _WIN64 = True
    _WIN32 = False
    ULONG_PTR = ctypes.c_ulonglong
else:
    _WIN32 = True
    _WIN64 = False
    ULONG_PTR = ctypes.c_ulong


def defined(macro):
    return macro is True


def load_library(lib):
    dll_path = ctypes.util.find_library(lib)
    if dll_path is not None:
        try:
            return ctypes.cdll.LoadLibrary(dll_path)
        except:
            pass


class _hDll(object):

    def __init__(self):
        self._hDll = None
        self.wrappers = []

    @property
    def hDll(self):
        return self._hDll

    @hDll.setter
    def hDll(self, obj):
        self._hDll = obj
        for wrapper in self.wrappers:
            wrapper.hDll = obj

    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]

        if self._hDll is not None:
            return getattr(self._hDll, item)

        class Wrapper(object):
            def __init__(self, name):
                self.__name__ = name
                self.__func = None
                self.hDll = None
                self.restype = None

            def __call__(self, *args, **kwargs):
                if self.__func is None:
                    if self.hDll is not None:
                        try:
                            self.__func = getattr(self.hDll, self.__name__)
                            self.__func.restype = self.restype
                        except:
                            return None
                    else:
                        raise RuntimeError(
                            'Module initilization problem function "{0}" is not available.'.format(self.__name__)
                        )

                return self.__func(*args, **kwargs)

        wrapper = Wrapper(item)
        self.wrappers += [wrapper]
        return wrapper


hDll = _hDll()


def InitNV():
    import os
    
    dll_path = os.path.dirname(__file__)
    
    if _WIN64:
        dll = 'nvapi64.dll'
    else:
        dll = 'nvapi.dll'

    hDll.hDll = load_library(os.path.join(dll_path, dll))
    
    if hDll.hDll is None:
        raise RuntimeError('Unable to locate Nvidia shared library')

    from . import nvapi_h

    nvapi_h.NvAPI_Initialize()


class _NV_RECT(ctypes.Structure):
    _pack_ = 8


NV_RECT = _NV_RECT


class NvSBox(ctypes.Structure):
    _pack_ = 8


class NvGUID(ctypes.Structure):
    _pack_ = 8


NvLUID = NvGUID


class NV_DISPLAY_DRIVER_MEMORY_INFO_V1(ctypes.Structure):
    _pack_ = 8


class NV_DISPLAY_DRIVER_MEMORY_INFO_V2(ctypes.Structure):
    _pack_ = 8


class NV_DISPLAY_DRIVER_MEMORY_INFO_V3(ctypes.Structure):
    _pack_ = 8


# Copyright 2012 NVIDIA Corporation. All rights reserved.

# NOTICE TO USER:
# | * This software is subject to NVIDIA ownership rights under U.S. and international Copyright laws.

# | * This software and the information contained herein are PROPRIETARY and CONFIDENTIAL to NVIDIA 
# | * and are being provided solely under the terms and conditions of an NVIDIA software license agreement.
# | * Otherwise, you have no rights to use or access this software in any manner.

# | * If not covered by the applicable NVIDIA software license agreement:
# | * NVIDIA MAKES NO REPRESENTATION ABOUT THE SUITABILITY OF THIS SOFTWARE FOR ANY PURPOSE.
# | * IT IS PROVIDED "AS IS" WITHOUT EXPRESS OR IMPLIED WARRANTY OF ANY KIND.
# | * NVIDIA DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, 
# | * INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY, NONINFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.
# | * IN NO EVENT SHALL NVIDIA BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL DAMAGES,
# | * OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, 
# | * NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS 
# | * SOURCE CODE.

# | * U.S. Government End Users.
# | * This software is a "commercial item" as that term is defined at 48 C.F.R. 2.101 (OCT 1995),
# | * consisting of "commercial computer software" and "commercial computer software documentation"
# | * as such terms are used in 48 C.F.R. 12.212 (SEPT 1995) and is provided to the U.S. Government only as a 
# | * commercial end item.
# | * Consistent with 48 C.F.R.12.212 and 48 C.F.R. 227.7202-1 through 227.7202-4 (JUNE 1995),
# | * all U.S. Government End Users acquire the software with only those rights set forth herein.

# | * Any use of this software in individual and commercial software must include,
# | * in the user documentation and internal comments to the code,
# | * the above Disclaimer (as applicable) and U.S. Government End Users Notice.


def __nvapi_deprecated_function(message):
    pass


def __nvapi_deprecated_datatype(_):
    return ''


NvU64 = ctypes.c_ulonglong
NvS64 = ctypes.c_longlong

NvS32 = ctypes.c_int
NvU32 = ctypes.c_ulong
temp_NvU32 = ctypes.c_ulong
NvS16 = ctypes.c_short
NvU16 = ctypes.c_ushort
NvU8 = ctypes.c_ubyte
NvS8 = ctypes.c_char
NvF32 = ctypes.c_float
   
   
# /*not Macro to convert NvU32 to NvF32.
def NvU32TONvF32(_pData):
    return NvF32(_pData)


# /*not Macro to convert NvF32 to NvU32.
def NvF32TONvU32(_pData):
    return NvU32(_pData)


# Boolean type
NvBool = NvU8
NV_TRUE = NvBool(1)
NV_FALSE = NvBool(0)


_NV_RECT._fields_ = [
    ('left', NvU32),
    ('top', NvU32),
    ('right', NvU32),
    ('bottom', NvU32),
]


glob = globals()


def NV_DECLARE_HANDLE(name):

    class Struct(ctypes.Structure):
        _fields_ = [('unused', INT)]
        _pack_ = 8

    cls = type(name + '__', (Struct,), {})

    glob.update({name + '__': cls})
    return cls
    

# not \addtogroup nvapihandles
# not NVAPI Handles - These handles are retrieved from various calls and
# passed in to others in NvAPI
# not   These are meant to be opaque types. Do not assume they correspond to
# indices, HDCs,
# not   display indexes or anything else.
# not
# not   Most handles remain valid until a display re-configuration
# (display mode set) or GPU
# not   reconfiguration (going into or out of SLI modes) occurs. If
# NVAPI_HANDLE_INVALIDATED
# not   is received by an app, it should discard all handles, and re-enumerate
# them.

# One or more physical GPUs acting in concert (SLI)
NvLogicalGpuHandle = NV_DECLARE_HANDLE('NvLogicalGpuHandle')
# A single physical GPU
NvPhysicalGpuHandle = NV_DECLARE_HANDLE('NvPhysicalGpuHandle')
# Display Device driven by NVIDIA GPU(s)
NvDisplayHandle = NV_DECLARE_HANDLE('NvDisplayHandle')
# Monitor handle
NvMonitorHandle = NV_DECLARE_HANDLE('NvMonitorHandle')
# Unattached Display Device driven by NVIDIA GPU(s)
NvUnAttachedDisplayHandle = NV_DECLARE_HANDLE('NvUnAttachedDisplayHandle')
# A handle to a Visual Computing Device
NvVisualComputingDeviceHandle = NV_DECLARE_HANDLE('NvVisualComputingDeviceHandle')
# A handle to an event registration instance
NvEventHandle = NV_DECLARE_HANDLE('NvEventHandle')
# A handle to a Host Interface Card
NvHICHandle = NV_DECLARE_HANDLE('NvHICHandle')
# A handle to a Sync device
NvGSyncDeviceHandle = NV_DECLARE_HANDLE('NvGSyncDeviceHandle')
# A handle to an SDI device
NvVioHandle = NV_DECLARE_HANDLE('NvVioHandle')
# A handle to address a single transition request
NvTransitionHandle = NV_DECLARE_HANDLE('NvTransitionHandle')
# NVIDIA HD Audio Device
NvAudioHandle = NV_DECLARE_HANDLE('NvAudioHandle')
# A handle for a 3D Vision Pro (3DVP) context
Nv3DVPContextHandle = NV_DECLARE_HANDLE('Nv3DVPContextHandle')
# A handle for a 3DVP RF transceiver
Nv3DVPTransceiverHandle = NV_DECLARE_HANDLE('Nv3DVPTransceiverHandle')
# A handle for a pair of 3DVP RF shutter glasses
Nv3DVPGlassesHandle = NV_DECLARE_HANDLE('Nv3DVPGlassesHandle')

# A stereo handle, that corresponds to the device interface
StereoHandle = POINTER(VOID)

# Unique source handle on the system
NvSourceHandle = NV_DECLARE_HANDLE('NvSourceHandle')
# Unique target handle on the system
NvTargetHandle = NV_DECLARE_HANDLE('NvTargetHandle')
# DirectX SwapChain objects
NVDX_SwapChainHandle = NV_DECLARE_HANDLE('NVDX_SwapChainHandle')

NVDX_SWAPCHAIN_NONE = NVDX_SwapChainHandle(0)
NVAPI_DEFAULT_HANDLE = 0


def NV_BIT(x):
    return 1 << x


# not @}
# not \addtogroup nvapitypes
# not @{
NVAPI_GENERIC_STRING_MAX = 4096
NVAPI_LONG_STRING_MAX = 256
NVAPI_SHORT_STRING_MAX = 64
NvSBox._fields_ = [
    ('sX', NvS32),
    ('sY', NvS32),
    ('sWidth', NvS32),
    ('sHeight', NvS32),
]


NvGUID._fields_ = [
    ('data1', NvU32),
    ('data2', NvU16),
    ('data3', NvU16),
    ('data4', NvU8 * 8),
]


# not < Maximum heads, each with NVAPI_DESKTOP_RES resolution
NV_MAX_HEADS = 4
NVAPI_MAX_HEADS_PER_GPU = 32

NVAPI_MAX_PHYSICAL_GPUS = 64
NVAPI_MAX_PHYSICAL_BRIDGES = 100
NVAPI_PHYSICAL_GPUS = 32
NVAPI_MAX_LOGICAL_GPUS = 64
NVAPI_MAX_AVAILABLE_GPU_TOPOLOGIES = 256
NVAPI_MAX_AVAILABLE_SLI_GROUPS = 256
NVAPI_MAX_GPU_TOPOLOGIES = NVAPI_MAX_PHYSICAL_GPUS
NVAPI_MAX_GPU_PER_TOPOLOGY = 8
NVAPI_MAX_DISPLAY_HEADS = 2
NVAPI_ADVANCED_DISPLAY_HEADS = 4
NVAPI_MAX_DISPLAYS = NVAPI_PHYSICAL_GPUS * NVAPI_ADVANCED_DISPLAY_HEADS
NVAPI_MAX_ACPI_IDS = 16
NVAPI_MAX_VIEW_MODES = 8
NVAPI_SYSTEM_MAX_HWBCS = 128
NVAPI_SYSTEM_HWBC_INVALID_ID = 0xFFFFFFFF
NVAPI_SYSTEM_MAX_DISPLAYS = NVAPI_MAX_PHYSICAL_GPUS * NV_MAX_HEADS

# not < Maximum number of input video streams, each with a NVAPI_VIDEO_SRC_INFO
NV_MAX_VID_STREAMS = 4

# not < Increasing MAX no. of input video streams, each with a
# NVAPI_VIDEO_SRC_INFO
NV_MAX_VID_STREAMS_EX = 20

# not < Maximum number of output video profiles supported
NV_MAX_VID_PROFILES = 4
NVAPI_MAX_AUDIO_DEVICES = 16
NvAPI_String = CHAR * NVAPI_GENERIC_STRING_MAX
NvAPI_LongString = CHAR * NVAPI_LONG_STRING_MAX
NvAPI_ShortString = CHAR * NVAPI_SHORT_STRING_MAX
NvAPI_UnicodeShortString = NvU16 * NVAPI_SHORT_STRING_MAX

# not @}
# == == == == == == == == == == == == == == == == == == == == == == == == ==
# == == == == == == == == == == == == == == == == == == == =
# not NvAPI Version Definition \n
# not Maintain per structure specific version define using the
# MAKE_NVAPI_VERSION macro. \n
# not Usage: define NV_GENLOCK_STATUS_VER
# MAKE_NVAPI_VERSION(NV_GENLOCK_STATUS, 1)
# not \ingroup nvapitypes
# == == == == == == == == == == == == == == == == == == == == == == == == ==
# == == == == == == == == == == == == == == == == == == == =
    
    
def MAKE_NVAPI_VERSION(typeName, ver):
    try:
        return NvU32(ctypes.sizeof(typeName) | (ver << 16))
    except TypeError:
        return NvU32(len(typeName.__dict__) | (ver << 16))


# not \ingroup nvapitypes
def GET_NVAPI_VERSION(ver):
    return NvU32(ver >> 16)


# not \ingroup nvapitypes
def GET_NVAPI_SIZE(ver):
    return NvU32(ver & 0xFFFF)


# == == == == == == == == == == == == == == == == == == == == == == == == == ==
# not NvAPI Status Values
# not All NvAPI functions return one of these codes.
# not \ingroup nvapistatus
# == == == == == == == == == == == == == == == == == == == == == == == == == ==
class _NvAPI_Status(ENUM):
    NVAPI_OK = EnumItem(0).set_string('OK')
    NVAPI_ERROR = EnumItem(-1).set_string('Error')
    NVAPI_LIBRARY_NOT_FOUND = EnumItem(-2).set_string('Library Not Found')
    NVAPI_NO_IMPLEMENTATION = - EnumItem(-3).set_string('No Implementation')
    NVAPI_API_NOT_INITIALIZED = EnumItem(-4).set_string('API Not Initilized')
    NVAPI_INVALID_ARGUMENT = EnumItem(-5).set_string('Invalid Argument')

    # not < No NVIDIA display driver, or NVIDIA GPU driving a display, was
    # found.
    NVAPI_NVIDIA_DEVICE_NOT_FOUND = EnumItem(-6).set_string('Nvidia Device Not Found')
    NVAPI_END_ENUMERATION = EnumItem(-7).set_string('End Enumeration')
    NVAPI_INVALID_HANDLE = EnumItem(-8).set_string('Invalid Handle')
    NVAPI_INCOMPATIBLE_STRUCT_VERSION = EnumItem(-9).set_string('Incompatible Struct Version')

    # not < The handle is no longer valid
    # (likely due to GPU or display re-configuration)
    NVAPI_HANDLE_INVALIDATED = EnumItem(-10).set_string('Handle Invalidated')
    NVAPI_OPENGL_CONTEXT_NOT_CURRENT = EnumItem(-11).set_string('Opengl Context Not Current')
    NVAPI_INVALID_POINTER = EnumItem(-14).set_string('Invalid Pointer')
    NVAPI_NO_GL_EXPERT = EnumItem(-12).set_string('No Gl Expert')

    # not < OpenGL Expert is supported, but driver instrumentation is
    # currently disabled
    NVAPI_INSTRUMENTATION_DISABLED = EnumItem(-13).set_string('Instrumentation Disabled')
    NVAPI_NO_GL_NSIGHT = EnumItem(-15).set_string('No Gl Nsight')
    NVAPI_EXPECTED_LOGICAL_GPU_HANDLE = EnumItem(-100).set_string('Expected Logical Gpu Handle')
    NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE = EnumItem(-101).set_string('Expected Physical Gpu Handle')
    NVAPI_EXPECTED_DISPLAY_HANDLE = EnumItem(-102).set_string('Expected Display Handle')
    NVAPI_INVALID_COMBINATION = EnumItem(-103).set_string('Invalid Combination')
    NVAPI_NOT_SUPPORTED = EnumItem(-104).set_string('Not Supported')
    NVAPI_PORTID_NOT_FOUND = EnumItem(-105).set_string('Portid Not Found')

    # not < Expected an unattached display handle as one of the input
    # parameters.
    NVAPI_EXPECTED_UNATTACHED_DISPLAY_HANDLE = EnumItem(-106).set_string('Expected Unattached Display Handle')
    NVAPI_INVALID_PERF_LEVEL = EnumItem(-107).set_string('Invalid Perf Level')
    NVAPI_DEVICE_BUSY = EnumItem(-108).set_string('Device Busy')
    NVAPI_NV_PERSIST_FILE_NOT_FOUND = EnumItem(-109).set_string('Nv Persist File Not Found')
    NVAPI_PERSIST_DATA_NOT_FOUND = EnumItem(-110).set_string('Persist Data Not Found')
    NVAPI_EXPECTED_TV_DISPLAY = EnumItem(-111).set_string('Expected Tv Display')
    NVAPI_EXPECTED_TV_DISPLAY_ON_DCONNECTOR = EnumItem(-112).set_string('Expected Tv Display On Dconnector')
    NVAPI_NO_ACTIVE_SLI_TOPOLOGY = EnumItem(-113).set_string('No Active Sli Topology')
    NVAPI_SLI_RENDERING_MODE_NOTALLOWED = EnumItem(-114).set_string('Sli Rendering Mode Notallowed')
    NVAPI_EXPECTED_DIGITAL_FLAT_PANEL = EnumItem(-115).set_string('Expected Digital Flat Panel')
    NVAPI_ARGUMENT_EXCEED_MAX_SIZE = EnumItem(-116).set_string('Argument Exceed Max Size')

    # not < Inhibit is ON due to one of the flags in
    # NV_GPU_DISPLAY_CHANGE_INHIBIT or SLI active.
    NVAPI_DEVICE_SWITCHING_NOT_ALLOWED = EnumItem(-117).set_string('Device Switching Not Allowed')
    NVAPI_TESTING_CLOCKS_NOT_SUPPORTED = EnumItem(-118).set_string('Testing Clocks Not Supported')
    NVAPI_UNKNOWN_UNDERSCAN_CONFIG = EnumItem(-119).set_string('Unknown Underscan Config')
    NVAPI_TIMEOUT_RECONFIGURING_GPU_TOPO = EnumItem(-120).set_string('Timeout Reconfiguring GPU Topo')
    NVAPI_DATA_NOT_FOUND = EnumItem(-121).set_string('Data Not Found')
    NVAPI_EXPECTED_ANALOG_DISPLAY = EnumItem(-122).set_string('Expected Analog Display')
    NVAPI_NO_VIDLINK = EnumItem(-123).set_string('No Vidlink')
    NVAPI_REQUIRES_REBOOT = EnumItem(-124).set_string('Requires Reboot')
    NVAPI_INVALID_HYBRID_MODE = EnumItem(-125).set_string('Invalid Hybrid Mode')
    NVAPI_MIXED_TARGET_TYPES = EnumItem(-126).set_string('Mixed Target Types')
    NVAPI_SYSWOW64_NOT_SUPPORTED = EnumItem(-127).set_string('Syswow64 Not Supported')

    # not < There is no implicit GPU topology active. Use NVAPI_SetHybridMode
    # to change topology.
    NVAPI_IMPLICIT_SET_GPU_TOPOLOGY_CHANGE_NOT_ALLOWED = EnumItem(-128).set_string('Implicit Set GPU Topology Change Not Allowed')
    NVAPI_REQUEST_USER_TO_CLOSE_NON_MIGRATABLE_APPS = EnumItem(-129).set_string('Request User To Close Non Migratable Apps')
    NVAPI_OUT_OF_MEMORY = EnumItem(-130).set_string('Out Of Memory')

    # not < The previous operation that is transferring information to or from
    # this surface is incomplete.
    NVAPI_WAS_STILL_DRAWING = EnumItem(-131).set_string('Was Still Drawing')
    NVAPI_FILE_NOT_FOUND = EnumItem(-132).set_string('File Not Found')

    # not < There are too many unique instances of a particular type of state
    # object.
    NVAPI_TOO_MANY_UNIQUE_STATE_OBJECTS = EnumItem(-133).set_string('Too Many Unique State Objects')

    # not < The method call is invalid. For example, a method's parameter may
    # not be a valid pointer.
    NVAPI_INVALID_CALL = EnumItem(-134).set_string('Invalid Call')
    NVAPI_D3D10_1_LIBRARY_NOT_FOUND = EnumItem(-135).set_string('D3D10 1 Library Not Found')
    NVAPI_FUNCTION_NOT_FOUND = EnumItem(-136).set_string('Function Not Found')

    # not < The application will require Administrator privileges to access
    # this API.
    NVAPI_INVALID_USER_PRIVILEGE = EnumItem(-137).set_string('Invalid User Privilege')
    NVAPI_EXPECTED_NON_PRIMARY_DISPLAY_HANDLE = EnumItem(-138).set_string('Expected Non Primary Display Handle')
    NVAPI_EXPECTED_COMPUTE_GPU_HANDLE = EnumItem(-139).set_string('Expected Compute GPU Handle')

    # not < The Stereo part of NVAPI failed to initialize completely. Check if
    # the stereo driver is installed.
    NVAPI_STEREO_NOT_INITIALIZED = EnumItem(-140).set_string('Stereo Not Initialized')
    NVAPI_STEREO_REGISTRY_ACCESS_FAILED = EnumItem(-141).set_string('Stereo Registry Access Failed')
    NVAPI_STEREO_REGISTRY_PROFILE_TYPE_NOT_SUPPORTED = EnumItem(-142).set_string('Stereo Registry Profile Type Not Supported')
    NVAPI_STEREO_REGISTRY_VALUE_NOT_SUPPORTED = EnumItem(-143).set_string('Stereo Registry Value Not Supported')

    # not < Stereo is not enabled and the function needed it to execute
    # completely.
    NVAPI_STEREO_NOT_ENABLED = EnumItem(-144).set_string('Stereo Not Enabled')

    # not < Stereo is not turned on and the function needed it to execute
    # completely.
    NVAPI_STEREO_NOT_TURNED_ON = EnumItem(-145).set_string('Stereo Not Turned On')
    NVAPI_STEREO_INVALID_DEVICE_INTERFACE = EnumItem(-146).set_string('Stereo Invalid Device Interface')

    # not < Separation percentage or JPEG image capture quality is out of
    # [0-100] range.
    NVAPI_STEREO_PARAMETER_OUT_OF_RANGE = EnumItem(-147).set_string('Stereo Parameter Out Of Range')
    NVAPI_STEREO_FRUSTUM_ADJUST_MODE_NOT_SUPPORTED = EnumItem(-148).set_string('Stereo Frustum Adjust Mode Not Supported')

    # not < The mosaic topology is not possible given the current state of the
    # hardware.
    NVAPI_TOPO_NOT_POSSIBLE = EnumItem(-149).set_string('Topo Not Possible')
    NVAPI_MODE_CHANGE_FAILED = EnumItem(-150).set_string('Mode Change Failed')
    NVAPI_D3D11_LIBRARY_NOT_FOUND = EnumItem(-151).set_string('D3D11 Library Not Found')
    NVAPI_INVALID_ADDRESS = EnumItem(-152).set_string('Invalid Address')
    NVAPI_STRING_TOO_SMALL = EnumItem(-153).set_string('String Too Small')
    NVAPI_MATCHING_DEVICE_NOT_FOUND = EnumItem(-154).set_string('Matching Device Not Found')
    NVAPI_DRIVER_RUNNING = EnumItem(-155).set_string('Driver Running')
    NVAPI_DRIVER_NOTRUNNING = EnumItem(-156).set_string('Driver Notrunning')
    NVAPI_ERROR_DRIVER_RELOAD_REQUIRED = EnumItem(-157).set_string('Error Driver Reload Required')
    NVAPI_SET_NOT_ALLOWED = EnumItem(-158).set_string('Set Not Allowed')
    NVAPI_ADVANCED_DISPLAY_TOPOLOGY_REQUIRED = EnumItem(-159).set_string('Advanced Display Topology Required')
    NVAPI_SETTING_NOT_FOUND = EnumItem(-160).set_string('Setting Not Found')
    NVAPI_SETTING_SIZE_TOO_LARGE = EnumItem(-161).set_string('Setting Size Too Large')
    NVAPI_TOO_MANY_SETTINGS_IN_PROFILE = EnumItem(-162).set_string('Too Many Settings In Profile')
    NVAPI_PROFILE_NOT_FOUND = EnumItem(-163).set_string('Profile Not Found')
    NVAPI_PROFILE_NAME_IN_USE = EnumItem(-164).set_string('Profile Name In Use')
    NVAPI_PROFILE_NAME_EMPTY = EnumItem(-165).set_string('Profile Name Empty')
    NVAPI_EXECUTABLE_NOT_FOUND = EnumItem(-166).set_string('Executable Not Found')
    NVAPI_EXECUTABLE_ALREADY_IN_USE = EnumItem(-167).set_string('Executable Already In Use')
    NVAPI_DATATYPE_MISMATCH = EnumItem(-168).set_string('Datatype Mismatch')

    # not < The profile passed as parameter has been removed and is no longer
    # valid.
    NVAPI_PROFILE_REMOVED = EnumItem(-169).set_string('Profile Removed')
    NVAPI_UNREGISTERED_RESOURCE = EnumItem(-170).set_string('Unregistered Resource')

    # not < The DisplayId corresponds to a display which is not within the
    # normal outputId range.
    NVAPI_ID_OUT_OF_RANGE = EnumItem(-171).set_string('Id Out Of Range')

    # not < Display topology is not valid so the driver cannot do a mode set
    # on this configuration.
    NVAPI_DISPLAYCONFIG_VALIDATION_FAILED = EnumItem(-172).set_string('Displayconfig Validation Failed')
    NVAPI_DPMST_CHANGED = EnumItem(-173).set_string('DPMST Changed')
    NVAPI_INSUFFICIENT_BUFFER = EnumItem(-174).set_string('Insufficient Buffer')
    NVAPI_ACCESS_DENIED = EnumItem(-175).set_string('Access Denied')

    # not < The requested action cannot be performed without Mosaic being
    # enabled.
    NVAPI_MOSAIC_NOT_ACTIVE = EnumItem(-176).set_string('Mosaic Not Active')
    NVAPI_SHARE_RESOURCE_RELOCATED = EnumItem(-177).set_string('Share Resource Relocated')
    NVAPI_REQUEST_USER_TO_DISABLE_DWM = EnumItem(-178).set_string('Request User To Disable Dwm')

    # not < D3D device status is D3DERR_DEVICELOST or D3DERR_DEVICENOTRESET -
    # the user has to reset the device.
    NVAPI_D3D_DEVICE_LOST = EnumItem(-179).set_string('D3D Device Lost')
    NVAPI_INVALID_CONFIGURATION = EnumItem(-180).set_string('Invalid Configuration')
    NVAPI_STEREO_HANDSHAKE_NOT_DONE = EnumItem(-181).set_string('Stereo Handshake Not Done')

    # not < The path provided was too SHORT to determine the correct
    # NVDRS_APPLICATION
    NVAPI_EXECUTABLE_PATH_IS_AMBIGUOUS = EnumItem(-182).set_string('Executable Path Is Ambiguous')
    NVAPI_DEFAULT_STEREO_PROFILE_IS_NOT_DEFINED = EnumItem(-183).set_string('Default Stereo Profile Is Not Defined')
    NVAPI_DEFAULT_STEREO_PROFILE_DOES_NOT_EXIST = EnumItem(-184).set_string('Default Stereo Profile Does Not Exist')
    NVAPI_CLUSTER_ALREADY_EXISTS = EnumItem(-185).set_string('Cluster Already Exists')

    # not < The input display id is not that of a multi stream enabled
    # connector or a display device in a multi stream topology
    NVAPI_DPMST_DISPLAY_ID_EXPECTED = EnumItem(-186).set_string('DPMST Display Id Expected')

    # not < The input display id is not valid or the monitor associated to it
    # does not support the current operation
    NVAPI_INVALID_DISPLAY_ID = EnumItem(-187).set_string('Invalid Display Id')
    NVAPI_STREAM_IS_OUT_OF_SYNC = EnumItem(-188).set_string('Stream Is Out Of Sync')
    NVAPI_INCOMPATIBLE_AUDIO_DRIVER = EnumItem(-189).set_string('Incompatible Audio Driver')
    NVAPI_VALUE_ALREADY_SET = EnumItem(-190).set_string('Value Already Set')
    NVAPI_TIMEOUT = EnumItem(-191).set_string('Timeout')

    # not < The requested workstation feature set has incomplete driver
    # internal allocation resources
    NVAPI_GPU_WORKSTATION_FEATURE_INCOMPLETE = EnumItem(-192).set_string('GPU Workstation Feature Incomplete')
    NVAPI_STEREO_INIT_ACTIVATION_NOT_DONE = EnumItem(-193).set_string('Stereo Init Activation Not Done')

    # not < The requested action cannot be performed without Sync being
    # enabled.
    NVAPI_SYNC_NOT_ACTIVE = EnumItem(-194).set_string('Sync Not Active')

    # not < The requested action cannot be performed without Sync Master being
    # enabled.
    NVAPI_SYNC_MASTER_NOT_FOUND = EnumItem(-195).set_string('Sync Master Not Found')
    NVAPI_INVALID_SYNC_TOPOLOGY = EnumItem(-196).set_string('Invalid Sync Topology')

    # not < The specified signing algorithm is not supported. Either an
    # incorrect value was entered or the current installed driver/hardware
    # does not support the input value.
    NVAPI_ECID_SIGN_ALGO_UNSUPPORTED = EnumItem(-197).set_string('ECID Sign Algo Unsupported')
    NVAPI_ECID_KEY_VERIFICATION_FAILED = EnumItem(-198).set_string('ECID Key Verification Failed')
    NVAPI_FIRMWARE_OUT_OF_DATE = EnumItem(-199).set_string('Firmware Out Of Date')
    NVAPI_FIRMWARE_REVISION_NOT_SUPPORTED = EnumItem(-200).set_string('Firmware Revision Not Supported')
    NVAPI_LICENSE_CALLER_AUTHENTICATION_FAILED = EnumItem(-201).set_string('License Caller Authentication Failed')

    # not < The user tried to use a deferred context without registering the
    # device first
    NVAPI_D3D_DEVICE_NOT_REGISTERED = EnumItem(-202).set_string('D3D Device Not Registered')

    # not < Head or SourceId was not reserved for the VR Display before doing
    # the Modeset.
    NVAPI_RESOURCE_NOT_ACQUIRED = EnumItem(-203).set_string('Resource Not Acquired')
    NVAPI_TIMING_NOT_SUPPORTED = EnumItem(-204).set_string('Timing Not Supported')

    # not < HDCP Encryption Failed for the device. Would be applicable when
    # the device is HDCP Capable.
    NVAPI_HDCP_ENCRYPTION_FAILED = EnumItem(-205).set_string('HDCP Encryption Failed')
    NVAPI_PCLK_LIMITATION_FAILED = EnumItem(-206).set_string('PCLK Limitation Failed')
    NVAPI_NO_CONNECTOR_FOUND = EnumItem(-207).set_string('No Connector Found')

    # not < When a non-HDCP capable HMD is connected, we would inform user by
    # this code.
    NVAPI_HDCP_DISABLED = EnumItem(-208).set_string('HDCP Disabled')
    NVAPI_API_IN_USE = EnumItem(-209).set_string('API In Use')
    NVAPI_NVIDIA_DISPLAY_NOT_FOUND = EnumItem(-210).set_string('Nvidia Display Not Found')
    NVAPI_PRIV_SEC_VIOLATION = EnumItem(-211).set_string('Priv Sec Violation')
    NVAPI_INCORRECT_VENDOR = EnumItem(-212).set_string('Incorrect Vendor')
    NVAPI_DISPLAY_IN_USE = EnumItem(-213).set_string('Display In Use')
    NVAPI_UNSUPPORTED_CONFIG_NON_HDCP_HMD = EnumItem(-214).set_string('Unsupported Config Non HDCP Hmd')
    NVAPI_MAX_DISPLAY_LIMIT_REACHED = EnumItem(-215).set_string('Max Display Limit Reached')
    NVAPI_INVALID_DIRECT_MODE_DISPLAY = EnumItem(-216).set_string('Invalid Direct Mode Display')
    NVAPI_GPU_IN_DEBUG_MODE = EnumItem(-217).set_string('GPU In Debug Mode')
    NVAPI_D3D_CONTEXT_NOT_FOUND = EnumItem(-218).set_string('D3D Context Not Found')
    NVAPI_STEREO_VERSION_MISMATCH = EnumItem(-219).set_string('Stereo Version Mismatch')
    NVAPI_GPU_NOT_POWERED = EnumItem(-220).set_string('GPU Not Powered')
    NVAPI_ERROR_DRIVER_RELOAD_IN_PROGRESS = EnumItem(-221).set_string('Error Driver Reload In Progress')
    NVAPI_WAIT_FOR_HW_RESOURCE = EnumItem(-222).set_string('Wait For Hw Resource')
    NVAPI_REQUIRE_FURTHER_HDCP_ACTION = EnumItem(-223).set_string('Require Further HDCP Action')
    NVAPI_DISPLAY_MUX_TRANSITION_FAILED = EnumItem(-224).set_string('Display Mux Transition Failed')


NvAPI_Status = _NvAPI_Status

NVAPI_INTERFACE = NvAPI_Status

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_SYS_GetDriverAndBranchVersion
# not DESCRIPTION: This API returns display driver version and driver-branch
# string.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [out] pDriverVersion  Contains the driver version after
# successful return.
# not \param [out] szBuildBranchString Contains the driver-branch string after
# successful return.
# not
# not \retval ::NVAPI_INVALID_ARGUMENT: either pDriverVersion is NULL or enum
# index too big
# not \retval ::NVAPI_OK - completed request
# not \retval ::NVAPI_API_NOT_INTIALIZED - NVAPI not initialized
# not \retval ::NVAPI_ERROR - miscellaneous error occurred
# not
# not \ingroup driverapi
# /////////////////////////////////////////////////////////////////////////////

# NVAPI_INTERFACE NvAPI_SYS_GetDriverAndBranchVersion(NvU32* pDriverVersion, NvAPI_ShortString szBuildBranchString);
NvAPI_SYS_GetDriverAndBranchVersion = hDll.SYS_GetDriverAndBranchVersion
NvAPI_SYS_GetDriverAndBranchVersion.restype = NVAPI_INTERFACE

# not \ingroup driverapi
# not Used in NvAPI_GPU_GetMemoryInfo().
NV_DISPLAY_DRIVER_MEMORY_INFO_V1._fields_ = [
    # not < Version info
    ('version', NvU32),
    # not < Size(in kb) of the physical framebuffer.
    ('dedicatedVideoMemory', NvU32),
    # not < Size(in kb) of the available physical framebuffer for allocating
    # video memory surfaces.
    ('availableDedicatedVideoMemory', NvU32),
    # not < Size(in kb) of system memory the driver allocates at load time.
    ('systemVideoMemory', NvU32),
    # not < Size(in kb) of shared system memory that driver is allowed to
    # commit for surfaces across all allocations.
    ('sharedSystemMemory', NvU32),
]

# not \ingroup driverapi
# not Used in NvAPI_GPU_GetMemoryInfo().
NV_DISPLAY_DRIVER_MEMORY_INFO_V2._fields_ = [
    # not < Version info
    ('version', NvU32),
    # not < Size(in kb) of the physical framebuffer.
    ('dedicatedVideoMemory', NvU32),
    # not < Size(in kb) of the available physical framebuffer for allocating
    # video memory surfaces.
    ('availableDedicatedVideoMemory', NvU32),
    # not < Size(in kb) of system memory the driver allocates at load time.
    ('systemVideoMemory', NvU32),
    # not < Size(in kb) of shared system memory that driver is allowed to
    # commit for surfaces across all allocations.
    ('sharedSystemMemory', NvU32),
    # not < Size(in kb) of the current available physical framebuffer for
    # allocating video memory surfaces.
    ('curAvailableDedicatedVideoMemory', NvU32),
]


# not \ingroup driverapi
# not Used in NvAPI_GPU_GetMemoryInfo().
NV_DISPLAY_DRIVER_MEMORY_INFO_V3._fields_ = [
    # not < Version info
    ('version', NvU32),
    # not < Size(in kb) of the physical framebuffer.
    ('dedicatedVideoMemory', NvU32),
    # not < Size(in kb) of the available physical framebuffer for allocating
    # video memory surfaces.
    ('availableDedicatedVideoMemory', NvU32),
    # not < Size(in kb) of system memory the driver allocates at load time.
    ('systemVideoMemory', NvU32),
    # not < Size(in kb) of shared system memory that driver is allowed to
    # commit for surfaces across all allocations.
    ('sharedSystemMemory', NvU32),
    # not < Size(in kb) of the current available physical framebuffer for
    # allocating video memory surfaces.
    ('curAvailableDedicatedVideoMemory', NvU32),
    # not < Size(in kb) of the total size of memory released as a result of
    # the evictions.
    ('dedicatedVideoMemoryEvictionsSize', NvU32),
    # not < Indicates the number of eviction events that caused an allocation
    # to be removed from dedicated video memory to free GPU
    ('dedicatedVideoMemoryEvictionCount', NvU32),
]

# not \ingroup driverapi
NV_DISPLAY_DRIVER_MEMORY_INFO = NV_DISPLAY_DRIVER_MEMORY_INFO_V3

# not \ingroup driverapi
# not Macro for constructing the version field of
# NV_DISPLAY_DRIVER_MEMORY_INFO_V1
NV_DISPLAY_DRIVER_MEMORY_INFO_VER_1 = (
    MAKE_NVAPI_VERSION(NV_DISPLAY_DRIVER_MEMORY_INFO_V1, 1)
)

# not \ingroup driverapi
# not Macro for constructing the version field of
# NV_DISPLAY_DRIVER_MEMORY_INFO_V2
NV_DISPLAY_DRIVER_MEMORY_INFO_VER_2 = (
    MAKE_NVAPI_VERSION(NV_DISPLAY_DRIVER_MEMORY_INFO_V2, 2)
)

# not \ingroup driverapi
# not Macro for constructing the version field of
# NV_DISPLAY_DRIVER_MEMORY_INFO_V3
NV_DISPLAY_DRIVER_MEMORY_INFO_VER_3 = (
    MAKE_NVAPI_VERSION(NV_DISPLAY_DRIVER_MEMORY_INFO_V3, 3)
)

# not \ingroup driverapi
NV_DISPLAY_DRIVER_MEMORY_INFO_VER = NV_DISPLAY_DRIVER_MEMORY_INFO_VER_3

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_GPU_GetMemoryInfo
# not DESCRIPTION: This function retrieves the available driver memory
# footprint for the specified GPU.
# not    If the GPU is in TCC Mode, only dedicatedVideoMemory will be returned
# in pMemoryInfo (NV_DISPLAY_DRIVER_MEMORY_INFO).
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not TCC_SUPPORTED
# not
# not \since Release: 177
# not
# not \param [in] hPhysicalGpu Handle of the physical GPU for which the memory
# information is to be extracted.
# not \param [out] pMemoryInfo The memory footprint available in the driver.
# See NV_DISPLAY_DRIVER_MEMORY_INFO.
# not
# not \retval  NVAPI_INVALID_ARGUMENT   pMemoryInfo is NULL.
# not \retval  NVAPI_OK     Call successful.
# not \retval  NVAPI_NVIDIA_DEVICE_NOT_FOUND No NVIDIA GPU driving a display
# was found.
# not \retval  NVAPI_INCOMPATIBLE_STRUCT_VERSION NV_DISPLAY_DRIVER_MEMORY_INFO
# structure version mismatch.
# not
# not \ingroup driverapi
# /////////////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_GPU_GetMemoryInfo(NvPhysicalGpuHandle hPhysicalGpu, NV_DISPLAY_DRIVER_MEMORY_INFO *pMemoryInfo);
NvAPI_GPU_GetMemoryInfo = hDll.GPU_GetMemoryInfo
NvAPI_GPU_GetMemoryInfo.restype = NVAPI_INTERFACE

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_EnumPhysicalGPUs
# not This function returns an array of physical GPU handles.
# not Each handle represents a physical GPU present in the system.
# not That GPU may be part of an SLI configuration, or may not be visible to
# the OS directly.
# not
# not At least one GPU must be present in the system and running an NVIDIA
# display driver.
# not
# not The array nvGPUHandle will be filled with physical GPU handle values.
# The returned
# not gpuCount determines how many entries in the array are valid.
# not
# not \note In drivers older than 105.00, all physical GPU handles get
# invalidated on a
# not  modeset. So the calling applications need to renum the handles after
# every modeset.\n
# not  With drivers 105.00 and up, all physical GPU handles are constant.
# not  Physical GPU handles are constant as LONG as the GPUs are not
# physically moved and
# not  the SBIOS VGA order is unchanged.
# not
# not  For GPU handles in TCC MODE please use NvAPI_EnumTCCPhysicalGPUs()
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \par Introduced in
# not \since Release: 80
# not
# not \retval NVAPI_INVALID_ARGUMENT  nvGPUHandle or pGpuCount is NULL
# not \retval NVAPI_OK     One or more handles were returned
# not \retval NVAPI_NVIDIA_DEVICE_NOT_FOUND No NVIDIA GPU driving a display
# was found
# not \ingroup gpu
# /////////////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_EnumPhysicalGPUs(NvPhysicalGpuHandle nvGPUHandle[NVAPI_MAX_PHYSICAL_GPUS], NvU32 *pGpuCount);
NvAPI_EnumPhysicalGPUs = hDll.EnumPhysicalGPUs
NvAPI_EnumPhysicalGPUs.restype = NVAPI_INTERFACE

# DX Objects#
#
NVDX_ObjectHandle = NV_DECLARE_HANDLE('NVDX_ObjectHandle')
NVDX_OBJECT_NONE = NVDX_ObjectHandle(0)

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_GetObjectHandleForResource
# not DESCRIPTION: This API gets a handle to a resource.
# not
# not \param [in] pDev  The ID3D11Device, ID3D10Device or IDirect3DDevice9
# or ID3D11DeviceContext to use
# not \param [in] pResource The ID3D11Resource, ID3D10Resource or
# IDirect3DResource9 from which
# not     we want the NvAPI handle
# not \param [out] pHandle A handle to the resource
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 185
# not
# not \return ::NVAPI_OK if the handle was populated.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////////

# NVAPI_INTERFACE NvAPI_D3D_GetObjectHandleForResource(
#     IUnknown *pDevice,
#     IUnknown *pResource,
#     NVDX_ObjectHandle *pHandle);
NvAPI_D3D_GetObjectHandleForResource = hDll.D3D_GetObjectHandleForResource
NvAPI_D3D_GetObjectHandleForResource.restype = NVAPI_INTERFACE
