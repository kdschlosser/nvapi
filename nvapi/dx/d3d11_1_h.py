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
    LPCWSTR,
    DWORD
)

UINT8 = ctypes.c_uint8
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

from dxgi_format_h import *
from dxgicommon_h import *


class ENUM(INT):
    pass


class ID3D11BlendState1(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = None


class D3D11_RENDER_TARGET_BLEND_DESC1(ctypes.Structure):
    pass


class D3D11_BLEND_DESC1(ctypes.Structure):
    pass


class D3D11_RASTERIZER_DESC1(ctypes.Structure):
    pass


class D3D11_VIDEO_DECODER_SUB_SAMPLE_MAPPING_BLOCK(ctypes.Structure):
    pass


class D3D11_VIDEO_DECODER_BUFFER_DESC1(ctypes.Structure):
    pass


class D3D11_VIDEO_DECODER_BEGIN_FRAME_CRYPTO_SESSION(ctypes.Structure):
    pass


class D3D11_VIDEO_PROCESSOR_STREAM_BEHAVIOR_HINT(ctypes.Structure):
    pass


class D3D11_KEY_EXCHANGE_HW_PROTECTION_INPUT_DATA(ctypes.Structure):
    pass


class D3D11_KEY_EXCHANGE_HW_PROTECTION_OUTPUT_DATA(ctypes.Structure):
    pass


class D3D11_KEY_EXCHANGE_HW_PROTECTION_DATA(ctypes.Structure):
    pass


class D3D11_VIDEO_SAMPLE_DESC(ctypes.Structure):
    pass


from .d3dcommon_h import * # NOQA
from .d3d11_h import * # NOQ


class ID3D11RasterizerState1(ID3D11RasterizerState):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3DDeviceContextState(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11DeviceContext1(ID3D11DeviceContext):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11VideoContext1(ID3D11VideoContext):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11VideoDevice1(ID3D11VideoDevice):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11VideoProcessorEnumerator1(ID3D11VideoProcessorEnumerator):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11Device1(ID3D11Device):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3DUserDefinedAnnotation(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class D3D11_COPY_FLAGS(ENUM):
    D3D11_COPY_NO_OVERWRITE = 0x1
    D3D11_COPY_DISCARD = 0x2


class D3D11_LOGIC_OP(ENUM):
    D3D11_LOGIC_OP_CLEAR = 0
    D3D11_LOGIC_OP_SET = D3D11_LOGIC_OP_CLEAR + 1
    D3D11_LOGIC_OP_COPY = D3D11_LOGIC_OP_SET + 1
    D3D11_LOGIC_OP_COPY_INVERTED = D3D11_LOGIC_OP_COPY + 1
    D3D11_LOGIC_OP_NOOP = D3D11_LOGIC_OP_COPY_INVERTED + 1
    D3D11_LOGIC_OP_INVERT = D3D11_LOGIC_OP_NOOP + 1
    D3D11_LOGIC_OP_AND = D3D11_LOGIC_OP_INVERT + 1
    D3D11_LOGIC_OP_NAND = D3D11_LOGIC_OP_AND + 1
    D3D11_LOGIC_OP_OR = D3D11_LOGIC_OP_NAND + 1
    D3D11_LOGIC_OP_NOR = D3D11_LOGIC_OP_OR + 1
    D3D11_LOGIC_OP_XOR = D3D11_LOGIC_OP_NOR + 1
    D3D11_LOGIC_OP_EQUIV = D3D11_LOGIC_OP_XOR + 1
    D3D11_LOGIC_OP_AND_REVERSE = D3D11_LOGIC_OP_EQUIV + 1
    D3D11_LOGIC_OP_AND_INVERTED = D3D11_LOGIC_OP_AND_REVERSE + 1
    D3D11_LOGIC_OP_OR_REVERSE = D3D11_LOGIC_OP_AND_INVERTED + 1
    D3D11_LOGIC_OP_OR_INVERTED = D3D11_LOGIC_OP_OR_REVERSE + 1


D3D11_RENDER_TARGET_BLEND_DESC1._fields_ = [
    ('BlendEnable', BOOL),
    ('LogicOpEnable', BOOL),
    ('SrcBlend', D3D11_BLEND),
    ('DestBlend', D3D11_BLEND),
    ('BlendOp', D3D11_BLEND_OP),
    ('SrcBlendAlpha', D3D11_BLEND),
    ('DestBlendAlpha', D3D11_BLEND),
    ('BlendOpAlpha', D3D11_BLEND_OP),
    ('LogicOp', D3D11_LOGIC_OP),
    ('RenderTargetWriteMask', UINT8),
]

D3D11_BLEND_DESC1._fields_ = [
    ('AlphaToCoverageEnable', BOOL),
    ('IndependentBlendEnable', BOOL),
    ('RenderTarget', D3D11_RENDER_TARGET_BLEND_DESC1 * 8),
]


CD3D11_BLEND_DESC1 = D3D11_BLEND_DESC1
      
IID_ID3D11BlendState1 = MIDL_INTERFACE(
    "{CC86FABE-DA55-401D-85E7-E3C9DE2877E9}"
)
ID3D11BlendState1._iid_ = IID_ID3D11BlendState1


ID3D11BlendState1._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc1')],
        VOID,
        'GetDesc1',
        (['out'], POINTER(D3D11_BLEND_DESC1), 'pDesc'),
    ),
]

D3D11_RASTERIZER_DESC1._fields_ = [
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
]

CD3D11_RASTERIZER_DESC1 = D3D11_RASTERIZER_DESC1


IID_ID3D11RasterizerState1 = MIDL_INTERFACE(
    "{1217D7A6-5039-418C-B042-9CBE256AFD6E}"
)
ID3D11RasterizerState1._iid_ = IID_ID3D11RasterizerState1


ID3D11RasterizerState1._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc1')],
        VOID,
        'GetDesc1',
        (['out'], POINTER(D3D11_RASTERIZER_DESC1), 'pDesc'),
    ),
]


