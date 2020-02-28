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


class ID3D11Texture2D1(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = None


class D3D11_TEXTURE2D_DESC1(ctypes.Structure):
    pass


class D3D11_TEXTURE3D_DESC1(ctypes.Structure):
    pass


class D3D11_RASTERIZER_DESC2(ctypes.Structure):
    pass


class D3D11_TEX2D_SRV1(ctypes.Structure):
    pass


class D3D11_TEX2D_ARRAY_SRV1(ctypes.Structure):
    pass


class D3D11_SHADER_RESOURCE_VIEW_DESC1(ctypes.Structure):
    pass


class D3D11_TEX2D_RTV1(ctypes.Structure):
    pass


class D3D11_TEX2D_ARRAY_RTV1(ctypes.Structure):
    pass


class D3D11_RENDER_TARGET_VIEW_DESC1(ctypes.Structure):
    pass


class D3D11_TEX2D_UAV1(ctypes.Structure):
    pass


class D3D11_TEX2D_ARRAY_UAV1(ctypes.Structure):
    pass


class D3D11_UNORDERED_ACCESS_VIEW_DESC1(ctypes.Structure):
    pass


class D3D11_QUERY_DESC1(ctypes.Structure):
    pass


from .dxgi1_3_h import * # NOQA
from .d3dcommon_h import * # NOQA
from .d3d11_2_h import * # NOQA


class ID3D11Texture3D1(ID3D11Texture3D):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11RasterizerState2(ID3D11RasterizerState1):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11ShaderResourceView1(ID3D11ShaderResourceView):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11RenderTargetView1(ID3D11RenderTargetView):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11UnorderedAccessView1(ID3D11UnorderedAccessView):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []

   
class ID3D11Query1(ID3D11Query):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11DeviceContext3(ID3D11DeviceContext2):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11Fence(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11DeviceContext4(ID3D11DeviceContext3):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []

   
class ID3D11Device3(ID3D11Device2):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class D3D11_CONTEXT_TYPE(ENUM):
    D3D11_CONTEXT_TYPE_ALL = 0
    D3D11_CONTEXT_TYPE_3D = 1
    D3D11_CONTEXT_TYPE_COMPUTE = 2
    D3D11_CONTEXT_TYPE_COPY = 3
    D3D11_CONTEXT_TYPE_VIDEO = 4


class D3D11_TEXTURE_LAYOUT(ENUM):
    D3D11_TEXTURE_LAYOUT_UNDEFINED = 0
    D3D11_TEXTURE_LAYOUT_ROW_MAJOR = 1
    D3D11_TEXTURE_LAYOUT_64K_STANDARD_SWIZZLE = 2

D3D11_TEXTURE2D_DESC1._fields_ = [
    ('Width', UINT),
    ('Height', UINT),
    ('MipLevels', UINT),
    ('ArraySize', UINT),
    ('Format', DXGI_FORMAT),
    ('SampleDesc', DXGI_SAMPLE_DESC),
    ('Usage', D3D11_USAGE),
    ('BindFlags', UINT),
    ('CPUAccessFlags', UINT),
    ('MiscFlags', UINT),
    ('TextureLayout', D3D11_TEXTURE_LAYOUT),
]

CD3D11_TEXTURE2D_DESC1 = D3D11_TEXTURE2D_DESC1
  
IID_ID3D11Texture2D1 = MIDL_INTERFACE(
    "{51218251-1E33-4617-9CCB-4D3A4367E7BB}"
)
ID3D11Texture2D1._iid_ = IID_ID3D11Texture2D1


ID3D11Texture2D1._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc1')],
        VOID,
        'GetDesc1',
        (['out'], POINTER(D3D11_TEXTURE2D_DESC1), 'pDesc'),
    ),
]

D3D11_TEXTURE3D_DESC1._fields_ = [
    ('Width', UINT),
    ('Height', UINT),
    ('Depth', UINT),
    ('MipLevels', UINT),
    ('Format', DXGI_FORMAT),
    ('Usage', D3D11_USAGE),
    ('BindFlags', UINT),
    ('CPUAccessFlags', UINT),
    ('MiscFlags', UINT),
    ('TextureLayout', D3D11_TEXTURE_LAYOUT),
]

CD3D11_TEXTURE3D_DESC1 = D3D11_TEXTURE3D_DESC1
      
