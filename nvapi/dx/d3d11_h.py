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


from .dxgi_format_h import *
from .dxgicommon_h import *
from .d3dcommon_h import *


class ID3D11Device(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = None



class D3D11_INPUT_ELEMENT_DESC(ctypes.Structure):
    pass


class D3D11_SO_DECLARATION_ENTRY(ctypes.Structure):
    pass


class D3D11_VIEWPORT(ctypes.Structure):
    pass


class D3D11_DRAW_INSTANCED_INDIRECT_ARGS(ctypes.Structure):
    pass


class D3D11_DRAW_INDEXED_INSTANCED_INDIRECT_ARGS(ctypes.Structure):
    pass


class D3D11_BOX(ctypes.Structure):
    pass


class D3D11_DEPTH_STENCILOP_DESC(ctypes.Structure):
    pass


class D3D11_DEPTH_STENCIL_DESC(ctypes.Structure):
    pass


class D3D11_RENDER_TARGET_BLEND_DESC(ctypes.Structure):
    pass


class D3D11_BLEND_DESC(ctypes.Structure):
    pass


class D3D11_RASTERIZER_DESC(ctypes.Structure):
    pass


class D3D11_MAPPED_SUBRESOURCE(ctypes.Structure):
    pass


class D3D11_BUFFER_DESC(ctypes.Structure):
    pass


class D3D11_TEXTURE1D_DESC(ctypes.Structure):
    pass


class D3D11_TEXTURE2D_DESC(ctypes.Structure):
    pass


class D3D11_TEXTURE3D_DESC(ctypes.Structure):
    pass


class D3D11_BUFFER_SRV(ctypes.Structure):
    pass


class D3D11_BUFFEREX_SRV(ctypes.Structure):
    pass


class D3D11_TEX1D_SRV(ctypes.Structure):
    pass


class D3D11_TEX1D_ARRAY_SRV(ctypes.Structure):
    pass


class D3D11_TEX2D_SRV(ctypes.Structure):
    pass


class D3D11_TEX2D_ARRAY_SRV(ctypes.Structure):
    pass


class D3D11_TEX3D_SRV(ctypes.Structure):
    pass


class D3D11_TEXCUBE_SRV(ctypes.Structure):
    pass


class D3D11_TEXCUBE_ARRAY_SRV(ctypes.Structure):
    pass


class D3D11_TEX2DMS_SRV(ctypes.Structure):
    pass


class D3D11_TEX2DMS_ARRAY_SRV(ctypes.Structure):
    pass


class D3D11_SHADER_RESOURCE_VIEW_DESC(ctypes.Structure):
    pass


class D3D11_BUFFER_RTV(ctypes.Structure):
    pass


class D3D11_TEX1D_RTV(ctypes.Structure):
    pass


class D3D11_TEX1D_ARRAY_RTV(ctypes.Structure):
    pass


class D3D11_TEX2D_RTV(ctypes.Structure):
    pass


class D3D11_TEX2DMS_RTV(ctypes.Structure):
    pass


class D3D11_TEX2D_ARRAY_RTV(ctypes.Structure):
    pass


class D3D11_TEX2DMS_ARRAY_RTV(ctypes.Structure):
    pass


class D3D11_TEX3D_RTV(ctypes.Structure):
    pass


class D3D11_RENDER_TARGET_VIEW_DESC(ctypes.Structure):
    pass


class D3D11_TEX1D_DSV(ctypes.Structure):
    pass


class D3D11_TEX1D_ARRAY_DSV(ctypes.Structure):
    pass


class D3D11_TEX2D_DSV(ctypes.Structure):
    pass


class D3D11_TEX2D_ARRAY_DSV(ctypes.Structure):
    pass


class D3D11_TEX2DMS_DSV(ctypes.Structure):
    pass


class D3D11_TEX2DMS_ARRAY_DSV(ctypes.Structure):
    pass


class D3D11_DEPTH_STENCIL_VIEW_DESC(ctypes.Structure):
    pass


class D3D11_BUFFER_UAV(ctypes.Structure):
    pass


class D3D11_TEX1D_UAV(ctypes.Structure):
    pass


class D3D11_TEX1D_ARRAY_UAV(ctypes.Structure):
    pass


class D3D11_TEX2D_UAV(ctypes.Structure):
    pass


class D3D11_TEX2D_ARRAY_UAV(ctypes.Structure):
    pass


class D3D11_TEX3D_UAV(ctypes.Structure):
    pass


class D3D11_UNORDERED_ACCESS_VIEW_DESC(ctypes.Structure):
    pass


class D3D11_SAMPLER_DESC(ctypes.Structure):
    pass


class D3D11_QUERY_DESC(ctypes.Structure):
    pass


class D3D11_QUERY_DATA_TIMESTAMP_DISJOINT(ctypes.Structure):
    pass


class D3D11_QUERY_DATA_PIPELINE_STATISTICS(ctypes.Structure):
    pass


class D3D11_QUERY_DATA_SO_STATISTICS(ctypes.Structure):
    pass


class D3D11_COUNTER_DESC(ctypes.Structure):
    pass


class D3D11_COUNTER_INFO(ctypes.Structure):
    pass


class D3D11_CLASS_INSTANCE_DESC(ctypes.Structure):
    pass


class D3D11_FEATURE_DATA_THREADING(ctypes.Structure):
    pass


class D3D11_FEATURE_DATA_DOUBLES(ctypes.Structure):
    pass


class D3D11_FEATURE_DATA_FORMAT_SUPPORT(ctypes.Structure):
    pass


class D3D11_FEATURE_DATA_FORMAT_SUPPORT2(ctypes.Structure):
    pass


class D3D11_FEATURE_DATA_D3D10_X_HARDWARE_OPTIONS(ctypes.Structure):
    pass


class D3D11_FEATURE_DATA_D3D11_OPTIONS(ctypes.Structure):
    pass


class D3D11_FEATURE_DATA_ARCHITECTURE_INFO(ctypes.Structure):
    pass


class D3D11_FEATURE_DATA_D3D9_OPTIONS(ctypes.Structure):
    pass


class D3D11_FEATURE_DATA_D3D9_SHADOW_SUPPORT(ctypes.Structure):
    pass


class D3D11_FEATURE_DATA_SHADER_MIN_PRECISION_SUPPORT(ctypes.Structure):
    pass


class D3D11_FEATURE_DATA_D3D11_OPTIONS1(ctypes.Structure):
    pass


class D3D11_FEATURE_DATA_D3D9_SIMPLE_INSTANCING_SUPPORT(ctypes.Structure):
    pass


class D3D11_FEATURE_DATA_MARKER_SUPPORT(ctypes.Structure):
    pass


class D3D11_FEATURE_DATA_D3D9_OPTIONS1(ctypes.Structure):
    pass


class D3D11_FEATURE_DATA_D3D11_OPTIONS2(ctypes.Structure):
    pass


class D3D11_FEATURE_DATA_D3D11_OPTIONS3(ctypes.Structure):
    pass


class D3D11_FEATURE_DATA_GPU_VIRTUAL_ADDRESS_SUPPORT(ctypes.Structure):
    pass


class D3D11_FEATURE_DATA_SHADER_CACHE(ctypes.Structure):
    pass


class D3D11_FEATURE_DATA_D3D11_OPTIONS5(ctypes.Structure):
    pass


class D3D11_VIDEO_DECODER_DESC(ctypes.Structure):
    pass


class D3D11_VIDEO_DECODER_CONFIG(ctypes.Structure):
    pass


class _D3D11_AES_CTR_IV(ctypes.Structure):
    pass


D3D11_AES_CTR_IV = _D3D11_AES_CTR_IV


class D3D11_ENCRYPTED_BLOCK_INFO(ctypes.Structure):
    pass


class D3D11_VIDEO_DECODER_BUFFER_DESC(ctypes.Structure):
    pass


class D3D11_VIDEO_DECODER_EXTENSION(ctypes.Structure):
    pass


class D3D11_VIDEO_PROCESSOR_CAPS(ctypes.Structure):
    pass


class D3D11_VIDEO_PROCESSOR_RATE_CONVERSION_CAPS(ctypes.Structure):
    pass


class D3D11_VIDEO_CONTENT_PROTECTION_CAPS(ctypes.Structure):
    pass


class D3D11_VIDEO_PROCESSOR_CUSTOM_RATE(ctypes.Structure):
    pass


class D3D11_VIDEO_PROCESSOR_FILTER_RANGE(ctypes.Structure):
    pass


class D3D11_VIDEO_PROCESSOR_CONTENT_DESC(ctypes.Structure):
    pass


class D3D11_VIDEO_COLOR_RGBA(ctypes.Structure):
    pass


class D3D11_VIDEO_COLOR_YCbCrA(ctypes.Structure):
    pass


class D3D11_VIDEO_COLOR(ctypes.Structure):
    pass


class D3D11_VIDEO_PROCESSOR_COLOR_SPACE(ctypes.Structure):
    pass


class D3D11_VIDEO_PROCESSOR_STREAM(ctypes.Structure):
    pass


class D3D11_OMAC(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_QUERY_INPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_QUERY_OUTPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_PROTECTION_FLAGS(ctypes.Union):
    pass


class D3D11_AUTHENTICATED_QUERY_PROTECTION_OUTPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_QUERY_CHANNEL_TYPE_OUTPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_QUERY_DEVICE_HANDLE_OUTPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_QUERY_CRYPTO_SESSION_INPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_QUERY_CRYPTO_SESSION_OUTPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_COUNT_OUTPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_INPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_OUTPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_QUERY_UNRESTRICTED_PROTECTED_SHARED_RESOURCE_COUNT_OUTPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_QUERY_OUTPUT_ID_COUNT_INPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_QUERY_OUTPUT_ID_COUNT_OUTPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_QUERY_OUTPUT_ID_INPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_QUERY_OUTPUT_ID_OUTPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_QUERY_ACESSIBILITY_OUTPUT(ctypes.Structure):
    pass


D3D11_AUTHENTICATED_QUERY_ACCESSIBILITY_OUTPUT = D3D11_AUTHENTICATED_QUERY_ACESSIBILITY_OUTPUT


class D3D11_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_COUNT_OUTPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_INPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_OUTPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_QUERY_CURRENT_ACCESSIBILITY_ENCRYPTION_OUTPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_CONFIGURE_INPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_CONFIGURE_OUTPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_CONFIGURE_INITIALIZE_INPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_CONFIGURE_PROTECTION_INPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_CONFIGURE_CRYPTO_SESSION_INPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE_INPUT(ctypes.Structure):
    pass


class D3D11_AUTHENTICATED_CONFIGURE_ACCESSIBLE_ENCRYPTION_INPUT(ctypes.Structure):
    pass


class D3D11_TEX2D_VDOV(ctypes.Structure):
    pass


class D3D11_VIDEO_DECODER_OUTPUT_VIEW_DESC(ctypes.Structure):
    pass


class D3D11_TEX2D_VPIV(ctypes.Structure):
    pass


class D3D11_VIDEO_PROCESSOR_INPUT_VIEW_DESC(ctypes.Structure):
    pass


class D3D11_TEX2D_VPOV(ctypes.Structure):
    pass


class D3D11_TEX2D_ARRAY_VPOV(ctypes.Structure):
    pass


class D3D11_VIDEO_PROCESSOR_OUTPUT_VIEW_DESC(ctypes.Structure):
    pass



class ID3D11DeviceChild(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []



class ID3D11DepthStencilState(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11BlendState(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11RasterizerState(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11Resource(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11Buffer(ID3D11Resource):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11Texture1D(ID3D11Resource):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11Texture2D(ID3D11Resource):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11Texture3D(ID3D11Resource):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11View(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11ShaderResourceView(ID3D11View):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11RenderTargetView(ID3D11View):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11DepthStencilView(ID3D11View):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11UnorderedAccessView(ID3D11View):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11VertexShader(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11HullShader(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11DomainShader(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11GeometryShader(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11PixelShader(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11ComputeShader(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11InputLayout(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11SamplerState(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11Asynchronous(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11Query(ID3D11Asynchronous):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11Predicate(ID3D11Query):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11Counter(ID3D11Asynchronous):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11ClassInstance(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11ClassLinkage(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11CommandList(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11DeviceContext(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class D3D11_FEATURE(ENUM):
    D3D11_FEATURE_THREADING	= 0
    D3D11_FEATURE_DOUBLES = D3D11_FEATURE_THREADING + 1
    D3D11_FEATURE_FORMAT_SUPPORT = D3D11_FEATURE_DOUBLES + 1
    D3D11_FEATURE_FORMAT_SUPPORT2 = D3D11_FEATURE_FORMAT_SUPPORT + 1
    D3D11_FEATURE_D3D10_X_HARDWARE_OPTIONS = D3D11_FEATURE_FORMAT_SUPPORT2 + 1
    D3D11_FEATURE_D3D11_OPTIONS	= D3D11_FEATURE_D3D10_X_HARDWARE_OPTIONS + 1
    D3D11_FEATURE_ARCHITECTURE_INFO	= D3D11_FEATURE_D3D11_OPTIONS + 1
    D3D11_FEATURE_D3D9_OPTIONS = D3D11_FEATURE_ARCHITECTURE_INFO + 1
    D3D11_FEATURE_SHADER_MIN_PRECISION_SUPPORT = D3D11_FEATURE_D3D9_OPTIONS + 1
    D3D11_FEATURE_D3D9_SHADOW_SUPPORT = D3D11_FEATURE_SHADER_MIN_PRECISION_SUPPORT + 1
    D3D11_FEATURE_D3D11_OPTIONS1 = D3D11_FEATURE_D3D9_SHADOW_SUPPORT + 1
    D3D11_FEATURE_D3D9_SIMPLE_INSTANCING_SUPPORT = D3D11_FEATURE_D3D11_OPTIONS1 + 1
    D3D11_FEATURE_MARKER_SUPPORT = D3D11_FEATURE_D3D9_SIMPLE_INSTANCING_SUPPORT + 1
    D3D11_FEATURE_D3D9_OPTIONS1	= D3D11_FEATURE_MARKER_SUPPORT + 1
    D3D11_FEATURE_D3D11_OPTIONS2 = D3D11_FEATURE_D3D9_OPTIONS1 + 1
    D3D11_FEATURE_D3D11_OPTIONS3 = D3D11_FEATURE_D3D11_OPTIONS2 + 1
    D3D11_FEATURE_GPU_VIRTUAL_ADDRESS_SUPPORT = D3D11_FEATURE_D3D11_OPTIONS3 + 1
    D3D11_FEATURE_D3D11_OPTIONS4 = D3D11_FEATURE_GPU_VIRTUAL_ADDRESS_SUPPORT + 1
    D3D11_FEATURE_SHADER_CACHE = D3D11_FEATURE_D3D11_OPTIONS4 + 1
    D3D11_FEATURE_D3D11_OPTIONS5 = D3D11_FEATURE_SHADER_CACHE + 1


class D3D11_COUNTER_TYPE(ENUM):
    D3D11_COUNTER_TYPE_FLOAT32 = 0
    D3D11_COUNTER_TYPE_UINT16 = D3D11_COUNTER_TYPE_FLOAT32 + 1
    D3D11_COUNTER_TYPE_UINT32 = D3D11_COUNTER_TYPE_UINT16 + 1
    D3D11_COUNTER_TYPE_UINT64 = D3D11_COUNTER_TYPE_UINT32 + 1


class D3D11_SUBRESOURCE_DATA(ctypes.Structure):
    _fields_ = [
        ('pSysMem', POINTER(VOID)),
        ('SysMemPitch', UINT),
        ('SysMemSlicePitch', UINT),
    ]


class D3D11_MAPPED_SUBRESOURCE(ctypes.Structure):
    _fields_ = [
        ('pData', POINTER(VOID)),
        ('RowPitch', UINT),
        ('DepthPitch', UINT)
    ]


ID3D11Device._methods_ = [
    # Create*
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateBuffer',
        (
            ['in'],
            POINTER(D3D11_BUFFER_DESC),
            'pDesc'
        ),
        (
            ['in'],
            POINTER(D3D11_SUBRESOURCE_DATA),
            'pInitialData'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11Buffer)),
            'ppBuffer'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateTexture1D',
        (
            ['in'],
            POINTER(D3D11_TEXTURE1D_DESC),
            'pDesc'
        ),
        (
            ['in'],
            POINTER(D3D11_SUBRESOURCE_DATA),
            'pInitialData'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11Texture1D)),
            'ppTexture1D'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateTexture2D',
        (
            ['in'],
            POINTER(D3D11_TEXTURE2D_DESC),
            'pDesc'
        ),
        (
            ['in'],
            POINTER(D3D11_SUBRESOURCE_DATA),
            'pInitialData'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11Texture2D)),
            'ppTexture2D'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateTexture3D',
        (
            ['in'],
            POINTER(D3D11_TEXTURE3D_DESC),
            'pDesc'
        ),
        (
            ['in'],
            POINTER(D3D11_SUBRESOURCE_DATA),
            'pInitialData'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11Texture3D)),
            'ppTexture3D'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateShaderResourceView',
        (
            ['in'],
            POINTER(ID3D11Resource),
            'pResource'
        ),
        (
            ['in'],
            POINTER(D3D11_SHADER_RESOURCE_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11ShaderResourceView)),
            'ppSRView'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateUnorderedAccessView',
        (
            ['in'],
            POINTER(ID3D11Resource),
            'pResource'
        ),
        (
            ['in'],
            POINTER(D3D11_UNORDERED_ACCESS_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11UnorderedAccessView)),
            'ppUAView'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateRenderTargetView',
        (
            ['in'],
            POINTER(ID3D11Resource),
            'pResource'
        ),
        (
            ['in'],
            POINTER(D3D11_RENDER_TARGET_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11RenderTargetView)),
            'ppRTView'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateDepthStencilView',
        (
            ['in'],
            POINTER(ID3D11Resource),
            'pResource'
        ),
        (
            ['in'],
            POINTER(D3D11_DEPTH_STENCIL_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11DepthStencilView)),
            'ppDepthStencilView'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateInputLayout',
        (
            ['in'],
            POINTER(D3D11_INPUT_ELEMENT_DESC),
            'pInputElementDescs'
        ),
        (
            ['in'],
            UINT,
            'NumElements'
        ),
        (
            ['in'],
            POINTER(VOID),
            'pShaderBytecodeWithInputSignature'
        ),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['out'],
            POINTER(POINTER(ID3D11InputLayout)),
            'ppInputLayout'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateVertexShader',
        (
            ['in'],
            POINTER(VOID),
            'pShaderBytecode'
        ),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11VertexShader)),
            'ppVertexShader'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateGeometryShader',
        (
            ['in'],
            POINTER(VOID),
            'pShaderBytecode'
        ),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11GeometryShader)),
            'ppGeometryShader'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateGeometryShaderWithStreamOutput',
        (
            ['in'],
            POINTER(VOID),
            'pShaderBytecode'
        ),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(D3D11_SO_DECLARATION_ENTRY),
            'pSODeclaration'
        ),
        (
            ['in'],
            UINT,
            'NumEntries'
        ),
        (
            ['in'],
            POINTER(UINT),
            'pBufferStrides'
        ),
        (
            ['in'],
            UINT,
            'NumStrides'
        ),
        (['in'], UINT, 'RasterizedStream'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11GeometryShader)),
            'ppGeometryShader'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreatePixelShader',
        (
            ['in'],
            POINTER(VOID),
            'pShaderBytecode'
        ),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11PixelShader)),
            'ppPixelShader'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateHullShader',
        (
            ['in'],
            POINTER(VOID),
            'pShaderBytecode'
        ),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11HullShader)),
            'ppHullShader'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateDomainShader',
        (
            ['in'],
            POINTER(VOID),
            'pShaderBytecode'
        ),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11DomainShader)),
            'ppDomainShader'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateComputeShader',
        (
            ['in'],
            POINTER(VOID),
            'pShaderBytecode'
        ),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11ComputeShader)),
            'ppComputeShader'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateClassLinkage',
        (
            ['out'],
            POINTER(POINTER(ID3D11ClassLinkage)),
            'ppLinkage'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateBlendState',
        (
            ['in'],
            POINTER(D3D11_BLEND_DESC),
            'pBlendStateDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11BlendState)),
            'ppBlendState'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateDepthStencilState',
        (
            ['in'],
            POINTER(D3D11_DEPTH_STENCIL_DESC),
            'pDepthStencilDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11DepthStencilState)),
            'ppDepthStencilState'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateRasterizerState',
        (
            ['in'],
            POINTER(D3D11_RASTERIZER_DESC),
            'pRasterizerDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11RasterizerState)),
            'ppRasterizerState'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateSamplerState',
        (
            ['in'],
            POINTER(D3D11_SAMPLER_DESC),
            'pSamplerDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11SamplerState)),
            'ppSamplerState'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateQuery',
        (
            ['in'],
            POINTER(D3D11_QUERY_DESC),
            'pQueryDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11Query)),
            'ppQuery'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreatePredicate',
        (
            ['in'],
            POINTER(D3D11_QUERY_DESC),
            'pPredicateDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11Predicate)),
            'ppPredicate'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateCounter',
        (
            ['in'],
            POINTER(D3D11_COUNTER_DESC),
            'pCounterDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11Counter)),
            'ppCounter'
        ),
    ),
    # Reserved parameter; must be 0        
    COMMETHOD(
        [],
        HRESULT,
        'CreateDeferredContext',
        (['in'], UINT, 'ContextFlags'),
        (
            ['out'],
            POINTER(POINTER(ID3D11DeviceContext)),
            'ppDeferredContext'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'OpenSharedResource',
        (['in'], HANDLE, 'hResource'),
        (['in'], REFIID, 'ReturnedInterface'),
        (
            ['out'],
            POINTER(POINTER(VOID)),
            'ppResource'
        ),
    ),
    # Check*
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CheckFormatSupport',
        (['in'], DXGI_FORMAT, 'Format'),
        (
            ['out'],
            POINTER(UINT),
            'pFormatSupport'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CheckMultisampleQualityLevels',
        (['in'], DXGI_FORMAT, 'Format'),
        (['in'], UINT, 'SampleCount'),
        (
            ['out'],
            POINTER(UINT),
            'pNumQualityLevels'
        ),
    ),
    COMMETHOD(
        [],
        VOID,
        'CheckCounterInfo',
        (
            ['out'],
            POINTER(D3D11_COUNTER_INFO),
            'pCounterInfo'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CheckCounter',
        (
            ['in'],
            POINTER(D3D11_COUNTER_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(D3D11_COUNTER_TYPE),
            'pType'
        ),
        (['in'], POINTER(UINT), 'pActiveCounters'),
        (
            ['out'],
            LPSTR,
            'szName'
        ),
        (
            ['out', 'in'],
            POINTER(UINT),
            'pNameLength'
        ),
        (
            ['out'],
            LPSTR,
            'szUnits'
        ),
        (['in'], POINTER(UINT), 'pUnitsLength'),
        (
            ['out'],
            LPSTR,
            'szDescription'
        ),
        (['in'], POINTER(UINT), 'pDescriptionLength'),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CheckFeatureSupport',
        (['in'], D3D11_FEATURE, 'Feature'),
        (
            ['out'],
            POINTER(VOID),
            'pFeatureSupportData'
        ),
        (['in'], UINT, 'FeatureSupportDataSize'),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'GetPrivateData',
        (['in'], REFGUID, 'guid'),
        (
            ['out', 'in'],
            POINTER(UINT),
            'pDataSize'
        ),
        (
            ['out'],
            POINTER(VOID),
            'pData'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'SetPrivateData',
        (['in'], REFGUID, 'guid'),
        (['in'], UINT, 'DataSize'),
        (
            ['in'],
            POINTER(VOID),
            'pData'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'SetPrivateDataInterface',
        (['in'], REFGUID, 'guid'),
        (
            ['in'],
            POINTER(comtypes.IUnknown),
            'pData'
        ),
    ),
    COMMETHOD(
        [],
        D3D_FEATURE_LEVEL,
        'GetFeatureLevel',
    ),
    COMMETHOD(
        [],
        UINT,
        'GetCreationFlags',
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDeviceRemovedReason',
    ),
    COMMETHOD(
        [],
        VOID,
        'GetImmediateContext',
        (
            ['out'],
            POINTER(POINTER(ID3D11DeviceContext)),
            'ppImmediateContext'
        ),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetExceptionMode',
        (['in'], UINT, 'RaiseFlags'),
    ),
    COMMETHOD(
        [],
        UINT,
        'GetExceptionMode',
    ),
]

class ID3D11VideoDecoder(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11VideoProcessorEnumerator(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11VideoProcessor(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11AuthenticatedChannel(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11CryptoSession(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11VideoDecoderOutputView(ID3D11View):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11VideoProcessorInputView(ID3D11View):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11VideoProcessorOutputView(ID3D11View):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11VideoContext(ID3D11DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11VideoDevice(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


ID3D11Device._methods_ = [
    # Create*
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateBuffer',
        (
            ['in'],
            POINTER(D3D11_BUFFER_DESC),
            'pDesc'
        ),
        (
            ['in'],
            POINTER(D3D11_SUBRESOURCE_DATA),
            'pInitialData'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11Buffer)),
            'ppBuffer'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateTexture1D',
        (
            ['in'],
            POINTER(D3D11_TEXTURE1D_DESC),
            'pDesc'
        ),
        (
            ['in'],
            POINTER(D3D11_SUBRESOURCE_DATA),
            'pInitialData'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11Texture1D)),
            'ppTexture1D'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateTexture2D',
        (
            ['in'],
            POINTER(D3D11_TEXTURE2D_DESC),
            'pDesc'
        ),
        (
            ['in'],
            POINTER(D3D11_SUBRESOURCE_DATA),
            'pInitialData'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11Texture2D)),
            'ppTexture2D'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateTexture3D',
        (
            ['in'],
            POINTER(D3D11_TEXTURE3D_DESC),
            'pDesc'
        ),
        (
            ['in'],
            POINTER(D3D11_SUBRESOURCE_DATA),
            'pInitialData'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11Texture3D)),
            'ppTexture3D'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateShaderResourceView',
        (
            ['in'],
            POINTER(ID3D11Resource),
            'pResource'
        ),
        (
            ['in'],
            POINTER(D3D11_SHADER_RESOURCE_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11ShaderResourceView)),
            'ppSRView'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateUnorderedAccessView',
        (
            ['in'],
            POINTER(ID3D11Resource),
            'pResource'
        ),
        (
            ['in'],
            POINTER(D3D11_UNORDERED_ACCESS_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11UnorderedAccessView)),
            'ppUAView'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateRenderTargetView',
        (
            ['in'],
            POINTER(ID3D11Resource),
            'pResource'
        ),
        (
            ['in'],
            POINTER(D3D11_RENDER_TARGET_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11RenderTargetView)),
            'ppRTView'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateDepthStencilView',
        (
            ['in'],
            POINTER(ID3D11Resource),
            'pResource'
        ),
        (
            ['in'],
            POINTER(D3D11_DEPTH_STENCIL_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11DepthStencilView)),
            'ppDepthStencilView'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateInputLayout',
        (
            ['in'],
            POINTER(D3D11_INPUT_ELEMENT_DESC),
            'pInputElementDescs'
        ),
        (
            ['in'],
            UINT,
            'NumElements'
        ),
        (
            ['in'],
            POINTER(VOID),
            'pShaderBytecodeWithInputSignature'
        ),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['out'],
            POINTER(POINTER(ID3D11InputLayout)),
            'ppInputLayout'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateVertexShader',
        (
            ['in'],
            POINTER(VOID),
            'pShaderBytecode'
        ),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11VertexShader)),
            'ppVertexShader'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateGeometryShader',
        (
            ['in'],
            POINTER(VOID),
            'pShaderBytecode'
        ),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11GeometryShader)),
            'ppGeometryShader'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateGeometryShaderWithStreamOutput',
        (
            ['in'],
            POINTER(VOID),
            'pShaderBytecode'
        ),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(D3D11_SO_DECLARATION_ENTRY),
            'pSODeclaration'
        ),
        (
            ['in'],
            UINT,
            'NumEntries'
        ),
        (
            ['in'],
            POINTER(UINT),
            'pBufferStrides'
        ),
        (
            ['in'],
            UINT,
            'NumStrides'
        ),
        (['in'], UINT, 'RasterizedStream'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11GeometryShader)),
            'ppGeometryShader'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreatePixelShader',
        (
            ['in'],
            POINTER(VOID),
            'pShaderBytecode'
        ),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11PixelShader)),
            'ppPixelShader'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateHullShader',
        (
            ['in'],
            POINTER(VOID),
            'pShaderBytecode'
        ),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11HullShader)),
            'ppHullShader'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateDomainShader',
        (
            ['in'],
            POINTER(VOID),
            'pShaderBytecode'
        ),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11DomainShader)),
            'ppDomainShader'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateComputeShader',
        (
            ['in'],
            POINTER(VOID),
            'pShaderBytecode'
        ),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11ComputeShader)),
            'ppComputeShader'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateClassLinkage',
        (
            ['out'],
            POINTER(POINTER(ID3D11ClassLinkage)),
            'ppLinkage'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateBlendState',
        (
            ['in'],
            POINTER(D3D11_BLEND_DESC),
            'pBlendStateDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11BlendState)),
            'ppBlendState'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateDepthStencilState',
        (
            ['in'],
            POINTER(D3D11_DEPTH_STENCIL_DESC),
            'pDepthStencilDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11DepthStencilState)),
            'ppDepthStencilState'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateRasterizerState',
        (
            ['in'],
            POINTER(D3D11_RASTERIZER_DESC),
            'pRasterizerDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11RasterizerState)),
            'ppRasterizerState'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateSamplerState',
        (
            ['in'],
            POINTER(D3D11_SAMPLER_DESC),
            'pSamplerDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11SamplerState)),
            'ppSamplerState'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateQuery',
        (
            ['in'],
            POINTER(D3D11_QUERY_DESC),
            'pQueryDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11Query)),
            'ppQuery'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreatePredicate',
        (
            ['in'],
            POINTER(D3D11_QUERY_DESC),
            'pPredicateDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11Predicate)),
            'ppPredicate'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateCounter',
        (
            ['in'],
            POINTER(D3D11_COUNTER_DESC),
            'pCounterDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11Counter)),
            'ppCounter'
        ),
    ),
    # Reserved parameter; must be 0        
    COMMETHOD(
        [],
        HRESULT,
        'CreateDeferredContext',
        (['in'], UINT, 'ContextFlags'),
        (
            ['out'],
            POINTER(POINTER(ID3D11DeviceContext)),
            'ppDeferredContext'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'OpenSharedResource',
        (['in'], HANDLE, 'hResource'),
        (['in'], REFIID, 'ReturnedInterface'),
        (
            ['out'],
            POINTER(POINTER(VOID)),
            'ppResource'
        ),
    ),
    # Check*
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CheckFormatSupport',
        (['in'], DXGI_FORMAT, 'Format'),
        (
            ['out'],
            POINTER(UINT),
            'pFormatSupport'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CheckMultisampleQualityLevels',
        (['in'], DXGI_FORMAT, 'Format'),
        (['in'], UINT, 'SampleCount'),
        (
            ['out'],
            POINTER(UINT),
            'pNumQualityLevels'
        ),
    ),
    COMMETHOD(
        [],
        VOID,
        'CheckCounterInfo',
        (
            ['out'],
            POINTER(D3D11_COUNTER_INFO),
            'pCounterInfo'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CheckCounter',
        (
            ['in'],
            POINTER(D3D11_COUNTER_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(D3D11_COUNTER_TYPE),
            'pType'
        ),
        (['in'], POINTER(UINT), 'pActiveCounters'),
        (
            ['out'],
            LPSTR,
            'szName'
        ),
        (
            ['out', 'in'],
            POINTER(UINT),
            'pNameLength'
        ),
        (
            ['out'],
            LPSTR,
            'szUnits'
        ),
        (['in'], POINTER(UINT), 'pUnitsLength'),
        (
            ['out'],
            LPSTR,
            'szDescription'
        ),
        (['in'], POINTER(UINT), 'pDescriptionLength'),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CheckFeatureSupport',
        (['in'], D3D11_FEATURE, 'Feature'),
        (
            ['out'],
            POINTER(VOID),
            'pFeatureSupportData'
        ),
        (['in'], UINT, 'FeatureSupportDataSize'),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'GetPrivateData',
        (['in'], REFGUID, 'guid'),
        (
            ['out', 'in'],
            POINTER(UINT),
            'pDataSize'
        ),
        (
            ['out'],
            POINTER(VOID),
            'pData'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'SetPrivateData',
        (['in'], REFGUID, 'guid'),
        (['in'], UINT, 'DataSize'),
        (
            ['in'],
            POINTER(VOID),
            'pData'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'SetPrivateDataInterface',
        (['in'], REFGUID, 'guid'),
        (
            ['in'],
            POINTER(comtypes.IUnknown),
            'pData'
        ),
    ),
    COMMETHOD(
        [],
        D3D_FEATURE_LEVEL,
        'GetFeatureLevel',
    ),
    COMMETHOD(
        [],
        UINT,
        'GetCreationFlags',
    ),
    COMMETHOD(
        [],
        HRESULT,
        'GetDeviceRemovedReason',
    ),
    COMMETHOD(
        [],
        VOID,
        'GetImmediateContext',
        (
            ['out'],
            POINTER(POINTER(ID3D11DeviceContext)),
            'ppImmediateContext'
        ),
    ),
    COMMETHOD(
        [],
        HRESULT,
        'SetExceptionMode',
        (['in'], UINT, 'RaiseFlags'),
    ),
    COMMETHOD(
        [],
        UINT,
        'GetExceptionMode',
    ),
]


from .dxgi_h import * # NOQA
from .d3dcommon_h import * # NOQA
   

class D3D11_INPUT_CLASSIFICATION(ENUM):
    D3D11_INPUT_PER_VERTEX_DATA = 0
    D3D11_INPUT_PER_INSTANCE_DATA = 1

D3D11_INPUT_ELEMENT_DESC._fields_ = [
    ('SemanticName', LPCSTR),
    ('SemanticIndex', UINT),
    ('Format', DXGI_FORMAT),
    ('InputSlot', UINT),
    ('AlignedByteOffset', UINT),
    ('InputSlotClass', D3D11_INPUT_CLASSIFICATION),
    ('InstanceDataStepRate', UINT),
]


class D3D11_FILL_MODE(ENUM):
    D3D11_FILL_WIREFRAME = 2
    D3D11_FILL_SOLID = 3

D3D11_PRIMITIVE_TOPOLOGY = D3D_PRIMITIVE_TOPOLOGY
D3D11_PRIMITIVE = D3D_PRIMITIVE


class D3D11_CULL_MODE(ENUM):
    D3D11_CULL_NONE = 1
    D3D11_CULL_FRONT = 2
    D3D11_CULL_BACK = 3

D3D11_SO_DECLARATION_ENTRY._fields_ = [
    ('Stream', UINT),
    ('SemanticName', LPCSTR),
    ('SemanticIndex', UINT),
    ('StartComponent', BYTE),
    ('ComponentCount', BYTE),
    ('OutputSlot', BYTE),
]

D3D11_VIEWPORT._fields_ = [
    ('TopLeftX', FLOAT),
    ('TopLeftY', FLOAT),
    ('Width', FLOAT),
    ('Height', FLOAT),
    ('MinDepth', FLOAT),
    ('MaxDepth', FLOAT),
]


D3D11_DRAW_INSTANCED_INDIRECT_ARGS._fields_ = [
    ('VertexCountPerInstance', UINT),
    ('InstanceCount', UINT),
    ('StartVertexLocation', UINT),
    ('StartInstanceLocation', UINT),
]

D3D11_DRAW_INDEXED_INSTANCED_INDIRECT_ARGS._fields_ = [
    ('IndexCountPerInstance', UINT),
    ('InstanceCount', UINT),
    ('StartIndexLocation', UINT),
    ('BaseVertexLocation', INT),
    ('StartInstanceLocation', UINT),
]


class D3D11_RESOURCE_DIMENSION(ENUM):
    D3D11_RESOURCE_DIMENSION_UNKNOWN = 0
    D3D11_RESOURCE_DIMENSION_BUFFER = 1
    D3D11_RESOURCE_DIMENSION_TEXTURE1D = 2
    D3D11_RESOURCE_DIMENSION_TEXTURE2D = 3
    D3D11_RESOURCE_DIMENSION_TEXTURE3D = 4

D3D11_SRV_DIMENSION = D3D_SRV_DIMENSION


class D3D11_DSV_DIMENSION(ENUM):
    D3D11_DSV_DIMENSION_UNKNOWN = 0
    D3D11_DSV_DIMENSION_TEXTURE1D = 1
    D3D11_DSV_DIMENSION_TEXTURE1DARRAY = 2
    D3D11_DSV_DIMENSION_TEXTURE2D = 3
    D3D11_DSV_DIMENSION_TEXTURE2DARRAY = 4
    D3D11_DSV_DIMENSION_TEXTURE2DMS = 5
    D3D11_DSV_DIMENSION_TEXTURE2DMSARRAY = 6


class D3D11_RTV_DIMENSION(ENUM):
    D3D11_RTV_DIMENSION_UNKNOWN = 0
    D3D11_RTV_DIMENSION_BUFFER = 1
    D3D11_RTV_DIMENSION_TEXTURE1D = 2
    D3D11_RTV_DIMENSION_TEXTURE1DARRAY = 3
    D3D11_RTV_DIMENSION_TEXTURE2D = 4
    D3D11_RTV_DIMENSION_TEXTURE2DARRAY = 5
    D3D11_RTV_DIMENSION_TEXTURE2DMS = 6
    D3D11_RTV_DIMENSION_TEXTURE2DMSARRAY = 7
    D3D11_RTV_DIMENSION_TEXTURE3D = 8


class D3D11_UAV_DIMENSION(ENUM):
    D3D11_UAV_DIMENSION_UNKNOWN = 0
    D3D11_UAV_DIMENSION_BUFFER = 1
    D3D11_UAV_DIMENSION_TEXTURE1D = 2
    D3D11_UAV_DIMENSION_TEXTURE1DARRAY = 3
    D3D11_UAV_DIMENSION_TEXTURE2D = 4
    D3D11_UAV_DIMENSION_TEXTURE2DARRAY = 5
    D3D11_UAV_DIMENSION_TEXTURE3D = 8


class D3D11_USAGE(ENUM):
    D3D11_USAGE_DEFAULT = 0
    D3D11_USAGE_IMMUTABLE = 1
    D3D11_USAGE_DYNAMIC = 2
    D3D11_USAGE_STAGING = 3


class D3D11_BIND_FLAG(ENUM):
    D3D11_BIND_VERTEX_BUFFER = 0x1
    D3D11_BIND_INDEX_BUFFER = 0x2
    D3D11_BIND_CONSTANT_BUFFER = 0x4
    D3D11_BIND_SHADER_RESOURCE = 0x8
    D3D11_BIND_STREAM_OUTPUT = 0x10
    D3D11_BIND_RENDER_TARGET = 0x20
    D3D11_BIND_DEPTH_STENCIL = 0x40
    D3D11_BIND_UNORDERED_ACCESS = 0x80
    D3D11_BIND_DECODER = 0x200
    D3D11_BIND_VIDEO_ENCODER = 0x400


class D3D11_CPU_ACCESS_FLAG(ENUM):
    D3D11_CPU_ACCESS_WRITE = 0x10000
    D3D11_CPU_ACCESS_READ = 0x20000


class D3D11_RESOURCE_MISC_FLAG(ENUM):
    D3D11_RESOURCE_MISC_GENERATE_MIPS = 0x1
    D3D11_RESOURCE_MISC_SHARED = 0x2
    D3D11_RESOURCE_MISC_TEXTURECUBE = 0x4
    D3D11_RESOURCE_MISC_DRAWINDIRECT_ARGS = 0x10
    D3D11_RESOURCE_MISC_BUFFER_ALLOW_RAW_VIEWS = 0x20
    D3D11_RESOURCE_MISC_BUFFER_STRUCTURED = 0x40
    D3D11_RESOURCE_MISC_RESOURCE_CLAMP = 0x80
    D3D11_RESOURCE_MISC_SHARED_KEYEDMUTEX = 0x100
    D3D11_RESOURCE_MISC_GDI_COMPATIBLE = 0x200
    D3D11_RESOURCE_MISC_SHARED_NTHANDLE = 0x800
    D3D11_RESOURCE_MISC_RESTRICTED_CONTENT = 0x1000
    D3D11_RESOURCE_MISC_RESTRICT_SHARED_RESOURCE = 0x2000
    D3D11_RESOURCE_MISC_RESTRICT_SHARED_RESOURCE_DRIVER = 0x4000
    D3D11_RESOURCE_MISC_GUARDED = 0x8000
    D3D11_RESOURCE_MISC_TILE_POOL = 0x20000
    D3D11_RESOURCE_MISC_TILED = 0x40000
    D3D11_RESOURCE_MISC_HW_PROTECTED = 0x80000


class D3D11_MAP(ENUM):
    D3D11_MAP_READ = 1
    D3D11_MAP_WRITE = 2
    D3D11_MAP_READ_WRITE = 3
    D3D11_MAP_WRITE_DISCARD = 4
    D3D11_MAP_WRITE_NO_OVERWRITE = 5


class D3D11_MAP_FLAG(ENUM):
    D3D11_MAP_FLAG_DO_NOT_WAIT = 0x100000


class D3D11_RAISE_FLAG(ENUM):
    D3D11_RAISE_FLAG_DRIVER_INTERNAL_ERROR = 0x1


class D3D11_CLEAR_FLAG(ENUM):
    D3D11_CLEAR_DEPTH = 0x1
    D3D11_CLEAR_STENCIL = 0x2

D3D11_RECT = RECT
CD3D11_RECT = D3D11_RECT

D3D11_BOX._fields_ = [
    ('left', UINT),
    ('top', UINT),
    ('front', UINT),
    ('right', UINT),
    ('bottom', UINT),
    ('back', UINT),
]

CD3D11_BOX = D3D11_BOX

IID_ID3D11DeviceChild = MIDL_INTERFACE(
    "{1841E5C8-16B0-489B-BCC8-44CFB0D5DEAE}"
)
ID3D11DeviceChild._iid_ = IID_ID3D11DeviceChild


ID3D11DeviceChild._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDevice')],
        VOID,
        'GetDevice',
        (['out'], POINTER(POINTER(ID3D11Device)), 'ppDevice'),
    ),
    COMMETHOD(
        [helpstring('Method GetPrivateData')],
        HRESULT,
        'GetPrivateData',
        (['in'], REFGUID, 'guid'),
        (['out', 'in'], POINTER(UINT), 'pDataSize'),
        (['out'], POINTER(VOID), 'pData'),
    ),
    COMMETHOD(
        [helpstring('Method SetPrivateData')],
        HRESULT,
        'SetPrivateData',
        (['in'], REFGUID, 'guid'),
        (['in'], UINT, 'DataSize'),
        (['in'], POINTER(VOID), 'pData'),
    ),
    COMMETHOD(
        [helpstring('Method SetPrivateDataInterface')],
        HRESULT,
        'SetPrivateDataInterface',
        (['in'], REFGUID, 'guid'),
        (['in'], POINTER(comtypes.IUnknown), 'pData'),
    ),
]

class D3D11_COMPARISON_FUNC(ENUM):
    D3D11_COMPARISON_NEVER = 1
    D3D11_COMPARISON_LESS = 2
    D3D11_COMPARISON_EQUAL = 3
    D3D11_COMPARISON_LESS_EQUAL = 4
    D3D11_COMPARISON_GREATER = 5
    D3D11_COMPARISON_NOT_EQUAL = 6
    D3D11_COMPARISON_GREATER_EQUAL = 7
    D3D11_COMPARISON_ALWAYS = 8


class D3D11_DEPTH_WRITE_MASK(ENUM):
    D3D11_DEPTH_WRITE_MASK_ZERO = 0
    D3D11_DEPTH_WRITE_MASK_ALL = 1


class D3D11_STENCIL_OP(ENUM):
    D3D11_STENCIL_OP_KEEP = 1
    D3D11_STENCIL_OP_ZERO = 2
    D3D11_STENCIL_OP_REPLACE = 3
    D3D11_STENCIL_OP_INCR_SAT = 4
    D3D11_STENCIL_OP_DECR_SAT = 5
    D3D11_STENCIL_OP_INVERT = 6
    D3D11_STENCIL_OP_INCR = 7
    D3D11_STENCIL_OP_DECR = 8

D3D11_DEPTH_STENCILOP_DESC._fields_ = [
    ('StencilFailOp', D3D11_STENCIL_OP),
    ('StencilDepthFailOp', D3D11_STENCIL_OP),
    ('StencilPassOp', D3D11_STENCIL_OP),
    ('StencilFunc', D3D11_COMPARISON_FUNC),
]

D3D11_DEPTH_STENCIL_DESC._fields_ = [
    ('DepthEnable', BOOL),
    ('DepthWriteMask', D3D11_DEPTH_WRITE_MASK),
    ('DepthFunc', D3D11_COMPARISON_FUNC),
    ('StencilEnable', BOOL),
    ('StencilReadMask', UINT8),
    ('StencilWriteMask', UINT8),
    ('FrontFace', D3D11_DEPTH_STENCILOP_DESC),
    ('BackFace', D3D11_DEPTH_STENCILOP_DESC),
]

CD3D11_DEPTH_STENCIL_DESC = D3D11_DEPTH_STENCIL_DESC
 
 
IID_ID3D11DepthStencilState = MIDL_INTERFACE(
    "{03823EFB-8D8F-4E1C-9AA2-F64BB2CBFDF1}"
)
ID3D11DepthStencilState._iid_ = IID_ID3D11DepthStencilState


ID3D11DepthStencilState._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(D3D11_DEPTH_STENCIL_DESC), 'pDesc'),
    ),
]

class D3D11_BLEND(ENUM):
    D3D11_BLEND_ZERO = 1
    D3D11_BLEND_ONE = 2
    D3D11_BLEND_SRC_COLOR = 3
    D3D11_BLEND_INV_SRC_COLOR = 4
    D3D11_BLEND_SRC_ALPHA = 5
    D3D11_BLEND_INV_SRC_ALPHA = 6
    D3D11_BLEND_DEST_ALPHA = 7
    D3D11_BLEND_INV_DEST_ALPHA = 8
    D3D11_BLEND_DEST_COLOR = 9
    D3D11_BLEND_INV_DEST_COLOR = 10
    D3D11_BLEND_SRC_ALPHA_SAT = 11
    D3D11_BLEND_BLEND_FACTOR = 14
    D3D11_BLEND_INV_BLEND_FACTOR = 15
    D3D11_BLEND_SRC1_COLOR = 16
    D3D11_BLEND_INV_SRC1_COLOR = 17
    D3D11_BLEND_SRC1_ALPHA = 18
    D3D11_BLEND_INV_SRC1_ALPHA = 19


class D3D11_BLEND_OP(ENUM):
    D3D11_BLEND_OP_ADD = 1
    D3D11_BLEND_OP_SUBTRACT = 2
    D3D11_BLEND_OP_REV_SUBTRACT = 3
    D3D11_BLEND_OP_MIN = 4
    D3D11_BLEND_OP_MAX = 5


class D3D11_COLOR_WRITE_ENABLE(ENUM):
    D3D11_COLOR_WRITE_ENABLE_RED = 1
    D3D11_COLOR_WRITE_ENABLE_GREEN = 2
    D3D11_COLOR_WRITE_ENABLE_BLUE = 4
    D3D11_COLOR_WRITE_ENABLE_ALPHA = 8
    D3D11_COLOR_WRITE_ENABLE_ALL = (
        D3D11_COLOR_WRITE_ENABLE_RED |
        D3D11_COLOR_WRITE_ENABLE_GREEN  |
        D3D11_COLOR_WRITE_ENABLE_BLUE  |
        D3D11_COLOR_WRITE_ENABLE_ALPHA
    )
    
    
D3D11_RENDER_TARGET_BLEND_DESC._fields_ = [
    ('BlendEnable', BOOL),
    ('SrcBlend', D3D11_BLEND),
    ('DestBlend', D3D11_BLEND),
    ('BlendOp', D3D11_BLEND_OP),
    ('SrcBlendAlpha', D3D11_BLEND),
    ('DestBlendAlpha', D3D11_BLEND),
    ('BlendOpAlpha', D3D11_BLEND_OP),
    ('RenderTargetWriteMask', UINT8),
]
D3D11_BLEND_DESC._fields_ = [
    ('AlphaToCoverageEnable', BOOL),
    ('IndependentBlendEnable', BOOL),
    ('RenderTarget', D3D11_RENDER_TARGET_BLEND_DESC * 8),
]
# /* Note, the array size for RenderTarget[] above is
# D3D11_SIMULTANEOUS_RENDERTARGET_COUNT. IDL processing/generation of this
# header replaces the define; this comment is merely explaining what
# happened.

CD3D11_BLEND_DESC = D3D11_BLEND_DESC
     
IID_ID3D11BlendState = MIDL_INTERFACE(
    "{75B68FAA-347D-4159-8F45-A0640F01CD9A}"
)
ID3D11BlendState._iid_ = IID_ID3D11BlendState


ID3D11BlendState._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(D3D11_BLEND_DESC), 'pDesc'),
    ),
]

D3D11_RASTERIZER_DESC._fields_ = [
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
]
CD3D11_RASTERIZER_DESC = D3D11_RASTERIZER_DESC
   
IID_ID3D11RasterizerState = MIDL_INTERFACE(
    "{9BB4AB81-AB1A-4D8F-B506-FC04200B6EE7}"
)
ID3D11RasterizerState._iid_ = IID_ID3D11RasterizerState


ID3D11RasterizerState._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(D3D11_RASTERIZER_DESC), 'pDesc'),
    ),
]

d3d11 = ctypes.windll.D3D11

# }
# inline UINT D3D11CalcSubresource( UINT MipSlice, UINT ArraySlice, UINT MipLevels )
# { return MipSlice + ArraySlice * MipLevels; }
# extern "C"{
# #endif
# typedef struct D3D11_SUBRESOURCE_DATA
# {
# VOID *pSysMem;
# D3D11CalcSubresource = d3d11.D3D11CalcSubresource
# D3D11CalcSubresource.restype = UINT

     
IID_ID3D11Resource = MIDL_INTERFACE(
    "{DC8E63F3-D12B-4952-B47B-5E45026A862D}"
)
ID3D11Resource._iid_ = IID_ID3D11Resource


ID3D11Resource._methods_ = [
    COMMETHOD(
        [helpstring('Method GetType')],
        VOID,
        'GetType',
        (
            ['out'],
            POINTER(D3D11_RESOURCE_DIMENSION),
            'pResourceDimension'
        ),
    ),
    COMMETHOD(
        [helpstring('Method SetEvictionPriority')],
        VOID,
        'SetEvictionPriority',
        (['in'], UINT, 'EvictionPriority'),
    ),
    COMMETHOD(
        [helpstring('Method GetEvictionPriority')],
        UINT,
        'GetEvictionPriority',
    ),
]

D3D11_BUFFER_DESC._fields_ = [
    ('ByteWidth', UINT),
    ('Usage', D3D11_USAGE),
    ('BindFlags', UINT),
    ('CPUAccessFlags', UINT),
    ('MiscFlags', UINT),
    ('StructureByteStride', UINT),
]

CD3D11_BUFFER_DESC = D3D11_BUFFER_DESC
        
IID_ID3D11Buffer = MIDL_INTERFACE(
    "{48570B85-D1EE-4FCD-A250-EB350722B037}"
)
ID3D11Buffer._iid_ = IID_ID3D11Buffer


ID3D11Buffer._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(D3D11_BUFFER_DESC), 'pDesc'),
    ),
]