class D3D11_1_CREATE_DEVICE_CONTEXT_STATE_FLAG(ENUM):
    D3D11_1_CREATE_DEVICE_CONTEXT_STATE_SINGLETHREADED = 0x1


IID_ID3DDeviceContextState = MIDL_INTERFACE(
    "{5C1E0D8A-7C23-48F9-8C59-A92958CEFF11}"
)
ID3DDeviceContextState._iid_ = IID_ID3DDeviceContextState


ID3DDeviceContextState._methods_ = []

IID_ID3D11DeviceContext1 = MIDL_INTERFACE(
    "{BB2C6FAA-B5FB-4082-8E6B-388B8CFA90E1}"
)
ID3D11DeviceContext1._iid_ = IID_ID3D11DeviceContext1


ID3D11DeviceContext1._methods_ = [
    COMMETHOD(
        [helpstring('Method CopySubresourceRegion1')],
        VOID,
        'CopySubresourceRegion1',
        (['in'], POINTER(ID3D11Resource), 'pDstResource'),
        (['in'], UINT, 'DstSubresource'),
        (['in'], UINT, 'DstX'),
        (['in'], UINT, 'DstY'),
        (['in'], UINT, 'DstZ'),
        (['in'], POINTER(ID3D11Resource), 'pSrcResource'),
        (['in'], UINT, 'SrcSubresource'),
        (['in'], POINTER(D3D11_BOX), 'pSrcBox'),
        (['in'], UINT, 'CopyFlags'),
    ),
    COMMETHOD(
        [helpstring('Method UpdateSubresource1')],
        VOID,
        'UpdateSubresource1',
        (['in'], POINTER(ID3D11Resource), 'pDstResource'),
        (['in'], UINT, 'DstSubresource'),
        (['in'], POINTER(D3D11_BOX), 'pDstBox'),
        (['in'], POINTER(VOID), 'pSrcData'),
        (['in'], UINT, 'SrcRowPitch'),
        (['in'], UINT, 'SrcDepthPitch'),
        (['in'], UINT, 'CopyFlags'),
    ),
    COMMETHOD(
        [helpstring('Method DiscardResource')],
        VOID,
        'DiscardResource',
        (['in'], POINTER(ID3D11Resource), 'pResource'),
    ),
    COMMETHOD(
        [helpstring('Method DiscardView')],
        VOID,
        'DiscardView',
        (['in'], POINTER(ID3D11View), 'pResourceView'),
    ),
    COMMETHOD(
        [helpstring('Method VSSetConstantBuffers1')],
        VOID,
        'VSSetConstantBuffers1',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (['in'], POINTER(ID3D11Buffer), 'ppConstantBuffers'),
        (['in'], POINTER(UINT), 'pFirstConstant'),
        (['in'], POINTER(UINT), 'pNumConstants'),
    ),
    COMMETHOD(
        [helpstring('Method HSSetConstantBuffers1')],
        VOID,
        'HSSetConstantBuffers1',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (['in'], POINTER(ID3D11Buffer), 'ppConstantBuffers'),
        (['in'], POINTER(UINT), 'pFirstConstant'),
        (['in'], POINTER(UINT), 'pNumConstants'),
    ),
    COMMETHOD(
        [helpstring('Method DSSetConstantBuffers1')],
        VOID,
        'DSSetConstantBuffers1',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (['in'], POINTER(ID3D11Buffer), 'ppConstantBuffers'),
        (['in'], POINTER(UINT), 'pFirstConstant'),
        (['in'], POINTER(UINT), 'pNumConstants'),
    ),
    COMMETHOD(
        [helpstring('Method GSSetConstantBuffers1')],
        VOID,
        'GSSetConstantBuffers1',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (['in'], POINTER(ID3D11Buffer), 'ppConstantBuffers'),
        (['in'], POINTER(UINT), 'pFirstConstant'),
        (['in'], POINTER(UINT), 'pNumConstants'),
    ),
    COMMETHOD(
        [helpstring('Method PSSetConstantBuffers1')],
        VOID,
        'PSSetConstantBuffers1',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (['in'], POINTER(ID3D11Buffer), 'ppConstantBuffers'),
        (['in'], POINTER(UINT), 'pFirstConstant'),
        (['in'], POINTER(UINT), 'pNumConstants'),
    ),
    COMMETHOD(
        [helpstring('Method CSSetConstantBuffers1')],
        VOID,
        'CSSetConstantBuffers1',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (['in'], POINTER(ID3D11Buffer), 'ppConstantBuffers'),
        (['in'], POINTER(UINT), 'pFirstConstant'),
        (['in'], POINTER(UINT), 'pNumConstants'),
    ),
    COMMETHOD(
        [helpstring('Method VSGetConstantBuffers1')],
        VOID,
        'VSGetConstantBuffers1',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (
            ['out'],
            POINTER(POINTER(ID3D11Buffer)),
            'ppConstantBuffers'
        ),
        (['out'], POINTER(UINT), 'pFirstConstant'),
        (['out'], POINTER(UINT), 'pNumConstants'),
    ),
    COMMETHOD(
        [helpstring('Method HSGetConstantBuffers1')],
        VOID,
        'HSGetConstantBuffers1',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (
            ['out'],
            POINTER(POINTER(ID3D11Buffer)),
            'ppConstantBuffers'
        ),
        (['out'], POINTER(UINT), 'pFirstConstant'),
        (['out'], POINTER(UINT), 'pNumConstants'),
    ),
    COMMETHOD(
        [helpstring('Method DSGetConstantBuffers1')],
        VOID,
        'DSGetConstantBuffers1',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (
            ['out'],
            POINTER(POINTER(ID3D11Buffer)),
            'ppConstantBuffers'
        ),
        (['out'], POINTER(UINT), 'pFirstConstant'),
        (['out'], POINTER(UINT), 'pNumConstants'),
    ),
    COMMETHOD(
        [helpstring('Method GSGetConstantBuffers1')],
        VOID,
        'GSGetConstantBuffers1',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (
            ['out'],
            POINTER(POINTER(ID3D11Buffer)),
            'ppConstantBuffers'
        ),
        (['out'], POINTER(UINT), 'pFirstConstant'),
        (['out'], POINTER(UINT), 'pNumConstants'),
    ),
    COMMETHOD(
        [helpstring('Method PSGetConstantBuffers1')],
        VOID,
        'PSGetConstantBuffers1',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (
            ['out'],
            POINTER(POINTER(ID3D11Buffer)),
            'ppConstantBuffers'
        ),
        (['out'], POINTER(UINT), 'pFirstConstant'),
        (['out'], POINTER(UINT), 'pNumConstants'),
    ),
    COMMETHOD(
        [helpstring('Method CSGetConstantBuffers1')],
        VOID,
        'CSGetConstantBuffers1',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (
            ['out'],
            POINTER(POINTER(ID3D11Buffer)),
            'ppConstantBuffers'
        ),
        (['out'], POINTER(UINT), 'pFirstConstant'),
        (['out'], POINTER(UINT), 'pNumConstants'),
    ),
    COMMETHOD(
        [helpstring('Method SwapDeviceContextState')],
        VOID,
        'SwapDeviceContextState',
        (['in'], POINTER(ID3DDeviceContextState), 'pState'),
        (
            ['out'],
            POINTER(POINTER(ID3DDeviceContextState)),
            'ppPreviousState'
        ),
    ),
    COMMETHOD(
        [helpstring('Method ClearView')],
        VOID,
        'ClearView',
        (['in'], POINTER(ID3D11View), 'pView'),
        (['in'], 4, ']'),
        (['in'], POINTER(D3D11_RECT), 'pRect'),
        ([], UINT, 'NumRects'),
    ),

    COMMETHOD(
        [helpstring('Method DiscardView1')],
        VOID,
        'DiscardView1',
        (['in'], POINTER(ID3D11View), 'pResourceView'),
        (['in'], POINTER(D3D11_RECT), 'pRects'),
        ([], UINT, 'NumRects'),
    ),
]


