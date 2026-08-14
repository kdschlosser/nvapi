# -*- coding: utf-8 -*-
"""
GPU identification/info functions absent from the original ported headers
because they postdate the 2019 (Release 440) SDK snapshot the generator ran
against. Structs and signatures below are transcribed from the current,
official NVIDIA header: https://github.com/NVIDIA/nvapi/blob/main/nvapi.h
and nvapi_lite_common.h (both MIT licensed, copyright NVIDIA CORPORATION).

Dispatch works the same way as everything else in this package: these
NvAPI_X = hDll.X assignments resolve through nvapi_QueryInterface using the
numeric IDs in nvapi_interface_ids.py, all of which already include these
newer functions (that table is NVIDIA's current published list; only the
struct/function declarations were stale, not the ID table).
"""

import ctypes

from .nvapi_lite_common_h import *  # noqa
from .nvapi_h import hDll, NVAPI_INTERFACE, NvPhysicalGpuHandle  # noqa


NVAPI_UUID_LEN = 16
NVAPI_GPU_MAX_BUILD_VERSION_LENGTH = 0x40


# ---------------------------------------------------------------------------
# NV_GPU_ARCH_INFO
# ---------------------------------------------------------------------------
class NV_GPU_ARCH_INFO_V2(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('architecture', NvU32),
        ('implementation', NvU32),
        ('revision', NvU32),
    ]


NV_GPU_ARCH_INFO = NV_GPU_ARCH_INFO_V2
NV_GPU_ARCH_INFO_VER2 = MAKE_NVAPI_VERSION(NV_GPU_ARCH_INFO_V2, 2)
NV_GPU_ARCH_INFO_VER = NV_GPU_ARCH_INFO_VER2

NvAPI_GPU_GetArchInfo = hDll.GPU_GetArchInfo
NvAPI_GPU_GetArchInfo.restype = NVAPI_INTERFACE


# ---------------------------------------------------------------------------
# NV_GPU_UUID
# ---------------------------------------------------------------------------
class NV_GPU_UUID_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('uuid', NvU8 * NVAPI_UUID_LEN),
    ]


NV_GPU_UUID = NV_GPU_UUID_V1
NV_GPU_UUID_VER1 = MAKE_NVAPI_VERSION(NV_GPU_UUID_V1, 1)
NV_GPU_UUID_VER = NV_GPU_UUID_VER1

NvAPI_GPU_GetUUID = hDll.GPU_GetUUID
NvAPI_GPU_GetUUID.restype = NVAPI_INTERFACE


# ---------------------------------------------------------------------------
# NV_GPU_VIRTUALIZATION_INFO
# ---------------------------------------------------------------------------
class NV_VIRTUALIZATION_MODE(ENUM):
    NV_VIRTUALIZATION_MODE_NONE = EnumItem(0).set_string('None')
    NV_VIRTUALIZATION_MODE_VGX = EnumItem(2).set_string('vGPU (guest)')
    NV_VIRTUALIZATION_MODE_HOST_VGPU = EnumItem(3).set_string('vGPU (host)')


class NV_GPU_VIRTUALIZATION_INFO_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('virtualizationMode', NvU32),
        ('reserved', NvU32),
    ]


NV_GPU_VIRTUALIZATION_INFO = NV_GPU_VIRTUALIZATION_INFO_V1
NV_GPU_VIRTUALIZATION_INFO_VER1 = MAKE_NVAPI_VERSION(NV_GPU_VIRTUALIZATION_INFO_V1, 1)
NV_GPU_VIRTUALIZATION_INFO_VER = NV_GPU_VIRTUALIZATION_INFO_VER1

NvAPI_GPU_GetVirtualizationInfo = hDll.GPU_GetVirtualizationInfo
NvAPI_GPU_GetVirtualizationInfo.restype = NVAPI_INTERFACE


# ---------------------------------------------------------------------------
# NV_LICENSABLE_FEATURES (V4) and its nested types
# ---------------------------------------------------------------------------
NV_LICENSE_MAX_COUNT = 3
NV_LICENSE_SIGNATURE_SIZE = 128
NV_LICENSE_INFO_MAX_LENGTH = 128

