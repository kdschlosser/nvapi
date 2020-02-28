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

from .dxgi_format_h import *
from .d3dcommon_h import *
from ..utils import *


class D3D10_INPUT_ELEMENT_DESC(ctypes.Structure):
    pass


class D3D10_SO_DECLARATION_ENTRY(ctypes.Structure):
    pass


class D3D10_VIEWPORT(ctypes.Structure):
    pass


class D3D10_BOX(ctypes.Structure):
    pass


class D3D10_DEPTH_STENCILOP_DESC(ctypes.Structure):
    pass


class D3D10_DEPTH_STENCIL_DESC(ctypes.Structure):
    pass


class D3D10_BLEND_DESC(ctypes.Structure):
    pass


class D3D10_RASTERIZER_DESC(ctypes.Structure):
    pass


class D3D10_BUFFER_DESC(ctypes.Structure):
    pass


class D3D10_TEXTURE1D_DESC(ctypes.Structure):
    pass


class D3D10_TEXTURE2D_DESC(ctypes.Structure):
    pass


class D3D10_MAPPED_TEXTURE2D(ctypes.Structure):
    pass


class D3D10_TEXTURE3D_DESC(ctypes.Structure):
    pass


class D3D10_MAPPED_TEXTURE3D(ctypes.Structure):
    pass


class D3D10_BUFFER_SRV(ctypes.Structure):
    pass


class D3D10_TEX1D_SRV(ctypes.Structure):
    pass


class D3D10_TEX1D_ARRAY_SRV(ctypes.Structure):
    pass


class D3D10_TEX2D_SRV(ctypes.Structure):
    pass


class D3D10_TEX2D_ARRAY_SRV(ctypes.Structure):
    pass


class D3D10_TEX3D_SRV(ctypes.Structure):
    pass


class D3D10_TEXCUBE_SRV(ctypes.Structure):
    pass


class D3D10_TEX2DMS_SRV(ctypes.Structure):
    pass


class D3D10_TEX2DMS_ARRAY_SRV(ctypes.Structure):
    pass


class D3D10_SHADER_RESOURCE_VIEW_DESC(ctypes.Structure):
    pass


class D3D10_BUFFER_RTV(ctypes.Structure):
    pass


class D3D10_TEX1D_RTV(ctypes.Structure):
    pass


class D3D10_TEX1D_ARRAY_RTV(ctypes.Structure):
    pass


class D3D10_TEX2D_RTV(ctypes.Structure):
    pass


class D3D10_TEX2DMS_RTV(ctypes.Structure):
    pass


class D3D10_TEX2D_ARRAY_RTV(ctypes.Structure):
    pass


class D3D10_TEX2DMS_ARRAY_RTV(ctypes.Structure):
    pass


class D3D10_TEX3D_RTV(ctypes.Structure):
    pass


class D3D10_RENDER_TARGET_VIEW_DESC(ctypes.Structure):
    pass


class D3D10_TEX1D_DSV(ctypes.Structure):
    pass


class D3D10_TEX1D_ARRAY_DSV(ctypes.Structure):
    pass


class D3D10_TEX2D_DSV(ctypes.Structure):
    pass


class D3D10_TEX2D_ARRAY_DSV(ctypes.Structure):
    pass


class D3D10_TEX2DMS_DSV(ctypes.Structure):
    pass


class D3D10_TEX2DMS_ARRAY_DSV(ctypes.Structure):
    pass


class D3D10_DEPTH_STENCIL_VIEW_DESC(ctypes.Structure):
    pass


class D3D10_SAMPLER_DESC(ctypes.Structure):
    pass


class D3D10_QUERY_DESC(ctypes.Structure):
    pass


class D3D10_QUERY_DATA_TIMESTAMP_DISJOINT(ctypes.Structure):
    pass


class D3D10_QUERY_DATA_PIPELINE_STATISTICS(ctypes.Structure):
    pass


class D3D10_QUERY_DATA_SO_STATISTICS(ctypes.Structure):
    pass


class D3D10_COUNTER_DESC(ctypes.Structure):
    pass


class D3D10_COUNTER_INFO(ctypes.Structure):
    pass


D3D10_16BIT_INDEX_STRIP_CUT_VALUE = 0xffff
D3D10_32BIT_INDEX_STRIP_CUT_VALUE = 0xffffffff
D3D10_8BIT_INDEX_STRIP_CUT_VALUE = 0xff
D3D10_ARRAY_AXIS_ADDRESS_RANGE_BIT_COUNT = 9
D3D10_CLIP_OR_CULL_DISTANCE_COUNT = 8
D3D10_CLIP_OR_CULL_DISTANCE_ELEMENT_COUNT = 2
D3D10_COMMONSHADER_CONSTANT_BUFFER_API_SLOT_COUNT = 14
D3D10_COMMONSHADER_CONSTANT_BUFFER_COMPONENTS = 4
D3D10_COMMONSHADER_CONSTANT_BUFFER_COMPONENT_BIT_COUNT = 32
D3D10_COMMONSHADER_CONSTANT_BUFFER_HW_SLOT_COUNT = 15
D3D10_COMMONSHADER_CONSTANT_BUFFER_REGISTER_COMPONENTS = 4
D3D10_COMMONSHADER_CONSTANT_BUFFER_REGISTER_COUNT = 15
D3D10_COMMONSHADER_CONSTANT_BUFFER_REGISTER_READS_PER_INST = 1
D3D10_COMMONSHADER_CONSTANT_BUFFER_REGISTER_READ_PORTS = 1
D3D10_COMMONSHADER_FLOWCONTROL_NESTING_LIMIT = 64
D3D10_COMMONSHADER_IMMEDIATE_CONSTANT_BUFFER_REGISTER_COMPONENTS = 4
D3D10_COMMONSHADER_IMMEDIATE_CONSTANT_BUFFER_REGISTER_COUNT = 1
D3D10_COMMONSHADER_IMMEDIATE_CONSTANT_BUFFER_REGISTER_READS_PER_INST = 1
D3D10_COMMONSHADER_IMMEDIATE_CONSTANT_BUFFER_REGISTER_READ_PORTS = 1
D3D10_COMMONSHADER_IMMEDIATE_VALUE_COMPONENT_BIT_COUNT = 32
D3D10_COMMONSHADER_INPUT_RESOURCE_REGISTER_COMPONENTS = 1
D3D10_COMMONSHADER_INPUT_RESOURCE_REGISTER_COUNT = 128
D3D10_COMMONSHADER_INPUT_RESOURCE_REGISTER_READS_PER_INST = 1
D3D10_COMMONSHADER_INPUT_RESOURCE_REGISTER_READ_PORTS = 1
D3D10_COMMONSHADER_INPUT_RESOURCE_SLOT_COUNT = 128
D3D10_COMMONSHADER_SAMPLER_REGISTER_COMPONENTS = 1
D3D10_COMMONSHADER_SAMPLER_REGISTER_COUNT = 16
D3D10_COMMONSHADER_SAMPLER_REGISTER_READS_PER_INST = 1
D3D10_COMMONSHADER_SAMPLER_REGISTER_READ_PORTS = 1
D3D10_COMMONSHADER_SAMPLER_SLOT_COUNT = 16
D3D10_COMMONSHADER_SUBROUTINE_NESTING_LIMIT = 32
D3D10_COMMONSHADER_TEMP_REGISTER_COMPONENTS = 4
D3D10_COMMONSHADER_TEMP_REGISTER_COMPONENT_BIT_COUNT = 32
D3D10_COMMONSHADER_TEMP_REGISTER_COUNT = 4096
D3D10_COMMONSHADER_TEMP_REGISTER_READS_PER_INST = 3
D3D10_COMMONSHADER_TEMP_REGISTER_READ_PORTS = 3
D3D10_COMMONSHADER_TEXCOORD_RANGE_REDUCTION_MAX = 10
D3D10_COMMONSHADER_TEXCOORD_RANGE_REDUCTION_MIN = -10
D3D10_COMMONSHADER_TEXEL_OFFSET_MAX_NEGATIVE = -8
D3D10_COMMONSHADER_TEXEL_OFFSET_MAX_POSITIVE = 7
D3D10_DEFAULT_BLEND_FACTOR_ALPHA = 1.0
D3D10_DEFAULT_BLEND_FACTOR_BLUE = 1.0
D3D10_DEFAULT_BLEND_FACTOR_GREEN = 1.0
D3D10_DEFAULT_BLEND_FACTOR_RED = 1.0
D3D10_DEFAULT_BORDER_COLOR_COMPONENT = 0.0
D3D10_DEFAULT_DEPTH_BIAS = 0
D3D10_DEFAULT_DEPTH_BIAS_CLAMP = 0.0
D3D10_DEFAULT_MAX_ANISOTROPY = 16.0
D3D10_DEFAULT_MIP_LOD_BIAS = 0.0
D3D10_DEFAULT_RENDER_TARGET_ARRAY_INDEX = 0
D3D10_DEFAULT_SAMPLE_MASK = 0xffffffff
D3D10_DEFAULT_SCISSOR_ENDX = 0
D3D10_DEFAULT_SCISSOR_ENDY = 0
D3D10_DEFAULT_SCISSOR_STARTX = 0
D3D10_DEFAULT_SCISSOR_STARTY = 0
D3D10_DEFAULT_SLOPE_SCALED_DEPTH_BIAS = 0.0
D3D10_DEFAULT_STENCIL_READ_MASK = 0xff
D3D10_DEFAULT_STENCIL_REFERENCE = 0
D3D10_DEFAULT_STENCIL_WRITE_MASK = 0xff
D3D10_DEFAULT_VIEWPORT_AND_SCISSORRECT_INDEX = 0
D3D10_DEFAULT_VIEWPORT_HEIGHT = 0
D3D10_DEFAULT_VIEWPORT_MAX_DEPTH = 0.0
D3D10_DEFAULT_VIEWPORT_MIN_DEPTH = 0.0
D3D10_DEFAULT_VIEWPORT_TOPLEFTX = 0
D3D10_DEFAULT_VIEWPORT_TOPLEFTY = 0
D3D10_DEFAULT_VIEWPORT_WIDTH = 0
D3D10_FLOAT16_FUSED_TOLERANCE_IN_ULP = 0.6
D3D10_FLOAT32_MAX = 3.402823466e+38
D3D10_FLOAT32_TO_INTEGER_TOLERANCE_IN_ULP = 0.6
D3D10_FLOAT_TO_SRGB_EXPONENT_DENOMINATOR = 2.4
D3D10_FLOAT_TO_SRGB_EXPONENT_NUMERATOR = 1.0
D3D10_FLOAT_TO_SRGB_OFFSET = 0.055
D3D10_FLOAT_TO_SRGB_SCALE_1 = 12.92
D3D10_FLOAT_TO_SRGB_SCALE_2 = 1.055
D3D10_FLOAT_TO_SRGB_THRESHOLD = 0.0031308
D3D10_FTOI_INSTRUCTION_MAX_INPUT = 2147483647.999
D3D10_FTOI_INSTRUCTION_MIN_INPUT = -2147483648.999
D3D10_FTOU_INSTRUCTION_MAX_INPUT = 4294967295.999
D3D10_FTOU_INSTRUCTION_MIN_INPUT = 0.0
D3D10_GS_INPUT_PRIM_CONST_REGISTER_COMPONENTS = 1
D3D10_GS_INPUT_PRIM_CONST_REGISTER_COMPONENT_BIT_COUNT = 32
D3D10_GS_INPUT_PRIM_CONST_REGISTER_COUNT = 1
D3D10_GS_INPUT_PRIM_CONST_REGISTER_READS_PER_INST = 2
D3D10_GS_INPUT_PRIM_CONST_REGISTER_READ_PORTS = 1
D3D10_GS_INPUT_REGISTER_COMPONENTS = 4
D3D10_GS_INPUT_REGISTER_COMPONENT_BIT_COUNT = 32
D3D10_GS_INPUT_REGISTER_COUNT = 16
D3D10_GS_INPUT_REGISTER_READS_PER_INST = 2
D3D10_GS_INPUT_REGISTER_READ_PORTS = 1
D3D10_GS_INPUT_REGISTER_VERTICES = 6
D3D10_GS_OUTPUT_ELEMENTS = 32
D3D10_GS_OUTPUT_REGISTER_COMPONENTS = 4
D3D10_GS_OUTPUT_REGISTER_COMPONENT_BIT_COUNT = 32
D3D10_GS_OUTPUT_REGISTER_COUNT = 32
D3D10_IA_DEFAULT_INDEX_BUFFER_OFFSET_IN_BYTES = 0
D3D10_IA_DEFAULT_PRIMITIVE_TOPOLOGY = 0
D3D10_IA_DEFAULT_VERTEX_BUFFER_OFFSET_IN_BYTES = 0
D3D10_IA_INDEX_INPUT_RESOURCE_SLOT_COUNT = 1
D3D10_IA_INSTANCE_ID_BIT_COUNT = 32
D3D10_IA_INTEGER_ARITHMETIC_BIT_COUNT = 32
D3D10_IA_PRIMITIVE_ID_BIT_COUNT = 32
D3D10_IA_VERTEX_ID_BIT_COUNT = 32
D3D10_IA_VERTEX_INPUT_RESOURCE_SLOT_COUNT = 16
D3D10_IA_VERTEX_INPUT_STRUCTURE_ELEMENTS_COMPONENTS = 64
D3D10_IA_VERTEX_INPUT_STRUCTURE_ELEMENT_COUNT = 16
D3D10_INTEGER_DIVIDE_BY_ZERO_QUOTIENT = 0xffffffff
D3D10_INTEGER_DIVIDE_BY_ZERO_REMAINDER = 0xffffffff
D3D10_LINEAR_GAMMA = 1.0
D3D10_MAX_BORDER_COLOR_COMPONENT = 1.0
D3D10_MAX_DEPTH = 1.0
D3D10_MAX_MAXANISOTROPY = 16
D3D10_MAX_MULTISAMPLE_SAMPLE_COUNT = 32
D3D10_MAX_POSITION_VALUE = 3.402823466e+34
D3D10_MAX_TEXTURE_DIMENSION_2_TO_EXP = 17
D3D10_MIN_BORDER_COLOR_COMPONENT = 0.0
D3D10_MIN_DEPTH = 0.0
D3D10_MIN_MAXANISOTROPY = 0
D3D10_MIP_LOD_BIAS_MAX = 15.99
D3D10_MIP_LOD_BIAS_MIN = -16.0
D3D10_MIP_LOD_FRACTIONAL_BIT_COUNT = 6
D3D10_MIP_LOD_RANGE_BIT_COUNT = 8
D3D10_MULTISAMPLE_ANTIALIAS_LINE_WIDTH = 1.4
D3D10_NONSAMPLE_FETCH_OUT_OF_RANGE_ACCESS_RESULT = 0
D3D10_PIXEL_ADDRESS_RANGE_BIT_COUNT = 13
D3D10_PRE_SCISSOR_PIXEL_ADDRESS_RANGE_BIT_COUNT = 15
D3D10_PS_FRONTFACING_DEFAULT_VALUE = 0xFFFFFFFF
D3D10_PS_FRONTFACING_FALSE_VALUE = 0x00000000
D3D10_PS_FRONTFACING_TRUE_VALUE = 0xFFFFFFFF
D3D10_PS_INPUT_REGISTER_COMPONENTS = 4
D3D10_PS_INPUT_REGISTER_COMPONENT_BIT_COUNT = 32
D3D10_PS_INPUT_REGISTER_COUNT = 32
D3D10_PS_INPUT_REGISTER_READS_PER_INST = 2
D3D10_PS_INPUT_REGISTER_READ_PORTS = 1
D3D10_PS_LEGACY_PIXEL_CENTER_FRACTIONAL_COMPONENT = 0.0
D3D10_PS_OUTPUT_DEPTH_REGISTER_COMPONENTS = 1
D3D10_PS_OUTPUT_DEPTH_REGISTER_COMPONENT_BIT_COUNT = 32
D3D10_PS_OUTPUT_DEPTH_REGISTER_COUNT = 1
D3D10_PS_OUTPUT_REGISTER_COMPONENTS = 4
D3D10_PS_OUTPUT_REGISTER_COMPONENT_BIT_COUNT = 32
D3D10_PS_OUTPUT_REGISTER_COUNT = 8
D3D10_PS_PIXEL_CENTER_FRACTIONAL_COMPONENT = 0.5
D3D10_REQ_BLEND_OBJECT_COUNT_PER_CONTEXT = 4096
D3D10_REQ_BUFFER_RESOURCE_TEXEL_COUNT_2_TO_EXP = 27
D3D10_REQ_CONSTANT_BUFFER_ELEMENT_COUNT = 4096
D3D10_REQ_DEPTH_STENCIL_OBJECT_COUNT_PER_CONTEXT = 4096
D3D10_REQ_DRAWINDEXED_INDEX_COUNT_2_TO_EXP = 32
D3D10_REQ_DRAW_VERTEX_COUNT_2_TO_EXP = 32
D3D10_REQ_FILTERING_HW_ADDRESSABLE_RESOURCE_DIMENSION = 8192
D3D10_REQ_GS_INVOCATION_32BIT_OUTPUT_COMPONENT_LIMIT = 1024
D3D10_REQ_IMMEDIATE_CONSTANT_BUFFER_ELEMENT_COUNT = 4096
D3D10_REQ_MAXANISOTROPY = 16
D3D10_REQ_MIP_LEVELS = 14
D3D10_REQ_MULTI_ELEMENT_STRUCTURE_SIZE_IN_BYTES = 2048
D3D10_REQ_RASTERIZER_OBJECT_COUNT_PER_CONTEXT = 4096
D3D10_REQ_RENDER_TO_BUFFER_WINDOW_WIDTH = 8192
D3D10_REQ_RESOURCE_SIZE_IN_MEGABYTES = 128
D3D10_REQ_RESOURCE_VIEW_COUNT_PER_CONTEXT_2_TO_EXP = 20
D3D10_REQ_SAMPLER_OBJECT_COUNT_PER_CONTEXT = 4096
D3D10_REQ_TEXTURE1D_ARRAY_AXIS_DIMENSION = 512
D3D10_REQ_TEXTURE1D_U_DIMENSION = 8192
D3D10_REQ_TEXTURE2D_ARRAY_AXIS_DIMENSION = 512
D3D10_REQ_TEXTURE2D_U_OR_V_DIMENSION = 8192
D3D10_REQ_TEXTURE3D_U_V_OR_W_DIMENSION = 2048
D3D10_REQ_TEXTURECUBE_DIMENSION = 8192
D3D10_RESINFO_INSTRUCTION_MISSING_COMPONENT_RETVAL = 0
D3D10_SHADER_MAJOR_VERSION = 4
D3D10_SHADER_MINOR_VERSION = 0
D3D10_SHIFT_INSTRUCTION_PAD_VALUE = 0
D3D10_SHIFT_INSTRUCTION_SHIFT_VALUE_BIT_COUNT = 5
D3D10_SIMULTANEOUS_RENDER_TARGET_COUNT = 8
D3D10_SO_BUFFER_MAX_STRIDE_IN_BYTES = 2048
D3D10_SO_BUFFER_MAX_WRITE_WINDOW_IN_BYTES = 256
D3D10_SO_BUFFER_SLOT_COUNT = 4
D3D10_SO_DDI_REGISTER_INDEX_DENOTING_GAP = 0xffffffff
D3D10_SO_MULTIPLE_BUFFER_ELEMENTS_PER_BUFFER = 1
D3D10_SO_SINGLE_BUFFER_COMPONENT_LIMIT = 64
D3D10_SRGB_GAMMA = 2.2
D3D10_SRGB_TO_FLOAT_DENOMINATOR_1 = 12.92
D3D10_SRGB_TO_FLOAT_DENOMINATOR_2 = 1.055
D3D10_SRGB_TO_FLOAT_EXPONENT = 2.4
D3D10_SRGB_TO_FLOAT_OFFSET = 0.055
D3D10_SRGB_TO_FLOAT_THRESHOLD = 0.04045
D3D10_SRGB_TO_FLOAT_TOLERANCE_IN_ULP = 0.5
D3D10_STANDARD_COMPONENT_BIT_COUNT = 32
D3D10_STANDARD_COMPONENT_BIT_COUNT_DOUBLED = 64
D3D10_STANDARD_MAXIMUM_ELEMENT_ALIGNMENT_BYTE_MULTIPLE = 4
D3D10_STANDARD_PIXEL_COMPONENT_COUNT = 128
D3D10_STANDARD_PIXEL_ELEMENT_COUNT = 32
D3D10_STANDARD_VECTOR_SIZE = 4
D3D10_STANDARD_VERTEX_ELEMENT_COUNT = 16
D3D10_STANDARD_VERTEX_TOTAL_COMPONENT_COUNT = 64
D3D10_SUBPIXEL_FRACTIONAL_BIT_COUNT = 8
D3D10_SUBTEXEL_FRACTIONAL_BIT_COUNT = 6
D3D10_TEXEL_ADDRESS_RANGE_BIT_COUNT = 18
D3D10_UNBOUND_MEMORY_ACCESS_RESULT = 0
D3D10_VIEWPORT_AND_SCISSORRECT_MAX_INDEX = 15
D3D10_VIEWPORT_AND_SCISSORRECT_OBJECT_COUNT_PER_PIPELINE = 16
D3D10_VIEWPORT_BOUNDS_MAX = 16383
D3D10_VIEWPORT_BOUNDS_MIN = -16384
D3D10_VS_INPUT_REGISTER_COMPONENTS = 4
D3D10_VS_INPUT_REGISTER_COMPONENT_BIT_COUNT = 32
D3D10_VS_INPUT_REGISTER_COUNT = 16
D3D10_VS_INPUT_REGISTER_READS_PER_INST = 2
D3D10_VS_INPUT_REGISTER_READ_PORTS = 1
D3D10_VS_OUTPUT_REGISTER_COMPONENTS = 4
D3D10_VS_OUTPUT_REGISTER_COMPONENT_BIT_COUNT = 32
D3D10_VS_OUTPUT_REGISTER_COUNT = 16
D3D10_WHQL_CONTEXT_COUNT_FOR_RESOURCE_LIMIT = 10
D3D10_WHQL_DRAWINDEXED_INDEX_COUNT_2_TO_EXP = 25
D3D10_WHQL_DRAW_VERTEX_COUNT_2_TO_EXP = 25
D3D_MAJOR_VERSION = 10
D3D_MINOR_VERSION = 0
D3D_SPEC_DATE_DAY = 8
D3D_SPEC_DATE_MONTH = 8
D3D_SPEC_DATE_YEAR = 2006

