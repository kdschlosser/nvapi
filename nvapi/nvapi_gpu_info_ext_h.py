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


# architecture is globally unique (safe as a flat enum); the same raw
# implementation value means a different chip depending on which
# architecture it's paired with, so implementation is a nested per-
# architecture lookup instead (see NV_GPU_ARCH_IMPLEMENTATION_ID_MAP
# below). Values transcribed from NVIDIA's current nvapi.h
# (NV_GPU_ARCHITECTURE_ID / NV_GPU_ARCH_IMPLEMENTATION_ID /
# NV_GPU_CHIP_REVISION).
class _NV_GPU_ARCHITECTURE_ID(ENUM):
    NV_GPU_ARCHITECTURE_T2X = EnumItem(0xE0000020).set_string('T2X')
    NV_GPU_ARCHITECTURE_T3X = EnumItem(0xE0000030).set_string('T3X')
    # T4X and T12X share the same raw value in NVIDIA's own header
    NV_GPU_ARCHITECTURE_T4X_T12X = EnumItem(0xE0000040).set_string('T4X/T12X')
    NV_GPU_ARCHITECTURE_NV40 = EnumItem(0x00000040).set_string('NV40')
    NV_GPU_ARCHITECTURE_NV50 = EnumItem(0x00000050).set_string('NV50')
    NV_GPU_ARCHITECTURE_G78 = EnumItem(0x00000060).set_string('G78')
    NV_GPU_ARCHITECTURE_G80 = EnumItem(0x00000080).set_string('G80')
    NV_GPU_ARCHITECTURE_G90 = EnumItem(0x00000090).set_string('G90')
    NV_GPU_ARCHITECTURE_GT200 = EnumItem(0x000000A0).set_string('GT200')
    NV_GPU_ARCHITECTURE_GF100 = EnumItem(0x000000C0).set_string('GF100')
    NV_GPU_ARCHITECTURE_GF110 = EnumItem(0x000000D0).set_string('GF110')
    NV_GPU_ARCHITECTURE_GK100 = EnumItem(0x000000E0).set_string('GK100')
    NV_GPU_ARCHITECTURE_GK110 = EnumItem(0x000000F0).set_string('GK110')
    NV_GPU_ARCHITECTURE_GK200 = EnumItem(0x00000100).set_string('GK200')
    NV_GPU_ARCHITECTURE_GM000 = EnumItem(0x00000110).set_string('GM000')
    NV_GPU_ARCHITECTURE_GM200 = EnumItem(0x00000120).set_string('GM200')
    NV_GPU_ARCHITECTURE_GP100 = EnumItem(0x00000130).set_string('GP100')
    NV_GPU_ARCHITECTURE_GV100 = EnumItem(0x00000140).set_string('GV100')
    NV_GPU_ARCHITECTURE_GV110 = EnumItem(0x00000150).set_string('GV110')
    NV_GPU_ARCHITECTURE_TU100 = EnumItem(0x00000160).set_string('TU100')
    NV_GPU_ARCHITECTURE_GA100 = EnumItem(0x00000170).set_string('GA100')
    NV_GPU_ARCHITECTURE_AD100 = EnumItem(0x00000190).set_string('AD100')
    NV_GPU_ARCHITECTURE_GB200 = EnumItem(0x000001B0).set_string('GB200')


NV_GPU_ARCHITECTURE_ID = _NV_GPU_ARCHITECTURE_ID