NvAPI_LicenseString = ctypes.c_char * NV_LICENSE_INFO_MAX_LENGTH


class NV_LICENSE_FEATURE_TYPE(ENUM):
    NV_LICENSE_FEATURE_UNKNOWN = EnumItem(0).set_string('Unknown')
    NV_LICENSE_FEATURE_VGPU = EnumItem(1).set_string('vGPU')
    NV_LICENSE_FEATURE_NVIDIA_RTX = EnumItem(2).set_string('NVIDIA RTX')
    NV_LICENSE_FEATURE_GAMING = EnumItem(3).set_string('Gaming')
    NV_LICENSE_FEATURE_COMPUTE = EnumItem(4).set_string('Compute')


class NV_LICENSE_EXPIRY_DETAILS(ctypes.Structure):
    _fields_ = [
        ('year', NvU32),
        ('month', NvU16),
        ('day', NvU16),
        ('hour', NvU16),
        ('minute', NvU16),
        ('second', NvU16),
        ('status', NvU8),
    ]


class NV_LICENSE_FEATURE_DETAILS_V4(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('flags', NvU32),  # isEnabled:1, isFeatureEnabled:1, reserved:30
        ('featureCode', NvU32),
        ('licenseInfo', NvAPI_LicenseString),
        ('productName', NvAPI_LicenseString),
        ('licenseExpiry', NV_LICENSE_EXPIRY_DETAILS),
    ]


class NV_LICENSABLE_FEATURES_V4(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('flags', NvU32),  # isLicenseSupported:1, reserved:31
        ('licensableFeatureCount', NvU32),
        ('signature', NvU8 * NV_LICENSE_SIGNATURE_SIZE),
        ('licenseDetails', NV_LICENSE_FEATURE_DETAILS_V4 * NV_LICENSE_MAX_COUNT),
    ]


NV_LICENSABLE_FEATURES = NV_LICENSABLE_FEATURES_V4
NV_LICENSABLE_FEATURES_VER4 = MAKE_NVAPI_VERSION(NV_LICENSABLE_FEATURES_V4, 4)
NV_LICENSABLE_FEATURES_VER = NV_LICENSABLE_FEATURES_VER4

NvAPI_GPU_GetLicensableFeatures = hDll.GPU_GetLicensableFeatures
NvAPI_GPU_GetLicensableFeatures.restype = NVAPI_INTERFACE


# ---------------------------------------------------------------------------
# NV_GPU_INFO (V2)
# ---------------------------------------------------------------------------
class NV_GPU_INFO_V2(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('flags', NvU32),  # bIsExternalGpu:1, reserved0:31
        ('reserved1', NvU64),
        ('rayTracingCores', NvU32),
        ('tensorCores', NvU32),
        ('reserved2', NvU32 * 14),
    ]


NV_GPU_INFO = NV_GPU_INFO_V2
NV_GPU_INFO_VER2 = MAKE_NVAPI_VERSION(NV_GPU_INFO_V2, 2)
NV_GPU_INFO_VER = NV_GPU_INFO_VER2

NvAPI_GPU_GetGPUInfo = hDll.GPU_GetGPUInfo
NvAPI_GPU_GetGPUInfo.restype = NVAPI_INTERFACE


# ---------------------------------------------------------------------------
# NV_GPU_VR_READY
# ---------------------------------------------------------------------------
class NV_GPU_VR_READY_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('flags', NvU32),  # isVRReady:1, reserved:31
    ]


NV_GPU_VR_READY = NV_GPU_VR_READY_V1
NV_GPU_VR_READY_VER1 = MAKE_NVAPI_VERSION(NV_GPU_VR_READY_V1, 1)
NV_GPU_VR_READY_VER = NV_GPU_VR_READY_VER1

NvAPI_GPU_GetVRReadyData = hDll.GPU_GetVRReadyData
NvAPI_GPU_GetVRReadyData.restype = NVAPI_INTERFACE


# ---------------------------------------------------------------------------
# NV_GPU_GSP_INFO
# ---------------------------------------------------------------------------
class NV_GPU_GSP_INFO_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('firmwareVersion', NvU8 * NVAPI_GPU_MAX_BUILD_VERSION_LENGTH),
        ('reserved', NvU32),
    ]