_FACD3D10 = 0x879
_FACD3D10DEBUG = _FACD3D10 + 1


def MAKE_HRESULT(sev, fac, code):
    return (sev << 31) | (fac << 16) | code


def MAKE_D3D10_HRESULT(code):
    return MAKE_HRESULT(1, _FACD3D10, code)


def MAKE_D3D10_STATUS(code):
    return MAKE_HRESULT(0, _FACD3D10, code)


class D3D10_COUNTER_TYPE(ENUM):
    D3D10_COUNTER_TYPE_FLOAT32 = 0
    D3D10_COUNTER_TYPE_UINT16 = 1
    D3D10_COUNTER_TYPE_UINT32 = 2
    D3D10_COUNTER_TYPE_UINT64 = 3


class D3D10_SUBRESOURCE_DATA(ctypes.Structure):
    _fields_ = [
        ('pSysMem', POINTER(VOID)),
        ('SysMemPitch', UINT),
        ('SysMemSlicePitch', UINT)
    ]


class ID3D10Device(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = None


class ID3D10DeviceChild(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10DepthStencilState(ID3D10DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10BlendState(ID3D10DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10RasterizerState(ID3D10DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10Resource(ID3D10DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10Buffer(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10Texture1D(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10Texture2D(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10Texture3D(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10View(ID3D10DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10ShaderResourceView(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10RenderTargetView(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10DepthStencilView(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10VertexShader(ID3D10DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10GeometryShader(ID3D10DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10PixelShader(ID3D10DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10InputLayout(ID3D10DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10SamplerState(ID3D10DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10Asynchronous(ID3D10DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10Query(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10Predicate(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10Counter(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []



D3D10_PRIMITIVE_TOPOLOGY = D3D_PRIMITIVE_TOPOLOGY
D3D10_PRIMITIVE = D3D_PRIMITIVE

ID3D10Device._methods_ = [
    # not not not Order of functions is in decreasing order of
    # priority ( as far as performance is concerned ) not not not
    # not not not BEGIN HIGH-FREQUENCY not not not
    #        
    COMMETHOD(
        [],
        VOID,
        'VSSetConstantBuffers',
        (
            ['in'],
            UINT,
            'StartSlot'
        ),
        (
            ['in'],
            UINT,
            'NumBuffers'
        ),
        (
            ['in'],
            POINTER(ID3D10Buffer),
            'ppConstantBuffers'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'PSSetShaderResources',
        (
            ['in'],
            UINT,
            'StartSlot'
        ),
        (
            ['in'],
            UINT,
            'NumViews'
        ),
        (
            ['in'],
            POINTER(ID3D10ShaderResourceView),
            'ppShaderResourceViews'
        ),
    ),
    COMMETHOD(
        [],
        VOID,
        'PSSetShader',
        (
            ['in'],
            POINTER(ID3D10PixelShader),
            'pPixelShader'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'PSSetSamplers',
        (
            ['in'],
            UINT,
            'StartSlot'
        ),
        (
            ['in'],
            UINT,
            'NumSamplers'
        ),
        (
            ['in'],
            POINTER(ID3D10SamplerState),
            'ppSamplers'
        ),
    ),
    COMMETHOD(
        [],
        VOID,
        'VSSetShader',
        (
            ['in'],
            POINTER(ID3D10VertexShader),
            'pVertexShader'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'DrawIndexed',
        (['in'], UINT, 'IndexCount'),
        (['in'], UINT, 'StartIndexLocation'),
        (['in'], INT, 'BaseVertexLocation'),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'Draw',
        (['in'], UINT, 'VertexCount'),
        (['in'], UINT, 'StartVertexLocation'),
    ),
    # CB Lock/ Dynamic Lock & Unlock
    #        
    COMMETHOD(
        [],
        VOID,
        'PSSetConstantBuffers',
        (
            ['in'],
            UINT,
            'StartSlot'
        ),
        (
            ['in'],
            UINT,
            'NumBuffers'
        ),
        (
            ['in'],
            POINTER(ID3D10Buffer),
            'ppConstantBuffers'
        ),
    ),
    COMMETHOD(
        [],
        VOID,
        'IASetInputLayout',
        (
            ['in'],
            POINTER(ID3D10InputLayout),
            'pInputLayout'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'IASetVertexBuffers',
        (
            ['in'],
            UINT,
            'StartSlot'
        ),
        (
            ['in'],
            UINT,
            'NumBuffers'
        ),
        (
            ['in'],
            POINTER(ID3D10Buffer),
            'ppVertexBuffers'
        ),
        (['in'], POINTER(UINT), 'pStrides'),
        (['in'], POINTER(UINT), 'pOffsets'),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'IASetIndexBuffer',
        (
            ['in'],
            POINTER(ID3D10Buffer),
            'pIndexBuffer'
        ),
        (['in'], DXGI_FORMAT, 'Format'),
        (['in'], UINT, 'Offset'),
    ),
    # not not not END HIGH-FREQUENCY not not not
    # not not not Order of functions is in decreasing order of
    # priority ( as far as performance is concerned ) not not not
    # not not not BEGIN MIDDLE-FREQUENCY not not not
    #        
    COMMETHOD(
        [],
        VOID,
        'DrawIndexedInstanced',
        (['in'], UINT, 'IndexCountPerInstance'),
        (['in'], UINT, 'InstanceCount'),
        (['in'], UINT, 'StartIndexLocation'),
        (['in'], INT, 'BaseVertexLocation'),
        (['in'], UINT, 'StartInstanceLocation'),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'DrawInstanced',
        (['in'], UINT, 'VertexCountPerInstance'),
        (['in'], UINT, 'InstanceCount'),
        (['in'], UINT, 'StartVertexLocation'),
        (['in'], UINT, 'StartInstanceLocation'),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'GSSetConstantBuffers',
        (
            ['in'],
            UINT,
            'StartSlot'
        ),
        (
            ['in'],
            UINT,
            'NumBuffers'
        ),
        (
            ['in'],
            POINTER(ID3D10Buffer),
            'ppConstantBuffers'
        ),
    ),
    COMMETHOD(
        [],
        VOID,
        'GSSetShader',
        (
            ['in'],
            POINTER(ID3D10GeometryShader),
            'pShader'
        ),
    ),
    COMMETHOD(
        [],
        VOID,
        'IASetPrimitiveTopology',
        (
            ['in'],
            D3D10_PRIMITIVE_TOPOLOGY,
            'Topology'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'VSSetShaderResources',
        (
            ['in'],
            UINT,
            'StartSlot'
        ),
        (
            ['in'],
            UINT,
            'NumViews'
        ),
        (
            ['in'],
            POINTER(ID3D10ShaderResourceView),
            'ppShaderResourceViews'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'VSSetSamplers',
        (
            ['in'],
            UINT,
            'StartSlot'
        ),
        (
            ['in'],
            UINT,
            'NumSamplers'
        ),
        (
            ['in'],
            POINTER(ID3D10SamplerState),
            'ppSamplers'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'SetPredication',
        (
            ['in'],
            POINTER(ID3D10Predicate),
            'pPredicate'
        ),
        (['in'], BOOL, 'PredicateValue'),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'GSSetShaderResources',
        (
            ['in'],
            UINT,
            'StartSlot'
        ),
        (
            ['in'],
            UINT,
            'NumViews'
        ),
        (
            ['in'],
            POINTER(ID3D10ShaderResourceView),
            'ppShaderResourceViews'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'GSSetSamplers',
        (
            ['in'],
            UINT,
            'StartSlot'
        ),
        (
            ['in'],
            UINT,
            'NumSamplers'
        ),
        (
            ['in'],
            POINTER(ID3D10SamplerState),
            'ppSamplers'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'OMSetRenderTargets',
        (
            ['in'],
            UINT,
            'NumViews'
        ),
        (
            ['in'],
            POINTER(ID3D10RenderTargetView),
            'ppRenderTargetViews'
        ),
        (
            ['in'],
            POINTER(ID3D10DepthStencilView),
            'pDepthStencilView'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'OMSetBlendState',
        (
            ['in'],
            POINTER(ID3D10BlendState),
            'pBlendState'
        ),
        (['in'], FLOAT * 4, 'BlendFactor'),
        (['in'], UINT, 'SampleMask'),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'OMSetDepthStencilState',
        (
            ['in'],
            POINTER(ID3D10DepthStencilState),
            'pDepthStencilState'
        ),
        (['in'], UINT, 'StencilRef'),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'SOSetTargets',
        (
            ['in'],
            UINT,
            'NumBuffers'
        ),
        (
            ['in'],
            POINTER(ID3D10Buffer),
            'ppSOTargets'
        ),
        (['in'], POINTER(UINT), 'pOffsets'),
    ),
    COMMETHOD(
        [],
        VOID,
        'DrawAuto',
    ),
    COMMETHOD(
        [],
        VOID,
        'RSSetState',
        (
            ['in'],
            POINTER(ID3D10RasterizerState),
            'pRasterizerState'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'RSSetViewports',
        (
            ['in'],
            UINT,
            'NumViewports'
        ),
        (
            ['in'],
            POINTER(D3D10_VIEWPORT),
            'pViewports'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'RSSetScissorRects',
        (
            ['in'],
            UINT,
            'NumRects'
        ),
        (
            ['in'],
            POINTER(D3D10_RECT),
            'pRects'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'CopySubresourceRegion',
        (
            ['in'],
            POINTER(ID3D10Resource),
            'pDstResource'
        ),
        (['in'], UINT, 'DstSubresource'),
        (['in'], UINT, 'DstX'),
        (['in'], UINT, 'DstY'),
        (['in'], UINT, 'DstZ'),
        (['in'], POINTER(ID3D10Resource), 'pSrcResource'),
        (['in'], UINT, 'SrcSubresource'),
        (
            ['in'],
            POINTER(D3D10_BOX),
            'pSrcBox'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'CopyResource',
        (
            ['in'],
            POINTER(ID3D10Resource),
            'pDstResource'
        ),
        (['in'], POINTER(ID3D10Resource), 'pSrcResource'),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'UpdateSubresource',
        (
            ['in'],
            POINTER(ID3D10Resource),
            'pDstResource'
        ),
        (['in'], UINT, 'DstSubresource'),
        (
            ['in'],
            POINTER(D3D10_BOX),
            'pDstBox'
        ),
        (['in'], POINTER(VOID), 'pSrcData'),
        (['in'], UINT, 'SrcRowPitch'),
        (['in'], UINT, 'SrcDepthPitch'),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'ClearRenderTargetView',
        (
            ['in'],
            POINTER(ID3D10RenderTargetView),
            'pRenderTargetView'
        ),
        (['in'], FLOAT * 4, 'ColorRGBA'),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'ClearDepthStencilView',
        (
            ['in'],
            POINTER(ID3D10DepthStencilView),
            'pDepthStencilView'
        ),
        (['in'], UINT, 'ClearFlags'),
        (['in'], FLOAT, 'Depth'),
        (['in'], UINT8, 'Stencil'),
    ),
    COMMETHOD(
        [],
        VOID,
        'GenerateMips',
        (
            ['in'],
            POINTER(ID3D10ShaderResourceView),
            'pShaderResourceView'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'ResolveSubresource',
        (
            ['in'],
            POINTER(ID3D10Resource),
            'pDstResource'
        ),
        (['in'], UINT, 'DstSubresource'),
        (['in'], POINTER(ID3D10Resource), 'pSrcResource'),
        (['in'], UINT, 'SrcSubresource'),
        (['in'], DXGI_FORMAT, 'Format'),
    ),
    # GET functions
    #        
    COMMETHOD(
        [],
        VOID,
        'VSGetConstantBuffers',
        (
            ['in'],
            UINT,
            'StartSlot'
        ),
        (
            ['in'],
            UINT,
            'NumBuffers'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10Buffer)),
            'ppConstantBuffers'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'PSGetShaderResources',
        (
            ['in'],
            UINT,
            'StartSlot'
        ),
        (
            ['in'],
            UINT,
            'NumViews'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10ShaderResourceView)),
            'ppShaderResourceViews'
        ),
    ),
    COMMETHOD(
        [],
        VOID,
        'PSGetShader',
        (
            ['out'],
            POINTER(POINTER(ID3D10PixelShader)),
            'ppPixelShader'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'PSGetSamplers',
        (
            ['in'],
            UINT,
            'StartSlot'
        ),
        (
            ['in'],
            UINT,
            'NumSamplers'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10SamplerState)),
            'ppSamplers'
        ),
    ),
    COMMETHOD(
        [],
        VOID,
        'VSGetShader',
        (
            ['out'],
            POINTER(POINTER(ID3D10VertexShader)),
            'ppVertexShader'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'PSGetConstantBuffers',
        (
            ['in'],
            UINT,
            'StartSlot'
        ),
        (
            ['in'],
            UINT,
            'NumBuffers'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10Buffer)),
            'ppConstantBuffers'
        ),
    ),
    COMMETHOD(
        [],
        VOID,
        'IAGetInputLayout',
        (
            ['out'],
            POINTER(POINTER(ID3D10InputLayout)),
            'ppInputLayout'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'IAGetVertexBuffers',
        (
            ['in'],
            UINT,
            'StartSlot'
        ),
        (
            ['in'],
            UINT,
            'NumBuffers'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10Buffer)),
            'ppVertexBuffers'
        ),
        (['in'], POINTER(UINT), 'pStrides'),
        (['in'], POINTER(UINT), 'pOffsets'),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'IAGetIndexBuffer',
        (
            ['out'],
            POINTER(POINTER(ID3D10Buffer)),
            'pIndexBuffer'
        ),
        (['in'], POINTER(DXGI_FORMAT), 'Format'),
        (['in'], POINTER(UINT), 'Offset'),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'GSGetConstantBuffers',
        (
            ['in'],
            UINT,
            'StartSlot'
        ),
        (
            ['in'],
            UINT,
            'NumBuffers'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10Buffer)),
            'ppConstantBuffers'
        ),
    ),
    COMMETHOD(
        [],
        VOID,
        'GSGetShader',
        (
            ['out'],
            POINTER(POINTER(ID3D10GeometryShader)),
            'ppGeometryShader'
        ),
    ),
    COMMETHOD(
        [],
        VOID,
        'IAGetPrimitiveTopology',
        (
            ['out'],
            POINTER(D3D10_PRIMITIVE_TOPOLOGY),
            'pTopology'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'VSGetShaderResources',
        (
            ['in'],
            UINT,
            'StartSlot'
        ),
        (
            ['in'],
            UINT,
            'NumViews'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10ShaderResourceView)),
            'ppShaderResourceViews'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'VSGetSamplers',
        (
            ['in'],
            UINT,
            'StartSlot'
        ),
        (
            ['in'],
            UINT,
            'NumSamplers'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10SamplerState)),
            'ppSamplers'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'GetPredication',
        (
            ['out'],
            POINTER(POINTER(ID3D10Predicate)),
            'ppPredicate'
        ),
        (['in'], POINTER(BOOL), 'pPredicateValue'),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'GSGetShaderResources',
        (
            ['in'],
            UINT,
            'StartSlot'
        ),
        (
            ['in'],
            UINT,
            'NumViews'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10ShaderResourceView)),
            'ppShaderResourceViews'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'GSGetSamplers',
        (
            ['in'],
            UINT,
            'StartSlot'
        ),
        (
            ['in'],
            UINT,
            'NumSamplers'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10SamplerState)),
            'ppSamplers'
        ),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'OMGetRenderTargets',
        (
            ['in'],
            UINT,
            'NumViews'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10RenderTargetView)),
            'ppRenderTargetViews'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10DepthStencilView)),
            'ppDepthStencilView'
        ),
    ),
    # 4        
    COMMETHOD(
        [],
        VOID,
        'OMGetBlendState',
        (
            ['out'],
            POINTER(POINTER(ID3D10BlendState)),
            'ppBlendState'
        ),
        (['in'], FLOAT * 4, 'BlendFactor'),
        (['in'], POINTER(UINT), 'pSampleMask'),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'OMGetDepthStencilState',
        (
            ['out'],
            POINTER(POINTER(ID3D10DepthStencilState)),
            'ppDepthStencilState'
        ),
        (['in'], POINTER(UINT), 'pStencilRef'),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'SOGetTargets',
        (
            ['in'],
            UINT,
            'NumBuffers'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10Buffer)),
            'ppSOTargets'
        ),
        (['in'], POINTER(UINT), 'pOffsets'),
    ),
    COMMETHOD(
        [],
        VOID,
        'RSGetState',
        (
            ['out'],
            POINTER(POINTER(ID3D10RasterizerState)),
            'ppRasterizerState'
        ),
    ),
    # _range(0, D3D10_VIEWPORT_AND_SCISSORRECT_OBJECT_COUNT_PER_PIPELINE )
    #         
    COMMETHOD(
        [],
        VOID,
        'RSGetViewports',
        (
            ['out', 'in'],
            POINTER(UINT),
            'NumViewports'
        ),
        (
            ['out'],
            POINTER(D3D10_VIEWPORT),
            'pViewports'
        ),
    ),
    # _range(0, D3D10_VIEWPORT_AND_SCISSORRECT_OBJECT_COUNT_PER_PIPELINE )
    #         
    COMMETHOD(
        [],
        VOID,
        'RSGetScissorRects',
        (
            ['out', 'in'],
            POINTER(UINT),
            'NumRects'
        ),
        (
            ['out'],
            POINTER(D3D10_RECT),
            'pRects'
        ),
    ),
    # /GET functions        
    COMMETHOD(
        [],
        HRESULT,
        'GetDeviceRemovedReason',
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
        VOID,
        'ClearState',
    ),
    COMMETHOD(
        [],
        VOID,
        'Flush',
    ),
    # not not not END MIDDLE-FREQUENCY not not not
    # not not not Order of functions is in decreasing order of
    # priority ( as far as performance is concerned ) not not not
    # not not not BEGIN LOW-FREQUENCY not not not
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateBuffer',
        (
            ['in'],
            POINTER(D3D10_BUFFER_DESC),
            'pDesc'
        ),
        (
            ['in'],
            POINTER(D3D10_SUBRESOURCE_DATA),
            'pInitialData'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10Buffer)),
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
            POINTER(D3D10_TEXTURE1D_DESC),
            'pDesc'
        ),
        (
            ['in'],
            POINTER(D3D10_SUBRESOURCE_DATA),
            'pInitialData'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10Texture1D)),
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
            POINTER(D3D10_TEXTURE2D_DESC),
            'pDesc'
        ),
        (
            ['in'],
            POINTER(D3D10_SUBRESOURCE_DATA),
            'pInitialData'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10Texture2D)),
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
            POINTER(D3D10_TEXTURE3D_DESC),
            'pDesc'
        ),
        (
            ['in'],
            POINTER(D3D10_SUBRESOURCE_DATA),
            'pInitialData'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10Texture3D)),
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
            POINTER(ID3D10Resource),
            'pResource'
        ),
        (
            ['in'],
            POINTER(D3D10_SHADER_RESOURCE_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10ShaderResourceView)),
            'ppSRView'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateRenderTargetView',
        (
            ['in'],
            POINTER(ID3D10Resource),
            'pResource'
        ),
        (
            ['in'],
            POINTER(D3D10_RENDER_TARGET_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10RenderTargetView)),
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
            POINTER(ID3D10Resource),
            'pResource'
        ),
        (
            ['in'],
            POINTER(D3D10_DEPTH_STENCIL_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10DepthStencilView)),
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
            POINTER(D3D10_INPUT_ELEMENT_DESC),
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
            POINTER(POINTER(ID3D10InputLayout)),
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
            ['out'],
            POINTER(POINTER(ID3D10VertexShader)),
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
            ['out'],
            POINTER(POINTER(ID3D10GeometryShader)),
            'ppGeometryShader'
        ),
    ),
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
            POINTER(D3D10_SO_DECLARATION_ENTRY),
            'pSODeclaration'
        ),
        (
            ['in'],
            UINT,
            'NumEntries'
        ),
        (['in'], UINT, 'OutputStreamStride'),
        (
            ['out'],
            POINTER(POINTER(ID3D10GeometryShader)),
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
            ['out'],
            POINTER(POINTER(ID3D10PixelShader)),
            'ppPixelShader'
        ),
    ),
    #        
    COMMETHOD(
        [],
        HRESULT,
        'CreateBlendState',
        (
            ['in'],
            POINTER(D3D10_BLEND_DESC),
            'pBlendStateDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10BlendState)),
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
            POINTER(D3D10_DEPTH_STENCIL_DESC),
            'pDepthStencilDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10DepthStencilState)),
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
            POINTER(D3D10_RASTERIZER_DESC),
            'pRasterizerDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10RasterizerState)),
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
            POINTER(D3D10_SAMPLER_DESC),
            'pSamplerDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10SamplerState)),
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
            POINTER(D3D10_QUERY_DESC),
            'pQueryDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10Query)),
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
            POINTER(D3D10_QUERY_DESC),
            'pPredicateDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10Predicate)),
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
            POINTER(D3D10_COUNTER_DESC),
            'pCounterDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10Counter)),
            'ppCounter'
        ),
    ),
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
            POINTER(D3D10_COUNTER_INFO),
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
            POINTER(D3D10_COUNTER_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(D3D10_COUNTER_TYPE),
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
    COMMETHOD(
        [],
        UINT,
        'GetCreationFlags',
    ),
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
    #        
    COMMETHOD(
        [],
        VOID,
        'SetTextFilterSize',
        (['in'], UINT, 'Width'),
        (['in'], UINT, 'Height'),
    ),
    #        
    COMMETHOD(
        [],
        VOID,
        'GetTextFilterSize',
        (['in'], POINTER(UINT), 'pWidth'),
        (['in'], POINTER(UINT), 'pHeight'),
    ),
        # not not not END LOW-FREQUENCY not not not        
]
# END IF  __ID3D10Device_FWD_DEFINED__

class ID3D10Multithread(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


# Direct3D errors are now found in winerror.h
class D3D10_INPUT_CLASSIFICATION(ENUM):
    D3D10_INPUT_PER_VERTEX_DATA = 0
    D3D10_INPUT_PER_INSTANCE_DATA = 1


D3D10_INPUT_ELEMENT_DESC._fields_ = [
    ('SemanticName', LPCSTR),
    ('SemanticIndex', UINT),
    ('Format', DXGI_FORMAT),
    ('InputSlot', UINT),
    ('AlignedByteOffset', UINT),
    ('InputSlotClass', D3D10_INPUT_CLASSIFICATION),
    ('InstanceDataStepRate', UINT),
]


class D3D10_FILL_MODE(ENUM):
    D3D10_FILL_WIREFRAME = 2
    D3D10_FILL_SOLID = 3


D3D10_PRIMITIVE_TOPOLOGY = D3D_PRIMITIVE_TOPOLOGY
D3D10_PRIMITIVE = D3D_PRIMITIVE


class D3D10_CULL_MODE(ENUM):
    D3D10_CULL_NONE = 1
    D3D10_CULL_FRONT = 2
    D3D10_CULL_BACK = 3


D3D10_SO_DECLARATION_ENTRY._fields_ = [
    ('SemanticName', LPCSTR),
    ('SemanticIndex', UINT),
    ('StartComponent', BYTE),
    ('ComponentCount', BYTE),
    ('OutputSlot', BYTE),
]

D3D10_VIEWPORT._fields_ = [
    ('TopLeftX', INT),
    ('TopLeftY', INT),
    ('Width', UINT),
    ('Height', UINT),
    ('MinDepth', FLOAT),
    ('MaxDepth', FLOAT),
]


class D3D10_RESOURCE_DIMENSION(ENUM):
    D3D10_RESOURCE_DIMENSION_UNKNOWN = 0
    D3D10_RESOURCE_DIMENSION_BUFFER = 1
    D3D10_RESOURCE_DIMENSION_TEXTURE1D = 2
    D3D10_RESOURCE_DIMENSION_TEXTURE2D = 3
    D3D10_RESOURCE_DIMENSION_TEXTURE3D = 4


D3D10_SRV_DIMENSION = D3D_SRV_DIMENSION


class D3D10_DSV_DIMENSION(ENUM):
    D3D10_DSV_DIMENSION_UNKNOWN = 0
    D3D10_DSV_DIMENSION_TEXTURE1D = 1
    D3D10_DSV_DIMENSION_TEXTURE1DARRAY = 2
    D3D10_DSV_DIMENSION_TEXTURE2D = 3
    D3D10_DSV_DIMENSION_TEXTURE2DARRAY = 4
    D3D10_DSV_DIMENSION_TEXTURE2DMS = 5
    D3D10_DSV_DIMENSION_TEXTURE2DMSARRAY = 6


class D3D10_RTV_DIMENSION(ENUM):
    D3D10_RTV_DIMENSION_UNKNOWN = 0
    D3D10_RTV_DIMENSION_BUFFER = 1
    D3D10_RTV_DIMENSION_TEXTURE1D = 2
    D3D10_RTV_DIMENSION_TEXTURE1DARRAY = 3
    D3D10_RTV_DIMENSION_TEXTURE2D = 4
    D3D10_RTV_DIMENSION_TEXTURE2DARRAY = 5
    D3D10_RTV_DIMENSION_TEXTURE2DMS = 6
    D3D10_RTV_DIMENSION_TEXTURE2DMSARRAY = 7
    D3D10_RTV_DIMENSION_TEXTURE3D = 8


class D3D10_USAGE(ENUM):
    D3D10_USAGE_DEFAULT = 0
    D3D10_USAGE_IMMUTABLE = 1
    D3D10_USAGE_DYNAMIC = 2
    D3D10_USAGE_STAGING = 3


class D3D10_BIND_FLAG(ENUM):
    D3D10_BIND_VERTEX_BUFFER = 0x1
    D3D10_BIND_INDEX_BUFFER = 0x2
    D3D10_BIND_CONSTANT_BUFFER = 0x4
    D3D10_BIND_SHADER_RESOURCE = 0x8
    D3D10_BIND_STREAM_OUTPUT = 0x10
    D3D10_BIND_RENDER_TARGET = 0x20
    D3D10_BIND_DEPTH_STENCIL = 0x40


class D3D10_CPU_ACCESS_FLAG(ENUM):
    D3D10_CPU_ACCESS_WRITE = 0x10000
    D3D10_CPU_ACCESS_READ = 0x20000


class D3D10_RESOURCE_MISC_FLAG(ENUM):
    D3D10_RESOURCE_MISC_GENERATE_MIPS = 0x1
    D3D10_RESOURCE_MISC_SHARED = 0x2
    D3D10_RESOURCE_MISC_TEXTURECUBE = 0x4
    D3D10_RESOURCE_MISC_SHARED_KEYEDMUTEX = 0x10
    D3D10_RESOURCE_MISC_GDI_COMPATIBLE = 0x20


class D3D10_MAP(ENUM):
    D3D10_MAP_READ = 1
    D3D10_MAP_WRITE = 2
    D3D10_MAP_READ_WRITE = 3
    D3D10_MAP_WRITE_DISCARD = 4
    D3D10_MAP_WRITE_NO_OVERWRITE = 5


class D3D10_MAP_FLAG(ENUM):
    D3D10_MAP_FLAG_DO_NOT_WAIT = 0x100000


class D3D10_RAISE_FLAG(ENUM):
    D3D10_RAISE_FLAG_DRIVER_INTERNAL_ERROR = 0x1


class D3D10_CLEAR_FLAG(ENUM):
    D3D10_CLEAR_DEPTH = 0x1
    D3D10_CLEAR_STENCIL = 0x2


D3D10_RECT = RECT

D3D10_BOX._fields_ = [
    ('left', UINT),
    ('top', UINT),
    ('front', UINT),
    ('right', UINT),
    ('bottom', UINT),
    ('back', UINT),
]

IID_ID3D10DeviceChild = GUID(
    "{9B7E4C00-342C-4106-A19F-4F2704F689F0}"
)

ID3D10DeviceChild._iid_ = IID_ID3D10DeviceChild


ID3D10DeviceChild._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDevice')],
        VOID,
        'GetDevice',
        (['out'], POINTER(POINTER(ID3D10Device)), 'ppDevice'),
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


class D3D10_COMPARISON_FUNC(ENUM):
    D3D10_COMPARISON_NEVER = 1
    D3D10_COMPARISON_LESS = 2
    D3D10_COMPARISON_EQUAL = 3
    D3D10_COMPARISON_LESS_EQUAL = 4
    D3D10_COMPARISON_GREATER = 5
    D3D10_COMPARISON_NOT_EQUAL = 6
    D3D10_COMPARISON_GREATER_EQUAL = 7
    D3D10_COMPARISON_ALWAYS = 8


class D3D10_DEPTH_WRITE_MASK(ENUM):
    D3D10_DEPTH_WRITE_MASK_ZERO = 0
    D3D10_DEPTH_WRITE_MASK_ALL = 1


class D3D10_STENCIL_OP(ENUM):
    D3D10_STENCIL_OP_KEEP = 1
    D3D10_STENCIL_OP_ZERO = 2
    D3D10_STENCIL_OP_REPLACE = 3
    D3D10_STENCIL_OP_INCR_SAT = 4
    D3D10_STENCIL_OP_DECR_SAT = 5
    D3D10_STENCIL_OP_INVERT = 6
    D3D10_STENCIL_OP_INCR = 7
    D3D10_STENCIL_OP_DECR = 8


D3D10_DEPTH_STENCILOP_DESC._fields_ = [
    ('StencilFailOp', D3D10_STENCIL_OP),
    ('StencilDepthFailOp', D3D10_STENCIL_OP),
    ('StencilPassOp', D3D10_STENCIL_OP),
    ('StencilFunc', D3D10_COMPARISON_FUNC),
]

D3D10_DEPTH_STENCIL_DESC._fields_ = [
    ('DepthEnable', BOOL),
    ('DepthWriteMask', D3D10_DEPTH_WRITE_MASK),
    ('DepthFunc', D3D10_COMPARISON_FUNC),
    ('StencilEnable', BOOL),
    ('StencilReadMask', UINT8),
    ('StencilWriteMask', UINT8),
    ('FrontFace', D3D10_DEPTH_STENCILOP_DESC),
    ('BackFace', D3D10_DEPTH_STENCILOP_DESC),
]

IID_ID3D10DepthStencilState = GUID(
    "{2B4B1CC8-A4AD-41F8-8322-CA86FC3EC675}"
)
ID3D10DepthStencilState._iid_ = IID_ID3D10DepthStencilState


ID3D10DepthStencilState._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(D3D10_DEPTH_STENCIL_DESC), 'pDesc'),
    ),
]


class D3D10_BLEND(ENUM):
    D3D10_BLEND_ZERO = 1
    D3D10_BLEND_ONE = 2
    D3D10_BLEND_SRC_COLOR = 3
    D3D10_BLEND_INV_SRC_COLOR = 4
    D3D10_BLEND_SRC_ALPHA = 5
    D3D10_BLEND_INV_SRC_ALPHA = 6
    D3D10_BLEND_DEST_ALPHA = 7
    D3D10_BLEND_INV_DEST_ALPHA = 8
    D3D10_BLEND_DEST_COLOR = 9
    D3D10_BLEND_INV_DEST_COLOR = 10
    D3D10_BLEND_SRC_ALPHA_SAT = 11
    D3D10_BLEND_BLEND_FACTOR = 14
    D3D10_BLEND_INV_BLEND_FACTOR = 15
    D3D10_BLEND_SRC1_COLOR = 16
    D3D10_BLEND_INV_SRC1_COLOR = 17
    D3D10_BLEND_SRC1_ALPHA = 18
    D3D10_BLEND_INV_SRC1_ALPHA = 19


class D3D10_BLEND_OP(ENUM):
    D3D10_BLEND_OP_ADD = 1
    D3D10_BLEND_OP_SUBTRACT = 2
    D3D10_BLEND_OP_REV_SUBTRACT = 3
    D3D10_BLEND_OP_MIN = 4
    D3D10_BLEND_OP_MAX = 5


class D3D10_COLOR_WRITE_ENABLE(ENUM):
    D3D10_COLOR_WRITE_ENABLE_RED = 1
    D3D10_COLOR_WRITE_ENABLE_GREEN = 2
    D3D10_COLOR_WRITE_ENABLE_BLUE = 4
    D3D10_COLOR_WRITE_ENABLE_ALPHA = 8
    D3D10_COLOR_WRITE_ENABLE_ALL = (
        D3D10_COLOR_WRITE_ENABLE_RED |
        D3D10_COLOR_WRITE_ENABLE_GREEN |
        D3D10_COLOR_WRITE_ENABLE_BLUE |
        D3D10_COLOR_WRITE_ENABLE_ALPHA 
    )
    

D3D10_BLEND_DESC._fields_ = [
    ('AlphaToCoverageEnable', BOOL),
    ('BlendEnable', BOOL * 8),
    ('SrcBlend', D3D10_BLEND),
    ('DestBlend', D3D10_BLEND),
    ('BlendOp', D3D10_BLEND_OP),
    ('SrcBlendAlpha', D3D10_BLEND),
    ('DestBlendAlpha', D3D10_BLEND),
    ('BlendOpAlpha', D3D10_BLEND_OP),
    ('RenderTargetWriteMask', UINT8 * 8),
]


IID_ID3D10BlendState = GUID(
    "{EDAD8D19-8A35-4D6D-8566-2EA276CDE161}"
)
ID3D10BlendState._iid_ = IID_ID3D10BlendState


ID3D10BlendState._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(D3D10_BLEND_DESC), 'pDesc'),
    ),
]



D3D10_RASTERIZER_DESC._fields_ = [
    ('FillMode', D3D10_FILL_MODE),
    ('CullMode', D3D10_CULL_MODE),
    ('FrontCounterClockwise', BOOL),
    ('DepthBias', INT),
    ('DepthBiasClamp', FLOAT),
    ('SlopeScaledDepthBias', FLOAT),
    ('DepthClipEnable', BOOL),
    ('ScissorEnable', BOOL),
    ('MultisampleEnable', BOOL),
    ('AntialiasedLineEnable', BOOL),
]


IID_ID3D10RasterizerState = GUID(
    "{A2A07292-89AF-4345-BE2E-C53D9FBB6E9F}"
)
ID3D10RasterizerState._iid_ = IID_ID3D10RasterizerState


ID3D10RasterizerState._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(D3D10_RASTERIZER_DESC), 'pDesc'),
    ),
]


