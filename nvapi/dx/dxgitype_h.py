import ctypes
import comtypes

from comtypes.GUID import GUID

from ctypes.wintypes import (
    BOOL,
    UINT,
    INT,
    FLOAT,
    BYTE,
    LPCSTR,
    LPSTR,
    HANDLE,
    RECT,
    USHORT,
    SIZE
)

ULONGLONG = ctypes.c_ulonglong
UINT8 = ctypes.c_uint8
UINT16 = ctypes.c_uint16
COMMETHOD = comtypes.COMMETHOD
helpstring = comtypes.helpstring
POINTER = ctypes.POINTER
VOID = ctypes.c_void_p
MIDL_INTERFACE = GUID
REFIID = POINTER(GUID)
SIZE_T = ctypes.c_size_t
REFGUID = POINTER(GUID)
HRESULT = ctypes.c_long
UINT64 = ctypes.c_uint64
D3D10_RECT = RECT
D3D10_IGNORE_SDK_LAYERS = None


class ENUM(INT):
    pass


class DXGI_RGB(ctypes.Structure):
    pass


class _D3DCOLORVALUE(ctypes.Structure):
    pass


D3DCOLORVALUE = _D3DCOLORVALUE


class DXGI_GAMMA_CONTROL(ctypes.Structure):
    pass


class DXGI_GAMMA_CONTROL_CAPABILITIES(ctypes.Structure):
    pass


class DXGI_MODE_DESC(ctypes.Structure):
    pass


class DXGI_JPEG_DC_HUFFMAN_TABLE(ctypes.Structure):
    pass


class DXGI_JPEG_AC_HUFFMAN_TABLE(ctypes.Structure):
    pass


class DXGI_JPEG_QUANTIZATION_TABLE(ctypes.Structure):
    pass


from .dxgicommon_h import *  # NOQA
from .dxgi_format_h import *  # NOQA
_FACDXGI = 0x87A
    

def MAKE_HRESULT(sev, fac, code):
    return (sev << 31) | (fac << 16) | code


def MAKE_DXGI_HRESULT(code):
    return MAKE_HRESULT(1, _FACDXGI, code)
    

def MAKE_DXGI_STATUS(code):
    return MAKE_HRESULT(0, _FACDXGI, code)


# DXGI error messages have moved to winerror.h
DXGI_CPU_ACCESS_NONE = 0
DXGI_CPU_ACCESS_DYNAMIC = 1
DXGI_CPU_ACCESS_READ_WRITE = 2
DXGI_CPU_ACCESS_SCRATCH = 3
DXGI_CPU_ACCESS_FIELD = 15


DXGI_RGB._fields_ = [
    ('Red', FLOAT),
    ('Green', FLOAT),
    ('Blue', FLOAT),
]

_D3DCOLORVALUE._fields_ = [
    ('r', FLOAT),
    ('g', FLOAT),
    ('b', FLOAT),
    ('a', FLOAT),
]


DXGI_RGBA = D3DCOLORVALUE


DXGI_GAMMA_CONTROL._fields_ = [
    ('Scale', DXGI_RGB),
    ('Offset', DXGI_RGB),
    ('GammaCurve', DXGI_RGB * 1025),
]

DXGI_GAMMA_CONTROL_CAPABILITIES._fields_ = [
    ('ScaleAndOffsetSupported', BOOL),
    ('MaxConvertedValue', FLOAT),
    ('MinConvertedValue', FLOAT),
    ('NumGammaControlPoints', UINT),
    ('ControlPointPositions', FLOAT * 1025),
]


class DXGI_MODE_SCANLINE_ORDER(ENUM):
    DXGI_MODE_SCANLINE_ORDER_UNSPECIFIED = 0
    DXGI_MODE_SCANLINE_ORDER_PROGRESSIVE = 1
    DXGI_MODE_SCANLINE_ORDER_UPPER_FIELD_FIRST = 2
    DXGI_MODE_SCANLINE_ORDER_LOWER_FIELD_FIRST = 3


class DXGI_MODE_SCALING(ENUM):
    DXGI_MODE_SCALING_UNSPECIFIED = 0
    DXGI_MODE_SCALING_CENTERED = 1
    DXGI_MODE_SCALING_STRETCHED = 2


class DXGI_MODE_ROTATION(ENUM):
    DXGI_MODE_ROTATION_UNSPECIFIED = 0
    DXGI_MODE_ROTATION_IDENTITY = 1
    DXGI_MODE_ROTATION_ROTATE90 = 2
    DXGI_MODE_ROTATION_ROTATE180 = 3
    DXGI_MODE_ROTATION_ROTATE270 = 4


DXGI_MODE_DESC._fields_ = [
    ('Width', UINT),
    ('Height', UINT),
    ('RefreshRate', DXGI_RATIONAL),
    ('Format', DXGI_FORMAT),
    ('ScanlineOrdering', DXGI_MODE_SCANLINE_ORDER),
    ('Scaling', DXGI_MODE_SCALING),
]

DXGI_JPEG_DC_HUFFMAN_TABLE._fields_ = [
    ('CodeCounts', BYTE * 12),
    ('CodeValues', BYTE * 12),
]

DXGI_JPEG_AC_HUFFMAN_TABLE._fields_ = [
    ('CodeCounts', BYTE * 16),
    ('CodeValues', BYTE * 162),
]

DXGI_JPEG_QUANTIZATION_TABLE._fields_ = [
    ('Elements', BYTE * 64),
]


