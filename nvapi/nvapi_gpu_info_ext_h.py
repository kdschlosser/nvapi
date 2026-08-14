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


# ---------------------------------------------------------------------------
# NVLink capability/status functions -- multi-GPU interconnect info
# (SLI/NVLink bridges, workstation/datacenter parts). All four return
# NVAPI_NOT_SUPPORTED on hardware without an NVLink bridge, which is
# expected, not an error.
# ---------------------------------------------------------------------------
NVAPI_NVLINK_MAX_LINKS = 32
NVAPI_NVLINK_MAX_LINKS_V2 = 128


class NVAPI_NVLINK_LINK_MASK_V1(ctypes.Structure):
    _fields_ = [
        ('lenMasks', NvU32),
        ('masks', NvU64 * NVAPI_NVLINK_MAX_LINKS_V2),
    ]


class NVLINK_GET_CAPS_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('capsTbl', NvU32),
        ('lowestNvlinkVersion', NvU8),
        ('highestNvlinkVersion', NvU8),
        ('lowestNciVersion', NvU8),
        ('highestNciVersion', NvU8),
        ('linkMask', NvU32),
    ]


NVLINK_GET_CAPS = NVLINK_GET_CAPS_V1
NVLINK_GET_CAPS_VER1 = MAKE_NVAPI_VERSION(NVLINK_GET_CAPS_V1, 1)
NVLINK_GET_CAPS_VER = NVLINK_GET_CAPS_VER1

NvAPI_GPU_NVLINK_GetCaps = hDll.GPU_NVLINK_GetCaps
NvAPI_GPU_NVLINK_GetCaps.restype = NVAPI_INTERFACE


class NVLINK_GET_CAPS_EX_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('capsTbl', NvU32),
        ('lowestNvlinkVersion', NvU8),
        ('highestNvlinkVersion', NvU8),
        ('lowestNciVersion', NvU8),
        ('highestNciVersion', NvU8),
        ('links', NVAPI_NVLINK_LINK_MASK_V1),
        ('reserved', NvU32 * 2),
    ]


NVLINK_GET_CAPS_EX = NVLINK_GET_CAPS_EX_V1
NVLINK_GET_CAPS_EX_VER1 = MAKE_NVAPI_VERSION(NVLINK_GET_CAPS_EX_V1, 1)
NVLINK_GET_CAPS_EX_VER = NVLINK_GET_CAPS_EX_VER1

NvAPI_GPU_NVLINK_GetCapsEx = hDll.GPU_NVLINK_GetCapsEx
NvAPI_GPU_NVLINK_GetCapsEx.restype = NVAPI_INTERFACE


class NVLINK_DEVICE_INFO_V1(ctypes.Structure):
    _fields_ = [
        ('deviceIdFlags', NvU32),
        ('domain', NvU16),
        ('bus', NvU16),
        ('device', NvU16),
        ('function', NvU16),
        ('pciDeviceId', NvU32),
        ('deviceType', NvU64),
        ('deviceUUID', NvU8 * NVAPI_UUID_LEN),
    ]


class NVLINK_LINK_STATUS_INFO_V2(ctypes.Structure):
    _fields_ = [
        ('capsTbl', NvU32),
        ('phyType', NvU8),
        ('subLinkWidth', NvU8),
        ('linkState', NvU32),
        ('rxSublinkStatus', NvU8),
        ('txSublinkStatus', NvU8),
        ('nvlinkVersion', NvU8),
        ('nciVersion', NvU8),
        ('phyVersion', NvU8),
        ('nvlinkCommonClockSpeedMhz', NvU32),
        ('nvlinkRefClkSpeedMhz', NvU32),
        ('nvlinkRefClkType', NvU8),
        ('nvlinkLinkClockMhz', NvU32),
        ('flags', NvU32),  # connected:1, reserved:31
        ('loopProperty', NvU8),
        ('remoteDeviceLinkNumber', NvU8),
        ('remoteDeviceInfo', NVLINK_DEVICE_INFO_V1),
        ('localDeviceLinkNumber', NvU8),
        ('localDeviceInfo', NVLINK_DEVICE_INFO_V1),
        ('nvlinkLineRateMbps', NvU32),
        ('nvlinkMinL1Threshold', NvU32),
        ('nvlinkMaxL1Threshold', NvU32),
        ('nvlinkL1ThresholdUnits', NvU32),
        ('reservedEx', NvU32 * 5),
    ]