d3d10 = ctypes.windll.D3D10


# inline UINT D3D10CalcSubresource( UINT MipSlice, UINT ArraySlice, UINT MipLevels )
# { return MipSlice + ArraySlice * MipLevels; }
# #endif
# typedef struct D3D10_SUBRESOURCE_DATA
# {
# VOID *pSysMem;
# D3D10CalcSubresource = d3d10.D3D10CalcSubresource
# D3D10CalcSubresource.restype = UINT

IID_ID3D10Resource = MIDL_INTERFACE(
    "{9B7E4C01-342C-4106-A19F-4F2704F689F0}"
)
ID3D10Resource._iid_ = IID_ID3D10Resource


ID3D10Resource._methods_ = [
    COMMETHOD(
        [helpstring('Method GetType')],
        VOID,
        'GetType',
        (
            ['out'],
            POINTER(D3D10_RESOURCE_DIMENSION),
            'rType'
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


D3D10_BUFFER_DESC._fields_ = [
    ('ByteWidth', UINT),
    ('Usage', D3D10_USAGE),
    ('BindFlags', UINT),
    ('CPUAccessFlags', UINT),
    ('MiscFlags', UINT),
]

CD3D10_BUFFER_DESC = D3D10_BUFFER_DESC

IID_ID3D10Buffer = MIDL_INTERFACE(
    "{9B7E4C02-342C-4106-A19F-4F2704F689F0}"
)
ID3D10Buffer._iid_ = IID_ID3D10Buffer


ID3D10Buffer._methods_ = [
    COMMETHOD(
        [helpstring('Method Map')],
        HRESULT,
        'Map',
        (['in'], D3D10_MAP, 'MapType'),
        (['in'], UINT, 'MapFlags'),
        (['out'], POINTER(POINTER(VOID)), 'ppData'),
    ),
    COMMETHOD(
        [helpstring('Method Unmap')],
        VOID,
        'Unmap',
    ),
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(D3D10_BUFFER_DESC), 'pDesc'),
    ),
]


D3D10_TEXTURE1D_DESC._fields_ = [
    ('Width', UINT),
    ('MipLevels', UINT),
    ('ArraySize', UINT),
    ('Format', DXGI_FORMAT),
    ('Usage', D3D10_USAGE),
    ('BindFlags', UINT),
    ('CPUAccessFlags', UINT),
    ('MiscFlags', UINT),
]
CD3D10_TEXTURE1D_DESC = D3D10_TEXTURE1D_DESC

IID_ID3D10Texture1D = MIDL_INTERFACE(
    "{9B7E4C03-342C-4106-A19F-4F2704F689F0}"
)
ID3D10Texture1D._iid_ = IID_ID3D10Texture1D


ID3D10Texture1D._methods_ = [
    COMMETHOD(
        [helpstring('Method Map')],
        HRESULT,
        'Map',
        (['in'], UINT, 'Subresource'),
        (['in'], D3D10_MAP, 'MapType'),
        (['in'], UINT, 'MapFlags'),
        (['out'], POINTER(POINTER(VOID)), 'ppData'),
    ),
    COMMETHOD(
        [helpstring('Method Unmap')],
        VOID,
        'Unmap',
        (['in'], UINT, 'Subresource'),
    ),
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(D3D10_TEXTURE1D_DESC), 'pDesc'),
    ),
]