D3D11_TEXTURE1D_DESC._fields_ = [
    ('Width', UINT),
    ('MipLevels', UINT),
    ('ArraySize', UINT),
    ('Format', DXGI_FORMAT),
    ('Usage', D3D11_USAGE),
    ('BindFlags', UINT),
    ('CPUAccessFlags', UINT),
    ('MiscFlags', UINT),
]

CD3D11_TEXTURE1D_DESC = D3D11_TEXTURE1D_DESC

IID_ID3D11Texture1D = MIDL_INTERFACE(
    "{F8FB5C27-C6B3-4F75-A4C8-439AF2EF564C}"
)
ID3D11Texture1D._iid_ = IID_ID3D11Texture1D


ID3D11Texture1D._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(D3D11_TEXTURE1D_DESC), 'pDesc'),
    ),
]


D3D11_TEXTURE2D_DESC._fields_ = [
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
]

CD3D11_TEXTURE2D_DESC= D3D11_TEXTURE2D_DESC
       
   
IID_ID3D11Texture2D = MIDL_INTERFACE(
    "{6F15AAF2-D208-4E89-9AB4-489535D34F9C}"
)
ID3D11Texture2D._iid_ = IID_ID3D11Texture2D


ID3D11Texture2D._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(D3D11_TEXTURE2D_DESC), 'pDesc'),
    ),
]

D3D11_TEXTURE3D_DESC._fields_ = [
    ('Width', UINT),
    ('Height', UINT),
    ('Depth', UINT),
    ('MipLevels', UINT),
    ('Format', DXGI_FORMAT),
    ('Usage', D3D11_USAGE),
    ('BindFlags', UINT),
    ('CPUAccessFlags', UINT),
    ('MiscFlags', UINT),
]

CD3D11_TEXTURE3D_DESC = D3D11_TEXTURE3D_DESC
   
   
IID_ID3D11Texture3D = MIDL_INTERFACE(
    "{037E866E-F56D-4357-A8AF-9DABBE6E250E}"
)
ID3D11Texture3D._iid_ = IID_ID3D11Texture3D


ID3D11Texture3D._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(D3D11_TEXTURE3D_DESC), 'pDesc'),
    ),
]

class D3D11_TEXTURECUBE_FACE(ENUM):
    D3D11_TEXTURECUBE_FACE_POSITIVE_X = 0
    D3D11_TEXTURECUBE_FACE_NEGATIVE_X = 1
    D3D11_TEXTURECUBE_FACE_POSITIVE_Y = 2
    D3D11_TEXTURECUBE_FACE_NEGATIVE_Y = 3
    D3D11_TEXTURECUBE_FACE_POSITIVE_Z = 4
    D3D11_TEXTURECUBE_FACE_NEGATIVE_Z = 5


IID_ID3D11View = MIDL_INTERFACE(
    "{839D1216-BB2E-412B-B7F4-A9DBEBE08ED1}"
)
ID3D11View._iid_ = IID_ID3D11View


ID3D11View._methods_ = [
    COMMETHOD(
        [helpstring('Method GetResource')],
        VOID,
        'GetResource',
        (
            ['out'],
            POINTER(POINTER(ID3D11Resource)),
            'ppResource'
        ),
    ),
]

class _Union_1(ctypes.Union):
    pass


_Union_1._fields_ = [
    ('FirstElement', UINT),
    ('ElementOffset', UINT),
]
D3D11_BUFFER_SRV._Union_1 = _Union_1


class _Union_2(ctypes.Union):
    pass


_Union_2._fields_ = [
    ('NumElements', UINT),
    ('ElementWidth', UINT),
]
D3D11_BUFFER_SRV._Union_2 = _Union_2

D3D11_BUFFER_SRV._anonymous_ = (
    '_Union_1',
    '_Union_2',
)

D3D11_BUFFER_SRV._fields_ = [
    ('_Union_1', D3D11_BUFFER_SRV._Union_1),
    ('_Union_2', D3D11_BUFFER_SRV._Union_2),
]


class D3D11_BUFFEREX_SRV_FLAG(ENUM):
    D3D11_BUFFEREX_SRV_FLAG_RAW = 0x1

D3D11_BUFFEREX_SRV._fields_ = [
    ('FirstElement', UINT),
    ('NumElements', UINT),
    ('Flags', UINT),
]

D3D11_TEX1D_SRV._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
]

D3D11_TEX1D_ARRAY_SRV._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]

D3D11_TEX2D_SRV._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
]

D3D11_TEX2D_ARRAY_SRV._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]

D3D11_TEX3D_SRV._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
]

D3D11_TEXCUBE_SRV._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
]

D3D11_TEXCUBE_ARRAY_SRV._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
    ('First2DArrayFace', UINT),
    ('NumCubes', UINT),
]

D3D11_TEX2DMS_SRV._fields_ = [
    ('UnusedField_NothingToDefine', UINT),
]

D3D11_TEX2DMS_ARRAY_SRV._fields_ = [
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]


class _Union_3(ctypes.Union):
    pass


_Union_3._fields_ = [
    ('Buffer', D3D11_BUFFER_SRV),
    ('Texture1D', D3D11_TEX1D_SRV),
    ('Texture1DArray', D3D11_TEX1D_ARRAY_SRV),
    ('Texture2D', D3D11_TEX2D_SRV),
    ('Texture2DArray', D3D11_TEX2D_ARRAY_SRV),
    ('Texture2DMS', D3D11_TEX2DMS_SRV),
    ('Texture2DMSArray', D3D11_TEX2DMS_ARRAY_SRV),
    ('Texture3D', D3D11_TEX3D_SRV),
    ('TextureCube', D3D11_TEXCUBE_SRV),
    ('TextureCubeArray', D3D11_TEXCUBE_ARRAY_SRV),
    ('BufferEx', D3D11_BUFFEREX_SRV),
]
D3D11_SHADER_RESOURCE_VIEW_DESC._Union_3 = _Union_3