class NVLINK_GET_STATUS_V2(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('linkMask', NvU32),
        ('linkInfo', NVLINK_LINK_STATUS_INFO_V2 * NVAPI_NVLINK_MAX_LINKS),
    ]


NVLINK_GET_STATUS = NVLINK_GET_STATUS_V2
NVLINK_GET_STATUS_VER2 = MAKE_NVAPI_VERSION(NVLINK_GET_STATUS_V2, 2)
NVLINK_GET_STATUS_VER = NVLINK_GET_STATUS_VER2

NvAPI_GPU_NVLINK_GetStatus = hDll.GPU_NVLINK_GetStatus
NvAPI_GPU_NVLINK_GetStatus.restype = NVAPI_INTERFACE


class NVLINK_GET_STATUS_EX_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('links', NVAPI_NVLINK_LINK_MASK_V1),
        ('linkInfo', NVLINK_LINK_STATUS_INFO_V2 * NVAPI_NVLINK_MAX_LINKS_V2),
    ]


NVLINK_GET_STATUS_EX = NVLINK_GET_STATUS_EX_V1
NVLINK_GET_STATUS_EX_VER1 = MAKE_NVAPI_VERSION(NVLINK_GET_STATUS_EX_V1, 1)
NVLINK_GET_STATUS_EX_VER = NVLINK_GET_STATUS_EX_VER1

NvAPI_GPU_NVLINK_GetStatusEx = hDll.GPU_NVLINK_GetStatusEx
NvAPI_GPU_NVLINK_GetStatusEx.restype = NVAPI_INTERFACE


# ---------------------------------------------------------------------------
# Hardware encoder (NVENC) monitoring -- session stats, not the encode
# pipeline itself.
# ---------------------------------------------------------------------------
class NV_ENCODER_STATISTICS_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('sessionsCount', NvU32),
        ('averageFps', NvU32),
        ('averageLatency', NvU32),
    ]


NV_ENCODER_STATISTICS = NV_ENCODER_STATISTICS_V1
NV_ENCODER_STATISTICS_VER1 = MAKE_NVAPI_VERSION(NV_ENCODER_STATISTICS_V1, 1)
NV_ENCODER_STATISTICS_VER = NV_ENCODER_STATISTICS_VER1

NvAPI_GPU_GetEncoderStatistics = hDll.GPU_GetEncoderStatistics
NvAPI_GPU_GetEncoderStatistics.restype = NVAPI_INTERFACE


class NV_ENCODER_PER_SESSION_INFO_V1(ctypes.Structure):
    _fields_ = [
        ('sessionId', NvU32),
        ('processId', NvU32),
        ('vgpuInstance', NvU32),
        ('codecType', NvU32),
        ('hResolution', NvU32),
        ('vResolution', NvU32),
        ('averageEncodeFps', NvU32),
        ('averageEncodeLatency', NvU32),
    ]


class NV_ENCODER_TYPE(ENUM):
    NV_ENCODER_H264 = EnumItem(0).set_string('H.264')
    NV_ENCODER_HEVC = EnumItem(1).set_string('HEVC')
    NV_ENCODER_UNKNOWN = EnumItem(0xFFFFFFFF).set_string('Unknown')


NV_ENCODER_SESSION_INFO_MAX_ENTRIES_V1 = 0x200  # 512 entries


class NV_ENCODER_SESSIONS_INFO_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('sessionsCount', NvU32),
        ('pSessionInfo', ctypes.POINTER(NV_ENCODER_PER_SESSION_INFO_V1)),
    ]


NV_ENCODER_SESSIONS_INFO = NV_ENCODER_SESSIONS_INFO_V1
NV_ENCODER_SESSIONS_INFO_VER1 = MAKE_NVAPI_VERSION(NV_ENCODER_SESSIONS_INFO_V1, 1)
NV_ENCODER_SESSIONS_INFO_VER = NV_ENCODER_SESSIONS_INFO_VER1

NvAPI_GPU_GetEncoderSessionsInfo = hDll.GPU_GetEncoderSessionsInfo
NvAPI_GPU_GetEncoderSessionsInfo.restype = NVAPI_INTERFACE
