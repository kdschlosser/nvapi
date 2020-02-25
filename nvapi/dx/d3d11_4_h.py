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


from .dxgi1_5_h import * # NOQA
from .d3dcommon_h import * # NOQA
from .d3d11_3_h import * # NOQA


class D3D11_FEATURE_DATA_VIDEO_DECODER_HISTOGRAM(ctypes.Structure):
    pass


class D3D11_VIDEO_DECODER_BUFFER_DESC2(ctypes.Structure):
    pass


class D3D11_FEATURE_DATA_D3D11_OPTIONS4(ctypes.Structure):
    pass


class ID3D11Device4(ID3D11Device3):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11Device5(ID3D11Device4):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11Multithread(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11VideoContext2(ID3D11VideoContext1):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11VideoDevice2(ID3D11VideoDevice1):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D11VideoContext3(ID3D11VideoContext2):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


IID_ID3D11Device4 = MIDL_INTERFACE(
    "{8992AB71-02E6-4B8D-BA48-B056DCDA42C4}"
)
ID3D11Device4._iid_ = IID_ID3D11Device4


ID3D11Device4._methods_ = [
    COMMETHOD(
        [helpstring('Method RegisterDeviceRemovedEvent')],
        HRESULT,
        'RegisterDeviceRemovedEvent',
        (['in'], HANDLE, 'hEvent'),
        (['out'], POINTER(DWORD), 'pdwCookie'),
    ),
    COMMETHOD(
        [helpstring('Method UnregisterDeviceRemoved')],
        VOID,
        'UnregisterDeviceRemoved',
        (['in'], DWORD, 'dwCookie'),
    ),
]

IID_ID3D11Device5 = MIDL_INTERFACE(
    "{8FFDE202-A0E7-45DF-9E01-E837801B5EA0}"
)
ID3D11Device5._iid_ = IID_ID3D11Device5


ID3D11Device5._methods_ = [
    COMMETHOD(
        [helpstring('Method OpenSharedFence')],
        HRESULT,
        'OpenSharedFence',
        (['in'], HANDLE, 'hFence'),
        (['in'], REFIID, 'ReturnedInterface'),
        (['out'], POINTER(POINTER(VOID)), 'ppFence'),
    ),
    COMMETHOD(
        [helpstring('Method CreateFence')],
        HRESULT,
        'CreateFence',
        (['in'], UINT64, 'InitialValue'),
        (['in'], D3D11_FENCE_FLAG, 'Flags'),
        (['in'], REFIID, 'ReturnedInterface'),
        (['out'], POINTER(POINTER(VOID)), 'ppFence'),
    ),
]

IID_ID3D11Multithread = MIDL_INTERFACE(
    "{9B7E4E00-342C-4106-A19F-4F2704F689F0}"
)
ID3D11Multithread._iid_ = IID_ID3D11Multithread


ID3D11Multithread._methods_ = [
    COMMETHOD(
        [helpstring('Method Enter')],
        VOID,
        'Enter',
    ),
    COMMETHOD(
        [helpstring('Method Leave')],
        VOID,
        'Leave',
    ),
    COMMETHOD(
        [helpstring('Method SetMultithreadProtected')],
        BOOL,
        'SetMultithreadProtected',
        (['in'], BOOL, 'bMTProtect'),
    ),
    COMMETHOD(
        [helpstring('Method GetMultithreadProtected')],
        BOOL,
        'GetMultithreadProtected',
    ),
]

IID_ID3D11VideoContext2 = MIDL_INTERFACE(
    "{C4E7374C-6243-4D1B-AE87-52B4F740E261}"
)
ID3D11VideoContext2._iid_ = IID_ID3D11VideoContext2


ID3D11VideoContext2._methods_ = [
    COMMETHOD(
        [helpstring('Method VideoProcessorSetOutputHDRMetaData')],
        VOID,
        'VideoProcessorSetOutputHDRMetaData',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], DXGI_HDR_METADATA_TYPE, 'Type'),
        (['in'], UINT, 'Size'),
        (['in'], POINTER(VOID), 'pHDRMetaData'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetOutputHDRMetaData')],
        VOID,
        'VideoProcessorGetOutputHDRMetaData',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['out'], POINTER(DXGI_HDR_METADATA_TYPE), 'pType'),
        (['in'], UINT, 'Size'),
        (['out'], POINTER(VOID), 'pMetaData'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorSetStreamHDRMetaData')],
        VOID,
        'VideoProcessorSetStreamHDRMetaData',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['in'], DXGI_HDR_METADATA_TYPE, 'Type'),
        (['in'], UINT, 'Size'),
        (['in'], POINTER(VOID), 'pHDRMetaData'),
    ),
    COMMETHOD(
        [helpstring('Method VideoProcessorGetStreamHDRMetaData')],
        VOID,
        'VideoProcessorGetStreamHDRMetaData',
        (
            ['in'],
            POINTER(ID3D11VideoProcessor),
            'pVideoProcessor'
        ),
        (['in'], UINT, 'StreamIndex'),
        (['out'], POINTER(DXGI_HDR_METADATA_TYPE), 'pType'),
        (['in'], UINT, 'Size'),
        (['out'], POINTER(VOID), 'pMetaData'),
    ),
]


class D3D11_FEATURE_VIDEO(ENUM):
    D3D11_FEATURE_VIDEO_DECODER_HISTOGRAM = 0