D3D11_VIDEO_DECODER_SUB_SAMPLE_MAPPING_BLOCK._fields_ = [
    ('ClearSize', UINT),
    ('EncryptedSize', UINT),
]
D3D11_VIDEO_DECODER_BUFFER_DESC1._fields_ = [
    ('BufferType', D3D11_VIDEO_DECODER_BUFFER_TYPE),
    ('DataOffset', UINT),
    ('DataSize', UINT),

    # [annotation]
    ('pIV', POINTER(VOID)),
    ('IVSize', UINT),

    # [annotation]
    ('pSubSampleMappingBlock', POINTER(D3D11_VIDEO_DECODER_SUB_SAMPLE_MAPPING_BLOCK)),
    ('SubSampleMappingCount', UINT),
]
D3D11_VIDEO_DECODER_BEGIN_FRAME_CRYPTO_SESSION._fields_ = [
    ('pCryptoSession', POINTER(ID3D11CryptoSession)),
    ('BlobSize', UINT),

    # [annotation]
    ('pBlob', POINTER(VOID)),
    ('pKeyInfoId', POINTER(GUID)),
    ('PrivateDataSize', UINT),

    # [annotation]
    ('pPrivateData', POINTER(VOID)),
]


class D3D11_VIDEO_DECODER_CAPS(ENUM):
    D3D11_VIDEO_DECODER_CAPS_DOWNSAMPLE = 0x1
    D3D11_VIDEO_DECODER_CAPS_NON_REAL_TIME = 0x2
    D3D11_VIDEO_DECODER_CAPS_DOWNSAMPLE_DYNAMIC = 0x4
    D3D11_VIDEO_DECODER_CAPS_DOWNSAMPLE_REQUIRED = 0x8
    D3D11_VIDEO_DECODER_CAPS_UNSUPPORTED = 0x10


