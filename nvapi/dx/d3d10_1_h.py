from .d3d10_1shader_h import *  # NOQA

import ctypes
import comtypes
from comtypes.GUID import GUID
from ctypes.wintypes import (
    INT,
    BOOL,
    UINT,
    HMODULE
)


VOID = ctypes.c_void_p
UINT8 = ctypes.c_uint8

HRESULT = ctypes.c_long
POINTER = ctypes.POINTER

COMMETHOD = comtypes.COMMETHOD
helpstring = comtypes.helpstring


class ENUM(INT):
    pass

from .d3d10_h import *
from dxgi_h import *

IID_ID3D10Device1 = GUID(
    "{9B7E4C8F-342C-4106-A19F-4F2704F689F0}"
)


class ID3D10Device1(ID3D10Device):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_ID3D10Device1


class D3D10_RENDER_TARGET_BLEND_DESC1(ctypes.Structure):
    pass


class D3D10_BLEND_DESC1(ctypes.Structure):
    pass


class D3D10_TEXCUBE_ARRAY_SRV1(ctypes.Structure):
    pass


class D3D10_SHADER_RESOURCE_VIEW_DESC1(ctypes.Structure):
    pass


IID_ID3D10BlendState1 = GUID(
    "{EDAD8D99-8A35-4D6D-8566-2EA276CDE161}"
)


class ID3D10BlendState1(ID3D10BlendState):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10BlendState1
    _idlflags_ = []


IID_ID3D10ShaderResourceView1 = GUID(
    "{9B7E4C87-342C-4106-A19F-4F2704F689F0}"
)


class ID3D10ShaderResourceView1(ID3D10ShaderResourceView):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10ShaderResourceView1
    _idlflags_ = []


class D3D10_FEATURE_LEVEL1(ENUM):
    D3D10_FEATURE_LEVEL_10_0 = 0xA000
    D3D10_FEATURE_LEVEL_10_1 = 0xA100
    D3D10_FEATURE_LEVEL_9_1 = 0x9100
    D3D10_FEATURE_LEVEL_9_2 = 0x9200
    D3D10_FEATURE_LEVEL_9_3 = 0x9300


D3D10_RENDER_TARGET_BLEND_DESC1._fields_ = [
    ('BlendEnable', BOOL),
    ('SrcBlend', D3D10_BLEND),
    ('DestBlend', D3D10_BLEND),
    ('BlendOp', D3D10_BLEND_OP),
    ('SrcBlendAlpha', D3D10_BLEND),
    ('DestBlendAlpha', D3D10_BLEND),
    ('BlendOpAlpha', D3D10_BLEND_OP),
    ('RenderTargetWriteMask', UINT8),
]

D3D10_BLEND_DESC1._fields_ = [
    ('AlphaToCoverageEnable', BOOL),
    ('IndependentBlendEnable', BOOL),
    ('RenderTarget', D3D10_RENDER_TARGET_BLEND_DESC1 * 8),
]


ID3D10BlendState1._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc1')],
        VOID,
        'GetDesc1',
        (['out'], POINTER(D3D10_BLEND_DESC1), 'pDesc'),
    ),
]


D3D10_TEXCUBE_ARRAY_SRV1._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
    ('First2DArrayFace', UINT),
    ('NumCubes', UINT),
]
D3D10_SRV_DIMENSION1 = D3D_SRV_DIMENSION


class _Union_1(ctypes.Union):
    pass


_Union_1._fields_ = [
    ('Buffer', D3D10_BUFFER_SRV),
    ('Texture1D', D3D10_TEX1D_SRV),
    ('Texture1DArray', D3D10_TEX1D_ARRAY_SRV),
    ('Texture2D', D3D10_TEX2D_SRV),
    ('Texture2DArray', D3D10_TEX2D_ARRAY_SRV),
    ('Texture2DMS', D3D10_TEX2DMS_SRV),
    ('Texture2DMSArray', D3D10_TEX2DMS_ARRAY_SRV),
    ('Texture3D', D3D10_TEX3D_SRV),
    ('TextureCube', D3D10_TEXCUBE_SRV),
    ('TextureCubeArray', D3D10_TEXCUBE_ARRAY_SRV1),
]
D3D10_SHADER_RESOURCE_VIEW_DESC1._Union_1 = _Union_1

D3D10_SHADER_RESOURCE_VIEW_DESC1._anonymous_ = (
    '_Union_1',
)

D3D10_SHADER_RESOURCE_VIEW_DESC1._fields_ = [
    ('Format', DXGI_FORMAT),
    ('ViewDimension', D3D10_SRV_DIMENSION1),
    ('_Union_1', D3D10_SHADER_RESOURCE_VIEW_DESC1._Union_1),
]


ID3D10ShaderResourceView1._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc1')],
        VOID,
        'GetDesc1',
        (
            ['out'],
            POINTER(D3D10_SHADER_RESOURCE_VIEW_DESC1),
            'pDesc'
        ),
    ),
]


class D3D10_STANDARD_MULTISAMPLE_QUALITY_LEVELS(ENUM):
    D3D10_STANDARD_MULTISAMPLE_PATTERN = 0xFFFFFFFF
    D3D10_CENTER_MULTISAMPLE_PATTERN = 0xFFFFFFFE

       
ID3D10Device1._methods_ = [
    COMMETHOD(
        [helpstring('Method CreateShaderResourceView1')],
        HRESULT,
        'CreateShaderResourceView1',
        (['in'], POINTER(ID3D10Resource), 'pResource'),
        (
            ['in'],
            POINTER(D3D10_SHADER_RESOURCE_VIEW_DESC1),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10ShaderResourceView1)),
            'ppSRView'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateBlendState1')],
        HRESULT,
        'CreateBlendState1',
        (
            ['in'],
            POINTER(D3D10_BLEND_DESC1),
            'pBlendStateDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10BlendState1)),
            'ppBlendState'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetFeatureLevel')],
        D3D10_FEATURE_LEVEL1,
        'GetFeatureLevel',
    ),
]