CD3D10_TEXTURE2D_DESC = D3D10_TEXTURE2D_DESC

D3D10_MAPPED_TEXTURE2D._fields_ = [
    ('pData', POINTER(VOID)),
    ('RowPitch', UINT),
]

IID_ID3D10Texture2D = MIDL_INTERFACE(
    "{9B7E4C04-342C-4106-A19F-4F2704F689F0}"
)
ID3D10Texture2D._iid_ = IID_ID3D10Texture2D


ID3D10Texture2D._methods_ = [
    COMMETHOD(
        [helpstring('Method Map')],
        HRESULT,
        'Map',
        (['in'], UINT, 'Subresource'),
        (['in'], D3D10_MAP, 'MapType'),
        (['in'], UINT, 'MapFlags'),
        (
            ['out'],
            POINTER(D3D10_MAPPED_TEXTURE2D),
            'pMappedTex2D'
        ),
    ),
    COMMETHOD(
        [helpstring('Method Unmap')],
        VOID,
        'Unmap',
        (['in'], UINT, 'Subresource'),
    ),
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(D3D10_TEXTURE2D_DESC), 'pDesc'),
    ),
]

D3D10_TEXTURE3D_DESC._fields_ = [
    ('Width', UINT),
    ('Height', UINT),
    ('Depth', UINT),
    ('MipLevels', UINT),
    ('Format', DXGI_FORMAT),
    ('Usage', D3D10_USAGE),
    ('BindFlags', UINT),
    ('CPUAccessFlags', UINT),
    ('MiscFlags', UINT),
]

