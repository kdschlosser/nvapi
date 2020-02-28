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
from ..utils import *


IID_IDXGIDisplayControl = MIDL_INTERFACE(
    "{EA9DBF1A-C88E-4486-854A-98AA0138F30C}"
)


class IDXGIDisplayControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_IDXGIDisplayControl



class DXGI_OUTDUPL_MOVE_RECT(ctypes.Structure):
    pass


class DXGI_OUTDUPL_DESC(ctypes.Structure):
    pass


class DXGI_OUTDUPL_POINTER_POSITION(ctypes.Structure):
    pass


class DXGI_OUTDUPL_POINTER_SHAPE_INFO(ctypes.Structure):
    pass


class DXGI_OUTDUPL_FRAME_INFO(ctypes.Structure):
    pass


class DXGI_MODE_DESC1(ctypes.Structure):
    pass


class DXGI_SWAP_CHAIN_DESC1(ctypes.Structure):
    pass


class DXGI_SWAP_CHAIN_FULLSCREEN_DESC(ctypes.Structure):
    pass


class DXGI_PRESENT_PARAMETERS(ctypes.Structure):
    pass


class DXGI_ADAPTER_DESC2(ctypes.Structure):
    pass

from .dxgi_h import * # NOQA


class IDXGIOutputDuplication(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGISurface2(IDXGISurface):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIResource1(IDXGIResource):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIDevice2(IDXGIDevice):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGISwapChain1(IDXGISwapChain):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIFactory2(IDXGIFactory):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIAdapter2(IDXGIAdapter):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIOutput1(IDXGIOutput):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []



IID_IDXGIDisplayControl = MIDL_INTERFACE(
    "{EA9DBF1A-C88E-4486-854A-98AA0138F30C}"
)
IDXGIDisplayControl._iid_ = IID_IDXGIDisplayControl


IDXGIDisplayControl._methods_ = [
    COMMETHOD(
        [helpstring('Method IsStereoEnabled')],
        BOOL,
        'IsStereoEnabled',
    ),
    COMMETHOD(
        [helpstring('Method SetStereoEnabled')],
        VOID,
        'SetStereoEnabled',
        ([], BOOL, 'enabled'),
    ),
]

DXGI_OUTDUPL_MOVE_RECT._fields_ = [
    ('SourcePoint', POINT),
    ('DestinationRect', RECT),
]

DXGI_OUTDUPL_DESC._fields_ = [
    ('ModeDesc', DXGI_MODE_DESC),
    ('Rotation', DXGI_MODE_ROTATION),
    ('DesktopImageInSystemMemory', BOOL),
]

DXGI_OUTDUPL_POINTER_POSITION._fields_ = [
    ('Position', POINT),
    ('Visible', BOOL),
]


class DXGI_OUTDUPL_POINTER_SHAPE_TYPE(ENUM):
    DXGI_OUTDUPL_POINTER_SHAPE_TYPE_MONOCHROME = 0x1
    DXGI_OUTDUPL_POINTER_SHAPE_TYPE_COLOR = 0x2
    DXGI_OUTDUPL_POINTER_SHAPE_TYPE_MASKED_COLOR = 0x4

DXGI_OUTDUPL_POINTER_SHAPE_INFO._fields_ = [
    ('Type', UINT),
    ('Width', UINT),
    ('Height', UINT),
    ('Pitch', UINT),
    ('HotSpot', POINT),
]

DXGI_OUTDUPL_FRAME_INFO._fields_ = [
    ('LastPresentTime', LARGE_INTEGER),
    ('LastMouseUpdateTime', LARGE_INTEGER),
    ('AccumulatedFrames', UINT),
    ('RectsCoalesced', BOOL),
    ('ProtectedContentMaskedOut', BOOL),
    ('PointerPosition', DXGI_OUTDUPL_POINTER_POSITION),
    ('TotalMetadataBufferSize', UINT),
    ('PointerShapeBufferSize', UINT),
]


IID_IDXGIOutputDuplication = MIDL_INTERFACE(
    "{191CFAC3-A341-470D-B26E-A864F428319C}"
)
IDXGIOutputDuplication._iid_ = IID_IDXGIOutputDuplication


IDXGIOutputDuplication._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(DXGI_OUTDUPL_DESC), 'pDesc'),
    ),
    COMMETHOD(
        [helpstring('Method AcquireNextFrame')],
        HRESULT,
        'AcquireNextFrame',
        (['in'], UINT, 'TimeoutInMilliseconds'),
        (
            ['out'],
            POINTER(DXGI_OUTDUPL_FRAME_INFO),
            'pFrameInfo'
        ),
        (
            ['out'],
            POINTER(POINTER(IDXGIResource)),
            'ppDesktopResource'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetFrameDirtyRects')],
        HRESULT,
        'GetFrameDirtyRects',
        (['in'], UINT, 'DirtyRectsBufferSize'),
        (['out'], POINTER(RECT), 'pDirtyRectsBuffer'),
        (
            ['out'],
            POINTER(UINT),
            'pDirtyRectsBufferSizeRequired'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetFrameMoveRects')],
        HRESULT,
        'GetFrameMoveRects',
        (['in'], UINT, 'MoveRectsBufferSize'),
        (
            ['out'],
            POINTER(DXGI_OUTDUPL_MOVE_RECT),
            'pMoveRectBuffer'
        ),
        (
            ['out'],
            POINTER(UINT),
            'pMoveRectsBufferSizeRequired'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetFramePointerShape')],
        HRESULT,
        'GetFramePointerShape',
        (['in'], UINT, 'PointerShapeBufferSize'),
        (['out', 'in'], POINTER(VOID), 'pPointerShapeBuffer'),
        (
            ['out'],
            POINTER(UINT),
            'pPointerShapeBufferSizeRequired'
        ),
        (
            ['out'],
            POINTER(DXGI_OUTDUPL_POINTER_SHAPE_INFO),
            'pPointerShapeInfo'
        ),
    ),
    COMMETHOD(
        [helpstring('Method MapDesktopSurface')],
        HRESULT,
        'MapDesktopSurface',
        (['out'], POINTER(DXGI_MAPPED_RECT), 'pLockedRect'),
    ),
    COMMETHOD(
        [helpstring('Method UnMapDesktopSurface')],
        HRESULT,
        'UnMapDesktopSurface',
    ),
    COMMETHOD(
        [helpstring('Method ReleaseFrame')],
        HRESULT,
        'ReleaseFrame',
    ),
]

class DXGI_ALPHA_MODE(ENUM):
    DXGI_ALPHA_MODE_UNSPECIFIED = 0
    DXGI_ALPHA_MODE_PREMULTIPLIED = 1
    DXGI_ALPHA_MODE_STRAIGHT = 2
    DXGI_ALPHA_MODE_IGNORE = 3
    DXGI_ALPHA_MODE_FORCE_DWORD = 0xFFFFFFFF


IID_IDXGISurface2 = MIDL_INTERFACE(
    "{ABA496DD-B617-4CB8-A866-BC44D7EB1FA2}"
)
IDXGISurface2._iid_ = IID_IDXGISurface2


IDXGISurface2._methods_ = [
    COMMETHOD(
        [helpstring('Method GetResource')],
        HRESULT,
        'GetResource',
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppParentResource'),
        (['out'], POINTER(UINT), 'pSubresourceIndex'),
    ),
]

IID_IDXGIResource1 = MIDL_INTERFACE(
    "{30961379-4609-4A41-998E-54FE567EE0C1}"
)
IDXGIResource1._iid_ = IID_IDXGIResource1


IDXGIResource1._methods_ = [
    COMMETHOD(
        [helpstring('Method CreateSubresourceSurface')],
        HRESULT,
        'CreateSubresourceSurface',
        ([], UINT, 'index'),
        (
            ['out'],
            POINTER(POINTER(IDXGISurface2)),
            'ppSurface'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateSharedHandle')],
        HRESULT,
        'CreateSharedHandle',
        # SECURITY_ATTRIBUTES
        (['in'], POINTER(VOID), 'pAttributes'),
        (['in'], DWORD, 'dwAccess'),
        (['in'], LPCWSTR, 'lpName'),
        (['out'], POINTER(HANDLE), 'pHandle'),
    ),
]


class _DXGI_OFFER_RESOURCE_PRIORITY(ENUM):
    DXGI_OFFER_RESOURCE_PRIORITY_LOW = 1
    DXGI_OFFER_RESOURCE_PRIORITY_NORMAL = (
        DXGI_OFFER_RESOURCE_PRIORITY_LOW + 1
    )
    DXGI_OFFER_RESOURCE_PRIORITY_HIGH = (
        DXGI_OFFER_RESOURCE_PRIORITY_NORMAL + 1
    )

DXGI_OFFER_RESOURCE_PRIORITY = _DXGI_OFFER_RESOURCE_PRIORITY
       
       
IID_IDXGIDevice2 = MIDL_INTERFACE(
    "{05008617-FBFD-4051-A790-144884B4F6A9}"
)
IDXGIDevice2._iid_ = IID_IDXGIDevice2


IDXGIDevice2._methods_ = [
    COMMETHOD(
        [helpstring('Method OfferResources')],
        HRESULT,
        'OfferResources',
        (['in'], UINT, 'NumResources'),
        (['in'], POINTER(IDXGIResource), 'ppResources'),
        (['in'], DXGI_OFFER_RESOURCE_PRIORITY, 'Priority'),
    ),
    COMMETHOD(
        [helpstring('Method ReclaimResources')],
        HRESULT,
        'ReclaimResources',
        (['in'], UINT, 'NumResources'),
        (['in'], POINTER(IDXGIResource), 'ppResources'),
        (['out'], POINTER(BOOL), 'pDiscarded'),
    ),
    COMMETHOD(
        [helpstring('Method EnqueueSetEvent')],
        HRESULT,
        'EnqueueSetEvent',
        (['in'], HANDLE, 'hEvent'),
    ),
]

DXGI_MODE_DESC1._fields_ = [
    ('Width', UINT),
    ('Height', UINT),
    ('RefreshRate', DXGI_RATIONAL),
    ('Format', DXGI_FORMAT),
    ('ScanlineOrdering', DXGI_MODE_SCANLINE_ORDER),
    ('Scaling', DXGI_MODE_SCALING),
    ('Stereo', BOOL),
]


class DXGI_SCALING(ENUM):
    DXGI_SCALING_STRETCH = 0
    DXGI_SCALING_NONE = 1
    DXGI_SCALING_ASPECT_RATIO_STRETCH = 2

DXGI_SWAP_CHAIN_DESC1._fields_ = [
    ('Width', UINT),
    ('Height', UINT),
    ('Format', DXGI_FORMAT),
    ('Stereo', BOOL),
    ('SampleDesc', DXGI_SAMPLE_DESC),
    ('BufferUsage', DXGI_USAGE),
    ('BufferCount', UINT),
    ('Scaling', DXGI_SCALING),
    ('SwapEffect', DXGI_SWAP_EFFECT),
    ('AlphaMode', DXGI_ALPHA_MODE),
    ('Flags', UINT),
]

DXGI_SWAP_CHAIN_FULLSCREEN_DESC._fields_ = [
    ('RefreshRate', DXGI_RATIONAL),
    ('ScanlineOrdering', DXGI_MODE_SCANLINE_ORDER),
    ('Scaling', DXGI_MODE_SCALING),
    ('Windowed', BOOL),
]

DXGI_PRESENT_PARAMETERS._fields_ = [
    ('DirtyRectsCount', UINT),
    # [annotation]
    ('pDirtyRects', POINTER(RECT)),
    ('pScrollRect', POINTER(RECT)),
    ('pScrollOffset', POINTER(POINT)),
]


IID_IDXGISwapChain1 = MIDL_INTERFACE(
    "{790A45F7-0D42-4876-983A-0A55CFE6F4AA}"
)
IDXGISwapChain1._iid_ = IID_IDXGISwapChain1


IDXGISwapChain1._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc1')],
        HRESULT,
        'GetDesc1',
        (['out'], POINTER(DXGI_SWAP_CHAIN_DESC1), 'pDesc'),
    ),
    COMMETHOD(
        [helpstring('Method GetFullscreenDesc')],
        HRESULT,
        'GetFullscreenDesc',
        (
            ['out'],
            POINTER(DXGI_SWAP_CHAIN_FULLSCREEN_DESC),
            'pDesc'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetHwnd')],
        HRESULT,
        'GetHwnd',
        (['out'], POINTER(HWND), 'pHwnd'),
    ),
    COMMETHOD(
        [helpstring('Method GetCoreWindow')],
        HRESULT,
        'GetCoreWindow',
        (['in'], REFIID, 'refiid'),
        (['out'], POINTER(POINTER(VOID)), 'ppUnk'),
    ),
    COMMETHOD(
        [helpstring('Method Present1')],
        HRESULT,
        'Present1',
        (['in'], UINT, 'SyncInterval'),
        (['in'], UINT, 'PresentFlags'),
        (
            ['in'],
            POINTER(DXGI_PRESENT_PARAMETERS),
            'pPresentParameters'
        ),
    ),
    COMMETHOD(
        [helpstring('Method IsTemporaryMonoSupported')],
        BOOL,
        'IsTemporaryMonoSupported',
    ),
    COMMETHOD(
        [helpstring('Method GetRestrictToOutput')],
        HRESULT,
        'GetRestrictToOutput',
        (
            ['out'],
            POINTER(POINTER(IDXGIOutput)),
            'ppRestrictToOutput'
        ),
    ),
    COMMETHOD(
        [helpstring('Method SetBackgroundColor')],
        HRESULT,
        'SetBackgroundColor',
        (['in'], POINTER(DXGI_RGBA), 'pColor'),
    ),
    COMMETHOD(
        [helpstring('Method GetBackgroundColor')],
        HRESULT,
        'GetBackgroundColor',
        (['out'], POINTER(DXGI_RGBA), 'pColor'),
    ),
    COMMETHOD(
        [helpstring('Method SetRotation')],
        HRESULT,
        'SetRotation',
        (['in'], DXGI_MODE_ROTATION, 'Rotation'),
    ),
    COMMETHOD(
        [helpstring('Method GetRotation')],
        HRESULT,
        'GetRotation',
        (['out'], POINTER(DXGI_MODE_ROTATION), 'pRotation'),
    ),
]

IID_IDXGIFactory2 = MIDL_INTERFACE(
    "{50C83A1C-E072-4C48-87B0-3630FA36A6D0}"
)
IDXGIFactory2._iid_ = IID_IDXGIFactory2


IDXGIFactory2._methods_ = [
    COMMETHOD(
        [helpstring('Method IsWindowedStereoEnabled')],
        BOOL,
        'IsWindowedStereoEnabled',
    ),
    COMMETHOD(
        [helpstring('Method CreateSwapChainForHwnd')],
        HRESULT,
        'CreateSwapChainForHwnd',
        (['in'], POINTER(comtypes.IUnknown), 'pDevice'),
        (['in'], HWND, 'hWnd'),
        (['in'], POINTER(DXGI_SWAP_CHAIN_DESC1), 'pDesc'),
        (
            ['in'],
            POINTER(DXGI_SWAP_CHAIN_FULLSCREEN_DESC),
            'pFullscreenDesc'
        ),
        (['in'], POINTER(IDXGIOutput), 'pRestrictToOutput'),
        (
            ['out'],
            POINTER(POINTER(IDXGISwapChain1)),
            'ppSwapChain'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateSwapChainForCoreWindow')],
        HRESULT,
        'CreateSwapChainForCoreWindow',
        (['in'], POINTER(comtypes.IUnknown), 'pDevice'),
        (['in'], POINTER(comtypes.IUnknown), 'pWindow'),
        (['in'], POINTER(DXGI_SWAP_CHAIN_DESC1), 'pDesc'),
        (['in'], POINTER(IDXGIOutput), 'pRestrictToOutput'),
        (
            ['out'],
            POINTER(POINTER(IDXGISwapChain1)),
            'ppSwapChain'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetSharedResourceAdapterLuid')],
        HRESULT,
        'GetSharedResourceAdapterLuid',
        (['in'], HANDLE, 'hResource'),
        (['out'], POINTER(LUID), 'pLuid'),
    ),
    COMMETHOD(
        [helpstring('Method RegisterStereoStatusWindow')],
        HRESULT,
        'RegisterStereoStatusWindow',
        (['in'], HWND, 'WindowHandle'),
        (['in'], UINT, 'wMsg'),
        (['out'], POINTER(DWORD), 'pdwCookie'),
    ),
    COMMETHOD(
        [helpstring('Method RegisterStereoStatusEvent')],
        HRESULT,
        'RegisterStereoStatusEvent',
        (['in'], HANDLE, 'hEvent'),
        (['out'], POINTER(DWORD), 'pdwCookie'),
    ),
    COMMETHOD(
        [helpstring('Method UnregisterStereoStatus')],
        VOID,
        'UnregisterStereoStatus',
        (['in'], DWORD, 'dwCookie'),
    ),
    COMMETHOD(
        [helpstring('Method RegisterOcclusionStatusWindow')],
        HRESULT,
        'RegisterOcclusionStatusWindow',
        (['in'], HWND, 'WindowHandle'),
        (['in'], UINT, 'wMsg'),
        (['out'], POINTER(DWORD), 'pdwCookie'),
    ),
    COMMETHOD(
        [helpstring('Method RegisterOcclusionStatusEvent')],
        HRESULT,
        'RegisterOcclusionStatusEvent',
        (['in'], HANDLE, 'hEvent'),
        (['out'], POINTER(DWORD), 'pdwCookie'),
    ),
    COMMETHOD(
        [helpstring('Method UnregisterOcclusionStatus')],
        VOID,
        'UnregisterOcclusionStatus',
        (['in'], DWORD, 'dwCookie'),
    ),
    COMMETHOD(
        [helpstring('Method CreateSwapChainForComposition')],
        HRESULT,
        'CreateSwapChainForComposition',
        (['in'], POINTER(comtypes.IUnknown), 'pDevice'),
        (['in'], POINTER(DXGI_SWAP_CHAIN_DESC1), 'pDesc'),
        (['in'], POINTER(IDXGIOutput), 'pRestrictToOutput'),
        (
            ['out'],
            POINTER(POINTER(IDXGISwapChain1)),
            'ppSwapChain'
        ),
    ),
]

class DXGI_GRAPHICS_PREEMPTION_GRANULARITY(ENUM):
    DXGI_GRAPHICS_PREEMPTION_DMA_BUFFER_BOUNDARY = 0
    DXGI_GRAPHICS_PREEMPTION_PRIMITIVE_BOUNDARY = 1
    DXGI_GRAPHICS_PREEMPTION_TRIANGLE_BOUNDARY = 2
    DXGI_GRAPHICS_PREEMPTION_PIXEL_BOUNDARY = 3
    DXGI_GRAPHICS_PREEMPTION_INSTRUCTION_BOUNDARY = 4


class DXGI_COMPUTE_PREEMPTION_GRANULARITY(ENUM):
    DXGI_COMPUTE_PREEMPTION_DMA_BUFFER_BOUNDARY = 0
    DXGI_COMPUTE_PREEMPTION_DISPATCH_BOUNDARY = 1
    DXGI_COMPUTE_PREEMPTION_THREAD_GROUP_BOUNDARY = 2
    DXGI_COMPUTE_PREEMPTION_THREAD_BOUNDARY = 3
    DXGI_COMPUTE_PREEMPTION_INSTRUCTION_BOUNDARY = 4

DXGI_ADAPTER_DESC2._fields_ = [
    ('Description', WCHAR * 128),
    ('VendorId', UINT),
    ('DeviceId', UINT),
    ('SubSysId', UINT),
    ('Revision', UINT),
    ('DedicatedVideoMemory', SIZE_T),
    ('DedicatedSystemMemory', SIZE_T),
    ('SharedSystemMemory', SIZE_T),
    ('AdapterLuid', LUID),
    ('Flags', UINT),
    ('GraphicsPreemptionGranularity', DXGI_GRAPHICS_PREEMPTION_GRANULARITY),
    ('ComputePreemptionGranularity', DXGI_COMPUTE_PREEMPTION_GRANULARITY),
]


IID_IDXGIAdapter2 = MIDL_INTERFACE(
    "{0AA1AE0A-FA0E-4B84-8644-E05FF8E5ACB5}"
)
IDXGIAdapter2._iid_ = IID_IDXGIAdapter2


IDXGIAdapter2._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc2')],
        HRESULT,
        'GetDesc2',
        (['out'], POINTER(DXGI_ADAPTER_DESC2), 'pDesc'),
    ),
]

IID_IDXGIOutput1 = MIDL_INTERFACE(
    "{00CDDEA8-939B-4B83-A340-A685226666CC}"
)
IDXGIOutput1._iid_ = IID_IDXGIOutput1


IDXGIOutput1._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDisplayModeList1')],
        HRESULT,
        'GetDisplayModeList1',
        (['in'], DXGI_FORMAT, 'EnumFormat'),
        (['in'], UINT, 'Flags'),
        (['out', 'in'], POINTER(UINT), 'pNumModes'),
        (['out'], POINTER(DXGI_MODE_DESC1), 'pDesc'),
    ),
    COMMETHOD(
        [helpstring('Method FindClosestMatchingMode1')],
        HRESULT,
        'FindClosestMatchingMode1',
        (['in'], POINTER(DXGI_MODE_DESC1), 'pModeToMatch'),
        (['out'], POINTER(DXGI_MODE_DESC1), 'pClosestMatch'),
        (
            ['in'],
            POINTER(comtypes.IUnknown),
            'pConcernedDevice'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetDisplaySurfaceData1')],
        HRESULT,
        'GetDisplaySurfaceData1',
        (['in'], POINTER(IDXGIResource), 'pDestination'),
    ),
    COMMETHOD(
        [helpstring('Method DuplicateOutput')],
        HRESULT,
        'DuplicateOutput',
        (['in'], POINTER(comtypes.IUnknown), 'pDevice'),
        (
            ['out'],
            POINTER(POINTER(IDXGIOutputDuplication)),
            'ppOutputDuplication'
        ),
    ),
]

IID_IDXGIDisplayControl = GUID('{EA9DBF1A-C88E-4486-854A-98AA0138F30C}')

IID_IDXGIOutputDuplication = GUID('{191CFAC3-A341-470D-B26E-A864F428319C}')

IID_IDXGISurface2 = GUID('{ABA496DD-B617-4CB8-A866-BC44D7EB1FA2}')

IID_IDXGIResource1 = GUID('{30961379-4609-4A41-998E-54FE567EE0C1}')

IID_IDXGIDevice2 = GUID('{5008617-FBFD-4051-A790-144884B4F6A9}')

IID_IDXGISwapChain1 = GUID('{790A45F7-D42-4876-983A-0A55CFE6F4AA}')

IID_IDXGIFactory2 = GUID('{50C83A1C-E072-4C48-87B0-3630FA36A6D0}')

IID_IDXGIAdapter2 = GUID('{AA1AE0A-FA0E-4B84-8644-E05FF8E5ACB5}')

IID_IDXGIOutput1 = GUID('{CDDEA8-939B-4B83-A340-A685226666CC}')