IID_ID3D11Texture3D1 = MIDL_INTERFACE(
    "{0C711683-2853-4846-9BB0-F3E60639E46A}"
)
ID3D11Texture3D1._iid_ = IID_ID3D11Texture3D1


ID3D11Texture3D1._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc1')],
        VOID,
        'GetDesc1',
        (['out'], POINTER(D3D11_TEXTURE3D_DESC1), 'pDesc'),
    ),
]

class D3D11_CONSERVATIVE_RASTERIZATION_MODE(ENUM):
    D3D11_CONSERVATIVE_RASTERIZATION_MODE_OFF = 0
    D3D11_CONSERVATIVE_RASTERIZATION_MODE_ON = 1

D3D11_RASTERIZER_DESC2._fields_ = [
    ('FillMode', D3D11_FILL_MODE),
    ('CullMode', D3D11_CULL_MODE),
    ('FrontCounterClockwise', BOOL),
    ('DepthBias', INT),
    ('DepthBiasClamp', FLOAT),
    ('SlopeScaledDepthBias', FLOAT),
    ('DepthClipEnable', BOOL),
    ('ScissorEnable', BOOL),
    ('MultisampleEnable', BOOL),
    ('AntialiasedLineEnable', BOOL),
    ('ForcedSampleCount', UINT),
    ('ConservativeRaster', D3D11_CONSERVATIVE_RASTERIZATION_MODE),
]

CD3D11_RASTERIZER_DESC2 = D3D11_RASTERIZER_DESC2
    
IID_ID3D11RasterizerState2 = MIDL_INTERFACE(
    "{6FBD02FB-209F-46C4-B059-2ED15586A6AC}"
)
ID3D11RasterizerState2._iid_ = IID_ID3D11RasterizerState2


ID3D11RasterizerState2._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc2')],
        VOID,
        'GetDesc2',
        (['out'], POINTER(D3D11_RASTERIZER_DESC2), 'pDesc'),
    ),
]

D3D11_TEX2D_SRV1._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
    ('PlaneSlice', UINT),
]

D3D11_TEX2D_ARRAY_SRV1._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
    ('PlaneSlice', UINT),
]


class _Union_1(ctypes.Union):
    pass


_Union_1._fields_ = [
    ('Buffer', D3D11_BUFFER_SRV),
    ('Texture1D', D3D11_TEX1D_SRV),
    ('Texture1DArray', D3D11_TEX1D_ARRAY_SRV),
    ('Texture2D', D3D11_TEX2D_SRV1),
    ('Texture2DArray', D3D11_TEX2D_ARRAY_SRV1),
    ('Texture2DMS', D3D11_TEX2DMS_SRV),
    ('Texture2DMSArray', D3D11_TEX2DMS_ARRAY_SRV),
    ('Texture3D', D3D11_TEX3D_SRV),
    ('TextureCube', D3D11_TEXCUBE_SRV),
    ('TextureCubeArray', D3D11_TEXCUBE_ARRAY_SRV),
    ('BufferEx', D3D11_BUFFEREX_SRV),
]
D3D11_SHADER_RESOURCE_VIEW_DESC1._Union_1 = _Union_1

D3D11_SHADER_RESOURCE_VIEW_DESC1._anonymous_ = (
    '_Union_1',
)

D3D11_SHADER_RESOURCE_VIEW_DESC1._fields_ = [
    ('Format', DXGI_FORMAT),
    ('ViewDimension', D3D11_SRV_DIMENSION),
    ('_Union_1', D3D11_SHADER_RESOURCE_VIEW_DESC1._Union_1),
]

CD3D11_SHADER_RESOURCE_VIEW_DESC1 = D3D11_SHADER_RESOURCE_VIEW_DESC1
  
IID_ID3D11ShaderResourceView1 = MIDL_INTERFACE(
    "{91308B87-9040-411D-8C67-C39253CE3802}"
)
ID3D11ShaderResourceView1._iid_ = IID_ID3D11ShaderResourceView1


ID3D11ShaderResourceView1._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc1')],
        VOID,
        'GetDesc1',
        (
            ['out'],
            POINTER(D3D11_SHADER_RESOURCE_VIEW_DESC1),
            'pDesc1'
        ),
    ),
]

D3D11_TEX2D_RTV1._fields_ = [
    ('MipSlice', UINT),
    ('PlaneSlice', UINT),
]

