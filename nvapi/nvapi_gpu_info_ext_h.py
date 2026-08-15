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
from .nvapi_h import hDll, NVAPI_INTERFACE, NvPhysicalGpuHandle, NV_GPU_CONNECTOR_TYPE  # noqa
from .nvapi_interface_ids import NVAPI_INTERFACE_IDS  # noqa


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


# ---------------------------------------------------------------------------
# Display/color management. Set* functions are ported and bound the same as
# everything else, but are never invoked from this package's own test code
# against live hardware -- they change real display state.
# ---------------------------------------------------------------------------
class NV_COLORSPACE_TYPE(ENUM):
    NV_COLORSPACE_sRGB = EnumItem(0).set_string('sRGB')
    NV_COLORSPACE_xRGB = EnumItem(1).set_string('xRGB (FP16 linear)')
    NV_COLORSPACE_REC2100 = EnumItem(12).set_string('Rec. 2100 (HDR10)')


NV_SOURCE_PID_CURRENT = 0

NvAPI_Disp_SetSourceColorSpace = hDll.Disp_SetSourceColorSpace
NvAPI_Disp_SetSourceColorSpace.restype = NVAPI_INTERFACE

NvAPI_Disp_GetSourceColorSpace = hDll.Disp_GetSourceColorSpace
NvAPI_Disp_GetSourceColorSpace.restype = NVAPI_INTERFACE


class NV_HDR_METADATA_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('displayPrimary_x0', NvU16),
        ('displayPrimary_y0', NvU16),
        ('displayPrimary_x1', NvU16),
        ('displayPrimary_y1', NvU16),
        ('displayPrimary_x2', NvU16),
        ('displayPrimary_y2', NvU16),
        ('displayWhitePoint_x', NvU16),
        ('displayWhitePoint_y', NvU16),
        ('max_display_mastering_luminance', NvU16),
        ('min_display_mastering_luminance', NvU16),
        ('max_content_light_level', NvU16),
        ('max_frame_average_light_level', NvU16),
    ]


NV_HDR_METADATA = NV_HDR_METADATA_V1
NV_HDR_METADATA_VER1 = MAKE_NVAPI_VERSION(NV_HDR_METADATA_V1, 1)
NV_HDR_METADATA_VER = NV_HDR_METADATA_VER1

NvAPI_Disp_SetSourceHdrMetadata = hDll.Disp_SetSourceHdrMetadata
NvAPI_Disp_SetSourceHdrMetadata.restype = NVAPI_INTERFACE

NvAPI_Disp_GetSourceHdrMetadata = hDll.Disp_GetSourceHdrMetadata
NvAPI_Disp_GetSourceHdrMetadata.restype = NVAPI_INTERFACE


class NV_DISPLAY_OUTPUT_MODE(ENUM):
    NV_DISPLAY_OUTPUT_MODE_SDR = EnumItem(0).set_string('SDR')
    NV_DISPLAY_OUTPUT_MODE_HDR10 = EnumItem(1).set_string('HDR10')
    NV_DISPLAY_OUTPUT_MODE_HDR10PLUS_GAMING = EnumItem(2).set_string('HDR10+ Gaming')


NvAPI_Disp_SetOutputMode = hDll.Disp_SetOutputMode
NvAPI_Disp_SetOutputMode.restype = NVAPI_INTERFACE

NvAPI_Disp_GetOutputMode = hDll.Disp_GetOutputMode
NvAPI_Disp_GetOutputMode.restype = NVAPI_INTERFACE


class NV_HDR_TONEMAPPING_METHOD(ENUM):
    NV_HDR_TONEMAPPING_APP = EnumItem(0).set_string('Application')
    NV_HDR_TONEMAPPING_GPU = EnumItem(1).set_string('GPU')


NvAPI_Disp_SetHdrToneMapping = hDll.Disp_SetHdrToneMapping
NvAPI_Disp_SetHdrToneMapping.restype = NVAPI_INTERFACE

NvAPI_Disp_GetHdrToneMapping = hDll.Disp_GetHdrToneMapping
NvAPI_Disp_GetHdrToneMapping.restype = NVAPI_INTERFACE


class NV_DISPLAY_COLORIMETRY_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('min_luminance', ctypes.c_float),
        ('max_full_frame_luminance', ctypes.c_float),
        ('max_luminance', ctypes.c_float),
        ('hdrBrightnessLuminanceScalingFactor', ctypes.c_float),
        ('red_primary_x', ctypes.c_float),
        ('red_primary_y', ctypes.c_float),
        ('green_primary_x', ctypes.c_float),
        ('green_primary_y', ctypes.c_float),
        ('blue_primary_x', ctypes.c_float),
        ('blue_primary_y', ctypes.c_float),
        ('white_point_x', ctypes.c_float),
        ('white_point_y', ctypes.c_float),
    ]


NV_DISPLAY_COLORIMETRY = NV_DISPLAY_COLORIMETRY_V1
NV_DISPLAY_COLORIMETRY_VER1 = MAKE_NVAPI_VERSION(NV_DISPLAY_COLORIMETRY_V1, 1)
NV_DISPLAY_COLORIMETRY_VER = NV_DISPLAY_COLORIMETRY_VER1

NvAPI_Disp_GetColorimetry = hDll.Disp_GetColorimetry
NvAPI_Disp_GetColorimetry.restype = NVAPI_INTERFACE


# EDID -- two-pass allocation (call once with pEDID=NULL to get sizeOfEDID,
# allocate, call again). More complete than the fixed-256-byte
# NvAPI_GPU_GetEDID used elsewhere in this package for large/extended EDIDs.
class NV_EDID_DATA_V2(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('pEDID', ctypes.POINTER(NvU8)),
        ('sizeOfEDID', NvU32),
        ('reserved', NvU32 * 8),
    ]


NV_EDID_DATA = NV_EDID_DATA_V2
NV_EDID_DATA_VER2 = MAKE_NVAPI_VERSION(NV_EDID_DATA_V2, 2)
NV_EDID_DATA_VER = NV_EDID_DATA_VER2


