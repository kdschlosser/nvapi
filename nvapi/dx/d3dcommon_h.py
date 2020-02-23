import ctypes
import comtypes

from comtypes.GUID import GUID
from ctypes.wintypes import (
    INT,
    LPCVOID,
    UINT,
    LPCSTR,
    LPVOID,
)

VOID = ctypes.c_void_p
HRESULT = ctypes.c_long
SIZE_T = ctypes.c_size_t
POINTER = ctypes.POINTER
COMMETHOD = comtypes.COMMETHOD
helpstring = comtypes.helpstring


class ENUM(INT):
    pass


class _D3D_SHADER_MACRO(ctypes.Structure):
    pass


D3D_SHADER_MACRO = _D3D_SHADER_MACRO


def annotation(value):
    if '_opt_' in value:
        return comtypes.defaultvalue(None)
    else:
        return None

IID_ID3D10Blob = GUID(
    "{8BA5FB08-5195-40E2-AC58-0D989C3A0102}"
)


class ID3D10Blob(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_ID3D10Blob


IID_ID3DDestructionNotifier = GUID(
    "{A06EB39A-50DA-425B-8C31-4EECD6C270F3}"
)


class ID3DDestructionNotifier(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ID3DDestructionNotifier
    _idlflags_ = []


class D3D_DRIVER_TYPE(ENUM):
    D3D_DRIVER_TYPE_UNKNOWN = 0
    D3D_DRIVER_TYPE_HARDWARE = D3D_DRIVER_TYPE_UNKNOWN + 1
    D3D_DRIVER_TYPE_REFERENCE = D3D_DRIVER_TYPE_HARDWARE + 1
    D3D_DRIVER_TYPE_NULL = D3D_DRIVER_TYPE_REFERENCE + 1
    D3D_DRIVER_TYPE_SOFTWARE = D3D_DRIVER_TYPE_NULL + 1
    D3D_DRIVER_TYPE_WARP = D3D_DRIVER_TYPE_SOFTWARE + 1


class D3D_FEATURE_LEVEL(ENUM):
    D3D_FEATURE_LEVEL_9_1 = 0x9100
    D3D_FEATURE_LEVEL_9_2 = 0x9200
    D3D_FEATURE_LEVEL_9_3 = 0x9300
    D3D_FEATURE_LEVEL_10_0 = 0xA000
    D3D_FEATURE_LEVEL_10_1 = 0xA100
    D3D_FEATURE_LEVEL_11_0 = 0xB000
    D3D_FEATURE_LEVEL_11_1 = 0xB100
    D3D_FEATURE_LEVEL_12_0 = 0xC000
    D3D_FEATURE_LEVEL_12_1 = 0xC100


class D3D_PRIMITIVE_TOPOLOGY(ENUM):
    D3D_PRIMITIVE_TOPOLOGY_UNDEFINED = 0
    D3D_PRIMITIVE_TOPOLOGY_POINTLIST = 1
    D3D_PRIMITIVE_TOPOLOGY_LINELIST = 2
    D3D_PRIMITIVE_TOPOLOGY_LINESTRIP = 3
    D3D_PRIMITIVE_TOPOLOGY_TRIANGLELIST = 4
    D3D_PRIMITIVE_TOPOLOGY_TRIANGLESTRIP = 5
    D3D_PRIMITIVE_TOPOLOGY_LINELIST_ADJ = 10
    D3D_PRIMITIVE_TOPOLOGY_LINESTRIP_ADJ = 11
    D3D_PRIMITIVE_TOPOLOGY_TRIANGLELIST_ADJ = 12
    D3D_PRIMITIVE_TOPOLOGY_TRIANGLESTRIP_ADJ = 13
    D3D_PRIMITIVE_TOPOLOGY_1_CONTROL_POINT_PATCHLIST = 33
    D3D_PRIMITIVE_TOPOLOGY_2_CONTROL_POINT_PATCHLIST = 34
    D3D_PRIMITIVE_TOPOLOGY_3_CONTROL_POINT_PATCHLIST = 35
    D3D_PRIMITIVE_TOPOLOGY_4_CONTROL_POINT_PATCHLIST = 36
    D3D_PRIMITIVE_TOPOLOGY_5_CONTROL_POINT_PATCHLIST = 37
    D3D_PRIMITIVE_TOPOLOGY_6_CONTROL_POINT_PATCHLIST = 38
    D3D_PRIMITIVE_TOPOLOGY_7_CONTROL_POINT_PATCHLIST = 39
    D3D_PRIMITIVE_TOPOLOGY_8_CONTROL_POINT_PATCHLIST = 40
    D3D_PRIMITIVE_TOPOLOGY_9_CONTROL_POINT_PATCHLIST = 41
    D3D_PRIMITIVE_TOPOLOGY_10_CONTROL_POINT_PATCHLIST = 42
    D3D_PRIMITIVE_TOPOLOGY_11_CONTROL_POINT_PATCHLIST = 43
    D3D_PRIMITIVE_TOPOLOGY_12_CONTROL_POINT_PATCHLIST = 44
    D3D_PRIMITIVE_TOPOLOGY_13_CONTROL_POINT_PATCHLIST = 45
    D3D_PRIMITIVE_TOPOLOGY_14_CONTROL_POINT_PATCHLIST = 46
    D3D_PRIMITIVE_TOPOLOGY_15_CONTROL_POINT_PATCHLIST = 47
    D3D_PRIMITIVE_TOPOLOGY_16_CONTROL_POINT_PATCHLIST = 48
    D3D_PRIMITIVE_TOPOLOGY_17_CONTROL_POINT_PATCHLIST = 49
    D3D_PRIMITIVE_TOPOLOGY_18_CONTROL_POINT_PATCHLIST = 50
    D3D_PRIMITIVE_TOPOLOGY_19_CONTROL_POINT_PATCHLIST = 51
    D3D_PRIMITIVE_TOPOLOGY_20_CONTROL_POINT_PATCHLIST = 52
    D3D_PRIMITIVE_TOPOLOGY_21_CONTROL_POINT_PATCHLIST = 53
    D3D_PRIMITIVE_TOPOLOGY_22_CONTROL_POINT_PATCHLIST = 54
    D3D_PRIMITIVE_TOPOLOGY_23_CONTROL_POINT_PATCHLIST = 55
    D3D_PRIMITIVE_TOPOLOGY_24_CONTROL_POINT_PATCHLIST = 56
    D3D_PRIMITIVE_TOPOLOGY_25_CONTROL_POINT_PATCHLIST = 57
    D3D_PRIMITIVE_TOPOLOGY_26_CONTROL_POINT_PATCHLIST = 58
    D3D_PRIMITIVE_TOPOLOGY_27_CONTROL_POINT_PATCHLIST = 59
    D3D_PRIMITIVE_TOPOLOGY_28_CONTROL_POINT_PATCHLIST = 60
    D3D_PRIMITIVE_TOPOLOGY_29_CONTROL_POINT_PATCHLIST = 61
    D3D_PRIMITIVE_TOPOLOGY_30_CONTROL_POINT_PATCHLIST = 62
    D3D_PRIMITIVE_TOPOLOGY_31_CONTROL_POINT_PATCHLIST = 63
    D3D_PRIMITIVE_TOPOLOGY_32_CONTROL_POINT_PATCHLIST = 64
    D3D10_PRIMITIVE_TOPOLOGY_UNDEFINED = D3D_PRIMITIVE_TOPOLOGY_UNDEFINED
    D3D10_PRIMITIVE_TOPOLOGY_POINTLIST = D3D_PRIMITIVE_TOPOLOGY_POINTLIST
    D3D10_PRIMITIVE_TOPOLOGY_LINELIST = D3D_PRIMITIVE_TOPOLOGY_LINELIST
    D3D10_PRIMITIVE_TOPOLOGY_LINESTRIP = D3D_PRIMITIVE_TOPOLOGY_LINESTRIP
    D3D10_PRIMITIVE_TOPOLOGY_TRIANGLELIST = (
        D3D_PRIMITIVE_TOPOLOGY_TRIANGLELIST
    )
    D3D10_PRIMITIVE_TOPOLOGY_TRIANGLESTRIP = (
        D3D_PRIMITIVE_TOPOLOGY_TRIANGLESTRIP
    )
    D3D10_PRIMITIVE_TOPOLOGY_LINELIST_ADJ = (
        D3D_PRIMITIVE_TOPOLOGY_LINELIST_ADJ
    )
    D3D10_PRIMITIVE_TOPOLOGY_LINESTRIP_ADJ = (
        D3D_PRIMITIVE_TOPOLOGY_LINESTRIP_ADJ
    )
    D3D10_PRIMITIVE_TOPOLOGY_TRIANGLELIST_ADJ = (
        D3D_PRIMITIVE_TOPOLOGY_TRIANGLELIST_ADJ
    )
    D3D10_PRIMITIVE_TOPOLOGY_TRIANGLESTRIP_ADJ = (
        D3D_PRIMITIVE_TOPOLOGY_TRIANGLESTRIP_ADJ
    )
    D3D11_PRIMITIVE_TOPOLOGY_UNDEFINED = D3D_PRIMITIVE_TOPOLOGY_UNDEFINED
    D3D11_PRIMITIVE_TOPOLOGY_POINTLIST = D3D_PRIMITIVE_TOPOLOGY_POINTLIST
    D3D11_PRIMITIVE_TOPOLOGY_LINELIST = D3D_PRIMITIVE_TOPOLOGY_LINELIST
    D3D11_PRIMITIVE_TOPOLOGY_LINESTRIP = D3D_PRIMITIVE_TOPOLOGY_LINESTRIP
    D3D11_PRIMITIVE_TOPOLOGY_TRIANGLELIST = (
        D3D_PRIMITIVE_TOPOLOGY_TRIANGLELIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_TRIANGLESTRIP = (
        D3D_PRIMITIVE_TOPOLOGY_TRIANGLESTRIP
    )
    D3D11_PRIMITIVE_TOPOLOGY_LINELIST_ADJ = (
        D3D_PRIMITIVE_TOPOLOGY_LINELIST_ADJ
    )
    D3D11_PRIMITIVE_TOPOLOGY_LINESTRIP_ADJ = (
        D3D_PRIMITIVE_TOPOLOGY_LINESTRIP_ADJ
    )
    D3D11_PRIMITIVE_TOPOLOGY_TRIANGLELIST_ADJ = (
        D3D_PRIMITIVE_TOPOLOGY_TRIANGLELIST_ADJ
    )
    D3D11_PRIMITIVE_TOPOLOGY_TRIANGLESTRIP_ADJ = (
        D3D_PRIMITIVE_TOPOLOGY_TRIANGLESTRIP_ADJ
    )
    D3D11_PRIMITIVE_TOPOLOGY_1_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_1_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_2_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_2_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_3_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_3_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_4_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_4_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_5_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_5_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_6_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_6_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_7_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_7_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_8_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_8_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_9_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_9_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_10_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_10_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_11_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_11_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_12_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_12_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_13_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_13_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_14_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_14_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_15_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_15_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_16_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_16_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_17_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_17_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_18_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_18_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_19_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_19_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_20_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_20_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_21_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_21_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_22_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_22_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_23_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_23_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_24_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_24_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_25_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_25_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_26_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_26_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_27_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_27_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_28_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_28_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_29_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_29_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_30_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_30_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_31_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_31_CONTROL_POINT_PATCHLIST
    )
    D3D11_PRIMITIVE_TOPOLOGY_32_CONTROL_POINT_PATCHLIST = (
        D3D_PRIMITIVE_TOPOLOGY_32_CONTROL_POINT_PATCHLIST
    )


class D3D_PRIMITIVE(ENUM):
    D3D_PRIMITIVE_UNDEFINED = 0
    D3D_PRIMITIVE_POINT = 1
    D3D_PRIMITIVE_LINE = 2
    D3D_PRIMITIVE_TRIANGLE = 3
    D3D_PRIMITIVE_LINE_ADJ = 6
    D3D_PRIMITIVE_TRIANGLE_ADJ = 7
    D3D_PRIMITIVE_1_CONTROL_POINT_PATCH = 8
    D3D_PRIMITIVE_2_CONTROL_POINT_PATCH = 9
    D3D_PRIMITIVE_3_CONTROL_POINT_PATCH = 10
    D3D_PRIMITIVE_4_CONTROL_POINT_PATCH = 11
    D3D_PRIMITIVE_5_CONTROL_POINT_PATCH = 12
    D3D_PRIMITIVE_6_CONTROL_POINT_PATCH = 13
    D3D_PRIMITIVE_7_CONTROL_POINT_PATCH = 14
    D3D_PRIMITIVE_8_CONTROL_POINT_PATCH = 15
    D3D_PRIMITIVE_9_CONTROL_POINT_PATCH = 16
    D3D_PRIMITIVE_10_CONTROL_POINT_PATCH = 17
    D3D_PRIMITIVE_11_CONTROL_POINT_PATCH = 18
    D3D_PRIMITIVE_12_CONTROL_POINT_PATCH = 19
    D3D_PRIMITIVE_13_CONTROL_POINT_PATCH = 20
    D3D_PRIMITIVE_14_CONTROL_POINT_PATCH = 21
    D3D_PRIMITIVE_15_CONTROL_POINT_PATCH = 22
    D3D_PRIMITIVE_16_CONTROL_POINT_PATCH = 23
    D3D_PRIMITIVE_17_CONTROL_POINT_PATCH = 24
    D3D_PRIMITIVE_18_CONTROL_POINT_PATCH = 25
    D3D_PRIMITIVE_19_CONTROL_POINT_PATCH = 26
    D3D_PRIMITIVE_20_CONTROL_POINT_PATCH = 27
    D3D_PRIMITIVE_21_CONTROL_POINT_PATCH = 28
    D3D_PRIMITIVE_22_CONTROL_POINT_PATCH = 29
    D3D_PRIMITIVE_23_CONTROL_POINT_PATCH = 30
    D3D_PRIMITIVE_24_CONTROL_POINT_PATCH = 31
    D3D_PRIMITIVE_25_CONTROL_POINT_PATCH = 32
    D3D_PRIMITIVE_26_CONTROL_POINT_PATCH = 33
    D3D_PRIMITIVE_27_CONTROL_POINT_PATCH = 34
    D3D_PRIMITIVE_28_CONTROL_POINT_PATCH = 35
    D3D_PRIMITIVE_29_CONTROL_POINT_PATCH = 36
    D3D_PRIMITIVE_30_CONTROL_POINT_PATCH = 37
    D3D_PRIMITIVE_31_CONTROL_POINT_PATCH = 38
    D3D_PRIMITIVE_32_CONTROL_POINT_PATCH = 39
    D3D10_PRIMITIVE_UNDEFINED = D3D_PRIMITIVE_UNDEFINED
    D3D10_PRIMITIVE_POINT = D3D_PRIMITIVE_POINT
    D3D10_PRIMITIVE_LINE = D3D_PRIMITIVE_LINE
    D3D10_PRIMITIVE_TRIANGLE = D3D_PRIMITIVE_TRIANGLE
    D3D10_PRIMITIVE_LINE_ADJ = D3D_PRIMITIVE_LINE_ADJ
    D3D10_PRIMITIVE_TRIANGLE_ADJ = D3D_PRIMITIVE_TRIANGLE_ADJ
    D3D11_PRIMITIVE_UNDEFINED = D3D_PRIMITIVE_UNDEFINED
    D3D11_PRIMITIVE_POINT = D3D_PRIMITIVE_POINT
    D3D11_PRIMITIVE_LINE = D3D_PRIMITIVE_LINE
    D3D11_PRIMITIVE_TRIANGLE = D3D_PRIMITIVE_TRIANGLE
    D3D11_PRIMITIVE_LINE_ADJ = D3D_PRIMITIVE_LINE_ADJ
    D3D11_PRIMITIVE_TRIANGLE_ADJ = D3D_PRIMITIVE_TRIANGLE_ADJ
    D3D11_PRIMITIVE_1_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_1_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_2_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_2_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_3_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_3_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_4_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_4_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_5_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_5_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_6_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_6_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_7_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_7_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_8_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_8_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_9_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_9_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_10_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_10_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_11_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_11_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_12_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_12_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_13_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_13_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_14_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_14_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_15_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_15_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_16_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_16_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_17_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_17_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_18_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_18_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_19_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_19_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_20_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_20_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_21_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_21_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_22_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_22_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_23_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_23_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_24_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_24_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_25_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_25_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_26_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_26_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_27_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_27_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_28_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_28_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_29_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_29_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_30_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_30_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_31_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_31_CONTROL_POINT_PATCH
    )
    D3D11_PRIMITIVE_32_CONTROL_POINT_PATCH = (
        D3D_PRIMITIVE_32_CONTROL_POINT_PATCH
    )


class D3D_SRV_DIMENSION(ENUM):
    D3D_SRV_DIMENSION_UNKNOWN = 0
    D3D_SRV_DIMENSION_BUFFER = 1
    D3D_SRV_DIMENSION_TEXTURE1D = 2
    D3D_SRV_DIMENSION_TEXTURE1DARRAY = 3
    D3D_SRV_DIMENSION_TEXTURE2D = 4
    D3D_SRV_DIMENSION_TEXTURE2DARRAY = 5
    D3D_SRV_DIMENSION_TEXTURE2DMS = 6
    D3D_SRV_DIMENSION_TEXTURE2DMSARRAY = 7
    D3D_SRV_DIMENSION_TEXTURE3D = 8
    D3D_SRV_DIMENSION_TEXTURECUBE = 9
    D3D_SRV_DIMENSION_TEXTURECUBEARRAY = 10
    D3D_SRV_DIMENSION_BUFFEREX = 11
    D3D10_SRV_DIMENSION_UNKNOWN = D3D_SRV_DIMENSION_UNKNOWN
    D3D10_SRV_DIMENSION_BUFFER = D3D_SRV_DIMENSION_BUFFER
    D3D10_SRV_DIMENSION_TEXTURE1D = D3D_SRV_DIMENSION_TEXTURE1D
    D3D10_SRV_DIMENSION_TEXTURE1DARRAY = D3D_SRV_DIMENSION_TEXTURE1DARRAY
    D3D10_SRV_DIMENSION_TEXTURE2D = D3D_SRV_DIMENSION_TEXTURE2D
    D3D10_SRV_DIMENSION_TEXTURE2DARRAY = D3D_SRV_DIMENSION_TEXTURE2DARRAY
    D3D10_SRV_DIMENSION_TEXTURE2DMS = D3D_SRV_DIMENSION_TEXTURE2DMS
    D3D10_SRV_DIMENSION_TEXTURE2DMSARRAY = (
        D3D_SRV_DIMENSION_TEXTURE2DMSARRAY
    )
    D3D10_SRV_DIMENSION_TEXTURE3D = D3D_SRV_DIMENSION_TEXTURE3D
    D3D10_SRV_DIMENSION_TEXTURECUBE = D3D_SRV_DIMENSION_TEXTURECUBE
    D3D10_1_SRV_DIMENSION_UNKNOWN = D3D_SRV_DIMENSION_UNKNOWN
    D3D10_1_SRV_DIMENSION_BUFFER = D3D_SRV_DIMENSION_BUFFER
    D3D10_1_SRV_DIMENSION_TEXTURE1D = D3D_SRV_DIMENSION_TEXTURE1D
    D3D10_1_SRV_DIMENSION_TEXTURE1DARRAY = D3D_SRV_DIMENSION_TEXTURE1DARRAY
    D3D10_1_SRV_DIMENSION_TEXTURE2D = D3D_SRV_DIMENSION_TEXTURE2D
    D3D10_1_SRV_DIMENSION_TEXTURE2DARRAY = D3D_SRV_DIMENSION_TEXTURE2DARRAY
    D3D10_1_SRV_DIMENSION_TEXTURE2DMS = D3D_SRV_DIMENSION_TEXTURE2DMS
    D3D10_1_SRV_DIMENSION_TEXTURE2DMSARRAY = (
        D3D_SRV_DIMENSION_TEXTURE2DMSARRAY
    )
    D3D10_1_SRV_DIMENSION_TEXTURE3D = D3D_SRV_DIMENSION_TEXTURE3D
    D3D10_1_SRV_DIMENSION_TEXTURECUBE = D3D_SRV_DIMENSION_TEXTURECUBE
    D3D10_1_SRV_DIMENSION_TEXTURECUBEARRAY = (
        D3D_SRV_DIMENSION_TEXTURECUBEARRAY
    )
    D3D11_SRV_DIMENSION_UNKNOWN = D3D_SRV_DIMENSION_UNKNOWN
    D3D11_SRV_DIMENSION_BUFFER = D3D_SRV_DIMENSION_BUFFER
    D3D11_SRV_DIMENSION_TEXTURE1D = D3D_SRV_DIMENSION_TEXTURE1D
    D3D11_SRV_DIMENSION_TEXTURE1DARRAY = D3D_SRV_DIMENSION_TEXTURE1DARRAY
    D3D11_SRV_DIMENSION_TEXTURE2D = D3D_SRV_DIMENSION_TEXTURE2D
    D3D11_SRV_DIMENSION_TEXTURE2DARRAY = D3D_SRV_DIMENSION_TEXTURE2DARRAY
    D3D11_SRV_DIMENSION_TEXTURE2DMS = D3D_SRV_DIMENSION_TEXTURE2DMS
    D3D11_SRV_DIMENSION_TEXTURE2DMSARRAY = (
        D3D_SRV_DIMENSION_TEXTURE2DMSARRAY
    )
    D3D11_SRV_DIMENSION_TEXTURE3D = D3D_SRV_DIMENSION_TEXTURE3D
    D3D11_SRV_DIMENSION_TEXTURECUBE = D3D_SRV_DIMENSION_TEXTURECUBE
    D3D11_SRV_DIMENSION_TEXTURECUBEARRAY = (
        D3D_SRV_DIMENSION_TEXTURECUBEARRAY
    )
    D3D11_SRV_DIMENSION_BUFFEREX = D3D_SRV_DIMENSION_BUFFEREX


_D3D_SHADER_MACRO._fields_ = [
    ('Name', LPCSTR),
    ('Definition', LPCSTR),
]
LPD3D_SHADER_MACRO = POINTER(_D3D_SHADER_MACRO)


ID3D10Blob._methods_ = [
    COMMETHOD(
        [helpstring('Method GetBufferPointer')],
        LPVOID,
        'GetBufferPointer',
    ),
    COMMETHOD(
        [helpstring('Method GetBufferSize')],
        SIZE_T,
        'GetBufferSize',
    ),
]

# END IF  C style interface
# END IF  __ID3D10Blob_INTERFACE_DEFINED__

# interface __MIDL_itf_d3dcommon_0000_0001
# [local]
ID3D10Blob._methods_ = [
    COMMETHOD(
        [],
        LPVOID,
        'GetBufferPointer',
    ),
    COMMETHOD(
        [],
        SIZE_T,
        'GetBufferSize',
    ),
]

ID3DBlob = ID3D10Blob
LPD3DBLOB = POINTER(ID3DBlob)

# VOID ( __stdcall *PFN_DESTRUCTION_CALLBACK )( VOID *pData);
PFN_DESTRUCTION_CALLBACK = ctypes.WINFUNCTYPE( 
    VOID,
    POINTER(VOID),
)


ID3DDestructionNotifier._methods_ = [
    COMMETHOD(
        [helpstring('Method RegisterDestructionCallback')],
        HRESULT,
        'RegisterDestructionCallback',
        (['in'], PFN_DESTRUCTION_CALLBACK, 'callbackFn'),
        (['in'], POINTER(VOID), 'pData'),
        (['out'], POINTER(UINT), 'pCallbackID'),
    ),
    COMMETHOD(
        [helpstring('Method UnregisterDestructionCallback')],
        HRESULT,
        'UnregisterDestructionCallback',
        (['in'], UINT, 'callbackID'),
    ),
]


class _D3D_INCLUDE_TYPE(ENUM):
    D3D_INCLUDE_LOCAL = 0
    D3D_INCLUDE_SYSTEM = D3D_INCLUDE_LOCAL + 1
    D3D10_INCLUDE_LOCAL = D3D_INCLUDE_LOCAL
    D3D10_INCLUDE_SYSTEM = D3D_INCLUDE_SYSTEM
    D3D_INCLUDE_FORCE_DWORD = 0x7FFFFFFF


D3D_INCLUDE_TYPE = _D3D_INCLUDE_TYPE


class ID3DInclude(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


ID3DInclude._methods_ = [
    comtypes.STDMETHOD(
        VOID,
        'Open',
        (D3D_INCLUDE_TYPE, LPCSTR, LPCVOID, POINTER(LPCVOID), POINTER(UINT))
    ),
    comtypes.STDMETHOD(
        VOID,
        'Close',
        (LPCVOID,)
    ),
]

LPD3DINCLUDE = POINTER(ID3DInclude)


class _D3D_SHADER_VARIABLE_CLASS(ENUM):
    D3D_SVC_SCALAR = 0
    D3D_SVC_VECTOR = D3D_SVC_SCALAR + 1
    D3D_SVC_MATRIX_ROWS = D3D_SVC_VECTOR + 1
    D3D_SVC_MATRIX_COLUMNS = D3D_SVC_MATRIX_ROWS + 1
    D3D_SVC_OBJECT = D3D_SVC_MATRIX_COLUMNS + 1
    D3D_SVC_STRUCT = D3D_SVC_OBJECT + 1
    D3D_SVC_INTERFACE_CLASS = D3D_SVC_STRUCT + 1
    D3D_SVC_INTERFACE_POINTER = D3D_SVC_INTERFACE_CLASS + 1
    D3D10_SVC_SCALAR = D3D_SVC_SCALAR
    D3D10_SVC_VECTOR = D3D_SVC_VECTOR
    D3D10_SVC_MATRIX_ROWS = D3D_SVC_MATRIX_ROWS
    D3D10_SVC_MATRIX_COLUMNS = D3D_SVC_MATRIX_COLUMNS
    D3D10_SVC_OBJECT = D3D_SVC_OBJECT
    D3D10_SVC_STRUCT = D3D_SVC_STRUCT
    D3D11_SVC_INTERFACE_CLASS = D3D_SVC_INTERFACE_CLASS
    D3D11_SVC_INTERFACE_POINTER = D3D_SVC_INTERFACE_POINTER
    D3D_SVC_FORCE_DWORD = 0x7FFFFFFF


D3D_SHADER_VARIABLE_CLASS = _D3D_SHADER_VARIABLE_CLASS


class _D3D_SHADER_VARIABLE_FLAGS(ENUM):
    D3D_SVF_USERPACKED = 1
    D3D_SVF_USED = 2
    D3D_SVF_INTERFACE_POINTER = 4
    D3D_SVF_INTERFACE_PARAMETER = 8
    D3D10_SVF_USERPACKED = D3D_SVF_USERPACKED
    D3D10_SVF_USED = D3D_SVF_USED
    D3D11_SVF_INTERFACE_POINTER = D3D_SVF_INTERFACE_POINTER
    D3D11_SVF_INTERFACE_PARAMETER = D3D_SVF_INTERFACE_PARAMETER
    D3D_SVF_FORCE_DWORD = 0x7FFFFFFF


D3D_SHADER_VARIABLE_FLAGS = _D3D_SHADER_VARIABLE_FLAGS


class _D3D_SHADER_VARIABLE_TYPE(ENUM):
    D3D_SVT_VOID = 0
    D3D_SVT_BOOL = 1
    D3D_SVT_INT = 2
    D3D_SVT_FLOAT = 3
    D3D_SVT_STRING = 4
    D3D_SVT_TEXTURE = 5
    D3D_SVT_TEXTURE1D = 6
    D3D_SVT_TEXTURE2D = 7
    D3D_SVT_TEXTURE3D = 8
    D3D_SVT_TEXTURECUBE = 9
    D3D_SVT_SAMPLER = 10
    D3D_SVT_SAMPLER1D = 11
    D3D_SVT_SAMPLER2D = 12
    D3D_SVT_SAMPLER3D = 13
    D3D_SVT_SAMPLERCUBE = 14
    D3D_SVT_PIXELSHADER = 15
    D3D_SVT_VERTEXSHADER = 16
    D3D_SVT_PIXELFRAGMENT = 17
    D3D_SVT_VERTEXFRAGMENT = 18
    D3D_SVT_UINT = 19
    D3D_SVT_UINT8 = 20
    D3D_SVT_GEOMETRYSHADER = 21
    D3D_SVT_RASTERIZER = 22
    D3D_SVT_DEPTHSTENCIL = 23
    D3D_SVT_BLEND = 24
    D3D_SVT_BUFFER = 25
    D3D_SVT_CBUFFER = 26
    D3D_SVT_TBUFFER = 27
    D3D_SVT_TEXTURE1DARRAY = 28
    D3D_SVT_TEXTURE2DARRAY = 29
    D3D_SVT_RENDERTARGETVIEW = 30
    D3D_SVT_DEPTHSTENCILVIEW = 31
    D3D_SVT_TEXTURE2DMS = 32
    D3D_SVT_TEXTURE2DMSARRAY = 33
    D3D_SVT_TEXTURECUBEARRAY = 34
    D3D_SVT_HULLSHADER = 35
    D3D_SVT_DOMAINSHADER = 36
    D3D_SVT_INTERFACE_POINTER = 37
    D3D_SVT_COMPUTESHADER = 38
    D3D_SVT_DOUBLE = 39
    D3D_SVT_RWTEXTURE1D = 40
    D3D_SVT_RWTEXTURE1DARRAY = 41
    D3D_SVT_RWTEXTURE2D = 42
    D3D_SVT_RWTEXTURE2DARRAY = 43
    D3D_SVT_RWTEXTURE3D = 44
    D3D_SVT_RWBUFFER = 45
    D3D_SVT_BYTEADDRESS_BUFFER = 46
    D3D_SVT_RWBYTEADDRESS_BUFFER = 47
    D3D_SVT_STRUCTURED_BUFFER = 48
    D3D_SVT_RWSTRUCTURED_BUFFER = 49
    D3D_SVT_APPEND_STRUCTURED_BUFFER = 50
    D3D_SVT_CONSUME_STRUCTURED_BUFFER = 51
    D3D_SVT_MIN8FLOAT = 52
    D3D_SVT_MIN10FLOAT = 53
    D3D_SVT_MIN16FLOAT = 54
    D3D_SVT_MIN12INT = 55
    D3D_SVT_MIN16INT = 56
    D3D_SVT_MIN16UINT = 57
    D3D10_SVT_VOID = D3D_SVT_VOID
    D3D10_SVT_BOOL = D3D_SVT_BOOL
    D3D10_SVT_INT = D3D_SVT_INT
    D3D10_SVT_FLOAT = D3D_SVT_FLOAT
    D3D10_SVT_STRING = D3D_SVT_STRING
    D3D10_SVT_TEXTURE = D3D_SVT_TEXTURE
    D3D10_SVT_TEXTURE1D = D3D_SVT_TEXTURE1D
    D3D10_SVT_TEXTURE2D = D3D_SVT_TEXTURE2D
    D3D10_SVT_TEXTURE3D = D3D_SVT_TEXTURE3D
    D3D10_SVT_TEXTURECUBE = D3D_SVT_TEXTURECUBE
    D3D10_SVT_SAMPLER = D3D_SVT_SAMPLER
    D3D10_SVT_SAMPLER1D = D3D_SVT_SAMPLER1D
    D3D10_SVT_SAMPLER2D = D3D_SVT_SAMPLER2D
    D3D10_SVT_SAMPLER3D = D3D_SVT_SAMPLER3D
    D3D10_SVT_SAMPLERCUBE = D3D_SVT_SAMPLERCUBE
    D3D10_SVT_PIXELSHADER = D3D_SVT_PIXELSHADER
    D3D10_SVT_VERTEXSHADER = D3D_SVT_VERTEXSHADER
    D3D10_SVT_PIXELFRAGMENT = D3D_SVT_PIXELFRAGMENT
    D3D10_SVT_VERTEXFRAGMENT = D3D_SVT_VERTEXFRAGMENT
    D3D10_SVT_UINT = D3D_SVT_UINT
    D3D10_SVT_UINT8 = D3D_SVT_UINT8
    D3D10_SVT_GEOMETRYSHADER = D3D_SVT_GEOMETRYSHADER
    D3D10_SVT_RASTERIZER = D3D_SVT_RASTERIZER
    D3D10_SVT_DEPTHSTENCIL = D3D_SVT_DEPTHSTENCIL
    D3D10_SVT_BLEND = D3D_SVT_BLEND
    D3D10_SVT_BUFFER = D3D_SVT_BUFFER
    D3D10_SVT_CBUFFER = D3D_SVT_CBUFFER
    D3D10_SVT_TBUFFER = D3D_SVT_TBUFFER
    D3D10_SVT_TEXTURE1DARRAY = D3D_SVT_TEXTURE1DARRAY
    D3D10_SVT_TEXTURE2DARRAY = D3D_SVT_TEXTURE2DARRAY
    D3D10_SVT_RENDERTARGETVIEW = D3D_SVT_RENDERTARGETVIEW
    D3D10_SVT_DEPTHSTENCILVIEW = D3D_SVT_DEPTHSTENCILVIEW
    D3D10_SVT_TEXTURE2DMS = D3D_SVT_TEXTURE2DMS
    D3D10_SVT_TEXTURE2DMSARRAY = D3D_SVT_TEXTURE2DMSARRAY
    D3D10_SVT_TEXTURECUBEARRAY = D3D_SVT_TEXTURECUBEARRAY
    D3D11_SVT_HULLSHADER = D3D_SVT_HULLSHADER
    D3D11_SVT_DOMAINSHADER = D3D_SVT_DOMAINSHADER
    D3D11_SVT_INTERFACE_POINTER = D3D_SVT_INTERFACE_POINTER
    D3D11_SVT_COMPUTESHADER = D3D_SVT_COMPUTESHADER
    D3D11_SVT_DOUBLE = D3D_SVT_DOUBLE
    D3D11_SVT_RWTEXTURE1D = D3D_SVT_RWTEXTURE1D
    D3D11_SVT_RWTEXTURE1DARRAY = D3D_SVT_RWTEXTURE1DARRAY
    D3D11_SVT_RWTEXTURE2D = D3D_SVT_RWTEXTURE2D
    D3D11_SVT_RWTEXTURE2DARRAY = D3D_SVT_RWTEXTURE2DARRAY
    D3D11_SVT_RWTEXTURE3D = D3D_SVT_RWTEXTURE3D
    D3D11_SVT_RWBUFFER = D3D_SVT_RWBUFFER
    D3D11_SVT_BYTEADDRESS_BUFFER = D3D_SVT_BYTEADDRESS_BUFFER
    D3D11_SVT_RWBYTEADDRESS_BUFFER = D3D_SVT_RWBYTEADDRESS_BUFFER
    D3D11_SVT_STRUCTURED_BUFFER = D3D_SVT_STRUCTURED_BUFFER
    D3D11_SVT_RWSTRUCTURED_BUFFER = D3D_SVT_RWSTRUCTURED_BUFFER
    D3D11_SVT_APPEND_STRUCTURED_BUFFER = D3D_SVT_APPEND_STRUCTURED_BUFFER
    D3D11_SVT_CONSUME_STRUCTURED_BUFFER = D3D_SVT_CONSUME_STRUCTURED_BUFFER
    D3D_SVT_FORCE_DWORD = 0x7FFFFFFF

D3D_SHADER_VARIABLE_TYPE = _D3D_SHADER_VARIABLE_TYPE


class _D3D_SHADER_INPUT_FLAGS(ENUM):
    D3D_SIF_USERPACKED = 0x1
    D3D_SIF_COMPARISON_SAMPLER = 0x2
    D3D_SIF_TEXTURE_COMPONENT_0 = 0x4
    D3D_SIF_TEXTURE_COMPONENT_1 = 0x8
    D3D_SIF_TEXTURE_COMPONENTS = 0xC
    D3D_SIF_UNUSED = 0x10
    D3D10_SIF_USERPACKED = D3D_SIF_USERPACKED
    D3D10_SIF_COMPARISON_SAMPLER = D3D_SIF_COMPARISON_SAMPLER
    D3D10_SIF_TEXTURE_COMPONENT_0 = D3D_SIF_TEXTURE_COMPONENT_0
    D3D10_SIF_TEXTURE_COMPONENT_1 = D3D_SIF_TEXTURE_COMPONENT_1
    D3D10_SIF_TEXTURE_COMPONENTS = D3D_SIF_TEXTURE_COMPONENTS
    D3D_SIF_FORCE_DWORD = 0x7FFFFFFF


D3D_SHADER_INPUT_FLAGS = _D3D_SHADER_INPUT_FLAGS


class _D3D_SHADER_INPUT_TYPE(ENUM):
    D3D_SIT_CBUFFER = 0
    D3D_SIT_TBUFFER = D3D_SIT_CBUFFER + 1
    D3D_SIT_TEXTURE = D3D_SIT_TBUFFER + 1
    D3D_SIT_SAMPLER = D3D_SIT_TEXTURE + 1
    D3D_SIT_UAV_RWTYPED = D3D_SIT_SAMPLER + 1
    D3D_SIT_STRUCTURED = D3D_SIT_UAV_RWTYPED + 1
    D3D_SIT_UAV_RWSTRUCTURED = D3D_SIT_STRUCTURED + 1
    D3D_SIT_BYTEADDRESS = D3D_SIT_UAV_RWSTRUCTURED + 1
    D3D_SIT_UAV_RWBYTEADDRESS = D3D_SIT_BYTEADDRESS + 1
    D3D_SIT_UAV_APPEND_STRUCTURED = D3D_SIT_UAV_RWBYTEADDRESS + 1
    D3D_SIT_UAV_CONSUME_STRUCTURED = D3D_SIT_UAV_APPEND_STRUCTURED + 1
    D3D_SIT_UAV_RWSTRUCTURED_WITH_COUNTER = (
        D3D_SIT_UAV_CONSUME_STRUCTURED + 1
    )
    D3D10_SIT_CBUFFER = D3D_SIT_CBUFFER
    D3D10_SIT_TBUFFER = D3D_SIT_TBUFFER
    D3D10_SIT_TEXTURE = D3D_SIT_TEXTURE
    D3D10_SIT_SAMPLER = D3D_SIT_SAMPLER
    D3D11_SIT_UAV_RWTYPED = D3D_SIT_UAV_RWTYPED
    D3D11_SIT_STRUCTURED = D3D_SIT_STRUCTURED
    D3D11_SIT_UAV_RWSTRUCTURED = D3D_SIT_UAV_RWSTRUCTURED
    D3D11_SIT_BYTEADDRESS = D3D_SIT_BYTEADDRESS
    D3D11_SIT_UAV_RWBYTEADDRESS = D3D_SIT_UAV_RWBYTEADDRESS
    D3D11_SIT_UAV_APPEND_STRUCTURED = D3D_SIT_UAV_APPEND_STRUCTURED
    D3D11_SIT_UAV_CONSUME_STRUCTURED = D3D_SIT_UAV_CONSUME_STRUCTURED
    D3D11_SIT_UAV_RWSTRUCTURED_WITH_COUNTER = (
        D3D_SIT_UAV_RWSTRUCTURED_WITH_COUNTER
    )


D3D_SHADER_INPUT_TYPE = _D3D_SHADER_INPUT_TYPE


class _D3D_SHADER_CBUFFER_FLAGS(ENUM):
    D3D_CBF_USERPACKED = 1
    D3D10_CBF_USERPACKED = D3D_CBF_USERPACKED
    D3D_CBF_FORCE_DWORD = 0x7FFFFFFF


D3D_SHADER_CBUFFER_FLAGS = _D3D_SHADER_CBUFFER_FLAGS


class _D3D_CBUFFER_TYPE(ENUM):
    D3D_CT_CBUFFER = 0
    D3D_CT_TBUFFER = D3D_CT_CBUFFER + 1
    D3D_CT_INTERFACE_POINTERS = D3D_CT_TBUFFER + 1
    D3D_CT_RESOURCE_BIND_INFO = D3D_CT_INTERFACE_POINTERS + 1
    D3D10_CT_CBUFFER = D3D_CT_CBUFFER
    D3D10_CT_TBUFFER = D3D_CT_TBUFFER
    D3D11_CT_CBUFFER = D3D_CT_CBUFFER
    D3D11_CT_TBUFFER = D3D_CT_TBUFFER
    D3D11_CT_INTERFACE_POINTERS = D3D_CT_INTERFACE_POINTERS
    D3D11_CT_RESOURCE_BIND_INFO = D3D_CT_RESOURCE_BIND_INFO


D3D_CBUFFER_TYPE = _D3D_CBUFFER_TYPE


class D3D_NAME(ENUM):
    D3D_NAME_UNDEFINED = 0
    D3D_NAME_POSITION = 1
    D3D_NAME_CLIP_DISTANCE = 2
    D3D_NAME_CULL_DISTANCE = 3
    D3D_NAME_RENDER_TARGET_ARRAY_INDEX = 4
    D3D_NAME_VIEWPORT_ARRAY_INDEX = 5
    D3D_NAME_VERTEX_ID = 6
    D3D_NAME_PRIMITIVE_ID = 7
    D3D_NAME_INSTANCE_ID = 8
    D3D_NAME_IS_FRONT_FACE = 9
    D3D_NAME_SAMPLE_INDEX = 10
    D3D_NAME_FINAL_QUAD_EDGE_TESSFACTOR = 11
    D3D_NAME_FINAL_QUAD_INSIDE_TESSFACTOR = 12
    D3D_NAME_FINAL_TRI_EDGE_TESSFACTOR = 13
    D3D_NAME_FINAL_TRI_INSIDE_TESSFACTOR = 14
    D3D_NAME_FINAL_LINE_DETAIL_TESSFACTOR = 15
    D3D_NAME_FINAL_LINE_DENSITY_TESSFACTOR = 16
    D3D_NAME_BARYCENTRICS = 23
    D3D_NAME_TARGET = 64
    D3D_NAME_DEPTH = 65
    D3D_NAME_COVERAGE = 66
    D3D_NAME_DEPTH_GREATER_EQUAL = 67
    D3D_NAME_DEPTH_LESS_EQUAL = 68
    D3D_NAME_STENCIL_REF = 69
    D3D_NAME_INNER_COVERAGE = 70
    D3D10_NAME_UNDEFINED = D3D_NAME_UNDEFINED
    D3D10_NAME_POSITION = D3D_NAME_POSITION
    D3D10_NAME_CLIP_DISTANCE = D3D_NAME_CLIP_DISTANCE
    D3D10_NAME_CULL_DISTANCE = D3D_NAME_CULL_DISTANCE
    D3D10_NAME_RENDER_TARGET_ARRAY_INDEX = (
        D3D_NAME_RENDER_TARGET_ARRAY_INDEX
    )
    D3D10_NAME_VIEWPORT_ARRAY_INDEX = D3D_NAME_VIEWPORT_ARRAY_INDEX
    D3D10_NAME_VERTEX_ID = D3D_NAME_VERTEX_ID
    D3D10_NAME_PRIMITIVE_ID = D3D_NAME_PRIMITIVE_ID
    D3D10_NAME_INSTANCE_ID = D3D_NAME_INSTANCE_ID
    D3D10_NAME_IS_FRONT_FACE = D3D_NAME_IS_FRONT_FACE
    D3D10_NAME_SAMPLE_INDEX = D3D_NAME_SAMPLE_INDEX
    D3D10_NAME_TARGET = D3D_NAME_TARGET
    D3D10_NAME_DEPTH = D3D_NAME_DEPTH
    D3D10_NAME_COVERAGE = D3D_NAME_COVERAGE
    D3D11_NAME_FINAL_QUAD_EDGE_TESSFACTOR = (
        D3D_NAME_FINAL_QUAD_EDGE_TESSFACTOR
    )
    D3D11_NAME_FINAL_QUAD_INSIDE_TESSFACTOR = (
        D3D_NAME_FINAL_QUAD_INSIDE_TESSFACTOR
    )
    D3D11_NAME_FINAL_TRI_EDGE_TESSFACTOR = (
        D3D_NAME_FINAL_TRI_EDGE_TESSFACTOR
    )
    D3D11_NAME_FINAL_TRI_INSIDE_TESSFACTOR = (
        D3D_NAME_FINAL_TRI_INSIDE_TESSFACTOR
    )
    D3D11_NAME_FINAL_LINE_DETAIL_TESSFACTOR = (
        D3D_NAME_FINAL_LINE_DETAIL_TESSFACTOR
    )
    D3D11_NAME_FINAL_LINE_DENSITY_TESSFACTOR = (
        D3D_NAME_FINAL_LINE_DENSITY_TESSFACTOR
    )
    D3D11_NAME_DEPTH_GREATER_EQUAL = D3D_NAME_DEPTH_GREATER_EQUAL
    D3D11_NAME_DEPTH_LESS_EQUAL = D3D_NAME_DEPTH_LESS_EQUAL
    D3D11_NAME_STENCIL_REF = D3D_NAME_STENCIL_REF
    D3D11_NAME_INNER_COVERAGE = D3D_NAME_INNER_COVERAGE
    D3D12_NAME_BARYCENTRICS = D3D_NAME_BARYCENTRICS


class D3D_RESOURCE_RETURN_TYPE(ENUM):
    D3D_RETURN_TYPE_UNORM = 1
    D3D_RETURN_TYPE_SNORM = 2
    D3D_RETURN_TYPE_SINT = 3
    D3D_RETURN_TYPE_UINT = 4
    D3D_RETURN_TYPE_FLOAT = 5
    D3D_RETURN_TYPE_MIXED = 6
    D3D_RETURN_TYPE_DOUBLE = 7
    D3D_RETURN_TYPE_CONTINUED = 8
    D3D10_RETURN_TYPE_UNORM = D3D_RETURN_TYPE_UNORM
    D3D10_RETURN_TYPE_SNORM = D3D_RETURN_TYPE_SNORM
    D3D10_RETURN_TYPE_SINT = D3D_RETURN_TYPE_SINT
    D3D10_RETURN_TYPE_UINT = D3D_RETURN_TYPE_UINT
    D3D10_RETURN_TYPE_FLOAT = D3D_RETURN_TYPE_FLOAT
    D3D10_RETURN_TYPE_MIXED = D3D_RETURN_TYPE_MIXED
    D3D11_RETURN_TYPE_UNORM = D3D_RETURN_TYPE_UNORM
    D3D11_RETURN_TYPE_SNORM = D3D_RETURN_TYPE_SNORM
    D3D11_RETURN_TYPE_SINT = D3D_RETURN_TYPE_SINT
    D3D11_RETURN_TYPE_UINT = D3D_RETURN_TYPE_UINT
    D3D11_RETURN_TYPE_FLOAT = D3D_RETURN_TYPE_FLOAT
    D3D11_RETURN_TYPE_MIXED = D3D_RETURN_TYPE_MIXED
    D3D11_RETURN_TYPE_DOUBLE = D3D_RETURN_TYPE_DOUBLE
    D3D11_RETURN_TYPE_CONTINUED = D3D_RETURN_TYPE_CONTINUED


class D3D_REGISTER_COMPONENT_TYPE(ENUM):
    D3D_REGISTER_COMPONENT_UNKNOWN = 0
    D3D_REGISTER_COMPONENT_UINT32 = 1
    D3D_REGISTER_COMPONENT_SINT32 = 2
    D3D_REGISTER_COMPONENT_FLOAT32 = 3
    D3D10_REGISTER_COMPONENT_UNKNOWN = D3D_REGISTER_COMPONENT_UNKNOWN
    D3D10_REGISTER_COMPONENT_UINT32 = D3D_REGISTER_COMPONENT_UINT32
    D3D10_REGISTER_COMPONENT_SINT32 = D3D_REGISTER_COMPONENT_SINT32
    D3D10_REGISTER_COMPONENT_FLOAT32 = D3D_REGISTER_COMPONENT_FLOAT32


class D3D_TESSELLATOR_DOMAIN(ENUM):
    D3D_TESSELLATOR_DOMAIN_UNDEFINED = 0
    D3D_TESSELLATOR_DOMAIN_ISOLINE = 1
    D3D_TESSELLATOR_DOMAIN_TRI = 2
    D3D_TESSELLATOR_DOMAIN_QUAD = 3
    D3D11_TESSELLATOR_DOMAIN_UNDEFINED = D3D_TESSELLATOR_DOMAIN_UNDEFINED
    D3D11_TESSELLATOR_DOMAIN_ISOLINE = D3D_TESSELLATOR_DOMAIN_ISOLINE
    D3D11_TESSELLATOR_DOMAIN_TRI = D3D_TESSELLATOR_DOMAIN_TRI
    D3D11_TESSELLATOR_DOMAIN_QUAD = D3D_TESSELLATOR_DOMAIN_QUAD


class D3D_TESSELLATOR_PARTITIONING(ENUM):
    D3D_TESSELLATOR_PARTITIONING_UNDEFINED = 0
    D3D_TESSELLATOR_PARTITIONING_INTEGER = 1
    D3D_TESSELLATOR_PARTITIONING_POW2 = 2
    D3D_TESSELLATOR_PARTITIONING_FRACTIONAL_ODD = 3
    D3D_TESSELLATOR_PARTITIONING_FRACTIONAL_EVEN = 4
    D3D11_TESSELLATOR_PARTITIONING_UNDEFINED = (
        D3D_TESSELLATOR_PARTITIONING_UNDEFINED
    )
    D3D11_TESSELLATOR_PARTITIONING_INTEGER = (
        D3D_TESSELLATOR_PARTITIONING_INTEGER
    )
    D3D11_TESSELLATOR_PARTITIONING_POW2 = D3D_TESSELLATOR_PARTITIONING_POW2
    D3D11_TESSELLATOR_PARTITIONING_FRACTIONAL_ODD = (
        D3D_TESSELLATOR_PARTITIONING_FRACTIONAL_ODD
    )
    D3D11_TESSELLATOR_PARTITIONING_FRACTIONAL_EVEN = (
        D3D_TESSELLATOR_PARTITIONING_FRACTIONAL_EVEN
    )


class D3D_TESSELLATOR_OUTPUT_PRIMITIVE(ENUM):
    D3D_TESSELLATOR_OUTPUT_UNDEFINED = 0
    D3D_TESSELLATOR_OUTPUT_POINT = 1
    D3D_TESSELLATOR_OUTPUT_LINE = 2
    D3D_TESSELLATOR_OUTPUT_TRIANGLE_CW = 3
    D3D_TESSELLATOR_OUTPUT_TRIANGLE_CCW = 4
    D3D11_TESSELLATOR_OUTPUT_UNDEFINED = D3D_TESSELLATOR_OUTPUT_UNDEFINED
    D3D11_TESSELLATOR_OUTPUT_POINT = D3D_TESSELLATOR_OUTPUT_POINT
    D3D11_TESSELLATOR_OUTPUT_LINE = D3D_TESSELLATOR_OUTPUT_LINE
    D3D11_TESSELLATOR_OUTPUT_TRIANGLE_CW = (
        D3D_TESSELLATOR_OUTPUT_TRIANGLE_CW
    )
    D3D11_TESSELLATOR_OUTPUT_TRIANGLE_CCW = (
        D3D_TESSELLATOR_OUTPUT_TRIANGLE_CCW
    )


class D3D_MIN_PRECISION(ENUM):
    D3D_MIN_PRECISION_DEFAULT = 0
    D3D_MIN_PRECISION_FLOAT_16 = 1
    D3D_MIN_PRECISION_FLOAT_2_8 = 2
    D3D_MIN_PRECISION_RESERVED = 3
    D3D_MIN_PRECISION_SINT_16 = 4
    D3D_MIN_PRECISION_UINT_16 = 5
    D3D_MIN_PRECISION_ANY_16 = 0xF0
    D3D_MIN_PRECISION_ANY_10 = 0xF1


class D3D_INTERPOLATION_MODE(ENUM):
    D3D_INTERPOLATION_UNDEFINED = 0
    D3D_INTERPOLATION_CONSTANT = 1
    D3D_INTERPOLATION_LINEAR = 2
    D3D_INTERPOLATION_LINEAR_CENTROID = 3
    D3D_INTERPOLATION_LINEAR_NOPERSPECTIVE = 4
    D3D_INTERPOLATION_LINEAR_NOPERSPECTIVE_CENTROID = 5
    D3D_INTERPOLATION_LINEAR_SAMPLE = 6
    D3D_INTERPOLATION_LINEAR_NOPERSPECTIVE_SAMPLE = 7


class _D3D_PARAMETER_FLAGS(ENUM):
    D3D_PF_NONE = 0
    D3D_PF_IN = 0x1
    D3D_PF_OUT = 0x2
    D3D_PF_FORCE_DWORD = 0x7FFFFFFF


D3D_PARAMETER_FLAGS = _D3D_PARAMETER_FLAGS

WKPDID_D3DDebugObjectName = GUID(
    '{429B8C22-9188-4B0C-8742-ACB0BF85C200}'
)
WKPDID_D3DDebugObjectNameW = GUID(
    '{4CCA5FD8-921F-42C8-8566-70CAF2A9B741}'
)
WKPDID_CommentStringW = GUID(
    '{D0149DC0-90E8-4EC8-8144-E900AD266BB2}'
)