class D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT(ENUM):
    D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_Y = 0
    D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_U = 1
    D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_V = 2
    D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_R = 0
    D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_G = 1
    D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_B = 2
    D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_A = 3


class D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_FLAGS(ENUM):
    D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_FLAG_NONE = 0
    D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_FLAG_Y = (
        1 << D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT.D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_Y
    )
    D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_FLAG_U = (
        1 << D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT.D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_U
    )
    D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_FLAG_V = (
        1 << D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT.D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_V
    )
    D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_FLAG_R = (
        1 << D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT.D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_R
    )
    D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_FLAG_G = (
        1 << D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT.D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_G
    )
    D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_FLAG_B = (
        1 << D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT.D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_B
    )
    D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_FLAG_A = (
        1 << D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT.D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_A
    )


D3D11_FEATURE_DATA_VIDEO_DECODER_HISTOGRAM._fields_ = [
    ('DecoderDesc', D3D11_VIDEO_DECODER_DESC),
    ('Components', D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT_FLAGS),
    ('BinCount', UINT),
    ('CounterBitDepth', UINT),
]


class D3D11_CRYPTO_SESSION_KEY_EXCHANGE_FLAGS(ENUM):
    D3D11_CRYPTO_SESSION_KEY_EXCHANGE_FLAG_NONE = 0


IID_ID3D11VideoDevice2 = MIDL_INTERFACE(
    "{59C0CB01-35F0-4A70-8F67-87905C906A53}"
)
ID3D11VideoDevice2._iid_ = IID_ID3D11VideoDevice2


ID3D11VideoDevice2._methods_ = [
    COMMETHOD(
        [helpstring('Method CheckFeatureSupport')],
        HRESULT,
        'CheckFeatureSupport',
        ([], D3D11_FEATURE_VIDEO, 'Feature'),
        (['out'], POINTER(VOID), 'pFeatureSupportData'),
        ([], UINT, 'FeatureSupportDataSize'),
    ),
    COMMETHOD(
        [helpstring('Method NegotiateCryptoSessionKeyExchangeMT')],
        HRESULT,
        'NegotiateCryptoSessionKeyExchangeMT',
        (
            ['in'],
            POINTER(ID3D11CryptoSession),
            'pCryptoSession'
        ),
        (
            ['in'],
            D3D11_CRYPTO_SESSION_KEY_EXCHANGE_FLAGS,
            'flags'
        ),
        (['in'], UINT, 'DataSize'),
        (['out', 'in'], POINTER(VOID), 'pData'),
    ),
]

D3D11_VIDEO_DECODER_BUFFER_DESC2._fields_ = [
    ('BufferType', D3D11_VIDEO_DECODER_BUFFER_TYPE),
    ('DataOffset', UINT),
    ('DataSize', UINT),
    # [annotation]
    ('pIV', POINTER(VOID)),
    ('IVSize', UINT),
    # [annotation]
    ('pSubSampleMappingBlock', POINTER(D3D11_VIDEO_DECODER_SUB_SAMPLE_MAPPING_BLOCK)),
    ('SubSampleMappingCount', UINT),
    ('cBlocksStripeEncrypted', UINT),
    ('cBlocksStripeClear', UINT),
]


IID_ID3D11VideoContext3 = MIDL_INTERFACE(
    "{A9E2FAA0-CB39-418F-A0B7-D8AAD4DE672E}"
)
ID3D11VideoContext3._iid_ = IID_ID3D11VideoContext3


ID3D11VideoContext3._methods_ = [
    COMMETHOD(
        [helpstring('Method DecoderBeginFrame1')],
        HRESULT,
        'DecoderBeginFrame1',
        (['in'], POINTER(ID3D11VideoDecoder), 'pDecoder'),
        (
            ['in'],
            POINTER(ID3D11VideoDecoderOutputView),
            'pView'
        ),
        ([], UINT, 'ContentKeySize'),
        (['in'], POINTER(VOID), 'pContentKey'),
        (['in'], UINT, 'NumComponentHistograms'),
        (['in'], POINTER(UINT), 'pHistogramOffsets'),
        (['in'], POINTER(ID3D11Buffer), 'ppHistogramBuffers'),
    ),
    COMMETHOD(
        [helpstring('Method SubmitDecoderBuffers2')],
        HRESULT,
        'SubmitDecoderBuffers2',
        (['in'], POINTER(ID3D11VideoDecoder), 'pDecoder'),
        (['in'], UINT, 'NumBuffers'),
        (
            ['in'],
            POINTER(D3D11_VIDEO_DECODER_BUFFER_DESC2),
            'pBufferDesc'
        ),
    ),
]

D3D11_FEATURE_DATA_D3D11_OPTIONS4._fields_ = [
    ('ExtendedNV12SharedTextureSupported', BOOL),
]
  
IID_ID3D11Device4 = GUID('{8992AB71-2E6-4B8D-BA48-B056DCDA42C4}')

IID_ID3D11Device5 = GUID('{8FFDE202-A0E7-45DF-9E01-E837801B5EA0}')

IID_ID3D11Multithread = GUID('{9B7E4E00-342C-4106-A19F-4F2704F689F0}')

IID_ID3D11VideoContext2 = GUID('{C4E7374C-6243-4D1B-AE87-52B4F740E261}')

IID_ID3D11VideoDevice2 = GUID('{59C0CB01-35F0-4A70-8F67-87905C906A53}')

IID_ID3D11VideoContext3 = GUID('{A9E2FAA0-CB39-418F-A0B7-D8AAD4DE672E}')