class D3D11_VIDEO_PROCESSOR_BEHAVIOR_HINTS(ENUM):
    D3D11_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_ROTATION = 0x1
    D3D11_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_RESIZE = 0x2
    D3D11_VIDEO_PROCESSOR_BEHAVIOR_HINT_MULTIPLANE_OVERLAY_COLOR_SPACE_CONVERSION = (
        0x4
    )
    D3D11_VIDEO_PROCESSOR_BEHAVIOR_HINT_TRIPLE_BUFFER_OUTPUT = 0x8


D3D11_VIDEO_PROCESSOR_STREAM_BEHAVIOR_HINT._fields_ = [
    ('Enable', BOOL),
    ('Width', UINT),
    ('Height', UINT),
    ('Format', DXGI_FORMAT),
]


class D3D11_CRYPTO_SESSION_STATUS(ENUM):
    D3D11_CRYPTO_SESSION_STATUS_OK = 0
    D3D11_CRYPTO_SESSION_STATUS_KEY_LOST = 1
    D3D11_CRYPTO_SESSION_STATUS_KEY_AND_CONTENT_LOST = 2


D3D11_KEY_EXCHANGE_HW_PROTECTION_INPUT_DATA._fields_ = [
    ('PrivateDataSize', UINT),
    ('HWProtectionDataSize', UINT),
    ('pbInput', BYTE * 4),
]

