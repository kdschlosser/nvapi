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


from .dxgi1_2_h import *


IID_IDXGIDevice3 = MIDL_INTERFACE(
    "{6007896C-3244-4AFD-BF18-A6D3BEDA5023}"
)


class IDXGIDevice3(IDXGIDevice2):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_IDXGIDevice3


class DXGI_MATRIX_3X2_F(ctypes.Structure):
    pass


class DXGI_DECODE_SWAP_CHAIN_DESC(ctypes.Structure):
    pass


class DXGI_FRAME_STATISTICS_MEDIA(ctypes.Structure):
    pass


from dxgi1_2_h import * # NOQA


class IDXGISwapChain2(IDXGISwapChain1):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIOutput2(IDXGIOutput1):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIFactory3(IDXGIFactory2):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIDecodeSwapChain(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIFactoryMedia(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGISwapChainMedia(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIOutput3(IDXGIOutput2):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


dxgi = ctypes.windll.DXGI


# extern "C"{
# #endif
# 
# 
# // interface __MIDL_itf_dxgi1_3_0000_0000
# // [local]
# 
# #include  < winapifamily.h >
# #pragma region App Family
# #if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP)
# #define DXGI_CREATE_FACTORY_DEBUG 0x1
# HRESULT WINAPI CreateDXGIFactory2(UINT Flags, REFIID riid, _COM_Outptr_ VOID **ppFactory);
CreateDXGIFactory2 = dxgi.CreateDXGIFactory2
CreateDXGIFactory2.restype = HRESULT
# HRESULT WINAPI DXGIGetDebugInterface1(UINT Flags, REFIID riid, _COM_Outptr_ VOID **pDebug);
DXGIGetDebugInterface1 = dxgi.DXGIGetDebugInterface1
DXGIGetDebugInterface1.restype = HRESULT

IID_IDXGIDevice3 = MIDL_INTERFACE(
    "{6007896C-3244-4AFD-BF18-A6D3BEDA5023}"
)
IDXGIDevice3._iid_ = IID_IDXGIDevice3


IDXGIDevice3._methods_ = [
    COMMETHOD(
        [helpstring('Method Trim')],
        VOID,
        'Trim',
    ),
]


DXGI_MATRIX_3X2_F._fields_ = [
    ('_11', FLOAT),
    ('_12', FLOAT),
    ('_21', FLOAT),
    ('_22', FLOAT),
    ('_31', FLOAT),
    ('_32', FLOAT),
]

IID_IDXGISwapChain2 = MIDL_INTERFACE(
    "{A8BE2AC4-199F-4946-B331-79599FB98DE7}"
)
IDXGISwapChain2._iid_ = IID_IDXGISwapChain2


IDXGISwapChain2._methods_ = [
    COMMETHOD(
        [helpstring('Method SetSourceSize')],
        HRESULT,
        'SetSourceSize',
        ([], UINT, 'Width'),
        ([], UINT, 'Height'),
    ),
    COMMETHOD(
        [helpstring('Method GetSourceSize')],
        HRESULT,
        'GetSourceSize',
        (['out'], POINTER(UINT), 'pWidth'),
        (['out'], POINTER(UINT), 'pHeight'),
    ),
    COMMETHOD(
        [helpstring('Method SetMaximumFrameLatency')],
        HRESULT,
        'SetMaximumFrameLatency',
        ([], UINT, 'MaxLatency'),
    ),
    COMMETHOD(
        [helpstring('Method GetMaximumFrameLatency')],
        HRESULT,
        'GetMaximumFrameLatency',
        (['out'], POINTER(UINT), 'pMaxLatency'),
    ),
    COMMETHOD(
        [helpstring('Method GetFrameLatencyWaitableObject')],
        HANDLE,
        'GetFrameLatencyWaitableObject',
    ),
    COMMETHOD(
        [helpstring('Method SetMatrixTransform')],
        HRESULT,
        'SetMatrixTransform',
        ([], POINTER(DXGI_MATRIX_3X2_F), 'pMatrix'),
    ),
    COMMETHOD(
        [helpstring('Method GetMatrixTransform')],
        HRESULT,
        'GetMatrixTransform',
        (['out'], POINTER(DXGI_MATRIX_3X2_F), 'pMatrix'),
    ),
]

IID_IDXGIOutput2 = MIDL_INTERFACE(
    "{595E39D1-2724-4663-99B1-DA969DE28364}"
)
IDXGIOutput2._iid_ = IID_IDXGIOutput2


IDXGIOutput2._methods_ = [
    COMMETHOD(
        [helpstring('Method SupportsOverlays')],
        BOOL,
        'SupportsOverlays',
    ),
]

IID_IDXGIFactory3 = MIDL_INTERFACE(
    "{25483823-CD46-4C7D-86CA-47AA95B837BD}"
)
IDXGIFactory3._iid_ = IID_IDXGIFactory3


IDXGIFactory3._methods_ = [
    COMMETHOD(
        [helpstring('Method GetCreationFlags')],
        UINT,
        'GetCreationFlags',
    ),
]

DXGI_DECODE_SWAP_CHAIN_DESC._fields_ = [
    ('Flags', UINT),
]


class DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAGS(ENUM):
    DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAG_NOMINAL_RANGE = 0x1
    DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAG_BT709 = 0x2
    DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAG_xvYCC = 0x4

IID_IDXGIDecodeSwapChain = MIDL_INTERFACE(
    "{2633066B-4514-4C7A-8FD8-12EA98059D18}"
)
IDXGIDecodeSwapChain._iid_ = IID_IDXGIDecodeSwapChain


IDXGIDecodeSwapChain._methods_ = [
    COMMETHOD(
        [helpstring('Method PresentBuffer')],
        HRESULT,
        'PresentBuffer',
        ([], UINT, 'BufferToPresent'),
        ([], UINT, 'SyncInterval'),
        ([], UINT, 'Flags'),
    ),
    COMMETHOD(
        [helpstring('Method SetSourceRect')],
        HRESULT,
        'SetSourceRect',
        ([], POINTER(RECT), 'pRect'),
    ),
    COMMETHOD(
        [helpstring('Method SetTargetRect')],
        HRESULT,
        'SetTargetRect',
        ([], POINTER(RECT), 'pRect'),
    ),
    COMMETHOD(
        [helpstring('Method SetDestSize')],
        HRESULT,
        'SetDestSize',
        ([], UINT, 'Width'),
        ([], UINT, 'Height'),
    ),
    COMMETHOD(
        [helpstring('Method GetSourceRect')],
        HRESULT,
        'GetSourceRect',
        (['out'], POINTER(RECT), 'pRect'),
    ),
    COMMETHOD(
        [helpstring('Method GetTargetRect')],
        HRESULT,
        'GetTargetRect',
        (['out'], POINTER(RECT), 'pRect'),
    ),
    COMMETHOD(
        [helpstring('Method GetDestSize')],
        HRESULT,
        'GetDestSize',
        (['out'], POINTER(UINT), 'pWidth'),
        (['out'], POINTER(UINT), 'pHeight'),
    ),
    COMMETHOD(
        [helpstring('Method SetColorSpace')],
        HRESULT,
        'SetColorSpace',
        (
            [],
            DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAGS,
            'ColorSpace'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetColorSpace')],
        DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAGS,
        'GetColorSpace',
    ),
]

IID_IDXGIFactoryMedia = MIDL_INTERFACE(
    "{41E7D1F2-A591-4F7B-A2E5-FA9C843E1C12}"
)
IDXGIFactoryMedia._iid_ = IID_IDXGIFactoryMedia


IDXGIFactoryMedia._methods_ = [
    COMMETHOD(
        [helpstring('Method CreateSwapChainForCompositionSurfaceHandle')],
        HRESULT,
        'CreateSwapChainForCompositionSurfaceHandle',
        (['in'], POINTER(comtypes.IUnknown), 'pDevice'),
        (['in'], HANDLE, 'hSurface'),
        (['in'], POINTER(DXGI_SWAP_CHAIN_DESC1), 'pDesc'),
        (['in'], POINTER(IDXGIOutput), 'pRestrictToOutput'),
        (
            ['out'],
            POINTER(POINTER(IDXGISwapChain1)),
            'ppSwapChain'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateDecodeSwapChainForCompositionSurfaceHandle')],
        HRESULT,
        'CreateDecodeSwapChainForCompositionSurfaceHandle',
        (['in'], POINTER(comtypes.IUnknown), 'pDevice'),
        (['in'], HANDLE, 'hSurface'),
        (
            ['in'],
            POINTER(DXGI_DECODE_SWAP_CHAIN_DESC),
            'pDesc'
        ),
        (['in'], POINTER(IDXGIResource), 'pYuvDecodeBuffers'),
        (['in'], POINTER(IDXGIOutput), 'pRestrictToOutput'),
        (
            ['out'],
            POINTER(POINTER(IDXGIDecodeSwapChain)),
            'ppSwapChain'
        ),
    ),
]

class DXGI_FRAME_PRESENTATION_MODE(ENUM):
    DXGI_FRAME_PRESENTATION_MODE_COMPOSED = 0
    DXGI_FRAME_PRESENTATION_MODE_OVERLAY = 1
    DXGI_FRAME_PRESENTATION_MODE_NONE = 2
    DXGI_FRAME_PRESENTATION_MODE_COMPOSITION_FAILURE = 3

DXGI_FRAME_STATISTICS_MEDIA._fields_ = [
    ('PresentCount', UINT),
    ('PresentRefreshCount', UINT),
    ('SyncRefreshCount', UINT),
    ('SyncQPCTime', LARGE_INTEGER),
    ('SyncGPUTime', LARGE_INTEGER),
    ('CompositionMode', DXGI_FRAME_PRESENTATION_MODE),
    ('ApprovedPresentDuration', UINT),
]


IID_IDXGISwapChainMedia = MIDL_INTERFACE(
    "{DD95B90B-F05F-4F6A-BD65-25BFB264BD84}"
)
IDXGISwapChainMedia._iid_ = IID_IDXGISwapChainMedia


IDXGISwapChainMedia._methods_ = [
    COMMETHOD(
        [helpstring('Method GetFrameStatisticsMedia')],
        HRESULT,
        'GetFrameStatisticsMedia',
        (
            ['out'],
            POINTER(DXGI_FRAME_STATISTICS_MEDIA),
            'pStats'
        ),
    ),
    COMMETHOD(
        [helpstring('Method SetPresentDuration')],
        HRESULT,
        'SetPresentDuration',
        ([], UINT, 'Duration'),
    ),
    COMMETHOD(
        [helpstring('Method CheckPresentDurationSupport')],
        HRESULT,
        'CheckPresentDurationSupport',
        ([], UINT, 'DesiredPresentDuration'),
        (
            ['out'],
            POINTER(UINT),
            'pClosestSmallerPresentDuration'
        ),
        (
            ['out'],
            POINTER(UINT),
            'pClosestLargerPresentDuration'
        ),
    ),
]

class DXGI_OVERLAY_SUPPORT_FLAG(ENUM):
    DXGI_OVERLAY_SUPPORT_FLAG_DIRECT = 0x1
    DXGI_OVERLAY_SUPPORT_FLAG_SCALING = 0x2

IID_IDXGIOutput3 = MIDL_INTERFACE(
    "{8A6BB301-7E7E-41F4-A8E0-5B32F7F99B18}"
)
IDXGIOutput3._iid_ = IID_IDXGIOutput3


IDXGIOutput3._methods_ = [
    COMMETHOD(
        [helpstring('Method CheckOverlaySupport')],
        HRESULT,
        'CheckOverlaySupport',
        (['in'], DXGI_FORMAT, 'EnumFormat'),
        (
            ['in'],
            POINTER(comtypes.IUnknown),
            'pConcernedDevice'
        ),
        (['out'], POINTER(UINT), 'pFlags'),
    ),
]

IID_IDXGIDevice3 = GUID('{6007896C-3244-4AFD-BF18-A6D3BEDA5023}')

IID_IDXGISwapChain2 = GUID('{A8BE2AC4-199F-4946-B331-79599FB98DE7}')

IID_IDXGIOutput2 = GUID('{595E39D1-2724-4663-99B1-DA969DE28364}')

IID_IDXGIFactory3 = GUID('{25483823-CD46-4C7D-86CA-47AA95B837BD}')

IID_IDXGIDecodeSwapChain = GUID('{2633066B-4514-4C7A-8FD8-12EA98059D18}')

IID_IDXGIFactoryMedia = GUID('{41E7D1F2-A591-4F7B-A2E5-FA9C843E1C12}')

IID_IDXGISwapChainMedia = GUID('{DD95B90B-F05F-4F6A-BD65-25BFB264BD84}')

IID_IDXGIOutput3 = GUID('{8A6BB301-7E7E-41F4-A8E0-5B32F7F99B18}')