CD3D10_TEXTURE3D_DESC = D3D10_TEXTURE3D_DESC

D3D10_MAPPED_TEXTURE3D._fields_ = [
    ('pData', POINTER(VOID)),
    ('RowPitch', UINT),
    ('DepthPitch', UINT),
]
   
IID_ID3D10Texture3D = MIDL_INTERFACE(
    "{9B7E4C05-342C-4106-A19F-4F2704F689F0}"
)
ID3D10Texture3D._iid_ = IID_ID3D10Texture3D


ID3D10Texture3D._methods_ = [
    COMMETHOD(
        [helpstring('Method Map')],
        HRESULT,
        'Map',
        (['in'], UINT, 'Subresource'),
        (['in'], D3D10_MAP, 'MapType'),
        (['in'], UINT, 'MapFlags'),
        (
            ['out'],
            POINTER(D3D10_MAPPED_TEXTURE3D),
            'pMappedTex3D'
        ),
    ),
    COMMETHOD(
        [helpstring('Method Unmap')],
        VOID,
        'Unmap',
        (['in'], UINT, 'Subresource'),
    ),
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(D3D10_TEXTURE3D_DESC), 'pDesc'),
    ),
]


class D3D10_TEXTURECUBE_FACE(ENUM):
    D3D10_TEXTURECUBE_FACE_POSITIVE_X = 0
    D3D10_TEXTURECUBE_FACE_NEGATIVE_X = 1
    D3D10_TEXTURECUBE_FACE_POSITIVE_Y = 2
    D3D10_TEXTURECUBE_FACE_NEGATIVE_Y = 3
    D3D10_TEXTURECUBE_FACE_POSITIVE_Z = 4
    D3D10_TEXTURECUBE_FACE_NEGATIVE_Z = 5


IID_ID3D10View = MIDL_INTERFACE(
    "{C902B03F-60A7-49BA-9936-2A3AB37A7E33}"
)
ID3D10View._iid_ = IID_ID3D10View


ID3D10View._methods_ = [
    COMMETHOD(
        [helpstring('Method GetResource')],
        VOID,
        'GetResource',
        (
            ['out'],
            POINTER(POINTER(ID3D10Resource)),
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
D3D10_BUFFER_SRV._Union_1 = _Union_1


class _Union_2(ctypes.Union):
    pass


_Union_2._fields_ = [
    ('NumElements', UINT),
    ('ElementWidth', UINT),
]
D3D10_BUFFER_SRV._Union_2 = _Union_2

D3D10_BUFFER_SRV._anonymous_ = (
    '_Union_1',
    '_Union_2',
)

D3D10_BUFFER_SRV._fields_ = [
    ('_Union_1', D3D10_BUFFER_SRV._Union_1),
    ('_Union_2', D3D10_BUFFER_SRV._Union_2),
]

D3D10_TEX1D_SRV._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
]

D3D10_TEX1D_ARRAY_SRV._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]

D3D10_TEX2D_SRV._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
]

D3D10_TEX2D_ARRAY_SRV._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]

D3D10_TEX3D_SRV._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
]

D3D10_TEXCUBE_SRV._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
]

D3D10_TEX2DMS_SRV._fields_ = [
    ('UnusedField_NothingToDefine', UINT),
]

D3D10_TEX2DMS_ARRAY_SRV._fields_ = [
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]


class _Union_3(ctypes.Union):
    pass


_Union_3._fields_ = [
    ('Buffer', D3D10_BUFFER_SRV),
    ('Texture1D', D3D10_TEX1D_SRV),
    ('Texture1DArray', D3D10_TEX1D_ARRAY_SRV),
    ('Texture2D', D3D10_TEX2D_SRV),
    ('Texture2DArray', D3D10_TEX2D_ARRAY_SRV),
    ('Texture2DMS', D3D10_TEX2DMS_SRV),
    ('Texture2DMSArray', D3D10_TEX2DMS_ARRAY_SRV),
    ('Texture3D', D3D10_TEX3D_SRV),
    ('TextureCube', D3D10_TEXCUBE_SRV),
]
D3D10_SHADER_RESOURCE_VIEW_DESC._Union_3 = _Union_3

D3D10_SHADER_RESOURCE_VIEW_DESC._anonymous_ = (
    '_Union_3',
)

D3D10_SHADER_RESOURCE_VIEW_DESC._fields_ = [
    ('Format', DXGI_FORMAT),
    ('ViewDimension', D3D10_SRV_DIMENSION),
    ('_Union_3', D3D10_SHADER_RESOURCE_VIEW_DESC._Union_3),
]


IID_ID3D10ShaderResourceView = MIDL_INTERFACE(
    "{9B7E4C07-342C-4106-A19F-4F2704F689F0}"
)
ID3D10ShaderResourceView._iid_ = IID_ID3D10ShaderResourceView


ID3D10ShaderResourceView._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (
            ['out'],
            POINTER(D3D10_SHADER_RESOURCE_VIEW_DESC),
            'pDesc'
        ),
    ),
]


class _Union_4(ctypes.Union):
    pass


_Union_4._fields_ = [
    ('FirstElement', UINT),
    ('ElementOffset', UINT),
]
D3D10_BUFFER_RTV._Union_4 = _Union_4


class _Union_5(ctypes.Union):
    pass


_Union_5._fields_ = [
    ('NumElements', UINT),
    ('ElementWidth', UINT),
]
D3D10_BUFFER_RTV._Union_5 = _Union_5

D3D10_BUFFER_RTV._anonymous_ = (
    '_Union_4',
    '_Union_5',
)

D3D10_BUFFER_RTV._fields_ = [
    ('_Union_4', D3D10_BUFFER_RTV._Union_4),
    ('_Union_5', D3D10_BUFFER_RTV._Union_5),
]

D3D10_TEX1D_RTV._fields_ = [
    ('MipSlice', UINT),
]