NV_GPU_GSP_INFO = NV_GPU_GSP_INFO_V1
NV_GPU_GSP_INFO_VER1 = MAKE_NVAPI_VERSION(NV_GPU_GSP_INFO_V1, 1)
NV_GPU_GSP_INFO_VER = NV_GPU_GSP_INFO_VER1

NvAPI_GPU_GetGspFeatures = hDll.GPU_GetGspFeatures
NvAPI_GPU_GetGspFeatures.restype = NVAPI_INTERFACE


# ---------------------------------------------------------------------------
# NV_GPU_OVERCLOCK_STATUS
# ---------------------------------------------------------------------------
class NV_GPU_OVERCLOCK_STATUS_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('flags', NvU32),  # bOverclockingDetected:1, reserved:31
        ('rsvd', NvU32 * 16),
    ]


NV_GPU_OVERCLOCK_STATUS = NV_GPU_OVERCLOCK_STATUS_V1
NV_GPU_OVERCLOCK_STATUS_VER1 = MAKE_NVAPI_VERSION(NV_GPU_OVERCLOCK_STATUS_V1, 1)
NV_GPU_OVERCLOCK_STATUS_VER = NV_GPU_OVERCLOCK_STATUS_VER1

NvAPI_GPU_GetOverclockStatus = hDll.GPU_GetOverclockStatus
NvAPI_GPU_GetOverclockStatus.restype = NVAPI_INTERFACE


# ---------------------------------------------------------------------------
# NV_GPU_MEMORY_INFO_EX -- modern replacement for the deprecated (since
# release 520) NV_DISPLAY_DRIVER_MEMORY_INFO already wrapped elsewhere.
# Units here are bytes, not KB.
# ---------------------------------------------------------------------------
class NV_GPU_MEMORY_INFO_EX_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('dedicatedVideoMemory', NvU64),
        ('availableDedicatedVideoMemory', NvU64),
        ('systemVideoMemory', NvU64),
        ('sharedSystemMemory', NvU64),
        ('curAvailableDedicatedVideoMemory', NvU64),
        ('dedicatedVideoMemoryEvictionsSize', NvU64),
        ('dedicatedVideoMemoryEvictionCount', NvU64),
        ('dedicatedVideoMemoryPromotionsSize', NvU64),
        ('dedicatedVideoMemoryPromotionCount', NvU64),
    ]


NV_GPU_MEMORY_INFO_EX = NV_GPU_MEMORY_INFO_EX_V1
NV_GPU_MEMORY_INFO_EX_VER1 = MAKE_NVAPI_VERSION(NV_GPU_MEMORY_INFO_EX_V1, 1)
NV_GPU_MEMORY_INFO_EX_VER = NV_GPU_MEMORY_INFO_EX_VER1

NvAPI_GPU_GetMemoryInfoEx = hDll.GPU_GetMemoryInfoEx
NvAPI_GPU_GetMemoryInfoEx.restype = NVAPI_INTERFACE


# ---------------------------------------------------------------------------
# Simple functions -- plain NvU32*/void* out-params, no new struct needed
# ---------------------------------------------------------------------------
NvAPI_GetPhysicalGPUFromGPUID = hDll.GetPhysicalGPUFromGPUID
NvAPI_GetPhysicalGPUFromGPUID.restype = NVAPI_INTERFACE

NvAPI_GetGPUIDfromPhysicalGPU = hDll.GetGPUIDfromPhysicalGPU
NvAPI_GetGPUIDfromPhysicalGPU.restype = NVAPI_INTERFACE

NvAPI_GPU_GetRamBusWidth = hDll.GPU_GetRamBusWidth
NvAPI_GPU_GetRamBusWidth.restype = NVAPI_INTERFACE

NvAPI_GPU_GetAdapterIdFromPhysicalGpu = hDll.GPU_GetAdapterIdFromPhysicalGpu
NvAPI_GPU_GetAdapterIdFromPhysicalGpu.restype = NVAPI_INTERFACE