D3D11_SHADER_RESOURCE_VIEW_DESC._anonymous_ = (
    '_Union_3',
)

D3D11_SHADER_RESOURCE_VIEW_DESC._fields_ = [
    ('Format', DXGI_FORMAT),
    ('ViewDimension', D3D11_SRV_DIMENSION),
    ('_Union_3', D3D11_SHADER_RESOURCE_VIEW_DESC._Union_3),
]

CD3D11_SHADER_RESOURCE_VIEW_DESC = D3D11_SHADER_RESOURCE_VIEW_DESC
     
IID_ID3D11ShaderResourceView = MIDL_INTERFACE(
    "{B0E06FE0-8192-4E1A-B1CA-36D7414710B2}"
)
ID3D11ShaderResourceView._iid_ = IID_ID3D11ShaderResourceView


ID3D11ShaderResourceView._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (
            ['out'],
            POINTER(D3D11_SHADER_RESOURCE_VIEW_DESC),
            'pDesc'
        ),
    ),
]

    # END IF  C style interface
# END IF  __ID3D11ShaderResourceView_INTERFACE_DEFINED__

# interface __MIDL_itf_d3d11_0000_0011
# [local]
class _Union_4(ctypes.Union):
    pass


_Union_4._fields_ = [
    ('FirstElement', UINT),
    ('ElementOffset', UINT),
]
D3D11_BUFFER_RTV._Union_4 = _Union_4


class _Union_5(ctypes.Union):
    pass


_Union_5._fields_ = [
    ('NumElements', UINT),
    ('ElementWidth', UINT),
]
D3D11_BUFFER_RTV._Union_5 = _Union_5

D3D11_BUFFER_RTV._anonymous_ = (
    '_Union_4',
    '_Union_5',
)

D3D11_BUFFER_RTV._fields_ = [
    ('_Union_4', D3D11_BUFFER_RTV._Union_4),
    ('_Union_5', D3D11_BUFFER_RTV._Union_5),
]

D3D11_TEX1D_RTV._fields_ = [
    ('MipSlice', UINT),
]

D3D11_TEX1D_ARRAY_RTV._fields_ = [
    ('MipSlice', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]

D3D11_TEX2D_RTV._fields_ = [
    ('MipSlice', UINT),
]

D3D11_TEX2DMS_RTV._fields_ = [
    ('UnusedField_NothingToDefine', UINT),
]

D3D11_TEX2D_ARRAY_RTV._fields_ = [
    ('MipSlice', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]

D3D11_TEX2DMS_ARRAY_RTV._fields_ = [
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]

D3D11_TEX3D_RTV._fields_ = [
    ('MipSlice', UINT),
    ('FirstWSlice', UINT),
    ('WSize', UINT),
]


class _Union_6(ctypes.Union):
    pass


_Union_6._fields_ = [
    ('Buffer', D3D11_BUFFER_RTV),
    ('Texture1D', D3D11_TEX1D_RTV),
    ('Texture1DArray', D3D11_TEX1D_ARRAY_RTV),
    ('Texture2D', D3D11_TEX2D_RTV),
    ('Texture2DArray', D3D11_TEX2D_ARRAY_RTV),
    ('Texture2DMS', D3D11_TEX2DMS_RTV),
    ('Texture2DMSArray', D3D11_TEX2DMS_ARRAY_RTV),
    ('Texture3D', D3D11_TEX3D_RTV),
]
D3D11_RENDER_TARGET_VIEW_DESC._Union_6 = _Union_6

D3D11_RENDER_TARGET_VIEW_DESC._anonymous_ = (
    '_Union_6',
)

D3D11_RENDER_TARGET_VIEW_DESC._fields_ = [
    ('Format', DXGI_FORMAT),
    ('ViewDimension', D3D11_RTV_DIMENSION),
    ('_Union_6', D3D11_RENDER_TARGET_VIEW_DESC._Union_6),
]

CD3D11_RENDER_TARGET_VIEW_DESC = D3D11_RENDER_TARGET_VIEW_DESC
       
   
IID_ID3D11RenderTargetView = MIDL_INTERFACE(
    "{DFDBA067-0B8D-4865-875B-D7B4516CC164}"
)
ID3D11RenderTargetView._iid_ = IID_ID3D11RenderTargetView


ID3D11RenderTargetView._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (
            ['out'],
            POINTER(D3D11_RENDER_TARGET_VIEW_DESC),
            'pDesc'
        ),
    ),
]
CD3D11_VIEWPORT = D3D11_VIEWPORT

D3D11_TEX1D_DSV._fields_ = [
    ('MipSlice', UINT),
]
D3D11_TEX1D_ARRAY_DSV._fields_ = [
    ('MipSlice', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]
D3D11_TEX2D_DSV._fields_ = [
    ('MipSlice', UINT),
]
D3D11_TEX2D_ARRAY_DSV._fields_ = [
    ('MipSlice', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]
D3D11_TEX2DMS_DSV._fields_ = [
    ('UnusedField_NothingToDefine', UINT),
]
D3D11_TEX2DMS_ARRAY_DSV._fields_ = [
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]


class D3D11_DSV_FLAG(ENUM):
    D3D11_DSV_READ_ONLY_DEPTH = 0x1
    D3D11_DSV_READ_ONLY_STENCIL = 0x2


class _Union_7(ctypes.Union):
    pass


_Union_7._fields_ = [
    ('Texture1D', D3D11_TEX1D_DSV),
    ('Texture1DArray', D3D11_TEX1D_ARRAY_DSV),
    ('Texture2D', D3D11_TEX2D_DSV),
    ('Texture2DArray', D3D11_TEX2D_ARRAY_DSV),
    ('Texture2DMS', D3D11_TEX2DMS_DSV),
    ('Texture2DMSArray', D3D11_TEX2DMS_ARRAY_DSV),
]
D3D11_DEPTH_STENCIL_VIEW_DESC._Union_7 = _Union_7

D3D11_DEPTH_STENCIL_VIEW_DESC._anonymous_ = (
    '_Union_7',
)

D3D11_DEPTH_STENCIL_VIEW_DESC._fields_ = [
    ('Format', DXGI_FORMAT),
    ('ViewDimension', D3D11_DSV_DIMENSION),
    ('Flags', UINT),
    ('_Union_7', D3D11_DEPTH_STENCIL_VIEW_DESC._Union_7),
]

CD3D11_DEPTH_STENCIL_VIEW_DESC = D3D11_DEPTH_STENCIL_VIEW_DESC

IID_ID3D11DepthStencilView = MIDL_INTERFACE(
    "{9FDAC92A-1876-48C3-AFAD-25B94F84A9B6}"
)
ID3D11DepthStencilView._iid_ = IID_ID3D11DepthStencilView


ID3D11DepthStencilView._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (
            ['out'],
            POINTER(D3D11_DEPTH_STENCIL_VIEW_DESC),
            'pDesc'
        ),
    ),
]

class D3D11_BUFFER_UAV_FLAG(ENUM):
    D3D11_BUFFER_UAV_FLAG_RAW = 0x1
    D3D11_BUFFER_UAV_FLAG_APPEND = 0x2
    D3D11_BUFFER_UAV_FLAG_COUNTER = 0x4

D3D11_BUFFER_UAV._fields_ = [
    ('FirstElement', UINT),
    ('NumElements', UINT),
    ('Flags', UINT),
]

D3D11_TEX1D_UAV._fields_ = [
    ('MipSlice', UINT),
]

D3D11_TEX1D_ARRAY_UAV._fields_ = [
    ('MipSlice', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]

D3D11_TEX2D_UAV._fields_ = [
    ('MipSlice', UINT),
]

D3D11_TEX2D_ARRAY_UAV._fields_ = [
    ('MipSlice', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]

D3D11_TEX3D_UAV._fields_ = [
    ('MipSlice', UINT),
    ('FirstWSlice', UINT),
    ('WSize', UINT),
]


class _Union_8(ctypes.Union):
    pass


_Union_8._fields_ = [
    ('Buffer', D3D11_BUFFER_UAV),
    ('Texture1D', D3D11_TEX1D_UAV),
    ('Texture1DArray', D3D11_TEX1D_ARRAY_UAV),
    ('Texture2D', D3D11_TEX2D_UAV),
    ('Texture2DArray', D3D11_TEX2D_ARRAY_UAV),
    ('Texture3D', D3D11_TEX3D_UAV),
]
D3D11_UNORDERED_ACCESS_VIEW_DESC._Union_8 = _Union_8

D3D11_UNORDERED_ACCESS_VIEW_DESC._anonymous_ = (
    '_Union_8',
)

D3D11_UNORDERED_ACCESS_VIEW_DESC._fields_ = [
    ('Format', DXGI_FORMAT),
    ('ViewDimension', D3D11_UAV_DIMENSION),
    ('_Union_8', D3D11_UNORDERED_ACCESS_VIEW_DESC._Union_8),
]

CD3D11_UNORDERED_ACCESS_VIEW_DESC = D3D11_UNORDERED_ACCESS_VIEW_DESC


IID_ID3D11UnorderedAccessView = MIDL_INTERFACE(
    "{28ACF509-7F5C-48F6-8611-F316010A6380}"
)
ID3D11UnorderedAccessView._iid_ = IID_ID3D11UnorderedAccessView


ID3D11UnorderedAccessView._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (
            ['out'],
            POINTER(D3D11_UNORDERED_ACCESS_VIEW_DESC),
            'pDesc'
        ),
    ),
]

IID_ID3D11VertexShader = MIDL_INTERFACE(
    "{3B301D64-D678-4289-8897-22F8928B72F3}"
)
ID3D11VertexShader._iid_ = IID_ID3D11VertexShader


ID3D11VertexShader._methods_ = []


IID_ID3D11HullShader = MIDL_INTERFACE(
    "{8E5C6061-628A-4C8E-8264-BBE45CB3D5DD}"
)
ID3D11HullShader._iid_ = IID_ID3D11HullShader


ID3D11HullShader._methods_ = []

IID_ID3D11DomainShader = MIDL_INTERFACE(
    "{F582C508-0F36-490C-9977-31EECE268CFA}"
)
ID3D11DomainShader._iid_ = IID_ID3D11DomainShader


ID3D11DomainShader._methods_ = []


IID_ID3D11GeometryShader = MIDL_INTERFACE(
    "{38325B96-EFFB-4022-BA02-2E795B70275C}"
)
ID3D11GeometryShader._iid_ = IID_ID3D11GeometryShader


ID3D11GeometryShader._methods_ = []


IID_ID3D11PixelShader = MIDL_INTERFACE(
    "{EA82E40D-51DC-4F33-93D4-DB7C9125AE8C}"
)
ID3D11PixelShader._iid_ = IID_ID3D11PixelShader


ID3D11PixelShader._methods_ = []

IID_ID3D11ComputeShader = MIDL_INTERFACE(
    "{4F5B196E-C2BD-495E-BD01-1FDED38E4969}"
)
ID3D11ComputeShader._iid_ = IID_ID3D11ComputeShader


ID3D11ComputeShader._methods_ = []


IID_ID3D11InputLayout = MIDL_INTERFACE(
    "{E4819DDC-4CF0-4025-BD26-5DE82A3E07B7}"
)
ID3D11InputLayout._iid_ = IID_ID3D11InputLayout


ID3D11InputLayout._methods_ = []


class D3D11_FILTER(ENUM):
    D3D11_FILTER_MIN_MAG_MIP_POINT = 0
    D3D11_FILTER_MIN_MAG_POINT_MIP_LINEAR = 0x1
    D3D11_FILTER_MIN_POINT_MAG_LINEAR_MIP_POINT = 0x4
    D3D11_FILTER_MIN_POINT_MAG_MIP_LINEAR = 0x5
    D3D11_FILTER_MIN_LINEAR_MAG_MIP_POINT = 0x10
    D3D11_FILTER_MIN_LINEAR_MAG_POINT_MIP_LINEAR = 0x11
    D3D11_FILTER_MIN_MAG_LINEAR_MIP_POINT = 0x14
    D3D11_FILTER_MIN_MAG_MIP_LINEAR = 0x15
    D3D11_FILTER_ANISOTROPIC = 0x55
    D3D11_FILTER_COMPARISON_MIN_MAG_MIP_POINT = 0x80
    D3D11_FILTER_COMPARISON_MIN_MAG_POINT_MIP_LINEAR = 0x81
    D3D11_FILTER_COMPARISON_MIN_POINT_MAG_LINEAR_MIP_POINT = 0x84
    D3D11_FILTER_COMPARISON_MIN_POINT_MAG_MIP_LINEAR = 0x85
    D3D11_FILTER_COMPARISON_MIN_LINEAR_MAG_MIP_POINT = 0x90
    D3D11_FILTER_COMPARISON_MIN_LINEAR_MAG_POINT_MIP_LINEAR = 0x91
    D3D11_FILTER_COMPARISON_MIN_MAG_LINEAR_MIP_POINT = 0x94
    D3D11_FILTER_COMPARISON_MIN_MAG_MIP_LINEAR = 0x95
    D3D11_FILTER_COMPARISON_ANISOTROPIC = 0xD5
    D3D11_FILTER_MINIMUM_MIN_MAG_MIP_POINT = 0x100
    D3D11_FILTER_MINIMUM_MIN_MAG_POINT_MIP_LINEAR = 0x101
    D3D11_FILTER_MINIMUM_MIN_POINT_MAG_LINEAR_MIP_POINT = 0x104
    D3D11_FILTER_MINIMUM_MIN_POINT_MAG_MIP_LINEAR = 0x105
    D3D11_FILTER_MINIMUM_MIN_LINEAR_MAG_MIP_POINT = 0x110
    D3D11_FILTER_MINIMUM_MIN_LINEAR_MAG_POINT_MIP_LINEAR = 0x111
    D3D11_FILTER_MINIMUM_MIN_MAG_LINEAR_MIP_POINT = 0x114
    D3D11_FILTER_MINIMUM_MIN_MAG_MIP_LINEAR = 0x115
    D3D11_FILTER_MINIMUM_ANISOTROPIC = 0x155
    D3D11_FILTER_MAXIMUM_MIN_MAG_MIP_POINT = 0x180
    D3D11_FILTER_MAXIMUM_MIN_MAG_POINT_MIP_LINEAR = 0x181
    D3D11_FILTER_MAXIMUM_MIN_POINT_MAG_LINEAR_MIP_POINT = 0x184
    D3D11_FILTER_MAXIMUM_MIN_POINT_MAG_MIP_LINEAR = 0x185
    D3D11_FILTER_MAXIMUM_MIN_LINEAR_MAG_MIP_POINT = 0x190
    D3D11_FILTER_MAXIMUM_MIN_LINEAR_MAG_POINT_MIP_LINEAR = 0x191
    D3D11_FILTER_MAXIMUM_MIN_MAG_LINEAR_MIP_POINT = 0x194
    D3D11_FILTER_MAXIMUM_MIN_MAG_MIP_LINEAR = 0x195
    D3D11_FILTER_MAXIMUM_ANISOTROPIC = 0x1D5


class D3D11_FILTER_TYPE(ENUM):
    D3D11_FILTER_TYPE_POINT = 0
    D3D11_FILTER_TYPE_LINEAR = 1


class D3D11_FILTER_REDUCTION_TYPE(ENUM):
    D3D11_FILTER_REDUCTION_TYPE_STANDARD = 0
    D3D11_FILTER_REDUCTION_TYPE_COMPARISON = 1
    D3D11_FILTER_REDUCTION_TYPE_MINIMUM = 2
    D3D11_FILTER_REDUCTION_TYPE_MAXIMUM = 3

# D3D11_COMPARISON_FILTERING_BIT is no longer used / meaningless. The
# D3D11_FILTER_REDUCTION_TYPE enum replaced it.
# Old code that uses D3D11_COMPARISON_FILTERING_BIT and would never
# use D3D11_FILTER_MINIMUM_* or D3D11_FILTER_MAXIMUM_*
# will still work fine though, so the define is left to aVOID breaks.
class D3D11_TEXTURE_ADDRESS_MODE(ENUM):
    D3D11_TEXTURE_ADDRESS_WRAP = 1
    D3D11_TEXTURE_ADDRESS_MIRROR = 2
    D3D11_TEXTURE_ADDRESS_CLAMP = 3
    D3D11_TEXTURE_ADDRESS_BORDER = 4
    D3D11_TEXTURE_ADDRESS_MIRROR_ONCE = 5

D3D11_SAMPLER_DESC._fields_ = [
    ('Filter', D3D11_FILTER),
    ('AddressU', D3D11_TEXTURE_ADDRESS_MODE),
    ('AddressV', D3D11_TEXTURE_ADDRESS_MODE),
    ('AddressW', D3D11_TEXTURE_ADDRESS_MODE),
    ('MipLODBias', FLOAT),
    ('MaxAnisotropy', UINT),
    ('ComparisonFunc', D3D11_COMPARISON_FUNC),
    ('BorderColor', FLOAT * 4),
    ('MinLOD', FLOAT),
    ('MaxLOD', FLOAT),
]

CD3D11_SAMPLER_DESC = D3D11_SAMPLER_DESC


IID_ID3D11SamplerState = MIDL_INTERFACE(
    "{DA6FEA51-564C-4487-9810-F0D0F9B4E3A5}"
)
ID3D11SamplerState._iid_ = IID_ID3D11SamplerState


ID3D11SamplerState._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(D3D11_SAMPLER_DESC), 'pDesc'),
    ),
]

class D3D11_FORMAT_SUPPORT(ENUM):
    D3D11_FORMAT_SUPPORT_BUFFER = 0x1
    D3D11_FORMAT_SUPPORT_IA_VERTEX_BUFFER = 0x2
    D3D11_FORMAT_SUPPORT_IA_INDEX_BUFFER = 0x4
    D3D11_FORMAT_SUPPORT_SO_BUFFER = 0x8
    D3D11_FORMAT_SUPPORT_TEXTURE1D = 0x10
    D3D11_FORMAT_SUPPORT_TEXTURE2D = 0x20
    D3D11_FORMAT_SUPPORT_TEXTURE3D = 0x40
    D3D11_FORMAT_SUPPORT_TEXTURECUBE = 0x80
    D3D11_FORMAT_SUPPORT_SHADER_LOAD = 0x100
    D3D11_FORMAT_SUPPORT_SHADER_SAMPLE = 0x200
    D3D11_FORMAT_SUPPORT_SHADER_SAMPLE_COMPARISON = 0x400
    D3D11_FORMAT_SUPPORT_SHADER_SAMPLE_MONO_TEXT = 0x800
    D3D11_FORMAT_SUPPORT_MIP = 0x1000
    D3D11_FORMAT_SUPPORT_MIP_AUTOGEN = 0x2000
    D3D11_FORMAT_SUPPORT_RENDER_TARGET = 0x4000
    D3D11_FORMAT_SUPPORT_BLENDABLE = 0x8000
    D3D11_FORMAT_SUPPORT_DEPTH_STENCIL = 0x10000
    D3D11_FORMAT_SUPPORT_CPU_LOCKABLE = 0x20000
    D3D11_FORMAT_SUPPORT_MULTISAMPLE_RESOLVE = 0x40000
    D3D11_FORMAT_SUPPORT_DISPLAY = 0x80000
    D3D11_FORMAT_SUPPORT_CAST_WITHIN_BIT_LAYOUT = 0x100000
    D3D11_FORMAT_SUPPORT_MULTISAMPLE_RENDERTARGET = 0x200000
    D3D11_FORMAT_SUPPORT_MULTISAMPLE_LOAD = 0x400000
    D3D11_FORMAT_SUPPORT_SHADER_GATHER = 0x800000
    D3D11_FORMAT_SUPPORT_BACK_BUFFER_CAST = 0x1000000
    D3D11_FORMAT_SUPPORT_TYPED_UNORDERED_ACCESS_VIEW = 0x2000000
    D3D11_FORMAT_SUPPORT_SHADER_GATHER_COMPARISON = 0x4000000
    D3D11_FORMAT_SUPPORT_DECODER_OUTPUT = 0x8000000
    D3D11_FORMAT_SUPPORT_VIDEO_PROCESSOR_OUTPUT = 0x10000000
    D3D11_FORMAT_SUPPORT_VIDEO_PROCESSOR_INPUT = 0x20000000
    D3D11_FORMAT_SUPPORT_VIDEO_ENCODER = 0x40000000


class D3D11_FORMAT_SUPPORT2(ENUM):
    D3D11_FORMAT_SUPPORT2_UAV_ATOMIC_ADD = 0x1
    D3D11_FORMAT_SUPPORT2_UAV_ATOMIC_BITWISE_OPS = 0x2
    D3D11_FORMAT_SUPPORT2_UAV_ATOMIC_COMPARE_STORE_OR_COMPARE_EXCHANGE = (
        0x4
    )
    D3D11_FORMAT_SUPPORT2_UAV_ATOMIC_EXCHANGE = 0x8
    D3D11_FORMAT_SUPPORT2_UAV_ATOMIC_SIGNED_MIN_OR_MAX = 0x10
    D3D11_FORMAT_SUPPORT2_UAV_ATOMIC_UNSIGNED_MIN_OR_MAX = 0x20
    D3D11_FORMAT_SUPPORT2_UAV_TYPED_LOAD = 0x40
    D3D11_FORMAT_SUPPORT2_UAV_TYPED_STORE = 0x80
    D3D11_FORMAT_SUPPORT2_OUTPUT_MERGER_LOGIC_OP = 0x100
    D3D11_FORMAT_SUPPORT2_TILED = 0x200
    D3D11_FORMAT_SUPPORT2_SHAREABLE = 0x400
    D3D11_FORMAT_SUPPORT2_MULTIPLANE_OVERLAY = 0x4000

IID_ID3D11Asynchronous = MIDL_INTERFACE(
    "{4B35D0CD-1E15-4258-9C98-1B1333F6DD3B}"
)
ID3D11Asynchronous._iid_ = IID_ID3D11Asynchronous


ID3D11Asynchronous._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDataSize')],
        UINT,
        'GetDataSize',
    ),
]

class D3D11_ASYNC_GETDATA_FLAG(ENUM):
    D3D11_ASYNC_GETDATA_DONOTFLUSH = 0x1


class D3D11_QUERY(ENUM):
    D3D11_QUERY_EVENT = 0
    D3D11_QUERY_OCCLUSION = D3D11_QUERY_EVENT + 1
    D3D11_QUERY_TIMESTAMP = D3D11_QUERY_OCCLUSION + 1
    D3D11_QUERY_TIMESTAMP_DISJOINT = D3D11_QUERY_TIMESTAMP + 1
    D3D11_QUERY_PIPELINE_STATISTICS = (
        D3D11_QUERY_TIMESTAMP_DISJOINT + 1
    )
    D3D11_QUERY_OCCLUSION_PREDICATE = (
        D3D11_QUERY_PIPELINE_STATISTICS + 1
    )
    D3D11_QUERY_SO_STATISTICS = D3D11_QUERY_OCCLUSION_PREDICATE + 1
    D3D11_QUERY_SO_OVERFLOW_PREDICATE = D3D11_QUERY_SO_STATISTICS + 1
    D3D11_QUERY_SO_STATISTICS_STREAM0 = (
        D3D11_QUERY_SO_OVERFLOW_PREDICATE + 1
    )
    D3D11_QUERY_SO_OVERFLOW_PREDICATE_STREAM0 = (
        D3D11_QUERY_SO_STATISTICS_STREAM0 + 1
    )
    D3D11_QUERY_SO_STATISTICS_STREAM1 = (
        D3D11_QUERY_SO_OVERFLOW_PREDICATE_STREAM0 + 1
    )
    D3D11_QUERY_SO_OVERFLOW_PREDICATE_STREAM1 = (
        D3D11_QUERY_SO_STATISTICS_STREAM1 + 1
    )
    D3D11_QUERY_SO_STATISTICS_STREAM2 = (
        D3D11_QUERY_SO_OVERFLOW_PREDICATE_STREAM1 + 1
    )
    D3D11_QUERY_SO_OVERFLOW_PREDICATE_STREAM2 = (
        D3D11_QUERY_SO_STATISTICS_STREAM2 + 1
    )
    D3D11_QUERY_SO_STATISTICS_STREAM3 = (
        D3D11_QUERY_SO_OVERFLOW_PREDICATE_STREAM2 + 1
    )
    D3D11_QUERY_SO_OVERFLOW_PREDICATE_STREAM3 = (
        D3D11_QUERY_SO_STATISTICS_STREAM3 + 1
    )


class D3D11_QUERY_MISC_FLAG(ENUM):
    D3D11_QUERY_MISC_PREDICATEHINT = 0x1

D3D11_QUERY_DESC._fields_ = [
    ('Query', D3D11_QUERY),
    ('MiscFlags', UINT),
]

CD3D11_QUERY_DESC = D3D11_QUERY_DESC
       
       
IID_ID3D11Query = MIDL_INTERFACE(
    "{D6C00747-87B7-425E-B84D-44D108560AFD}"
)
ID3D11Query._iid_ = IID_ID3D11Query


ID3D11Query._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(D3D11_QUERY_DESC), 'pDesc'),
    ),
]

IID_ID3D11Predicate = MIDL_INTERFACE(
    "{9EB576DD-9F77-4D86-81AA-8BAB5FE490E2}"
)
ID3D11Predicate._iid_ = IID_ID3D11Predicate


ID3D11Predicate._methods_ = []


D3D11_QUERY_DATA_TIMESTAMP_DISJOINT._fields_ = [
    ('Frequency', UINT64),
    ('Disjoint', BOOL),
]

D3D11_QUERY_DATA_PIPELINE_STATISTICS._fields_ = [
    ('IAVertices', UINT64),
    ('IAPrimitives', UINT64),
    ('VSInvocations', UINT64),
    ('GSInvocations', UINT64),
    ('GSPrimitives', UINT64),
    ('CInvocations', UINT64),
    ('CPrimitives', UINT64),
    ('PSInvocations', UINT64),
    ('HSInvocations', UINT64),
    ('DSInvocations', UINT64),
    ('CSInvocations', UINT64),
]

D3D11_QUERY_DATA_SO_STATISTICS._fields_ = [
    ('NumPrimitivesWritten', UINT64),
    ('PrimitivesStorageNeeded', UINT64),
]


class D3D11_COUNTER(ENUM):
    D3D11_COUNTER_DEVICE_DEPENDENT_0 = 0x40000000


class D3D11_COUNTER_TYPE(ENUM):
    D3D11_COUNTER_TYPE_FLOAT32 = 0
    D3D11_COUNTER_TYPE_UINT16 = D3D11_COUNTER_TYPE_FLOAT32 + 1
    D3D11_COUNTER_TYPE_UINT32 = D3D11_COUNTER_TYPE_UINT16 + 1
    D3D11_COUNTER_TYPE_UINT64 = D3D11_COUNTER_TYPE_UINT32 + 1

D3D11_COUNTER_DESC._fields_ = [
    ('Counter', D3D11_COUNTER),
    ('MiscFlags', UINT),
]

CD3D11_COUNTER_DESC = D3D11_COUNTER_DESC

D3D11_COUNTER_INFO._fields_ = [
    ('LastDeviceDependentCounter', D3D11_COUNTER),
    ('NumSimultaneousCounters', UINT),
    ('NumDetectableParallelUnits', UINT8),
]


IID_ID3D11Counter = MIDL_INTERFACE(
    "{6E8C49FB-A371-4770-B440-29086022B741}"
)
ID3D11Counter._iid_ = IID_ID3D11Counter


ID3D11Counter._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(D3D11_COUNTER_DESC), 'pDesc'),
    ),
]

class D3D11_STANDARD_MULTISAMPLE_QUALITY_LEVELS(ENUM):
    D3D11_STANDARD_MULTISAMPLE_PATTERN = 0xFFFFFFFF
    D3D11_CENTER_MULTISAMPLE_PATTERN = 0xFFFFFFFE


class D3D11_DEVICE_CONTEXT_TYPE(ENUM):
    D3D11_DEVICE_CONTEXT_IMMEDIATE = 0
    D3D11_DEVICE_CONTEXT_DEFERRED = D3D11_DEVICE_CONTEXT_IMMEDIATE + 1

D3D11_CLASS_INSTANCE_DESC._fields_ = [
    ('InstanceId', UINT),
    ('InstanceIndex', UINT),
    ('TypeId', UINT),
    ('ConstantBuffer', UINT),
    ('BaseConstantBufferOffset', UINT),
    ('BaseTexture', UINT),
    ('BaseSampler', UINT),
    ('Created', BOOL),
]