D3D10_TEX1D_ARRAY_RTV._fields_ = [
    ('MipSlice', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]

D3D10_TEX2D_RTV._fields_ = [
    ('MipSlice', UINT),
]

D3D10_TEX2DMS_RTV._fields_ = [
    ('UnusedField_NothingToDefine', UINT),
]

D3D10_TEX2D_ARRAY_RTV._fields_ = [
    ('MipSlice', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]

D3D10_TEX2DMS_ARRAY_RTV._fields_ = [
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]

D3D10_TEX3D_RTV._fields_ = [
    ('MipSlice', UINT),
    ('FirstWSlice', UINT),
    ('WSize', UINT),
]


class _Union_6(ctypes.Union):
    pass


_Union_6._fields_ = [
    ('Buffer', D3D10_BUFFER_RTV),
    ('Texture1D', D3D10_TEX1D_RTV),
    ('Texture1DArray', D3D10_TEX1D_ARRAY_RTV),
    ('Texture2D', D3D10_TEX2D_RTV),
    ('Texture2DArray', D3D10_TEX2D_ARRAY_RTV),
    ('Texture2DMS', D3D10_TEX2DMS_RTV),
    ('Texture2DMSArray', D3D10_TEX2DMS_ARRAY_RTV),
    ('Texture3D', D3D10_TEX3D_RTV),
]
D3D10_RENDER_TARGET_VIEW_DESC._Union_6 = _Union_6

D3D10_RENDER_TARGET_VIEW_DESC._anonymous_ = (
    '_Union_6',
)

D3D10_RENDER_TARGET_VIEW_DESC._fields_ = [
    ('Format', DXGI_FORMAT),
    ('ViewDimension', D3D10_RTV_DIMENSION),
    ('_Union_6', D3D10_RENDER_TARGET_VIEW_DESC._Union_6),
]


IID_ID3D10RenderTargetView = MIDL_INTERFACE(
    "{9B7E4C08-342C-4106-A19F-4F2704F689F0}"
)
ID3D10RenderTargetView._iid_ = IID_ID3D10RenderTargetView


ID3D10RenderTargetView._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (
            ['out'],
            POINTER(D3D10_RENDER_TARGET_VIEW_DESC),
            'pDesc'
        ),
    ),
]

D3D10_TEX1D_DSV._fields_ = [
    ('MipSlice', UINT),
]

D3D10_TEX1D_ARRAY_DSV._fields_ = [
    ('MipSlice', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]

D3D10_TEX2D_DSV._fields_ = [
    ('MipSlice', UINT),
]

D3D10_TEX2D_ARRAY_DSV._fields_ = [
    ('MipSlice', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]

D3D10_TEX2DMS_DSV._fields_ = [
    ('UnusedField_NothingToDefine', UINT),
]

D3D10_TEX2DMS_ARRAY_DSV._fields_ = [
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]


class _Union_7(ctypes.Union):
    pass


_Union_7._fields_ = [
    ('Texture1D', D3D10_TEX1D_DSV),
    ('Texture1DArray', D3D10_TEX1D_ARRAY_DSV),
    ('Texture2D', D3D10_TEX2D_DSV),
    ('Texture2DArray', D3D10_TEX2D_ARRAY_DSV),
    ('Texture2DMS', D3D10_TEX2DMS_DSV),
    ('Texture2DMSArray', D3D10_TEX2DMS_ARRAY_DSV),
]
D3D10_DEPTH_STENCIL_VIEW_DESC._Union_7 = _Union_7

D3D10_DEPTH_STENCIL_VIEW_DESC._anonymous_ = (
    '_Union_7',
)

D3D10_DEPTH_STENCIL_VIEW_DESC._fields_ = [
    ('Format', DXGI_FORMAT),
    ('ViewDimension', D3D10_DSV_DIMENSION),
    ('_Union_7', D3D10_DEPTH_STENCIL_VIEW_DESC._Union_7),
]

IID_ID3D10DepthStencilView = MIDL_INTERFACE(
    "{9B7E4C09-342C-4106-A19F-4F2704F689F0}"
)
ID3D10DepthStencilView._iid_ = IID_ID3D10DepthStencilView


ID3D10DepthStencilView._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (
            ['out'],
            POINTER(D3D10_DEPTH_STENCIL_VIEW_DESC),
            'pDesc'
        ),
    ),
]

IID_ID3D10VertexShader = MIDL_INTERFACE(
    "{9B7E4C0A-342C-4106-A19F-4F2704F689F0}"
)
ID3D10VertexShader._iid_ = IID_ID3D10VertexShader


ID3D10VertexShader._methods_ = []


IID_ID3D10GeometryShader = MIDL_INTERFACE(
    "{6316BE88-54CD-4040-AB44-20461BC81F68}"
)
ID3D10GeometryShader._iid_ = IID_ID3D10GeometryShader


ID3D10GeometryShader._methods_ = []

IID_ID3D10PixelShader = MIDL_INTERFACE(
    "{4968B601-9D00-4CDE-8346-8E7F675819B6}"
)
ID3D10PixelShader._iid_ = IID_ID3D10PixelShader


ID3D10PixelShader._methods_ = []


IID_ID3D10InputLayout = MIDL_INTERFACE(
    "{9B7E4C0B-342C-4106-A19F-4F2704F689F0}"
)
ID3D10InputLayout._iid_ = IID_ID3D10InputLayout


ID3D10InputLayout._methods_ = []


class D3D10_FILTER(ENUM):
    D3D10_FILTER_MIN_MAG_MIP_POINT = 0
    D3D10_FILTER_MIN_MAG_POINT_MIP_LINEAR = 0x1
    D3D10_FILTER_MIN_POINT_MAG_LINEAR_MIP_POINT = 0x4
    D3D10_FILTER_MIN_POINT_MAG_MIP_LINEAR = 0x5
    D3D10_FILTER_MIN_LINEAR_MAG_MIP_POINT = 0x10
    D3D10_FILTER_MIN_LINEAR_MAG_POINT_MIP_LINEAR = 0x11
    D3D10_FILTER_MIN_MAG_LINEAR_MIP_POINT = 0x14
    D3D10_FILTER_MIN_MAG_MIP_LINEAR = 0x15
    D3D10_FILTER_ANISOTROPIC = 0x55
    D3D10_FILTER_COMPARISON_MIN_MAG_MIP_POINT = 0x80
    D3D10_FILTER_COMPARISON_MIN_MAG_POINT_MIP_LINEAR = 0x81
    D3D10_FILTER_COMPARISON_MIN_POINT_MAG_LINEAR_MIP_POINT = 0x84
    D3D10_FILTER_COMPARISON_MIN_POINT_MAG_MIP_LINEAR = 0x85
    D3D10_FILTER_COMPARISON_MIN_LINEAR_MAG_MIP_POINT = 0x90
    D3D10_FILTER_COMPARISON_MIN_LINEAR_MAG_POINT_MIP_LINEAR = 0x91
    D3D10_FILTER_COMPARISON_MIN_MAG_LINEAR_MIP_POINT = 0x94
    D3D10_FILTER_COMPARISON_MIN_MAG_MIP_LINEAR = 0x95
    D3D10_FILTER_COMPARISON_ANISOTROPIC = 0xD5
    D3D10_FILTER_TEXT_1BIT = 0x80000000


class D3D10_FILTER_TYPE(ENUM):
    D3D10_FILTER_TYPE_POINT = 0
    D3D10_FILTER_TYPE_LINEAR = 1


class D3D10_TEXTURE_ADDRESS_MODE(ENUM):
    D3D10_TEXTURE_ADDRESS_WRAP = 1
    D3D10_TEXTURE_ADDRESS_MIRROR = 2
    D3D10_TEXTURE_ADDRESS_CLAMP = 3
    D3D10_TEXTURE_ADDRESS_BORDER = 4
    D3D10_TEXTURE_ADDRESS_MIRROR_ONCE = 5

D3D10_SAMPLER_DESC._fields_ = [
    ('Filter', D3D10_FILTER),
    ('AddressU', D3D10_TEXTURE_ADDRESS_MODE),
    ('AddressV', D3D10_TEXTURE_ADDRESS_MODE),
    ('AddressW', D3D10_TEXTURE_ADDRESS_MODE),
    ('MipLODBias', FLOAT),
    ('MaxAnisotropy', UINT),
    ('ComparisonFunc', D3D10_COMPARISON_FUNC),
    ('BorderColor', FLOAT * 4),
    ('MinLOD', FLOAT),
    ('MaxLOD', FLOAT),
]


IID_ID3D10SamplerState = MIDL_INTERFACE(
    "{9B7E4C0C-342C-4106-A19F-4F2704F689F0}"
)
ID3D10SamplerState._iid_ = IID_ID3D10SamplerState


ID3D10SamplerState._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(D3D10_SAMPLER_DESC), 'pDesc'),
    ),
]


class D3D10_FORMAT_SUPPORT(ENUM):
    D3D10_FORMAT_SUPPORT_BUFFER = 0x1
    D3D10_FORMAT_SUPPORT_IA_VERTEX_BUFFER = 0x2
    D3D10_FORMAT_SUPPORT_IA_INDEX_BUFFER = 0x4
    D3D10_FORMAT_SUPPORT_SO_BUFFER = 0x8
    D3D10_FORMAT_SUPPORT_TEXTURE1D = 0x10
    D3D10_FORMAT_SUPPORT_TEXTURE2D = 0x20
    D3D10_FORMAT_SUPPORT_TEXTURE3D = 0x40
    D3D10_FORMAT_SUPPORT_TEXTURECUBE = 0x80
    D3D10_FORMAT_SUPPORT_SHADER_LOAD = 0x100
    D3D10_FORMAT_SUPPORT_SHADER_SAMPLE = 0x200
    D3D10_FORMAT_SUPPORT_SHADER_SAMPLE_COMPARISON = 0x400
    D3D10_FORMAT_SUPPORT_SHADER_SAMPLE_MONO_TEXT = 0x800
    D3D10_FORMAT_SUPPORT_MIP = 0x1000
    D3D10_FORMAT_SUPPORT_MIP_AUTOGEN = 0x2000
    D3D10_FORMAT_SUPPORT_RENDER_TARGET = 0x4000
    D3D10_FORMAT_SUPPORT_BLENDABLE = 0x8000
    D3D10_FORMAT_SUPPORT_DEPTH_STENCIL = 0x10000
    D3D10_FORMAT_SUPPORT_CPU_LOCKABLE = 0x20000
    D3D10_FORMAT_SUPPORT_MULTISAMPLE_RESOLVE = 0x40000
    D3D10_FORMAT_SUPPORT_DISPLAY = 0x80000
    D3D10_FORMAT_SUPPORT_CAST_WITHIN_BIT_LAYOUT = 0x100000
    D3D10_FORMAT_SUPPORT_MULTISAMPLE_RENDERTARGET = 0x200000
    D3D10_FORMAT_SUPPORT_MULTISAMPLE_LOAD = 0x400000
    D3D10_FORMAT_SUPPORT_SHADER_GATHER = 0x800000
    D3D10_FORMAT_SUPPORT_BACK_BUFFER_CAST = 0x1000000



IID_ID3D10Asynchronous = MIDL_INTERFACE(
    "{9B7E4C0D-342C-4106-A19F-4F2704F689F0}"
)
ID3D10Asynchronous._iid_ = IID_ID3D10Asynchronous


ID3D10Asynchronous._methods_ = [
    COMMETHOD(
        [helpstring('Method Begin')],
        VOID,
        'Begin',
    ),
    COMMETHOD(
        [helpstring('Method End')],
        VOID,
        'End',
    ),
    COMMETHOD(
        [helpstring('Method GetData')],
        HRESULT,
        'GetData',
        (['out'], POINTER(VOID), 'pData'),
        (['in'], UINT, 'DataSize'),
        (['in'], UINT, 'GetDataFlags'),
    ),
    COMMETHOD(
        [helpstring('Method GetDataSize')],
        UINT,
        'GetDataSize',
    ),
]



class D3D10_ASYNC_GETDATA_FLAG(ENUM):
    D3D10_ASYNC_GETDATA_DONOTFLUSH = 0x1


class D3D10_QUERY(ENUM):
    D3D10_QUERY_EVENT = 0
    D3D10_QUERY_OCCLUSION = D3D10_QUERY_EVENT + 1
    D3D10_QUERY_TIMESTAMP = D3D10_QUERY_OCCLUSION + 1
    D3D10_QUERY_TIMESTAMP_DISJOINT = D3D10_QUERY_TIMESTAMP + 1
    D3D10_QUERY_PIPELINE_STATISTICS = (
        D3D10_QUERY_TIMESTAMP_DISJOINT + 1
    )
    D3D10_QUERY_OCCLUSION_PREDICATE = (
        D3D10_QUERY_PIPELINE_STATISTICS + 1
    )
    D3D10_QUERY_SO_STATISTICS = D3D10_QUERY_OCCLUSION_PREDICATE + 1
    D3D10_QUERY_SO_OVERFLOW_PREDICATE = (
        D3D10_QUERY_SO_STATISTICS + 1
    )


class D3D10_QUERY_MISC_FLAG(ENUM):
    D3D10_QUERY_MISC_PREDICATEHINT = 0x1

D3D10_QUERY_DESC._fields_ = [
    ('Query', D3D10_QUERY),
    ('MiscFlags', UINT),
]


IID_ID3D10Query = MIDL_INTERFACE(
    "{9B7E4C0E-342C-4106-A19F-4F2704F689F0}"
)
ID3D10Query._iid_ = IID_ID3D10Query


ID3D10Query._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(D3D10_QUERY_DESC), 'pDesc'),
    ),
]

IID_ID3D10Predicate = MIDL_INTERFACE(
    "{9B7E4C10-342C-4106-A19F-4F2704F689F0}"
)
ID3D10Predicate._iid_ = IID_ID3D10Predicate


ID3D10Predicate._methods_ = []

D3D10_QUERY_DATA_TIMESTAMP_DISJOINT._fields_ = [
    ('Frequency', UINT64),
    ('Disjoint', BOOL),
]

D3D10_QUERY_DATA_PIPELINE_STATISTICS._fields_ = [
    ('IAVertices', UINT64),
    ('IAPrimitives', UINT64),
    ('VSInvocations', UINT64),
    ('GSInvocations', UINT64),
    ('GSPrimitives', UINT64),
    ('CInvocations', UINT64),
    ('CPrimitives', UINT64),
    ('PSInvocations', UINT64),
]

D3D10_QUERY_DATA_SO_STATISTICS._fields_ = [
    ('NumPrimitivesWritten', UINT64),
    ('PrimitivesStorageNeeded', UINT64),
]