class NV_EDID_FLAG(ENUM):
    NV_EDID_FLAG_DEFAULT = EnumItem(0).set_string('Default (active)')
    NV_EDID_FLAG_RAW = EnumItem(1).set_string('Raw (unmodified)')
    NV_EDID_FLAG_COOKED = EnumItem(2).set_string('Cooked (driver-modified)')
    NV_EDID_FLAG_FORCED = EnumItem(3).set_string('Forced (user override)')
    NV_EDID_FLAG_INF = EnumItem(4).set_string('From monitor INF')
    NV_EDID_FLAG_HW = EnumItem(5).set_string('Hardware (I2C, unmodified)')


NvAPI_DISP_GetEdidData = hDll.DISP_GetEdidData
NvAPI_DISP_GetEdidData.restype = NVAPI_INTERFACE


class NV_GET_ADAPTIVE_SYNC_DATA_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('maxFrameInterval', NvU32),
        ('flags', NvU32),  # bDisableAdaptiveSync:1, bDisableFrameSplitting:1, reserved:30
        ('lastFlipRefreshCount', NvU32),
        ('lastFlipTimeStamp', NvU64),
        ('reservedEx', NvU32 * 4),
    ]


NV_GET_ADAPTIVE_SYNC_DATA = NV_GET_ADAPTIVE_SYNC_DATA_V1
NV_GET_ADAPTIVE_SYNC_DATA_VER1 = MAKE_NVAPI_VERSION(NV_GET_ADAPTIVE_SYNC_DATA_V1, 1)
NV_GET_ADAPTIVE_SYNC_DATA_VER = NV_GET_ADAPTIVE_SYNC_DATA_VER1

NvAPI_DISP_GetAdaptiveSyncData = hDll.DISP_GetAdaptiveSyncData
NvAPI_DISP_GetAdaptiveSyncData.restype = NVAPI_INTERFACE


class NV_SET_ADAPTIVE_SYNC_DATA_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('maxFrameInterval', NvU32),  # deprecated, use maxFrameIntervalNs
        ('flags', NvU32),  # bDisableAdaptiveSync:1, bDisableFrameSplitting:1, reserved:30
        ('reserved1', NvU32),
        ('maxFrameIntervalNs', NvU64),
        ('reservedEx', NvU32 * 4),
    ]


NV_SET_ADAPTIVE_SYNC_DATA = NV_SET_ADAPTIVE_SYNC_DATA_V1
NV_SET_ADAPTIVE_SYNC_DATA_VER2 = MAKE_NVAPI_VERSION(NV_SET_ADAPTIVE_SYNC_DATA_V1, 2)
NV_SET_ADAPTIVE_SYNC_DATA_VER = NV_SET_ADAPTIVE_SYNC_DATA_VER2

NvAPI_DISP_SetAdaptiveSyncData = hDll.DISP_SetAdaptiveSyncData
NvAPI_DISP_SetAdaptiveSyncData.restype = NVAPI_INTERFACE


class NV_GET_VIRTUAL_REFRESH_RATE_DATA_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('frameIntervalUs', NvU32),
        ('rrx1k', NvU32),
        ('bIsGamingVrr', NvU32),
        ('reservedEx', NvU32 * 6),
    ]


class NV_GET_VIRTUAL_REFRESH_RATE_DATA_V2(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('frameIntervalUs', NvU32),  # deprecated in V2
        ('rrx1k', NvU32),
        ('bIsGamingVrr', NvU32),
        ('frameIntervalNs', NvU64),
        ('reservedEx', NvU32 * 4),
    ]


# V2 is same size as V1 but this driver rejects the V2 revision tag
# (confirmed live: identical sizeof, V1's version macro succeeds, V2's
# returns NVAPI_INCOMPATIBLE_STRUCT_VERSION) -- default to V1, the
# revision actually accepted, rather than always the newest one defined
NV_GET_VIRTUAL_REFRESH_RATE_DATA = NV_GET_VIRTUAL_REFRESH_RATE_DATA_V1
NV_GET_VIRTUAL_REFRESH_RATE_DATA_VER1 = MAKE_NVAPI_VERSION(NV_GET_VIRTUAL_REFRESH_RATE_DATA_V1, 1)
NV_GET_VIRTUAL_REFRESH_RATE_DATA_VER2 = MAKE_NVAPI_VERSION(NV_GET_VIRTUAL_REFRESH_RATE_DATA_V2, 2)
NV_GET_VIRTUAL_REFRESH_RATE_DATA_VER = NV_GET_VIRTUAL_REFRESH_RATE_DATA_VER1

NvAPI_DISP_GetVirtualRefreshRateData = hDll.DISP_GetVirtualRefreshRateData
NvAPI_DISP_GetVirtualRefreshRateData.restype = NVAPI_INTERFACE


class NV_SET_VIRTUAL_REFRESH_RATE_DATA_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('frameIntervalUs', NvU32),
        ('rrx1k', NvU32),
        ('bIsGamingVrr', NvU32),
        ('reservedEx', NvU32 * 6),
    ]


class NV_SET_VIRTUAL_REFRESH_RATE_DATA_V2(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('frameIntervalUs', NvU32),  # deprecated in V2
        ('rrx1k', NvU32),
        ('bIsGamingVrr', NvU32),
        ('frameIntervalNs', NvU64),
        ('reservedEx', NvU32 * 4),
    ]


# same driver-support situation as the GET side (see above): default to
# the V1 revision tag rather than assume V2 is accepted
NV_SET_VIRTUAL_REFRESH_RATE_DATA = NV_SET_VIRTUAL_REFRESH_RATE_DATA_V1
NV_SET_VIRTUAL_REFRESH_RATE_DATA_VER1 = MAKE_NVAPI_VERSION(NV_SET_VIRTUAL_REFRESH_RATE_DATA_V1, 1)
NV_SET_VIRTUAL_REFRESH_RATE_DATA_VER2 = MAKE_NVAPI_VERSION(NV_SET_VIRTUAL_REFRESH_RATE_DATA_V2, 2)
NV_SET_VIRTUAL_REFRESH_RATE_DATA_VER = NV_SET_VIRTUAL_REFRESH_RATE_DATA_VER1

