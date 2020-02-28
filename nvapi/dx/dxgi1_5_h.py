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


class DXGI_HDR_METADATA_HDR10(ctypes.Structure):
    pass


class DXGI_HDR_METADATA_HDR10PLUS(ctypes.Structure):
    pass


from .dxgi1_4_h import *


class IDXGIOutput5(IDXGIOutput4):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = None


class IDXGISwapChain4(IDXGISwapChain3):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIDevice4(IDXGIDevice3):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIFactory5(IDXGIFactory4):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class DXGI_OUTDUPL_FLAG(ENUM):
    DXGI_OUTDUPL_COMPOSITED_UI_CAPTURE_ONLY = 1


IID_IDXGIOutput5 = MIDL_INTERFACE(
    "{80A07424-AB52-42EB-833C-0C42FD282D98}"
)
IDXGIOutput5._iid_ = IID_IDXGIOutput5

IDXGIOutput5._methods_ = [
    COMMETHOD(
        [helpstring('Method DuplicateOutput1')],
        HRESULT,
        'DuplicateOutput1',
        (['in'], POINTER(comtypes.IUnknown), 'pDevice'),
        (['in'], UINT, 'Flags'),
        (['in'], UINT, 'SupportedFormatsCount'),
        (['in'], POINTER(DXGI_FORMAT), 'pSupportedFormats'),
        (
            ['out'],
            POINTER(POINTER(IDXGIOutputDuplication)),
            'ppOutputDuplication'
        ),
    ),
]

class DXGI_HDR_METADATA_TYPE(ENUM):
    DXGI_HDR_METADATA_TYPE_NONE = 0
    DXGI_HDR_METADATA_TYPE_HDR10 = 1
    DXGI_HDR_METADATA_TYPE_HDR10PLUS = 2


DXGI_HDR_METADATA_HDR10._fields_ = [
    ('RedPrimary', UINT16 * 2),
    ('GreenPrimary', UINT16 * 2),
    ('BluePrimary', UINT16 * 2),
    ('WhitePoint', UINT16 * 2),
    ('MaxMasteringLuminance', UINT),
    ('MinMasteringLuminance', UINT),
    ('MaxContentLightLevel', UINT16),
    ('MaxFrameAverageLightLevel', UINT16),
]

DXGI_HDR_METADATA_HDR10PLUS._fields_ = [
    ('Data', BYTE * 72),
]


IID_IDXGISwapChain4 = MIDL_INTERFACE(
    "{3D585D5A-BD4A-489E-B1F4-3DBCB6452FFB}"
)
IDXGISwapChain4._iid_ = IID_IDXGISwapChain4

IDXGISwapChain4._methods_ = [
    COMMETHOD(
        [helpstring('Method SetHDRMetaData')],
        HRESULT,
        'SetHDRMetaData',
        (['in'], DXGI_HDR_METADATA_TYPE, 'Type'),
        (['in'], UINT, 'Size'),
        (['in'], POINTER(VOID), 'pMetaData'),
    ),
]


class _DXGI_OFFER_RESOURCE_FLAGS(ENUM):
    DXGI_OFFER_RESOURCE_FLAG_ALLOW_DECOMMIT = 0x1


DXGI_OFFER_RESOURCE_FLAGS = _DXGI_OFFER_RESOURCE_FLAGS


class _DXGI_RECLAIM_RESOURCE_RESULTS(ENUM):
    DXGI_RECLAIM_RESOURCE_RESULT_OK = 0
    DXGI_RECLAIM_RESOURCE_RESULT_DISCARDED = 1
    DXGI_RECLAIM_RESOURCE_RESULT_NOT_COMMITTED = 2


DXGI_RECLAIM_RESOURCE_RESULTS = _DXGI_RECLAIM_RESOURCE_RESULTS


IID_IDXGIDevice4 = MIDL_INTERFACE(
    "{95B4F95F-D8DA-4CA4-9EE6-3B76D5968A10}"
)
IDXGIDevice4._iid_ = IID_IDXGIDevice4

IDXGIDevice4._methods_ = [
    COMMETHOD(
        [helpstring('Method OfferResources1')],
        HRESULT,
        'OfferResources1',
        (['in'], UINT, 'NumResources'),
        (['in'], POINTER(IDXGIResource), 'ppResources'),
        (['in'], DXGI_OFFER_RESOURCE_PRIORITY, 'Priority'),
        (['in'], UINT, 'Flags'),
    ),
    COMMETHOD(
        [helpstring('Method ReclaimResources1')],
        HRESULT,
        'ReclaimResources1',
        (['in'], UINT, 'NumResources'),
        (['in'], POINTER(IDXGIResource), 'ppResources'),
        (
            ['out'],
            POINTER(DXGI_RECLAIM_RESOURCE_RESULTS),
            'pResults'
        ),
    ),
]


class DXGI_FEATURE(ENUM):
    DXGI_FEATURE_PRESENT_ALLOW_TEARING = 0


IID_IDXGIFactory5 = MIDL_INTERFACE(
    "{7632E1F5-EE65-4DCA-87FD-84CD75F8838D}"
)
IDXGIFactory5._iid_ = IID_IDXGIFactory5

IDXGIFactory5._methods_ = [
    COMMETHOD(
        [helpstring('Method CheckFeatureSupport')],
        HRESULT,
        'CheckFeatureSupport',
        ([], DXGI_FEATURE, 'Feature'),
        (['out', 'in'], POINTER(VOID), 'pFeatureSupportData'),
        ([], UINT, 'FeatureSupportDataSize'),
    ),
]

IID_IDXGIOutput5 = GUID('{80A07424-AB52-42EB-833C-0C42FD282D98}')

IID_IDXGISwapChain4 = GUID('{3D585D5A-BD4A-489E-B1F4-3DBCB6452FFB}')

IID_IDXGIDevice4 = GUID('{95B4F95F-D8DA-4CA4-9EE6-3B76D5968A10}')

IID_IDXGIFactory5 = GUID('{7632E1F5-EE65-4DCA-87FD-84CD75F8838D}')