# ///////////////////////////////////////////////////////////////
# D3D10CreateDevice1
# ------------------
# pAdapter
# If NULL, D3D10CreateDevice1 will choose the primary adapter and
# create a new instance from a temporarily created IDXGIFactory.
# If non-NULL, D3D10CreateDevice1 will register the appropriate
# device, if necessary (via IDXGIAdapter::RegisterDrver), before
# creating the device.
# DriverType
# Specifies the driver type to be created: hardware, reference or
# null.
# Software
# HMODULE of a DLL implementing a software rasterizer. Must be NULL for
# non-Software driver types.
# Flags
# Any of those documented for D3D10CreateDeviceAndSwapChain1.
# HardwareLevel
# Any of those documented for D3D10CreateDeviceAndSwapChain1.
# SDKVersion
# SDK version. Use the D3D10_1_SDK_VERSION macro.
# ppDevice
# Pointer to returned interface.
# Return Values
# Any of those documented for
# CreateDXGIFactory
# IDXGIFactory::EnumAdapters
# IDXGIAdapter::RegisterDriver
# D3D10CreateDevice1
# ///////////////////////////////////////////////////////////////
# HRESULT (WINAPI* PFN_D3D10_CREATE_DEVICE1)(
# IDXGIAdapter *,
# D3D10_DRIVER_TYPE,
# HMODULE,
# UINT,
# D3D10_FEATURE_LEVEL1,
# UINT,
# ID3D10Device1**
# );
PFN_D3D10_CREATE_DEVICE1 = ctypes.WINFUNCTYPE(
    HRESULT,
    POINTER(IDXGIAdapter),
    D3D10_DRIVER_TYPE,
    HMODULE,
    UINT,
    D3D10_FEATURE_LEVEL1,
    UINT,
    POINTER(POINTER(ID3D10Device1)),
)


rdpd3d = ctypes.windll.RDPD3D


# HRESULT WINAPI D3D10CreateDevice1(
# _In_opt_ IDXGIAdapter *pAdapter,
# D3D10_DRIVER_TYPE DriverType,
# HMODULE Software,
# UINT Flags,
# D3D10_FEATURE_LEVEL1 HardwareLevel,
# UINT SDKVersion,
# _Out_opt_ ID3D10Device1 **ppDevice);
D3D10CreateDevice1 = rdpd3d.D3D10CreateDevice1
D3D10CreateDevice1.restype = HRESULT


# ///////////////////////////////////////////////////////////////
# D3D10CreateDeviceAndSwapChain1
# ------------------------------
# ppAdapter
# If NULL, D3D10CreateDevice1 will choose the primary adapter and
# create a new instance from a temporarily created IDXGIFactory.
# If non-NULL, D3D10CreateDevice1 will register the appropriate
# device, if necessary (via IDXGIAdapter::RegisterDrver), before
# creating the device.
# DriverType
# Specifies the driver type to be created: hardware, reference or
# null.
# Software
# HMODULE of a DLL implementing a software rasterizer. Must be NULL for
# non-Software driver types.
# Flags
# Any of those documented for D3D10CreateDevice1.
# HardwareLevel
# Any of:
# D3D10_CREATE_LEVEL_10_0
# D3D10_CREATE_LEVEL_10_1
# SDKVersion
# SDK version. Use the D3D10_1_SDK_VERSION macro.
# pSwapChainDesc
# Swap chain description, may be NULL.
# ppSwapChain
# Pointer to returned interface. May be NULL.
# ppDevice
# Pointer to returned interface.
# Return Values
# Any of those documented for
# CreateDXGIFactory
# IDXGIFactory::EnumAdapters
# IDXGIAdapter::RegisterDriver
# D3D10CreateDevice1
# IDXGIFactory::CreateSwapChain
# ///////////////////////////////////////////////////////////////
# HRESULT (WINAPI* PFN_D3D10_CREATE_DEVICE_AND_SWAP_CHAIN1)(IDXGIAdapter *, D3D10_DRIVER_TYPE, HMODULE, UINT, D3D10_FEATURE_LEVEL1, UINT, DXGI_SWAP_CHAIN_DESC *, IDXGISwapChain **, ID3D10Device1 **);
PFN_D3D10_CREATE_DEVICE_AND_SWAP_CHAIN1 = ctypes.WINFUNCTYPE(
    HRESULT,
    POINTER(IDXGIAdapter),
    D3D10_DRIVER_TYPE,
    HMODULE,
    UINT,
    D3D10_FEATURE_LEVEL1,
    UINT,
    POINTER(DXGI_SWAP_CHAIN_DESC),
    POINTER(POINTER(IDXGISwapChain)),
    POINTER(POINTER(ID3D10Device1)),
)


d3d10_1 = ctypes.windll.D3D10_1


# HRESULT WINAPI D3D10CreateDeviceAndSwapChain1(
# _In_opt_ IDXGIAdapter *pAdapter,
# D3D10_DRIVER_TYPE DriverType,
# HMODULE Software,
# UINT Flags,
# D3D10_FEATURE_LEVEL1 HardwareLevel,
# UINT SDKVersion,
# _In_opt_ DXGI_SWAP_CHAIN_DESC *pSwapChainDesc,
# _Out_opt_ IDXGISwapChain **ppSwapChain,
# _Out_opt_ ID3D10Device1 **ppDevice);
D3D10CreateDeviceAndSwapChain1 = d3d10_1.D3D10CreateDeviceAndSwapChain1
D3D10CreateDeviceAndSwapChain1.restype = HRESULT