NvAPI_DISP_SetVirtualRefreshRateData = hDll.DISP_SetVirtualRefreshRateData
NvAPI_DISP_SetVirtualRefreshRateData.restype = NVAPI_INTERFACE


class NV_SET_PREFERRED_STEREO_DISPLAY_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('displayId', NvU32),
        ('reserved', NvU32),
    ]


NV_SET_PREFERRED_STEREO_DISPLAY = NV_SET_PREFERRED_STEREO_DISPLAY_V1
NV_SET_PREFERRED_STEREO_DISPLAY_VER1 = MAKE_NVAPI_VERSION(NV_SET_PREFERRED_STEREO_DISPLAY_V1, 1)
NV_SET_PREFERRED_STEREO_DISPLAY_VER = NV_SET_PREFERRED_STEREO_DISPLAY_VER1

NvAPI_DISP_SetPreferredStereoDisplay = hDll.DISP_SetPreferredStereoDisplay
NvAPI_DISP_SetPreferredStereoDisplay.restype = NVAPI_INTERFACE


class NV_GET_PREFERRED_STEREO_DISPLAY_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('displayId', NvU32),
        ('reserved', NvU32),
    ]


NV_GET_PREFERRED_STEREO_DISPLAY = NV_GET_PREFERRED_STEREO_DISPLAY_V1
NV_GET_PREFERRED_STEREO_DISPLAY_VER1 = MAKE_NVAPI_VERSION(NV_GET_PREFERRED_STEREO_DISPLAY_V1, 1)
NV_GET_PREFERRED_STEREO_DISPLAY_VER = NV_GET_PREFERRED_STEREO_DISPLAY_VER1

NvAPI_DISP_GetPreferredStereoDisplay = hDll.DISP_GetPreferredStereoDisplay
NvAPI_DISP_GetPreferredStereoDisplay.restype = NVAPI_INTERFACE


class NV_MANAGED_DEDICATED_DISPLAY_INFO_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('displayId', NvU32),
        ('flags', NvU32),  # isAcquired:1, isMosaic:1, reserved:30
    ]


NV_MANAGED_DEDICATED_DISPLAY_INFO = NV_MANAGED_DEDICATED_DISPLAY_INFO_V1
NV_MANAGED_DEDICATED_DISPLAY_INFO_VER1 = MAKE_NVAPI_VERSION(NV_MANAGED_DEDICATED_DISPLAY_INFO_V1, 1)
NV_MANAGED_DEDICATED_DISPLAY_INFO_VER = NV_MANAGED_DEDICATED_DISPLAY_INFO_VER1

NvAPI_DISP_GetNvManagedDedicatedDisplays = hDll.DISP_GetNvManagedDedicatedDisplays
NvAPI_DISP_GetNvManagedDedicatedDisplays.restype = NVAPI_INTERFACE

NvAPI_DISP_AcquireDedicatedDisplay = hDll.DISP_AcquireDedicatedDisplay
NvAPI_DISP_AcquireDedicatedDisplay.restype = NVAPI_INTERFACE

NvAPI_DISP_ReleaseDedicatedDisplay = hDll.DISP_ReleaseDedicatedDisplay
NvAPI_DISP_ReleaseDedicatedDisplay.restype = NVAPI_INTERFACE


class NV_MANAGED_DEDICATED_DISPLAY_METADATA_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('displayId', NvU32),
        ('flags', NvU32),  # bSetPosition:1, bRemovePosition:1, bPositionIsAvailable:1,
                           # bSetName:1, bRemoveName:1, bNameIsAvailable:1, reserved:26
        ('positionX', ctypes.c_int32),
        ('positionY', ctypes.c_int32),
        ('name', NvAPI_ShortString),
    ]


NV_MANAGED_DEDICATED_DISPLAY_METADATA = NV_MANAGED_DEDICATED_DISPLAY_METADATA_V1
NV_MANAGED_DEDICATED_DISPLAY_METADATA_VER1 = MAKE_NVAPI_VERSION(NV_MANAGED_DEDICATED_DISPLAY_METADATA_V1, 1)
NV_MANAGED_DEDICATED_DISPLAY_METADATA_VER = NV_MANAGED_DEDICATED_DISPLAY_METADATA_VER1

NvAPI_DISP_GetNvManagedDedicatedDisplayMetadata = hDll.DISP_GetNvManagedDedicatedDisplayMetadata
NvAPI_DISP_GetNvManagedDedicatedDisplayMetadata.restype = NVAPI_INTERFACE

NvAPI_DISP_SetNvManagedDedicatedDisplayMetadata = hDll.DISP_SetNvManagedDedicatedDisplayMetadata
NvAPI_DISP_SetNvManagedDedicatedDisplayMetadata.restype = NVAPI_INTERFACE


# real Windows LUID (8 bytes: LowPart NvU32 + HighPart NvS32) -- distinct
# from this package's existing NvLUID (aliased to the 16-byte NvGUID shape
# elsewhere), needed here to match the real C struct layout exactly
class WIN_LUID(ctypes.Structure):
    _fields_ = [
        ('LowPart', NvU32),
        ('HighPart', ctypes.c_int32),
    ]


class NV_DISPLAY_ID_INFO_DATA_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('adapterId', WIN_LUID),
        ('targetId', NvU32),
        ('reserved', NvU32 * 4),
    ]


NV_DISPLAY_ID_INFO_DATA = NV_DISPLAY_ID_INFO_DATA_V1
NV_DISPLAY_ID_INFO_DATA_VER1 = MAKE_NVAPI_VERSION(NV_DISPLAY_ID_INFO_DATA_V1, 1)
NV_DISPLAY_ID_INFO_DATA_VER = NV_DISPLAY_ID_INFO_DATA_VER1

NvAPI_Disp_GetDisplayIdInfo = hDll.Disp_GetDisplayIdInfo
NvAPI_Disp_GetDisplayIdInfo.restype = NVAPI_INTERFACE