D3D11_TEX2D_ARRAY_RTV1._fields_ = [
    ('MipSlice', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
    ('PlaneSlice', UINT),
]


class _Union_2(ctypes.Union):
    pass


_Union_2._fields_ = [
    ('Buffer', D3D11_BUFFER_RTV),
    ('Texture1D', D3D11_TEX1D_RTV),
    ('Texture1DArray', D3D11_TEX1D_ARRAY_RTV),
    ('Texture2D', D3D11_TEX2D_RTV1),
    ('Texture2DArray', D3D11_TEX2D_ARRAY_RTV1),
    ('Texture2DMS', D3D11_TEX2DMS_RTV),
    ('Texture2DMSArray', D3D11_TEX2DMS_ARRAY_RTV),
    ('Texture3D', D3D11_TEX3D_RTV),
]
D3D11_RENDER_TARGET_VIEW_DESC1._Union_2 = _Union_2

D3D11_RENDER_TARGET_VIEW_DESC1._anonymous_ = (
    '_Union_2',
)

D3D11_RENDER_TARGET_VIEW_DESC1._fields_ = [
    ('Format', DXGI_FORMAT),
    ('ViewDimension', D3D11_RTV_DIMENSION),
    ('_Union_2', D3D11_RENDER_TARGET_VIEW_DESC1._Union_2),
]

CD3D11_RENDER_TARGET_VIEW_DESC1 = D3D11_RENDER_TARGET_VIEW_DESC1

IID_ID3D11RenderTargetView1 = MIDL_INTERFACE(
    "{FFBE2E23-F011-418A-AC56-5CEED7C5B94B}"
)
ID3D11RenderTargetView1._iid_ = IID_ID3D11RenderTargetView1


ID3D11RenderTargetView1._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc1')],
        VOID,
        'GetDesc1',
        (
            ['out'],
            POINTER(D3D11_RENDER_TARGET_VIEW_DESC1),
            'pDesc1'
        ),
    ),
]

D3D11_TEX2D_UAV1._fields_ = [
    ('MipSlice', UINT),
    ('PlaneSlice', UINT),
]

D3D11_TEX2D_ARRAY_UAV1._fields_ = [
    ('MipSlice', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
    ('PlaneSlice', UINT),
]


class _Union_3(ctypes.Union):
    pass


_Union_3._fields_ = [
    ('Buffer', D3D11_BUFFER_UAV),
    ('Texture1D', D3D11_TEX1D_UAV),
    ('Texture1DArray', D3D11_TEX1D_ARRAY_UAV),
    ('Texture2D', D3D11_TEX2D_UAV1),
    ('Texture2DArray', D3D11_TEX2D_ARRAY_UAV1),
    ('Texture3D', D3D11_TEX3D_UAV),
]
D3D11_UNORDERED_ACCESS_VIEW_DESC1._Union_3 = _Union_3

D3D11_UNORDERED_ACCESS_VIEW_DESC1._anonymous_ = (
    '_Union_3',
)

D3D11_UNORDERED_ACCESS_VIEW_DESC1._fields_ = [
    ('Format', DXGI_FORMAT),
    ('ViewDimension', D3D11_UAV_DIMENSION),
    ('_Union_3', D3D11_UNORDERED_ACCESS_VIEW_DESC1._Union_3),
]

CD3D11_UNORDERED_ACCESS_VIEW_DESC1 = D3D11_UNORDERED_ACCESS_VIEW_DESC1
   
IID_ID3D11UnorderedAccessView1 = MIDL_INTERFACE(
    "{7B3B6153-A886-4544-AB37-6537C8500403}"
)
ID3D11UnorderedAccessView1._iid_ = IID_ID3D11UnorderedAccessView1


ID3D11UnorderedAccessView1._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc1')],
        VOID,
        'GetDesc1',
        (
            ['out'],
            POINTER(D3D11_UNORDERED_ACCESS_VIEW_DESC1),
            'pDesc1'
        ),
    ),
]

D3D11_QUERY_DESC1._fields_ = [
    ('Query', D3D11_QUERY),
    ('MiscFlags', UINT),
    ('ContextType', D3D11_CONTEXT_TYPE),
]

CD3D11_QUERY_DESC1 = D3D11_QUERY_DESC1
  
IID_ID3D11Query1 = MIDL_INTERFACE(
    "{631B4766-36DC-461D-8DB6-C47E13E60916}"
)
ID3D11Query1._iid_ = IID_ID3D11Query1


