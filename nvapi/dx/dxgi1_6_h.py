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
    SIZE,
    LARGE_INTEGER,
    LONG,
    DWORD,
    WCHAR,
    HDC,
    HWND,
    HMODULE
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


class DXGI_ADAPTER_DESC3(ctypes.Structure):
    pass


class DXGI_OUTPUT_DESC1(ctypes.Structure):
    pass


from .dxgi1_5_h import * # NOQA


class IDXGIAdapter4(IDXGIAdapter3):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = None


class IDXGIOutput6(IDXGIOutput5):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIFactory6(IDXGIFactory5):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []

class DXGI_ADAPTER_FLAG3(ENUM):
    DXGI_ADAPTER_FLAG3_NONE = 0
    DXGI_ADAPTER_FLAG3_REMOTE = 1
    DXGI_ADAPTER_FLAG3_SOFTWARE = 2
    DXGI_ADAPTER_FLAG3_ACG_COMPATIBLE = 4
    DXGI_ADAPTER_FLAG3_SUPPORT_MONITORED_FENCES = 8
    DXGI_ADAPTER_FLAG3_SUPPORT_NON_MONITORED_FENCES = 0x10
    DXGI_ADAPTER_FLAG3_KEYED_MUTEX_CONFORMANCE = 0x20
    DXGI_ADAPTER_FLAG3_FORCE_DWORD = 0xFFFFFFFF


DXGI_ADAPTER_DESC3._fields_ = [
    ('Description', WCHAR * 128),
    ('VendorId', UINT),
    ('DeviceId', UINT),
    ('SubSysId', UINT),
    ('Revision', UINT),
    ('DedicatedVideoMemory', SIZE_T),
    ('DedicatedSystemMemory', SIZE_T),
    ('SharedSystemMemory', SIZE_T),
    ('AdapterLuid', LUID),
    ('Flags', DXGI_ADAPTER_FLAG3),
    ('GraphicsPreemptionGranularity', DXGI_GRAPHICS_PREEMPTION_GRANULARITY),
    ('ComputePreemptionGranularity', DXGI_COMPUTE_PREEMPTION_GRANULARITY),
]

IID_IDXGIAdapter4 = MIDL_INTERFACE(
    "{3C8D99D1-4FBF-4181-A82C-AF66BF7BD24E}"
)
IDXGIAdapter4._iid_ = IID_IDXGIAdapter4

IDXGIAdapter4._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc3')],
        HRESULT,
        'GetDesc3',
        (['out'], POINTER(DXGI_ADAPTER_DESC3), 'pDesc'),
    ),
]

DXGI_OUTPUT_DESC1._fields_ = [
    ('DeviceName', WCHAR * 32),
    ('DesktopCoordinates', RECT),
    ('AttachedToDesktop', BOOL),
    ('Rotation', DXGI_MODE_ROTATION),
    ('Monitor', HMONITOR),
    ('BitsPerColor', UINT),
    ('ColorSpace', DXGI_COLOR_SPACE_TYPE),
    ('RedPrimary', FLOAT * 2),
    ('GreenPrimary', FLOAT * 2),
    ('BluePrimary', FLOAT * 2),
    ('WhitePoint', FLOAT * 2),
    ('MinLuminance', FLOAT),
    ('MaxLuminance', FLOAT),
    ('MaxFullFrameLuminance', FLOAT),
]


class DXGI_HARDWARE_COMPOSITION_SUPPORT_FLAGS(ENUM):
    DXGI_HARDWARE_COMPOSITION_SUPPORT_FLAG_FULLSCREEN = 1
    DXGI_HARDWARE_COMPOSITION_SUPPORT_FLAG_WINDOWED = 2
    DXGI_HARDWARE_COMPOSITION_SUPPORT_FLAG_CURSOR_STRETCHED = 4

IID_IDXGIOutput6 = MIDL_INTERFACE(
    "{068346E8-AAEC-4B84-ADD7-137F513F77A1}"
)
IDXGIOutput6._iid_ = IID_IDXGIOutput6

IDXGIOutput6._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc1')],
        HRESULT,
        'GetDesc1',
        (['out'], POINTER(DXGI_OUTPUT_DESC1), 'pDesc'),
    ),
    COMMETHOD(
        [helpstring('Method CheckHardwareCompositionSupport')],
        HRESULT,
        'CheckHardwareCompositionSupport',
        (['out'], POINTER(UINT), 'pFlags'),
    ),
]


class DXGI_GPU_PREFERENCE(ENUM):
    DXGI_GPU_PREFERENCE_UNSPECIFIED = 0
    DXGI_GPU_PREFERENCE_MINIMUM_POWER = (
        DXGI_GPU_PREFERENCE_UNSPECIFIED + 1
    )
    DXGI_GPU_PREFERENCE_HIGH_PERFORMANCE = (
        DXGI_GPU_PREFERENCE_MINIMUM_POWER + 1
    )


IID_IDXGIFactory6 = MIDL_INTERFACE(
    "{C1B6694F-FF09-44A9-B03C-77900A0A1D17}"
)
IDXGIFactory6._iid_ = IID_IDXGIFactory6

IDXGIFactory6._methods_ = [
    COMMETHOD(
        [helpstring('Method EnumAdapterByGpuPreference')],
        HRESULT,
        'EnumAdapterByGpuPreference',
        (['in'], UINT, 'Adapter'),
        (['in'], DXGI_GPU_PREFERENCE, 'GpuPreference'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvAdapter'),
    ),
]

IID_IDXGIAdapter4 = GUID('{3C8D99D1-4FBF-4181-A82C-AF66BF7BD24E}')

IID_IDXGIOutput6 = GUID('{68346E8-AAEC-4B84-ADD7-137F513F77A1}')

IID_IDXGIFactory6 = GUID('{C1B6694F-FF09-44A9-B03C-77900A0A1D17}')