NVAPI_MAX_DISPLAYS = NVAPI_PHYSICAL_GPUS * NVAPI_ADVANCED_DISPLAY_HEADS


class NV_TARGET_INFO_DATA_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('adapterId', WIN_LUID),
        ('targetId', NvU32),
        ('displayId', NvU32 * NVAPI_MAX_DISPLAYS),
        ('displayIdCount', NvU32),
        ('reserved', NvU32 * 4),
    ]


NV_TARGET_INFO_DATA = NV_TARGET_INFO_DATA_V1
NV_TARGET_INFO_DATA_VER1 = MAKE_NVAPI_VERSION(NV_TARGET_INFO_DATA_V1, 1)
NV_TARGET_INFO_DATA_VER = NV_TARGET_INFO_DATA_VER1

NvAPI_Disp_GetDisplayIdsFromTarget = hDll.Disp_GetDisplayIdsFromTarget
NvAPI_Disp_GetDisplayIdsFromTarget.restype = NVAPI_INTERFACE


class NV_GET_VRR_INFO_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('flags', NvU32),  # bIsVRREnabled:1, bIsVRRPossible:1, bIsVRRRequested:1,
                           # bIsVRRIndicatorEnabled:1, bIsDisplayInVRRMode:1, reserved:27
        ('reservedEx', NvU32 * 4),
    ]


NV_GET_VRR_INFO = NV_GET_VRR_INFO_V1
NV_GET_VRR_INFO_VER1 = MAKE_NVAPI_VERSION(NV_GET_VRR_INFO_V1, 1)
NV_GET_VRR_INFO_VER = NV_GET_VRR_INFO_VER1

NvAPI_Disp_GetVRRInfo = hDll.Disp_GetVRRInfo
NvAPI_Disp_GetVRRInfo.restype = NVAPI_INTERFACE


# ---------------------------------------------------------------------------
# System-level enumeration
# ---------------------------------------------------------------------------
class NV_DISPLAY_DRIVER_INFO_V2(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('driverVersion', NvU32),
        ('szBuildBranch', NvAPI_ShortString),
        ('flags', NvU32),  # bIsDCHDriver:1, bIsNVIDIAStudioPackage:1,
                           # bIsNVIDIAGameReadyPackage:1,
                           # bIsNVIDIARTXProductionBranchPackage:1,
                           # bIsNVIDIARTXNewFeatureBranchPackage:1, reserved:27
        ('szBuildBaseBranch', NvAPI_ShortString),
        ('reservedEx', NvU32),
    ]


NV_DISPLAY_DRIVER_INFO = NV_DISPLAY_DRIVER_INFO_V2
NV_DISPLAY_DRIVER_INFO_VER2 = MAKE_NVAPI_VERSION(NV_DISPLAY_DRIVER_INFO_V2, 2)
NV_DISPLAY_DRIVER_INFO_VER = NV_DISPLAY_DRIVER_INFO_VER2

NvAPI_SYS_GetDisplayDriverInfo = hDll.SYS_GetDisplayDriverInfo
NvAPI_SYS_GetDisplayDriverInfo.restype = NVAPI_INTERFACE


class NV_ADAPTER_TYPE(ENUM):
    NV_ADAPTER_TYPE_UNKNOWN = EnumItem(0x0).set_string('Unknown')
    NV_ADAPTER_TYPE_WDDM = EnumItem(1 << 0).set_string('WDDM')
    NV_ADAPTER_TYPE_MCDM = EnumItem(1 << 1).set_string('MCDM')
    NV_ADAPTER_TYPE_TCC = EnumItem(1 << 2).set_string('TCC')


class NV_PHYSICAL_GPU_HANDLE_DATA(ctypes.Structure):
    _fields_ = [
        ('hPhysicalGpu', ctypes.c_void_p),
        ('adapterType', NvU32),
        ('reserved2', NvU32 * 4),
    ]


class NV_PHYSICAL_GPUS_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('gpuHandleData', NV_PHYSICAL_GPU_HANDLE_DATA * NVAPI_MAX_PHYSICAL_GPUS),
        ('gpuHandleCount', NvU32),
        ('reserved', NvU32 * 4),
    ]


NV_PHYSICAL_GPUS = NV_PHYSICAL_GPUS_V1
NV_PHYSICAL_GPUS_VER1 = MAKE_NVAPI_VERSION(NV_PHYSICAL_GPUS_V1, 1)
NV_PHYSICAL_GPUS_VER = NV_PHYSICAL_GPUS_VER1

NvAPI_SYS_GetPhysicalGPUs = hDll.SYS_GetPhysicalGPUs
NvAPI_SYS_GetPhysicalGPUs.restype = NVAPI_INTERFACE


class NV_LOGICAL_GPU_HANDLE_DATA(ctypes.Structure):
    _fields_ = [
        ('hLogicalGpu', ctypes.c_void_p),
        ('adapterType', NvU32),
        ('reserved', NvU32 * 4),
    ]


class NV_LOGICAL_GPUS_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('gpuHandleData', NV_LOGICAL_GPU_HANDLE_DATA * NVAPI_MAX_LOGICAL_GPUS),
        ('gpuHandleCount', NvU32),
        ('reserved', NvU32 * 4),
    ]


NV_LOGICAL_GPUS = NV_LOGICAL_GPUS_V1
NV_LOGICAL_GPUS_VER1 = MAKE_NVAPI_VERSION(NV_LOGICAL_GPUS_V1, 1)
NV_LOGICAL_GPUS_VER = NV_LOGICAL_GPUS_VER1

NvAPI_SYS_GetLogicalGPUs = hDll.SYS_GetLogicalGPUs
NvAPI_SYS_GetLogicalGPUs.restype = NVAPI_INTERFACE


# ---------------------------------------------------------------------------
# NGX (DLSS) driver feature support -- a support-status query only, not
# the rendering path itself
# ---------------------------------------------------------------------------
NVAPI_MAX_NGX_FEATURES_PER_QUERY = 16