ID3D11Query1._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc1')],
        VOID,
        'GetDesc1',
        (['out'], POINTER(D3D11_QUERY_DESC1), 'pDesc1'),
    ),
]

class D3D11_FENCE_FLAG(ENUM):
    D3D11_FENCE_FLAG_NONE = 0
    D3D11_FENCE_FLAG_SHARED = 0x2
    D3D11_FENCE_FLAG_SHARED_CROSS_ADAPTER = 0x4
    D3D11_FENCE_FLAG_NON_MONITORED = 0x8


IID_ID3D11DeviceContext3 = MIDL_INTERFACE(
    "{B4E3C01D-E79E-4637-91B2-510E9F4C9B8F}"
)
ID3D11DeviceContext3._iid_ = IID_ID3D11DeviceContext3


ID3D11DeviceContext3._methods_ = [
    COMMETHOD(
        [helpstring('Method Flush1')],
        VOID,
        'Flush1',
        ([], D3D11_CONTEXT_TYPE, 'ContextType'),
        (['in'], HANDLE, 'hEvent'),
    ),
    COMMETHOD(
        [helpstring('Method SetHardwareProtectionState')],
        VOID,
        'SetHardwareProtectionState',
        (['in'], BOOL, 'HwProtectionEnable'),
    ),
    COMMETHOD(
        [helpstring('Method GetHardwareProtectionState')],
        VOID,
        'GetHardwareProtectionState',
        (['out'], POINTER(BOOL), 'pHwProtectionEnable'),
    ),
]

IID_ID3D11Fence = MIDL_INTERFACE(
    "{AFFDE9D1-1DF7-4BB7-8A34-0F46251DAB80}"
)
ID3D11Fence._iid_ = IID_ID3D11Fence


ID3D11Fence._methods_ = [
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
    COMMETHOD(
        [helpstring('Method GetCompletedValue')],
        UINT64,
        'GetCompletedValue',
    ),
    COMMETHOD(
        [helpstring('Method SetEventOnCompletion')],
        HRESULT,
        'SetEventOnCompletion',
        (['in'], UINT64, 'Value'),
        (['in'], HANDLE, 'hEvent'),
    ),
]

IID_ID3D11DeviceContext4 = MIDL_INTERFACE(
    "{917600DA-F58C-4C33-98D8-3E15B390FA24}"
)
ID3D11DeviceContext4._iid_ = IID_ID3D11DeviceContext4


ID3D11DeviceContext4._methods_ = [
    COMMETHOD(
        [helpstring('Method Signal')],
        HRESULT,
        'Signal',
        (['in'], POINTER(ID3D11Fence), 'pFence'),
        (['in'], UINT64, 'Value'),
    ),
    COMMETHOD(
        [helpstring('Method Wait')],
        HRESULT,
        'Wait',
        (['in'], POINTER(ID3D11Fence), 'pFence'),
        (['in'], UINT64, 'Value'),
    ),
]

IID_ID3D11Device3 = MIDL_INTERFACE(
    "{A05C8C37-D2C6-4732-B3A0-9CE0B0DC9AE6}"
)
ID3D11Device3._iid_ = IID_ID3D11Device3