class D3D10_COUNTER(ENUM):
    D3D10_COUNTER_GPU_IDLE = 0
    D3D10_COUNTER_VERTEX_PROCESSING = D3D10_COUNTER_GPU_IDLE + 1
    D3D10_COUNTER_GEOMETRY_PROCESSING = (
        D3D10_COUNTER_VERTEX_PROCESSING + 1
    )
    D3D10_COUNTER_PIXEL_PROCESSING = (
        D3D10_COUNTER_GEOMETRY_PROCESSING + 1
    )
    D3D10_COUNTER_OTHER_GPU_PROCESSING = (
        D3D10_COUNTER_PIXEL_PROCESSING + 1
    )
    D3D10_COUNTER_HOST_ADAPTER_BANDWIDTH_UTILIZATION = (
        D3D10_COUNTER_OTHER_GPU_PROCESSING + 1
    )
    D3D10_COUNTER_LOCAL_VIDMEM_BANDWIDTH_UTILIZATION = (
        D3D10_COUNTER_HOST_ADAPTER_BANDWIDTH_UTILIZATION + 1
    )
    D3D10_COUNTER_VERTEX_THROUGHPUT_UTILIZATION = (
        D3D10_COUNTER_LOCAL_VIDMEM_BANDWIDTH_UTILIZATION + 1
    )
    D3D10_COUNTER_TRIANGLE_SETUP_THROUGHPUT_UTILIZATION = (
        D3D10_COUNTER_VERTEX_THROUGHPUT_UTILIZATION + 1
    )
    D3D10_COUNTER_FILLRATE_THROUGHPUT_UTILIZATION = (
        D3D10_COUNTER_TRIANGLE_SETUP_THROUGHPUT_UTILIZATION + 1
    )
    D3D10_COUNTER_VS_MEMORY_LIMITED = (
        D3D10_COUNTER_FILLRATE_THROUGHPUT_UTILIZATION + 1
    )
    D3D10_COUNTER_VS_COMPUTATION_LIMITED = (
        D3D10_COUNTER_VS_MEMORY_LIMITED + 1
    )
    D3D10_COUNTER_GS_MEMORY_LIMITED = (
        D3D10_COUNTER_VS_COMPUTATION_LIMITED + 1
    )
    D3D10_COUNTER_GS_COMPUTATION_LIMITED = (
        D3D10_COUNTER_GS_MEMORY_LIMITED + 1
    )
    D3D10_COUNTER_PS_MEMORY_LIMITED = (
        D3D10_COUNTER_GS_COMPUTATION_LIMITED + 1
    )
    D3D10_COUNTER_PS_COMPUTATION_LIMITED = (
        D3D10_COUNTER_PS_MEMORY_LIMITED + 1
    )
    D3D10_COUNTER_POST_TRANSFORM_CACHE_HIT_RATE = (
        D3D10_COUNTER_PS_COMPUTATION_LIMITED + 1
    )
    D3D10_COUNTER_TEXTURE_CACHE_HIT_RATE = (
        D3D10_COUNTER_POST_TRANSFORM_CACHE_HIT_RATE + 1
    )
    D3D10_COUNTER_DEVICE_DEPENDENT_0 = 0x40000000


class D3D10_COUNTER_TYPE(ENUM):
    D3D10_COUNTER_TYPE_FLOAT32 = 0
    D3D10_COUNTER_TYPE_UINT16 = D3D10_COUNTER_TYPE_FLOAT32 + 1
    D3D10_COUNTER_TYPE_UINT32 = D3D10_COUNTER_TYPE_UINT16 + 1
    D3D10_COUNTER_TYPE_UINT64 = D3D10_COUNTER_TYPE_UINT32 + 1

D3D10_COUNTER_DESC._fields_ = [
    ('Counter', D3D10_COUNTER),
    ('MiscFlags', UINT),
]

D3D10_COUNTER_INFO._fields_ = [
    ('LastDeviceDependentCounter', D3D10_COUNTER),
    ('NumSimultaneousCounters', UINT),
    ('NumDetectableParallelUnits', UINT8),
]



IID_ID3D10Counter = MIDL_INTERFACE(
    "{9B7E4C11-342C-4106-A19F-4F2704F689F0}"
)
ID3D10Counter._iid_ = IID_ID3D10Counter


ID3D10Counter._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        VOID,
        'GetDesc',
        (['out'], POINTER(D3D10_COUNTER_DESC), 'pDesc'),
    ),
]

IID_ID3D10Device = MIDL_INTERFACE(
    "{9B7E4C0F-342C-4106-A19F-4F2704F689F0}"
)
ID3D10Device._iid_ = IID_ID3D10Device