D3D11_KEY_EXCHANGE_HW_PROTECTION_OUTPUT_DATA._fields_ = [
    ('PrivateDataSize', UINT),
    ('MaxHWProtectionDataSize', UINT),
    ('HWProtectionDataSize', UINT),
    ('TransportTime', UINT64),
    ('ExecutionTime', UINT64),
    ('pbOutput', BYTE * 4),
]

D3D11_KEY_EXCHANGE_HW_PROTECTION_DATA._fields_ = [
    ('HWProtectionFunctionID', UINT),
    ('pInputData', POINTER(D3D11_KEY_EXCHANGE_HW_PROTECTION_INPUT_DATA)),
    ('pOutputData', POINTER(D3D11_KEY_EXCHANGE_HW_PROTECTION_OUTPUT_DATA)),
    ('Status', HRESULT),
]

D3D11_VIDEO_SAMPLE_DESC._fields_ = [
    ('Width', UINT),
    ('Height', UINT),
    ('Format', DXGI_FORMAT),
    ('ColorSpace', DXGI_COLOR_SPACE_TYPE),
]


IID_ID3D11VideoContext1 = MIDL_INTERFACE(
    "{A7F026DA-A5F8-4487-A564-15E34357651E}"
)
ID3D11VideoContext1._iid_ = IID_ID3D11VideoContext1