# keyed by NV_GPU_ARCHITECTURE_ID raw value -> {implementation raw value:
# chip name}. Groupings below follow the blank-line block structure of
# NVIDIA's own header, which is not explicit about which architecture each
# implementation constant belongs to but consistently separates families
# this way.
NV_GPU_ARCH_IMPLEMENTATION_ID_MAP = {
    0xE0000020: {0x0: 'T20'},
    0xE0000030: {0x0: 'T30', 0x5: 'T35'},
    0xE0000040: {0x0: 'T40/T124'},
    0x00000040: {
        0x0: 'NV40', 0x1: 'NV41', 0x2: 'NV42', 0x3: 'NV43', 0x4: 'NV44',
        0xA: 'NV44A', 0x6: 'NV46', 0x7: 'NV47', 0x9: 'NV49', 0xB: 'NV4B',
        0xC: 'NV4C', 0xE: 'NV4E',
    },
    0x00000050: {0x0: 'NV50', 0x3: 'NV63', 0x7: 'NV67'},
    0x00000060: {0x4: 'G84', 0x6: 'G86'},
    0x00000080: {0x2: 'G92', 0x4: 'G94', 0x6: 'G96', 0x8: 'G98'},
    0x000000A0: {
        0x0: 'GT200', 0x2: 'GT212', 0x4: 'GT214', 0x3: 'GT215', 0x5: 'GT216',
        0x8: 'GT218', 0xA: 'MCP77', 0xB: 'GT21C', 0xC: 'MCP79', 0xD: 'GT21A',
        0xF: 'MCP89',
    },
    0x000000C0: {0x0: 'GF100', 0x4: 'GF104', 0x3: 'GF106', 0x1: 'GF108'},
    0x000000D0: {0x0: 'GF110', 0x6: 'GF116', 0x7: 'GF117', 0x8: 'GF118', 0x9: 'GF119'},
    0x000000E0: {0x4: 'GK104', 0x6: 'GK106', 0x7: 'GK107', 0xA: 'GK20A', 0x0: 'GK110'},
    0x00000100: {0x8: 'GK208'},
    0x00000120: {0x4: 'GM204', 0x6: 'GM206'},
    0x00000130: {
        0x0: 'GP100', 0x1: 'GP000', 0x2: 'GP102', 0x4: 'GP104', 0x6: 'GP106',
        0x7: 'GP107', 0x8: 'GP108',
    },
    0x00000140: {0x0: 'GV100', 0xB: 'GV10B'},
    0x00000160: {
        0x0: 'TU100', 0x1: 'TU000', 0x2: 'TU102', 0x4: 'TU104', 0x6: 'TU106',
        0x7: 'TU117', 0x8: 'TU116',
    },
    0x00000170: {0x0: 'GA100', 0x2: 'GA102', 0x4: 'GA104'},
    0x00000190: {0x2: 'AD102', 0x3: 'AD103', 0x4: 'AD104'},
    0x000001B0: {0x2: 'GB202'},
}


def get_arch_implementation_name(architecture, implementation):
    return NV_GPU_ARCH_IMPLEMENTATION_ID_MAP.get(int(architecture), {}).get(int(implementation))


class _NV_GPU_CHIP_REVISION(ENUM):
    NV_GPU_CHIP_REV_EMULATION_QT = EnumItem(0x00000000).set_string('Emulation (QT)')
    NV_GPU_CHIP_REV_EMULATION_FPGA = EnumItem(0x00000001).set_string('Emulation (FPGA)')
    NV_GPU_CHIP_REV_A01 = EnumItem(0x00000011).set_string('A01')
    NV_GPU_CHIP_REV_A02 = EnumItem(0x00000012).set_string('A02')
    NV_GPU_CHIP_REV_A03 = EnumItem(0x00000013).set_string('A03')
    NV_GPU_CHIP_REV_UNKNOWN = EnumItem(0xFFFFFFFF).set_string('Unknown')


NV_GPU_CHIP_REVISION = _NV_GPU_CHIP_REVISION


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