IID_ID3D11ClassInstance = MIDL_INTERFACE(
    "{A6CD7FAA-B0B7-4A2F-9436-8662A65797CB}"
)
ID3D11ClassInstance._iid_ = IID_ID3D11ClassInstance


ID3D11ClassInstance._methods_ = [
    COMMETHOD(
        [helpstring('Method GetClassLinkage')],
        VOID,
        'GetClassLinkage',
        (
            ['out'],
            POINTER(POINTER(ID3D11ClassLinkage)),
            'ppLinkage'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (
            ['out'],
            POINTER(D3D11_CLASS_INSTANCE_DESC),
            'pDesc'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetInstanceName')],
        VOID,
        'GetInstanceName',
        (['out'], LPSTR, 'pInstanceName'),
        (['out', 'in'], POINTER(SIZE_T), 'pBufferLength'),
    ),
    COMMETHOD(
        [helpstring('Method GetTypeName')],
        VOID,
        'GetTypeName',
        (['out'], LPSTR, 'pTypeName'),
        (['out', 'in'], POINTER(SIZE_T), 'pBufferLength'),
    ),
]


IID_ID3D11ClassLinkage = MIDL_INTERFACE(
    "{DDF57CBA-9543-46E4-A12B-F207A0FE7FED}"
)
ID3D11ClassLinkage._iid_ = IID_ID3D11ClassLinkage


ID3D11ClassLinkage._methods_ = [
    COMMETHOD(
        [helpstring('Method GetClassInstance')],
        HRESULT,
        'GetClassInstance',
        (['in'], LPCSTR, 'pClassInstanceName'),
        (['in'], UINT, 'InstanceIndex'),
        (
            ['out'],
            POINTER(POINTER(ID3D11ClassInstance)),
            'ppInstance'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateClassInstance')],
        HRESULT,
        'CreateClassInstance',
        (['in'], LPCSTR, 'pClassTypeName'),
        (['in'], UINT, 'ConstantBufferOffset'),
        (['in'], UINT, 'ConstantVectorOffset'),
        (['in'], UINT, 'TextureOffset'),
        (['in'], UINT, 'SamplerOffset'),
        (
            ['out'],
            POINTER(POINTER(ID3D11ClassInstance)),
            'ppInstance'
        ),
    ),
]

IID_ID3D11CommandList = MIDL_INTERFACE(
    "{A24BC4D1-769E-43F7-8013-98FF566C18E2}"
)
ID3D11CommandList._iid_ = IID_ID3D11CommandList


ID3D11CommandList._methods_ = [
    COMMETHOD(
        [helpstring('Method GetContextFlags')],
        UINT,
        'GetContextFlags',
    ),
]


class D3D11_FEATURE(ENUM):
    D3D11_FEATURE_THREADING = 0
    D3D11_FEATURE_DOUBLES = D3D11_FEATURE_THREADING + 1
    D3D11_FEATURE_FORMAT_SUPPORT = D3D11_FEATURE_DOUBLES + 1
    D3D11_FEATURE_FORMAT_SUPPORT2 = D3D11_FEATURE_FORMAT_SUPPORT + 1
    D3D11_FEATURE_D3D10_X_HARDWARE_OPTIONS = (
        D3D11_FEATURE_FORMAT_SUPPORT2 + 1
    )
    D3D11_FEATURE_D3D11_OPTIONS = (
        D3D11_FEATURE_D3D10_X_HARDWARE_OPTIONS + 1
    )
    D3D11_FEATURE_ARCHITECTURE_INFO = D3D11_FEATURE_D3D11_OPTIONS + 1
    D3D11_FEATURE_D3D9_OPTIONS = D3D11_FEATURE_ARCHITECTURE_INFO + 1
    D3D11_FEATURE_SHADER_MIN_PRECISION_SUPPORT = (
        D3D11_FEATURE_D3D9_OPTIONS + 1
    )
    D3D11_FEATURE_D3D9_SHADOW_SUPPORT = (
        D3D11_FEATURE_SHADER_MIN_PRECISION_SUPPORT + 1
    )
    D3D11_FEATURE_D3D11_OPTIONS1 = (
        D3D11_FEATURE_D3D9_SHADOW_SUPPORT + 1
    )
    D3D11_FEATURE_D3D9_SIMPLE_INSTANCING_SUPPORT = (
        D3D11_FEATURE_D3D11_OPTIONS1 + 1
    )
    D3D11_FEATURE_MARKER_SUPPORT = (
        D3D11_FEATURE_D3D9_SIMPLE_INSTANCING_SUPPORT + 1
    )
    D3D11_FEATURE_D3D9_OPTIONS1 = D3D11_FEATURE_MARKER_SUPPORT + 1
    D3D11_FEATURE_D3D11_OPTIONS2 = D3D11_FEATURE_D3D9_OPTIONS1 + 1
    D3D11_FEATURE_D3D11_OPTIONS3 = D3D11_FEATURE_D3D11_OPTIONS2 + 1
    D3D11_FEATURE_GPU_VIRTUAL_ADDRESS_SUPPORT = (
        D3D11_FEATURE_D3D11_OPTIONS3 + 1
    )
    D3D11_FEATURE_D3D11_OPTIONS4 = (
        D3D11_FEATURE_GPU_VIRTUAL_ADDRESS_SUPPORT + 1
    )
    D3D11_FEATURE_SHADER_CACHE = D3D11_FEATURE_D3D11_OPTIONS4 + 1
    D3D11_FEATURE_D3D11_OPTIONS5 = D3D11_FEATURE_SHADER_CACHE + 1

D3D11_FEATURE_DATA_THREADING._fields_ = [
    ('DriverConcurrentCreates', BOOL),
    ('DriverCommandLists', BOOL),
]

D3D11_FEATURE_DATA_DOUBLES._fields_ = [
    ('DoublePrecisionFloatShaderOps', BOOL),
]

D3D11_FEATURE_DATA_FORMAT_SUPPORT._fields_ = [
    ('InFormat', DXGI_FORMAT),
    ('OutFormatSupport', UINT),
]

D3D11_FEATURE_DATA_FORMAT_SUPPORT2._fields_ = [
    ('InFormat', DXGI_FORMAT),
    ('OutFormatSupport2', UINT),
]

D3D11_FEATURE_DATA_D3D10_X_HARDWARE_OPTIONS._fields_ = [
    ('ComputeShaders_Plus_RawAndStructuredBuffers_Via_Shader_4_x', BOOL),
]

# == == == == == == == == == == == == == == == == == == == == == == ==
# == == == == == == == == == == == == == == == =
# In the D3D11_FEATURE_DATA_D3D11_OPTIONS struct below,
# the following groupings of capabilities will always be set
# identically.
# That is, all the BOOLs in a grouping will be TRUE or FALSE together.
# Group: DiscardAPIsSeenByDriver, FlagsForUpdateAndCopySeenByDriver
# Group: ClearView, CopyWithOverlap, ConstantBufferPartialUpdate
# ConstantBufferOffsetting, MapNoOverwriteOnDynamicConstantBuffer
# Group: MapNoOverwriteOnDynamicBufferSRV,
# MultisampleRTVWithForcedSampleCountOne
D3D11_FEATURE_DATA_D3D11_OPTIONS._fields_ = [
    ('OutputMergerLogicOp', BOOL),
    ('UAVOnlyRenderingForcedSampleCount', BOOL),
    ('DiscardAPIsSeenByDriver', BOOL),
    ('FlagsForUpdateAndCopySeenByDriver', BOOL),
    ('ClearView', BOOL),
    ('CopyWithOverlap', BOOL),
    ('ConstantBufferPartialUpdate', BOOL),
    ('ConstantBufferOffsetting', BOOL),
    ('MapNoOverwriteOnDynamicConstantBuffer', BOOL),
    ('MapNoOverwriteOnDynamicBufferSRV', BOOL),
    ('MultisampleRTVWithForcedSampleCountOne', BOOL),
    ('SAD4ShaderInstructions', BOOL),
    ('ExtendedDoublesShaderInstructions', BOOL),
    ('ExtendedResourceSharing', BOOL),
]

D3D11_FEATURE_DATA_ARCHITECTURE_INFO._fields_ = [
    ('TileBasedDeferredRenderer', BOOL),
]

D3D11_FEATURE_DATA_D3D9_OPTIONS._fields_ = [
    ('FullNonPow2TextureSupport', BOOL),
]

D3D11_FEATURE_DATA_D3D9_SHADOW_SUPPORT._fields_ = [
    ('SupportsDepthAsTextureWithLessEqualComparisonFilter', BOOL),
]


class D3D11_SHADER_MIN_PRECISION_SUPPORT(ENUM):
    D3D11_SHADER_MIN_PRECISION_10_BIT = 0x1
    D3D11_SHADER_MIN_PRECISION_16_BIT = 0x2

D3D11_FEATURE_DATA_SHADER_MIN_PRECISION_SUPPORT._fields_ = [
    ('PixelShaderMinPrecision', UINT),
    ('AllOtherShaderStagesMinPrecision', UINT),
]


class D3D11_TILED_RESOURCES_TIER(ENUM):
    D3D11_TILED_RESOURCES_NOT_SUPPORTED = 0
    D3D11_TILED_RESOURCES_TIER_1 = 1
    D3D11_TILED_RESOURCES_TIER_2 = 2
    D3D11_TILED_RESOURCES_TIER_3 = 3

D3D11_FEATURE_DATA_D3D11_OPTIONS1._fields_ = [
    ('TiledResourcesTier', D3D11_TILED_RESOURCES_TIER),
    ('MinMaxFiltering', BOOL),
    ('ClearViewAlsoSupportsDepthOnlyFormats', BOOL),
    ('MapOnDefaultBuffers', BOOL),
]

D3D11_FEATURE_DATA_D3D9_SIMPLE_INSTANCING_SUPPORT._fields_ = [
    ('SimpleInstancingSupported', BOOL),
]

D3D11_FEATURE_DATA_MARKER_SUPPORT._fields_ = [
    ('Profile', BOOL),
]

D3D11_FEATURE_DATA_D3D9_OPTIONS1._fields_ = [
    ('FullNonPow2TextureSupported', BOOL),
    ('DepthAsTextureWithLessEqualComparisonFilterSupported', BOOL),
    ('SimpleInstancingSupported', BOOL),
    ('TextureCubeFaceRenderTargetWithNonCubeDepthStencilSupported', BOOL),
]


class D3D11_CONSERVATIVE_RASTERIZATION_TIER(ENUM):
    D3D11_CONSERVATIVE_RASTERIZATION_NOT_SUPPORTED = 0
    D3D11_CONSERVATIVE_RASTERIZATION_TIER_1 = 1
    D3D11_CONSERVATIVE_RASTERIZATION_TIER_2 = 2
    D3D11_CONSERVATIVE_RASTERIZATION_TIER_3 = 3

D3D11_FEATURE_DATA_D3D11_OPTIONS2._fields_ = [
    ('PSSpecifiedStencilRefSupported', BOOL),
    ('TypedUAVLoadAdditionalFormats', BOOL),
    ('ROVsSupported', BOOL),
    ('ConservativeRasterizationTier', D3D11_CONSERVATIVE_RASTERIZATION_TIER),
    ('TiledResourcesTier', D3D11_TILED_RESOURCES_TIER),
    ('MapOnDefaultTextures', BOOL),
    ('StandardSwizzle', BOOL),
    ('UnifiedMemoryArchitecture', BOOL),
]

D3D11_FEATURE_DATA_D3D11_OPTIONS3._fields_ = [
    ('VPAndRTArrayIndexFromAnyShaderFeedingRasterizer', BOOL),
]

D3D11_FEATURE_DATA_GPU_VIRTUAL_ADDRESS_SUPPORT._fields_ = [
    ('MaxGPUVirtualAddressBitsPerResource', UINT),
    ('MaxGPUVirtualAddressBitsPerProcess', UINT),
]


class D3D11_SHADER_CACHE_SUPPORT_FLAGS(ENUM):
    D3D11_SHADER_CACHE_SUPPORT_NONE = 0
    D3D11_SHADER_CACHE_SUPPORT_AUTOMATIC_INPROC_CACHE = 0x1
    D3D11_SHADER_CACHE_SUPPORT_AUTOMATIC_DISK_CACHE = 0x2

D3D11_FEATURE_DATA_SHADER_CACHE._fields_ = [
    ('SupportFlags', UINT),
]


class D3D11_SHARED_RESOURCE_TIER(ENUM):
    D3D11_SHARED_RESOURCE_TIER_0 = 0
    D3D11_SHARED_RESOURCE_TIER_1 = D3D11_SHARED_RESOURCE_TIER_0 + 1
    D3D11_SHARED_RESOURCE_TIER_2 = D3D11_SHARED_RESOURCE_TIER_1 + 1

D3D11_FEATURE_DATA_D3D11_OPTIONS5._fields_ = [
    ('SharedResourceTier', D3D11_SHARED_RESOURCE_TIER),
]

IID_ID3D11DeviceContext = MIDL_INTERFACE(
    "{C0BFA96C-E089-44FB-8EAF-26F8796190DA}"
)
ID3D11DeviceContext._iid_ = IID_ID3D11DeviceContext


ID3D11DeviceContext._methods_ = [
    COMMETHOD(
        [helpstring('Method VSSetConstantBuffers')],
        VOID,
        'VSSetConstantBuffers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (['in'], POINTER(ID3D11Buffer), 'ppConstantBuffers'),
    ),
    COMMETHOD(
        [helpstring('Method PSSetShaderResources')],
        VOID,
        'PSSetShaderResources',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumViews'),
        (['in'], POINTER(ID3D11ShaderResourceView), 'ppShaderResourceViews'),
    ),
    COMMETHOD(
        [helpstring('Method PSSetShader')],
        VOID,
        'PSSetShader',
        (['in'], POINTER(ID3D11PixelShader), 'pPixelShader'),
        (['in'], POINTER(ID3D11ClassInstance), 'ppClassInstances'),
        ([], UINT, 'NumClassInstances'),
    ),
    COMMETHOD(
        [helpstring('Method PSSetSamplers')],
        VOID,
        'PSSetSamplers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumSamplers'),
        (['in'], POINTER(ID3D11SamplerState), 'ppSamplers'),
    ),
    COMMETHOD(
        [helpstring('Method VSSetShader')],
        VOID,
        'VSSetShader',
        (
            ['in'],
            POINTER(ID3D11VertexShader),
            'pVertexShader'
        ),
        (['in'], POINTER(ID3D11ClassInstance), 'ppClassInstances'),
        ([], UINT, 'NumClassInstances'),
    ),
    COMMETHOD(
        [helpstring('Method DrawIndexed')],
        VOID,
        'DrawIndexed',
        (['in'], UINT, 'IndexCount'),
        (['in'], UINT, 'StartIndexLocation'),
        (['in'], INT, 'BaseVertexLocation'),
    ),
    COMMETHOD(
        [helpstring('Method Draw')],
        VOID,
        'Draw',
        (['in'], UINT, 'VertexCount'),
        (['in'], UINT, 'StartVertexLocation'),
    ),
    COMMETHOD(
        [helpstring('Method Map')],
        HRESULT,
        'Map',
        (['in'], POINTER(ID3D11Resource), 'pResource'),
        (['in'], UINT, 'Subresource'),
        (['in'], D3D11_MAP, 'MapType'),
        (['in'], UINT, 'MapFlags'),
        (
            ['out'],
            POINTER(D3D11_MAPPED_SUBRESOURCE),
            'pMappedResource'
        ),
    ),
    COMMETHOD(
        [helpstring('Method Unmap')],
        VOID,
        'Unmap',
        (['in'], POINTER(ID3D11Resource), 'pResource'),
        (['in'], UINT, 'Subresource'),
    ),
    COMMETHOD(
        [helpstring('Method PSSetConstantBuffers')],
        VOID,
        'PSSetConstantBuffers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (['in'], POINTER(ID3D11Buffer), 'ppConstantBuffers'),
    ),
    COMMETHOD(
        [helpstring('Method IASetInputLayout')],
        VOID,
        'IASetInputLayout',
        (['in'], POINTER(ID3D11InputLayout), 'pInputLayout'),
    ),
    COMMETHOD(
        [helpstring('Method IASetVertexBuffers')],
        VOID,
        'IASetVertexBuffers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (['in'], POINTER(ID3D11Buffer), 'ppVertexBuffers'),
        (['in'], POINTER(UINT), 'pStrides'),
        (['in'], POINTER(UINT), 'pOffsets'),
    ),
    COMMETHOD(
        [helpstring('Method IASetIndexBuffer')],
        VOID,
        'IASetIndexBuffer',
        (['in'], POINTER(ID3D11Buffer), 'pIndexBuffer'),
        (['in'], DXGI_FORMAT, 'Format'),
        (['in'], UINT, 'Offset'),
    ),
    COMMETHOD(
        [helpstring('Method DrawIndexedInstanced')],
        VOID,
        'DrawIndexedInstanced',
        (['in'], UINT, 'IndexCountPerInstance'),
        (['in'], UINT, 'InstanceCount'),
        (['in'], UINT, 'StartIndexLocation'),
        (['in'], INT, 'BaseVertexLocation'),
        (['in'], UINT, 'StartInstanceLocation'),
    ),
    COMMETHOD(
        [helpstring('Method DrawInstanced')],
        VOID,
        'DrawInstanced',
        (['in'], UINT, 'VertexCountPerInstance'),
        (['in'], UINT, 'InstanceCount'),
        (['in'], UINT, 'StartVertexLocation'),
        (['in'], UINT, 'StartInstanceLocation'),
    ),
    COMMETHOD(
        [helpstring('Method GSSetConstantBuffers')],
        VOID,
        'GSSetConstantBuffers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (['in'], POINTER(ID3D11Buffer), 'ppConstantBuffers'),
    ),
    COMMETHOD(
        [helpstring('Method GSSetShader')],
        VOID,
        'GSSetShader',
        (['in'], POINTER(ID3D11GeometryShader), 'pShader'),
        (['in'], POINTER(ID3D11ClassInstance), 'ppClassInstances'),
        ([], UINT, 'NumClassInstances'),
    ),
    COMMETHOD(
        [helpstring('Method IASetPrimitiveTopology')],
        VOID,
        'IASetPrimitiveTopology',
        (['in'], D3D11_PRIMITIVE_TOPOLOGY, 'Topology'),
    ),
    COMMETHOD(
        [helpstring('Method VSSetShaderResources')],
        VOID,
        'VSSetShaderResources',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumViews'),
        (['in'], POINTER(ID3D11ShaderResourceView), 'ppShaderResourceViews'),
    ),
    COMMETHOD(
        [helpstring('Method VSSetSamplers')],
        VOID,
        'VSSetSamplers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumSamplers'),
        (['in'], POINTER(ID3D11SamplerState), 'ppSamplers'),
    ),
    COMMETHOD(
        [helpstring('Method Begin')],
        VOID,
        'Begin',
        (['in'], POINTER(ID3D11Asynchronous), 'pAsync'),
    ),
    COMMETHOD(
        [helpstring('Method End')],
        VOID,
        'End',
        (['in'], POINTER(ID3D11Asynchronous), 'pAsync'),
    ),
    COMMETHOD(
        [helpstring('Method GetData')],
        HRESULT,
        'GetData',
        (['in'], POINTER(ID3D11Asynchronous), 'pAsync'),
        (['out'], POINTER(VOID), 'pData'),
        (['in'], UINT, 'DataSize'),
        (['in'], UINT, 'GetDataFlags'),
    ),
    COMMETHOD(
        [helpstring('Method SetPredication')],
        VOID,
        'SetPredication',
        (['in'], POINTER(ID3D11Predicate), 'pPredicate'),
        (['in'], BOOL, 'PredicateValue'),
    ),
    COMMETHOD(
        [helpstring('Method GSSetShaderResources')],
        VOID,
        'GSSetShaderResources',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumViews'),
        (['in'], POINTER(ID3D11ShaderResourceView), 'ppShaderResourceViews'),
    ),
    COMMETHOD(
        [helpstring('Method GSSetSamplers')],
        VOID,
        'GSSetSamplers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumSamplers'),
        (['in'], POINTER(ID3D11SamplerState), 'ppSamplers'),
    ),
    COMMETHOD(
        [helpstring('Method OMSetRenderTargets')],
        VOID,
        'OMSetRenderTargets',
        (['in'], UINT, 'NumViews'),
        (['in'], POINTER(ID3D11RenderTargetView), 'ppRenderTargetViews'),
        (
            ['in'],
            POINTER(ID3D11DepthStencilView),
            'pDepthStencilView'
        ),
    ),
    COMMETHOD(
        [helpstring('Method OMSetRenderTargetsAndUnorderedAccessViews')],
        VOID,
        'OMSetRenderTargetsAndUnorderedAccessViews',
        (['in'], UINT, 'NumRTVs'),
        (['in'], POINTER(ID3D11RenderTargetView), 'ppRenderTargetViews'),
        (
            ['in'],
            POINTER(ID3D11DepthStencilView),
            'pDepthStencilView'
        ),
        (['in'], UINT, 'UAVStartSlot'),
        (['in'], UINT, 'NumUAVs'),
        (['in'], POINTER(ID3D11UnorderedAccessView), 'ppUnorderedAccessViews'),
        (['in'], POINTER(UINT), 'pUAVInitialCounts'),
    ),
    COMMETHOD(
        [helpstring('Method OMSetBlendState')],
        VOID,
        'OMSetBlendState',
        (['in'], POINTER(ID3D11BlendState), 'pBlendState'),
        (['in'], FLOAT * 4, 'BlendFactor'),
        (['in'], UINT, 'SampleMask'),
    ),

    COMMETHOD(
        [helpstring('Method OMSetDepthStencilState')],
        VOID,
        'OMSetDepthStencilState',
        (
            ['in'],
            POINTER(ID3D11DepthStencilState),
            'pDepthStencilState'
        ),
        (['in'], UINT, 'StencilRef'),
    ),

    COMMETHOD(
        [helpstring('Method SOSetTargets')],
        VOID,
        'SOSetTargets',
        (['in'], UINT, 'NumBuffers'),
        (['in'], POINTER(ID3D11Buffer), 'ppSOTargets'),
        (['in'], POINTER(UINT), 'pOffsets'),
    ),

    COMMETHOD(
        [helpstring('Method DrawAuto')],
        VOID,
        'DrawAuto',
    ),

    COMMETHOD(
        [helpstring('Method DrawIndexedInstancedIndirect')],
        VOID,
        'DrawIndexedInstancedIndirect',
        (['in'], POINTER(ID3D11Buffer), 'pBufferForArgs'),
        (['in'], UINT, 'AlignedByteOffsetForArgs'),
    ),

    COMMETHOD(
        [helpstring('Method DrawInstancedIndirect')],
        VOID,
        'DrawInstancedIndirect',
        (['in'], POINTER(ID3D11Buffer), 'pBufferForArgs'),
        (['in'], UINT, 'AlignedByteOffsetForArgs'),
    ),

    COMMETHOD(
        [helpstring('Method Dispatch')],
        VOID,
        'Dispatch',
        (['in'], UINT, 'ThreadGroupCountX'),
        (['in'], UINT, 'ThreadGroupCountY'),
        (['in'], UINT, 'ThreadGroupCountZ'),
    ),

    COMMETHOD(
        [helpstring('Method DispatchIndirect')],
        VOID,
        'DispatchIndirect',
        (['in'], POINTER(ID3D11Buffer), 'pBufferForArgs'),
        (['in'], UINT, 'AlignedByteOffsetForArgs'),
    ),

    COMMETHOD(
        [helpstring('Method RSSetState')],
        VOID,
        'RSSetState',
        (
            ['in'],
            POINTER(ID3D11RasterizerState),
            'pRasterizerState'
        ),
    ),

    COMMETHOD(
        [helpstring('Method RSSetViewports')],
        VOID,
        'RSSetViewports',
        (['in'], UINT, 'NumViewports'),
        (['in'], POINTER(D3D11_VIEWPORT), 'pViewports'),
    ),

    COMMETHOD(
        [helpstring('Method RSSetScissorRects')],
        VOID,
        'RSSetScissorRects',
        (['in'], UINT, 'NumRects'),
        (['in'], POINTER(D3D11_RECT), 'pRects'),
    ),

    COMMETHOD(
        [helpstring('Method CopySubresourceRegion')],
        VOID,
        'CopySubresourceRegion',
        (['in'], POINTER(ID3D11Resource), 'pDstResource'),
        (['in'], UINT, 'DstSubresource'),
        (['in'], UINT, 'DstX'),
        (['in'], UINT, 'DstY'),
        (['in'], UINT, 'DstZ'),
        (['in'], POINTER(ID3D11Resource), 'pSrcResource'),
        (['in'], UINT, 'SrcSubresource'),
        (['in'], POINTER(D3D11_BOX), 'pSrcBox'),
    ),

    COMMETHOD(
        [helpstring('Method CopyResource')],
        VOID,
        'CopyResource',
        (['in'], POINTER(ID3D11Resource), 'pDstResource'),
        (['in'], POINTER(ID3D11Resource), 'pSrcResource'),
    ),

    COMMETHOD(
        [helpstring('Method UpdateSubresource')],
        VOID,
        'UpdateSubresource',
        (['in'], POINTER(ID3D11Resource), 'pDstResource'),
        (['in'], UINT, 'DstSubresource'),
        (['in'], POINTER(D3D11_BOX), 'pDstBox'),
        (['in'], POINTER(VOID), 'pSrcData'),
        (['in'], UINT, 'SrcRowPitch'),
        (['in'], UINT, 'SrcDepthPitch'),
    ),

    COMMETHOD(
        [helpstring('Method CopyStructureCount')],
        VOID,
        'CopyStructureCount',
        (['in'], POINTER(ID3D11Buffer), 'pDstBuffer'),
        (['in'], UINT, 'DstAlignedByteOffset'),
        (
            ['in'],
            POINTER(ID3D11UnorderedAccessView),
            'pSrcView'
        ),
    ),

    COMMETHOD(
        [helpstring('Method ClearRenderTargetView')],
        VOID,
        'ClearRenderTargetView',
        (
            ['in'],
            POINTER(ID3D11RenderTargetView),
            'pRenderTargetView'
        ),
        (['in'], FLOAT * 4, 'ColorRGBA'),
    ),
    COMMETHOD(
        [helpstring('Method ClearUnorderedAccessViewUint')],
        VOID,
        'ClearUnorderedAccessViewUint',
        (
            ['in'],
            POINTER(ID3D11UnorderedAccessView),
            'pUnorderedAccessView'
        ),
        (['in'], UINT * 4, 'Values'),
    ),
    COMMETHOD(
        [helpstring('Method ClearUnorderedAccessViewFloat')],
        VOID,
        'ClearUnorderedAccessViewFloat',
        (
            ['in'],
            POINTER(ID3D11UnorderedAccessView),
            'pUnorderedAccessView'
        ),
        (['in'], FLOAT * 4, 'Values'),
    ),
    COMMETHOD(
        [helpstring('Method ClearDepthStencilView')],
        VOID,
        'ClearDepthStencilView',
        (
            ['in'],
            POINTER(ID3D11DepthStencilView),
            'pDepthStencilView'
        ),
        (['in'], UINT, 'ClearFlags'),
        (['in'], FLOAT, 'Depth'),
        (['in'], UINT8, 'Stencil'),
    ),
    COMMETHOD(
        [helpstring('Method GenerateMips')],
        VOID,
        'GenerateMips',
        (
            ['in'],
            POINTER(ID3D11ShaderResourceView),
            'pShaderResourceView'
        ),
    ),
    COMMETHOD(
        [helpstring('Method SetResourceMinLOD')],
        VOID,
        'SetResourceMinLOD',
        (['in'], POINTER(ID3D11Resource), 'pResource'),
        ([], FLOAT, 'MinLOD'),
    ),
    COMMETHOD(
        [helpstring('Method GetResourceMinLOD')],
        FLOAT,
        'GetResourceMinLOD',
        (['in'], POINTER(ID3D11Resource), 'pResource'),
    ),
    COMMETHOD(
        [helpstring('Method ResolveSubresource')],
        VOID,
        'ResolveSubresource',
        (['in'], POINTER(ID3D11Resource), 'pDstResource'),
        (['in'], UINT, 'DstSubresource'),
        (['in'], POINTER(ID3D11Resource), 'pSrcResource'),
        (['in'], UINT, 'SrcSubresource'),
        (['in'], DXGI_FORMAT, 'Format'),
    ),
    COMMETHOD(
        [helpstring('Method ExecuteCommandList')],
        VOID,
        'ExecuteCommandList',
        (['in'], POINTER(ID3D11CommandList), 'pCommandList'),
        ([], BOOL, 'RestoreContextState'),
    ),
    COMMETHOD(
        [helpstring('Method HSSetShaderResources')],
        VOID,
        'HSSetShaderResources',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumViews'),
        (['in'], POINTER(ID3D11ShaderResourceView), 'ppShaderResourceViews'),
    ),
    COMMETHOD(
        [helpstring('Method HSSetShader')],
        VOID,
        'HSSetShader',
        (['in'], POINTER(ID3D11HullShader), 'pHullShader'),
        (['in'], POINTER(ID3D11ClassInstance), 'ppClassInstances'),
        ([], UINT, 'NumClassInstances'),
    ),
    COMMETHOD(
        [helpstring('Method HSSetSamplers')],
        VOID,
        'HSSetSamplers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumSamplers'),
        (['in'], POINTER(ID3D11SamplerState), 'ppSamplers'),
    ),
    COMMETHOD(
        [helpstring('Method HSSetConstantBuffers')],
        VOID,
        'HSSetConstantBuffers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (['in'], POINTER(ID3D11Buffer), 'ppConstantBuffers'),
    ),
    COMMETHOD(
        [helpstring('Method DSSetShaderResources')],
        VOID,
        'DSSetShaderResources',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumViews'),
        (['in'], POINTER(ID3D11ShaderResourceView), 'ppShaderResourceViews'),
    ),
    COMMETHOD(
        [helpstring('Method DSSetShader')],
        VOID,
        'DSSetShader',
        (
            ['in'],
            POINTER(ID3D11DomainShader),
            'pDomainShader'
        ),
        (['in'], POINTER(ID3D11ClassInstance), 'ppClassInstances'),
        ([], UINT, 'NumClassInstances'),
    ),
    COMMETHOD(
        [helpstring('Method DSSetSamplers')],
        VOID,
        'DSSetSamplers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumSamplers'),
        (['in'], POINTER(ID3D11SamplerState), 'ppSamplers'),
    ),
    COMMETHOD(
        [helpstring('Method DSSetConstantBuffers')],
        VOID,
        'DSSetConstantBuffers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (['in'], POINTER(ID3D11Buffer), 'ppConstantBuffers'),
    ),
    COMMETHOD(
        [helpstring('Method CSSetShaderResources')],
        VOID,
        'CSSetShaderResources',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumViews'),
        (['in'], POINTER(ID3D11ShaderResourceView), 'ppShaderResourceViews'),
    ),
    COMMETHOD(
        [helpstring('Method CSSetUnorderedAccessViews')],
        VOID,
        'CSSetUnorderedAccessViews',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumUAVs'),
        (['in'], POINTER(ID3D11UnorderedAccessView), 'ppUnorderedAccessViews'),
        (['in'], POINTER(UINT), 'pUAVInitialCounts'),
    ),
    COMMETHOD(
        [helpstring('Method CSSetShader')],
        VOID,
        'CSSetShader',
        (
            ['in'],
            POINTER(ID3D11ComputeShader),
            'pComputeShader'
        ),
        (['in'], POINTER(ID3D11ClassInstance), 'ppClassInstances'),
        (['in'], UINT, 'NumClassInstances'),
    ),
    COMMETHOD(
        [helpstring('Method CSSetSamplers')],
        VOID,
        'CSSetSamplers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumSamplers'),
        (['in'], POINTER(ID3D11SamplerState), 'ppSamplers'),
    ),
    COMMETHOD(
        [helpstring('Method CSSetConstantBuffers')],
        VOID,
        'CSSetConstantBuffers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (['in'], POINTER(ID3D11Buffer), 'ppConstantBuffers'),
    ),
    COMMETHOD(
        [helpstring('Method VSGetConstantBuffers')],
        VOID,
        'VSGetConstantBuffers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (
            ['out'],
            POINTER(POINTER(ID3D11Buffer)),
            'ppConstantBuffers'
        ),
    ),
    COMMETHOD(
        [helpstring('Method PSGetShaderResources')],
        VOID,
        'PSGetShaderResources',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumViews'),
        (
            ['out'],
            POINTER(POINTER(ID3D11ShaderResourceView)),
            'ppShaderResourceViews'
        ),
    ),
    COMMETHOD(
        [helpstring('Method PSGetShader')],
        VOID,
        'PSGetShader',
        (
            ['out'],
            POINTER(POINTER(ID3D11PixelShader)),
            'ppPixelShader'
        ),
        (
            ['out', 'in'],
            POINTER(POINTER(ID3D11ClassInstance)),
            'ppClassInstances'
        ),
        (['out', 'in'], POINTER(UINT), 'pNumClassInstances'),
    ),
    COMMETHOD(
        [helpstring('Method PSGetSamplers')],
        VOID,
        'PSGetSamplers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumSamplers'),
        (
            ['out'],
            POINTER(POINTER(ID3D11SamplerState)),
            'ppSamplers'
        ),
    ),
    COMMETHOD(
        [helpstring('Method VSGetShader')],
        VOID,
        'VSGetShader',
        (
            ['out'],
            POINTER(POINTER(ID3D11VertexShader)),
            'ppVertexShader'
        ),
        (
            ['out', 'in'],
            POINTER(POINTER(ID3D11ClassInstance)),
            'ppClassInstances'
        ),
        (['out', 'in'], POINTER(UINT), 'pNumClassInstances'),
    ),
    COMMETHOD(
        [helpstring('Method PSGetConstantBuffers')],
        VOID,
        'PSGetConstantBuffers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (
            ['out'],
            POINTER(POINTER(ID3D11Buffer)),
            'ppConstantBuffers'
        ),
    ),
    COMMETHOD(
        [helpstring('Method IAGetInputLayout')],
        VOID,
        'IAGetInputLayout',
        (
            ['out'],
            POINTER(POINTER(ID3D11InputLayout)),
            'ppInputLayout'
        ),
    ),
    COMMETHOD(
        [helpstring('Method IAGetVertexBuffers')],
        VOID,
        'IAGetVertexBuffers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (
            ['out'],
            POINTER(POINTER(ID3D11Buffer)),
            'ppVertexBuffers'
        ),
        (['out'], POINTER(UINT), 'pStrides'),
        (['out'], POINTER(UINT), 'pOffsets'),
    ),
    COMMETHOD(
        [helpstring('Method IAGetIndexBuffer')],
        VOID,
        'IAGetIndexBuffer',
        (
            ['out'],
            POINTER(POINTER(ID3D11Buffer)),
            'pIndexBuffer'
        ),
        (['out'], POINTER(DXGI_FORMAT), 'Format'),
        (['out'], POINTER(UINT), 'Offset'),
    ),
    COMMETHOD(
        [helpstring('Method GSGetConstantBuffers')],
        VOID,
        'GSGetConstantBuffers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (
            ['out'],
            POINTER(POINTER(ID3D11Buffer)),
            'ppConstantBuffers'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GSGetShader')],
        VOID,
        'GSGetShader',
        (
            ['out'],
            POINTER(POINTER(ID3D11GeometryShader)),
            'ppGeometryShader'
        ),
        (
            ['out', 'in'],
            POINTER(POINTER(ID3D11ClassInstance)),
            'ppClassInstances'
        ),
        (['out', 'in'], POINTER(UINT), 'pNumClassInstances'),
    ),
    COMMETHOD(
        [helpstring('Method IAGetPrimitiveTopology')],
        VOID,
        'IAGetPrimitiveTopology',
        (
            ['out'],
            POINTER(D3D11_PRIMITIVE_TOPOLOGY),
            'pTopology'
        ),
    ),
    COMMETHOD(
        [helpstring('Method VSGetShaderResources')],
        VOID,
        'VSGetShaderResources',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumViews'),
        (
            ['out'],
            POINTER(POINTER(ID3D11ShaderResourceView)),
            'ppShaderResourceViews'
        ),
    ),
    COMMETHOD(
        [helpstring('Method VSGetSamplers')],
        VOID,
        'VSGetSamplers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumSamplers'),
        (
            ['out'],
            POINTER(POINTER(ID3D11SamplerState)),
            'ppSamplers'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetPredication')],
        VOID,
        'GetPredication',
        (
            ['out'],
            POINTER(POINTER(ID3D11Predicate)),
            'ppPredicate'
        ),
        (['out'], POINTER(BOOL), 'pPredicateValue'),
    ),
    COMMETHOD(
        [helpstring('Method GSGetShaderResources')],
        VOID,
        'GSGetShaderResources',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumViews'),
        (
            ['out'],
            POINTER(POINTER(ID3D11ShaderResourceView)),
            'ppShaderResourceViews'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GSGetSamplers')],
        VOID,
        'GSGetSamplers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumSamplers'),
        (
            ['out'],
            POINTER(POINTER(ID3D11SamplerState)),
            'ppSamplers'
        ),
    ),
    COMMETHOD(
        [helpstring('Method OMGetRenderTargets')],
        VOID,
        'OMGetRenderTargets',
        (['in'], UINT, 'NumViews'),
        (
            ['out'],
            POINTER(POINTER(ID3D11RenderTargetView)),
            'ppRenderTargetViews'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11DepthStencilView)),
            'ppDepthStencilView'
        ),
    ),
    COMMETHOD(
        [helpstring('Method OMGetRenderTargetsAndUnorderedAccessViews')],
        VOID,
        'OMGetRenderTargetsAndUnorderedAccessViews',
        (['in'], UINT, 'NumRTVs'),
        (
            ['out'],
            POINTER(POINTER(ID3D11RenderTargetView)),
            'ppRenderTargetViews'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11DepthStencilView)),
            'ppDepthStencilView'
        ),
        (['in'], UINT, 'UAVStartSlot'),
        (['in'], UINT, 'NumUAVs'),
        (
            ['out'],
            POINTER(POINTER(ID3D11UnorderedAccessView)),
            'ppUnorderedAccessViews'
        ),
    ),
    COMMETHOD(
        [helpstring('Method OMGetBlendState')],
        VOID,
        'OMGetBlendState',
        (
            ['out'],
            POINTER(POINTER(ID3D11BlendState)),
            'ppBlendState'
        ),
        (['out'], FLOAT * 4, 'BlendFactor'),
        (['out'], POINTER(UINT), 'pSampleMask'),
    ),
    COMMETHOD(
        [helpstring('Method OMGetDepthStencilState')],
        VOID,
        'OMGetDepthStencilState',
        (
            ['out'],
            POINTER(POINTER(ID3D11DepthStencilState)),
            'ppDepthStencilState'
        ),
        (['out'], POINTER(UINT), 'pStencilRef'),
    ),
    COMMETHOD(
        [helpstring('Method SOGetTargets')],
        VOID,
        'SOGetTargets',
        (['in'], UINT, 'NumBuffers'),
        (
            ['out'],
            POINTER(POINTER(ID3D11Buffer)),
            'ppSOTargets'
        ),
    ),
    COMMETHOD(
        [helpstring('Method RSGetState')],
        VOID,
        'RSGetState',
        (
            ['out'],
            POINTER(POINTER(ID3D11RasterizerState)),
            'ppRasterizerState'
        ),
    ),
    COMMETHOD(
        [helpstring('Method RSGetViewports')],
        VOID,
        'RSGetViewports',
        (['out', 'in'], POINTER(UINT), 'pNumViewports'),
        (['out'], POINTER(D3D11_VIEWPORT), 'pViewports'),
    ),
    COMMETHOD(
        [helpstring('Method RSGetScissorRects')],
        VOID,
        'RSGetScissorRects',
        (['out', 'in'], POINTER(UINT), 'pNumRects'),
        (['out'], POINTER(D3D11_RECT), 'pRects'),
    ),
    COMMETHOD(
        [helpstring('Method HSGetShaderResources')],
        VOID,
        'HSGetShaderResources',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumViews'),
        (
            ['out'],
            POINTER(POINTER(ID3D11ShaderResourceView)),
            'ppShaderResourceViews'
        ),
    ),
    COMMETHOD(
        [helpstring('Method HSGetShader')],
        VOID,
        'HSGetShader',
        (
            ['out'],
            POINTER(POINTER(ID3D11HullShader)),
            'ppHullShader'
        ),
        (
            ['out', 'in'],
            POINTER(POINTER(ID3D11ClassInstance)),
            'ppClassInstances'
        ),
        (['out', 'in'], POINTER(UINT), 'pNumClassInstances'),
    ),
    COMMETHOD(
        [helpstring('Method HSGetSamplers')],
        VOID,
        'HSGetSamplers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumSamplers'),
        (
            ['out'],
            POINTER(POINTER(ID3D11SamplerState)),
            'ppSamplers'
        ),
    ),
    COMMETHOD(
        [helpstring('Method HSGetConstantBuffers')],
        VOID,
        'HSGetConstantBuffers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (
            ['out'],
            POINTER(POINTER(ID3D11Buffer)),
            'ppConstantBuffers'
        ),
    ),
    COMMETHOD(
        [helpstring('Method DSGetShaderResources')],
        VOID,
        'DSGetShaderResources',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumViews'),
        (
            ['out'],
            POINTER(POINTER(ID3D11ShaderResourceView)),
            'ppShaderResourceViews'
        ),
    ),
    COMMETHOD(
        [helpstring('Method DSGetShader')],
        VOID,
        'DSGetShader',
        (
            ['out'],
            POINTER(POINTER(ID3D11DomainShader)),
            'ppDomainShader'
        ),
        (
            ['out', 'in'],
            POINTER(POINTER(ID3D11ClassInstance)),
            'ppClassInstances'
        ),
        (['out', 'in'], POINTER(UINT), 'pNumClassInstances'),
    ),
    COMMETHOD(
        [helpstring('Method DSGetSamplers')],
        VOID,
        'DSGetSamplers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumSamplers'),
        (
            ['out'],
            POINTER(POINTER(ID3D11SamplerState)),
            'ppSamplers'
        ),
    ),
    COMMETHOD(
        [helpstring('Method DSGetConstantBuffers')],
        VOID,
        'DSGetConstantBuffers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (
            ['out'],
            POINTER(POINTER(ID3D11Buffer)),
            'ppConstantBuffers'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CSGetShaderResources')],
        VOID,
        'CSGetShaderResources',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumViews'),
        (
            ['out'],
            POINTER(POINTER(ID3D11ShaderResourceView)),
            'ppShaderResourceViews'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CSGetUnorderedAccessViews')],
        VOID,
        'CSGetUnorderedAccessViews',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumUAVs'),
        (
            ['out'],
            POINTER(POINTER(ID3D11UnorderedAccessView)),
            'ppUnorderedAccessViews'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CSGetShader')],
        VOID,
        'CSGetShader',
        (
            ['out'],
            POINTER(POINTER(ID3D11ComputeShader)),
            'ppComputeShader'
        ),
        (
            ['out', 'in'],
            POINTER(POINTER(ID3D11ClassInstance)),
            'ppClassInstances'
        ),
        (['out', 'in'], POINTER(UINT), 'pNumClassInstances'),
    ),
    COMMETHOD(
        [helpstring('Method CSGetSamplers')],
        VOID,
        'CSGetSamplers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumSamplers'),
        (
            ['out'],
            POINTER(POINTER(ID3D11SamplerState)),
            'ppSamplers'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CSGetConstantBuffers')],
        VOID,
        'CSGetConstantBuffers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (
            ['out'],
            POINTER(POINTER(ID3D11Buffer)),
            'ppConstantBuffers'
        ),
    ),
    COMMETHOD(
        [helpstring('Method ClearState')],
        VOID,
        'ClearState',
    ),
    COMMETHOD(
        [helpstring('Method Flush')],
        VOID,
        'Flush',
    ),
    COMMETHOD(
        [helpstring('Method GetType')],
        D3D11_DEVICE_CONTEXT_TYPE,
        'GetType',
    ),
    COMMETHOD(
        [helpstring('Method GetContextFlags')],
        UINT,
        'GetContextFlags',
    ),
    COMMETHOD(
        [helpstring('Method FinishCommandList')],
        HRESULT,
        'FinishCommandList',
        ([], BOOL, 'RestoreDeferredContextState'),
        (
            ['out'],
            POINTER(POINTER(ID3D11CommandList)),
            'ppCommandList'
        ),
    ),
]
CD3D11_VIDEO_DEFAULT = None
APP_DEPRECATED_HRESULT = None

