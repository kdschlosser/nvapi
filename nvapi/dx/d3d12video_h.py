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

from .d3d12_h import *
from .dxgicommon_h import *
from ..utils import *


class ID3D12VideoDecoderHeap(ID3D12Pageable):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = None


class D3D12_VIDEO_FORMAT(ctypes.Structure):
    pass


class D3D12_VIDEO_SAMPLE(ctypes.Structure):
    pass


class D3D12_VIDEO_DECODE_CONFIGURATION(ctypes.Structure):
    pass


class D3D12_VIDEO_DECODER_DESC(ctypes.Structure):
    pass


class D3D12_VIDEO_DECODER_HEAP_DESC(ctypes.Structure):
    pass


class D3D12_VIDEO_SIZE_RANGE(ctypes.Structure):
    pass


class D3D12_VIDEO_PROCESS_ALPHA_BLENDING(ctypes.Structure):
    pass


class D3D12_VIDEO_PROCESS_LUMA_KEY(ctypes.Structure):
    pass


class D3D12_VIDEO_PROCESS_INPUT_STREAM_DESC(ctypes.Structure):
    pass


class D3D12_VIDEO_PROCESS_OUTPUT_STREAM_DESC(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_VIDEO_DECODE_SUPPORT(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_VIDEO_DECODE_PROFILE_COUNT(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_VIDEO_DECODE_PROFILES(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_VIDEO_DECODE_FORMAT_COUNT(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_VIDEO_DECODE_FORMATS(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_VIDEO_ARCHITECTURE(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_VIDEO_DECODE_HISTOGRAM(ctypes.Structure):
    pass


class D3D12_VIDEO_SCALE_SUPPORT(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_VIDEO_DECODE_CONVERSION_SUPPORT(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_VIDEO_DECODER_HEAP_SIZE(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_VIDEO_PROCESSOR_SIZE(ctypes.Structure):
    pass


class D3D12_QUERY_DATA_VIDEO_DECODE_STATISTICS(ctypes.Structure):
    pass


class D3D12_VIDEO_DECODE_SUB_SAMPLE_MAPPING_BLOCK(ctypes.Structure):
    pass


class D3D12_VIDEO_DECODE_FRAME_ARGUMENT(ctypes.Structure):
    pass


class D3D12_VIDEO_DECODE_REFERENCE_FRAMES(ctypes.Structure):
    pass


class D3D12_VIDEO_DECODE_COMPRESSED_BITSTREAM(ctypes.Structure):
    pass


class D3D12_VIDEO_DECODE_CONVERSION_ARGUMENTS(ctypes.Structure):
    pass


class D3D12_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS(ctypes.Structure):
    pass


class D3D12_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS(ctypes.Structure):
    pass


class D3D12_VIDEO_PROCESS_FILTER_RANGE(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_VIDEO_PROCESS_SUPPORT(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_VIDEO_PROCESS_MAX_INPUT_STREAMS(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_VIDEO_PROCESS_REFERENCE_INFO(ctypes.Structure):
    pass


class D3D12_VIDEO_PROCESS_REFERENCE_SET(ctypes.Structure):
    pass


class D3D12_VIDEO_PROCESS_TRANSFORM(ctypes.Structure):
    pass


class D3D12_VIDEO_PROCESS_INPUT_STREAM_RATE(ctypes.Structure):
    pass


class D3D12_VIDEO_PROCESS_INPUT_STREAM(ctypes.Structure):
    pass


class D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS(ctypes.Structure):
    pass


class D3D12_VIDEO_PROCESS_OUTPUT_STREAM(ctypes.Structure):
    pass


class D3D12_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS(ctypes.Structure):
    pass


class D3D12_VIDEO_DECODE_OUTPUT_HISTOGRAM(ctypes.Structure):
    pass


class D3D12_VIDEO_DECODE_CONVERSION_ARGUMENTS1(ctypes.Structure):
    pass


class D3D12_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS1(ctypes.Structure):
    pass


class D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS1(ctypes.Structure):
    pass


class ID3D12VideoDevice(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12VideoDecoder(ID3D12Pageable):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12VideoProcessor(ID3D12Pageable):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12VideoDecodeCommandList(ID3D12CommandList):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12VideoProcessCommandList(ID3D12CommandList):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12VideoDecodeCommandList1(ID3D12VideoDecodeCommandList):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12VideoProcessCommandList1(ID3D12VideoProcessCommandList):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []

 
class D3D12_VIDEO_FIELD_TYPE(ENUM):
    D3D12_VIDEO_FIELD_TYPE_NONE = 0
    D3D12_VIDEO_FIELD_TYPE_INTERLACED_TOP_FIELD_FIRST = 1
    D3D12_VIDEO_FIELD_TYPE_INTERLACED_BOTTOM_FIELD_FIRST = 2


class D3D12_VIDEO_FRAME_STEREO_FORMAT(ENUM):
    D3D12_VIDEO_FRAME_STEREO_FORMAT_NONE = 0
    D3D12_VIDEO_FRAME_STEREO_FORMAT_MONO = 1
    D3D12_VIDEO_FRAME_STEREO_FORMAT_HORIZONTAL = 2
    D3D12_VIDEO_FRAME_STEREO_FORMAT_VERTICAL = 3
    D3D12_VIDEO_FRAME_STEREO_FORMAT_SEPARATE = 4

D3D12_VIDEO_FORMAT._fields_ = [
    ('Format', DXGI_FORMAT),
    ('ColorSpace', DXGI_COLOR_SPACE_TYPE),
]

D3D12_VIDEO_SAMPLE._fields_ = [
    ('Width', UINT),
    ('Height', UINT),
    ('Format', D3D12_VIDEO_FORMAT),
]


class D3D12_VIDEO_FRAME_CODED_INTERLACE_TYPE(ENUM):
    D3D12_VIDEO_FRAME_CODED_INTERLACE_TYPE_NONE = 0
    D3D12_VIDEO_FRAME_CODED_INTERLACE_TYPE_FIELD_BASED = 1


class D3D12_FEATURE_VIDEO(ENUM):
    D3D12_FEATURE_VIDEO_DECODE_SUPPORT = 0
    D3D12_FEATURE_VIDEO_DECODE_PROFILES = 1
    D3D12_FEATURE_VIDEO_DECODE_FORMATS = 2
    D3D12_FEATURE_VIDEO_DECODE_CONVERSION_SUPPORT = 3
    D3D12_FEATURE_VIDEO_PROCESS_SUPPORT = 5
    D3D12_FEATURE_VIDEO_PROCESS_MAX_INPUT_STREAMS = 6
    D3D12_FEATURE_VIDEO_PROCESS_REFERENCE_INFO = 7
    D3D12_FEATURE_VIDEO_DECODER_HEAP_SIZE = 8
    D3D12_FEATURE_VIDEO_PROCESSOR_SIZE = 9
    D3D12_FEATURE_VIDEO_DECODE_PROFILE_COUNT = 10
    D3D12_FEATURE_VIDEO_DECODE_FORMAT_COUNT = 11
    D3D12_FEATURE_VIDEO_ARCHITECTURE = 17
    D3D12_FEATURE_VIDEO_DECODE_HISTOGRAM = 18


class D3D12_BITSTREAM_ENCRYPTION_TYPE(ENUM):
    D3D12_BITSTREAM_ENCRYPTION_TYPE_NONE = 0

D3D12_VIDEO_DECODE_CONFIGURATION._fields_ = [
    ('DecodeProfile', GUID),
    ('BitstreamEncryption', D3D12_BITSTREAM_ENCRYPTION_TYPE),
    ('InterlaceType', D3D12_VIDEO_FRAME_CODED_INTERLACE_TYPE),
]

D3D12_VIDEO_DECODER_DESC._fields_ = [
    ('NodeMask', UINT),
    ('Configuration', D3D12_VIDEO_DECODE_CONFIGURATION),
]

D3D12_VIDEO_DECODER_HEAP_DESC._fields_ = [
    ('NodeMask', UINT),
    ('Configuration', D3D12_VIDEO_DECODE_CONFIGURATION),
    ('DecodeWidth', UINT),
    ('DecodeHeight', UINT),
    ('Format', DXGI_FORMAT),
    ('FrameRate', DXGI_RATIONAL),
    ('BitRate', UINT),
    ('MaxDecodePictureBufferCount', UINT),
]

D3D12_VIDEO_SIZE_RANGE._fields_ = [
    ('MaxWidth', UINT),
    ('MaxHeight', UINT),
    ('MinWidth', UINT),
    ('MinHeight', UINT),
]


class D3D12_VIDEO_PROCESS_FILTER(ENUM):
    D3D12_VIDEO_PROCESS_FILTER_BRIGHTNESS = 0
    D3D12_VIDEO_PROCESS_FILTER_CONTRAST = 1
    D3D12_VIDEO_PROCESS_FILTER_HUE = 2
    D3D12_VIDEO_PROCESS_FILTER_SATURATION = 3
    D3D12_VIDEO_PROCESS_FILTER_NOISE_REDUCTION = 4
    D3D12_VIDEO_PROCESS_FILTER_EDGE_ENHANCEMENT = 5
    D3D12_VIDEO_PROCESS_FILTER_ANAMORPHIC_SCALING = 6
    D3D12_VIDEO_PROCESS_FILTER_STEREO_ADJUSTMENT = 7


class D3D12_VIDEO_PROCESS_FILTER_FLAGS(ENUM):
    D3D12_VIDEO_PROCESS_FILTER_FLAG_NONE = 0
    D3D12_VIDEO_PROCESS_FILTER_FLAG_BRIGHTNESS = (
        1 << D3D12_VIDEO_PROCESS_FILTER.D3D12_VIDEO_PROCESS_FILTER_BRIGHTNESS
    )
    D3D12_VIDEO_PROCESS_FILTER_FLAG_CONTRAST = (
        1 << D3D12_VIDEO_PROCESS_FILTER.D3D12_VIDEO_PROCESS_FILTER_CONTRAST
    )
    D3D12_VIDEO_PROCESS_FILTER_FLAG_HUE = (
        1 << D3D12_VIDEO_PROCESS_FILTER.D3D12_VIDEO_PROCESS_FILTER_HUE
    )
    D3D12_VIDEO_PROCESS_FILTER_FLAG_SATURATION = (
        1 << D3D12_VIDEO_PROCESS_FILTER.D3D12_VIDEO_PROCESS_FILTER_SATURATION
    )
    D3D12_VIDEO_PROCESS_FILTER_FLAG_NOISE_REDUCTION = (
        1 << D3D12_VIDEO_PROCESS_FILTER.D3D12_VIDEO_PROCESS_FILTER_NOISE_REDUCTION
    )
    D3D12_VIDEO_PROCESS_FILTER_FLAG_EDGE_ENHANCEMENT = (
        1 << D3D12_VIDEO_PROCESS_FILTER.D3D12_VIDEO_PROCESS_FILTER_EDGE_ENHANCEMENT
    )
    D3D12_VIDEO_PROCESS_FILTER_FLAG_ANAMORPHIC_SCALING = (
        1 << D3D12_VIDEO_PROCESS_FILTER.D3D12_VIDEO_PROCESS_FILTER_ANAMORPHIC_SCALING
    )
    D3D12_VIDEO_PROCESS_FILTER_FLAG_STEREO_ADJUSTMENT = (
        1 << D3D12_VIDEO_PROCESS_FILTER.D3D12_VIDEO_PROCESS_FILTER_STEREO_ADJUSTMENT
    )


class D3D12_VIDEO_PROCESS_DEINTERLACE_FLAGS(ENUM):
    D3D12_VIDEO_PROCESS_DEINTERLACE_FLAG_NONE = 0
    D3D12_VIDEO_PROCESS_DEINTERLACE_FLAG_BOB = 0x1
    D3D12_VIDEO_PROCESS_DEINTERLACE_FLAG_CUSTOM = 0x80000000

D3D12_VIDEO_PROCESS_ALPHA_BLENDING._fields_ = [
    ('Enable', BOOL),
    ('Alpha', FLOAT),
]

D3D12_VIDEO_PROCESS_LUMA_KEY._fields_ = [
    ('Enable', BOOL),
    ('Lower', FLOAT),
    ('Upper', FLOAT),
]

D3D12_VIDEO_PROCESS_INPUT_STREAM_DESC._fields_ = [
    ('Format', DXGI_FORMAT),
    ('ColorSpace', DXGI_COLOR_SPACE_TYPE),
    ('SourceAspectRatio', DXGI_RATIONAL),
    ('DestinationAspectRatio', DXGI_RATIONAL),
    ('FrameRate', DXGI_RATIONAL),
    ('SourceSizeRange', D3D12_VIDEO_SIZE_RANGE),
    ('DestinationSizeRange', D3D12_VIDEO_SIZE_RANGE),
    ('EnableOrientation', BOOL),
    ('FilterFlags', D3D12_VIDEO_PROCESS_FILTER_FLAGS),
    ('StereoFormat', D3D12_VIDEO_FRAME_STEREO_FORMAT),
    ('FieldType', D3D12_VIDEO_FIELD_TYPE),
    ('DeinterlaceMode', D3D12_VIDEO_PROCESS_DEINTERLACE_FLAGS),
    ('EnableAlphaBlending', BOOL),
    ('LumaKey', D3D12_VIDEO_PROCESS_LUMA_KEY),
    ('NumPastFrames', UINT),
    ('NumFutureFrames', UINT),
    ('EnableAutoProcessing', BOOL),
]


class D3D12_VIDEO_PROCESS_ALPHA_FILL_MODE(ENUM):
    D3D12_VIDEO_PROCESS_ALPHA_FILL_MODE_OPAQUE = 0
    D3D12_VIDEO_PROCESS_ALPHA_FILL_MODE_BACKGROUND = 1
    D3D12_VIDEO_PROCESS_ALPHA_FILL_MODE_DESTINATION = 2
    D3D12_VIDEO_PROCESS_ALPHA_FILL_MODE_SOURCE_STREAM = 3

D3D12_VIDEO_PROCESS_OUTPUT_STREAM_DESC._fields_ = [
    ('Format', DXGI_FORMAT),
    ('ColorSpace', DXGI_COLOR_SPACE_TYPE),
    ('AlphaFillMode', D3D12_VIDEO_PROCESS_ALPHA_FILL_MODE),
    ('AlphaFillModeSourceStreamIndex', UINT),
    ('BackgroundColor', FLOAT * 4),
    ('FrameRate', DXGI_RATIONAL),
    ('EnableStereo', BOOL),
]
    
IID_ID3D12VideoDecoderHeap = MIDL_INTERFACE(
    "{0946B7C9-EBF6-4047-BB73-8683E27DBB1F}"
)
ID3D12VideoDecoderHeap._iid_ = IID_ID3D12VideoDecoderHeap


ID3D12VideoDecoderHeap._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        D3D12_VIDEO_DECODER_HEAP_DESC,
        'GetDesc',
    ),
]

IID_ID3D12VideoDevice = MIDL_INTERFACE(
    "{1F052807-0B46-4ACC-8A89-364F793718A4}"
)
ID3D12VideoDevice._iid_ = IID_ID3D12VideoDevice


ID3D12VideoDevice._methods_ = [
    COMMETHOD(
        [helpstring('Method CheckFeatureSupport')],
        HRESULT,
        'CheckFeatureSupport',
        ([], D3D12_FEATURE_VIDEO, 'FeatureVideo'),
        (['out', 'in'], POINTER(VOID), 'pFeatureSupportData'),
        ([], UINT, 'FeatureSupportDataSize'),
    ),
    COMMETHOD(
        [helpstring('Method CreateVideoDecoder')],
        HRESULT,
        'CreateVideoDecoder',
        (['in'], POINTER(D3D12_VIDEO_DECODER_DESC), 'pDesc'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppVideoDecoder'),
    ),
    COMMETHOD(
        [helpstring('Method CreateVideoDecoderHeap')],
        HRESULT,
        'CreateVideoDecoderHeap',
        (
            ['in'],
            POINTER(D3D12_VIDEO_DECODER_HEAP_DESC),
            'pVideoDecoderHeapDesc'
        ),
        (['in'], REFIID, 'riid'),
        (
            ['out'],
            POINTER(POINTER(VOID)),
            'ppVideoDecoderHeap'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateVideoProcessor')],
        HRESULT,
        'CreateVideoProcessor',
        ([], UINT, 'NodeMask'),
        (
            ['in'],
            POINTER(D3D12_VIDEO_PROCESS_OUTPUT_STREAM_DESC),
            'pOutputStreamDesc'
        ),
        ([], UINT, 'NumInputStreamDescs'),
        (
            ['in'],
            POINTER(D3D12_VIDEO_PROCESS_INPUT_STREAM_DESC),
            'pInputStreamDescs'
        ),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppVideoProcessor'),
    ),
]

IID_ID3D12VideoDecoder = MIDL_INTERFACE(
    "{C59B6BDC-7720-4074-A136-17A156037470}"
)
ID3D12VideoDecoder._iid_ = IID_ID3D12VideoDecoder


ID3D12VideoDecoder._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        D3D12_VIDEO_DECODER_DESC,
        'GetDesc',
    ),
]

class D3D12_VIDEO_DECODE_TIER(ENUM):
    D3D12_VIDEO_DECODE_TIER_NOT_SUPPORTED = 0
    D3D12_VIDEO_DECODE_TIER_1 = 1
    D3D12_VIDEO_DECODE_TIER_2 = 2
    D3D12_VIDEO_DECODE_TIER_3 = 3


class D3D12_VIDEO_DECODE_SUPPORT_FLAGS(ENUM):
    D3D12_VIDEO_DECODE_SUPPORT_FLAG_NONE = 0
    D3D12_VIDEO_DECODE_SUPPORT_FLAG_SUPPORTED = 0x1


class D3D12_VIDEO_DECODE_CONFIGURATION_FLAGS(ENUM):
    D3D12_VIDEO_DECODE_CONFIGURATION_FLAG_NONE = 0
    D3D12_VIDEO_DECODE_CONFIGURATION_FLAG_HEIGHT_ALIGNMENT_MULTIPLE_32_REQUIRED = (
        0x1
    )
    D3D12_VIDEO_DECODE_CONFIGURATION_FLAG_POST_PROCESSING_SUPPORTED = (
        0x2
    )
    D3D12_VIDEO_DECODE_CONFIGURATION_FLAG_REFERENCE_ONLY_ALLOCATIONS_REQUIRED = (
        0x4
    )
    D3D12_VIDEO_DECODE_CONFIGURATION_FLAG_ALLOW_RESOLUTION_CHANGE_ON_NON_KEY_FRAME = (
        0x8
    )


class D3D12_VIDEO_DECODE_STATUS(ENUM):
    D3D12_VIDEO_DECODE_STATUS_OK = 0
    D3D12_VIDEO_DECODE_STATUS_CONTINUE = 1
    D3D12_VIDEO_DECODE_STATUS_CONTINUE_SKIP_DISPLAY = 2
    D3D12_VIDEO_DECODE_STATUS_RESTART = 3


class D3D12_VIDEO_DECODE_ARGUMENT_TYPE(ENUM):
    D3D12_VIDEO_DECODE_ARGUMENT_TYPE_PICTURE_PARAMETERS = 0
    D3D12_VIDEO_DECODE_ARGUMENT_TYPE_INVERSE_QUANTIZATION_MATRIX = 1
    D3D12_VIDEO_DECODE_ARGUMENT_TYPE_SLICE_CONTROL = 2
    D3D12_VIDEO_DECODE_ARGUMENT_TYPE_MAX_VALID = 3

D3D12_FEATURE_DATA_VIDEO_DECODE_SUPPORT._fields_ = [
    ('NodeIndex', UINT),
    ('Configuration', D3D12_VIDEO_DECODE_CONFIGURATION),
    ('Width', UINT),
    ('Height', UINT),
    ('DecodeFormat', DXGI_FORMAT),
    ('FrameRate', DXGI_RATIONAL),
    ('BitRate', UINT),
    ('SupportFlags', D3D12_VIDEO_DECODE_SUPPORT_FLAGS),
    ('ConfigurationFlags', D3D12_VIDEO_DECODE_CONFIGURATION_FLAGS),
    ('DecodeTier', D3D12_VIDEO_DECODE_TIER),
]

D3D12_FEATURE_DATA_VIDEO_DECODE_PROFILE_COUNT._fields_ = [
    ('NodeIndex', UINT),
    ('ProfileCount', UINT),
]

D3D12_FEATURE_DATA_VIDEO_DECODE_PROFILES._fields_ = [
    ('NodeIndex', UINT),
    ('ProfileCount', UINT),
    ('pProfiles', POINTER(GUID)),
]

D3D12_FEATURE_DATA_VIDEO_DECODE_FORMAT_COUNT._fields_ = [
    ('NodeIndex', UINT),
    ('Configuration', D3D12_VIDEO_DECODE_CONFIGURATION),
    ('FormatCount', UINT),
]

D3D12_FEATURE_DATA_VIDEO_DECODE_FORMATS._fields_ = [
    ('NodeIndex', UINT),
    ('Configuration', D3D12_VIDEO_DECODE_CONFIGURATION),
    ('FormatCount', UINT),
    ('pOutputFormats', POINTER(DXGI_FORMAT)),
]

D3D12_FEATURE_DATA_VIDEO_ARCHITECTURE._fields_ = [
    ('IOCoherent', BOOL),
]


class D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT(ENUM):
    D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_Y = 0
    D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_U = 1
    D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_V = 2
    D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_R = 0
    D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_G = 1
    D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_B = 2
    D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_A = 3


class D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAGS(ENUM):
    D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAG_NONE = 0
    D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAG_Y = (
        1 << D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT.D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_Y
    )
    D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAG_U = (
        1 << D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT.D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_U
    )
    D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAG_V = (
        1 << D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT.D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_V
    )
    D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAG_R = (
        1 << D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT.D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_R
    )
    D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAG_G = (
        1 << D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT.D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_G
    )
    D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAG_B = (
        1 << D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT.D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_B
    )
    D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAG_A = (
        1 << D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT.D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_A
    )

D3D12_FEATURE_DATA_VIDEO_DECODE_HISTOGRAM._fields_ = [
    ('NodeIndex', UINT),
    ('DecodeProfile', GUID),
    ('Width', UINT),
    ('Height', UINT),
    ('DecodeFormat', DXGI_FORMAT),
    ('Components', D3D12_VIDEO_DECODE_HISTOGRAM_COMPONENT_FLAGS),
    ('BinCount', UINT),
    ('CounterBitDepth', UINT),
]


class D3D12_VIDEO_DECODE_CONVERSION_SUPPORT_FLAGS(ENUM):
    D3D12_VIDEO_DECODE_CONVERSION_SUPPORT_FLAG_NONE = 0
    D3D12_VIDEO_DECODE_CONVERSION_SUPPORT_FLAG_SUPPORTED = 0x1


class D3D12_VIDEO_SCALE_SUPPORT_FLAGS(ENUM):
    D3D12_VIDEO_SCALE_SUPPORT_FLAG_NONE = 0
    D3D12_VIDEO_SCALE_SUPPORT_FLAG_POW2_ONLY = 0x1
    D3D12_VIDEO_SCALE_SUPPORT_FLAG_EVEN_DIMENSIONS_ONLY = 0x2

D3D12_VIDEO_SCALE_SUPPORT._fields_ = [
    ('OutputSizeRange', D3D12_VIDEO_SIZE_RANGE),
    ('Flags', D3D12_VIDEO_SCALE_SUPPORT_FLAGS),
]

D3D12_FEATURE_DATA_VIDEO_DECODE_CONVERSION_SUPPORT._fields_ = [
    ('NodeIndex', UINT),
    ('Configuration', D3D12_VIDEO_DECODE_CONFIGURATION),
    ('DecodeSample', D3D12_VIDEO_SAMPLE),
    ('OutputFormat', D3D12_VIDEO_FORMAT),
    ('FrameRate', DXGI_RATIONAL),
    ('BitRate', UINT),
    ('SupportFlags', D3D12_VIDEO_DECODE_CONVERSION_SUPPORT_FLAGS),
    ('ScaleSupport', D3D12_VIDEO_SCALE_SUPPORT),
]

D3D12_FEATURE_DATA_VIDEO_DECODER_HEAP_SIZE._fields_ = [
    ('VideoDecoderHeapDesc', D3D12_VIDEO_DECODER_HEAP_DESC),
    ('MemoryPoolL0Size', UINT64),
    ('MemoryPoolL1Size', UINT64),
]

D3D12_FEATURE_DATA_VIDEO_PROCESSOR_SIZE._fields_ = [
    ('NodeMask', UINT),
    ('pOutputStreamDesc', POINTER(D3D12_VIDEO_PROCESS_OUTPUT_STREAM_DESC)),
    ('NumInputStreamDescs', UINT),
    ('pInputStreamDescs', POINTER(D3D12_VIDEO_PROCESS_INPUT_STREAM_DESC)),
    ('MemoryPoolL0Size', UINT64),
    ('MemoryPoolL1Size', UINT64),
]

D3D12_QUERY_DATA_VIDEO_DECODE_STATISTICS._fields_ = [
    ('Status', UINT64),
    ('NumMacroblocksAffected', UINT64),
    ('FrameRate', DXGI_RATIONAL),
    ('BitRate', UINT),
]

D3D12_VIDEO_DECODE_SUB_SAMPLE_MAPPING_BLOCK._fields_ = [
    ('ClearSize', UINT),
    ('EncryptedSize', UINT),
]

D3D12_VIDEO_DECODE_FRAME_ARGUMENT._fields_ = [
    ('Type', D3D12_VIDEO_DECODE_ARGUMENT_TYPE),
    ('Size', UINT),
    ('pData', POINTER(VOID)),
]

D3D12_VIDEO_DECODE_REFERENCE_FRAMES._fields_ = [
    ('NumTexture2Ds', UINT),
    ('ppTexture2Ds', POINTER(POINTER(ID3D12Resource))),
    ('pSubresources', POINTER(UINT)),
    ('ppHeaps', POINTER(POINTER(ID3D12VideoDecoderHeap))),
]

D3D12_VIDEO_DECODE_COMPRESSED_BITSTREAM._fields_ = [
    ('pBuffer', POINTER(ID3D12Resource)),
    ('Offset', UINT64),
    ('Size', UINT64),
]

D3D12_VIDEO_DECODE_CONVERSION_ARGUMENTS._fields_ = [
    ('Enable', BOOL),
    ('pReferenceTexture2D', POINTER(ID3D12Resource)),
    ('ReferenceSubresource', UINT),
    ('OutputColorSpace', DXGI_COLOR_SPACE_TYPE),
    ('DecodeColorSpace', DXGI_COLOR_SPACE_TYPE),
]

D3D12_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS._fields_ = [
    ('NumFrameArguments', UINT),
    ('FrameArguments', D3D12_VIDEO_DECODE_FRAME_ARGUMENT * 10),
    ('ReferenceFrames', D3D12_VIDEO_DECODE_REFERENCE_FRAMES),
    ('CompressedBitstream', D3D12_VIDEO_DECODE_COMPRESSED_BITSTREAM),
    ('pHeap', POINTER(ID3D12VideoDecoderHeap)),
]

D3D12_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS._fields_ = [
    ('pOutputTexture2D', POINTER(ID3D12Resource)),
    ('OutputSubresource', UINT),
    ('ConversionArguments', D3D12_VIDEO_DECODE_CONVERSION_ARGUMENTS),
]
      
IID_ID3D12VideoProcessor = MIDL_INTERFACE(
    "{304FDB32-BEDE-410A-8545-943AC6A46138}"
)
ID3D12VideoProcessor._iid_ = IID_ID3D12VideoProcessor


ID3D12VideoProcessor._methods_ = [
    COMMETHOD(
        [helpstring('Method GetNodeMask')],
        UINT,
        'GetNodeMask',
    ),
    COMMETHOD(
        [helpstring('Method GetNumInputStreamDescs')],
        UINT,
        'GetNumInputStreamDescs',
    ),
    COMMETHOD(
        [helpstring('Method GetInputStreamDescs')],
        HRESULT,
        'GetInputStreamDescs',
        ([], UINT, 'NumInputStreamDescs'),
        (
            ['out', 'in'],
            POINTER(D3D12_VIDEO_PROCESS_INPUT_STREAM_DESC),
            'pInputStreamDescs'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetOutputStreamDesc')],
        D3D12_VIDEO_PROCESS_OUTPUT_STREAM_DESC,
        'GetOutputStreamDesc',
    ),
]

class D3D12_VIDEO_PROCESS_FEATURE_FLAGS(ENUM):
    D3D12_VIDEO_PROCESS_FEATURE_FLAG_NONE = 0
    D3D12_VIDEO_PROCESS_FEATURE_FLAG_ALPHA_FILL = 0x1
    D3D12_VIDEO_PROCESS_FEATURE_FLAG_LUMA_KEY = 0x2
    D3D12_VIDEO_PROCESS_FEATURE_FLAG_STEREO = 0x4
    D3D12_VIDEO_PROCESS_FEATURE_FLAG_ROTATION = 0x8
    D3D12_VIDEO_PROCESS_FEATURE_FLAG_FLIP = 0x10
    D3D12_VIDEO_PROCESS_FEATURE_FLAG_ALPHA_BLENDING = 0x20
    D3D12_VIDEO_PROCESS_FEATURE_FLAG_PIXEL_ASPECT_RATIO = 0x40


class D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAGS(ENUM):
    D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAG_NONE = 0
    D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAG_DENOISE = 0x1
    D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAG_DERINGING = 0x2
    D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAG_EDGE_ENHANCEMENT = 0x4
    D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAG_COLOR_CORRECTION = 0x8
    D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAG_FLESH_TONE_MAPPING = 0x10
    D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAG_IMAGE_STABILIZATION = 0x20
    D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAG_SUPER_RESOLUTION = 0x40
    D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAG_ANAMORPHIC_SCALING = 0x80
    D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAG_CUSTOM = 0x80000000


class D3D12_VIDEO_PROCESS_ORIENTATION(ENUM):
    D3D12_VIDEO_PROCESS_ORIENTATION_DEFAULT = 0
    D3D12_VIDEO_PROCESS_ORIENTATION_FLIP_HORIZONTAL = 1
    D3D12_VIDEO_PROCESS_ORIENTATION_CLOCKWISE_90 = 2
    D3D12_VIDEO_PROCESS_ORIENTATION_CLOCKWISE_90_FLIP_HORIZONTAL = 3
    D3D12_VIDEO_PROCESS_ORIENTATION_CLOCKWISE_180 = 4
    D3D12_VIDEO_PROCESS_ORIENTATION_FLIP_VERTICAL = 5
    D3D12_VIDEO_PROCESS_ORIENTATION_CLOCKWISE_270 = 6
    D3D12_VIDEO_PROCESS_ORIENTATION_CLOCKWISE_270_FLIP_HORIZONTAL = 7


class D3D12_VIDEO_PROCESS_INPUT_STREAM_FLAGS(ENUM):
    D3D12_VIDEO_PROCESS_INPUT_STREAM_FLAG_NONE = 0
    D3D12_VIDEO_PROCESS_INPUT_STREAM_FLAG_FRAME_DISCONTINUITY = 0x1
    D3D12_VIDEO_PROCESS_INPUT_STREAM_FLAG_FRAME_REPEAT = 0x2

D3D12_VIDEO_PROCESS_FILTER_RANGE._fields_ = [
    ('Minimum', INT),
    ('Maximum', INT),
    ('Default', INT),
    ('Multiplier', FLOAT),
]


class D3D12_VIDEO_PROCESS_SUPPORT_FLAGS(ENUM):
    D3D12_VIDEO_PROCESS_SUPPORT_FLAG_NONE = 0
    D3D12_VIDEO_PROCESS_SUPPORT_FLAG_SUPPORTED = 0x1

D3D12_FEATURE_DATA_VIDEO_PROCESS_SUPPORT._fields_ = [
    ('NodeIndex', UINT),
    ('InputSample', D3D12_VIDEO_SAMPLE),
    ('InputFieldType', D3D12_VIDEO_FIELD_TYPE),
    ('InputStereoFormat', D3D12_VIDEO_FRAME_STEREO_FORMAT),
    ('InputFrameRate', DXGI_RATIONAL),
    ('OutputFormat', D3D12_VIDEO_FORMAT),
    ('OutputStereoFormat', D3D12_VIDEO_FRAME_STEREO_FORMAT),
    ('OutputFrameRate', DXGI_RATIONAL),
    ('SupportFlags', D3D12_VIDEO_PROCESS_SUPPORT_FLAGS),
    ('ScaleSupport', D3D12_VIDEO_SCALE_SUPPORT),
    ('FeatureSupport', D3D12_VIDEO_PROCESS_FEATURE_FLAGS),
    ('DeinterlaceSupport', D3D12_VIDEO_PROCESS_DEINTERLACE_FLAGS),
    ('AutoProcessingSupport', D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAGS),
    ('FilterSupport', D3D12_VIDEO_PROCESS_FILTER_FLAGS),
    ('FilterRangeSupport', D3D12_VIDEO_PROCESS_FILTER_RANGE * 32),
]

D3D12_FEATURE_DATA_VIDEO_PROCESS_MAX_INPUT_STREAMS._fields_ = [
    ('NodeIndex', UINT),
    ('MaxInputStreams', UINT),
]

D3D12_FEATURE_DATA_VIDEO_PROCESS_REFERENCE_INFO._fields_ = [
    ('NodeIndex', UINT),
    ('DeinterlaceMode', D3D12_VIDEO_PROCESS_DEINTERLACE_FLAGS),
    ('Filters', D3D12_VIDEO_PROCESS_FILTER_FLAGS),
    ('FeatureSupport', D3D12_VIDEO_PROCESS_FEATURE_FLAGS),
    ('InputFrameRate', DXGI_RATIONAL),
    ('OutputFrameRate', DXGI_RATIONAL),
    ('EnableAutoProcessing', BOOL),
    ('PastFrames', UINT),
    ('FutureFrames', UINT),
]

D3D12_VIDEO_PROCESS_REFERENCE_SET._fields_ = [
    ('NumPastFrames', UINT),
    ('ppPastFrames', POINTER(POINTER(ID3D12Resource))),
    ('pPastSubresources', POINTER(UINT)),
    ('NumFutureFrames', UINT),
    ('ppFutureFrames', POINTER(POINTER(ID3D12Resource))),
    ('pFutureSubresources', POINTER(UINT)),
]

D3D12_VIDEO_PROCESS_TRANSFORM._fields_ = [
    ('SourceRectangle', D3D12_RECT),
    ('DestinationRectangle', D3D12_RECT),
    ('Orientation', D3D12_VIDEO_PROCESS_ORIENTATION),
]

D3D12_VIDEO_PROCESS_INPUT_STREAM_RATE._fields_ = [
    ('OutputIndex', UINT),
    ('InputFrameOrField', UINT),
]

D3D12_VIDEO_PROCESS_INPUT_STREAM._fields_ = [
    ('pTexture2D', POINTER(ID3D12Resource)),
    ('Subresource', UINT),
    ('ReferenceSet', D3D12_VIDEO_PROCESS_REFERENCE_SET),
]

D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS._fields_ = [
    ('InputStream', D3D12_VIDEO_PROCESS_INPUT_STREAM * 2),
    ('Transform', D3D12_VIDEO_PROCESS_TRANSFORM),
    ('Flags', D3D12_VIDEO_PROCESS_INPUT_STREAM_FLAGS),
    ('RateInfo', D3D12_VIDEO_PROCESS_INPUT_STREAM_RATE),
    ('FilterLevels', INT * 32),
    ('AlphaBlending', D3D12_VIDEO_PROCESS_ALPHA_BLENDING),
]

D3D12_VIDEO_PROCESS_OUTPUT_STREAM._fields_ = [
    ('pTexture2D', POINTER(ID3D12Resource)),
    ('Subresource', UINT),
]

D3D12_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS._fields_ = [
    ('OutputStream', D3D12_VIDEO_PROCESS_OUTPUT_STREAM * 2),
    ('TargetRectangle', D3D12_RECT),
]


IID_ID3D12VideoDecodeCommandList = MIDL_INTERFACE(
    "{3B60536E-AD29-4E64-A269-F853837E5E53}"
)
ID3D12VideoDecodeCommandList._iid_ = IID_ID3D12VideoDecodeCommandList


ID3D12VideoDecodeCommandList._methods_ = [
    COMMETHOD(
        [helpstring('Method Close')],
        HRESULT,
        'Close',
    ),
    COMMETHOD(
        [helpstring('Method Reset')],
        HRESULT,
        'Reset',
        (
            ['in'],
            POINTER(ID3D12CommandAllocator),
            'pAllocator'
        ),
    ),
    COMMETHOD(
        [helpstring('Method ClearState')],
        VOID,
        'ClearState',
    ),
    COMMETHOD(
        [helpstring('Method ResourceBarrier')],
        VOID,
        'ResourceBarrier',
        (['in'], UINT, 'NumBarriers'),
        (
            ['in'],
            POINTER(D3D12_RESOURCE_BARRIER),
            'pBarriers'
        ),
    ),
    COMMETHOD(
        [helpstring('Method DiscardResource')],
        VOID,
        'DiscardResource',
        (['in'], POINTER(ID3D12Resource), 'pResource'),
        (['in'], POINTER(D3D12_DISCARD_REGION), 'pRegion'),
    ),
    COMMETHOD(
        [helpstring('Method BeginQuery')],
        VOID,
        'BeginQuery',
        (['in'], POINTER(ID3D12QueryHeap), 'pQueryHeap'),
        (['in'], D3D12_QUERY_TYPE, 'Type'),
        (['in'], UINT, 'Index'),
    ),
    COMMETHOD(
        [helpstring('Method EndQuery')],
        VOID,
        'EndQuery',
        (['in'], POINTER(ID3D12QueryHeap), 'pQueryHeap'),
        (['in'], D3D12_QUERY_TYPE, 'Type'),
        (['in'], UINT, 'Index'),
    ),
    COMMETHOD(
        [helpstring('Method ResolveQueryData')],
        VOID,
        'ResolveQueryData',
        (['in'], POINTER(ID3D12QueryHeap), 'pQueryHeap'),
        (['in'], D3D12_QUERY_TYPE, 'Type'),
        (['in'], UINT, 'StartIndex'),
        (['in'], UINT, 'NumQueries'),
        (
            ['in'],
            POINTER(ID3D12Resource),
            'pDestinationBuffer'
        ),
        (['in'], UINT64, 'AlignedDestinationBufferOffset'),
    ),
    COMMETHOD(
        [helpstring('Method SetPredication')],
        VOID,
        'SetPredication',
        (['in'], POINTER(ID3D12Resource), 'pBuffer'),
        (['in'], UINT64, 'AlignedBufferOffset'),
        (['in'], D3D12_PREDICATION_OP, 'Operation'),
    ),
    COMMETHOD(
        [helpstring('Method SetMarker')],
        VOID,
        'SetMarker',
        ([], UINT, 'Metadata'),
        (['in'], POINTER(VOID), 'pData'),
        ([], UINT, 'Size'),
    ),
    COMMETHOD(
        [helpstring('Method BeginEvent')],
        VOID,
        'BeginEvent',
        ([], UINT, 'Metadata'),
        (['in'], POINTER(VOID), 'pData'),
        ([], UINT, 'Size'),
    ),
    COMMETHOD(
        [helpstring('Method EndEvent')],
        VOID,
        'EndEvent',
    ),
    COMMETHOD(
        [helpstring('Method DecodeFrame')],
        VOID,
        'DecodeFrame',
        (['in'], POINTER(ID3D12VideoDecoder), 'pDecoder'),
        (
            ['in'],
            POINTER(D3D12_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS),
            'pOutputArguments'
        ),
        (
            ['in'],
            POINTER(D3D12_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS),
            'pInputArguments'
        ),
    ),
    COMMETHOD(
        [helpstring('Method WriteBufferImmediate')],
        VOID,
        'WriteBufferImmediate',
        ([], UINT, 'Count'),
        (
            ['in'],
            POINTER(D3D12_WRITEBUFFERIMMEDIATE_PARAMETER),
            'pParams'
        ),
        (
            ['in'],
            POINTER(D3D12_WRITEBUFFERIMMEDIATE_MODE),
            'pModes'
        ),
    ),
]

IID_ID3D12VideoProcessCommandList = MIDL_INTERFACE(
    "{AEB2543A-167F-4682-ACC8-D159ED4A6209}"
)
ID3D12VideoProcessCommandList._iid_ = IID_ID3D12VideoProcessCommandList


ID3D12VideoProcessCommandList._methods_ = [
    COMMETHOD(
        [helpstring('Method Close')],
        HRESULT,
        'Close',
    ),
    COMMETHOD(
        [helpstring('Method Reset')],
        HRESULT,
        'Reset',
        (
            ['in'],
            POINTER(ID3D12CommandAllocator),
            'pAllocator'
        ),
    ),
    COMMETHOD(
        [helpstring('Method ClearState')],
        VOID,
        'ClearState',
    ),
    COMMETHOD(
        [helpstring('Method ResourceBarrier')],
        VOID,
        'ResourceBarrier',
        (['in'], UINT, 'NumBarriers'),
        (
            ['in'],
            POINTER(D3D12_RESOURCE_BARRIER),
            'pBarriers'
        ),
    ),
    COMMETHOD(
        [helpstring('Method DiscardResource')],
        VOID,
        'DiscardResource',
        (['in'], POINTER(ID3D12Resource), 'pResource'),
        (['in'], POINTER(D3D12_DISCARD_REGION), 'pRegion'),
    ),
    COMMETHOD(
        [helpstring('Method BeginQuery')],
        VOID,
        'BeginQuery',
        (['in'], POINTER(ID3D12QueryHeap), 'pQueryHeap'),
        (['in'], D3D12_QUERY_TYPE, 'Type'),
        (['in'], UINT, 'Index'),
    ),
    COMMETHOD(
        [helpstring('Method EndQuery')],
        VOID,
        'EndQuery',
        (['in'], POINTER(ID3D12QueryHeap), 'pQueryHeap'),
        (['in'], D3D12_QUERY_TYPE, 'Type'),
        (['in'], UINT, 'Index'),
    ),
    COMMETHOD(
        [helpstring('Method ResolveQueryData')],
        VOID,
        'ResolveQueryData',
        (['in'], POINTER(ID3D12QueryHeap), 'pQueryHeap'),
        (['in'], D3D12_QUERY_TYPE, 'Type'),
        (['in'], UINT, 'StartIndex'),
        (['in'], UINT, 'NumQueries'),
        (
            ['in'],
            POINTER(ID3D12Resource),
            'pDestinationBuffer'
        ),
        (['in'], UINT64, 'AlignedDestinationBufferOffset'),
    ),
    COMMETHOD(
        [helpstring('Method SetPredication')],
        VOID,
        'SetPredication',
        (['in'], POINTER(ID3D12Resource), 'pBuffer'),
        (['in'], UINT64, 'AlignedBufferOffset'),
        (['in'], D3D12_PREDICATION_OP, 'Operation'),
    ),
    COMMETHOD(
        [helpstring('Method SetMarker')],
        VOID,
        'SetMarker',
        ([], UINT, 'Metadata'),
        (['in'], POINTER(VOID), 'pData'),
        ([], UINT, 'Size'),
    ),
    COMMETHOD(
        [helpstring('Method BeginEvent')],
        VOID,
        'BeginEvent',
        ([], UINT, 'Metadata'),
        (['in'], POINTER(VOID), 'pData'),
        ([], UINT, 'Size'),
    ),
    COMMETHOD(
        [helpstring('Method EndEvent')],
        VOID,
        'EndEvent',
    ),
    COMMETHOD(
        [helpstring('Method ProcessFrames')],
        VOID,
        'ProcessFrames',
        (
            ['in'],
            POINTER(ID3D12VideoProcessor),
            'pVideoProcessor'
        ),
        (
            ['in'],
            POINTER(D3D12_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS),
            'pOutputArguments'
        ),
        ([], UINT, 'NumInputStreams'),
        (
            ['in'],
            POINTER(D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS),
            'pInputArguments'
        ),
    ),
    COMMETHOD(
        [helpstring('Method WriteBufferImmediate')],
        VOID,
        'WriteBufferImmediate',
        ([], UINT, 'Count'),
        (
            ['in'],
            POINTER(D3D12_WRITEBUFFERIMMEDIATE_PARAMETER),
            'pParams'
        ),
        (
            ['in'],
            POINTER(D3D12_WRITEBUFFERIMMEDIATE_MODE),
            'pModes'
        ),
    ),
]


D3D12_VIDEO_DECODE_OUTPUT_HISTOGRAM._fields_ = [
    ('Offset', UINT64),
    ('pBuffer', POINTER(ID3D12Resource)),
]

D3D12_VIDEO_DECODE_CONVERSION_ARGUMENTS1._fields_ = [
    ('Enable', BOOL),
    ('pReferenceTexture2D', POINTER(ID3D12Resource)),
    ('ReferenceSubresource', UINT),
    ('OutputColorSpace', DXGI_COLOR_SPACE_TYPE),
    ('DecodeColorSpace', DXGI_COLOR_SPACE_TYPE),
    ('OutputWidth', UINT),
    ('OutputHeight', UINT),
]

D3D12_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS1._fields_ = [
    ('pOutputTexture2D', POINTER(ID3D12Resource)),
    ('OutputSubresource', UINT),
    ('ConversionArguments', D3D12_VIDEO_DECODE_CONVERSION_ARGUMENTS1),
    ('Histograms', D3D12_VIDEO_DECODE_OUTPUT_HISTOGRAM * 4),
]
       
   
IID_ID3D12VideoDecodeCommandList1 = MIDL_INTERFACE(
    "{D52F011B-B56E-453C-A05A-A7F311C8F472}"
)
ID3D12VideoDecodeCommandList1._iid_ = IID_ID3D12VideoDecodeCommandList1


ID3D12VideoDecodeCommandList1._methods_ = [
    COMMETHOD(
        [helpstring('Method DecodeFrame1')],
        VOID,
        'DecodeFrame1',
        (['in'], POINTER(ID3D12VideoDecoder), 'pDecoder'),
        (
            ['in'],
            POINTER(D3D12_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS1),
            'pOutputArguments'
        ),
        (
            ['in'],
            POINTER(D3D12_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS),
            'pInputArguments'
        ),
    ),
]

D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS1._fields_ = [
    ('InputStream', D3D12_VIDEO_PROCESS_INPUT_STREAM * 2),
    ('Transform', D3D12_VIDEO_PROCESS_TRANSFORM),
    ('Flags', D3D12_VIDEO_PROCESS_INPUT_STREAM_FLAGS),
    ('RateInfo', D3D12_VIDEO_PROCESS_INPUT_STREAM_RATE),
    ('FilterLevels', INT * 32),
    ('AlphaBlending', D3D12_VIDEO_PROCESS_ALPHA_BLENDING),
    ('FieldType', D3D12_VIDEO_FIELD_TYPE),
]
      
      
IID_ID3D12VideoProcessCommandList1 = MIDL_INTERFACE(
    "{542C5C4D-7596-434F-8C93-4EFA6766F267}"
)
ID3D12VideoProcessCommandList1._iid_ = IID_ID3D12VideoProcessCommandList1


ID3D12VideoProcessCommandList1._methods_ = [
    COMMETHOD(
        [helpstring('Method ProcessFrames1')],
        VOID,
        'ProcessFrames1',
        (
            ['in'],
            POINTER(ID3D12VideoProcessor),
            'pVideoProcessor'
        ),
        (
            ['in'],
            POINTER(D3D12_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS),
            'pOutputArguments'
        ),
        ([], UINT, 'NumInputStreams'),
        (
            ['in'],
            POINTER(D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS1),
            'pInputArguments'
        ),
    ),
]

        
D3D12_VIDEO_DECODE_PROFILE_MPEG2 = GUID('{EE27417F-5E28-4E65-BEEA-1D26B508ADC9}')

D3D12_VIDEO_DECODE_PROFILE_MPEG1_AND_MPEG2 = GUID('{86695F12-340E-4F04-9FD3-9253DD327460}')

D3D12_VIDEO_DECODE_PROFILE_H264 = GUID('{1B81BE68-A0C7-11D3-B984-00C04F2E73C5}')

D3D12_VIDEO_DECODE_PROFILE_H264_STEREO_PROGRESSIVE = GUID('{D79BE8DA-CF1-4C81-B82A-69A4E236F43D}')

D3D12_VIDEO_DECODE_PROFILE_H264_STEREO = GUID('{F9AACCBB-C2B6-4CFC-8779-5707B1760552}')

D3D12_VIDEO_DECODE_PROFILE_H264_MULTIVIEW = GUID('{705B9D82-76CF-49D6-B7E6-AC8872DB013C}')

D3D12_VIDEO_DECODE_PROFILE_VC1 = GUID('{1B81BEA3-A0C7-11D3-B984-00C04F2E73C5}')

D3D12_VIDEO_DECODE_PROFILE_VC1_D2010 = GUID('{1B81BEA4-A0C7-11D3-B984-00C04F2E73C5}')

D3D12_VIDEO_DECODE_PROFILE_MPEG4PT2_SIMPLE = GUID('{EFD64D74-C9E8-41D7-A5E9-E9B0E39FA319}')

D3D12_VIDEO_DECODE_PROFILE_MPEG4PT2_ADVSIMPLE_NOGMC = GUID('{ED418A9F-10D-4EDA-9AE3-9A65358D8D2E}')

D3D12_VIDEO_DECODE_PROFILE_HEVC_MAIN = GUID('{5B11D51B-2F4C-4452-BCC3-09F2A1160CC0}')

D3D12_VIDEO_DECODE_PROFILE_HEVC_MAIN10 = GUID('{107AF0E0-EF1A-4D19-ABA8-67A163073D13}')

D3D12_VIDEO_DECODE_PROFILE_VP9 = GUID('{463707F8-A1D0-4585-876D-83AA6D60B89E}')

D3D12_VIDEO_DECODE_PROFILE_VP9_10BIT_PROFILE2 = GUID('{A4C749EF-6ECF-48AA-8448-50A7A1165FF7}')

D3D12_VIDEO_DECODE_PROFILE_VP8 = GUID('{90B899EA-3A62-4705-88B3-8DF04B2744E7}')

IID_ID3D12VideoDecoderHeap = GUID('{946B7C9-EBF6-4047-BB73-8683E27DBB1F}')

IID_ID3D12VideoDevice = GUID('{1F052807-B46-4ACC-8A89-364F793718A4}')

IID_ID3D12VideoDecoder = GUID('{C59B6BDC-7720-4074-A136-17A156037470}')

IID_ID3D12VideoProcessor = GUID('{304FDB32-BEDE-410A-8545-943AC6A46138}')

IID_ID3D12VideoDecodeCommandList = GUID('{3B60536E-AD29-4E64-A269-F853837E5E53}')

IID_ID3D12VideoProcessCommandList = GUID('{AEB2543A-167F-4682-ACC8-D159ED4A6209}')

IID_ID3D12VideoDecodeCommandList1 = GUID('{D52F011B-B56E-453C-A05A-A7F311C8F472}')

IID_ID3D12VideoProcessCommandList1 = GUID('{542C5C4D-7596-434F-8C93-4EFA6766F267}')