# capsTbl bitmask from NvAPI_GPU_NVLINK_GetCaps(); VALID and
# UNCONTAINED_ERROR_RECOVERY are documented as per-link caps only, not
# global caps, but are decoded the same way either way.
class _NVAPI_NVLINK_CAPS(ENUM):
    NVAPI_NVLINK_CAPS_SUPPORTED = EnumItem(0x00000001).set_string('Supported')
    NVAPI_NVLINK_CAPS_P2P_SUPPORTED = EnumItem(0x00000002).set_string('P2P Supported')
    NVAPI_NVLINK_CAPS_SYSMEM_ACCESS = EnumItem(0x00000004).set_string('Sysmem Access')
    NVAPI_NVLINK_CAPS_P2P_ATOMICS = EnumItem(0x00000008).set_string('P2P Atomics')
    NVAPI_NVLINK_CAPS_SYSMEM_ATOMICS = EnumItem(0x00000010).set_string('Sysmem Atomics')
    NVAPI_NVLINK_CAPS_PEX_TUNNELING = EnumItem(0x00000020).set_string('PEX Tunneling')
    NVAPI_NVLINK_CAPS_SLI_BRIDGE = EnumItem(0x00000040).set_string('SLI Bridge')
    NVAPI_NVLINK_CAPS_SLI_BRIDGE_SENSABLE = EnumItem(0x00000080).set_string('SLI Bridge Sensable')
    NVAPI_NVLINK_CAPS_POWER_STATE_L0 = EnumItem(0x00000100).set_string('Power State L0')
    NVAPI_NVLINK_CAPS_POWER_STATE_L1 = EnumItem(0x00000200).set_string('Power State L1')
    NVAPI_NVLINK_CAPS_POWER_STATE_L2 = EnumItem(0x00000400).set_string('Power State L2')
    NVAPI_NVLINK_CAPS_POWER_STATE_L3 = EnumItem(0x00000800).set_string('Power State L3')
    NVAPI_NVLINK_CAPS_VALID = EnumItem(0x00001000).set_string('Valid')
    NVAPI_NVLINK_CAPS_UNCONTAINED_ERROR_RECOVERY = EnumItem(0x00002000).set_string('Uncontained Error Recovery')


NVAPI_NVLINK_CAPS = _NVAPI_NVLINK_CAPS


# same value table for both NVLINK_CAPS_NVLINK_VERSION_* and
# NVLINK_CAPS_NCI_VERSION_* -- NVIDIA's header defines two macro sets with
# identical values for these, one enum covers both.
class _NVAPI_NVLINK_VERSION(ENUM):
    NVAPI_NVLINK_VERSION_INVALID = EnumItem(0x00000000).set_string('Invalid')
    NVAPI_NVLINK_VERSION_1_0 = EnumItem(0x00000001).set_string('1.0')
    NVAPI_NVLINK_VERSION_2_0 = EnumItem(0x00000002).set_string('2.0')
    NVAPI_NVLINK_VERSION_2_2 = EnumItem(0x00000004).set_string('2.2')
    NVAPI_NVLINK_VERSION_3_0 = EnumItem(0x00000005).set_string('3.0')
    NVAPI_NVLINK_VERSION_3_1 = EnumItem(0x00000006).set_string('3.1')
    NVAPI_NVLINK_VERSION_4_0 = EnumItem(0x00000007).set_string('4.0')
    NVAPI_NVLINK_VERSION_5_0 = EnumItem(0x00000008).set_string('5.0')


NVAPI_NVLINK_VERSION = _NVAPI_NVLINK_VERSION


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
    # 11 still unlabeled -- not present in either source list. 12/14/15
    # added from a second list the user found; 14 matches the
    # independently-verified live value below exactly.
    NV_GPU_RAM_HBM2 = EnumItem(12).set_string('HBM2')
    # 13 still unlabeled -- not present in either source list.
    # confirmed live on a Quadro RTX 4000 (TU104 die, verified separately
    # via short_name) -- TU104-based cards are publicly documented to use
    # GDDR6 (GDDR6X didn't exist until Ampere/GA10x), so this is a
    # verified fact, not a guess.
    NV_GPU_RAM_GDDR6 = EnumItem(14).set_string('GDDR6')
    NV_GPU_RAM_GDDR6X = EnumItem(15).set_string('GDDR6X')


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