D3D11_DECODER_PROFILE_MPEG2_MOCOMP = GUID('{E6A9F44B-61B0-4563-9EA4-63D2A3C6FE66}')
D3D11_DECODER_PROFILE_MPEG2_IDCT = GUID('{BF22AD00-03EA-4690-8077-473346209B7E}')
D3D11_DECODER_PROFILE_MPEG2_VLD = GUID('{EE27417F-5E28-4E65-BEEA-1D26B508ADC9}')
D3D11_DECODER_PROFILE_MPEG1_VLD = GUID('{6F3EC719-3735-42CC-8063-65CC3CB36616}')
D3D11_DECODER_PROFILE_MPEG2and1_VLD = GUID('{86695F12-340E-4F04-9FD3-9253DD327460}')
D3D11_DECODER_PROFILE_H264_MOCOMP_NOFGT = GUID('{1B81BE64-A0C7-11D3-B984-00C04F2E73C5}')
D3D11_DECODER_PROFILE_H264_MOCOMP_FGT = GUID('{1B81BE65-A0C7-11D3-B984-00C04F2E73C5}')
D3D11_DECODER_PROFILE_H264_IDCT_NOFGT = GUID('{1B81BE66-A0C7-11D3-B984-00C04F2E73C5}')
D3D11_DECODER_PROFILE_H264_IDCT_FGT = GUID('{1B81BE67-A0C7-11D3-B984-00C04F2E73C5}')
D3D11_DECODER_PROFILE_H264_VLD_NOFGT = GUID('{1B81BE68-A0C7-11D3-B984-00C04F2E73C5}')
D3D11_DECODER_PROFILE_H264_VLD_FGT = GUID('{1B81BE69-A0C7-11D3-B984-00C04F2E73C5}')
D3D11_DECODER_PROFILE_H264_VLD_WITHFMOASO_NOFGT = GUID('{D5F04FF9-3418-45D8-9561-32A76AAE2DDD}')
D3D11_DECODER_PROFILE_H264_VLD_STEREO_PROGRESSIVE_NOFGT = GUID('{D79BE8DA-0CF1-4C81-B82A-69A4E236F43D}')
D3D11_DECODER_PROFILE_H264_VLD_STEREO_NOFGT = GUID('{F9AACCBB-C2B6-4CFC-8779-5707B1760552}')
D3D11_DECODER_PROFILE_H264_VLD_MULTIVIEW_NOFGT = GUID('{705B9D82-76CF-49D6-B7E6-AC8872DB013C}')
D3D11_DECODER_PROFILE_WMV8_POSTPROC = GUID('{1B81BE80-A0C7-11D3-B984-00C04F2E73C5}')
D3D11_DECODER_PROFILE_WMV8_MOCOMP = GUID('{1B81BE81-A0C7-11D3-B984-00C04F2E73C5}')
D3D11_DECODER_PROFILE_WMV9_POSTPROC = GUID('{1B81BE90-A0C7-11D3-B984-00C04F2E73C5}')
D3D11_DECODER_PROFILE_WMV9_MOCOMP = GUID('{1B81BE91-A0C7-11D3-B984-00C04F2E73C5}')
D3D11_DECODER_PROFILE_WMV9_IDCT = GUID('{1B81BE94-A0C7-11D3-B984-00C04F2E73C5}')
D3D11_DECODER_PROFILE_VC1_POSTPROC = GUID('{1B81BEA0-A0C7-11D3-B984-00C04F2E73C5}')
D3D11_DECODER_PROFILE_VC1_MOCOMP = GUID('{1B81BEA1-A0C7-11D3-B984-00C04F2E73C5}')
D3D11_DECODER_PROFILE_VC1_IDCT = GUID('{1B81BEA2-A0C7-11D3-B984-00C04F2E73C5}')
D3D11_DECODER_PROFILE_VC1_VLD = GUID('{1B81BEA3-A0C7-11D3-B984-00C04F2E73C5}')
D3D11_DECODER_PROFILE_VC1_D2010 = GUID('{1B81BEA4-A0C7-11D3-B984-00C04F2E73C5}')
D3D11_DECODER_PROFILE_MPEG4PT2_VLD_SIMPLE = GUID('{EFD64D74-C9E8-41D7-A5E9-E9B0E39FA319}')
D3D11_DECODER_PROFILE_MPEG4PT2_VLD_ADVSIMPLE_NOGMC = GUID('{ED418A9F-010D-4EDA-9AE3-9A65358D8D2E}')
D3D11_DECODER_PROFILE_MPEG4PT2_VLD_ADVSIMPLE_GMC = GUID('{AB998B5B-4258-44A9-9FEB-94E597A6BAAE}')
D3D11_DECODER_PROFILE_HEVC_VLD_MAIN = GUID('{5B11D51B-2F4C-4452-BCC3-09F2A1160CC0}')
D3D11_DECODER_PROFILE_HEVC_VLD_MAIN10 = GUID('{107AF0E0-EF1A-4D19-ABA8-67A163073D13}')
D3D11_DECODER_PROFILE_VP9_VLD_PROFILE0 = GUID('{463707F8-A1D0-4585-876D-83AA6D60B89E}')
D3D11_DECODER_PROFILE_VP9_VLD_10BIT_PROFILE2 = GUID('{A4C749EF-6ECF-48AA-8448-50A7A1165FF7}')
D3D11_DECODER_PROFILE_VP8_VLD = GUID('{90B899EA-3A62-4705-88B3-8DF04B2744E7}')

D3D11_VIDEO_DECODER_DESC._fields_ = [
    ('Guid', GUID),
    ('SampleWidth', UINT),
    ('SampleHeight', UINT),
    ('OutputFormat', DXGI_FORMAT),
]

D3D11_VIDEO_DECODER_CONFIG._fields_ = [
    ('guidConfigBitstreamEncryption', GUID),
    ('guidConfigMBcontrolEncryption', GUID),
    ('guidConfigResidDiffEncryption', GUID),
    ('ConfigBitstreamRaw', UINT),
    ('ConfigMBcontrolRasterOrder', UINT),
    ('ConfigResidDiffHost', UINT),
    ('ConfigSpatialResid8', UINT),
    ('ConfigResid8Subtraction', UINT),
    ('ConfigSpatialHost8or9Clipping', UINT),
    ('ConfigSpatialResidInterleaved', UINT),
    ('ConfigIntraResidUnsigned', UINT),
    ('ConfigResidDiffAccelerator', UINT),
    ('ConfigHostInverseScan', UINT),
    ('ConfigSpecificIDCT', UINT),
    ('Config4GroupedCoefs', UINT),
    ('ConfigMinRenderTargetBuffCount', USHORT),
    ('ConfigDecoderSpecific', USHORT),
]


class D3D11_VIDEO_DECODER_BUFFER_TYPE(ENUM):
    D3D11_VIDEO_DECODER_BUFFER_PICTURE_PARAMETERS = 0
    D3D11_VIDEO_DECODER_BUFFER_MACROBLOCK_CONTROL = 1
    D3D11_VIDEO_DECODER_BUFFER_RESIDUAL_DIFFERENCE = 2
    D3D11_VIDEO_DECODER_BUFFER_DEBLOCKING_CONTROL = 3
    D3D11_VIDEO_DECODER_BUFFER_INVERSE_QUANTIZATION_MATRIX = 4
    D3D11_VIDEO_DECODER_BUFFER_SLICE_CONTROL = 5
    D3D11_VIDEO_DECODER_BUFFER_BITSTREAM = 6
    D3D11_VIDEO_DECODER_BUFFER_MOTION_VECTOR = 7
    D3D11_VIDEO_DECODER_BUFFER_FILM_GRAIN = 8

_D3D11_AES_CTR_IV._fields_ = [
    ('IV', UINT64),
    ('Count', UINT64),
]

D3D11_ENCRYPTED_BLOCK_INFO._fields_ = [
    ('NumEncryptedBytesAtBeginning', UINT),
    ('NumBytesInSkipPattern', UINT),
    ('NumBytesInEncryptPattern', UINT),
]

D3D11_VIDEO_DECODER_BUFFER_DESC._fields_ = [
    ('BufferType', D3D11_VIDEO_DECODER_BUFFER_TYPE),
    ('BufferIndex', UINT),
    ('DataOffset', UINT),
    ('DataSize', UINT),
    ('FirstMBaddress', UINT),
    ('NumMBsInBuffer', UINT),
    ('Width', UINT),
    ('Height', UINT),
    ('Stride', UINT),
    ('ReservedBits', UINT),
    # [annotation]
    ('pIV', POINTER(VOID)),
    ('IVSize', UINT),
    ('PartialEncryption', BOOL),
    ('EncryptedBlockInfo', D3D11_ENCRYPTED_BLOCK_INFO),
]

D3D11_VIDEO_DECODER_EXTENSION._fields_ = [
    ('Function', UINT),
    # [annotation]
    ('pPrivateInputData', POINTER(VOID)),
    ('PrivateInputDataSize', UINT),
    # [annotation]
    ('pPrivateOutputData', POINTER(VOID)),
    ('PrivateOutputDataSize', UINT),
    ('ResourceCount', UINT),
    # [annotation]
    ('ppResourceList', POINTER(POINTER(ID3D11Resource))),
]

IID_ID3D11VideoDecoder = MIDL_INTERFACE(
    "{3C9C5B51-995D-48D1-9B8D-FA5CAEDED65C}"
)
ID3D11VideoDecoder._iid_ = IID_ID3D11VideoDecoder