ID3D11VideoContext1._methods_ = [
    COMMETHOD(
        [helpstring('Method SubmitDecoderBuffers1')],
        HRESULT,
        'SubmitDecoderBuffers1',
        (['in'], POINTER(ID3D11VideoDecoder), 'pDecoder'),
        (['in'], UINT, 'NumBuffers'),
        (
            ['in'],
            POINTER(D3D11_VIDEO_DECODER_BUFFER_DESC1),
            'pBufferDesc'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetDataForNewHardwareKey')],
        HRESULT,
        'GetDataForNewHardwareKey',
        (['in'], POINTER(ID3D11CryptoSession), 'pCryptoSession'),
        (['in'], UINT, 'PrivateInputSize'),
        (['in'], POINTER(VOID), 'pPrivatInputData'),
        (['out'], POINTER(UINT64), 'pPrivateOutputData'),
    ),
    COMMETHOD(
        [helpstring('Method CheckCryptoSessionStatus')],
        HRESULT,
        'CheckCryptoSessionStatus',
        (['in'], POINTER(ID3D11CryptoSession), 'pCryptoSession'),
        (
            ['out'],
            POINTER(D3D11_CRYPTO_SESSION_STATUS),
            'pStatus'
        ),
    ),
    COMMETHOD(
        [helpstring('Method DecoderEnableDownsampling')],
        HRESULT,
        'DecoderEnableDownsampling',
        (['in'], POINTER(ID3D11VideoDecoder), 'pDecoder'),
        (['in'], DXGI_COLOR_SPACE_TYPE, 'InputColorSpace'),
        (['in'], POINTER(D3D11_VIDEO_SAMPLE_DESC), 'pOutputDesc'),
        (['in'], UINT, 'ReferenceFrameCount'),
    ),
    COMMETHOD(
        [helpstring('Method DecoderUpdateDownsampling')],
        HRESULT,
        'DecoderUpdateDownsampling',
        (['in'], POINTER(ID3D11VideoDecoder), 'pDecoder'),
        (['in'], POINTER(D3D11_VIDEO_SAMPLE_DESC), 'pOutputDesc'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetOutputColorSpace1')],
        VOID,
        'VideoProcessorSetOutputColorSpace1',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], DXGI_COLOR_SPACE_TYPE, 'ColorSpace'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetOutputShaderUsage')],
        VOID,
        'VideoProcessorSetOutputShaderUsage',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], BOOL, 'ShaderUsage'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetOutputColorSpace1')],
        VOID,
        'VideoProcessorGetOutputColorSpace1',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['out'], POINTER(DXGI_COLOR_SPACE_TYPE), 'pColorSpace'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetOutputShaderUsage')],
        VOID,
        'VideoProcessorGetOutputShaderUsage',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['out'], POINTER(BOOL), 'pShaderUsage'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetStreamColorSpace1')],
        VOID,
        'VideoProcessorSetStreamColorSpace1',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['in'], DXGI_COLOR_SPACE_TYPE, 'ColorSpace'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetStreamMirror')],
        VOID,
        'VideoProcessorSetStreamMirror',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['in'], BOOL, 'Enable'),
        (['in'], BOOL, 'FlipHorizontal'),
        (['in'], BOOL, 'FlipVertical'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetStreamColorSpace1')],
        VOID,
        'VideoProcessorGetStreamColorSpace1',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['out'], POINTER(DXGI_COLOR_SPACE_TYPE), 'pColorSpace'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetStreamMirror')],
        VOID,
        'VideoProcessorGetStreamMirror',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['out'], POINTER(BOOL), 'pEnable'),
        (['out'], POINTER(BOOL), 'pFlipHorizontal'),
        (['out'], POINTER(BOOL), 'pFlipVertical'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetBehaviorHints')],
        HRESULT,
        'VideoProcessorGetBehaviorHints',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'OutputWidth'),
        (['in'], UINT, 'OutputHeight'),
        (['in'], DXGI_FORMAT, 'OutputFormat'),
        (['in'], UINT, 'StreamCount'),
        (
            ['in'],
            POINTER(D3D11_VIDEO_PROCESSOR_STREAM_BEHAVIOR_HINT),
            'pStreams'
        ),
        (['out'], POINTER(UINT), 'pBehaviorHints'),
    ),
]


IID_ID3D11VideoDevice1 = MIDL_INTERFACE(
    "{29DA1D51-1321-4454-804B-F5FC9F861F0F}"
)
ID3D11VideoDevice1._iid_ = IID_ID3D11VideoDevice1