# ---------------------------------------------------------------------------
# Fan/cooler control -- not in NVIDIA's public header at all (the only
# officially documented fan function is NvAPI_GPU_GetTachReading, already
# wired up elsewhere). Everything below is private/undocumented. Structs,
# enums and function signatures transcribed from falahati/NvAPIWrapper
# (https://github.com/falahati/NvAPIWrapper, MIT licensed), the same
# community source already used for NvAPI_GPU_GetConnectorInfo; interface
# IDs from arcnmx/nvapi-rs (https://github.com/arcnmx/nvapi-rs).
#
# Two generations exist:
#  - the legacy "Cooler" API (GetCoolerSettings/SetCoolerLevels/
#    RestoreCoolerSettings/GetCoolerPolicyTable/SetCoolerPolicyTable/
#    RestoreCoolerPolicyTable) -- older GPUs.
#  - the modern "ClientFanCoolers" API (GetInfo/GetStatus/GetControl/
#    SetControl) -- what current-generation GPUs use.
# ---------------------------------------------------------------------------
class _NV_COOLER_TYPE(ENUM):
    NVAPI_COOLER_TYPE_NONE = EnumItem(0).set_string('None')
    NVAPI_COOLER_TYPE_FAN = EnumItem(1).set_string('Fan')
    NVAPI_COOLER_TYPE_WATER = EnumItem(2).set_string('Water')
    NVAPI_COOLER_TYPE_LIQUID_NITROGEN = EnumItem(3).set_string('Liquid Nitrogen')


NV_COOLER_TYPE = _NV_COOLER_TYPE


class _NV_COOLER_CONTROLLER(ENUM):
    NVAPI_COOLER_CONTROLLER_NONE = EnumItem(0).set_string('None')
    NVAPI_COOLER_CONTROLLER_ADI = EnumItem(1).set_string('ADI')
    NVAPI_COOLER_CONTROLLER_INTERNAL = EnumItem(2).set_string('Internal')


NV_COOLER_CONTROLLER = _NV_COOLER_CONTROLLER


# bitmask
class _NV_COOLER_POLICY(ENUM):
    NVAPI_COOLER_POLICY_NONE = EnumItem(0).set_string('None')
    NVAPI_COOLER_POLICY_MANUAL = EnumItem(0b1).set_string('Manual')
    NVAPI_COOLER_POLICY_PERFORMANCE = EnumItem(0b10).set_string('Performance')
    NVAPI_COOLER_POLICY_TEMPERATURE_DISCRETE = EnumItem(0b100).set_string('Temperature Discrete')
    NVAPI_COOLER_POLICY_TEMPERATURE_CONTINUOUS = EnumItem(0b1000).set_string('Temperature Continuous')
    NVAPI_COOLER_POLICY_SILENT = EnumItem(0b10000).set_string('Silent')


NV_COOLER_POLICY = _NV_COOLER_POLICY


# bitmask
class _NV_COOLER_TARGET(ENUM):
    NVAPI_COOLER_TARGET_NONE = EnumItem(0).set_string('None')
    NVAPI_COOLER_TARGET_GPU = EnumItem(0b1).set_string('GPU')
    NVAPI_COOLER_TARGET_MEMORY = EnumItem(0b10).set_string('Memory')
    NVAPI_COOLER_TARGET_POWER_SUPPLY = EnumItem(0b100).set_string('Power Supply')
    NVAPI_COOLER_TARGET_ALL = EnumItem(0b111).set_string('All')


NV_COOLER_TARGET = _NV_COOLER_TARGET


class _NV_COOLER_CONTROL_MODE(ENUM):
    NVAPI_COOLER_CONTROL_MODE_NONE = EnumItem(0).set_string('None')
    NVAPI_COOLER_CONTROL_MODE_TOGGLE = EnumItem(1).set_string('Toggle')
    NVAPI_COOLER_CONTROL_MODE_VARIABLE = EnumItem(2).set_string('Variable')


NV_COOLER_CONTROL_MODE = _NV_COOLER_CONTROL_MODE


NVAPI_MAX_COOLERS_PER_GPU = 3
NVAPI_MAX_COOLER_POLICY_LEVELS = 24