ID3D11VideoDecoder._methods_ = [
    COMMETHOD(
        [helpstring('Method GetCreationParameters')],
        HRESULT,
        'GetCreationParameters',
        (
            ['out'],
            POINTER(D3D11_VIDEO_DECODER_DESC),
            'pVideoDesc'
        ),
        (
            ['out'],
            POINTER(D3D11_VIDEO_DECODER_CONFIG),
            'pConfig'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetDriverHandle')],
        HRESULT,
        'GetDriverHandle',
        (['out'], POINTER(HANDLE), 'pDriverHandle'),
    ),
]

class D3D11_VIDEO_PROCESSOR_FORMAT_SUPPORT(ENUM):
    D3D11_VIDEO_PROCESSOR_FORMAT_SUPPORT_INPUT = 0x1
    D3D11_VIDEO_PROCESSOR_FORMAT_SUPPORT_OUTPUT = 0x2


class D3D11_VIDEO_PROCESSOR_DEVICE_CAPS(ENUM):
    D3D11_VIDEO_PROCESSOR_DEVICE_CAPS_LINEAR_SPACE = 0x1
    D3D11_VIDEO_PROCESSOR_DEVICE_CAPS_xvYCC = 0x2
    D3D11_VIDEO_PROCESSOR_DEVICE_CAPS_RGB_RANGE_CONVERSION = 0x4
    D3D11_VIDEO_PROCESSOR_DEVICE_CAPS_YCbCr_MATRIX_CONVERSION = 0x8
    D3D11_VIDEO_PROCESSOR_DEVICE_CAPS_NOMINAL_RANGE = 0x10


class D3D11_VIDEO_PROCESSOR_FEATURE_CAPS(ENUM):
    D3D11_VIDEO_PROCESSOR_FEATURE_CAPS_ALPHA_FILL = 0x1
    D3D11_VIDEO_PROCESSOR_FEATURE_CAPS_CONSTRICTION = 0x2
    D3D11_VIDEO_PROCESSOR_FEATURE_CAPS_LUMA_KEY = 0x4
    D3D11_VIDEO_PROCESSOR_FEATURE_CAPS_ALPHA_PALETTE = 0x8
    D3D11_VIDEO_PROCESSOR_FEATURE_CAPS_LEGACY = 0x10
    D3D11_VIDEO_PROCESSOR_FEATURE_CAPS_STEREO = 0x20
    D3D11_VIDEO_PROCESSOR_FEATURE_CAPS_ROTATION = 0x40
    D3D11_VIDEO_PROCESSOR_FEATURE_CAPS_ALPHA_STREAM = 0x80
    D3D11_VIDEO_PROCESSOR_FEATURE_CAPS_PIXEL_ASPECT_RATIO = 0x100
    D3D11_VIDEO_PROCESSOR_FEATURE_CAPS_MIRROR = 0x200
    D3D11_VIDEO_PROCESSOR_FEATURE_CAPS_SHADER_USAGE = 0x400
    D3D11_VIDEO_PROCESSOR_FEATURE_CAPS_METADATA_HDR10 = 0x800


class D3D11_VIDEO_PROCESSOR_FILTER_CAPS(ENUM):
    D3D11_VIDEO_PROCESSOR_FILTER_CAPS_BRIGHTNESS = 0x1
    D3D11_VIDEO_PROCESSOR_FILTER_CAPS_CONTRAST = 0x2
    D3D11_VIDEO_PROCESSOR_FILTER_CAPS_HUE = 0x4
    D3D11_VIDEO_PROCESSOR_FILTER_CAPS_SATURATION = 0x8
    D3D11_VIDEO_PROCESSOR_FILTER_CAPS_NOISE_REDUCTION = 0x10
    D3D11_VIDEO_PROCESSOR_FILTER_CAPS_EDGE_ENHANCEMENT = 0x20
    D3D11_VIDEO_PROCESSOR_FILTER_CAPS_ANAMORPHIC_SCALING = 0x40
    D3D11_VIDEO_PROCESSOR_FILTER_CAPS_STEREO_ADJUSTMENT = 0x80


class D3D11_VIDEO_PROCESSOR_FORMAT_CAPS(ENUM):
    D3D11_VIDEO_PROCESSOR_FORMAT_CAPS_RGB_INTERLACED = 0x1
    D3D11_VIDEO_PROCESSOR_FORMAT_CAPS_RGB_PROCAMP = 0x2
    D3D11_VIDEO_PROCESSOR_FORMAT_CAPS_RGB_LUMA_KEY = 0x4
    D3D11_VIDEO_PROCESSOR_FORMAT_CAPS_PALETTE_INTERLACED = 0x8


class D3D11_VIDEO_PROCESSOR_AUTO_STREAM_CAPS(ENUM):
    D3D11_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_DENOISE = 0x1
    D3D11_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_DERINGING = 0x2
    D3D11_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_EDGE_ENHANCEMENT = 0x4
    D3D11_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_COLOR_CORRECTION = 0x8
    D3D11_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_FLESH_TONE_MAPPING = 0x10
    D3D11_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_IMAGE_STABILIZATION = 0x20
    D3D11_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_SUPER_RESOLUTION = 0x40
    D3D11_VIDEO_PROCESSOR_AUTO_STREAM_CAPS_ANAMORPHIC_SCALING = 0x80


class D3D11_VIDEO_PROCESSOR_STEREO_CAPS(ENUM):
    D3D11_VIDEO_PROCESSOR_STEREO_CAPS_MONO_OFFSET = 0x1
    D3D11_VIDEO_PROCESSOR_STEREO_CAPS_ROW_INTERLEAVED = 0x2
    D3D11_VIDEO_PROCESSOR_STEREO_CAPS_COLUMN_INTERLEAVED = 0x4
    D3D11_VIDEO_PROCESSOR_STEREO_CAPS_CHECKERBOARD = 0x8
    D3D11_VIDEO_PROCESSOR_STEREO_CAPS_FLIP_MODE = 0x10

D3D11_VIDEO_PROCESSOR_CAPS._fields_ = [
    ('DeviceCaps', UINT),
    ('FeatureCaps', UINT),
    ('FilterCaps', UINT),
    ('InputFormatCaps', UINT),
    ('AutoStreamCaps', UINT),
    ('StereoCaps', UINT),
    ('RateConversionCapsCount', UINT),
    ('MaxInputStreams', UINT),
    ('MaxStreamStates', UINT),
]


class D3D11_VIDEO_PROCESSOR_PROCESSOR_CAPS(ENUM):
    D3D11_VIDEO_PROCESSOR_PROCESSOR_CAPS_DEINTERLACE_BLEND = 0x1
    D3D11_VIDEO_PROCESSOR_PROCESSOR_CAPS_DEINTERLACE_BOB = 0x2
    D3D11_VIDEO_PROCESSOR_PROCESSOR_CAPS_DEINTERLACE_ADAPTIVE = 0x4
    D3D11_VIDEO_PROCESSOR_PROCESSOR_CAPS_DEINTERLACE_MOTION_COMPENSATION = (
        0x8
    )
    D3D11_VIDEO_PROCESSOR_PROCESSOR_CAPS_INVERSE_TELECINE = 0x10
    D3D11_VIDEO_PROCESSOR_PROCESSOR_CAPS_FRAME_RATE_CONVERSION = 0x20


class D3D11_VIDEO_PROCESSOR_ITELECINE_CAPS(ENUM):
    D3D11_VIDEO_PROCESSOR_ITELECINE_CAPS_32 = 0x1
    D3D11_VIDEO_PROCESSOR_ITELECINE_CAPS_22 = 0x2
    D3D11_VIDEO_PROCESSOR_ITELECINE_CAPS_2224 = 0x4
    D3D11_VIDEO_PROCESSOR_ITELECINE_CAPS_2332 = 0x8
    D3D11_VIDEO_PROCESSOR_ITELECINE_CAPS_32322 = 0x10
    D3D11_VIDEO_PROCESSOR_ITELECINE_CAPS_55 = 0x20
    D3D11_VIDEO_PROCESSOR_ITELECINE_CAPS_64 = 0x40
    D3D11_VIDEO_PROCESSOR_ITELECINE_CAPS_87 = 0x80
    D3D11_VIDEO_PROCESSOR_ITELECINE_CAPS_222222222223 = 0x100
    D3D11_VIDEO_PROCESSOR_ITELECINE_CAPS_OTHER = 0x80000000

D3D11_VIDEO_PROCESSOR_RATE_CONVERSION_CAPS._fields_ = [
    ('PastFrames', UINT),
    ('FutureFrames', UINT),
    ('ProcessorCaps', UINT),
    ('ITelecineCaps', UINT),
    ('CustomRateCount', UINT),
]


class D3D11_CONTENT_PROTECTION_CAPS(ENUM):
    D3D11_CONTENT_PROTECTION_CAPS_SOFTWARE = 0x1
    D3D11_CONTENT_PROTECTION_CAPS_HARDWARE = 0x2
    D3D11_CONTENT_PROTECTION_CAPS_PROTECTION_ALWAYS_ON = 0x4
    D3D11_CONTENT_PROTECTION_CAPS_PARTIAL_DECRYPTION = 0x8
    D3D11_CONTENT_PROTECTION_CAPS_CONTENT_KEY = 0x10
    D3D11_CONTENT_PROTECTION_CAPS_FRESHEN_SESSION_KEY = 0x20
    D3D11_CONTENT_PROTECTION_CAPS_ENCRYPTED_READ_BACK = 0x40
    D3D11_CONTENT_PROTECTION_CAPS_ENCRYPTED_READ_BACK_KEY = 0x80
    D3D11_CONTENT_PROTECTION_CAPS_SEQUENTIAL_CTR_IV = 0x100
    D3D11_CONTENT_PROTECTION_CAPS_ENCRYPT_SLICEDATA_ONLY = 0x200
    D3D11_CONTENT_PROTECTION_CAPS_DECRYPTION_BLT = 0x400
    D3D11_CONTENT_PROTECTION_CAPS_HARDWARE_PROTECT_UNCOMPRESSED = 0x800
    D3D11_CONTENT_PROTECTION_CAPS_HARDWARE_PROTECTED_MEMORY_PAGEABLE = (
        0x1000
    )
    D3D11_CONTENT_PROTECTION_CAPS_HARDWARE_TEARDOWN = 0x2000
    D3D11_CONTENT_PROTECTION_CAPS_HARDWARE_DRM_COMMUNICATION = 0x4000
    D3D11_CONTENT_PROTECTION_CAPS_HARDWARE_DRM_COMMUNICATION_MULTI_THREADED = (
        0x8000
    )
    

D3D11_CRYPTO_TYPE_AES128_CTR = GUID('{9B6BD711-4F74-41C9-9E7B-0BE2D7D93B4F}')
D3D11_DECODER_ENCRYPTION_HW_CENC = GUID('{89D6AC4F-09F2-4229-B2CD-37740A6DFD81}')
D3D11_DECODER_BITSTREAM_ENCRYPTION_TYPE_CENC = GUID('{B0405235-C13D-44F2-9AE5-DD48E08E5B67}')
D3D11_DECODER_BITSTREAM_ENCRYPTION_TYPE_CBCS = GUID('{422D9319-9D21-4BB7-9371-FAF5A82C3E04}')
D3D11_KEY_EXCHANGE_HW_PROTECTION = GUID('{B1170D8A-628D-4DA3-AD3B-82DDB08B4970}')

D3D11_VIDEO_CONTENT_PROTECTION_CAPS._fields_ = [
    ('Caps', UINT),
    ('KeyExchangeTypeCount', UINT),
    ('BlockAlignmentSize', UINT),
    ('ProtectedMemorySize', ULONGLONG),
]

D3D11_VIDEO_PROCESSOR_CUSTOM_RATE._fields_ = [
    ('CustomRate', DXGI_RATIONAL),
    ('OutputFrames', UINT),
    ('InputInterlaced', BOOL),
    ('InputFramesOrFields', UINT),
]


class D3D11_VIDEO_PROCESSOR_FILTER(ENUM):
    D3D11_VIDEO_PROCESSOR_FILTER_BRIGHTNESS = 0
    D3D11_VIDEO_PROCESSOR_FILTER_CONTRAST = 1
    D3D11_VIDEO_PROCESSOR_FILTER_HUE = 2
    D3D11_VIDEO_PROCESSOR_FILTER_SATURATION = 3
    D3D11_VIDEO_PROCESSOR_FILTER_NOISE_REDUCTION = 4
    D3D11_VIDEO_PROCESSOR_FILTER_EDGE_ENHANCEMENT = 5
    D3D11_VIDEO_PROCESSOR_FILTER_ANAMORPHIC_SCALING = 6
    D3D11_VIDEO_PROCESSOR_FILTER_STEREO_ADJUSTMENT = 7

D3D11_VIDEO_PROCESSOR_FILTER_RANGE._fields_ = [
    ('Minimum', INT),
    ('Maximum', INT),
    ('Default', INT),
    ('Multiplier', FLOAT),
]


class D3D11_VIDEO_FRAME_FORMAT(ENUM):
    D3D11_VIDEO_FRAME_FORMAT_PROGRESSIVE = 0
    D3D11_VIDEO_FRAME_FORMAT_INTERLACED_TOP_FIELD_FIRST = 1
    D3D11_VIDEO_FRAME_FORMAT_INTERLACED_BOTTOM_FIELD_FIRST = 2


class D3D11_VIDEO_USAGE(ENUM):
    D3D11_VIDEO_USAGE_PLAYBACK_NORMAL = 0
    D3D11_VIDEO_USAGE_OPTIMAL_SPEED = 1
    D3D11_VIDEO_USAGE_OPTIMAL_QUALITY = 2

D3D11_VIDEO_PROCESSOR_CONTENT_DESC._fields_ = [
    ('InputFrameFormat', D3D11_VIDEO_FRAME_FORMAT),
    ('InputFrameRate', DXGI_RATIONAL),
    ('InputWidth', UINT),
    ('InputHeight', UINT),
    ('OutputFrameRate', DXGI_RATIONAL),
    ('OutputWidth', UINT),
    ('OutputHeight', UINT),
    ('Usage', D3D11_VIDEO_USAGE),
]


IID_ID3D11VideoProcessorEnumerator = MIDL_INTERFACE(
    "{31627037-53AB-4200-9061-05FAA9AB45F9}"
)
ID3D11VideoProcessorEnumerator._iid_ = IID_ID3D11VideoProcessorEnumerator


ID3D11VideoProcessorEnumerator._methods_ = [
    COMMETHOD(
        [helpstring('Method GetVideoProcessorContentDesc')],
        HRESULT,
        'GetVideoProcessorContentDesc',
        (
            ['out'],
            POINTER(D3D11_VIDEO_PROCESSOR_CONTENT_DESC),
            'pContentDesc'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CheckVideoProcessorFormat')],
        HRESULT,
        'CheckVideoProcessorFormat',
        (['in'], DXGI_FORMAT, 'Format'),
        (['out'], POINTER(UINT), 'pFlags'),
    ),
    COMMETHOD(
        [helpstring('Method GetVideoProcessorCaps')],
        HRESULT,
        'GetVideoProcessorCaps',
        (
            ['out'],
            POINTER(D3D11_VIDEO_PROCESSOR_CAPS),
            'pCaps'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetVideoProcessorRateConversionCaps')],
        HRESULT,
        'GetVideoProcessorRateConversionCaps',
        (['in'], UINT, 'TypeIndex'),
        (
            ['out'],
            POINTER(D3D11_VIDEO_PROCESSOR_RATE_CONVERSION_CAPS),
            'pCaps'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetVideoProcessorCustomRate')],
        HRESULT,
        'GetVideoProcessorCustomRate',
        (['in'], UINT, 'TypeIndex'),
        (['in'], UINT, 'CustomRateIndex'),
        (
            ['out'],
            POINTER(D3D11_VIDEO_PROCESSOR_CUSTOM_RATE),
            'pRate'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetVideoProcessorFilterRange')],
        HRESULT,
        'GetVideoProcessorFilterRange',
        (['in'], D3D11_VIDEO_PROCESSOR_FILTER, 'Filter'),
        (
            ['out'],
            POINTER(D3D11_VIDEO_PROCESSOR_FILTER_RANGE),
            'pRange'
        ),
    ),
]

D3D11_VIDEO_COLOR_RGBA._fields_ = [
    ('R', FLOAT),
    ('G', FLOAT),
    ('B', FLOAT),
    ('A', FLOAT),
]

D3D11_VIDEO_COLOR_YCbCrA._fields_ = [
    ('Y', FLOAT),
    ('Cb', FLOAT),
    ('Cr', FLOAT),
    ('A', FLOAT),
]


class _Union_9(ctypes.Union):
    pass


_Union_9._fields_ = [
    ('YCbCr', D3D11_VIDEO_COLOR_YCbCrA),
    ('RGBA', D3D11_VIDEO_COLOR_RGBA),
]
D3D11_VIDEO_COLOR._Union_9 = _Union_9

D3D11_VIDEO_COLOR._anonymous_ = (
    '_Union_9',
)

D3D11_VIDEO_COLOR._fields_ = [
    ('_Union_9', D3D11_VIDEO_COLOR._Union_9),
]


class D3D11_VIDEO_PROCESSOR_NOMINAL_RANGE(ENUM):
    D3D11_VIDEO_PROCESSOR_NOMINAL_RANGE_UNDEFINED = 0
    D3D11_VIDEO_PROCESSOR_NOMINAL_RANGE_16_235 = 1
    D3D11_VIDEO_PROCESSOR_NOMINAL_RANGE_0_255 = 2

D3D11_VIDEO_PROCESSOR_COLOR_SPACE._fields_ = [
    ('Usage', UINT, 1),
    ('RGB_Range', UINT, 1),
    ('YCbCr_Matrix', UINT, 1),
    ('YCbCr_xvYCC', UINT, 1),
    ('Nominal_Range', UINT, 2),
    ('Reserved', UINT, 26),
]


class D3D11_VIDEO_PROCESSOR_ALPHA_FILL_MODE(ENUM):
    D3D11_VIDEO_PROCESSOR_ALPHA_FILL_MODE_OPAQUE = 0
    D3D11_VIDEO_PROCESSOR_ALPHA_FILL_MODE_BACKGROUND = 1
    D3D11_VIDEO_PROCESSOR_ALPHA_FILL_MODE_DESTINATION = 2
    D3D11_VIDEO_PROCESSOR_ALPHA_FILL_MODE_SOURCE_STREAM = 3


class D3D11_VIDEO_PROCESSOR_OUTPUT_RATE(ENUM):
    D3D11_VIDEO_PROCESSOR_OUTPUT_RATE_NORMAL = 0
    D3D11_VIDEO_PROCESSOR_OUTPUT_RATE_HALF = 1
    D3D11_VIDEO_PROCESSOR_OUTPUT_RATE_CUSTOM = 2


class D3D11_VIDEO_PROCESSOR_STEREO_FORMAT(ENUM):
    D3D11_VIDEO_PROCESSOR_STEREO_FORMAT_MONO = 0
    D3D11_VIDEO_PROCESSOR_STEREO_FORMAT_HORIZONTAL = 1
    D3D11_VIDEO_PROCESSOR_STEREO_FORMAT_VERTICAL = 2
    D3D11_VIDEO_PROCESSOR_STEREO_FORMAT_SEPARATE = 3
    D3D11_VIDEO_PROCESSOR_STEREO_FORMAT_MONO_OFFSET = 4
    D3D11_VIDEO_PROCESSOR_STEREO_FORMAT_ROW_INTERLEAVED = 5
    D3D11_VIDEO_PROCESSOR_STEREO_FORMAT_COLUMN_INTERLEAVED = 6
    D3D11_VIDEO_PROCESSOR_STEREO_FORMAT_CHECKERBOARD = 7


class D3D11_VIDEO_PROCESSOR_STEREO_FLIP_MODE(ENUM):
    D3D11_VIDEO_PROCESSOR_STEREO_FLIP_NONE = 0
    D3D11_VIDEO_PROCESSOR_STEREO_FLIP_FRAME0 = 1
    D3D11_VIDEO_PROCESSOR_STEREO_FLIP_FRAME1 = 2


class D3D11_VIDEO_PROCESSOR_ROTATION(ENUM):
    D3D11_VIDEO_PROCESSOR_ROTATION_IDENTITY = 0
    D3D11_VIDEO_PROCESSOR_ROTATION_90 = 1
    D3D11_VIDEO_PROCESSOR_ROTATION_180 = 2
    D3D11_VIDEO_PROCESSOR_ROTATION_270 = 3

D3D11_VIDEO_PROCESSOR_STREAM._fields_ = [
    ('Enable', BOOL),
    ('OutputIndex', UINT),
    ('InputFrameOrField', UINT),
    ('PastFrames', UINT),
    ('FutureFrames', UINT),
    # [annotation]
    ('ppPastSurfaces', POINTER(POINTER(ID3D11VideoProcessorInputView))),
    ('pInputSurface', POINTER(ID3D11VideoProcessorInputView)),
    # [annotation]
    ('ppFutureSurfaces', POINTER(POINTER(ID3D11VideoProcessorInputView))),
    # [annotation]
    ('ppPastSurfacesRight', POINTER(POINTER(ID3D11VideoProcessorInputView))),
    ('pInputSurfaceRight', POINTER(ID3D11VideoProcessorInputView)),
    # [annotation]
    ('ppFutureSurfacesRight', POINTER(POINTER(ID3D11VideoProcessorInputView))),
]


IID_ID3D11VideoProcessor = MIDL_INTERFACE(
    "{1D7B0652-185F-41C6-85CE-0C5BE3D4AE6C}"
)
ID3D11VideoProcessor._iid_ = IID_ID3D11VideoProcessor


ID3D11VideoProcessor._methods_ = [
    COMMETHOD(
        [helpstring('Method GetContentDesc')],
        VOID,
        'GetContentDesc',
        (
            ['out'],
            POINTER(D3D11_VIDEO_PROCESSOR_CONTENT_DESC),
            'pDesc'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetRateConversionCaps')],
        VOID,
        'GetRateConversionCaps',
        (
            ['out'],
            POINTER(D3D11_VIDEO_PROCESSOR_RATE_CONVERSION_CAPS),
            'pCaps'
        ),
    ),
]

D3D11_OMAC._fields_ = [
    ('Omac', BYTE * 16),
]


class D3D11_AUTHENTICATED_CHANNEL_TYPE(ENUM):
    D3D11_AUTHENTICATED_CHANNEL_D3D11 = 1
    D3D11_AUTHENTICATED_CHANNEL_DRIVER_SOFTWARE = 2
    D3D11_AUTHENTICATED_CHANNEL_DRIVER_HARDWARE = 3


IID_ID3D11AuthenticatedChannel = MIDL_INTERFACE(
    "{3015A308-DCBD-47AA-A747-192486D14D4A}"
)
ID3D11AuthenticatedChannel._iid_ = IID_ID3D11AuthenticatedChannel


ID3D11AuthenticatedChannel._methods_ = [
    COMMETHOD(
        [helpstring('Method GetCertificateSize')],
        HRESULT,
        'GetCertificateSize',
        (['out'], POINTER(UINT), 'pCertificateSize'),
    ),
    COMMETHOD(
        [helpstring('Method GetCertificate')],
        HRESULT,
        'GetCertificate',
        (['in'], UINT, 'CertificateSize'),
        (['out'], POINTER(BYTE), 'pCertificate'),
    ),
    COMMETHOD(
        [helpstring('Method GetChannelHandle')],
        VOID,
        'GetChannelHandle',
        (['out'], POINTER(HANDLE), 'pChannelHandle'),
    ),
]


D3D11_AUTHENTICATED_QUERY_PROTECTION = GUID('{A84EB584-C495-48AA-B94D-8BD2D6FBCE05}')
D3D11_AUTHENTICATED_QUERY_CHANNEL_TYPE = GUID('{BC1B18A5-B1FB-42AB-BD94-B5828B4BF7BE}')
D3D11_AUTHENTICATED_QUERY_DEVICE_HANDLE = GUID('{EC1C539D-8CFF-4E2A-BCC4-F5692F99F480}')
D3D11_AUTHENTICATED_QUERY_CRYPTO_SESSION = GUID('{2634499E-D018-4D74-AC17-7F724059528D}')
D3D11_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_COUNT = GUID('{0DB207B3-9450-46A6-82DE-1B96D44F9CF2}')
D3D11_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS = GUID('{649BBADB-F0F4-4639-A15B-24393FC3ABAC}')
D3D11_AUTHENTICATED_QUERY_UNRESTRICTED_PROTECTED_SHARED_RESOURCE_COUNT = GUID('{012F0BD6-E662-4474-BEFD-AA53E5143C6D}')
D3D11_AUTHENTICATED_QUERY_OUTPUT_ID_COUNT = GUID('{2C042B5E-8C07-46D5-AABE-8F75CBAD4C31}')
D3D11_AUTHENTICATED_QUERY_OUTPUT_ID = GUID('{839DDCA3-9B4E-41E4-B053-892BD2A11EE7}')
D3D11_AUTHENTICATED_QUERY_ACCESSIBILITY_ATTRIBUTES = GUID('{6214D9D2-432C-4ABB-9FCE-216EEA269E3B}')
D3D11_AUTHENTICATED_QUERY_ENCRYPTION_WHEN_ACCESSIBLE_GUID_COUNT = GUID('{B30F7066-203C-4B07-93FC-CEAAFD61241E}')
D3D11_AUTHENTICATED_QUERY_ENCRYPTION_WHEN_ACCESSIBLE_GUID = GUID('{F83A5958-E986-4BDA-BEB0-411F6A7A01B7}')
D3D11_AUTHENTICATED_QUERY_CURRENT_ENCRYPTION_WHEN_ACCESSIBLE = GUID('{EC1791C7-DAD3-4F15-9EC3-FAA93D60D4F0}')
D3D11_AUTHENTICATED_CONFIGURE_INITIALIZE = GUID('{06114BDB-3523-470A-8DCA-FBC2845154F0}')
D3D11_AUTHENTICATED_CONFIGURE_PROTECTION = GUID('{50455658-3F47-4362-BF99-BFDFCDE9ED29}')
D3D11_AUTHENTICATED_CONFIGURE_CRYPTO_SESSION = GUID('{6346CC54-2CFC-4AD4-8224-D15837DE7700}')
D3D11_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE = GUID('{0772D047-1B40-48E8-9CA6-B5F510DE9F01}')
D3D11_AUTHENTICATED_CONFIGURE_ENCRYPTION_WHEN_ACCESSIBLE = GUID('{41FFF286-6AE0-4D43-9D55-A46E9EFD158A}')

D3D11_AUTHENTICATED_QUERY_INPUT._fields_ = [
    ('QueryType', GUID),
    ('hChannel', HANDLE),
    ('SequenceNumber', UINT),
]

D3D11_AUTHENTICATED_QUERY_OUTPUT._fields_ = [
    ('omac', D3D11_OMAC),
    ('QueryType', GUID),
    ('hChannel', HANDLE),
    ('SequenceNumber', UINT),
    ('ReturnCode', HRESULT),
]


class __MIDL___MIDL_itf_d3d11_0000_0034_0001(ctypes.Structure):
    pass


__MIDL___MIDL_itf_d3d11_0000_0034_0001._fields_ = [
    ('ProtectionEnabled', UINT, 1),
    ('OverlayOrFullscreenRequired', UINT, 1),
    ('Reserved', UINT, 30),
]
Flags = __MIDL___MIDL_itf_d3d11_0000_0034_0001
D3D11_AUTHENTICATED_PROTECTION_FLAGS.Flags = Flags


D3D11_AUTHENTICATED_PROTECTION_FLAGS._fields_ = [
    ('Flags', D3D11_AUTHENTICATED_PROTECTION_FLAGS.Flags),
    ('Value', UINT),
]

D3D11_AUTHENTICATED_QUERY_PROTECTION_OUTPUT._fields_ = [
    ('Output', D3D11_AUTHENTICATED_QUERY_OUTPUT),
    ('ProtectionFlags', D3D11_AUTHENTICATED_PROTECTION_FLAGS),
]

D3D11_AUTHENTICATED_QUERY_CHANNEL_TYPE_OUTPUT._fields_ = [
    ('Output', D3D11_AUTHENTICATED_QUERY_OUTPUT),
    ('ChannelType', D3D11_AUTHENTICATED_CHANNEL_TYPE),
]

D3D11_AUTHENTICATED_QUERY_DEVICE_HANDLE_OUTPUT._fields_ = [
    ('Output', D3D11_AUTHENTICATED_QUERY_OUTPUT),
    ('DeviceHandle', HANDLE),
]

D3D11_AUTHENTICATED_QUERY_CRYPTO_SESSION_INPUT._fields_ = [
    ('Input', D3D11_AUTHENTICATED_QUERY_INPUT),
    ('DecoderHandle', HANDLE),
]

D3D11_AUTHENTICATED_QUERY_CRYPTO_SESSION_OUTPUT._fields_ = [
    ('Output', D3D11_AUTHENTICATED_QUERY_OUTPUT),
    ('DecoderHandle', HANDLE),
    ('CryptoSessionHandle', HANDLE),
    ('DeviceHandle', HANDLE),
]

D3D11_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_COUNT_OUTPUT._fields_ = [
    ('Output', D3D11_AUTHENTICATED_QUERY_OUTPUT),
    ('RestrictedSharedResourceProcessCount', UINT),
]

D3D11_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_INPUT._fields_ = [
    ('Input', D3D11_AUTHENTICATED_QUERY_INPUT),
    ('ProcessIndex', UINT),
]


class D3D11_AUTHENTICATED_PROCESS_IDENTIFIER_TYPE(ENUM):
    D3D11_PROCESSIDTYPE_UNKNOWN = 0
    D3D11_PROCESSIDTYPE_DWM = 1
    D3D11_PROCESSIDTYPE_HANDLE = 2

D3D11_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_OUTPUT._fields_ = [
    ('Output', D3D11_AUTHENTICATED_QUERY_OUTPUT),
    ('ProcessIndex', UINT),
    ('ProcessIdentifier', D3D11_AUTHENTICATED_PROCESS_IDENTIFIER_TYPE),
    ('ProcessHandle', HANDLE),
]

D3D11_AUTHENTICATED_QUERY_UNRESTRICTED_PROTECTED_SHARED_RESOURCE_COUNT_OUTPUT._fields_ = [
    ('Output', D3D11_AUTHENTICATED_QUERY_OUTPUT),
    ('UnrestrictedProtectedSharedResourceCount', UINT),
]

D3D11_AUTHENTICATED_QUERY_OUTPUT_ID_COUNT_INPUT._fields_ = [
    ('Input', D3D11_AUTHENTICATED_QUERY_INPUT),
    ('DeviceHandle', HANDLE),
    ('CryptoSessionHandle', HANDLE),
]

D3D11_AUTHENTICATED_QUERY_OUTPUT_ID_COUNT_OUTPUT._fields_ = [
    ('Output', D3D11_AUTHENTICATED_QUERY_OUTPUT),
    ('DeviceHandle', HANDLE),
    ('CryptoSessionHandle', HANDLE),
    ('OutputIDCount', UINT),
]

D3D11_AUTHENTICATED_QUERY_OUTPUT_ID_INPUT._fields_ = [
    ('Input', D3D11_AUTHENTICATED_QUERY_INPUT),
    ('DeviceHandle', HANDLE),
    ('CryptoSessionHandle', HANDLE),
    ('OutputIDIndex', UINT),
]

D3D11_AUTHENTICATED_QUERY_OUTPUT_ID_OUTPUT._fields_ = [
    ('Output', D3D11_AUTHENTICATED_QUERY_OUTPUT),
    ('DeviceHandle', HANDLE),
    ('CryptoSessionHandle', HANDLE),
    ('OutputIDIndex', UINT),
    ('OutputID', UINT64),
]


class D3D11_BUS_TYPE(ENUM):
    D3D11_BUS_TYPE_OTHER = 0
    D3D11_BUS_TYPE_PCI = 0x1
    D3D11_BUS_TYPE_PCIX = 0x2
    D3D11_BUS_TYPE_PCIEXPRESS = 0x3
    D3D11_BUS_TYPE_AGP = 0x4
    D3D11_BUS_IMPL_MODIFIER_INSIDE_OF_CHIPSET = 0x10000
    D3D11_BUS_IMPL_MODIFIER_TRACKS_ON_MOTHER_BOARD_TO_CHIP = 0x20000
    D3D11_BUS_IMPL_MODIFIER_TRACKS_ON_MOTHER_BOARD_TO_SOCKET = 0x30000
    D3D11_BUS_IMPL_MODIFIER_DAUGHTER_BOARD_CONNECTOR = 0x40000
    D3D11_BUS_IMPL_MODIFIER_DAUGHTER_BOARD_CONNECTOR_INSIDE_OF_NUAE = (
        0x50000
    )
    D3D11_BUS_IMPL_MODIFIER_NON_STANDARD = 0x80000000

D3D11_AUTHENTICATED_QUERY_ACESSIBILITY_OUTPUT._fields_ = [
    ('Output', D3D11_AUTHENTICATED_QUERY_OUTPUT),
    ('BusType', D3D11_BUS_TYPE),
    ('AccessibleInContiguousBlocks', BOOL),
    ('AccessibleInNonContiguousBlocks', BOOL),
]

D3D11_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_COUNT_OUTPUT._fields_ = [
    ('Output', D3D11_AUTHENTICATED_QUERY_OUTPUT),
    ('EncryptionGuidCount', UINT),
]

D3D11_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_INPUT._fields_ = [
    ('Input', D3D11_AUTHENTICATED_QUERY_INPUT),
    ('EncryptionGuidIndex', UINT),
]

D3D11_AUTHENTICATED_QUERY_ACCESSIBILITY_ENCRYPTION_GUID_OUTPUT._fields_ = [
    ('Output', D3D11_AUTHENTICATED_QUERY_OUTPUT),
    ('EncryptionGuidIndex', UINT),
    ('EncryptionGuid', GUID),
]

D3D11_AUTHENTICATED_QUERY_CURRENT_ACCESSIBILITY_ENCRYPTION_OUTPUT._fields_ = [
    ('Output', D3D11_AUTHENTICATED_QUERY_OUTPUT),
    ('EncryptionGuid', GUID),
]

D3D11_AUTHENTICATED_CONFIGURE_INPUT._fields_ = [
    ('omac', D3D11_OMAC),
    ('ConfigureType', GUID),
    ('hChannel', HANDLE),
    ('SequenceNumber', UINT),
]

D3D11_AUTHENTICATED_CONFIGURE_OUTPUT._fields_ = [
    ('omac', D3D11_OMAC),
    ('ConfigureType', GUID),
    ('hChannel', HANDLE),
    ('SequenceNumber', UINT),
    ('ReturnCode', HRESULT),
]

D3D11_AUTHENTICATED_CONFIGURE_INITIALIZE_INPUT._fields_ = [
    ('Parameters', D3D11_AUTHENTICATED_CONFIGURE_INPUT),
    ('StartSequenceQuery', UINT),
    ('StartSequenceConfigure', UINT),
]

D3D11_AUTHENTICATED_CONFIGURE_PROTECTION_INPUT._fields_ = [
    ('Parameters', D3D11_AUTHENTICATED_CONFIGURE_INPUT),
    ('Protections', D3D11_AUTHENTICATED_PROTECTION_FLAGS),
]

D3D11_AUTHENTICATED_CONFIGURE_CRYPTO_SESSION_INPUT._fields_ = [
    ('Parameters', D3D11_AUTHENTICATED_CONFIGURE_INPUT),
    ('DecoderHandle', HANDLE),
    ('CryptoSessionHandle', HANDLE),
    ('DeviceHandle', HANDLE),
]

D3D11_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE_INPUT._fields_ = [
    ('Parameters', D3D11_AUTHENTICATED_CONFIGURE_INPUT),
    ('ProcessType', D3D11_AUTHENTICATED_PROCESS_IDENTIFIER_TYPE),
    ('ProcessHandle', HANDLE),
    ('AllowAccess', BOOL),
]

D3D11_AUTHENTICATED_CONFIGURE_ACCESSIBLE_ENCRYPTION_INPUT._fields_ = [
    ('Parameters', D3D11_AUTHENTICATED_CONFIGURE_INPUT),
    ('EncryptionGuid', GUID),
]

D3D11_KEY_EXCHANGE_RSAES_OAEP = GUID('{C1949895-D72A-4A1D-8E5D-ED857D171520}')


IID_ID3D11CryptoSession = MIDL_INTERFACE(
    "{9B32F9AD-BDCC-40A6-A39D-D5C865845720}"
)
ID3D11CryptoSession._iid_ = IID_ID3D11CryptoSession


ID3D11CryptoSession._methods_ = [
    COMMETHOD(
        [helpstring('Method GetCryptoType')],
        VOID,
        'GetCryptoType',
        (['out'], POINTER(GUID), 'pCryptoType'),
    ),
    COMMETHOD(
        [helpstring('Method GetDecoderProfile')],
        VOID,
        'GetDecoderProfile',
        (['out'], POINTER(GUID), 'pDecoderProfile'),
    ),
    COMMETHOD(
        [helpstring('Method GetCertificateSize')],
        HRESULT,
        'GetCertificateSize',
        (['out'], POINTER(UINT), 'pCertificateSize'),
    ),
    COMMETHOD(
        [helpstring('Method GetCertificate')],
        HRESULT,
        'GetCertificate',
        (['in'], UINT, 'CertificateSize'),
        (['out'], POINTER(BYTE), 'pCertificate'),
    ),
    COMMETHOD(
        [helpstring('Method GetCryptoSessionHandle')],
        VOID,
        'GetCryptoSessionHandle',
        (['out'], POINTER(HANDLE), 'pCryptoSessionHandle'),
    ),
]

class D3D11_VDOV_DIMENSION(ENUM):
    D3D11_VDOV_DIMENSION_UNKNOWN = 0
    D3D11_VDOV_DIMENSION_TEXTURE2D = 1

D3D11_TEX2D_VDOV._fields_ = [
    ('ArraySlice', UINT),
]


class _Union_10(ctypes.Union):
    pass


_Union_10._fields_ = [
    ('Texture2D', D3D11_TEX2D_VDOV),
]
D3D11_VIDEO_DECODER_OUTPUT_VIEW_DESC._Union_10 = _Union_10

D3D11_VIDEO_DECODER_OUTPUT_VIEW_DESC._anonymous_ = (
    '_Union_10',
)

D3D11_VIDEO_DECODER_OUTPUT_VIEW_DESC._fields_ = [
    ('DecodeProfile', GUID),
    ('ViewDimension', D3D11_VDOV_DIMENSION),
    ('_Union_10', D3D11_VIDEO_DECODER_OUTPUT_VIEW_DESC._Union_10),
]

IID_ID3D11VideoDecoderOutputView = MIDL_INTERFACE(
    "{C2931AEA-2A85-4F20-860F-FBA1FD256E18}"
)
ID3D11VideoDecoderOutputView._iid_ = IID_ID3D11VideoDecoderOutputView


ID3D11VideoDecoderOutputView._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (
            ['out'],
            POINTER(D3D11_VIDEO_DECODER_OUTPUT_VIEW_DESC),
            'pDesc'
        ),
    ),
]

class D3D11_VPIV_DIMENSION(ENUM):
    D3D11_VPIV_DIMENSION_UNKNOWN = 0
    D3D11_VPIV_DIMENSION_TEXTURE2D = 1

D3D11_TEX2D_VPIV._fields_ = [
    ('MipSlice', UINT),
    ('ArraySlice', UINT),
]


class _Union_11(ctypes.Union):
    pass


_Union_11._fields_ = [
    ('Texture2D', D3D11_TEX2D_VPIV),
]
D3D11_VIDEO_PROCESSOR_INPUT_VIEW_DESC._Union_11 = _Union_11

D3D11_VIDEO_PROCESSOR_INPUT_VIEW_DESC._anonymous_ = (
    '_Union_11',
)

D3D11_VIDEO_PROCESSOR_INPUT_VIEW_DESC._fields_ = [
    ('FourCC', UINT),
    ('ViewDimension', D3D11_VPIV_DIMENSION),
    ('_Union_11', D3D11_VIDEO_PROCESSOR_INPUT_VIEW_DESC._Union_11),
]

IID_ID3D11VideoProcessorInputView = MIDL_INTERFACE(
    "{11EC5A5F-51DC-4945-AB34-6E8C21300EA5}"
)
ID3D11VideoProcessorInputView._iid_ = IID_ID3D11VideoProcessorInputView


ID3D11VideoProcessorInputView._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (
            ['out'],
            POINTER(D3D11_VIDEO_PROCESSOR_INPUT_VIEW_DESC),
            'pDesc'
        ),
    ),
]

class D3D11_VPOV_DIMENSION(ENUM):
    D3D11_VPOV_DIMENSION_UNKNOWN = 0
    D3D11_VPOV_DIMENSION_TEXTURE2D = 1
    D3D11_VPOV_DIMENSION_TEXTURE2DARRAY = 2

D3D11_TEX2D_VPOV._fields_ = [
    ('MipSlice', UINT),
]

D3D11_TEX2D_ARRAY_VPOV._fields_ = [
    ('MipSlice', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]


class _Union_12(ctypes.Union):
    pass


_Union_12._fields_ = [
    ('Texture2D', D3D11_TEX2D_VPOV),
    ('Texture2DArray', D3D11_TEX2D_ARRAY_VPOV),
]
D3D11_VIDEO_PROCESSOR_OUTPUT_VIEW_DESC._Union_12 = _Union_12

D3D11_VIDEO_PROCESSOR_OUTPUT_VIEW_DESC._anonymous_ = (
    '_Union_12',
)

D3D11_VIDEO_PROCESSOR_OUTPUT_VIEW_DESC._fields_ = [
    ('ViewDimension', D3D11_VPOV_DIMENSION),
    ('_Union_12', D3D11_VIDEO_PROCESSOR_OUTPUT_VIEW_DESC._Union_12),
]


IID_ID3D11VideoProcessorOutputView = MIDL_INTERFACE(
    "{A048285E-25A9-4527-BD93-D68B68C44254}"
)
ID3D11VideoProcessorOutputView._iid_ = IID_ID3D11VideoProcessorOutputView


ID3D11VideoProcessorOutputView._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (
            ['out'],
            POINTER(D3D11_VIDEO_PROCESSOR_OUTPUT_VIEW_DESC),
            'pDesc'
        ),
    ),
]

IID_ID3D11VideoContext = MIDL_INTERFACE(
    "{61F21C45-3C0E-4A74-9CEA-67100D9AD5E4}"
)
ID3D11VideoContext._iid_ = IID_ID3D11VideoContext


ID3D11VideoContext._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDecoderBuffer')],
        HRESULT,
        'GetDecoderBuffer',
        (['in'], POINTER(ID3D11VideoDecoder), 'pDecoder'),
        ([], D3D11_VIDEO_DECODER_BUFFER_TYPE, 'Type'),
        (['out'], POINTER(UINT), 'pBufferSize'),
        (['out'], POINTER(POINTER(VOID)), 'ppBuffer'),
    ),
    COMMETHOD(
        [helpstring('Method ReleaseDecoderBuffer')],
        HRESULT,
        'ReleaseDecoderBuffer',
        (['in'], POINTER(ID3D11VideoDecoder), 'pDecoder'),
        (['in'], D3D11_VIDEO_DECODER_BUFFER_TYPE, 'Type'),
    ),
    COMMETHOD(
        [helpstring('Method DecoderBeginFrame')],
        HRESULT,
        'DecoderBeginFrame',
        (['in'], POINTER(ID3D11VideoDecoder), 'pDecoder'),
        (
            ['in'],
            POINTER(ID3D11VideoDecoderOutputView),
            'pView'
        ),
        ([], UINT, 'ContentKeySize'),
        (['in'], POINTER(VOID), 'pContentKey'),
    ),
    COMMETHOD(
        [helpstring('Method DecoderEndFrame')],
        HRESULT,
        'DecoderEndFrame',
        (['in'], POINTER(ID3D11VideoDecoder), 'pDecoder'),
    ),
    COMMETHOD(
        [helpstring('Method SubmitDecoderBuffers')],
        HRESULT,
        'SubmitDecoderBuffers',
        (['in'], POINTER(ID3D11VideoDecoder), 'pDecoder'),
        (['in'], UINT, 'NumBuffers'),
        (
            ['in'],
            POINTER(D3D11_VIDEO_DECODER_BUFFER_DESC),
            'pBufferDesc'
        ),
    ),
    COMMETHOD(
        [helpstring('Method DecoderExtension')],
        APP_DEPRECATED_HRESULT,
        'DecoderExtension',
        (['in'], POINTER(ID3D11VideoDecoder), 'pDecoder'),
        (
            ['in'],
            POINTER(D3D11_VIDEO_DECODER_EXTENSION),
            'pExtensionData'
        ),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetOutputTargetRect')],
        VOID,
        'VideoProcessorSetOutputTargetRect',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], BOOL, 'Enable'),
        (['in'], POINTER(RECT), 'pRect'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetOutputBackgroundColor')],
        VOID,
        'VideoProcessorSetOutputBackgroundColor',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], BOOL, 'YCbCr'),
        (['in'], POINTER(D3D11_VIDEO_COLOR), 'pColor'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetOutputColorSpace')],
        VOID,
        'VideoProcessorSetOutputColorSpace',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (
            ['in'],
            POINTER(D3D11_VIDEO_PROCESSOR_COLOR_SPACE),
            'pColorSpace'
        ),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetOutputAlphaFillMode')],
        VOID,
        'VideoProcessorSetOutputAlphaFillMode',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (
            ['in'],
            D3D11_VIDEO_PROCESSOR_ALPHA_FILL_MODE,
            'AlphaFillMode'
        ),
        (['in'], UINT, 'StreamIndex'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetOutputConstriction')],
        VOID,
        'VideoProcessorSetOutputConstriction',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], BOOL, 'Enable'),
        (['in'], SIZE, 'Size'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetOutputStereoMode')],
        VOID,
        'VideoProcessorSetOutputStereoMode',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], BOOL, 'Enable'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetOutputExtension')],
        APP_DEPRECATED_HRESULT,
        'VideoProcessorSetOutputExtension',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], POINTER(GUID), 'pExtensionGuid'),
        (['in'], UINT, 'DataSize'),
        (['in'], POINTER(VOID), 'pData'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetOutputTargetRect')],
        VOID,
        'VideoProcessorGetOutputTargetRect',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['out'], POINTER(BOOL), 'Enabled'),
        (['out'], POINTER(RECT), 'pRect'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetOutputBackgroundColor')],
        VOID,
        'VideoProcessorGetOutputBackgroundColor',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['out'], POINTER(BOOL), 'pYCbCr'),
        (['out'], POINTER(D3D11_VIDEO_COLOR), 'pColor'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetOutputColorSpace')],
        VOID,
        'VideoProcessorGetOutputColorSpace',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (
            ['out'],
            POINTER(D3D11_VIDEO_PROCESSOR_COLOR_SPACE),
            'pColorSpace'
        ),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetOutputAlphaFillMode')],
        VOID,
        'VideoProcessorGetOutputAlphaFillMode',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (
            ['out'],
            POINTER(D3D11_VIDEO_PROCESSOR_ALPHA_FILL_MODE),
            'pAlphaFillMode'
        ),
        (['out'], POINTER(UINT), 'pStreamIndex'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetOutputConstriction')],
        VOID,
        'VideoProcessorGetOutputConstriction',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['out'], POINTER(BOOL), 'pEnabled'),
        (['out'], POINTER(SIZE), 'pSize'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetOutputStereoMode')],
        VOID,
        'VideoProcessorGetOutputStereoMode',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['out'], POINTER(BOOL), 'pEnabled'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetOutputExtension')],
        APP_DEPRECATED_HRESULT,
        'VideoProcessorGetOutputExtension',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], POINTER(GUID), 'pExtensionGuid'),
        (['in'], UINT, 'DataSize'),
        (['out'], POINTER(VOID), 'pData'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetStreamFrameFormat')],
        VOID,
        'VideoProcessorSetStreamFrameFormat',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['in'], D3D11_VIDEO_FRAME_FORMAT, 'FrameFormat'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetStreamColorSpace')],
        VOID,
        'VideoProcessorSetStreamColorSpace',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (
            ['in'],
            POINTER(D3D11_VIDEO_PROCESSOR_COLOR_SPACE),
            'pColorSpace'
        ),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetStreamOutputRate')],
        VOID,
        'VideoProcessorSetStreamOutputRate',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (
            ['in'],
            D3D11_VIDEO_PROCESSOR_OUTPUT_RATE,
            'OutputRate'
        ),
        (['in'], BOOL, 'RepeatFrame'),
        (['in'], POINTER(DXGI_RATIONAL), 'pCustomRate'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetStreamSourceRect')],
        VOID,
        'VideoProcessorSetStreamSourceRect',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['in'], BOOL, 'Enable'),
        (['in'], POINTER(RECT), 'pRect'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetStreamDestRect')],
        VOID,
        'VideoProcessorSetStreamDestRect',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['in'], BOOL, 'Enable'),
        (['in'], POINTER(RECT), 'pRect'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetStreamAlpha')],
        VOID,
        'VideoProcessorSetStreamAlpha',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['in'], BOOL, 'Enable'),
        (['in'], FLOAT, 'Alpha'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetStreamPalette')],
        VOID,
        'VideoProcessorSetStreamPalette',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['in'], UINT, 'Count'),
        (['in'], POINTER(UINT), 'pEntries'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetStreamPixelAspectRatio')],
        VOID,
        'VideoProcessorSetStreamPixelAspectRatio',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['in'], BOOL, 'Enable'),
        (
            ['in'],
            POINTER(DXGI_RATIONAL),
            'pSourceAspectRatio'
        ),
        (
            ['in'],
            POINTER(DXGI_RATIONAL),
            'pDestinationAspectRatio'
        ),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetStreamLumaKey')],
        VOID,
        'VideoProcessorSetStreamLumaKey',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['in'], BOOL, 'Enable'),
        (['in'], FLOAT, 'Lower'),
        (['in'], FLOAT, 'Upper'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetStreamStereoFormat')],
        VOID,
        'VideoProcessorSetStreamStereoFormat',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['in'], BOOL, 'Enable'),
        (
            ['in'],
            D3D11_VIDEO_PROCESSOR_STEREO_FORMAT,
            'Format'
        ),
        (['in'], BOOL, 'LeftViewFrame0'),
        (['in'], BOOL, 'BaseViewFrame0'),
        (
            ['in'],
            D3D11_VIDEO_PROCESSOR_STEREO_FLIP_MODE,
            'FlipMode'
        ),
        (['in'], INT, 'MonoOffset'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetStreamAutoProcessingMode')],
        VOID,
        'VideoProcessorSetStreamAutoProcessingMode',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['in'], BOOL, 'Enable'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetStreamFilter')],
        VOID,
        'VideoProcessorSetStreamFilter',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['in'], D3D11_VIDEO_PROCESSOR_FILTER, 'Filter'),
        (['in'], BOOL, 'Enable'),
        (['in'], INT, 'Level'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetStreamExtension')],
        APP_DEPRECATED_HRESULT,
        'VideoProcessorSetStreamExtension',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['in'], POINTER(GUID), 'pExtensionGuid'),
        (['in'], UINT, 'DataSize'),
        (['in'], POINTER(VOID), 'pData'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetStreamFrameFormat')],
        VOID,
        'VideoProcessorGetStreamFrameFormat',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (
            ['out'],
            POINTER(D3D11_VIDEO_FRAME_FORMAT),
            'pFrameFormat'
        ),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetStreamColorSpace')],
        VOID,
        'VideoProcessorGetStreamColorSpace',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (
            ['out'],
            POINTER(D3D11_VIDEO_PROCESSOR_COLOR_SPACE),
            'pColorSpace'
        ),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetStreamOutputRate')],
        VOID,
        'VideoProcessorGetStreamOutputRate',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (
            ['out'],
            POINTER(D3D11_VIDEO_PROCESSOR_OUTPUT_RATE),
            'pOutputRate'
        ),
        (['out'], POINTER(BOOL), 'pRepeatFrame'),
        (['out'], POINTER(DXGI_RATIONAL), 'pCustomRate'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetStreamSourceRect')],
        VOID,
        'VideoProcessorGetStreamSourceRect',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['out'], POINTER(BOOL), 'pEnabled'),
        (['out'], POINTER(RECT), 'pRect'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetStreamDestRect')],
        VOID,
        'VideoProcessorGetStreamDestRect',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['out'], POINTER(BOOL), 'pEnabled'),
        (['out'], POINTER(RECT), 'pRect'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetStreamAlpha')],
        VOID,
        'VideoProcessorGetStreamAlpha',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['out'], POINTER(BOOL), 'pEnabled'),
        (['out'], POINTER(FLOAT), 'pAlpha'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetStreamPalette')],
        VOID,
        'VideoProcessorGetStreamPalette',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['in'], UINT, 'Count'),
        (['out'], POINTER(UINT), 'pEntries'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetStreamPixelAspectRatio')],
        VOID,
        'VideoProcessorGetStreamPixelAspectRatio',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['out'], POINTER(BOOL), 'pEnabled'),
        (
            ['out'],
            POINTER(DXGI_RATIONAL),
            'pSourceAspectRatio'
        ),
        (
            ['out'],
            POINTER(DXGI_RATIONAL),
            'pDestinationAspectRatio'
        ),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetStreamLumaKey')],
        VOID,
        'VideoProcessorGetStreamLumaKey',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['out'], POINTER(BOOL), 'pEnabled'),
        (['out'], POINTER(FLOAT), 'pLower'),
        (['out'], POINTER(FLOAT), 'pUpper'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetStreamStereoFormat')],
        VOID,
        'VideoProcessorGetStreamStereoFormat',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['out'], POINTER(BOOL), 'pEnable'),
        (
            ['out'],
            POINTER(D3D11_VIDEO_PROCESSOR_STEREO_FORMAT),
            'pFormat'
        ),
        (['out'], POINTER(BOOL), 'pLeftViewFrame0'),
        (['out'], POINTER(BOOL), 'pBaseViewFrame0'),
        (
            ['out'],
            POINTER(D3D11_VIDEO_PROCESSOR_STEREO_FLIP_MODE),
            'pFlipMode'
        ),
        (['out'], POINTER(INT), 'MonoOffset'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetStreamAutoProcessingMode')],
        VOID,
        'VideoProcessorGetStreamAutoProcessingMode',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['out'], POINTER(BOOL), 'pEnabled'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetStreamFilter')],
        VOID,
        'VideoProcessorGetStreamFilter',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['in'], D3D11_VIDEO_PROCESSOR_FILTER, 'Filter'),
        (['out'], POINTER(BOOL), 'pEnabled'),
        (['out'], POINTER(INT), 'pLevel'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetStreamExtension')],
        APP_DEPRECATED_HRESULT,
        'VideoProcessorGetStreamExtension',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['in'], POINTER(GUID), 'pExtensionGuid'),
        (['in'], UINT, 'DataSize'),
        (['out'], POINTER(VOID), 'pData'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorBlt')],
        HRESULT,
        'VideoProcessorBlt',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (
            ['in'],
            POINTER(ID3D11VideoProcessorOutputView),
            'pView'
        ),
        (['in'], UINT, 'OutputFrame'),
        (['in'], UINT, 'StreamCount'),
        (
            ['in'],
            POINTER(D3D11_VIDEO_PROCESSOR_STREAM),
            'pStreams'
        ),
    ),
    COMMETHOD(
        [helpstring('Method NegotiateCryptoSessionKeyExchange')],
        HRESULT,
        'NegotiateCryptoSessionKeyExchange',
        (
            ['in'],
            POINTER(ID3D11CryptoSession),
            'pCryptoSession'
        ),
        (['in'], UINT, 'DataSize'),
        (['out', 'in'], POINTER(VOID), 'pData'),
    ),
    COMMETHOD(
        [helpstring('Method EncryptionBlt')],
        VOID,
        'EncryptionBlt',
        (
            ['in'],
            POINTER(ID3D11CryptoSession),
            'pCryptoSession'
        ),
        (['in'], POINTER(ID3D11Texture2D), 'pSrcSurface'),
        (['in'], POINTER(ID3D11Texture2D), 'pDstSurface'),
        (['in'], UINT, 'IVSize'),
        (['out', 'in'], POINTER(VOID), 'pIV'),
    ),
    COMMETHOD(
        [helpstring('Method DecryptionBlt')],
        VOID,
        'DecryptionBlt',
        (
            ['in'],
            POINTER(ID3D11CryptoSession),
            'pCryptoSession'
        ),
        (['in'], POINTER(ID3D11Texture2D), 'pSrcSurface'),
        (['in'], POINTER(ID3D11Texture2D), 'pDstSurface'),
        (
            ['in'],
            POINTER(D3D11_ENCRYPTED_BLOCK_INFO),
            'pEncryptedBlockInfo'
        ),
        (['in'], UINT, 'ContentKeySize'),
        (['in'], POINTER(VOID), 'pContentKey'),
        (['in'], UINT, 'IVSize'),
        (['out', 'in'], POINTER(VOID), 'pIV'),
    ),
    COMMETHOD(
        [helpstring('Method StartSessionKeyRefresh')],
        VOID,
        'StartSessionKeyRefresh',
        (
            ['in'],
            POINTER(ID3D11CryptoSession),
            'pCryptoSession'
        ),
        (['in'], UINT, 'RandomNumberSize'),
        (['out'], POINTER(VOID), 'pRandomNumber'),
    ),
    COMMETHOD(
        [helpstring('Method FinishSessionKeyRefresh')],
        VOID,
        'FinishSessionKeyRefresh',
        (
            ['in'],
            POINTER(ID3D11CryptoSession),
            'pCryptoSession'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetEncryptionBltKey')],
        HRESULT,
        'GetEncryptionBltKey',
        (
            ['in'],
            POINTER(ID3D11CryptoSession),
            'pCryptoSession'
        ),
        (['in'], UINT, 'KeySize'),
        (['out'], POINTER(VOID), 'pReadbackKey'),
    ),
    COMMETHOD(
        [helpstring('Method NegotiateAuthenticatedChannelKeyExchange')],
        HRESULT,
        'NegotiateAuthenticatedChannelKeyExchange',
        (
            ['in'],
            POINTER(ID3D11AuthenticatedChannel),
            'pChannel'
        ),
        (['in'], UINT, 'DataSize'),
        (['out', 'in'], POINTER(VOID), 'pData'),
    ),
    COMMETHOD(
        [helpstring('Method QueryAuthenticatedChannel')],
        HRESULT,
        'QueryAuthenticatedChannel',
        (
            ['in'],
            POINTER(ID3D11AuthenticatedChannel),
            'pChannel'
        ),
        (['in'], UINT, 'InputSize'),
        (['in'], POINTER(VOID), 'pInput'),
        (['in'], UINT, 'OutputSize'),
        (['out'], POINTER(VOID), 'pOutput'),
    ),
    COMMETHOD(
        [helpstring('Method ConfigureAuthenticatedChannel')],
        HRESULT,
        'ConfigureAuthenticatedChannel',
        (
            ['in'],
            POINTER(ID3D11AuthenticatedChannel),
            'pChannel'
        ),
        (['in'], UINT, 'InputSize'),
        (['in'], POINTER(VOID), 'pInput'),
        (
            ['out'],
            POINTER(D3D11_AUTHENTICATED_CONFIGURE_OUTPUT),
            'pOutput'
        ),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetStreamRotation')],
        VOID,
        'VideoProcessorSetStreamRotation',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['in'], BOOL, 'Enable'),
        (['in'], D3D11_VIDEO_PROCESSOR_ROTATION, 'Rotation'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetStreamRotation')],
        VOID,
        'VideoProcessorGetStreamRotation',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['out'], POINTER(BOOL), 'pEnable'),
        (
            ['out'],
            POINTER(D3D11_VIDEO_PROCESSOR_ROTATION),
            'pRotation'
        ),
    ),
]