ID3D11VideoDevice1._methods_ = [
    COMMETHOD(
        [helpstring('Method GetCryptoSessionPrivateDataSize')],
        HRESULT,
        'GetCryptoSessionPrivateDataSize',
        (['in'], POINTER(GUID), 'pCryptoType'),
        (['in'], POINTER(GUID), 'pDecoderProfile'),
        (['in'], POINTER(GUID), 'pKeyExchangeType'),
        (['out'], POINTER(UINT), 'pPrivateInputSize'),
        (['out'], POINTER(UINT), 'pPrivateOutputSize'),
    ),
    COMMETHOD(
        [helpstring('Method GetVideoDecoderCaps')],
        HRESULT,
        'GetVideoDecoderCaps',
        (['in'], POINTER(GUID), 'pDecoderProfile'),
        (['in'], UINT, 'SampleWidth'),
        (['in'], UINT, 'SampleHeight'),
        (['in'], POINTER(DXGI_RATIONAL), 'pFrameRate'),
        (['in'], UINT, 'BitRate'),
        (['in'], POINTER(GUID), 'pCryptoType'),
        (['out'], POINTER(UINT), 'pDecoderCaps'),
    ),
    COMMETHOD(
        [helpstring('Method CheckVideoDecoderDownsampling')],
        HRESULT,
        'CheckVideoDecoderDownsampling',
        (['in'], POINTER(D3D11_VIDEO_DECODER_DESC), 'pInputDesc'),
        (['in'], DXGI_COLOR_SPACE_TYPE, 'InputColorSpace'),
        (
            ['in'],
            POINTER(D3D11_VIDEO_DECODER_CONFIG),
            'pInputConfig'
        ),
        (['in'], POINTER(DXGI_RATIONAL), 'pFrameRate'),
        (['in'], POINTER(D3D11_VIDEO_SAMPLE_DESC), 'pOutputDesc'),
        (['out'], POINTER(BOOL), 'pSupported'),
        (['out'], POINTER(BOOL), 'pRealTimeHint'),
    ),
    COMMETHOD(
        [helpstring('Method RecommendVideoDecoderDownsampleParameters')],
        HRESULT,
        'RecommendVideoDecoderDownsampleParameters',
        (['in'], POINTER(D3D11_VIDEO_DECODER_DESC), 'pInputDesc'),
        (['in'], DXGI_COLOR_SPACE_TYPE, 'InputColorSpace'),
        (
            ['in'],
            POINTER(D3D11_VIDEO_DECODER_CONFIG),
            'pInputConfig'
        ),
        (['in'], POINTER(DXGI_RATIONAL), 'pFrameRate'),
        (
            ['out'],
            POINTER(D3D11_VIDEO_SAMPLE_DESC),
            'pRecommendedOutputDesc'
        ),
    ),
]

IID_ID3D11VideoProcessorEnumerator1 = MIDL_INTERFACE(
    "{465217F2-5568-43CF-B5B9-F61D54531CA1}"
)
ID3D11VideoProcessorEnumerator1._iid_ = IID_ID3D11VideoProcessorEnumerator1


ID3D11VideoProcessorEnumerator1._methods_ = [
    COMMETHOD(
        [helpstring('Method CheckVideoProcessorFormatConversion')],
        HRESULT,
        'CheckVideoProcessorFormatConversion',
        (['in'], DXGI_FORMAT, 'InputFormat'),
        (['in'], DXGI_COLOR_SPACE_TYPE, 'InputColorSpace'),
        (['in'], DXGI_FORMAT, 'OutputFormat'),
        (['in'], DXGI_COLOR_SPACE_TYPE, 'OutputColorSpace'),
        (['out'], POINTER(BOOL), 'pSupported'),
    ),
]


IID_ID3D11Device1 = MIDL_INTERFACE(
    "{A04BFB29-08EF-43D6-A49C-A9BDBDCBE686}"
)
ID3D11Device1._iid_ = IID_ID3D11Device1