class NV_COOLER_SETTING(ctypes.Structure):
    _fields_ = [
        ('coolerType', NvU32),
        ('controller', NvU32),
        ('defaultMinLevel', NvU32),
        ('defaultMaxLevel', NvU32),
        ('currentMinLevel', NvU32),
        ('currentMaxLevel', NvU32),
        ('currentLevel', NvU32),
        ('defaultPolicy', NvU32),
        ('currentPolicy', NvU32),
        ('target', NvU32),
        ('controlMode', NvU32),
        ('isActive', NvU32),
    ]


class NV_GPU_COOLER_SETTINGS_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('count', NvU32),
        ('settings', NV_COOLER_SETTING * NVAPI_MAX_COOLERS_PER_GPU),
    ]


NV_GPU_COOLER_SETTINGS = NV_GPU_COOLER_SETTINGS_V1
NV_GPU_COOLER_SETTINGS_VER1 = MAKE_NVAPI_VERSION(NV_GPU_COOLER_SETTINGS_V1, 1)
NV_GPU_COOLER_SETTINGS_VER = NV_GPU_COOLER_SETTINGS_VER1

NVAPI_INTERFACE_IDS['NvAPI_GPU_GetCoolerSettings'] = 0xda141340
NvAPI_GPU_GetCoolerSettings = hDll.GPU_GetCoolerSettings
NvAPI_GPU_GetCoolerSettings.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetCoolerSettings(NvPhysicalGpuHandle hPhysicalGpu, NV_COOLER_TARGET coolerTarget, NV_GPU_COOLER_SETTINGS *pCoolerSettings);


class NV_COOLER_LEVEL_ENTRY(ctypes.Structure):
    _fields_ = [
        ('currentLevel', NvU32),
        ('currentPolicy', NvU32),
    ]


class NV_GPU_COOLER_LEVELS_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('levels', NV_COOLER_LEVEL_ENTRY * NVAPI_MAX_COOLERS_PER_GPU),
    ]


NV_GPU_COOLER_LEVELS = NV_GPU_COOLER_LEVELS_V1
NV_GPU_COOLER_LEVELS_VER1 = MAKE_NVAPI_VERSION(NV_GPU_COOLER_LEVELS_V1, 1)
NV_GPU_COOLER_LEVELS_VER = NV_GPU_COOLER_LEVELS_VER1

NVAPI_INTERFACE_IDS['NvAPI_GPU_SetCoolerLevels'] = 0x891fa0ae
NvAPI_GPU_SetCoolerLevels = hDll.GPU_SetCoolerLevels
NvAPI_GPU_SetCoolerLevels.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_SetCoolerLevels(NvPhysicalGpuHandle hPhysicalGpu, NvU32 coolerIndex, NV_GPU_COOLER_LEVELS *pCoolerLevels, NvU32 count);

NVAPI_INTERFACE_IDS['NvAPI_GPU_RestoreCoolerSettings'] = 0x8f6ed0fb
NvAPI_GPU_RestoreCoolerSettings = hDll.GPU_RestoreCoolerSettings
NvAPI_GPU_RestoreCoolerSettings.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_RestoreCoolerSettings(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *coolerIndexes, NvU32 count);


class NV_COOLER_POLICY_TABLE_ENTRY(ctypes.Structure):
    _fields_ = [
        ('entryId', NvU32),
        ('currentLevel', NvU32),
        ('defaultLevel', NvU32),
    ]


class NV_GPU_COOLER_POLICY_TABLE_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('policy', NvU32),
        ('entries', NV_COOLER_POLICY_TABLE_ENTRY * NVAPI_MAX_COOLER_POLICY_LEVELS),
    ]


NV_GPU_COOLER_POLICY_TABLE = NV_GPU_COOLER_POLICY_TABLE_V1
NV_GPU_COOLER_POLICY_TABLE_VER1 = MAKE_NVAPI_VERSION(NV_GPU_COOLER_POLICY_TABLE_V1, 1)
NV_GPU_COOLER_POLICY_TABLE_VER = NV_GPU_COOLER_POLICY_TABLE_VER1

