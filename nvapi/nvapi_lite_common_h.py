import ctypes.util
import ctypes
from ctypes import POINTER
import sys

from ctypes.wintypes import BOOL, CHAR, INT,  UINT


VOID = ctypes.c_void_p
NULL = None

NVAPI_INTERFACE = INT


class ENUM(INT):
    pass


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

            def __call__(self, *args, **kwargs):
                if self.__func is None:
                    if self.hDll is not None:
                        self.__func = getattr(self.hDll, self.__name__)
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
    for lib in ('atiadlxx.dll', 'atiadlxy.dll'):
        hDll.hDll = load_library(lib)
        if hDll.hDll is not None:
            break
    else:
        hDll.hDll = None

    if hDll.hDll is None:
        raise RuntimeError('Unable to locate Nvidia shared library')


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
    print message


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
    namespace = {
        '_fields_': [('unused', INT)],
        '_pack_': 8
    }
    
    cls = type(name + '__', (ctypes.Structure,), namespace)

    glob.update({name + '__': cls})
    return POINTER(cls)
    

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
    return NvU32(ctypes.sizeof(typeName) | (ver << 16))


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
    NVAPI_OK = 0
    NVAPI_ERROR = - 1
    NVAPI_LIBRARY_NOT_FOUND = - 2
    NVAPI_NO_IMPLEMENTATION = - 3
    NVAPI_API_NOT_INITIALIZED = - 4
    NVAPI_INVALID_ARGUMENT = - 5

    # not < No NVIDIA display driver, or NVIDIA GPU driving a display, was
    # found.
    NVAPI_NVIDIA_DEVICE_NOT_FOUND = - 6
    NVAPI_END_ENUMERATION = - 7
    NVAPI_INVALID_HANDLE = - 8
    NVAPI_INCOMPATIBLE_STRUCT_VERSION = - 9

    # not < The handle is no longer valid
    # (likely due to GPU or display re-configuration)
    NVAPI_HANDLE_INVALIDATED = - 10
    NVAPI_OPENGL_CONTEXT_NOT_CURRENT = - 11
    NVAPI_INVALID_POINTER = - 14
    NVAPI_NO_GL_EXPERT = - 12

    # not < OpenGL Expert is supported, but driver instrumentation is
    # currently disabled
    NVAPI_INSTRUMENTATION_DISABLED = - 13
    NVAPI_NO_GL_NSIGHT = - 15
    NVAPI_EXPECTED_LOGICAL_GPU_HANDLE = - 100
    NVAPI_EXPECTED_PHYSICAL_GPU_HANDLE = - 101
    NVAPI_EXPECTED_DISPLAY_HANDLE = - 102
    NVAPI_INVALID_COMBINATION = - 103
    NVAPI_NOT_SUPPORTED = - 104
    NVAPI_PORTID_NOT_FOUND = - 105

    # not < Expected an unattached display handle as one of the input
    # parameters.
    NVAPI_EXPECTED_UNATTACHED_DISPLAY_HANDLE = - 106
    NVAPI_INVALID_PERF_LEVEL = - 107
    NVAPI_DEVICE_BUSY = - 108
    NVAPI_NV_PERSIST_FILE_NOT_FOUND = - 109
    NVAPI_PERSIST_DATA_NOT_FOUND = - 110
    NVAPI_EXPECTED_TV_DISPLAY = - 111
    NVAPI_EXPECTED_TV_DISPLAY_ON_DCONNECTOR = - 112
    NVAPI_NO_ACTIVE_SLI_TOPOLOGY = - 113
    NVAPI_SLI_RENDERING_MODE_NOTALLOWED = - 114
    NVAPI_EXPECTED_DIGITAL_FLAT_PANEL = - 115
    NVAPI_ARGUMENT_EXCEED_MAX_SIZE = - 116

    # not < Inhibit is ON due to one of the flags in
    # NV_GPU_DISPLAY_CHANGE_INHIBIT or SLI active.
    NVAPI_DEVICE_SWITCHING_NOT_ALLOWED = - 117
    NVAPI_TESTING_CLOCKS_NOT_SUPPORTED = - 118
    NVAPI_UNKNOWN_UNDERSCAN_CONFIG = - 119
    NVAPI_TIMEOUT_RECONFIGURING_GPU_TOPO = - 120
    NVAPI_DATA_NOT_FOUND = - 121
    NVAPI_EXPECTED_ANALOG_DISPLAY = - 122
    NVAPI_NO_VIDLINK = - 123
    NVAPI_REQUIRES_REBOOT = - 124
    NVAPI_INVALID_HYBRID_MODE = - 125
    NVAPI_MIXED_TARGET_TYPES = - 126
    NVAPI_SYSWOW64_NOT_SUPPORTED = - 127

    # not < There is no implicit GPU topology active. Use NVAPI_SetHybridMode
    # to change topology.
    NVAPI_IMPLICIT_SET_GPU_TOPOLOGY_CHANGE_NOT_ALLOWED = - 128
    NVAPI_REQUEST_USER_TO_CLOSE_NON_MIGRATABLE_APPS = - 129
    NVAPI_OUT_OF_MEMORY = - 130

    # not < The previous operation that is transferring information to or from
    # this surface is incomplete.
    NVAPI_WAS_STILL_DRAWING = - 131
    NVAPI_FILE_NOT_FOUND = - 132

    # not < There are too many unique instances of a particular type of state
    # object.
    NVAPI_TOO_MANY_UNIQUE_STATE_OBJECTS = - 133

    # not < The method call is invalid. For example, a method's parameter may
    # not be a valid pointer.
    NVAPI_INVALID_CALL = - 134
    NVAPI_D3D10_1_LIBRARY_NOT_FOUND = - 135
    NVAPI_FUNCTION_NOT_FOUND = - 136

    # not < The application will require Administrator privileges to access
    # this API.
    NVAPI_INVALID_USER_PRIVILEGE = - 137
    NVAPI_EXPECTED_NON_PRIMARY_DISPLAY_HANDLE = - 138
    NVAPI_EXPECTED_COMPUTE_GPU_HANDLE = - 139

    # not < The Stereo part of NVAPI failed to initialize completely. Check if
    # the stereo driver is installed.
    NVAPI_STEREO_NOT_INITIALIZED = - 140
    NVAPI_STEREO_REGISTRY_ACCESS_FAILED = - 141
    NVAPI_STEREO_REGISTRY_PROFILE_TYPE_NOT_SUPPORTED = - 142
    NVAPI_STEREO_REGISTRY_VALUE_NOT_SUPPORTED = - 143

    # not < Stereo is not enabled and the function needed it to execute
    # completely.
    NVAPI_STEREO_NOT_ENABLED = - 144

    # not < Stereo is not turned on and the function needed it to execute
    # completely.
    NVAPI_STEREO_NOT_TURNED_ON = - 145
    NVAPI_STEREO_INVALID_DEVICE_INTERFACE = - 146

    # not < Separation percentage or JPEG image capture quality is out of
    # [0-100] range.
    NVAPI_STEREO_PARAMETER_OUT_OF_RANGE = - 147
    NVAPI_STEREO_FRUSTUM_ADJUST_MODE_NOT_SUPPORTED = - 148

    # not < The mosaic topology is not possible given the current state of the
    # hardware.
    NVAPI_TOPO_NOT_POSSIBLE = - 149
    NVAPI_MODE_CHANGE_FAILED = - 150
    NVAPI_D3D11_LIBRARY_NOT_FOUND = - 151
    NVAPI_INVALID_ADDRESS = - 152
    NVAPI_STRING_TOO_SMALL = - 153
    NVAPI_MATCHING_DEVICE_NOT_FOUND = - 154
    NVAPI_DRIVER_RUNNING = - 155
    NVAPI_DRIVER_NOTRUNNING = - 156
    NVAPI_ERROR_DRIVER_RELOAD_REQUIRED = - 157
    NVAPI_SET_NOT_ALLOWED = - 158
    NVAPI_ADVANCED_DISPLAY_TOPOLOGY_REQUIRED = - 159
    NVAPI_SETTING_NOT_FOUND = - 160
    NVAPI_SETTING_SIZE_TOO_LARGE = - 161
    NVAPI_TOO_MANY_SETTINGS_IN_PROFILE = - 162
    NVAPI_PROFILE_NOT_FOUND = - 163
    NVAPI_PROFILE_NAME_IN_USE = - 164
    NVAPI_PROFILE_NAME_EMPTY = - 165
    NVAPI_EXECUTABLE_NOT_FOUND = - 166
    NVAPI_EXECUTABLE_ALREADY_IN_USE = - 167
    NVAPI_DATATYPE_MISMATCH = - 168

    # not < The profile passed as parameter has been removed and is no longer
    # valid.
    NVAPI_PROFILE_REMOVED = - 169
    NVAPI_UNREGISTERED_RESOURCE = - 170

    # not < The DisplayId corresponds to a display which is not within the
    # normal outputId range.
    NVAPI_ID_OUT_OF_RANGE = - 171

    # not < Display topology is not valid so the driver cannot do a mode set
    # on this configuration.
    NVAPI_DISPLAYCONFIG_VALIDATION_FAILED = - 172
    NVAPI_DPMST_CHANGED = - 173
    NVAPI_INSUFFICIENT_BUFFER = - 174
    NVAPI_ACCESS_DENIED = - 175

    # not < The requested action cannot be performed without Mosaic being
    # enabled.
    NVAPI_MOSAIC_NOT_ACTIVE = - 176
    NVAPI_SHARE_RESOURCE_RELOCATED = - 177
    NVAPI_REQUEST_USER_TO_DISABLE_DWM = - 178

    # not < D3D device status is D3DERR_DEVICELOST or D3DERR_DEVICENOTRESET -
    # the user has to reset the device.
    NVAPI_D3D_DEVICE_LOST = - 179
    NVAPI_INVALID_CONFIGURATION = - 180
    NVAPI_STEREO_HANDSHAKE_NOT_DONE = - 181

    # not < The path provided was too SHORT to determine the correct
    # NVDRS_APPLICATION
    NVAPI_EXECUTABLE_PATH_IS_AMBIGUOUS = - 182
    NVAPI_DEFAULT_STEREO_PROFILE_IS_NOT_DEFINED = - 183
    NVAPI_DEFAULT_STEREO_PROFILE_DOES_NOT_EXIST = - 184
    NVAPI_CLUSTER_ALREADY_EXISTS = - 185

    # not < The input display id is not that of a multi stream enabled
    # connector or a display device in a multi stream topology
    NVAPI_DPMST_DISPLAY_ID_EXPECTED = - 186

    # not < The input display id is not valid or the monitor associated to it
    # does not support the current operation
    NVAPI_INVALID_DISPLAY_ID = - 187
    NVAPI_STREAM_IS_OUT_OF_SYNC = - 188
    NVAPI_INCOMPATIBLE_AUDIO_DRIVER = - 189
    NVAPI_VALUE_ALREADY_SET = - 190
    NVAPI_TIMEOUT = - 191

    # not < The requested workstation feature set has incomplete driver
    # internal allocation resources
    NVAPI_GPU_WORKSTATION_FEATURE_INCOMPLETE = - 192
    NVAPI_STEREO_INIT_ACTIVATION_NOT_DONE = - 193

    # not < The requested action cannot be performed without Sync being
    # enabled.
    NVAPI_SYNC_NOT_ACTIVE = - 194

    # not < The requested action cannot be performed without Sync Master being
    # enabled.
    NVAPI_SYNC_MASTER_NOT_FOUND = - 195
    NVAPI_INVALID_SYNC_TOPOLOGY = - 196

    # not < The specified signing algorithm is not supported. Either an
    # incorrect value was entered or the current installed driver/hardware
    # does not support the input value.
    NVAPI_ECID_SIGN_ALGO_UNSUPPORTED = - 197
    NVAPI_ECID_KEY_VERIFICATION_FAILED = - 198
    NVAPI_FIRMWARE_OUT_OF_DATE = - 199
    NVAPI_FIRMWARE_REVISION_NOT_SUPPORTED = - 200
    NVAPI_LICENSE_CALLER_AUTHENTICATION_FAILED = - 201

    # not < The user tried to use a deferred context without registering the
    # device first
    NVAPI_D3D_DEVICE_NOT_REGISTERED = - 202

    # not < Head or SourceId was not reserved for the VR Display before doing
    # the Modeset.
    NVAPI_RESOURCE_NOT_ACQUIRED = - 203
    NVAPI_TIMING_NOT_SUPPORTED = - 204

    # not < HDCP Encryption Failed for the device. Would be applicable when
    # the device is HDCP Capable.
    NVAPI_HDCP_ENCRYPTION_FAILED = - 205
    NVAPI_PCLK_LIMITATION_FAILED = - 206
    NVAPI_NO_CONNECTOR_FOUND = - 207

    # not < When a non-HDCP capable HMD is connected, we would inform user by
    # this code.
    NVAPI_HDCP_DISABLED = - 208
    NVAPI_API_IN_USE = - 209
    NVAPI_NVIDIA_DISPLAY_NOT_FOUND = - 210
    NVAPI_PRIV_SEC_VIOLATION = - 211
    NVAPI_INCORRECT_VENDOR = - 212
    NVAPI_DISPLAY_IN_USE = - 213
    NVAPI_UNSUPPORTED_CONFIG_NON_HDCP_HMD = - 214
    NVAPI_MAX_DISPLAY_LIMIT_REACHED = - 215
    NVAPI_INVALID_DIRECT_MODE_DISPLAY = - 216
    NVAPI_GPU_IN_DEBUG_MODE = - 217
    NVAPI_D3D_CONTEXT_NOT_FOUND = - 218
    NVAPI_STEREO_VERSION_MISMATCH = - 219
    NVAPI_GPU_NOT_POWERED = - 220
    NVAPI_ERROR_DRIVER_RELOAD_IN_PROGRESS = - 221
    NVAPI_WAIT_FOR_HW_RESOURCE = - 222
    NVAPI_REQUIRE_FURTHER_HDCP_ACTION = - 223
    NVAPI_DISPLAY_MUX_TRANSITION_FAILED = - 224


NvAPI_Status = _NvAPI_Status

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
NvAPI_SYS_GetDriverAndBranchVersion = hDll.NvAPI_SYS_GetDriverAndBranchVersion
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
NvAPI_GPU_GetMemoryInfo = hDll.NvAPI_GPU_GetMemoryInfo
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
NvAPI_EnumPhysicalGPUs = hDll.NvAPI_EnumPhysicalGPUs
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
NvAPI_D3D_GetObjectHandleForResource = hDll.NvAPI_D3D_GetObjectHandleForResource
NvAPI_D3D_GetObjectHandleForResource.restype = NVAPI_INTERFACE