IID_ID3D11VideoDevice = MIDL_INTERFACE(
    "{10EC4D5B-975A-4689-B9E4-D0AAC30FE333}"
)
ID3D11VideoDevice._iid_ = IID_ID3D11VideoDevice


ID3D11VideoDevice._methods_ = [
    COMMETHOD(
        [helpstring('Method CreateVideoDecoder')],
        HRESULT,
        'CreateVideoDecoder',
        (
            ['in'],
            POINTER(D3D11_VIDEO_DECODER_DESC),
            'pVideoDesc'
        ),
        (
            ['in'],
            POINTER(D3D11_VIDEO_DECODER_CONFIG),
            'pConfig'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11VideoDecoder)),
            'ppDecoder'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateVideoProcessor')],
        HRESULT,
        'CreateVideoProcessor',
        (
            ['in'],
            POINTER(ID3D11VideoProcessorEnumerator),
            'pEnum'
        ),
        (['in'], UINT, 'RateConversionIndex'),
        (
            ['out'],
            POINTER(POINTER(ID3D11VideoProcessor)),
            'ppVideoProcessor'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateAuthenticatedChannel')],
        HRESULT,
        'CreateAuthenticatedChannel',
        (
            ['in'],
            D3D11_AUTHENTICATED_CHANNEL_TYPE,
            'ChannelType'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11AuthenticatedChannel)),
            'ppAuthenticatedChannel'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateCryptoSession')],
        HRESULT,
        'CreateCryptoSession',
        (['in'], POINTER(GUID), 'pCryptoType'),
        (['in'], POINTER(GUID), 'pDecoderProfile'),
        (['in'], POINTER(GUID), 'pKeyExchangeType'),
        (
            ['out'],
            POINTER(POINTER(ID3D11CryptoSession)),
            'ppCryptoSession'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateVideoDecoderOutputView')],
        HRESULT,
        'CreateVideoDecoderOutputView',
        (['in'], POINTER(ID3D11Resource), 'pResource'),
        (
            ['in'],
            POINTER(D3D11_VIDEO_DECODER_OUTPUT_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11VideoDecoderOutputView)),
            'ppVDOVView'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateVideoProcessorInputView')],
        HRESULT,
        'CreateVideoProcessorInputView',
        (['in'], POINTER(ID3D11Resource), 'pResource'),
        (
            ['in'],
            POINTER(ID3D11VideoProcessorEnumerator),
            'pEnum'
        ),
        (
            ['in'],
            POINTER(D3D11_VIDEO_PROCESSOR_INPUT_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11VideoProcessorInputView)),
            'ppVPIView'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateVideoProcessorOutputView')],
        HRESULT,
        'CreateVideoProcessorOutputView',
        (['in'], POINTER(ID3D11Resource), 'pResource'),
        (
            ['in'],
            POINTER(ID3D11VideoProcessorEnumerator),
            'pEnum'
        ),
        (
            ['in'],
            POINTER(D3D11_VIDEO_PROCESSOR_OUTPUT_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11VideoProcessorOutputView)),
            'ppVPOView'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateVideoProcessorEnumerator')],
        HRESULT,
        'CreateVideoProcessorEnumerator',
        (
            ['in'],
            POINTER(D3D11_VIDEO_PROCESSOR_CONTENT_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11VideoProcessorEnumerator)),
            'ppEnum'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetVideoDecoderProfileCount')],
        UINT,
        'GetVideoDecoderProfileCount',
    ),
    COMMETHOD(
        [helpstring('Method GetVideoDecoderProfile')],
        HRESULT,
        'GetVideoDecoderProfile',
        (['in'], UINT, 'Index'),
        (['out'], POINTER(GUID), 'pDecoderProfile'),
    ),
    COMMETHOD(
        [helpstring('Method CheckVideoDecoderFormat')],
        HRESULT,
        'CheckVideoDecoderFormat',
        (['in'], POINTER(GUID), 'pDecoderProfile'),
        (['in'], DXGI_FORMAT, 'Format'),
        (['out'], POINTER(BOOL), 'pSupported'),
    ),
    COMMETHOD(
        [helpstring('Method GetVideoDecoderConfigCount')],
        HRESULT,
        'GetVideoDecoderConfigCount',
        (['in'], POINTER(D3D11_VIDEO_DECODER_DESC), 'pDesc'),
        (['out'], POINTER(UINT), 'pCount'),
    ),
    COMMETHOD(
        [helpstring('Method GetVideoDecoderConfig')],
        HRESULT,
        'GetVideoDecoderConfig',
        (['in'], POINTER(D3D11_VIDEO_DECODER_DESC), 'pDesc'),
        (['in'], UINT, 'Index'),
        (
            ['out'],
            POINTER(D3D11_VIDEO_DECODER_CONFIG),
            'pConfig'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetContentProtectionCaps')],
        HRESULT,
        'GetContentProtectionCaps',
        (['in'], POINTER(GUID), 'pCryptoType'),
        (['in'], POINTER(GUID), 'pDecoderProfile'),
        (
            ['out'],
            POINTER(D3D11_VIDEO_CONTENT_PROTECTION_CAPS),
            'pCaps'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CheckCryptoKeyExchange')],
        HRESULT,
        'CheckCryptoKeyExchange',
        (['in'], POINTER(GUID), 'pCryptoType'),
        (['in'], POINTER(GUID), 'pDecoderProfile'),
        (['in'], UINT, 'Index'),
        (['out'], POINTER(GUID), 'pKeyExchangeType'),
    ),
    COMMETHOD(
        [helpstring('Method SetPrivateData')],
        HRESULT,
        'SetPrivateData',
        (['in'], REFGUID, 'guid'),
        (['in'], UINT, 'DataSize'),
        (['in'], POINTER(VOID), 'pData'),
    ),
    COMMETHOD(
        [helpstring('Method SetPrivateDataInterface')],
        HRESULT,
        'SetPrivateDataInterface',
        (['in'], REFGUID, 'guid'),
        (['in'], POINTER(comtypes.IUnknown), 'pData'),
    ),
]

IID_ID3D11Device = MIDL_INTERFACE(
    "{DB6F6DDB-AC77-4E88-8253-819DF9BBF140}"
)
ID3D11Device._iid_ = IID_ID3D11Device


ID3D11Device._methods_ = [
    COMMETHOD(
        [helpstring('Method CreateBuffer')],
        HRESULT,
        'CreateBuffer',
        (['in'], POINTER(D3D11_BUFFER_DESC), 'pDesc'),
        (
            ['in'],
            POINTER(D3D11_SUBRESOURCE_DATA),
            'pInitialData'
        ),
        (['out'], POINTER(POINTER(ID3D11Buffer)), 'ppBuffer'),
    ),
    COMMETHOD(
        [helpstring('Method CreateTexture1D')],
        HRESULT,
        'CreateTexture1D',
        (['in'], POINTER(D3D11_TEXTURE1D_DESC), 'pDesc'),
        (
            ['in'],
            POINTER(D3D11_SUBRESOURCE_DATA),
            'pInitialData'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11Texture1D)),
            'ppTexture1D'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateTexture2D')],
        HRESULT,
        'CreateTexture2D',
        (['in'], POINTER(D3D11_TEXTURE2D_DESC), 'pDesc'),
        (
            ['in'],
            POINTER(D3D11_SUBRESOURCE_DATA),
            'pInitialData'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11Texture2D)),
            'ppTexture2D'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateTexture3D')],
        HRESULT,
        'CreateTexture3D',
        (['in'], POINTER(D3D11_TEXTURE3D_DESC), 'pDesc'),
        (
            ['in'],
            POINTER(D3D11_SUBRESOURCE_DATA),
            'pInitialData'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11Texture3D)),
            'ppTexture3D'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateShaderResourceView')],
        HRESULT,
        'CreateShaderResourceView',
        (['in'], POINTER(ID3D11Resource), 'pResource'),
        (
            ['in'],
            POINTER(D3D11_SHADER_RESOURCE_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11ShaderResourceView)),
            'ppSRView'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateUnorderedAccessView')],
        HRESULT,
        'CreateUnorderedAccessView',
        (['in'], POINTER(ID3D11Resource), 'pResource'),
        (
            ['in'],
            POINTER(D3D11_UNORDERED_ACCESS_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11UnorderedAccessView)),
            'ppUAView'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateRenderTargetView')],
        HRESULT,
        'CreateRenderTargetView',
        (['in'], POINTER(ID3D11Resource), 'pResource'),
        (
            ['in'],
            POINTER(D3D11_RENDER_TARGET_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11RenderTargetView)),
            'ppRTView'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateDepthStencilView')],
        HRESULT,
        'CreateDepthStencilView',
        (['in'], POINTER(ID3D11Resource), 'pResource'),
        (
            ['in'],
            POINTER(D3D11_DEPTH_STENCIL_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11DepthStencilView)),
            'ppDepthStencilView'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateInputLayout')],
        HRESULT,
        'CreateInputLayout',
        (
            ['in'],
            POINTER(D3D11_INPUT_ELEMENT_DESC),
            'pInputElementDescs'
        ),
        (['in'], UINT, 'NumElements'),
        (
            ['in'],
            POINTER(VOID),
            'pShaderBytecodeWithInputSignature'
        ),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['out'],
            POINTER(POINTER(ID3D11InputLayout)),
            'ppInputLayout'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateVertexShader')],
        HRESULT,
        'CreateVertexShader',
        (['in'], POINTER(VOID), 'pShaderBytecode'),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11VertexShader)),
            'ppVertexShader'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateGeometryShader')],
        HRESULT,
        'CreateGeometryShader',
        (['in'], POINTER(VOID), 'pShaderBytecode'),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11GeometryShader)),
            'ppGeometryShader'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateGeometryShaderWithStreamOutput')],
        HRESULT,
        'CreateGeometryShaderWithStreamOutput',
        (['in'], POINTER(VOID), 'pShaderBytecode'),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(D3D11_SO_DECLARATION_ENTRY),
            'pSODeclaration'
        ),
        (['in'], UINT, 'NumEntries'),
        (['in'], POINTER(UINT), 'pBufferStrides'),
        (['in'], UINT, 'NumStrides'),
        (['in'], UINT, 'RasterizedStream'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11GeometryShader)),
            'ppGeometryShader'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreatePixelShader')],
        HRESULT,
        'CreatePixelShader',
        (['in'], POINTER(VOID), 'pShaderBytecode'),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11PixelShader)),
            'ppPixelShader'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateHullShader')],
        HRESULT,
        'CreateHullShader',
        (['in'], POINTER(VOID), 'pShaderBytecode'),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11HullShader)),
            'ppHullShader'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateDomainShader')],
        HRESULT,
        'CreateDomainShader',
        (['in'], POINTER(VOID), 'pShaderBytecode'),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11DomainShader)),
            'ppDomainShader'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateComputeShader')],
        HRESULT,
        'CreateComputeShader',
        (['in'], POINTER(VOID), 'pShaderBytecode'),
        (['in'], SIZE_T, 'BytecodeLength'),
        (
            ['in'],
            POINTER(ID3D11ClassLinkage),
            'pClassLinkage'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11ComputeShader)),
            'ppComputeShader'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateClassLinkage')],
        HRESULT,
        'CreateClassLinkage',
        (
            ['out'],
            POINTER(POINTER(ID3D11ClassLinkage)),
            'ppLinkage'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateBlendState')],
        HRESULT,
        'CreateBlendState',
        (
            ['in'],
            POINTER(D3D11_BLEND_DESC),
            'pBlendStateDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11BlendState)),
            'ppBlendState'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateDepthStencilState')],
        HRESULT,
        'CreateDepthStencilState',
        (
            ['in'],
            POINTER(D3D11_DEPTH_STENCIL_DESC),
            'pDepthStencilDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11DepthStencilState)),
            'ppDepthStencilState'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateRasterizerState')],
        HRESULT,
        'CreateRasterizerState',
        (
            ['in'],
            POINTER(D3D11_RASTERIZER_DESC),
            'pRasterizerDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11RasterizerState)),
            'ppRasterizerState'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateSamplerState')],
        HRESULT,
        'CreateSamplerState',
        (['in'], POINTER(D3D11_SAMPLER_DESC), 'pSamplerDesc'),
        (
            ['out'],
            POINTER(POINTER(ID3D11SamplerState)),
            'ppSamplerState'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateQuery')],
        HRESULT,
        'CreateQuery',
        (['in'], POINTER(D3D11_QUERY_DESC), 'pQueryDesc'),
        (['out'], POINTER(POINTER(ID3D11Query)), 'ppQuery'),
    ),
    COMMETHOD(
        [helpstring('Method CreatePredicate')],
        HRESULT,
        'CreatePredicate',
        (['in'], POINTER(D3D11_QUERY_DESC), 'pPredicateDesc'),
        (
            ['out'],
            POINTER(POINTER(ID3D11Predicate)),
            'ppPredicate'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateCounter')],
        HRESULT,
        'CreateCounter',
        (['in'], POINTER(D3D11_COUNTER_DESC), 'pCounterDesc'),
        (
            ['out'],
            POINTER(POINTER(ID3D11Counter)),
            'ppCounter'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateDeferredContext')],
        HRESULT,
        'CreateDeferredContext',
        ([], UINT, 'ContextFlags'),
        (
            ['out'],
            POINTER(POINTER(ID3D11DeviceContext)),
            'ppDeferredContext'
        ),
    ),
    COMMETHOD(
        [helpstring('Method OpenSharedResource')],
        HRESULT,
        'OpenSharedResource',
        (['in'], HANDLE, 'hResource'),
        (['in'], REFIID, 'ReturnedInterface'),
        (['out'], POINTER(POINTER(VOID)), 'ppResource'),
    ),
    COMMETHOD(
        [helpstring('Method CheckFormatSupport')],
        HRESULT,
        'CheckFormatSupport',
        (['in'], DXGI_FORMAT, 'Format'),
        (['out'], POINTER(UINT), 'pFormatSupport'),
    ),
    COMMETHOD(
        [helpstring('Method CheckMultisampleQualityLevels')],
        HRESULT,
        'CheckMultisampleQualityLevels',
        (['in'], DXGI_FORMAT, 'Format'),
        (['in'], UINT, 'SampleCount'),
        (['out'], POINTER(UINT), 'pNumQualityLevels'),
    ),
    COMMETHOD(
        [helpstring('Method CheckCounterInfo')],
        VOID,
        'CheckCounterInfo',
        (
            ['out'],
            POINTER(D3D11_COUNTER_INFO),
            'pCounterInfo'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CheckCounter')],
        HRESULT,
        'CheckCounter',
        (['in'], POINTER(D3D11_COUNTER_DESC), 'pDesc'),
        (['out'], POINTER(D3D11_COUNTER_TYPE), 'pType'),
        (['out'], POINTER(UINT), 'pActiveCounters'),
        (['out'], LPSTR, 'szName'),
        (['out', 'in'], POINTER(UINT), 'pNameLength'),
        (['out'], LPSTR, 'szUnits'),
        (['out', 'in'], POINTER(UINT), 'pUnitsLength'),
        (['out'], LPSTR, 'szDescription'),
        (['out', 'in'], POINTER(UINT), 'pDescriptionLength'),
    ),
    COMMETHOD(
        [helpstring('Method CheckFeatureSupport')],
        HRESULT,
        'CheckFeatureSupport',
        ([], D3D11_FEATURE, 'Feature'),
        (['out'], POINTER(VOID), 'pFeatureSupportData'),
        ([], UINT, 'FeatureSupportDataSize'),
    ),
    COMMETHOD(
        [helpstring('Method GetPrivateData')],
        HRESULT,
        'GetPrivateData',
        (['in'], REFGUID, 'guid'),
        (['out', 'in'], POINTER(UINT), 'pDataSize'),
        (['out'], POINTER(VOID), 'pData'),
    ),
    COMMETHOD(
        [helpstring('Method SetPrivateData')],
        HRESULT,
        'SetPrivateData',
        (['in'], REFGUID, 'guid'),
        (['in'], UINT, 'DataSize'),
        (['in'], POINTER(VOID), 'pData'),
    ),
    COMMETHOD(
        [helpstring('Method SetPrivateDataInterface')],
        HRESULT,
        'SetPrivateDataInterface',
        (['in'], REFGUID, 'guid'),
        (['in'], POINTER(comtypes.IUnknown), 'pData'),
    ),
    COMMETHOD(
        [helpstring('Method GetFeatureLevel')],
        D3D_FEATURE_LEVEL,
        'GetFeatureLevel',
    ),
    COMMETHOD(
        [helpstring('Method GetCreationFlags')],
        UINT,
        'GetCreationFlags',
    ),
    COMMETHOD(
        [helpstring('Method GetDeviceRemovedReason')],
        HRESULT,
        'GetDeviceRemovedReason',
    ),
    COMMETHOD(
        [helpstring('Method GetImmediateContext')],
        VOID,
        'GetImmediateContext',
        (
            ['out'],
            POINTER(POINTER(ID3D11DeviceContext)),
            'ppImmediateContext'
        ),
    ),
    COMMETHOD(
        [helpstring('Method SetExceptionMode')],
        HRESULT,
        'SetExceptionMode',
        ([], UINT, 'RaiseFlags'),
    ),
    COMMETHOD(
        [helpstring('Method GetExceptionMode')],
        UINT,
        'GetExceptionMode',
    ),
]

class D3D11_CREATE_DEVICE_FLAG(ENUM):
    D3D11_CREATE_DEVICE_SINGLETHREADED = 0x1
    D3D11_CREATE_DEVICE_DEBUG = 0x2
    D3D11_CREATE_DEVICE_SWITCH_TO_REF = 0x4
    D3D11_CREATE_DEVICE_PREVENT_INTERNAL_THREADING_OPTIMIZATIONS = 0x8
    D3D11_CREATE_DEVICE_BGRA_SUPPORT = 0x20
    D3D11_CREATE_DEVICE_DEBUGGABLE = 0x40
    D3D11_CREATE_DEVICE_PREVENT_ALTERING_LAYER_SETTINGS_FROM_REGISTRY = (
        0x80
    )
    D3D11_CREATE_DEVICE_DISABLE_GPU_TIMEOUT = 0x100
    D3D11_CREATE_DEVICE_VIDEO_SUPPORT = 0x800

from .d3d11sdklayers_h import * # NOQA
from .d3d10_1_h import * # NOQA

from .d3d10shader_h import * # NOQA
from .d3d10_1shader_h import * # NOQA
from .d3d10misc_h import * # NOQA
from .d3d10effect_h import * # NOQA
    

# ///////////////////////////////////////////////////////////////
# D3D11CreateDevice
# ------------------
# pAdapter
# If NULL, D3D11CreateDevice will choose the primary adapter and
# create a new instance from a temporarily created IDXGIFactory.
# If non-NULL, D3D11CreateDevice will register the appropriate
# device, if necessary (via IDXGIAdapter::RegisterDrver), before
# creating the device.
# DriverType
# Specifies the driver type to be created: hardware, reference or
# null.
# Software
# HMODULE of a DLL implementing a software rasterizer. Must be NULL for
# non-Software driver types.
# Flags
# Any of those documented for D3D11CreateDeviceAndSwapChain.
# pFeatureLevels
# Any of those documented for D3D11CreateDeviceAndSwapChain.
# FeatureLevels
# Size of feature levels array.
# SDKVersion
# SDK version. Use the D3D11_SDK_VERSION macro.
# ppDevice
# Pointer to returned interface. May be NULL.
# pFeatureLevel
# Pointer to returned feature level. May be NULL.
# ppImmediateContext
# Pointer to returned interface. May be NULL.
# Return Values
# Any of those documented for
# CreateDXGIFactory1
# IDXGIFactory::EnumAdapters
# IDXGIAdapter::RegisterDriver
# D3D11CreateDevice
# ///////////////////////////////////////////////////////////////
# HRESULT (WINAPI* PFN_D3D11_CREATE_DEVICE)(
# _In_opt_ IDXGIAdapter*, 
# D3D_DRIVER_TYPE, 
# HMODULE, 
# UINT, 
# _In_reads_opt_( FeatureLevels ) CONST D3D_FEATURE_LEVEL*,
# UINT FeatureLevels, 
# UINT, 
# _COM_Outptr_opt_ ID3D11Device**, 
# _Out_opt_ D3D_FEATURE_LEVEL*, 
# _COM_Outptr_opt_ ID3D11DeviceContext** 
# );
PFN_D3D11_CREATE_DEVICE = ctypes.WINFUNCTYPE(
    HRESULT,
    POINTER(IDXGIAdapter),
    D3D_DRIVER_TYPE,
    HMODULE,
    UINT,
    POINTER(D3D_FEATURE_LEVEL),
    UINT,
    UINT,
    POINTER(POINTER(ID3D11Device)),
    POINTER(D3D_FEATURE_LEVEL),
    POINTER(POINTER(ID3D11DeviceContext)),
)

# ///////////////////////////////////////////////////////////
# D3D11CreateDeviceAndSwapChain
# ------------------------------
# ppAdapter
# If NULL, D3D11CreateDevice will choose the primary adapter and
# create a new instance from a temporarily created IDXGIFactory.
# If non-NULL, D3D11CreateDevice will register the appropriate
# device, if necessary (via IDXGIAdapter::RegisterDrver), before
# creating the device.
# DriverType
# Specifies the driver type to be created: hardware, reference or
# null.
# Software
# HMODULE of a DLL implementing a software rasterizer. Must be
# NULL for
# non-Software driver types.
# Flags
# Any of those documented for D3D11CreateDevice.
# pFeatureLevels
# Array of any of the following:
# D3D_FEATURE_LEVEL_11_0
# D3D_FEATURE_LEVEL_10_1
# D3D_FEATURE_LEVEL_10_0
# D3D_FEATURE_LEVEL_9_3
# D3D_FEATURE_LEVEL_9_2
# D3D_FEATURE_LEVEL_9_1
# Order indicates sequence in which instantiation will be
# attempted. If
# NULL, then the implied order is the same as previously listed
# (i.e.
# prefer most features available).
# FeatureLevels
# Size of feature levels array.
# SDKVersion
# SDK version. Use the D3D11_SDK_VERSION macro.
# pSwapChainDesc
# Swap chain description, may be NULL.
# ppSwapChain
# Pointer to returned interface. May be NULL.
# ppDevice
# Pointer to returned interface. May be NULL.
# pFeatureLevel
# Pointer to returned feature level. May be NULL.
# ppImmediateContext
# Pointer to returned interface. May be NULL.
# Return Values
# Any of those documented for
# CreateDXGIFactory1
# IDXGIFactory::EnumAdapters
# IDXGIAdapter::RegisterDriver
# D3D11CreateDevice
# IDXGIFactory::CreateSwapChain
# ///////////////////////////////////////////////////////////
# HRESULT (WINAPI* PFN_D3D11_CREATE_DEVICE_AND_SWAP_CHAIN)(
# _In_opt_ IDXGIAdapter*, 
# D3D_DRIVER_TYPE,
# HMODULE, UINT, 
# _In_reads_opt_( FeatureLevels ) CONST D3D_FEATURE_LEVEL*,
# UINT FeatureLevels, 
# UINT,
# _In_opt_ CONST DXGI_SWAP_CHAIN_DESC*,
# _COM_Outptr_opt_ IDXGISwapChain**, 
# _COM_Outptr_opt_ ID3D11Device**,
# _Out_opt_ D3D_FEATURE_LEVEL*,
# _COM_Outptr_opt_ ID3D11DeviceContext** 
# );
PFN_D3D11_CREATE_DEVICE_AND_SWAP_CHAIN = ctypes.WINFUNCTYPE(
    HRESULT,
    POINTER(IDXGIAdapter),
    D3D_DRIVER_TYPE,
    HMODULE,
    UINT,
    POINTER(D3D_FEATURE_LEVEL),
    UINT,
    UINT,
    POINTER(DXGI_SWAP_CHAIN_DESC),
    POINTER(POINTER(IDXGISwapChain)),
    POINTER(POINTER(ID3D11Device)),
    POINTER(D3D_FEATURE_LEVEL),
    POINTER(POINTER(ID3D11DeviceContext)),
)
IID_ID3D11DeviceChild = GUID('{1841E5C8-16B0-489B-BCC8-44CFB0D5DEAE}')

IID_ID3D11DepthStencilState = GUID('{03823EFB-8D8F-4E1C-9AA2-F64BB2CBFDF1}')

IID_ID3D11BlendState = GUID('{75B68FAA-347D-4159-8F45-A0640F01CD9A}')

IID_ID3D11RasterizerState = GUID('{9BB4AB81-AB1A-4D8F-B506-FC04200B6EE7}')

IID_ID3D11Resource = GUID('{DC8E63F3-D12B-4952-B47B-5E45026A862D}')

IID_ID3D11Buffer = GUID('{48570B85-D1EE-4FCD-A250-EB350722B037}')

IID_ID3D11Texture1D = GUID('{F8FB5C27-C6B3-4F75-A4C8-439AF2EF564C}')

IID_ID3D11Texture2D = GUID('{6F15AAF2-D208-4E89-9AB4-489535D34F9C}')

IID_ID3D11Texture3D = GUID('{037E866E-F56D-4357-A8AF-9DABBE6E250E}')

IID_ID3D11View = GUID('{839D1216-BB2E-412B-B7F4-A9DBEBE08ED1}')

IID_ID3D11ShaderResourceView = GUID('{B0E06FE0-8192-4E1A-B1CA-36D7414710B2}')

IID_ID3D11RenderTargetView = GUID('{DFDBA067-0B8D-4865-875B-D7B4516CC164}')

IID_ID3D11DepthStencilView = GUID('{9FDAC92A-1876-48C3-AFAD-25B94F84A9B6}')

IID_ID3D11UnorderedAccessView = GUID('{28ACF509-7F5C-48F6-8611-F316010A6380}')

IID_ID3D11VertexShader = GUID('{3B301D64-D678-4289-8897-22F8928B72F3}')

IID_ID3D11HullShader = GUID('{8E5C6061-628A-4C8E-8264-BBE45CB3D5DD}')

IID_ID3D11DomainShader = GUID('{F582C508-0F36-490C-9977-31EECE268CFA}')

IID_ID3D11GeometryShader = GUID('{38325B96-EFFB-4022-BA02-2E795B70275C}')

IID_ID3D11PixelShader = GUID('{EA82E40D-51DC-4F33-93D4-DB7C9125AE8C}')

IID_ID3D11ComputeShader = GUID('{4F5B196E-C2BD-495E-BD01-1FDED38E4969}')

IID_ID3D11InputLayout = GUID('{E4819DDC-4CF0-4025-BD26-5DE82A3E07B7}')

IID_ID3D11SamplerState = GUID('{DA6FEA51-564C-4487-9810-F0D0F9B4E3A5}')

IID_ID3D11Asynchronous = GUID('{4B35D0CD-1E15-4258-9C98-1B1333F6DD3B}')

IID_ID3D11Query = GUID('{D6C00747-87B7-425E-B84D-44D108560AFD}')

IID_ID3D11Predicate = GUID('{9EB576DD-9F77-4D86-81AA-8BAB5FE490E2}')

IID_ID3D11Counter = GUID('{6E8C49FB-A371-4770-B440-29086022B741}')

IID_ID3D11ClassInstance = GUID('{A6CD7FAA-B0B7-4A2F-9436-8662A65797CB}')

IID_ID3D11ClassLinkage = GUID('{DDF57CBA-9543-46E4-A12B-F207A0FE7FED}')

IID_ID3D11CommandList = GUID('{A24BC4D1-769E-43F7-8013-98FF566C18E2}')

IID_ID3D11DeviceContext = GUID('{C0BFA96C-E089-44FB-8EAF-26F8796190DA}')

IID_ID3D11VideoDecoder = GUID('{3C9C5B51-995D-48D1-9B8D-FA5CAEDED65C}')

IID_ID3D11VideoProcessorEnumerator = GUID('{31627037-53AB-4200-9061-05FAA9AB45F9}')

IID_ID3D11VideoProcessor = GUID('{1D7B0652-185F-41C6-85CE-0C5BE3D4AE6C}')

IID_ID3D11AuthenticatedChannel = GUID('{3015A308-DCBD-47AA-A747-192486D14D4A}')

IID_ID3D11CryptoSession = GUID('{9B32F9AD-BDCC-40A6-A39D-D5C865845720}')

IID_ID3D11VideoDecoderOutputView = GUID('{C2931AEA-2A85-4F20-860F-FBA1FD256E18}')

IID_ID3D11VideoProcessorInputView = GUID('{11EC5A5F-51DC-4945-AB34-6E8C21300EA5}')

IID_ID3D11VideoProcessorOutputView = GUID('{A048285E-25A9-4527-BD93-D68B68C44254}')

IID_ID3D11VideoContext = GUID('{61F21C45-3C0E-4A74-9CEA-67100D9AD5E4}')

IID_ID3D11VideoDevice = GUID('{10EC4D5B-975A-4689-B9E4-D0AAC30FE333}')

IID_ID3D11Device = GUID('{DB6F6DDB-AC77-4E88-8253-819DF9BBF140}')