NVAPI_INTERFACE_IDS['NvAPI_GPU_GetCoolerPolicyTable'] = 0x0518a32c
NvAPI_GPU_GetCoolerPolicyTable = hDll.GPU_GetCoolerPolicyTable
NvAPI_GPU_GetCoolerPolicyTable.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetCoolerPolicyTable(NvPhysicalGpuHandle hPhysicalGpu, NvU32 coolerIndex, NV_GPU_COOLER_POLICY_TABLE *pPolicyTable, NvU32 *pCount);

NVAPI_INTERFACE_IDS['NvAPI_GPU_SetCoolerPolicyTable'] = 0x987947cd
NvAPI_GPU_SetCoolerPolicyTable = hDll.GPU_SetCoolerPolicyTable
NvAPI_GPU_SetCoolerPolicyTable.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_SetCoolerPolicyTable(NvPhysicalGpuHandle hPhysicalGpu, NvU32 coolerIndex, NV_GPU_COOLER_POLICY_TABLE *pPolicyTable, NvU32 count);

NVAPI_INTERFACE_IDS['NvAPI_GPU_RestoreCoolerPolicyTable'] = 0xd8c4fe63
NvAPI_GPU_RestoreCoolerPolicyTable = hDll.GPU_RestoreCoolerPolicyTable
NvAPI_GPU_RestoreCoolerPolicyTable.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_RestoreCoolerPolicyTable(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *coolerIndexes, NvU32 count, NV_COOLER_POLICY policy);

NVAPI_INTERFACE_IDS['NvAPI_GPU_GetCurrentFanSpeedLevel'] = 0xbd71f0c9
NvAPI_GPU_GetCurrentFanSpeedLevel = hDll.GPU_GetCurrentFanSpeedLevel
NvAPI_GPU_GetCurrentFanSpeedLevel.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_GetCurrentFanSpeedLevel(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pFanLevel);


# --- modern ClientFanCoolers API ---
# bitmask
class _NV_FAN_COOLERS_CONTROL_MODE(ENUM):
    NVAPI_FAN_COOLERS_CONTROL_MODE_AUTO = EnumItem(0).set_string('Auto')
    NVAPI_FAN_COOLERS_CONTROL_MODE_MANUAL = EnumItem(0b1).set_string('Manual')


NV_FAN_COOLERS_CONTROL_MODE = _NV_FAN_COOLERS_CONTROL_MODE

NVAPI_MAX_FAN_COOLERS_PER_GPU = 32


class NV_FAN_COOLERS_INFO_ENTRY(ctypes.Structure):
    _fields_ = [
        ('coolerId', NvU32),
        ('unknown1', NvU32),
        ('unknown2', NvU32),
        ('maximumRPM', NvU32),
        ('reserved', NvU32 * 8),
    ]


class NV_GPU_CLIENT_FAN_COOLERS_INFO_V1(ctypes.Structure):
    # JustAMan/pynvraw independently identifies this leading field (called
    # unknown1/unknown in falahati/NvAPIWrapper) as a `supported` bool --
    # same byte offset/struct size either way (bool + padding == a full
    # uint32 field), verified by comparing ctypes.sizeof() of both layouts.
    _fields_ = [
        ('version', NvU32),
        ('supported', ctypes.c_bool),
        ('count', NvU32),
        ('reserved', NvU32 * 8),
        ('entries', NV_FAN_COOLERS_INFO_ENTRY * NVAPI_MAX_FAN_COOLERS_PER_GPU),
    ]


NV_GPU_CLIENT_FAN_COOLERS_INFO = NV_GPU_CLIENT_FAN_COOLERS_INFO_V1
NV_GPU_CLIENT_FAN_COOLERS_INFO_VER1 = MAKE_NVAPI_VERSION(NV_GPU_CLIENT_FAN_COOLERS_INFO_V1, 1)
NV_GPU_CLIENT_FAN_COOLERS_INFO_VER = NV_GPU_CLIENT_FAN_COOLERS_INFO_VER1