class NV_NGX_DRIVER_FEATURE_ID(ENUM):
    NV_NGX_DRIVER_FEATURE_ID_SET_FLIP_CONFIG_V2 = EnumItem(0x00343dcf).set_string('SetFlipConfig V2')
    NV_NGX_DRIVER_FEATURE_ID_FRAME_PRESENT_NOTIFY_HYBRID = EnumItem(0x836af07b).set_string('FramePresentNotifyHybrid')


class NV_NGX_DRIVER_FEATURE_SUPPORT_INFO(ctypes.Structure):
    _fields_ = [
        ('featureId', NvU32),
        ('flags', NvU32),  # bSupported:1, reserved1:31
        ('reserved2', NvU32 * 2),
    ]


class NV_NGX_GET_DRIVER_FEATURE_SUPPORT_PARAMS_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('featureCount', NvU32),
        ('featureSupportInfo', NV_NGX_DRIVER_FEATURE_SUPPORT_INFO * NVAPI_MAX_NGX_FEATURES_PER_QUERY),
        ('reserved', NvU32 * 6),
    ]


NV_NGX_GET_DRIVER_FEATURE_SUPPORT_PARAMS = NV_NGX_GET_DRIVER_FEATURE_SUPPORT_PARAMS_V1
NV_NGX_GET_DRIVER_FEATURE_SUPPORT_PARAMS_VER1 = MAKE_NVAPI_VERSION(NV_NGX_GET_DRIVER_FEATURE_SUPPORT_PARAMS_V1, 1)
NV_NGX_GET_DRIVER_FEATURE_SUPPORT_PARAMS_VER = NV_NGX_GET_DRIVER_FEATURE_SUPPORT_PARAMS_VER1

NvAPI_NGX_GetDriverFeatureSupport = hDll.NGX_GetDriverFeatureSupport
NvAPI_NGX_GetDriverFeatureSupport.restype = NVAPI_INTERFACE


# ---------------------------------------------------------------------------
# Deprecated since driver release 319 (NVIDIA's own header still carries it,
# and its interface ID is still in the current published ID table, so it's
# included per the agreed scope) -- superseded by physical GPU enumeration
# plus compute-capability checks elsewhere.
# ---------------------------------------------------------------------------
NVAPI_MAX_GPU_PER_TOPOLOGY = 8


class NV_COMPUTE_GPU(ctypes.Structure):
    _fields_ = [
        ('hPhysicalGpu', ctypes.c_void_p),
        ('flags', NvU32),
    ]


# V1 uses a fixed-size embedded array (NVAPI_MAX_GPU_PER_TOPOLOGY entries);
# V2 switched to a caller-allocated pointer, but this driver rejects V2's
# version tag for this specific (deprecated-since-319) call -- confirmed
# live: V1 succeeds, V2 returns NVAPI_INCOMPATIBLE_STRUCT_VERSION. Default
# to V1, the revision this driver actually accepts.
class NV_COMPUTE_GPU_TOPOLOGY_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('gpuCount', NvU32),
        ('computeGpus', NV_COMPUTE_GPU * NVAPI_MAX_GPU_PER_TOPOLOGY),
    ]


class NV_COMPUTE_GPU_TOPOLOGY_V2(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('gpuCount', NvU32),
        ('computeGpus', ctypes.POINTER(NV_COMPUTE_GPU)),
    ]


NV_COMPUTE_GPU_TOPOLOGY = NV_COMPUTE_GPU_TOPOLOGY_V1
NV_COMPUTE_GPU_TOPOLOGY_VER1 = MAKE_NVAPI_VERSION(NV_COMPUTE_GPU_TOPOLOGY_V1, 1)
NV_COMPUTE_GPU_TOPOLOGY_VER2 = MAKE_NVAPI_VERSION(NV_COMPUTE_GPU_TOPOLOGY_V2, 2)
NV_COMPUTE_GPU_TOPOLOGY_VER = NV_COMPUTE_GPU_TOPOLOGY_VER1

NvAPI_GPU_CudaEnumComputeCapableGpus = hDll.GPU_CudaEnumComputeCapableGpus
NvAPI_GPU_CudaEnumComputeCapableGpus.restype = NVAPI_INTERFACE


# ---------------------------------------------------------------------------
# Event callbacks -- genuinely different in kind from everything else ported
# here: async, driver-invoked, and require the caller to keep the ctypes
# callback object alive for as long as it's registered (letting it be
# garbage collected after registration is a real use-after-free risk, since
# the driver holds a raw function pointer into it). Structurally ported and
# confirmed to dispatch/register without error, but NOT verified to
# actually fire a callback in this session -- doing that needs a live event
# (e.g. an actual output-mode change) to trigger during the test.
# ---------------------------------------------------------------------------
class NV_QSYNC_EVENT_DATA(ctypes.Structure):
    _fields_ = [
        ('qsyncEvent', NvU32),
        ('reserved', NvU32 * 7),
    ]


NVAPI_CALLBACK_QSYNCEVENT = ctypes.CFUNCTYPE(None, NV_QSYNC_EVENT_DATA, ctypes.c_void_p)


class NV_DISPLAY_OUTPUT_MODE_CHANGE_EVENT_DATA(ctypes.Structure):
    _fields_ = [
        ('displayId', NvU32),
        ('outputMode', NvU32),
    ]


NVAPI_CALLBACK_DISPLAY_OUTPUT_MODE_CHANGE_EVENT = ctypes.CFUNCTYPE(
    None, ctypes.POINTER(NV_DISPLAY_OUTPUT_MODE_CHANGE_EVENT_DATA), ctypes.c_void_p
)