ID3D10Device._methods_ = [
    COMMETHOD(
        [helpstring('Method VSSetConstantBuffers')],
        VOID,
        'VSSetConstantBuffers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (['in'], POINTER(POINTER(ID3D10Buffer)), 'ppConstantBuffers'),
    ),
    COMMETHOD(
        [helpstring('Method PSSetShaderResources')],
        VOID,
        'PSSetShaderResources',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumViews'),
        (
            ['in'],
            POINTER(POINTER(ID3D10ShaderResourceView)),
            'ppShaderResourceViews'
        ),
    ),
    COMMETHOD(
        [helpstring('Method PSSetShader')],
        VOID,
        'PSSetShader',
        (
            ['in'],
            POINTER(ID3D10PixelShader),
            'pPixelShader'
        ),
    ),
    COMMETHOD(
        [helpstring('Method PSSetSamplers')],
        VOID,
        'PSSetSamplers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumSamplers'),
        (['in'], POINTER(POINTER(ID3D10SamplerState)), 'ppSamplers'),
    ),
    COMMETHOD(
        [helpstring('Method VSSetShader')],
        VOID,
        'VSSetShader',
        (
            ['in'],
            POINTER(ID3D10VertexShader),
            'pVertexShader'
        ),
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
        [helpstring('Method PSSetConstantBuffers')],
        VOID,
        'PSSetConstantBuffers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (['in'], POINTER(POINTER(ID3D10Buffer)), 'ppConstantBuffers'),
    ),
    COMMETHOD(
        [helpstring('Method IASetInputLayout')],
        VOID,
        'IASetInputLayout',
        (
            ['in'],
            POINTER(ID3D10InputLayout),
            'pInputLayout'
        ),
    ),
    COMMETHOD(
        [helpstring('Method IASetVertexBuffers')],
        VOID,
        'IASetVertexBuffers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (['in'], POINTER(POINTER(ID3D10Buffer)), 'ppVertexBuffers'),
        (['in'], POINTER(UINT), 'pStrides'),
        (['in'], POINTER(UINT), 'pOffsets'),
    ),
    COMMETHOD(
        [helpstring('Method IASetIndexBuffer')],
        VOID,
        'IASetIndexBuffer',
        (['in'], POINTER(ID3D10Buffer), 'pIndexBuffer'),
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
        (['in'], POINTER(POINTER(ID3D10Buffer)), 'ppConstantBuffers'),
    ),
    COMMETHOD(
        [helpstring('Method GSSetShader')],
        VOID,
        'GSSetShader',
        (
            ['in'],
            POINTER(ID3D10GeometryShader),
            'pShader'
        ),
    ),
    COMMETHOD(
        [helpstring('Method IASetPrimitiveTopology')],
        VOID,
        'IASetPrimitiveTopology',
        (['in'], D3D10_PRIMITIVE_TOPOLOGY, 'Topology'),
    ),
    COMMETHOD(
        [helpstring('Method VSSetShaderResources')],
        VOID,
        'VSSetShaderResources',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumViews'),
        (
            ['in'],
            POINTER(POINTER(ID3D10ShaderResourceView)),
            'ppShaderResourceViews'
        ),
    ),
    COMMETHOD(
        [helpstring('Method VSSetSamplers')],
        VOID,
        'VSSetSamplers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumSamplers'),
        (['in'], POINTER(POINTER(ID3D10SamplerState)), 'ppSamplers'),
    ),
    COMMETHOD(
        [helpstring('Method SetPredication')],
        VOID,
        'SetPredication',
        (['in'], POINTER(ID3D10Predicate), 'pPredicate'),
        (['in'], BOOL, 'PredicateValue'),
    ),
    COMMETHOD(
        [helpstring('Method GSSetShaderResources')],
        VOID,
        'GSSetShaderResources',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumViews'),
        (
            ['in'],
            POINTER(POINTER(ID3D10ShaderResourceView)),
            'ppShaderResourceViews'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GSSetSamplers')],
        VOID,
        'GSSetSamplers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumSamplers'),
        (['in'], POINTER(POINTER(ID3D10SamplerState)), 'ppSamplers'),
    ),
    COMMETHOD(
        [helpstring('Method OMSetRenderTargets')],
        VOID,
        'OMSetRenderTargets',
        (['in'], UINT, 'NumViews'),
        (['in'], POINTER(POINTER(ID3D10RenderTargetView)), 'ppRenderTargetViews'),
        (
            ['in'],
            POINTER(ID3D10DepthStencilView),
            'pDepthStencilView'
        ),
    ),
    COMMETHOD(
        [helpstring('Method OMSetBlendState')],
        VOID,
        'OMSetBlendState',
        (
            ['in'],
            POINTER(ID3D10BlendState),
            'pBlendState'
        ),
        (['in'], FLOAT * 4, 'BlendFactor'),
        (['in'], UINT, 'SampleMask'),
    ),

    COMMETHOD(
        [helpstring('Method OMSetDepthStencilState')],
        VOID,
        'OMSetDepthStencilState',
        (
            ['in'],
            POINTER(ID3D10DepthStencilState),
            'pDepthStencilState'
        ),
        (['in'], UINT, 'StencilRef'),
    ),

    COMMETHOD(
        [helpstring('Method SOSetTargets')],
        VOID,
        'SOSetTargets',
        (['in'], UINT, 'NumBuffers'),
        (['in'], POINTER(POINTER(ID3D10Buffer)), 'ppSOTargets'),
        (['in'], POINTER(UINT), 'pOffsets'),
    ),

    COMMETHOD(
        [helpstring('Method DrawAuto')],
        VOID,
        'DrawAuto',
    ),

    COMMETHOD(
        [helpstring('Method RSSetState')],
        VOID,
        'RSSetState',
        (
            ['in'],
            POINTER(ID3D10RasterizerState),
            'pRasterizerState'
        ),
    ),

    COMMETHOD(
        [helpstring('Method RSSetViewports')],
        VOID,
        'RSSetViewports',
        (['in'], UINT, 'NumViewports'),
        (['in'], POINTER(D3D10_VIEWPORT), 'pViewports'),
    ),

    COMMETHOD(
        [helpstring('Method RSSetScissorRects')],
        VOID,
        'RSSetScissorRects',
        (['in'], UINT, 'NumRects'),
        (['in'], POINTER(D3D10_RECT), 'pRects'),
    ),

    COMMETHOD(
        [helpstring('Method CopySubresourceRegion')],
        VOID,
        'CopySubresourceRegion',
        (['in'], POINTER(ID3D10Resource), 'pDstResource'),
        (['in'], UINT, 'DstSubresource'),
        (['in'], UINT, 'DstX'),
        (['in'], UINT, 'DstY'),
        (['in'], UINT, 'DstZ'),
        (['in'], POINTER(ID3D10Resource), 'pSrcResource'),
        (['in'], UINT, 'SrcSubresource'),
        (['in'], POINTER(D3D10_BOX), 'pSrcBox'),
    ),

    COMMETHOD(
        [helpstring('Method CopyResource')],
        VOID,
        'CopyResource',
        (['in'], POINTER(ID3D10Resource), 'pDstResource'),
        (['in'], POINTER(ID3D10Resource), 'pSrcResource'),
    ),

    COMMETHOD(
        [helpstring('Method UpdateSubresource')],
        VOID,
        'UpdateSubresource',
        (['in'], POINTER(ID3D10Resource), 'pDstResource'),
        (['in'], UINT, 'DstSubresource'),
        (['in'], POINTER(D3D10_BOX), 'pDstBox'),
        (['in'], POINTER(VOID), 'pSrcData'),
        (['in'], UINT, 'SrcRowPitch'),
        (['in'], UINT, 'SrcDepthPitch'),
    ),

    COMMETHOD(
        [helpstring('Method ClearRenderTargetView')],
        VOID,
        'ClearRenderTargetView',
        (
            ['in'],
            POINTER(ID3D10RenderTargetView),
            'pRenderTargetView'
        ),
        (['in'], FLOAT * 4, 'ColorRGBA'),
    ),
    COMMETHOD(
        [helpstring('Method ClearDepthStencilView')],
        VOID,
        'ClearDepthStencilView',
        (
            ['in'],
            POINTER(ID3D10DepthStencilView),
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
            POINTER(ID3D10ShaderResourceView),
            'pShaderResourceView'
        ),
    ),
    COMMETHOD(
        [helpstring('Method ResolveSubresource')],
        VOID,
        'ResolveSubresource',
        (['in'], POINTER(ID3D10Resource), 'pDstResource'),
        (['in'], UINT, 'DstSubresource'),
        (['in'], POINTER(ID3D10Resource), 'pSrcResource'),
        (['in'], UINT, 'SrcSubresource'),
        (['in'], DXGI_FORMAT, 'Format'),
    ),
    COMMETHOD(
        [helpstring('Method VSGetConstantBuffers')],
        VOID,
        'VSGetConstantBuffers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (
            ['out'],
            POINTER(POINTER(ID3D10Buffer)),
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
            POINTER(POINTER(ID3D10ShaderResourceView)),
            'ppShaderResourceViews'
        ),
    ),
    COMMETHOD(
        [helpstring('Method PSGetShader')],
        VOID,
        'PSGetShader',
        (
            ['out'],
            POINTER(POINTER(ID3D10PixelShader)),
            'ppPixelShader'
        ),
    ),
    COMMETHOD(
        [helpstring('Method PSGetSamplers')],
        VOID,
        'PSGetSamplers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumSamplers'),
        (
            ['out'],
            POINTER(POINTER(ID3D10SamplerState)),
            'ppSamplers'
        ),
    ),
    COMMETHOD(
        [helpstring('Method VSGetShader')],
        VOID,
        'VSGetShader',
        (
            ['out'],
            POINTER(POINTER(ID3D10VertexShader)),
            'ppVertexShader'
        ),
    ),
    COMMETHOD(
        [helpstring('Method PSGetConstantBuffers')],
        VOID,
        'PSGetConstantBuffers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumBuffers'),
        (
            ['out'],
            POINTER(POINTER(ID3D10Buffer)),
            'ppConstantBuffers'
        ),
    ),
    COMMETHOD(
        [helpstring('Method IAGetInputLayout')],
        VOID,
        'IAGetInputLayout',
        (
            ['out'],
            POINTER(POINTER(ID3D10InputLayout)),
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
            POINTER(POINTER(ID3D10Buffer)),
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
            POINTER(POINTER(ID3D10Buffer)),
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
            POINTER(POINTER(ID3D10Buffer)),
            'ppConstantBuffers'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GSGetShader')],
        VOID,
        'GSGetShader',
        (
            ['out'],
            POINTER(POINTER(ID3D10GeometryShader)),
            'ppGeometryShader'
        ),
    ),
    COMMETHOD(
        [helpstring('Method IAGetPrimitiveTopology')],
        VOID,
        'IAGetPrimitiveTopology',
        (
            ['out'],
            POINTER(D3D10_PRIMITIVE_TOPOLOGY),
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
            POINTER(POINTER(ID3D10ShaderResourceView)),
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
            POINTER(POINTER(ID3D10SamplerState)),
            'ppSamplers'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetPredication')],
        VOID,
        'GetPredication',
        (
            ['out'],
            POINTER(POINTER(ID3D10Predicate)),
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
            POINTER(POINTER(ID3D10ShaderResourceView)),
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
            POINTER(POINTER(ID3D10SamplerState)),
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
            POINTER(POINTER(ID3D10RenderTargetView)),
            'ppRenderTargetViews'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10DepthStencilView)),
            'ppDepthStencilView'
        ),
    ),
    COMMETHOD(
        [helpstring('Method OMGetBlendState')],
        VOID,
        'OMGetBlendState',
        (
            ['out'],
            POINTER(POINTER(ID3D10BlendState)),
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
            POINTER(POINTER(ID3D10DepthStencilState)),
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
            POINTER(POINTER(ID3D10Buffer)),
            'ppSOTargets'
        ),
        (['out'], POINTER(UINT), 'pOffsets'),
    ),
    COMMETHOD(
        [helpstring('Method RSGetState')],
        VOID,
        'RSGetState',
        (
            ['out'],
            POINTER(POINTER(ID3D10RasterizerState)),
            'ppRasterizerState'
        ),
    ),
    COMMETHOD(
        [helpstring('Method RSGetViewports')],
        VOID,
        'RSGetViewports',
        (['out', 'in'], POINTER(UINT), 'NumViewports'),
        (['out'], POINTER(D3D10_VIEWPORT), 'pViewports'),
    ),
    COMMETHOD(
        [helpstring('Method RSGetScissorRects')],
        VOID,
        'RSGetScissorRects',
        (['out', 'in'], POINTER(UINT), 'NumRects'),
        (['out'], POINTER(D3D10_RECT), 'pRects'),
    ),
    COMMETHOD(
        [helpstring('Method GetDeviceRemovedReason')],
        HRESULT,
        'GetDeviceRemovedReason',
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
        [helpstring('Method CreateBuffer')],
        HRESULT,
        'CreateBuffer',
        (['in'], POINTER(D3D10_BUFFER_DESC), 'pDesc'),
        (
            ['in'],
            POINTER(D3D10_SUBRESOURCE_DATA),
            'pInitialData'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10Buffer)),
            'ppBuffer'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateTexture1D')],
        HRESULT,
        'CreateTexture1D',
        (['in'], POINTER(D3D10_TEXTURE1D_DESC), 'pDesc'),
        (
            ['in'],
            POINTER(D3D10_SUBRESOURCE_DATA),
            'pInitialData'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10Texture1D)),
            'ppTexture1D'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateTexture2D')],
        HRESULT,
        'CreateTexture2D',
        (['in'], POINTER(D3D10_TEXTURE2D_DESC), 'pDesc'),
        (
            ['in'],
            POINTER(D3D10_SUBRESOURCE_DATA),
            'pInitialData'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10Texture2D)),
            'ppTexture2D'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateTexture3D')],
        HRESULT,
        'CreateTexture3D',
        (['in'], POINTER(D3D10_TEXTURE3D_DESC), 'pDesc'),
        (
            ['in'],
            POINTER(D3D10_SUBRESOURCE_DATA),
            'pInitialData'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10Texture3D)),
            'ppTexture3D'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateShaderResourceView')],
        HRESULT,
        'CreateShaderResourceView',
        (['in'], POINTER(ID3D10Resource), 'pResource'),
        (
            ['in'],
            POINTER(D3D10_SHADER_RESOURCE_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10ShaderResourceView)),
            'ppSRView'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateRenderTargetView')],
        HRESULT,
        'CreateRenderTargetView',
        (['in'], POINTER(ID3D10Resource), 'pResource'),
        (
            ['in'],
            POINTER(D3D10_RENDER_TARGET_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10RenderTargetView)),
            'ppRTView'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateDepthStencilView')],
        HRESULT,
        'CreateDepthStencilView',
        (['in'], POINTER(ID3D10Resource), 'pResource'),
        (
            ['in'],
            POINTER(D3D10_DEPTH_STENCIL_VIEW_DESC),
            'pDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10DepthStencilView)),
            'ppDepthStencilView'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateInputLayout')],
        HRESULT,
        'CreateInputLayout',
        (
            ['in'],
            POINTER(D3D10_INPUT_ELEMENT_DESC),
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
            POINTER(POINTER(ID3D10InputLayout)),
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
            ['out'],
            POINTER(POINTER(ID3D10VertexShader)),
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
            ['out'],
            POINTER(POINTER(ID3D10GeometryShader)),
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
            POINTER(D3D10_SO_DECLARATION_ENTRY),
            'pSODeclaration'
        ),
        (['in'], UINT, 'NumEntries'),
        (['in'], UINT, 'OutputStreamStride'),
        (
            ['out'],
            POINTER(POINTER(ID3D10GeometryShader)),
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
            ['out'],
            POINTER(POINTER(ID3D10PixelShader)),
            'ppPixelShader'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateBlendState')],
        HRESULT,
        'CreateBlendState',
        (
            ['in'],
            POINTER(D3D10_BLEND_DESC),
            'pBlendStateDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10BlendState)),
            'ppBlendState'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateDepthStencilState')],
        HRESULT,
        'CreateDepthStencilState',
        (
            ['in'],
            POINTER(D3D10_DEPTH_STENCIL_DESC),
            'pDepthStencilDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10DepthStencilState)),
            'ppDepthStencilState'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateRasterizerState')],
        HRESULT,
        'CreateRasterizerState',
        (
            ['in'],
            POINTER(D3D10_RASTERIZER_DESC),
            'pRasterizerDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10RasterizerState)),
            'ppRasterizerState'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateSamplerState')],
        HRESULT,
        'CreateSamplerState',
        (
            ['in'],
            POINTER(D3D10_SAMPLER_DESC),
            'pSamplerDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10SamplerState)),
            'ppSamplerState'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateQuery')],
        HRESULT,
        'CreateQuery',
        (['in'], POINTER(D3D10_QUERY_DESC), 'pQueryDesc'),
        (
            ['out'],
            POINTER(POINTER(ID3D10Query)),
            'ppQuery'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreatePredicate')],
        HRESULT,
        'CreatePredicate',
        (
            ['in'],
            POINTER(D3D10_QUERY_DESC),
            'pPredicateDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10Predicate)),
            'ppPredicate'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateCounter')],
        HRESULT,
        'CreateCounter',
        (
            ['in'],
            POINTER(D3D10_COUNTER_DESC),
            'pCounterDesc'
        ),
        (
            ['out'],
            POINTER(POINTER(ID3D10Counter)),
            'ppCounter'
        ),
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
            POINTER(D3D10_COUNTER_INFO),
            'pCounterInfo'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CheckCounter')],
        HRESULT,
        'CheckCounter',
        (['in'], POINTER(D3D10_COUNTER_DESC), 'pDesc'),
        (['out'], POINTER(D3D10_COUNTER_TYPE), 'pType'),
        (['out'], POINTER(UINT), 'pActiveCounters'),
        (['out'], LPSTR, 'szName'),
        (['out', 'in'], POINTER(UINT), 'pNameLength'),
        (['out'], LPSTR, 'szUnits'),
        (['out', 'in'], POINTER(UINT), 'pUnitsLength'),
        (['out'], LPSTR, 'szDescription'),
        (
            ['out', 'in'],
            POINTER(UINT),
            'pDescriptionLength'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetCreationFlags')],
        UINT,
        'GetCreationFlags',
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
        [helpstring('Method SetTextFilterSize')],
        VOID,
        'SetTextFilterSize',
        (['in'], UINT, 'Width'),
        (['in'], UINT, 'Height'),
    ),
    COMMETHOD(
        [helpstring('Method GetTextFilterSize')],
        VOID,
        'GetTextFilterSize',
        (['out'], POINTER(UINT), 'pWidth'),
        (['out'], POINTER(UINT), 'pHeight'),
    ),
]


 
IID_ID3D10Multithread = MIDL_INTERFACE(
    "{9B7E4E00-342C-4106-A19F-4F2704F689F0}"
)
ID3D10Multithread._iid_ = IID_ID3D10Multithread


ID3D10Multithread._methods_ = [
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


class D3D10_CREATE_DEVICE_FLAG(ENUM):
    D3D10_CREATE_DEVICE_SINGLETHREADED = 0x1
    D3D10_CREATE_DEVICE_DEBUG = 0x2
    D3D10_CREATE_DEVICE_SWITCH_TO_REF = 0x4
    D3D10_CREATE_DEVICE_PREVENT_INTERNAL_THREADING_OPTIMIZATIONS = (
        0x8
    )
    D3D10_CREATE_DEVICE_ALLOW_NULL_FROM_MAP = 0x10
    D3D10_CREATE_DEVICE_BGRA_SUPPORT = 0x20
    D3D10_CREATE_DEVICE_PREVENT_ALTERING_LAYER_SETTINGS_FROM_REGISTRY = (
        0x80
    )
    D3D10_CREATE_DEVICE_STRICT_VALIDATION = 0x200
    D3D10_CREATE_DEVICE_DEBUGGABLE = 0x400


from .d3d10sdklayers_h import * # NOQA
from .d3d10misc_h import * # NOQA
from .d3d10shader_h import * # NOQA
from .d3d10effect_h import * # NOQA


IID_ID3D10DeviceChild = GUID('{9B7E4C00-342C-4106-A19F-4F2704F689F0}')
IID_ID3D10DepthStencilState = GUID('{2B4B1CC8-A4AD-41F8-8322-CA86FC3EC675}')
IID_ID3D10BlendState = GUID('{EDAD8D19-8A35-4D6D-8566-2EA276CDE161}')
IID_ID3D10RasterizerState = GUID('{A2A07292-89AF-4345-BE2E-C53D9FBB6E9F}')
IID_ID3D10Resource = GUID('{9B7E4C01-342C-4106-A19F-4F2704F689F0}')
IID_ID3D10Buffer = GUID('{9B7E4C02-342C-4106-A19F-4F2704F689F0}')
IID_ID3D10Texture1D = GUID('{9B7E4C03-342C-4106-A19F-4F2704F689F0}')
IID_ID3D10Texture2D = GUID('{9B7E4C04-342C-4106-A19F-4F2704F689F0}')
IID_ID3D10Texture3D = GUID('{9B7E4C05-342C-4106-A19F-4F2704F689F0}')
IID_ID3D10View = GUID('{C902B03F-60A7-49BA-9936-2A3AB37A7E33}')
IID_ID3D10ShaderResourceView = GUID('{9B7E4C07-342C-4106-A19F-4F2704F689F0}')
IID_ID3D10RenderTargetView = GUID('{9B7E4C08-342C-4106-A19F-4F2704F689F0}')
IID_ID3D10DepthStencilView = GUID('{9B7E4C09-342C-4106-A19F-4F2704F689F0}')
IID_ID3D10VertexShader = GUID('{9B7E4C0A-342C-4106-A19F-4F2704F689F0}')
IID_ID3D10GeometryShader = GUID('{6316BE88-54CD-4040-AB44-20461BC81F68}')
IID_ID3D10PixelShader = GUID('{4968B601-9D00-4CDE-8346-8E7F675819B6}')
IID_ID3D10InputLayout = GUID('{9B7E4C0B-342C-4106-A19F-4F2704F689F0}')
IID_ID3D10SamplerState = GUID('{9B7E4C0C-342C-4106-A19F-4F2704F689F0}')
IID_ID3D10Asynchronous = GUID('{9B7E4C0D-342C-4106-A19F-4F2704F689F0}')
IID_ID3D10Query = GUID('{9B7E4C0E-342C-4106-A19F-4F2704F689F0}')
IID_ID3D10Predicate = GUID('{9B7E4C10-342C-4106-A19F-4F2704F689F0}')
IID_ID3D10Counter = GUID('{9B7E4C11-342C-4106-A19F-4F2704F689F0}')
IID_ID3D10Device = GUID('{9B7E4C0F-342C-4106-A19F-4F2704F689F0}')
IID_ID3D10Multithread = GUID('{9B7E4E00-342C-4106-A19F-4F2704F689F0}')