NVAPI_INTERFACE_IDS['NvAPI_GPU_ClientFanCoolersGetInfo'] = 0xfb85b01e
NvAPI_GPU_ClientFanCoolersGetInfo = hDll.GPU_ClientFanCoolersGetInfo
NvAPI_GPU_ClientFanCoolersGetInfo.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_ClientFanCoolersGetInfo(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_CLIENT_FAN_COOLERS_INFO *pInfo);


class NV_FAN_COOLERS_STATUS_ENTRY(ctypes.Structure):
    _fields_ = [
        ('coolerId', NvU32),
        ('currentRPM', NvU32),
        ('currentMinimumLevel', NvU32),
        ('currentMaximumLevel', NvU32),
        ('currentLevel', NvU32),
        ('reserved', NvU32 * 8),
    ]


class NV_GPU_CLIENT_FAN_COOLERS_STATUS_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('count', NvU32),
        ('reserved', NvU32 * 8),
        ('entries', NV_FAN_COOLERS_STATUS_ENTRY * NVAPI_MAX_FAN_COOLERS_PER_GPU),
    ]


NV_GPU_CLIENT_FAN_COOLERS_STATUS = NV_GPU_CLIENT_FAN_COOLERS_STATUS_V1
NV_GPU_CLIENT_FAN_COOLERS_STATUS_VER1 = MAKE_NVAPI_VERSION(NV_GPU_CLIENT_FAN_COOLERS_STATUS_V1, 1)
NV_GPU_CLIENT_FAN_COOLERS_STATUS_VER = NV_GPU_CLIENT_FAN_COOLERS_STATUS_VER1

NVAPI_INTERFACE_IDS['NvAPI_GPU_ClientFanCoolersGetStatus'] = 0x35aed5e8
NvAPI_GPU_ClientFanCoolersGetStatus = hDll.GPU_ClientFanCoolersGetStatus
NvAPI_GPU_ClientFanCoolersGetStatus.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_ClientFanCoolersGetStatus(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_CLIENT_FAN_COOLERS_STATUS *pStatus);


class NV_FAN_COOLERS_CONTROL_ENTRY(ctypes.Structure):
    _fields_ = [
        ('coolerId', NvU32),
        ('level', NvU32),
        ('controlMode', NvU32),
        ('reserved', NvU32 * 8),
    ]


class NV_GPU_CLIENT_FAN_COOLERS_CONTROL_V1(ctypes.Structure):
    _fields_ = [
        ('version', NvU32),
        ('unknown1', NvU32),
        ('count', NvU32),
        ('reserved', NvU32 * 8),
        ('entries', NV_FAN_COOLERS_CONTROL_ENTRY * NVAPI_MAX_FAN_COOLERS_PER_GPU),
    ]


NV_GPU_CLIENT_FAN_COOLERS_CONTROL = NV_GPU_CLIENT_FAN_COOLERS_CONTROL_V1
NV_GPU_CLIENT_FAN_COOLERS_CONTROL_VER1 = MAKE_NVAPI_VERSION(NV_GPU_CLIENT_FAN_COOLERS_CONTROL_V1, 1)
NV_GPU_CLIENT_FAN_COOLERS_CONTROL_VER = NV_GPU_CLIENT_FAN_COOLERS_CONTROL_VER1

NVAPI_INTERFACE_IDS['NvAPI_GPU_ClientFanCoolersGetControl'] = 0x814b209f
NvAPI_GPU_ClientFanCoolersGetControl = hDll.GPU_ClientFanCoolersGetControl
NvAPI_GPU_ClientFanCoolersGetControl.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_ClientFanCoolersGetControl(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_CLIENT_FAN_COOLERS_CONTROL *pControl);

NVAPI_INTERFACE_IDS['NvAPI_GPU_ClientFanCoolersSetControl'] = 0xa58971a5
NvAPI_GPU_ClientFanCoolersSetControl = hDll.GPU_ClientFanCoolersSetControl
NvAPI_GPU_ClientFanCoolersSetControl.restype = NVAPI_INTERFACE
# NVAPI_INTERFACE NvAPI_GPU_ClientFanCoolersSetControl(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_CLIENT_FAN_COOLERS_CONTROL *pControl);