ID3D11Device3._methods_ = [
    COMMETHOD(
        [helpstring('Method CreateTexture2D1')],
        HRESULT,
        'CreateTexture2D1',
        (['in'], POINTER(D3D11_TEXTURE2D_DESC1), 'pDesc1'),
        (['in'], POINTER(D3D11_SUBRESOURCE_DATA), 'pInitialData'),
        (
            ['out'],
            POINTER(POINTER(ID3D11Texture2D1)),
            'ppTexture2D'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateTexture3D1')],
        HRESULT,
        'CreateTexture3D1',
        (['in'], POINTER(D3D11_TEXTURE3D_DESC1), 'pDesc1'),
        (['in'], POINTER(D3D11_SUBRESOURCE_DATA), 'pInitialData'),
        (
            ['out'],
            POINTER(POINTER(ID3D11Texture3D1)),
            'ppTexture3D'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateRasterizerState2')],
        HRESULT,
        'CreateRasterizerState2',
        (
            ['in'],
            POINTER(D3D11_RASTERIZER_DESC2),
            'pRasterizerDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11RasterizerState2)),
            'ppRasterizerState'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateShaderResourceView1')],
        HRESULT,
        'CreateShaderResourceView1',
        (['in'], POINTER(ID3D11Resource), 'pResource'),
        (
            ['in'],
            POINTER(D3D11_SHADER_RESOURCE_VIEW_DESC1),
            'pDesc1'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11ShaderResourceView1)),
            'ppSRView1'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateUnorderedAccessView1')],
        HRESULT,
        'CreateUnorderedAccessView1',
        (['in'], POINTER(ID3D11Resource), 'pResource'),
        (
            ['in'],
            POINTER(D3D11_UNORDERED_ACCESS_VIEW_DESC1),
            'pDesc1'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11UnorderedAccessView1)),
            'ppUAView1'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateRenderTargetView1')],
        HRESULT,
        'CreateRenderTargetView1',
        (['in'], POINTER(ID3D11Resource), 'pResource'),
        (
            ['in'],
            POINTER(D3D11_RENDER_TARGET_VIEW_DESC1),
            'pDesc1'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11RenderTargetView1)),
            'ppRTView1'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateQuery1')],
        HRESULT,
        'CreateQuery1',
        (['in'], POINTER(D3D11_QUERY_DESC1), 'pQueryDesc1'),
        (['out'], POINTER(POINTER(ID3D11Query1)), 'ppQuery1'),
    ),
    COMMETHOD(
        [helpstring('Method GetImmediateContext3')],
        VOID,
        'GetImmediateContext3',
        (
            ['out'],
            POINTER(POINTER(ID3D11DeviceContext3)),
            'ppImmediateContext'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateDeferredContext3')],
        HRESULT,
        'CreateDeferredContext3',
        ([], UINT, 'ContextFlags'),
        (
            ['out'],
            POINTER(POINTER(ID3D11DeviceContext3)),
            'ppDeferredContext'
        ),
    ),
    COMMETHOD(
        [helpstring('Method WriteToSubresource')],
        VOID,
        'WriteToSubresource',
        (['in'], POINTER(ID3D11Resource), 'pDstResource'),
        (['in'], UINT, 'DstSubresource'),
        (['in'], POINTER(D3D11_BOX), 'pDstBox'),
        (['in'], POINTER(VOID), 'pSrcData'),
        (['in'], UINT, 'SrcRowPitch'),
        (['in'], UINT, 'SrcDepthPitch'),
    ),
    COMMETHOD(
        [helpstring('Method ReadFromSubresource')],
        VOID,
        'ReadFromSubresource',
        (['out'], POINTER(VOID), 'pDstData'),
        (['in'], UINT, 'DstRowPitch'),
        (['in'], UINT, 'DstDepthPitch'),
        (['in'], POINTER(ID3D11Resource), 'pSrcResource'),
        (['in'], UINT, 'SrcSubresource'),
        (['in'], POINTER(D3D11_BOX), 'pSrcBox'),
    ),
]
IID_ID3D11Texture2D1 = GUID('{51218251-1E33-4617-9CCB-4D3A4367E7BB}')

IID_ID3D11Texture3D1 = GUID('{C711683-2853-4846-9BB0-F3E60639E46A}')

IID_ID3D11RasterizerState2 = GUID('{6FBD02FB-209F-46C4-B059-2ED15586A6AC}')

IID_ID3D11ShaderResourceView1 = GUID('{91308B87-9040-411D-8C67-C39253CE3802}')

IID_ID3D11RenderTargetView1 = GUID('{FFBE2E23-F011-418A-AC56-5CEED7C5B94B}')

IID_ID3D11UnorderedAccessView1 = GUID('{7B3B6153-A886-4544-AB37-6537C8500403}')

IID_ID3D11Query1 = GUID('{631B4766-36DC-461D-8DB6-C47E13E60916}')

IID_ID3D11DeviceContext3 = GUID('{B4E3C01D-E79E-4637-91B2-510E9F4C9B8F}')

IID_ID3D11Fence = GUID('{AFFDE9D1-1DF7-4BB7-8A34-0F46251DAB80}')

IID_ID3D11DeviceContext4 = GUID('{917600DA-F58C-4C33-98D8-3E15B390FA24}')

IID_ID3D11Device3 = GUID('{A05C8C37-D2C6-4732-B3A0-9CE0B0DC9AE6}')