class NV_DISPLAY_COLORIMETRY_CHANGE_EVENT_DATA(ctypes.Structure):
    _fields_ = [
        ('displayId', NvU32),
        ('min_luminance', ctypes.c_float),
        ('max_full_frame_luminance', ctypes.c_float),
        ('max_luminance', ctypes.c_float),
        ('hdrBrightnessLuminanceScalingFactor', ctypes.c_float),
        ('red_primary_x', ctypes.c_float),
        ('red_primary_y', ctypes.c_float),
        ('green_primary_x', ctypes.c_float),
        ('green_primary_y', ctypes.c_float),
        ('blue_primary_x', ctypes.c_float),
        ('blue_primary_y', ctypes.c_float),
        ('white_point_x', ctypes.c_float),
        ('white_point_y', ctypes.c_float),
    ]


NVAPI_CALLBACK_DISPLAY_COLORIMETRY_CHANGE_EVENT = ctypes.CFUNCTYPE(
    None, ctypes.POINTER(NV_DISPLAY_COLORIMETRY_CHANGE_EVENT_DATA), ctypes.c_void_p
)


class NV_EVENT_TYPE(ENUM):
    NV_EVENT_TYPE_NONE = EnumItem(0).set_string('None')
    NV_EVENT_TYPE_QSYNC = EnumItem(6).set_string('QSync')
    NV_EVENT_TYPE_DISPLAY_OUTPUT_MODE_CHANGE = EnumItem(103).set_string('Display Output Mode Change')
    NV_EVENT_TYPE_DISPLAY_COLORIMETRY_CHANGE = EnumItem(104).set_string('Display Colorimetry Change')


class _NvCallBackFuncUnion(ctypes.Union):
    _fields_ = [
        ('nvQSYNCEventCallback', NVAPI_CALLBACK_QSYNCEVENT),
        ('nvDisplayOutputModeChangeEventCallback', NVAPI_CALLBACK_DISPLAY_OUTPUT_MODE_CHANGE_EVENT),
        ('nvDisplayColorimetryChangeEventCallback', NVAPI_CALLBACK_DISPLAY_COLORIMETRY_CHANGE_EVENT),
    ]


class NV_EVENT_REGISTER_CALLBACK(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('eventId', NvU32),
        ('callbackParam', ctypes.c_void_p),
        ('nvCallBackFunc', _NvCallBackFuncUnion),
    ]


NV_EVENT_REGISTER_CALLBACK_VERSION = MAKE_NVAPI_VERSION(NV_EVENT_REGISTER_CALLBACK, 1)

NvAPI_Event_RegisterCallback = hDll.Event_RegisterCallback
NvAPI_Event_RegisterCallback.restype = NVAPI_INTERFACE

NvAPI_Event_UnregisterCallback = hDll.Event_UnregisterCallback
NvAPI_Event_UnregisterCallback.restype = NVAPI_INTERFACE


# ---------------------------------------------------------------------------
# Periodic utilization-sample callback (distinct newer API from the
# performance_monitor polling already wrapped elsewhere)
# ---------------------------------------------------------------------------
class NV_CLIENT_CALLBACK_SETTINGS_SUPER_V1(ctypes.Structure):
    _fields_ = [
        ('pCallbackParam', ctypes.c_void_p),
        ('rsvd', NvU8 * 64),
    ]


NV_GPU_CLIENT_CALLBACK_SETTINGS_SUPER_V1 = NV_CLIENT_CALLBACK_SETTINGS_SUPER_V1


class NV_GPU_CLIENT_PERIODIC_CALLBACK_SETTINGS_SUPER_V1(ctypes.Structure):
    _fields_ = [
        ('super', NV_GPU_CLIENT_CALLBACK_SETTINGS_SUPER_V1),
        ('callbackPeriodms', NvU32),
        ('rsvd', NvU8 * 64),
    ]


class NV_GPU_CLIENT_CALLBACK_DATA_SUPER_V1(ctypes.Structure):
    _fields_ = [
        ('pCallbackParam', ctypes.c_void_p),
        ('rsvd', NvU8 * 64),
    ]


class NV_GPU_CLIENT_UTIL_DOMAIN_ID(ENUM):
    NV_GPU_CLIENT_UTIL_DOMAIN_GRAPHICS = EnumItem(0).set_string('Graphics')
    NV_GPU_CLIENT_UTIL_DOMAIN_FRAME_BUFFER = EnumItem(1).set_string('Frame Buffer')
    NV_GPU_CLIENT_UTIL_DOMAIN_VIDEO = EnumItem(2).set_string('Video')
    NV_GPU_CLIENT_UTIL_DOMAIN_RSVD = EnumItem(3).set_string('Reserved')


NV_GPU_CLIENT_UTIL_DOMAINS_MAX_V1 = 4


class NV_GPU_CLIENT_UTILIZATION_DATA_V1(ctypes.Structure):
    _fields_ = [
        ('utilId', NvU32),
        ('utilizationPercent', NvU32),
        ('rsvd', NvU8 * 61),
    ]


class NV_GPU_CLIENT_CALLBACK_UTILIZATION_DATA_V1(ctypes.Structure):
    _fields_ = [
        ('numUtils', NvU32),
        ('timestamp', NvU64),
        ('rsvd', NvU8 * 64),
        ('utils', NV_GPU_CLIENT_UTILIZATION_DATA_V1 * NV_GPU_CLIENT_UTIL_DOMAINS_MAX_V1),
    ]


NV_GPU_CLIENT_UTILIZATION_PERIODIC_CALLBACK_V1 = ctypes.CFUNCTYPE(
    None, ctypes.c_void_p, ctypes.POINTER(NV_GPU_CLIENT_CALLBACK_UTILIZATION_DATA_V1)
)


class NV_GPU_CLIENT_UTILIZATION_PERIODIC_CALLBACK_SETTINGS_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('super', NV_GPU_CLIENT_PERIODIC_CALLBACK_SETTINGS_SUPER_V1),
        ('callback', NV_GPU_CLIENT_UTILIZATION_PERIODIC_CALLBACK_V1),
        ('rsvd', NvU8 * 64),
    ]