ID3D11Device1._methods_ = [
    COMMETHOD(
        [helpstring('Method GetImmediateContext1')],
        VOID,
        'GetImmediateContext1',
        (
            ['out'],
            POINTER(POINTER(ID3D11DeviceContext1)),
            'ppImmediateContext'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateDeferredContext1')],
        HRESULT,
        'CreateDeferredContext1',
        ([], UINT, 'ContextFlags'),
        (
            ['out'],
            POINTER(POINTER(ID3D11DeviceContext1)),
            'ppDeferredContext'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateBlendState1')],
        HRESULT,
        'CreateBlendState1',
        (['in'], POINTER(D3D11_BLEND_DESC1), 'pBlendStateDesc'),
        (
            ['out'],
            POINTER(POINTER(ID3D11BlendState1)),
            'ppBlendState'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateRasterizerState1')],
        HRESULT,
        'CreateRasterizerState1',
        (
            ['in'],
            POINTER(D3D11_RASTERIZER_DESC1),
            'pRasterizerDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D11RasterizerState1)),
            'ppRasterizerState'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateDeviceContextState')],
        HRESULT,
        'CreateDeviceContextState',
        ([], UINT, 'Flags'),
        (['in'], POINTER(D3D_FEATURE_LEVEL), 'pFeatureLevels'),
        ([], UINT, 'FeatureLevels'),
        ([], UINT, 'SDKVersion'),
        ([], REFIID, 'EmulatedInterface'),
        (
            ['out'],
            POINTER(D3D_FEATURE_LEVEL),
            'pChosenFeatureLevel'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3DDeviceContextState)),
            'ppContextState'
        ),
    ),
    COMMETHOD(
        [helpstring('Method OpenSharedResource1')],
        HRESULT,
        'OpenSharedResource1',
        (['in'], HANDLE, 'hResource'),
        (['in'], REFIID, 'returnedInterface'),
        (['out'], POINTER(POINTER(VOID)), 'ppResource'),
    ),
    COMMETHOD(
        [helpstring('Method OpenSharedResourceByName')],
        HRESULT,
        'OpenSharedResourceByName',
        (['in'], LPCWSTR, 'lpName'),
        (['in'], DWORD, 'dwDesiredAccess'),
        (['in'], REFIID, 'returnedInterface'),
        (['out'], POINTER(POINTER(VOID)), 'ppResource'),
    ),
]


IID_ID3DUserDefinedAnnotation = MIDL_INTERFACE(
    "{B2DAAD8B-03D4-4DBF-95EB-32AB4B63D0AB}"
)
ID3DUserDefinedAnnotation._iid_ = IID_ID3DUserDefinedAnnotation


ID3DUserDefinedAnnotation._methods_ = [
    COMMETHOD(
        [helpstring('Method BeginEvent')],
        INT,
        'BeginEvent',
        (['in'], LPCWSTR, 'Name'),
    ),
    COMMETHOD(
        [helpstring('Method EndEvent')],
        INT,
        'EndEvent',
    ),
    COMMETHOD(
        [helpstring('Method SetMarker')],
        VOID,
        'SetMarker',
        (['in'], LPCWSTR, 'Name'),
    ),
    COMMETHOD(
        [helpstring('Method GetStatus')],
        BOOL,
        'GetStatus',
    ),
]


IID_ID3D11BlendState1 = GUID('{CC86FABE-DA55-401D-85E7-E3C9DE2877E9}')
IID_ID3D11RasterizerState1 = GUID('{1217D7A6-5039-418C-B042-9CBE256AFD6E}')
IID_ID3DDeviceContextState = GUID('{5C1E0D8A-7C23-48F9-8C59-A92958CEFF11}')
IID_ID3D11DeviceContext1 = GUID('{BB2C6FAA-B5FB-4082-8E6B-388B8CFA90E1}')
IID_ID3D11VideoContext1 = GUID('{A7F026DA-A5F8-4487-A564-15E34357651E}')
IID_ID3D11VideoDevice1 = GUID('{29DA1D51-1321-4454-804B-F5FC9F861F0F}')
IID_ID3D11VideoProcessorEnumerator1 = GUID('{465217F2-5568-43CF-B5B9-F61D54531CA1}')
IID_ID3D11Device1 = GUID('{A04BFB29-8EF-43D6-A49C-A9BDBDCBE686}')
IID_ID3DUserDefinedAnnotation = GUID('{B2DAAD8B-3D4-4DBF-95EB-32AB4B63D0AB}')