NV_GPU_CLIENT_UTILIZATION_PERIODIC_CALLBACK_SETTINGS = NV_GPU_CLIENT_UTILIZATION_PERIODIC_CALLBACK_SETTINGS_V1
NV_GPU_CLIENT_UTILIZATION_PERIODIC_CALLBACK_SETTINGS_VER1 = MAKE_NVAPI_VERSION(
    NV_GPU_CLIENT_UTILIZATION_PERIODIC_CALLBACK_SETTINGS_V1, 1
)
NV_GPU_CLIENT_UTILIZATION_PERIODIC_CALLBACK_SETTINGS_VER = NV_GPU_CLIENT_UTILIZATION_PERIODIC_CALLBACK_SETTINGS_VER1

NvAPI_GPU_ClientRegisterForUtilizationSampleUpdates = hDll.GPU_ClientRegisterForUtilizationSampleUpdates
NvAPI_GPU_ClientRegisterForUtilizationSampleUpdates.restype = NVAPI_INTERFACE


# ---------------------------------------------------------------------------
# NV_GPU_CONNECTOR_INFO -- NvAPI_GPU_GetConnectorInfo
# ---------------------------------------------------------------------------
# Unlike everything else in this file, this function and its interface ID
# are not published anywhere checked: not in NVIDIA's current or archived
# nvapi.h, not in nvapi_interface.h (the source for nvapi_interface_ids.py),
# and not in any community NVAPI port (nvapi-rs, NvAPIWrapper, the Pascal/
# FPC port). Several of those do reference the function by name in doc
# comments copied from NVIDIA's own header -- NV_GPU_DISPLAYIDS.connectorType
# says "get the GPU connector type from
# NvAPI_GPU_GetConnectorInfo/NvAPI_GPU_GetConnectorInfoEx" -- but none
# declare it or its struct.
#
# The interface ID (0x4ECA2C10) is published in several community
# NVAPI-interface-ID lists (e.g. NvAPIWrapper's FunctionId enum), used by
# tools that call it via the same nvapi_QueryInterface dispatch this
# package already uses for every other function. The struct layout below
# was reverse-engineered by probing a live GPU: sweeping candidate
# `version` field values (every 4-byte size from 4-256, revisions 1-6)
# against NvAPI_GPU_GetConnectorInfo(hPhysicalGpu, outputId, buffer) until
# the driver returned NVAPI_OK instead of NVAPI_INCOMPATIBLE_STRUCT_VERSION
# (a safe, non-destructive failure mode observed on every wrong guess), then
# decoding the returned bytes.
#
# Verified against real hardware (a Quadro RTX 4000): decodes correctly as
# 3x DisplayPort External + 1x USB Type-C (the card's actual VirtualLink
# port -- something no other function in this package can detect).
# connectorIndex also correctly groups multiple legacy output-mask bits
# that share one physical jack: this GPU's all_outputs bitmask has 7 set
# bits, but only 4 distinct connectorIndex values, matching its actual 4
# physical connectors.
#
# Fields past connectorIndex were observed to always read back as zero
# across every output on the test GPU; kept as reserved padding rather
# than guessed at.
class NV_GPU_CONNECTOR_INFO(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('reserved0', NvU32),
        ('reserved1', NvU32),
        ('connectorType', NV_GPU_CONNECTOR_TYPE),
        ('connectorIndex', NvU32),
        ('reserved', NvU32 * 6),
    ]


NV_GPU_CONNECTOR_INFO_VER = MAKE_NVAPI_VERSION(NV_GPU_CONNECTOR_INFO, 1)

NVAPI_INTERFACE_IDS['NvAPI_GPU_GetConnectorInfo'] = 0x4ECA2C10
NvAPI_GPU_GetConnectorInfo = hDll.GPU_GetConnectorInfo
NvAPI_GPU_GetConnectorInfo.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetConnectorInfo(NvPhysicalGpuHandle hPhysicalGpu, NvU32 outputId, NV_GPU_CONNECTOR_INFO *pConnectorInfo);
# -- reverse-engineered, not from a published header; see comment above.


# ---------------------------------------------------------------------------
# Undocumented single-out-param GPU info functions
# ---------------------------------------------------------------------------
# None of these are declared in any published NVAPI header (current or
# archived) or listed in NVIDIA's own published nvapi_interface.h -- same
# situation as NvAPI_GPU_GetConnectorInfo above. Unlike GetConnectorInfo,
# though, both the function signatures and interface IDs for these come
# from a real, mature open-source reverse-engineering project (arcnmx/
# nvapi-rs on GitHub -- sys/src/gpu/mod.rs's `private` module for the
# signatures/enum tables, sys/src/nvid.rs for the numeric interface IDs),
# not from black-box probing here. All take a single bare NvU32*/enum*/
# NvAPI_ShortString* out-param -- no struct/version field to get wrong.
#
# Verified live against real hardware (Quadro RTX 4000, TU104 die):
# - short_name correctly returns "TU104GL-A" -- TU104 is the real,
#   publicly documented die used in the Quadro RTX 4000/RTX 2070/2080.
# - ram_maker correctly decodes to Samsung -- plausible for this card's
#   GDDR6.
# - shader_pipe_count (5) returns a different value than the already-
#   verified shader_sub_pipe_count (18) -- confirming these are two
#   distinct real metrics, not the same call under two names.
# - ram_type returned 14, outside the source enum's known range (which
#   tops out at 10/GDDR5X and predates GDDR6 driver support). Added as
#   NV_GPU_RAM_GDDR6 = 14 since it's independently verifiable (TU104 cards
#   are publicly documented to use GDDR6, never GDDR6X), not a guess; 11-13
#   remain unlabeled since nothing pins down what they are.
# - foundry returned NVAPI_NOT_SUPPORTED on the test GPU -- a legitimate
#   per-GPU "not supported" result, not a decode failure.
class NV_GPU_RAM_TYPE(ENUM):
    NV_GPU_RAM_UNKNOWN = EnumItem(0).set_string('Unknown')
    NV_GPU_RAM_SDRAM = EnumItem(1).set_string('SDRAM')
    NV_GPU_RAM_DDR1 = EnumItem(2).set_string('DDR1')
    NV_GPU_RAM_DDR2 = EnumItem(3).set_string('DDR2')
    NV_GPU_RAM_GDDR2 = EnumItem(4).set_string('GDDR2')
    NV_GPU_RAM_GDDR3 = EnumItem(5).set_string('GDDR3')
    NV_GPU_RAM_GDDR4 = EnumItem(6).set_string('GDDR4')
    NV_GPU_RAM_DDR3 = EnumItem(7).set_string('DDR3')
    NV_GPU_RAM_GDDR5 = EnumItem(8).set_string('GDDR5')
    NV_GPU_RAM_LPDDR2 = EnumItem(9).set_string('LPDDR2')
    NV_GPU_RAM_GDDR5X = EnumItem(10).set_string('GDDR5X')
    # 11-13 unknown (not present in the source enum table, which predates
    # GDDR6 driver support -- left unlabeled rather than guessed at). 14
    # confirmed live on a Quadro RTX 4000 (TU104 die, verified separately
    # via short_name) -- TU104-based cards are publicly documented to use
    # GDDR6 (GDDR6X didn't exist until Ampere/GA10x), so this is a
    # verified fact, not a guess.
    NV_GPU_RAM_GDDR6 = EnumItem(14).set_string('GDDR6')


class NV_GPU_RAM_MAKER(ENUM):
    NV_GPU_RAM_MAKER_UNKNOWN = EnumItem(0).set_string('Unknown')
    NV_GPU_RAM_MAKER_SAMSUNG = EnumItem(1).set_string('Samsung')
    NV_GPU_RAM_MAKER_QIMONDA = EnumItem(2).set_string('Qimonda')
    NV_GPU_RAM_MAKER_ELPIDA = EnumItem(3).set_string('Elpida')
    NV_GPU_RAM_MAKER_ETRON = EnumItem(4).set_string('Etron')
    NV_GPU_RAM_MAKER_NANYA = EnumItem(5).set_string('Nanya')
    NV_GPU_RAM_MAKER_HYNIX = EnumItem(6).set_string('Hynix')
    NV_GPU_RAM_MAKER_MOSEL = EnumItem(7).set_string('Mosel')
    NV_GPU_RAM_MAKER_WINBOND = EnumItem(8).set_string('Winbond')
    NV_GPU_RAM_MAKER_ELITE = EnumItem(9).set_string('Elite')
    NV_GPU_RAM_MAKER_MICRON = EnumItem(10).set_string('Micron')


class NV_GPU_FOUNDRY(ENUM):
    NV_GPU_FOUNDRY_UNKNOWN = EnumItem(0).set_string('Unknown')
    NV_GPU_FOUNDRY_TSMC = EnumItem(1).set_string('Taiwan Semiconductor Manufacturing Company (TSMC)')
    NV_GPU_FOUNDRY_UMC = EnumItem(2).set_string('United Microelectronics Corporation (UMC)')
    NV_GPU_FOUNDRY_IBM = EnumItem(3).set_string('IBM Microelectronics')
    NV_GPU_FOUNDRY_SMIC = EnumItem(4).set_string('Semiconductor Manufacturing International Corporation (SMIC)')
    NV_GPU_FOUNDRY_CSM = EnumItem(5).set_string('Chartered Semiconductor Manufacturing (CSM)')
    NV_GPU_FOUNDRY_TOSHIBA = EnumItem(6).set_string('Toshiba Corporation')


NVAPI_INTERFACE_IDS['NvAPI_GPU_GetRamType'] = 0x57f7caac
NvAPI_GPU_GetRamType = hDll.GPU_GetRamType
NvAPI_GPU_GetRamType.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetRamType(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_RAM_TYPE *pMemType);

NVAPI_INTERFACE_IDS['NvAPI_GPU_GetRamMaker'] = 0x42aea16a
NvAPI_GPU_GetRamMaker = hDll.GPU_GetRamMaker
NvAPI_GPU_GetRamMaker.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetRamMaker(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_RAM_MAKER *pRamMaker);

NVAPI_INTERFACE_IDS['NvAPI_GPU_GetRamBankCount'] = 0x17073a3c
NvAPI_GPU_GetRamBankCount = hDll.GPU_GetRamBankCount
NvAPI_GPU_GetRamBankCount.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetRamBankCount(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pRamBankCount);

NVAPI_INTERFACE_IDS['NvAPI_GPU_GetFoundry'] = 0x5d857a00
NvAPI_GPU_GetFoundry = hDll.GPU_GetFoundry
NvAPI_GPU_GetFoundry.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetFoundry(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_FOUNDRY *pFoundry);

NVAPI_INTERFACE_IDS['NvAPI_GPU_GetShaderPipeCount'] = 0x63e2f56f
NvAPI_GPU_GetShaderPipeCount = hDll.GPU_GetShaderPipeCount
NvAPI_GPU_GetShaderPipeCount.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetShaderPipeCount(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pCount);

NVAPI_INTERFACE_IDS['NvAPI_GPU_GetPartitionCount'] = 0x86f05d7a
NvAPI_GPU_GetPartitionCount = hDll.GPU_GetPartitionCount
NvAPI_GPU_GetPartitionCount.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetPartitionCount(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pPartitionCount);

NVAPI_INTERFACE_IDS['NvAPI_GetDriverModel'] = 0x25eeb2c4
NvAPI_GetDriverModel = hDll.GetDriverModel
NvAPI_GetDriverModel.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GetDriverModel(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pDriverModel);

NVAPI_INTERFACE_IDS['NvAPI_GPU_GetShortName'] = 0xd988f0f3
NvAPI_GPU_GetShortName = hDll.GPU_GetShortName
NvAPI_GPU_GetShortName.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetShortName(NvPhysicalGpuHandle hPhysicalGpu, NvAPI_ShortString pName);

NVAPI_INTERFACE_IDS['NvAPI_GPU_GetFBWidthAndLocation'] = 0x11104158
NvAPI_GPU_GetFBWidthAndLocation = hDll.GPU_GetFBWidthAndLocation
NvAPI_GPU_GetFBWidthAndLocation.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetFBWidthAndLocation(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pWidth, NvU32 *pLocation);
