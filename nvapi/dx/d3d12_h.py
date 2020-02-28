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


class ID3D12CommandQueue(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = None


class D3D12_COMMAND_QUEUE_DESC(ctypes.Structure):
    pass


class D3D12_INPUT_ELEMENT_DESC(ctypes.Structure):
    pass


class D3D12_SO_DECLARATION_ENTRY(ctypes.Structure):
    pass


class D3D12_VIEWPORT(ctypes.Structure):
    pass


class D3D12_BOX(ctypes.Structure):
    pass


class D3D12_DEPTH_STENCILOP_DESC(ctypes.Structure):
    pass


class D3D12_DEPTH_STENCIL_DESC(ctypes.Structure):
    pass


class D3D12_DEPTH_STENCIL_DESC1(ctypes.Structure):
    pass


class D3D12_RENDER_TARGET_BLEND_DESC(ctypes.Structure):
    pass


class D3D12_BLEND_DESC(ctypes.Structure):
    pass


class D3D12_RASTERIZER_DESC(ctypes.Structure):
    pass


class D3D12_SHADER_BYTECODE(ctypes.Structure):
    pass


class D3D12_STREAM_OUTPUT_DESC(ctypes.Structure):
    pass


class D3D12_INPUT_LAYOUT_DESC(ctypes.Structure):
    pass


class D3D12_CACHED_PIPELINE_STATE(ctypes.Structure):
    pass


class D3D12_GRAPHICS_PIPELINE_STATE_DESC(ctypes.Structure):
    pass


class D3D12_COMPUTE_PIPELINE_STATE_DESC(ctypes.Structure):
    pass


class D3D12_RT_FORMAT_ARRAY(ctypes.Structure):
    pass


class D3D12_PIPELINE_STATE_STREAM_DESC(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_D3D12_OPTIONS(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_D3D12_OPTIONS1(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_D3D12_OPTIONS2(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_ROOT_SIGNATURE(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_ARCHITECTURE(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_ARCHITECTURE1(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_FEATURE_LEVELS(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_SHADER_MODEL(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_FORMAT_SUPPORT(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_MULTISAMPLE_QUALITY_LEVELS(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_FORMAT_INFO(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_GPU_VIRTUAL_ADDRESS_SUPPORT(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_SHADER_CACHE(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_COMMAND_QUEUE_PRIORITY(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_D3D12_OPTIONS3(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_EXISTING_HEAPS(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_D3D12_OPTIONS4(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_SERIALIZATION(ctypes.Structure):
    pass


class D3D12_FEATURE_DATA_CROSS_NODE(ctypes.Structure):
    pass


class D3D12_RESOURCE_ALLOCATION_INFO(ctypes.Structure):
    pass


class D3D12_RESOURCE_ALLOCATION_INFO1(ctypes.Structure):
    pass


class D3D12_HEAP_PROPERTIES(ctypes.Structure):
    pass


class D3D12_HEAP_DESC(ctypes.Structure):
    pass


class D3D12_RESOURCE_DESC(ctypes.Structure):
    pass


class D3D12_DEPTH_STENCIL_VALUE(ctypes.Structure):
    pass


class D3D12_CLEAR_VALUE(ctypes.Structure):
    pass


class D3D12_RANGE(ctypes.Structure):
    pass


class D3D12_RANGE_UINT64(ctypes.Structure):
    pass


class D3D12_SUBRESOURCE_RANGE_UINT64(ctypes.Structure):
    pass


class D3D12_SUBRESOURCE_INFO(ctypes.Structure):
    pass


class D3D12_TILED_RESOURCE_COORDINATE(ctypes.Structure):
    pass


class D3D12_TILE_REGION_SIZE(ctypes.Structure):
    pass


class D3D12_SUBRESOURCE_TILING(ctypes.Structure):
    pass


class D3D12_TILE_SHAPE(ctypes.Structure):
    pass


class D3D12_PACKED_MIP_INFO(ctypes.Structure):
    pass


class D3D12_RESOURCE_TRANSITION_BARRIER(ctypes.Structure):
    pass


class D3D12_RESOURCE_ALIASING_BARRIER(ctypes.Structure):
    pass


class D3D12_RESOURCE_UAV_BARRIER(ctypes.Structure):
    pass


class D3D12_RESOURCE_BARRIER(ctypes.Structure):
    pass


class D3D12_SUBRESOURCE_FOOTPRINT(ctypes.Structure):
    pass


class D3D12_PLACED_SUBRESOURCE_FOOTPRINT(ctypes.Structure):
    pass


class D3D12_TEXTURE_COPY_LOCATION(ctypes.Structure):
    pass


class D3D12_SAMPLE_POSITION(ctypes.Structure):
    pass


class D3D12_VIEW_INSTANCE_LOCATION(ctypes.Structure):
    pass


class D3D12_VIEW_INSTANCING_DESC(ctypes.Structure):
    pass


class D3D12_BUFFER_SRV(ctypes.Structure):
    pass


class D3D12_TEX1D_SRV(ctypes.Structure):
    pass


class D3D12_TEX1D_ARRAY_SRV(ctypes.Structure):
    pass


class D3D12_TEX2D_SRV(ctypes.Structure):
    pass


class D3D12_TEX2D_ARRAY_SRV(ctypes.Structure):
    pass


class D3D12_TEX3D_SRV(ctypes.Structure):
    pass


class D3D12_TEXCUBE_SRV(ctypes.Structure):
    pass


class D3D12_TEXCUBE_ARRAY_SRV(ctypes.Structure):
    pass


class D3D12_TEX2DMS_SRV(ctypes.Structure):
    pass


class D3D12_TEX2DMS_ARRAY_SRV(ctypes.Structure):
    pass


class D3D12_SHADER_RESOURCE_VIEW_DESC(ctypes.Structure):
    pass


class D3D12_CONSTANT_BUFFER_VIEW_DESC(ctypes.Structure):
    pass


class D3D12_SAMPLER_DESC(ctypes.Structure):
    pass


class D3D12_BUFFER_UAV(ctypes.Structure):
    pass


class D3D12_TEX1D_UAV(ctypes.Structure):
    pass


class D3D12_TEX1D_ARRAY_UAV(ctypes.Structure):
    pass


class D3D12_TEX2D_UAV(ctypes.Structure):
    pass


class D3D12_TEX2D_ARRAY_UAV(ctypes.Structure):
    pass


class D3D12_TEX3D_UAV(ctypes.Structure):
    pass


class D3D12_UNORDERED_ACCESS_VIEW_DESC(ctypes.Structure):
    pass


class D3D12_BUFFER_RTV(ctypes.Structure):
    pass


class D3D12_TEX1D_RTV(ctypes.Structure):
    pass


class D3D12_TEX1D_ARRAY_RTV(ctypes.Structure):
    pass


class D3D12_TEX2D_RTV(ctypes.Structure):
    pass


class D3D12_TEX2DMS_RTV(ctypes.Structure):
    pass


class D3D12_TEX2D_ARRAY_RTV(ctypes.Structure):
    pass


class D3D12_TEX2DMS_ARRAY_RTV(ctypes.Structure):
    pass


class D3D12_TEX3D_RTV(ctypes.Structure):
    pass


class D3D12_RENDER_TARGET_VIEW_DESC(ctypes.Structure):
    pass


class D3D12_TEX1D_DSV(ctypes.Structure):
    pass


class D3D12_TEX1D_ARRAY_DSV(ctypes.Structure):
    pass


class D3D12_TEX2D_DSV(ctypes.Structure):
    pass


class D3D12_TEX2D_ARRAY_DSV(ctypes.Structure):
    pass


class D3D12_TEX2DMS_DSV(ctypes.Structure):
    pass


class D3D12_TEX2DMS_ARRAY_DSV(ctypes.Structure):
    pass


class D3D12_DEPTH_STENCIL_VIEW_DESC(ctypes.Structure):
    pass


class D3D12_DESCRIPTOR_HEAP_DESC(ctypes.Structure):
    pass


class D3D12_DESCRIPTOR_RANGE(ctypes.Structure):
    pass


class D3D12_ROOT_DESCRIPTOR_TABLE(ctypes.Structure):
    pass


class D3D12_ROOT_CONSTANTS(ctypes.Structure):
    pass


class D3D12_ROOT_DESCRIPTOR(ctypes.Structure):
    pass


class D3D12_ROOT_PARAMETER(ctypes.Structure):
    pass


class D3D12_STATIC_SAMPLER_DESC(ctypes.Structure):
    pass


class D3D12_ROOT_SIGNATURE_DESC(ctypes.Structure):
    pass


class D3D12_DESCRIPTOR_RANGE1(ctypes.Structure):
    pass


class D3D12_ROOT_DESCRIPTOR_TABLE1(ctypes.Structure):
    pass


class D3D12_ROOT_DESCRIPTOR1(ctypes.Structure):
    pass


class D3D12_ROOT_PARAMETER1(ctypes.Structure):
    pass


class D3D12_ROOT_SIGNATURE_DESC1(ctypes.Structure):
    pass


class D3D12_VERSIONED_ROOT_SIGNATURE_DESC(ctypes.Structure):
    pass


class D3D12_CPU_DESCRIPTOR_HANDLE(ctypes.Structure):
    pass


class D3D12_GPU_DESCRIPTOR_HANDLE(ctypes.Structure):
    pass


class D3D12_DISCARD_REGION(ctypes.Structure):
    pass


class D3D12_QUERY_HEAP_DESC(ctypes.Structure):
    pass


class D3D12_QUERY_DATA_PIPELINE_STATISTICS(ctypes.Structure):
    pass


class D3D12_QUERY_DATA_SO_STATISTICS(ctypes.Structure):
    pass


class D3D12_STREAM_OUTPUT_BUFFER_VIEW(ctypes.Structure):
    pass


class D3D12_DRAW_ARGUMENTS(ctypes.Structure):
    pass


class D3D12_DRAW_INDEXED_ARGUMENTS(ctypes.Structure):
    pass


class D3D12_DISPATCH_ARGUMENTS(ctypes.Structure):
    pass


class D3D12_VERTEX_BUFFER_VIEW(ctypes.Structure):
    pass


class D3D12_INDEX_BUFFER_VIEW(ctypes.Structure):
    pass


class D3D12_INDIRECT_ARGUMENT_DESC(ctypes.Structure):
    pass


class D3D12_COMMAND_SIGNATURE_DESC(ctypes.Structure):
    pass


class D3D12_WRITEBUFFERIMMEDIATE_PARAMETER(ctypes.Structure):
    pass


class __LUID(ctypes.Structure):
    pass


LUID = __LUID


class D3D12_FEATURE_DATA_PROTECTED_RESOURCE_SESSION_SUPPORT(ctypes.Structure):
    pass


class D3D12_PROTECTED_RESOURCE_SESSION_DESC(ctypes.Structure):
    pass


class D3D12_SUBRESOURCE_DATA(ctypes.Structure):
    pass


class D3D12_MEMCPY_DEST(ctypes.Structure):
    pass


from .dxgicommon_h import *  # NOQA
from .dxgi_format_h import *  # NOQA
from .d3dcommon_h import *  # NOQA


class ID3D12Object(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12DeviceChild(ID3D12Object):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12RootSignature(ID3D12DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12RootSignatureDeserializer(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12VersionedRootSignatureDeserializer(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12Pageable(ID3D12DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12Heap(ID3D12Pageable):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12Resource(ID3D12Pageable):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12CommandAllocator(ID3D12Pageable):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12Fence(ID3D12Pageable):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12Fence1(ID3D12Fence):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12PipelineState(ID3D12Pageable):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12DescriptorHeap(ID3D12Pageable):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12QueryHeap(ID3D12Pageable):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12CommandSignature(ID3D12Pageable):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12CommandList(ID3D12DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12GraphicsCommandList(ID3D12CommandList):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12GraphicsCommandList1(ID3D12GraphicsCommandList):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12GraphicsCommandList2(ID3D12GraphicsCommandList1):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12Device(ID3D12Object):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12PipelineLibrary(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12PipelineLibrary1(ID3D12DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12Device1(ID3D12Device):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12Device2(ID3D12Device1):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12Device3(ID3D12Device2):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12ProtectedSession(ID3D12DeviceChild):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12ProtectedResourceSession(ID3D12ProtectedSession):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12Device4(ID3D12Device3):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12Resource1(ID3D12Resource):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12Heap1(ID3D12Heap):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12GraphicsCommandList3(ID3D12GraphicsCommandList2):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D12Tools(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


D3D12_GPU_VIRTUAL_ADDRESS = UINT64


class D3D12_COMMAND_LIST_TYPE(ENUM):
    D3D12_COMMAND_LIST_TYPE_DIRECT = 0
    D3D12_COMMAND_LIST_TYPE_BUNDLE = 1
    D3D12_COMMAND_LIST_TYPE_COMPUTE = 2
    D3D12_COMMAND_LIST_TYPE_COPY = 3
    D3D12_COMMAND_LIST_TYPE_VIDEO_DECODE = 4
    D3D12_COMMAND_LIST_TYPE_VIDEO_PROCESS = 5


class D3D12_COMMAND_QUEUE_FLAGS(ENUM):
    D3D12_COMMAND_QUEUE_FLAG_NONE = 0
    D3D12_COMMAND_QUEUE_FLAG_DISABLE_GPU_TIMEOUT = 0x1


class D3D12_COMMAND_QUEUE_PRIORITY(ENUM):
    D3D12_COMMAND_QUEUE_PRIORITY_NORMAL = 0
    D3D12_COMMAND_QUEUE_PRIORITY_HIGH = 100
    D3D12_COMMAND_QUEUE_PRIORITY_GLOBAL_REALTIME = 10000

D3D12_COMMAND_QUEUE_DESC._fields_ = [
    ('Type', D3D12_COMMAND_LIST_TYPE),
    ('Priority', INT),
    ('Flags', D3D12_COMMAND_QUEUE_FLAGS),
    ('NodeMask', UINT),
]


class D3D12_PRIMITIVE_TOPOLOGY_TYPE(ENUM):
    D3D12_PRIMITIVE_TOPOLOGY_TYPE_UNDEFINED = 0
    D3D12_PRIMITIVE_TOPOLOGY_TYPE_POINT = 1
    D3D12_PRIMITIVE_TOPOLOGY_TYPE_LINE = 2
    D3D12_PRIMITIVE_TOPOLOGY_TYPE_TRIANGLE = 3
    D3D12_PRIMITIVE_TOPOLOGY_TYPE_PATCH = 4


class D3D12_INPUT_CLASSIFICATION(ENUM):
    D3D12_INPUT_CLASSIFICATION_PER_VERTEX_DATA = 0
    D3D12_INPUT_CLASSIFICATION_PER_INSTANCE_DATA = 1

D3D12_INPUT_ELEMENT_DESC._fields_ = [
    ('SemanticName', LPCSTR),
    ('SemanticIndex', UINT),
    ('Format', DXGI_FORMAT),
    ('InputSlot', UINT),
    ('AlignedByteOffset', UINT),
    ('InputSlotClass', D3D12_INPUT_CLASSIFICATION),
    ('InstanceDataStepRate', UINT),
]


class D3D12_FILL_MODE(ENUM):
    D3D12_FILL_MODE_WIREFRAME = 2
    D3D12_FILL_MODE_SOLID = 3

D3D12_PRIMITIVE_TOPOLOGY = D3D_PRIMITIVE_TOPOLOGY
D3D12_PRIMITIVE = D3D_PRIMITIVE


class D3D12_CULL_MODE(ENUM):
    D3D12_CULL_MODE_NONE = 1
    D3D12_CULL_MODE_FRONT = 2
    D3D12_CULL_MODE_BACK = 3

D3D12_SO_DECLARATION_ENTRY._fields_ = [
    ('Stream', UINT),
    ('SemanticName', LPCSTR),
    ('SemanticIndex', UINT),
    ('StartComponent', BYTE),
    ('ComponentCount', BYTE),
    ('OutputSlot', BYTE),
]

D3D12_VIEWPORT._fields_ = [
    ('TopLeftX', FLOAT),
    ('TopLeftY', FLOAT),
    ('Width', FLOAT),
    ('Height', FLOAT),
    ('MinDepth', FLOAT),
    ('MaxDepth', FLOAT),
]
D3D12_RECT = RECT

D3D12_BOX._fields_ = [
    ('left', UINT),
    ('top', UINT),
    ('front', UINT),
    ('right', UINT),
    ('bottom', UINT),
    ('back', UINT),
]


class D3D12_COMPARISON_FUNC(ENUM):
    D3D12_COMPARISON_FUNC_NEVER = 1
    D3D12_COMPARISON_FUNC_LESS = 2
    D3D12_COMPARISON_FUNC_EQUAL = 3
    D3D12_COMPARISON_FUNC_LESS_EQUAL = 4
    D3D12_COMPARISON_FUNC_GREATER = 5
    D3D12_COMPARISON_FUNC_NOT_EQUAL = 6
    D3D12_COMPARISON_FUNC_GREATER_EQUAL = 7
    D3D12_COMPARISON_FUNC_ALWAYS = 8


class D3D12_DEPTH_WRITE_MASK(ENUM):
    D3D12_DEPTH_WRITE_MASK_ZERO = 0
    D3D12_DEPTH_WRITE_MASK_ALL = 1


class D3D12_STENCIL_OP(ENUM):
    D3D12_STENCIL_OP_KEEP = 1
    D3D12_STENCIL_OP_ZERO = 2
    D3D12_STENCIL_OP_REPLACE = 3
    D3D12_STENCIL_OP_INCR_SAT = 4
    D3D12_STENCIL_OP_DECR_SAT = 5
    D3D12_STENCIL_OP_INVERT = 6
    D3D12_STENCIL_OP_INCR = 7
    D3D12_STENCIL_OP_DECR = 8

D3D12_DEPTH_STENCILOP_DESC._fields_ = [
    ('StencilFailOp', D3D12_STENCIL_OP),
    ('StencilDepthFailOp', D3D12_STENCIL_OP),
    ('StencilPassOp', D3D12_STENCIL_OP),
    ('StencilFunc', D3D12_COMPARISON_FUNC),
]

D3D12_DEPTH_STENCIL_DESC._fields_ = [
    ('DepthEnable', BOOL),
    ('DepthWriteMask', D3D12_DEPTH_WRITE_MASK),
    ('DepthFunc', D3D12_COMPARISON_FUNC),
    ('StencilEnable', BOOL),
    ('StencilReadMask', UINT8),
    ('StencilWriteMask', UINT8),
    ('FrontFace', D3D12_DEPTH_STENCILOP_DESC),
    ('BackFace', D3D12_DEPTH_STENCILOP_DESC),
]

D3D12_DEPTH_STENCIL_DESC1._fields_ = [
    ('DepthEnable', BOOL),
    ('DepthWriteMask', D3D12_DEPTH_WRITE_MASK),
    ('DepthFunc', D3D12_COMPARISON_FUNC),
    ('StencilEnable', BOOL),
    ('StencilReadMask', UINT8),
    ('StencilWriteMask', UINT8),
    ('FrontFace', D3D12_DEPTH_STENCILOP_DESC),
    ('BackFace', D3D12_DEPTH_STENCILOP_DESC),
    ('DepthBoundsTestEnable', BOOL),
]


class D3D12_BLEND(ENUM):
    D3D12_BLEND_ZERO = 1
    D3D12_BLEND_ONE = 2
    D3D12_BLEND_SRC_COLOR = 3
    D3D12_BLEND_INV_SRC_COLOR = 4
    D3D12_BLEND_SRC_ALPHA = 5
    D3D12_BLEND_INV_SRC_ALPHA = 6
    D3D12_BLEND_DEST_ALPHA = 7
    D3D12_BLEND_INV_DEST_ALPHA = 8
    D3D12_BLEND_DEST_COLOR = 9
    D3D12_BLEND_INV_DEST_COLOR = 10
    D3D12_BLEND_SRC_ALPHA_SAT = 11
    D3D12_BLEND_BLEND_FACTOR = 14
    D3D12_BLEND_INV_BLEND_FACTOR = 15
    D3D12_BLEND_SRC1_COLOR = 16
    D3D12_BLEND_INV_SRC1_COLOR = 17
    D3D12_BLEND_SRC1_ALPHA = 18
    D3D12_BLEND_INV_SRC1_ALPHA = 19


class D3D12_BLEND_OP(ENUM):
    D3D12_BLEND_OP_ADD = 1
    D3D12_BLEND_OP_SUBTRACT = 2
    D3D12_BLEND_OP_REV_SUBTRACT = 3
    D3D12_BLEND_OP_MIN = 4
    D3D12_BLEND_OP_MAX = 5


class D3D12_COLOR_WRITE_ENABLE(ENUM):
    D3D12_COLOR_WRITE_ENABLE_RED = 1
    D3D12_COLOR_WRITE_ENABLE_GREEN = 2
    D3D12_COLOR_WRITE_ENABLE_BLUE = 4
    D3D12_COLOR_WRITE_ENABLE_ALPHA = 8
    D3D12_COLOR_WRITE_ENABLE_ALL = (
        D3D12_COLOR_WRITE_ENABLE_RED |
        D3D12_COLOR_WRITE_ENABLE_GREEN |
        D3D12_COLOR_WRITE_ENABLE_BLUE |
        D3D12_COLOR_WRITE_ENABLE_ALPHA
    )


class D3D12_LOGIC_OP(ENUM):
    D3D12_LOGIC_OP_CLEAR = 0
    D3D12_LOGIC_OP_SET = D3D12_LOGIC_OP_CLEAR + 1
    D3D12_LOGIC_OP_COPY = D3D12_LOGIC_OP_SET + 1
    D3D12_LOGIC_OP_COPY_INVERTED = D3D12_LOGIC_OP_COPY + 1
    D3D12_LOGIC_OP_NOOP = D3D12_LOGIC_OP_COPY_INVERTED + 1
    D3D12_LOGIC_OP_INVERT = D3D12_LOGIC_OP_NOOP + 1
    D3D12_LOGIC_OP_AND = D3D12_LOGIC_OP_INVERT + 1
    D3D12_LOGIC_OP_NAND = D3D12_LOGIC_OP_AND + 1
    D3D12_LOGIC_OP_OR = D3D12_LOGIC_OP_NAND + 1
    D3D12_LOGIC_OP_NOR = D3D12_LOGIC_OP_OR + 1
    D3D12_LOGIC_OP_XOR = D3D12_LOGIC_OP_NOR + 1
    D3D12_LOGIC_OP_EQUIV = D3D12_LOGIC_OP_XOR + 1
    D3D12_LOGIC_OP_AND_REVERSE = D3D12_LOGIC_OP_EQUIV + 1
    D3D12_LOGIC_OP_AND_INVERTED = D3D12_LOGIC_OP_AND_REVERSE + 1
    D3D12_LOGIC_OP_OR_REVERSE = D3D12_LOGIC_OP_AND_INVERTED + 1
    D3D12_LOGIC_OP_OR_INVERTED = D3D12_LOGIC_OP_OR_REVERSE + 1

D3D12_RENDER_TARGET_BLEND_DESC._fields_ = [
    ('BlendEnable', BOOL),
    ('LogicOpEnable', BOOL),
    ('SrcBlend', D3D12_BLEND),
    ('DestBlend', D3D12_BLEND),
    ('BlendOp', D3D12_BLEND_OP),
    ('SrcBlendAlpha', D3D12_BLEND),
    ('DestBlendAlpha', D3D12_BLEND),
    ('BlendOpAlpha', D3D12_BLEND_OP),
    ('LogicOp', D3D12_LOGIC_OP),
    ('RenderTargetWriteMask', UINT8),
]

D3D12_BLEND_DESC._fields_ = [
    ('AlphaToCoverageEnable', BOOL),
    ('IndependentBlendEnable', BOOL),
    ('RenderTarget', D3D12_RENDER_TARGET_BLEND_DESC * 8),
]

# /* Note, the array size for RenderTarget[] above is
# D3D12_SIMULTANEOUS_RENDERTARGET_COUNT. IDL processing/generation of
# this header replaces the define; this comment is merely explaining
# what happened.
class D3D12_CONSERVATIVE_RASTERIZATION_MODE(ENUM):
    D3D12_CONSERVATIVE_RASTERIZATION_MODE_OFF = 0
    D3D12_CONSERVATIVE_RASTERIZATION_MODE_ON = 1

D3D12_RASTERIZER_DESC._fields_ = [
    ('FillMode', D3D12_FILL_MODE),
    ('CullMode', D3D12_CULL_MODE),
    ('FrontCounterClockwise', BOOL),
    ('DepthBias', INT),
    ('DepthBiasClamp', FLOAT),
    ('SlopeScaledDepthBias', FLOAT),
    ('DepthClipEnable', BOOL),
    ('MultisampleEnable', BOOL),
    ('AntialiasedLineEnable', BOOL),
    ('ForcedSampleCount', UINT),
    ('ConservativeRaster', D3D12_CONSERVATIVE_RASTERIZATION_MODE),
]
      
IID_ID3D12Object = MIDL_INTERFACE(
    "{C4FEC28F-7966-4E95-9F94-F431CB56C3B8}"
)
ID3D12Object._iid_ = IID_ID3D12Object


ID3D12Object._methods_ = [
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
        [helpstring('Method SetName')],
        HRESULT,
        'SetName',
        (['in'], LPCWSTR, 'Name'),
    ),
]

IID_ID3D12DeviceChild = MIDL_INTERFACE(
    "{905DB94B-A00C-4140-9DF5-2B64CA9EA357}"
)
ID3D12DeviceChild._iid_ = IID_ID3D12DeviceChild


ID3D12DeviceChild._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDevice')],
        HRESULT,
        'GetDevice',
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvDevice'),
    ),
]

IID_ID3D12RootSignature = MIDL_INTERFACE(
    "{C54A6B66-72DF-4EE8-8BE5-A946A1429214}"
)
ID3D12RootSignature._iid_ = IID_ID3D12RootSignature


ID3D12RootSignature._methods_ = []


D3D12_SHADER_BYTECODE._fields_ = [
    ('pShaderBytecode', POINTER(VOID)),
    ('BytecodeLength', SIZE_T),
]

D3D12_STREAM_OUTPUT_DESC._fields_ = [
    ('pSODeclaration', POINTER(D3D12_SO_DECLARATION_ENTRY)),
    ('NumEntries', UINT),
    ('pBufferStrides', POINTER(UINT)),
    ('NumStrides', UINT),
    ('RasterizedStream', UINT),
]

D3D12_INPUT_LAYOUT_DESC._fields_ = [
    ('pInputElementDescs', POINTER(D3D12_INPUT_ELEMENT_DESC)),
    ('NumElements', UINT),
]


class D3D12_INDEX_BUFFER_STRIP_CUT_VALUE(ENUM):
    D3D12_INDEX_BUFFER_STRIP_CUT_VALUE_DISABLED = 0
    D3D12_INDEX_BUFFER_STRIP_CUT_VALUE_0xFFFF = 1
    D3D12_INDEX_BUFFER_STRIP_CUT_VALUE_0xFFFFFFFF = 2

D3D12_CACHED_PIPELINE_STATE._fields_ = [
    ('pCachedBlob', POINTER(VOID)),
    ('CachedBlobSizeInBytes', SIZE_T),
]


class D3D12_PIPELINE_STATE_FLAGS(ENUM):
    D3D12_PIPELINE_STATE_FLAG_NONE = 0
    D3D12_PIPELINE_STATE_FLAG_TOOL_DEBUG = 0x1

D3D12_GRAPHICS_PIPELINE_STATE_DESC._fields_ = [
    ('pRootSignature', POINTER(ID3D12RootSignature)),
    ('VS', D3D12_SHADER_BYTECODE),
    ('PS', D3D12_SHADER_BYTECODE),
    ('DS', D3D12_SHADER_BYTECODE),
    ('HS', D3D12_SHADER_BYTECODE),
    ('GS', D3D12_SHADER_BYTECODE),
    ('StreamOutput', D3D12_STREAM_OUTPUT_DESC),
    ('BlendState', D3D12_BLEND_DESC),
    ('SampleMask', UINT),
    ('RasterizerState', D3D12_RASTERIZER_DESC),
    ('DepthStencilState', D3D12_DEPTH_STENCIL_DESC),
    ('InputLayout', D3D12_INPUT_LAYOUT_DESC),
    ('IBStripCutValue', D3D12_INDEX_BUFFER_STRIP_CUT_VALUE),
    ('PrimitiveTopologyType', D3D12_PRIMITIVE_TOPOLOGY_TYPE),
    ('NumRenderTargets', UINT),
    ('RTVFormats', DXGI_FORMAT * 8),
    ('DSVFormat', DXGI_FORMAT),
    ('SampleDesc', DXGI_SAMPLE_DESC),
    ('NodeMask', UINT),
    ('CachedPSO', D3D12_CACHED_PIPELINE_STATE),
    ('Flags', D3D12_PIPELINE_STATE_FLAGS),
]

D3D12_COMPUTE_PIPELINE_STATE_DESC._fields_ = [
    ('pRootSignature', POINTER(ID3D12RootSignature)),
    ('CS', D3D12_SHADER_BYTECODE),
    ('NodeMask', UINT),
    ('CachedPSO', D3D12_CACHED_PIPELINE_STATE),
    ('Flags', D3D12_PIPELINE_STATE_FLAGS),
]

D3D12_RT_FORMAT_ARRAY._fields_ = [
    ('RTFormats', DXGI_FORMAT * 8),
    ('NumRenderTargets', UINT),
]

D3D12_PIPELINE_STATE_STREAM_DESC._fields_ = [
    ('SizeInBytes', SIZE_T),
    ('pPipelineStateSubobjectStream', POINTER(VOID)),
]


class D3D12_PIPELINE_STATE_SUBOBJECT_TYPE(ENUM):
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_ROOT_SIGNATURE = 0
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_VS = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_ROOT_SIGNATURE + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_PS = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_VS + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_DS = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_PS + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_HS = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_DS + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_GS = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_HS + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_CS = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_GS + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_STREAM_OUTPUT = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_CS + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_BLEND = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_STREAM_OUTPUT + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_SAMPLE_MASK = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_BLEND + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_RASTERIZER = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_SAMPLE_MASK + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_DEPTH_STENCIL = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_RASTERIZER + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_INPUT_LAYOUT = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_DEPTH_STENCIL + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_IB_STRIP_CUT_VALUE = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_INPUT_LAYOUT + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_PRIMITIVE_TOPOLOGY = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_IB_STRIP_CUT_VALUE + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_RENDER_TARGET_FORMATS = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_PRIMITIVE_TOPOLOGY + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_DEPTH_STENCIL_FORMAT = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_RENDER_TARGET_FORMATS + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_SAMPLE_DESC = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_DEPTH_STENCIL_FORMAT + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_NODE_MASK = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_SAMPLE_DESC + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_CACHED_PSO = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_NODE_MASK + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_FLAGS = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_CACHED_PSO + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_DEPTH_STENCIL1 = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_FLAGS + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_VIEW_INSTANCING = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_DEPTH_STENCIL1 + 1
    )
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_MAX_VALID = (
        D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_VIEW_INSTANCING + 1
    )


class D3D12_FEATURE(ENUM):
    D3D12_FEATURE_D3D12_OPTIONS = 0
    D3D12_FEATURE_ARCHITECTURE = 1
    D3D12_FEATURE_FEATURE_LEVELS = 2
    D3D12_FEATURE_FORMAT_SUPPORT = 3
    D3D12_FEATURE_MULTISAMPLE_QUALITY_LEVELS = 4
    D3D12_FEATURE_FORMAT_INFO = 5
    D3D12_FEATURE_GPU_VIRTUAL_ADDRESS_SUPPORT = 6
    D3D12_FEATURE_SHADER_MODEL = 7
    D3D12_FEATURE_D3D12_OPTIONS1 = 8
    D3D12_FEATURE_PROTECTED_RESOURCE_SESSION_SUPPORT = 10
    D3D12_FEATURE_ROOT_SIGNATURE = 12
    D3D12_FEATURE_ARCHITECTURE1 = 16
    D3D12_FEATURE_D3D12_OPTIONS2 = 18
    D3D12_FEATURE_SHADER_CACHE = 19
    D3D12_FEATURE_COMMAND_QUEUE_PRIORITY = 20
    D3D12_FEATURE_D3D12_OPTIONS3 = 21
    D3D12_FEATURE_EXISTING_HEAPS = 22
    D3D12_FEATURE_D3D12_OPTIONS4 = 23
    D3D12_FEATURE_SERIALIZATION = 24
    D3D12_FEATURE_CROSS_NODE = 25


class D3D12_SHADER_MIN_PRECISION_SUPPORT(ENUM):
    D3D12_SHADER_MIN_PRECISION_SUPPORT_NONE = 0
    D3D12_SHADER_MIN_PRECISION_SUPPORT_10_BIT = 0x1
    D3D12_SHADER_MIN_PRECISION_SUPPORT_16_BIT = 0x2


class D3D12_TILED_RESOURCES_TIER(ENUM):
    D3D12_TILED_RESOURCES_TIER_NOT_SUPPORTED = 0
    D3D12_TILED_RESOURCES_TIER_1 = 1
    D3D12_TILED_RESOURCES_TIER_2 = 2
    D3D12_TILED_RESOURCES_TIER_3 = 3
    D3D12_TILED_RESOURCES_TIER_4 = 4


class D3D12_RESOURCE_BINDING_TIER(ENUM):
    D3D12_RESOURCE_BINDING_TIER_1 = 1
    D3D12_RESOURCE_BINDING_TIER_2 = 2
    D3D12_RESOURCE_BINDING_TIER_3 = 3


class D3D12_CONSERVATIVE_RASTERIZATION_TIER(ENUM):
    D3D12_CONSERVATIVE_RASTERIZATION_TIER_NOT_SUPPORTED = 0
    D3D12_CONSERVATIVE_RASTERIZATION_TIER_1 = 1
    D3D12_CONSERVATIVE_RASTERIZATION_TIER_2 = 2
    D3D12_CONSERVATIVE_RASTERIZATION_TIER_3 = 3


class D3D12_FORMAT_SUPPORT1(ENUM):
    D3D12_FORMAT_SUPPORT1_NONE = 0
    D3D12_FORMAT_SUPPORT1_BUFFER = 0x1
    D3D12_FORMAT_SUPPORT1_IA_VERTEX_BUFFER = 0x2
    D3D12_FORMAT_SUPPORT1_IA_INDEX_BUFFER = 0x4
    D3D12_FORMAT_SUPPORT1_SO_BUFFER = 0x8
    D3D12_FORMAT_SUPPORT1_TEXTURE1D = 0x10
    D3D12_FORMAT_SUPPORT1_TEXTURE2D = 0x20
    D3D12_FORMAT_SUPPORT1_TEXTURE3D = 0x40
    D3D12_FORMAT_SUPPORT1_TEXTURECUBE = 0x80
    D3D12_FORMAT_SUPPORT1_SHADER_LOAD = 0x100
    D3D12_FORMAT_SUPPORT1_SHADER_SAMPLE = 0x200
    D3D12_FORMAT_SUPPORT1_SHADER_SAMPLE_COMPARISON = 0x400
    D3D12_FORMAT_SUPPORT1_SHADER_SAMPLE_MONO_TEXT = 0x800
    D3D12_FORMAT_SUPPORT1_MIP = 0x1000
    D3D12_FORMAT_SUPPORT1_RENDER_TARGET = 0x4000
    D3D12_FORMAT_SUPPORT1_BLENDABLE = 0x8000
    D3D12_FORMAT_SUPPORT1_DEPTH_STENCIL = 0x10000
    D3D12_FORMAT_SUPPORT1_MULTISAMPLE_RESOLVE = 0x40000
    D3D12_FORMAT_SUPPORT1_DISPLAY = 0x80000
    D3D12_FORMAT_SUPPORT1_CAST_WITHIN_BIT_LAYOUT = 0x100000
    D3D12_FORMAT_SUPPORT1_MULTISAMPLE_RENDERTARGET = 0x200000
    D3D12_FORMAT_SUPPORT1_MULTISAMPLE_LOAD = 0x400000
    D3D12_FORMAT_SUPPORT1_SHADER_GATHER = 0x800000
    D3D12_FORMAT_SUPPORT1_BACK_BUFFER_CAST = 0x1000000
    D3D12_FORMAT_SUPPORT1_TYPED_UNORDERED_ACCESS_VIEW = 0x2000000
    D3D12_FORMAT_SUPPORT1_SHADER_GATHER_COMPARISON = 0x4000000
    D3D12_FORMAT_SUPPORT1_DECODER_OUTPUT = 0x8000000
    D3D12_FORMAT_SUPPORT1_VIDEO_PROCESSOR_OUTPUT = 0x10000000
    D3D12_FORMAT_SUPPORT1_VIDEO_PROCESSOR_INPUT = 0x20000000
    D3D12_FORMAT_SUPPORT1_VIDEO_ENCODER = 0x40000000


class D3D12_FORMAT_SUPPORT2(ENUM):
    D3D12_FORMAT_SUPPORT2_NONE = 0
    D3D12_FORMAT_SUPPORT2_UAV_ATOMIC_ADD = 0x1
    D3D12_FORMAT_SUPPORT2_UAV_ATOMIC_BITWISE_OPS = 0x2
    D3D12_FORMAT_SUPPORT2_UAV_ATOMIC_COMPARE_STORE_OR_COMPARE_EXCHANGE = (
        0x4
    )
    D3D12_FORMAT_SUPPORT2_UAV_ATOMIC_EXCHANGE = 0x8
    D3D12_FORMAT_SUPPORT2_UAV_ATOMIC_SIGNED_MIN_OR_MAX = 0x10
    D3D12_FORMAT_SUPPORT2_UAV_ATOMIC_UNSIGNED_MIN_OR_MAX = 0x20
    D3D12_FORMAT_SUPPORT2_UAV_TYPED_LOAD = 0x40
    D3D12_FORMAT_SUPPORT2_UAV_TYPED_STORE = 0x80
    D3D12_FORMAT_SUPPORT2_OUTPUT_MERGER_LOGIC_OP = 0x100
    D3D12_FORMAT_SUPPORT2_TILED = 0x200
    D3D12_FORMAT_SUPPORT2_MULTIPLANE_OVERLAY = 0x4000


class D3D12_MULTISAMPLE_QUALITY_LEVEL_FLAGS(ENUM):
    D3D12_MULTISAMPLE_QUALITY_LEVELS_FLAG_NONE = 0
    D3D12_MULTISAMPLE_QUALITY_LEVELS_FLAG_TILED_RESOURCE = 0x1


class D3D12_CROSS_NODE_SHARING_TIER(ENUM):
    D3D12_CROSS_NODE_SHARING_TIER_NOT_SUPPORTED = 0
    D3D12_CROSS_NODE_SHARING_TIER_1_EMULATED = 1
    D3D12_CROSS_NODE_SHARING_TIER_1 = 2
    D3D12_CROSS_NODE_SHARING_TIER_2 = 3
    D3D12_CROSS_NODE_SHARING_TIER_3 = 4


class D3D12_RESOURCE_HEAP_TIER(ENUM):
    D3D12_RESOURCE_HEAP_TIER_1 = 1
    D3D12_RESOURCE_HEAP_TIER_2 = 2


class D3D12_PROGRAMMABLE_SAMPLE_POSITIONS_TIER(ENUM):
    D3D12_PROGRAMMABLE_SAMPLE_POSITIONS_TIER_NOT_SUPPORTED = 0
    D3D12_PROGRAMMABLE_SAMPLE_POSITIONS_TIER_1 = 1
    D3D12_PROGRAMMABLE_SAMPLE_POSITIONS_TIER_2 = 2


class D3D12_VIEW_INSTANCING_TIER(ENUM):
    D3D12_VIEW_INSTANCING_TIER_NOT_SUPPORTED = 0
    D3D12_VIEW_INSTANCING_TIER_1 = 1
    D3D12_VIEW_INSTANCING_TIER_2 = 2
    D3D12_VIEW_INSTANCING_TIER_3 = 3

D3D12_FEATURE_DATA_D3D12_OPTIONS._fields_ = [
    ('DoublePrecisionFloatShaderOps', BOOL),
    ('OutputMergerLogicOp', BOOL),
    ('MinPrecisionSupport', D3D12_SHADER_MIN_PRECISION_SUPPORT),
    ('TiledResourcesTier', D3D12_TILED_RESOURCES_TIER),
    ('ResourceBindingTier', D3D12_RESOURCE_BINDING_TIER),
    ('PSSpecifiedStencilRefSupported', BOOL),
    ('TypedUAVLoadAdditionalFormats', BOOL),
    ('ROVsSupported', BOOL),
    ('ConservativeRasterizationTier', D3D12_CONSERVATIVE_RASTERIZATION_TIER),
    ('MaxGPUVirtualAddressBitsPerResource', UINT),
    ('StandardSwizzle64KBSupported', BOOL),
    ('CrossNodeSharingTier', D3D12_CROSS_NODE_SHARING_TIER),
    ('CrossAdapterRowMajorTextureSupported', BOOL),
    ('VPAndRTArrayIndexFromAnyShaderFeedingRasterizerSupportedWithoutGSEmulation', BOOL),
    ('ResourceHeapTier', D3D12_RESOURCE_HEAP_TIER),
]

D3D12_FEATURE_DATA_D3D12_OPTIONS1._fields_ = [
    ('WaveOps', BOOL),
    ('WaveLaneCountMin', UINT),
    ('WaveLaneCountMax', UINT),
    ('TotalLaneCount', UINT),
    ('ExpandedComputeResourceStates', BOOL),
    ('Int64ShaderOps', BOOL),
]

D3D12_FEATURE_DATA_D3D12_OPTIONS2._fields_ = [
    ('DepthBoundsTestSupported', BOOL),
    ('ProgrammableSamplePositionsTier', D3D12_PROGRAMMABLE_SAMPLE_POSITIONS_TIER),
]


class D3D_ROOT_SIGNATURE_VERSION(ENUM):
    D3D_ROOT_SIGNATURE_VERSION_1 = 0x1
    D3D_ROOT_SIGNATURE_VERSION_1_0 = 0x1
    D3D_ROOT_SIGNATURE_VERSION_1_1 = 0x2

D3D12_FEATURE_DATA_ROOT_SIGNATURE._fields_ = [
    ('HighestVersion', D3D_ROOT_SIGNATURE_VERSION),
]

D3D12_FEATURE_DATA_ARCHITECTURE._fields_ = [
    ('NodeIndex', UINT),
    ('TileBasedRenderer', BOOL),
    ('UMA', BOOL),
    ('CacheCoherentUMA', BOOL),
]

D3D12_FEATURE_DATA_ARCHITECTURE1._fields_ = [
    ('NodeIndex', UINT),
    ('TileBasedRenderer', BOOL),
    ('UMA', BOOL),
    ('CacheCoherentUMA', BOOL),
    ('IsolatedMMU', BOOL),
]

D3D12_FEATURE_DATA_FEATURE_LEVELS._fields_ = [
    ('NumFeatureLevels', UINT),
    ('pFeatureLevelsRequested', POINTER(D3D_FEATURE_LEVEL)),
    ('MaxSupportedFeatureLevel', D3D_FEATURE_LEVEL),
]


class D3D_SHADER_MODEL(ENUM):
    D3D_SHADER_MODEL_5_1 = 0x51
    D3D_SHADER_MODEL_6_0 = 0x60
    D3D_SHADER_MODEL_6_1 = 0x61
    D3D_SHADER_MODEL_6_2 = 0x62

D3D12_FEATURE_DATA_SHADER_MODEL._fields_ = [
    ('HighestShaderModel', D3D_SHADER_MODEL),
]

D3D12_FEATURE_DATA_FORMAT_SUPPORT._fields_ = [
    ('Format', DXGI_FORMAT),
    ('Support1', D3D12_FORMAT_SUPPORT1),
    ('Support2', D3D12_FORMAT_SUPPORT2),
]

D3D12_FEATURE_DATA_MULTISAMPLE_QUALITY_LEVELS._fields_ = [
    ('Format', DXGI_FORMAT),
    ('SampleCount', UINT),
    ('Flags', D3D12_MULTISAMPLE_QUALITY_LEVEL_FLAGS),
    ('NumQualityLevels', UINT),
]

D3D12_FEATURE_DATA_FORMAT_INFO._fields_ = [
    ('Format', DXGI_FORMAT),
    ('PlaneCount', UINT8),
]

D3D12_FEATURE_DATA_GPU_VIRTUAL_ADDRESS_SUPPORT._fields_ = [
    ('MaxGPUVirtualAddressBitsPerResource', UINT),
    ('MaxGPUVirtualAddressBitsPerProcess', UINT),
]


class D3D12_SHADER_CACHE_SUPPORT_FLAGS(ENUM):
    D3D12_SHADER_CACHE_SUPPORT_NONE = 0
    D3D12_SHADER_CACHE_SUPPORT_SINGLE_PSO = 0x1
    D3D12_SHADER_CACHE_SUPPORT_LIBRARY = 0x2
    D3D12_SHADER_CACHE_SUPPORT_AUTOMATIC_INPROC_CACHE = 0x4
    D3D12_SHADER_CACHE_SUPPORT_AUTOMATIC_DISK_CACHE = 0x8

D3D12_FEATURE_DATA_SHADER_CACHE._fields_ = [
    ('SupportFlags', D3D12_SHADER_CACHE_SUPPORT_FLAGS),
]

D3D12_FEATURE_DATA_COMMAND_QUEUE_PRIORITY._fields_ = [
    ('CommandListType', D3D12_COMMAND_LIST_TYPE),
    ('Priority', UINT),
    ('PriorityForTypeIsSupported', BOOL),
]


class D3D12_COMMAND_LIST_SUPPORT_FLAGS(ENUM):
    D3D12_COMMAND_LIST_SUPPORT_FLAG_NONE = 0
    D3D12_COMMAND_LIST_SUPPORT_FLAG_DIRECT = (
        1 << D3D12_COMMAND_LIST_TYPE.D3D12_COMMAND_LIST_TYPE_DIRECT
    )
    D3D12_COMMAND_LIST_SUPPORT_FLAG_BUNDLE = (
        1 << D3D12_COMMAND_LIST_TYPE.D3D12_COMMAND_LIST_TYPE_BUNDLE
    )
    D3D12_COMMAND_LIST_SUPPORT_FLAG_COMPUTE = (
        1 << D3D12_COMMAND_LIST_TYPE.D3D12_COMMAND_LIST_TYPE_COMPUTE
    )
    D3D12_COMMAND_LIST_SUPPORT_FLAG_COPY = (
        1 << D3D12_COMMAND_LIST_TYPE.D3D12_COMMAND_LIST_TYPE_COPY
    )
    D3D12_COMMAND_LIST_SUPPORT_FLAG_VIDEO_DECODE = (
        1 << D3D12_COMMAND_LIST_TYPE.D3D12_COMMAND_LIST_TYPE_VIDEO_DECODE
    )
    D3D12_COMMAND_LIST_SUPPORT_FLAG_VIDEO_PROCESS = (
        1 << D3D12_COMMAND_LIST_TYPE.D3D12_COMMAND_LIST_TYPE_VIDEO_PROCESS
    )

D3D12_FEATURE_DATA_D3D12_OPTIONS3._fields_ = [
    ('CopyQueueTimestampQueriesSupported', BOOL),
    ('CastingFullyTypedFormatSupported', BOOL),
    ('WriteBufferImmediateSupportFlags', D3D12_COMMAND_LIST_SUPPORT_FLAGS),
    ('ViewInstancingTier', D3D12_VIEW_INSTANCING_TIER),
    ('BarycentricsSupported', BOOL),
]

D3D12_FEATURE_DATA_EXISTING_HEAPS._fields_ = [
    ('Supported', BOOL),
]


class D3D12_SHARED_RESOURCE_COMPATIBILITY_TIER(ENUM):
    D3D12_SHARED_RESOURCE_COMPATIBILITY_TIER_0 = 0
    D3D12_SHARED_RESOURCE_COMPATIBILITY_TIER_1 = (
        D3D12_SHARED_RESOURCE_COMPATIBILITY_TIER_0 + 1
    )

D3D12_FEATURE_DATA_D3D12_OPTIONS4._fields_ = [
    ('MSAA64KBAlignedTextureSupported', BOOL),
    ('SharedResourceCompatibilityTier', D3D12_SHARED_RESOURCE_COMPATIBILITY_TIER),
    ('Native16BitShaderOpsSupported', BOOL),
]


class D3D12_HEAP_SERIALIZATION_TIER(ENUM):
    D3D12_HEAP_SERIALIZATION_TIER_0 = 0
    D3D12_HEAP_SERIALIZATION_TIER_10 = 10

D3D12_FEATURE_DATA_SERIALIZATION._fields_ = [
    ('NodeIndex', UINT),
    ('HeapSerializationTier', D3D12_HEAP_SERIALIZATION_TIER),
]

D3D12_FEATURE_DATA_CROSS_NODE._fields_ = [
    ('SharingTier', D3D12_CROSS_NODE_SHARING_TIER),
    ('AtomicShaderInstructions', BOOL),
]

D3D12_RESOURCE_ALLOCATION_INFO._fields_ = [
    ('SizeInBytes', UINT64),
    ('Alignment', UINT64),
]

D3D12_RESOURCE_ALLOCATION_INFO1._fields_ = [
    ('Offset', UINT64),
    ('Alignment', UINT64),
    ('SizeInBytes', UINT64),
]


class D3D12_HEAP_TYPE(ENUM):
    D3D12_HEAP_TYPE_DEFAULT = 1
    D3D12_HEAP_TYPE_UPLOAD = 2
    D3D12_HEAP_TYPE_READBACK = 3
    D3D12_HEAP_TYPE_CUSTOM = 4


class D3D12_CPU_PAGE_PROPERTY(ENUM):
    D3D12_CPU_PAGE_PROPERTY_UNKNOWN = 0
    D3D12_CPU_PAGE_PROPERTY_NOT_AVAILABLE = 1
    D3D12_CPU_PAGE_PROPERTY_WRITE_COMBINE = 2
    D3D12_CPU_PAGE_PROPERTY_WRITE_BACK = 3


class D3D12_MEMORY_POOL(ENUM):
    D3D12_MEMORY_POOL_UNKNOWN = 0
    D3D12_MEMORY_POOL_L0 = 1
    D3D12_MEMORY_POOL_L1 = 2

D3D12_HEAP_PROPERTIES._fields_ = [
    ('Type', D3D12_HEAP_TYPE),
    ('CPUPageProperty', D3D12_CPU_PAGE_PROPERTY),
    ('MemoryPoolPreference', D3D12_MEMORY_POOL),
    ('CreationNodeMask', UINT),
    ('VisibleNodeMask', UINT),
]


class D3D12_HEAP_FLAGS(ENUM):
    D3D12_HEAP_FLAG_NONE = 0
    D3D12_HEAP_FLAG_SHARED = 0x1
    D3D12_HEAP_FLAG_DENY_BUFFERS = 0x4
    D3D12_HEAP_FLAG_ALLOW_DISPLAY = 0x8
    D3D12_HEAP_FLAG_SHARED_CROSS_ADAPTER = 0x20
    D3D12_HEAP_FLAG_DENY_RT_DS_TEXTURES = 0x40
    D3D12_HEAP_FLAG_DENY_NON_RT_DS_TEXTURES = 0x80
    D3D12_HEAP_FLAG_HARDWARE_PROTECTED = 0x100
    D3D12_HEAP_FLAG_ALLOW_WRITE_WATCH = 0x200
    D3D12_HEAP_FLAG_ALLOW_SHADER_ATOMICS = 0x400
    D3D12_HEAP_FLAG_ALLOW_ALL_BUFFERS_AND_TEXTURES = 0
    D3D12_HEAP_FLAG_ALLOW_ONLY_BUFFERS = 0xC0
    D3D12_HEAP_FLAG_ALLOW_ONLY_NON_RT_DS_TEXTURES = 0x44
    D3D12_HEAP_FLAG_ALLOW_ONLY_RT_DS_TEXTURES = 0x84

D3D12_HEAP_DESC._fields_ = [
    ('SizeInBytes', UINT64),
    ('Properties', D3D12_HEAP_PROPERTIES),
    ('Alignment', UINT64),
    ('Flags', D3D12_HEAP_FLAGS),
]


class D3D12_RESOURCE_DIMENSION(ENUM):
    D3D12_RESOURCE_DIMENSION_UNKNOWN = 0
    D3D12_RESOURCE_DIMENSION_BUFFER = 1
    D3D12_RESOURCE_DIMENSION_TEXTURE1D = 2
    D3D12_RESOURCE_DIMENSION_TEXTURE2D = 3
    D3D12_RESOURCE_DIMENSION_TEXTURE3D = 4


class D3D12_TEXTURE_LAYOUT(ENUM):
    D3D12_TEXTURE_LAYOUT_UNKNOWN = 0
    D3D12_TEXTURE_LAYOUT_ROW_MAJOR = 1
    D3D12_TEXTURE_LAYOUT_64KB_UNDEFINED_SWIZZLE = 2
    D3D12_TEXTURE_LAYOUT_64KB_STANDARD_SWIZZLE = 3


class D3D12_RESOURCE_FLAGS(ENUM):
    D3D12_RESOURCE_FLAG_NONE = 0
    D3D12_RESOURCE_FLAG_ALLOW_RENDER_TARGET = 0x1
    D3D12_RESOURCE_FLAG_ALLOW_DEPTH_STENCIL = 0x2
    D3D12_RESOURCE_FLAG_ALLOW_UNORDERED_ACCESS = 0x4
    D3D12_RESOURCE_FLAG_DENY_SHADER_RESOURCE = 0x8
    D3D12_RESOURCE_FLAG_ALLOW_CROSS_ADAPTER = 0x10
    D3D12_RESOURCE_FLAG_ALLOW_SIMULTANEOUS_ACCESS = 0x20
    D3D12_RESOURCE_FLAG_VIDEO_DECODE_REFERENCE_ONLY = 0x40

D3D12_RESOURCE_DESC._fields_ = [
    ('Dimension', D3D12_RESOURCE_DIMENSION),
    ('Alignment', UINT64),
    ('Width', UINT64),
    ('Height', UINT),
    ('DepthOrArraySize', UINT16),
    ('MipLevels', UINT16),
    ('Format', DXGI_FORMAT),
    ('SampleDesc', DXGI_SAMPLE_DESC),
    ('Layout', D3D12_TEXTURE_LAYOUT),
    ('Flags', D3D12_RESOURCE_FLAGS),
]

D3D12_DEPTH_STENCIL_VALUE._fields_ = [
    ('Depth', FLOAT),
    ('Stencil', UINT8),
]


class _Union_1(ctypes.Union):
    pass


_Union_1._fields_ = [
    ('Color', FLOAT * 4),
    ('DepthStencil', D3D12_DEPTH_STENCIL_VALUE),
]
D3D12_CLEAR_VALUE._Union_1 = _Union_1

D3D12_CLEAR_VALUE._anonymous_ = (
    '_Union_1',
)

D3D12_CLEAR_VALUE._fields_ = [
    ('Format', DXGI_FORMAT),
    ('_Union_1', D3D12_CLEAR_VALUE._Union_1),
]

D3D12_RANGE._fields_ = [
    ('Begin', SIZE_T),
    ('End', SIZE_T),
]

D3D12_RANGE_UINT64._fields_ = [
    ('Begin', UINT64),
    ('End', UINT64),
]

D3D12_SUBRESOURCE_RANGE_UINT64._fields_ = [
    ('Subresource', UINT),
    ('Range', D3D12_RANGE_UINT64),
]

D3D12_SUBRESOURCE_INFO._fields_ = [
    ('Offset', UINT64),
    ('RowPitch', UINT),
    ('DepthPitch', UINT),
]

D3D12_TILED_RESOURCE_COORDINATE._fields_ = [
    ('X', UINT),
    ('Y', UINT),
    ('Z', UINT),
    ('Subresource', UINT),
]

D3D12_TILE_REGION_SIZE._fields_ = [
    ('NumTiles', UINT),
    ('UseBox', BOOL),
    ('Width', UINT),
    ('Height', UINT16),
    ('Depth', UINT16),
]


class D3D12_TILE_RANGE_FLAGS(ENUM):
    D3D12_TILE_RANGE_FLAG_NONE = 0
    D3D12_TILE_RANGE_FLAG_NULL = 1
    D3D12_TILE_RANGE_FLAG_SKIP = 2
    D3D12_TILE_RANGE_FLAG_REUSE_SINGLE_TILE = 4

D3D12_SUBRESOURCE_TILING._fields_ = [
    ('WidthInTiles', UINT),
    ('HeightInTiles', UINT16),
    ('DepthInTiles', UINT16),
    ('StartTileIndexInOverallResource', UINT),
]

D3D12_TILE_SHAPE._fields_ = [
    ('WidthInTexels', UINT),
    ('HeightInTexels', UINT),
    ('DepthInTexels', UINT),
]

D3D12_PACKED_MIP_INFO._fields_ = [
    ('NumStandardMips', UINT8),
    ('NumPackedMips', UINT8),
    ('NumTilesForPackedMips', UINT),
    ('StartTileIndexInOverallResource', UINT),
]


class D3D12_TILE_MAPPING_FLAGS(ENUM):
    D3D12_TILE_MAPPING_FLAG_NONE = 0
    D3D12_TILE_MAPPING_FLAG_NO_HAZARD = 0x1


class D3D12_TILE_COPY_FLAGS(ENUM):
    D3D12_TILE_COPY_FLAG_NONE = 0
    D3D12_TILE_COPY_FLAG_NO_HAZARD = 0x1
    D3D12_TILE_COPY_FLAG_LINEAR_BUFFER_TO_SWIZZLED_TILED_RESOURCE = 0x2
    D3D12_TILE_COPY_FLAG_SWIZZLED_TILED_RESOURCE_TO_LINEAR_BUFFER = 0x4


class D3D12_RESOURCE_STATES(ENUM):
    D3D12_RESOURCE_STATE_COMMON = 0
    D3D12_RESOURCE_STATE_VERTEX_AND_CONSTANT_BUFFER = 0x1
    D3D12_RESOURCE_STATE_INDEX_BUFFER = 0x2
    D3D12_RESOURCE_STATE_RENDER_TARGET = 0x4
    D3D12_RESOURCE_STATE_UNORDERED_ACCESS = 0x8
    D3D12_RESOURCE_STATE_DEPTH_WRITE = 0x10
    D3D12_RESOURCE_STATE_DEPTH_READ = 0x20
    D3D12_RESOURCE_STATE_NON_PIXEL_SHADER_RESOURCE = 0x40
    D3D12_RESOURCE_STATE_PIXEL_SHADER_RESOURCE = 0x80
    D3D12_RESOURCE_STATE_STREAM_OUT = 0x100
    D3D12_RESOURCE_STATE_INDIRECT_ARGUMENT = 0x200
    D3D12_RESOURCE_STATE_COPY_DEST = 0x400
    D3D12_RESOURCE_STATE_COPY_SOURCE = 0x800
    D3D12_RESOURCE_STATE_RESOLVE_DEST = 0x1000
    D3D12_RESOURCE_STATE_RESOLVE_SOURCE = 0x2000
    D3D12_RESOURCE_STATE_GENERIC_READ = (
        0x1 |
        0x2  |
        0x40 |
        0x80 |
        0x200 |
        0x800
    )
    D3D12_RESOURCE_STATE_PRESENT = 0
    D3D12_RESOURCE_STATE_PREDICATION = 0x200
    D3D12_RESOURCE_STATE_VIDEO_DECODE_READ = 0x10000
    D3D12_RESOURCE_STATE_VIDEO_DECODE_WRITE = 0x20000
    D3D12_RESOURCE_STATE_VIDEO_PROCESS_READ = 0x40000
    D3D12_RESOURCE_STATE_VIDEO_PROCESS_WRITE = 0x80000


class D3D12_RESOURCE_BARRIER_TYPE(ENUM):
    D3D12_RESOURCE_BARRIER_TYPE_TRANSITION = 0
    D3D12_RESOURCE_BARRIER_TYPE_ALIASING = (
        D3D12_RESOURCE_BARRIER_TYPE_TRANSITION + 1
    )
    D3D12_RESOURCE_BARRIER_TYPE_UAV = (
        D3D12_RESOURCE_BARRIER_TYPE_ALIASING + 1
    )

D3D12_RESOURCE_TRANSITION_BARRIER._fields_ = [
    ('pResource', POINTER(ID3D12Resource)),
    ('Subresource', UINT),
    ('StateBefore', D3D12_RESOURCE_STATES),
    ('StateAfter', D3D12_RESOURCE_STATES),
]

D3D12_RESOURCE_ALIASING_BARRIER._fields_ = [
    ('pResourceBefore', POINTER(ID3D12Resource)),
    ('pResourceAfter', POINTER(ID3D12Resource)),
]

D3D12_RESOURCE_UAV_BARRIER._fields_ = [
    ('pResource', POINTER(ID3D12Resource)),
]


class D3D12_RESOURCE_BARRIER_FLAGS(ENUM):
    D3D12_RESOURCE_BARRIER_FLAG_NONE = 0
    D3D12_RESOURCE_BARRIER_FLAG_BEGIN_ONLY = 0x1
    D3D12_RESOURCE_BARRIER_FLAG_END_ONLY = 0x2


class _Union_2(ctypes.Union):
    pass


_Union_2._fields_ = [
    ('Transition', D3D12_RESOURCE_TRANSITION_BARRIER),
    ('Aliasing', D3D12_RESOURCE_ALIASING_BARRIER),
    ('UAV', D3D12_RESOURCE_UAV_BARRIER),
]
D3D12_RESOURCE_BARRIER._Union_2 = _Union_2

D3D12_RESOURCE_BARRIER._anonymous_ = (
    '_Union_2',
)

D3D12_RESOURCE_BARRIER._fields_ = [
    ('Type', D3D12_RESOURCE_BARRIER_TYPE),
    ('Flags', D3D12_RESOURCE_BARRIER_FLAGS),
    ('_Union_2', D3D12_RESOURCE_BARRIER._Union_2),
]

D3D12_SUBRESOURCE_FOOTPRINT._fields_ = [
    ('Format', DXGI_FORMAT),
    ('Width', UINT),
    ('Height', UINT),
    ('Depth', UINT),
    ('RowPitch', UINT),
]

D3D12_PLACED_SUBRESOURCE_FOOTPRINT._fields_ = [
    ('Offset', UINT64),
    ('Footprint', D3D12_SUBRESOURCE_FOOTPRINT),
]


class D3D12_TEXTURE_COPY_TYPE(ENUM):
    D3D12_TEXTURE_COPY_TYPE_SUBRESOURCE_INDEX = 0
    D3D12_TEXTURE_COPY_TYPE_PLACED_FOOTPRINT = 1


class _Union_3(ctypes.Union):
    pass


_Union_3._fields_ = [
    ('PlacedFootprint', D3D12_PLACED_SUBRESOURCE_FOOTPRINT),
    ('SubresourceIndex', UINT),
]
D3D12_TEXTURE_COPY_LOCATION._Union_3 = _Union_3

D3D12_TEXTURE_COPY_LOCATION._anonymous_ = (
    '_Union_3',
)

D3D12_TEXTURE_COPY_LOCATION._fields_ = [
    ('pResource', POINTER(ID3D12Resource)),
    ('Type', D3D12_TEXTURE_COPY_TYPE),
    ('_Union_3', D3D12_TEXTURE_COPY_LOCATION._Union_3),
]


class D3D12_RESOLVE_MODE(ENUM):
    D3D12_RESOLVE_MODE_DECOMPRESS = 0
    D3D12_RESOLVE_MODE_MIN = 1
    D3D12_RESOLVE_MODE_MAX = 2
    D3D12_RESOLVE_MODE_AVERAGE = 3

D3D12_SAMPLE_POSITION._fields_ = [
    ('X', INT8),
    ('Y', INT8),
]

D3D12_VIEW_INSTANCE_LOCATION._fields_ = [
    ('ViewportArrayIndex', UINT),
    ('RenderTargetArrayIndex', UINT),
]


class D3D12_VIEW_INSTANCING_FLAGS(ENUM):
    D3D12_VIEW_INSTANCING_FLAG_NONE = 0
    D3D12_VIEW_INSTANCING_FLAG_ENABLE_VIEW_INSTANCE_MASKING = 0x1

D3D12_VIEW_INSTANCING_DESC._fields_ = [
    ('ViewInstanceCount', UINT),
    ('pViewInstanceLocations', POINTER(D3D12_VIEW_INSTANCE_LOCATION)),
    ('Flags', D3D12_VIEW_INSTANCING_FLAGS),
]


class D3D12_SHADER_COMPONENT_MAPPING(ENUM):
    D3D12_SHADER_COMPONENT_MAPPING_FROM_MEMORY_COMPONENT_0 = 0
    D3D12_SHADER_COMPONENT_MAPPING_FROM_MEMORY_COMPONENT_1 = 1
    D3D12_SHADER_COMPONENT_MAPPING_FROM_MEMORY_COMPONENT_2 = 2
    D3D12_SHADER_COMPONENT_MAPPING_FROM_MEMORY_COMPONENT_3 = 3
    D3D12_SHADER_COMPONENT_MAPPING_FORCE_VALUE_0 = 4
    D3D12_SHADER_COMPONENT_MAPPING_FORCE_VALUE_1 = 5


class D3D12_BUFFER_SRV_FLAGS(ENUM):
    D3D12_BUFFER_SRV_FLAG_NONE = 0
    D3D12_BUFFER_SRV_FLAG_RAW = 0x1

D3D12_BUFFER_SRV._fields_ = [
    ('FirstElement', UINT64),
    ('NumElements', UINT),
    ('StructureByteStride', UINT),
    ('Flags', D3D12_BUFFER_SRV_FLAGS),
]

D3D12_TEX1D_SRV._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
    ('ResourceMinLODClamp', FLOAT),
]

D3D12_TEX1D_ARRAY_SRV._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
    ('ResourceMinLODClamp', FLOAT),
]

D3D12_TEX2D_SRV._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
    ('PlaneSlice', UINT),
    ('ResourceMinLODClamp', FLOAT),
]

D3D12_TEX2D_ARRAY_SRV._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
    ('PlaneSlice', UINT),
    ('ResourceMinLODClamp', FLOAT),
]

D3D12_TEX3D_SRV._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
    ('ResourceMinLODClamp', FLOAT),
]

D3D12_TEXCUBE_SRV._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
    ('ResourceMinLODClamp', FLOAT),
]

D3D12_TEXCUBE_ARRAY_SRV._fields_ = [
    ('MostDetailedMip', UINT),
    ('MipLevels', UINT),
    ('First2DArrayFace', UINT),
    ('NumCubes', UINT),
    ('ResourceMinLODClamp', FLOAT),
]

D3D12_TEX2DMS_SRV._fields_ = [
    ('UnusedField_NothingToDefine', UINT),
]

D3D12_TEX2DMS_ARRAY_SRV._fields_ = [
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]


class D3D12_SRV_DIMENSION(ENUM):
    D3D12_SRV_DIMENSION_UNKNOWN = 0
    D3D12_SRV_DIMENSION_BUFFER = 1
    D3D12_SRV_DIMENSION_TEXTURE1D = 2
    D3D12_SRV_DIMENSION_TEXTURE1DARRAY = 3
    D3D12_SRV_DIMENSION_TEXTURE2D = 4
    D3D12_SRV_DIMENSION_TEXTURE2DARRAY = 5
    D3D12_SRV_DIMENSION_TEXTURE2DMS = 6
    D3D12_SRV_DIMENSION_TEXTURE2DMSARRAY = 7
    D3D12_SRV_DIMENSION_TEXTURE3D = 8
    D3D12_SRV_DIMENSION_TEXTURECUBE = 9
    D3D12_SRV_DIMENSION_TEXTURECUBEARRAY = 10


class _Union_4(ctypes.Union):
    pass


_Union_4._fields_ = [
    ('Buffer', D3D12_BUFFER_SRV),
    ('Texture1D', D3D12_TEX1D_SRV),
    ('Texture1DArray', D3D12_TEX1D_ARRAY_SRV),
    ('Texture2D', D3D12_TEX2D_SRV),
    ('Texture2DArray', D3D12_TEX2D_ARRAY_SRV),
    ('Texture2DMS', D3D12_TEX2DMS_SRV),
    ('Texture2DMSArray', D3D12_TEX2DMS_ARRAY_SRV),
    ('Texture3D', D3D12_TEX3D_SRV),
    ('TextureCube', D3D12_TEXCUBE_SRV),
    ('TextureCubeArray', D3D12_TEXCUBE_ARRAY_SRV),
]
D3D12_SHADER_RESOURCE_VIEW_DESC._Union_4 = _Union_4

D3D12_SHADER_RESOURCE_VIEW_DESC._anonymous_ = (
    '_Union_4',
)

D3D12_SHADER_RESOURCE_VIEW_DESC._fields_ = [
    ('Format', DXGI_FORMAT),
    ('ViewDimension', D3D12_SRV_DIMENSION),
    ('Shader4ComponentMapping', UINT),
    ('_Union_4', D3D12_SHADER_RESOURCE_VIEW_DESC._Union_4),
]

D3D12_CONSTANT_BUFFER_VIEW_DESC._fields_ = [
    ('BufferLocation', D3D12_GPU_VIRTUAL_ADDRESS),
    ('SizeInBytes', UINT),
]


class D3D12_FILTER(ENUM):
    D3D12_FILTER_MIN_MAG_MIP_POINT = 0
    D3D12_FILTER_MIN_MAG_POINT_MIP_LINEAR = 0x1
    D3D12_FILTER_MIN_POINT_MAG_LINEAR_MIP_POINT = 0x4
    D3D12_FILTER_MIN_POINT_MAG_MIP_LINEAR = 0x5
    D3D12_FILTER_MIN_LINEAR_MAG_MIP_POINT = 0x10
    D3D12_FILTER_MIN_LINEAR_MAG_POINT_MIP_LINEAR = 0x11
    D3D12_FILTER_MIN_MAG_LINEAR_MIP_POINT = 0x14
    D3D12_FILTER_MIN_MAG_MIP_LINEAR = 0x15
    D3D12_FILTER_ANISOTROPIC = 0x55
    D3D12_FILTER_COMPARISON_MIN_MAG_MIP_POINT = 0x80
    D3D12_FILTER_COMPARISON_MIN_MAG_POINT_MIP_LINEAR = 0x81
    D3D12_FILTER_COMPARISON_MIN_POINT_MAG_LINEAR_MIP_POINT = 0x84
    D3D12_FILTER_COMPARISON_MIN_POINT_MAG_MIP_LINEAR = 0x85
    D3D12_FILTER_COMPARISON_MIN_LINEAR_MAG_MIP_POINT = 0x90
    D3D12_FILTER_COMPARISON_MIN_LINEAR_MAG_POINT_MIP_LINEAR = 0x91
    D3D12_FILTER_COMPARISON_MIN_MAG_LINEAR_MIP_POINT = 0x94
    D3D12_FILTER_COMPARISON_MIN_MAG_MIP_LINEAR = 0x95
    D3D12_FILTER_COMPARISON_ANISOTROPIC = 0xD5
    D3D12_FILTER_MINIMUM_MIN_MAG_MIP_POINT = 0x100
    D3D12_FILTER_MINIMUM_MIN_MAG_POINT_MIP_LINEAR = 0x101
    D3D12_FILTER_MINIMUM_MIN_POINT_MAG_LINEAR_MIP_POINT = 0x104
    D3D12_FILTER_MINIMUM_MIN_POINT_MAG_MIP_LINEAR = 0x105
    D3D12_FILTER_MINIMUM_MIN_LINEAR_MAG_MIP_POINT = 0x110
    D3D12_FILTER_MINIMUM_MIN_LINEAR_MAG_POINT_MIP_LINEAR = 0x111
    D3D12_FILTER_MINIMUM_MIN_MAG_LINEAR_MIP_POINT = 0x114
    D3D12_FILTER_MINIMUM_MIN_MAG_MIP_LINEAR = 0x115
    D3D12_FILTER_MINIMUM_ANISOTROPIC = 0x155
    D3D12_FILTER_MAXIMUM_MIN_MAG_MIP_POINT = 0x180
    D3D12_FILTER_MAXIMUM_MIN_MAG_POINT_MIP_LINEAR = 0x181
    D3D12_FILTER_MAXIMUM_MIN_POINT_MAG_LINEAR_MIP_POINT = 0x184
    D3D12_FILTER_MAXIMUM_MIN_POINT_MAG_MIP_LINEAR = 0x185
    D3D12_FILTER_MAXIMUM_MIN_LINEAR_MAG_MIP_POINT = 0x190
    D3D12_FILTER_MAXIMUM_MIN_LINEAR_MAG_POINT_MIP_LINEAR = 0x191
    D3D12_FILTER_MAXIMUM_MIN_MAG_LINEAR_MIP_POINT = 0x194
    D3D12_FILTER_MAXIMUM_MIN_MAG_MIP_LINEAR = 0x195
    D3D12_FILTER_MAXIMUM_ANISOTROPIC = 0x1D5


class D3D12_FILTER_TYPE(ENUM):
    D3D12_FILTER_TYPE_POINT = 0
    D3D12_FILTER_TYPE_LINEAR = 1


class D3D12_FILTER_REDUCTION_TYPE(ENUM):
    D3D12_FILTER_REDUCTION_TYPE_STANDARD = 0
    D3D12_FILTER_REDUCTION_TYPE_COMPARISON = 1
    D3D12_FILTER_REDUCTION_TYPE_MINIMUM = 2
    D3D12_FILTER_REDUCTION_TYPE_MAXIMUM = 3


class D3D12_TEXTURE_ADDRESS_MODE(ENUM):
    D3D12_TEXTURE_ADDRESS_MODE_WRAP = 1
    D3D12_TEXTURE_ADDRESS_MODE_MIRROR = 2
    D3D12_TEXTURE_ADDRESS_MODE_CLAMP = 3
    D3D12_TEXTURE_ADDRESS_MODE_BORDER = 4
    D3D12_TEXTURE_ADDRESS_MODE_MIRROR_ONCE = 5

D3D12_SAMPLER_DESC._fields_ = [
    ('Filter', D3D12_FILTER),
    ('AddressU', D3D12_TEXTURE_ADDRESS_MODE),
    ('AddressV', D3D12_TEXTURE_ADDRESS_MODE),
    ('AddressW', D3D12_TEXTURE_ADDRESS_MODE),
    ('MipLODBias', FLOAT),
    ('MaxAnisotropy', UINT),
    ('ComparisonFunc', D3D12_COMPARISON_FUNC),
    ('BorderColor', FLOAT * 4),
    ('MinLOD', FLOAT),
    ('MaxLOD', FLOAT),
]


class D3D12_BUFFER_UAV_FLAGS(ENUM):
    D3D12_BUFFER_UAV_FLAG_NONE = 0
    D3D12_BUFFER_UAV_FLAG_RAW = 0x1

D3D12_BUFFER_UAV._fields_ = [
    ('FirstElement', UINT64),
    ('NumElements', UINT),
    ('StructureByteStride', UINT),
    ('CounterOffsetInBytes', UINT64),
    ('Flags', D3D12_BUFFER_UAV_FLAGS),
]

D3D12_TEX1D_UAV._fields_ = [
    ('MipSlice', UINT),
]

D3D12_TEX1D_ARRAY_UAV._fields_ = [
    ('MipSlice', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]

D3D12_TEX2D_UAV._fields_ = [
    ('MipSlice', UINT),
    ('PlaneSlice', UINT),
]

D3D12_TEX2D_ARRAY_UAV._fields_ = [
    ('MipSlice', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
    ('PlaneSlice', UINT),
]

D3D12_TEX3D_UAV._fields_ = [
    ('MipSlice', UINT),
    ('FirstWSlice', UINT),
    ('WSize', UINT),
]


class D3D12_UAV_DIMENSION(ENUM):
    D3D12_UAV_DIMENSION_UNKNOWN = 0
    D3D12_UAV_DIMENSION_BUFFER = 1
    D3D12_UAV_DIMENSION_TEXTURE1D = 2
    D3D12_UAV_DIMENSION_TEXTURE1DARRAY = 3
    D3D12_UAV_DIMENSION_TEXTURE2D = 4
    D3D12_UAV_DIMENSION_TEXTURE2DARRAY = 5
    D3D12_UAV_DIMENSION_TEXTURE3D = 8


class _Union_5(ctypes.Union):
    pass


_Union_5._fields_ = [
    ('Buffer', D3D12_BUFFER_UAV),
    ('Texture1D', D3D12_TEX1D_UAV),
    ('Texture1DArray', D3D12_TEX1D_ARRAY_UAV),
    ('Texture2D', D3D12_TEX2D_UAV),
    ('Texture2DArray', D3D12_TEX2D_ARRAY_UAV),
    ('Texture3D', D3D12_TEX3D_UAV),
]
D3D12_UNORDERED_ACCESS_VIEW_DESC._Union_5 = _Union_5

D3D12_UNORDERED_ACCESS_VIEW_DESC._anonymous_ = (
    '_Union_5',
)

D3D12_UNORDERED_ACCESS_VIEW_DESC._fields_ = [
    ('Format', DXGI_FORMAT),
    ('ViewDimension', D3D12_UAV_DIMENSION),
    ('_Union_5', D3D12_UNORDERED_ACCESS_VIEW_DESC._Union_5),
]

D3D12_BUFFER_RTV._fields_ = [
    ('FirstElement', UINT64),
    ('NumElements', UINT),
]

D3D12_TEX1D_RTV._fields_ = [
    ('MipSlice', UINT),
]

D3D12_TEX1D_ARRAY_RTV._fields_ = [
    ('MipSlice', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]

D3D12_TEX2D_RTV._fields_ = [
    ('MipSlice', UINT),
    ('PlaneSlice', UINT),
]

D3D12_TEX2DMS_RTV._fields_ = [
    ('UnusedField_NothingToDefine', UINT),
]

D3D12_TEX2D_ARRAY_RTV._fields_ = [
    ('MipSlice', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
    ('PlaneSlice', UINT),
]

D3D12_TEX2DMS_ARRAY_RTV._fields_ = [
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]

D3D12_TEX3D_RTV._fields_ = [
    ('MipSlice', UINT),
    ('FirstWSlice', UINT),
    ('WSize', UINT),
]


class D3D12_RTV_DIMENSION(ENUM):
    D3D12_RTV_DIMENSION_UNKNOWN = 0
    D3D12_RTV_DIMENSION_BUFFER = 1
    D3D12_RTV_DIMENSION_TEXTURE1D = 2
    D3D12_RTV_DIMENSION_TEXTURE1DARRAY = 3
    D3D12_RTV_DIMENSION_TEXTURE2D = 4
    D3D12_RTV_DIMENSION_TEXTURE2DARRAY = 5
    D3D12_RTV_DIMENSION_TEXTURE2DMS = 6
    D3D12_RTV_DIMENSION_TEXTURE2DMSARRAY = 7
    D3D12_RTV_DIMENSION_TEXTURE3D = 8


class _Union_6(ctypes.Union):
    pass


_Union_6._fields_ = [
    ('Buffer', D3D12_BUFFER_RTV),
    ('Texture1D', D3D12_TEX1D_RTV),
    ('Texture1DArray', D3D12_TEX1D_ARRAY_RTV),
    ('Texture2D', D3D12_TEX2D_RTV),
    ('Texture2DArray', D3D12_TEX2D_ARRAY_RTV),
    ('Texture2DMS', D3D12_TEX2DMS_RTV),
    ('Texture2DMSArray', D3D12_TEX2DMS_ARRAY_RTV),
    ('Texture3D', D3D12_TEX3D_RTV),
]
D3D12_RENDER_TARGET_VIEW_DESC._Union_6 = _Union_6

D3D12_RENDER_TARGET_VIEW_DESC._anonymous_ = (
    '_Union_6',
)

D3D12_RENDER_TARGET_VIEW_DESC._fields_ = [
    ('Format', DXGI_FORMAT),
    ('ViewDimension', D3D12_RTV_DIMENSION),
    ('_Union_6', D3D12_RENDER_TARGET_VIEW_DESC._Union_6),
]

D3D12_TEX1D_DSV._fields_ = [
    ('MipSlice', UINT),
]

D3D12_TEX1D_ARRAY_DSV._fields_ = [
    ('MipSlice', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]

D3D12_TEX2D_DSV._fields_ = [
    ('MipSlice', UINT),
]

D3D12_TEX2D_ARRAY_DSV._fields_ = [
    ('MipSlice', UINT),
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]

D3D12_TEX2DMS_DSV._fields_ = [
    ('UnusedField_NothingToDefine', UINT),
]

D3D12_TEX2DMS_ARRAY_DSV._fields_ = [
    ('FirstArraySlice', UINT),
    ('ArraySize', UINT),
]


class D3D12_DSV_FLAGS(ENUM):
    D3D12_DSV_FLAG_NONE = 0
    D3D12_DSV_FLAG_READ_ONLY_DEPTH = 0x1
    D3D12_DSV_FLAG_READ_ONLY_STENCIL = 0x2


class D3D12_DSV_DIMENSION(ENUM):
    D3D12_DSV_DIMENSION_UNKNOWN = 0
    D3D12_DSV_DIMENSION_TEXTURE1D = 1
    D3D12_DSV_DIMENSION_TEXTURE1DARRAY = 2
    D3D12_DSV_DIMENSION_TEXTURE2D = 3
    D3D12_DSV_DIMENSION_TEXTURE2DARRAY = 4
    D3D12_DSV_DIMENSION_TEXTURE2DMS = 5
    D3D12_DSV_DIMENSION_TEXTURE2DMSARRAY = 6


class _Union_7(ctypes.Union):
    pass


_Union_7._fields_ = [
    ('Texture1D', D3D12_TEX1D_DSV),
    ('Texture1DArray', D3D12_TEX1D_ARRAY_DSV),
    ('Texture2D', D3D12_TEX2D_DSV),
    ('Texture2DArray', D3D12_TEX2D_ARRAY_DSV),
    ('Texture2DMS', D3D12_TEX2DMS_DSV),
    ('Texture2DMSArray', D3D12_TEX2DMS_ARRAY_DSV),
]
D3D12_DEPTH_STENCIL_VIEW_DESC._Union_7 = _Union_7

D3D12_DEPTH_STENCIL_VIEW_DESC._anonymous_ = (
    '_Union_7',
)

D3D12_DEPTH_STENCIL_VIEW_DESC._fields_ = [
    ('Format', DXGI_FORMAT),
    ('ViewDimension', D3D12_DSV_DIMENSION),
    ('Flags', D3D12_DSV_FLAGS),
    ('_Union_7', D3D12_DEPTH_STENCIL_VIEW_DESC._Union_7),
]


class D3D12_CLEAR_FLAGS(ENUM):
    D3D12_CLEAR_FLAG_DEPTH = 0x1
    D3D12_CLEAR_FLAG_STENCIL = 0x2


class D3D12_FENCE_FLAGS(ENUM):
    D3D12_FENCE_FLAG_NONE = 0
    D3D12_FENCE_FLAG_SHARED = 0x1
    D3D12_FENCE_FLAG_SHARED_CROSS_ADAPTER = 0x2
    D3D12_FENCE_FLAG_NON_MONITORED = 0x4


class D3D12_DESCRIPTOR_HEAP_TYPE(ENUM):
    D3D12_DESCRIPTOR_HEAP_TYPE_CBV_SRV_UAV = 0
    D3D12_DESCRIPTOR_HEAP_TYPE_SAMPLER = (
        D3D12_DESCRIPTOR_HEAP_TYPE_CBV_SRV_UAV + 1
    )
    D3D12_DESCRIPTOR_HEAP_TYPE_RTV = (
        D3D12_DESCRIPTOR_HEAP_TYPE_SAMPLER + 1
    )
    D3D12_DESCRIPTOR_HEAP_TYPE_DSV = D3D12_DESCRIPTOR_HEAP_TYPE_RTV + 1
    D3D12_DESCRIPTOR_HEAP_TYPE_NUM_TYPES = (
        D3D12_DESCRIPTOR_HEAP_TYPE_DSV + 1
    )


class D3D12_DESCRIPTOR_HEAP_FLAGS(ENUM):
    D3D12_DESCRIPTOR_HEAP_FLAG_NONE = 0
    D3D12_DESCRIPTOR_HEAP_FLAG_SHADER_VISIBLE = 0x1

D3D12_DESCRIPTOR_HEAP_DESC._fields_ = [
    ('Type', D3D12_DESCRIPTOR_HEAP_TYPE),
    ('NumDescriptors', UINT),
    ('Flags', D3D12_DESCRIPTOR_HEAP_FLAGS),
    ('NodeMask', UINT),
]


class D3D12_DESCRIPTOR_RANGE_TYPE(ENUM):
    D3D12_DESCRIPTOR_RANGE_TYPE_SRV = 0
    D3D12_DESCRIPTOR_RANGE_TYPE_UAV = (
        D3D12_DESCRIPTOR_RANGE_TYPE_SRV + 1
    )
    D3D12_DESCRIPTOR_RANGE_TYPE_CBV = (
        D3D12_DESCRIPTOR_RANGE_TYPE_UAV + 1
    )
    D3D12_DESCRIPTOR_RANGE_TYPE_SAMPLER = (
        D3D12_DESCRIPTOR_RANGE_TYPE_CBV + 1
    )

D3D12_DESCRIPTOR_RANGE._fields_ = [
    ('RangeType', D3D12_DESCRIPTOR_RANGE_TYPE),
    ('NumDescriptors', UINT),
    ('BaseShaderRegister', UINT),
    ('RegisterSpace', UINT),
    ('OffsetInDescriptorsFromTableStart', UINT),
]

D3D12_ROOT_DESCRIPTOR_TABLE._fields_ = [
    ('NumDescriptorRanges', UINT),
    ('pDescriptorRanges', POINTER(D3D12_DESCRIPTOR_RANGE)),
]

D3D12_ROOT_CONSTANTS._fields_ = [
    ('ShaderRegister', UINT),
    ('RegisterSpace', UINT),
    ('Num32BitValues', UINT),
]

D3D12_ROOT_DESCRIPTOR._fields_ = [
    ('ShaderRegister', UINT),
    ('RegisterSpace', UINT),
]


class D3D12_SHADER_VISIBILITY(ENUM):
    D3D12_SHADER_VISIBILITY_ALL = 0
    D3D12_SHADER_VISIBILITY_VERTEX = 1
    D3D12_SHADER_VISIBILITY_HULL = 2
    D3D12_SHADER_VISIBILITY_DOMAIN = 3
    D3D12_SHADER_VISIBILITY_GEOMETRY = 4
    D3D12_SHADER_VISIBILITY_PIXEL = 5


class D3D12_ROOT_PARAMETER_TYPE(ENUM):
    D3D12_ROOT_PARAMETER_TYPE_DESCRIPTOR_TABLE = 0
    D3D12_ROOT_PARAMETER_TYPE_32BIT_CONSTANTS = (
        D3D12_ROOT_PARAMETER_TYPE_DESCRIPTOR_TABLE + 1
    )
    D3D12_ROOT_PARAMETER_TYPE_CBV = (
        D3D12_ROOT_PARAMETER_TYPE_32BIT_CONSTANTS + 1
    )
    D3D12_ROOT_PARAMETER_TYPE_SRV = D3D12_ROOT_PARAMETER_TYPE_CBV + 1
    D3D12_ROOT_PARAMETER_TYPE_UAV = D3D12_ROOT_PARAMETER_TYPE_SRV + 1


class _Union_8(ctypes.Union):
    pass


_Union_8._fields_ = [
    ('DescriptorTable', D3D12_ROOT_DESCRIPTOR_TABLE),
    ('Constants', D3D12_ROOT_CONSTANTS),
    ('Descriptor', D3D12_ROOT_DESCRIPTOR),
]
D3D12_ROOT_PARAMETER._Union_8 = _Union_8

D3D12_ROOT_PARAMETER._anonymous_ = (
    '_Union_8',
)

D3D12_ROOT_PARAMETER._fields_ = [
    ('ParameterType', D3D12_ROOT_PARAMETER_TYPE),
    ('_Union_8', D3D12_ROOT_PARAMETER._Union_8),
    ('ShaderVisibility', D3D12_SHADER_VISIBILITY),
]


class D3D12_ROOT_SIGNATURE_FLAGS(ENUM):
    D3D12_ROOT_SIGNATURE_FLAG_NONE = 0
    D3D12_ROOT_SIGNATURE_FLAG_ALLOW_INPUT_ASSEMBLER_INPUT_LAYOUT = 0x1
    D3D12_ROOT_SIGNATURE_FLAG_DENY_VERTEX_SHADER_ROOT_ACCESS = 0x2
    D3D12_ROOT_SIGNATURE_FLAG_DENY_HULL_SHADER_ROOT_ACCESS = 0x4
    D3D12_ROOT_SIGNATURE_FLAG_DENY_DOMAIN_SHADER_ROOT_ACCESS = 0x8
    D3D12_ROOT_SIGNATURE_FLAG_DENY_GEOMETRY_SHADER_ROOT_ACCESS = 0x10
    D3D12_ROOT_SIGNATURE_FLAG_DENY_PIXEL_SHADER_ROOT_ACCESS = 0x20
    D3D12_ROOT_SIGNATURE_FLAG_ALLOW_STREAM_OUTPUT = 0x40


class D3D12_STATIC_BORDER_COLOR(ENUM):
    D3D12_STATIC_BORDER_COLOR_TRANSPARENT_BLACK = 0
    D3D12_STATIC_BORDER_COLOR_OPAQUE_BLACK = (
        D3D12_STATIC_BORDER_COLOR_TRANSPARENT_BLACK + 1
    )
    D3D12_STATIC_BORDER_COLOR_OPAQUE_WHITE = (
        D3D12_STATIC_BORDER_COLOR_OPAQUE_BLACK + 1
    )

D3D12_STATIC_SAMPLER_DESC._fields_ = [
    ('Filter', D3D12_FILTER),
    ('AddressU', D3D12_TEXTURE_ADDRESS_MODE),
    ('AddressV', D3D12_TEXTURE_ADDRESS_MODE),
    ('AddressW', D3D12_TEXTURE_ADDRESS_MODE),
    ('MipLODBias', FLOAT),
    ('MaxAnisotropy', UINT),
    ('ComparisonFunc', D3D12_COMPARISON_FUNC),
    ('BorderColor', D3D12_STATIC_BORDER_COLOR),
    ('MinLOD', FLOAT),
    ('MaxLOD', FLOAT),
    ('ShaderRegister', UINT),
    ('RegisterSpace', UINT),
    ('ShaderVisibility', D3D12_SHADER_VISIBILITY),
]

D3D12_ROOT_SIGNATURE_DESC._fields_ = [
    ('NumParameters', UINT),
    ('pParameters', POINTER(D3D12_ROOT_PARAMETER)),
    ('NumStaticSamplers', UINT),
    ('pStaticSamplers', POINTER(D3D12_STATIC_SAMPLER_DESC)),
    ('Flags', D3D12_ROOT_SIGNATURE_FLAGS),
]


class D3D12_DESCRIPTOR_RANGE_FLAGS(ENUM):
    D3D12_DESCRIPTOR_RANGE_FLAG_NONE = 0
    D3D12_DESCRIPTOR_RANGE_FLAG_DESCRIPTORS_VOLATILE = 0x1
    D3D12_DESCRIPTOR_RANGE_FLAG_DATA_VOLATILE = 0x2
    D3D12_DESCRIPTOR_RANGE_FLAG_DATA_STATIC_WHILE_SET_AT_EXECUTE = 0x4
    D3D12_DESCRIPTOR_RANGE_FLAG_DATA_STATIC = 0x8

D3D12_DESCRIPTOR_RANGE1._fields_ = [
    ('RangeType', D3D12_DESCRIPTOR_RANGE_TYPE),
    ('NumDescriptors', UINT),
    ('BaseShaderRegister', UINT),
    ('RegisterSpace', UINT),
    ('Flags', D3D12_DESCRIPTOR_RANGE_FLAGS),
    ('OffsetInDescriptorsFromTableStart', UINT),
]

D3D12_ROOT_DESCRIPTOR_TABLE1._fields_ = [
    ('NumDescriptorRanges', UINT),
    ('pDescriptorRanges', POINTER(D3D12_DESCRIPTOR_RANGE1)),
]


class D3D12_ROOT_DESCRIPTOR_FLAGS(ENUM):
    D3D12_ROOT_DESCRIPTOR_FLAG_NONE = 0
    D3D12_ROOT_DESCRIPTOR_FLAG_DATA_VOLATILE = 0x2
    D3D12_ROOT_DESCRIPTOR_FLAG_DATA_STATIC_WHILE_SET_AT_EXECUTE = 0x4
    D3D12_ROOT_DESCRIPTOR_FLAG_DATA_STATIC = 0x8

D3D12_ROOT_DESCRIPTOR1._fields_ = [
    ('ShaderRegister', UINT),
    ('RegisterSpace', UINT),
    ('Flags', D3D12_ROOT_DESCRIPTOR_FLAGS),
]


class _Union_9(ctypes.Union):
    pass


_Union_9._fields_ = [
    ('DescriptorTable', D3D12_ROOT_DESCRIPTOR_TABLE1),
    ('Constants', D3D12_ROOT_CONSTANTS),
    ('Descriptor', D3D12_ROOT_DESCRIPTOR1),
]
D3D12_ROOT_PARAMETER1._Union_9 = _Union_9

D3D12_ROOT_PARAMETER1._anonymous_ = (
    '_Union_9',
)

D3D12_ROOT_PARAMETER1._fields_ = [
    ('ParameterType', D3D12_ROOT_PARAMETER_TYPE),
    ('_Union_9', D3D12_ROOT_PARAMETER1._Union_9),
    ('ShaderVisibility', D3D12_SHADER_VISIBILITY),
]

D3D12_ROOT_SIGNATURE_DESC1._fields_ = [
    ('NumParameters', UINT),
    ('pParameters', POINTER(D3D12_ROOT_PARAMETER1)),
    ('NumStaticSamplers', UINT),
    ('pStaticSamplers', POINTER(D3D12_STATIC_SAMPLER_DESC)),
    ('Flags', D3D12_ROOT_SIGNATURE_FLAGS),
]


class _Union_10(ctypes.Union):
    pass


_Union_10._fields_ = [
    ('Desc_1_0', D3D12_ROOT_SIGNATURE_DESC),
    ('Desc_1_1', D3D12_ROOT_SIGNATURE_DESC1),
]
D3D12_VERSIONED_ROOT_SIGNATURE_DESC._Union_10 = _Union_10

D3D12_VERSIONED_ROOT_SIGNATURE_DESC._anonymous_ = (
    '_Union_10',
)

D3D12_VERSIONED_ROOT_SIGNATURE_DESC._fields_ = [
    ('Version', D3D_ROOT_SIGNATURE_VERSION),
    ('_Union_10', D3D12_VERSIONED_ROOT_SIGNATURE_DESC._Union_10),
]


IID_ID3D12RootSignatureDeserializer = MIDL_INTERFACE(
    "{34AB647B-3CC8-46AC-841B-C0965645C046}"
)
ID3D12RootSignatureDeserializer._iid_ = IID_ID3D12RootSignatureDeserializer


ID3D12RootSignatureDeserializer._methods_ = [
    COMMETHOD(
        [helpstring('Method *GetRootSignatureDesc')],
        D3D12_ROOT_SIGNATURE_DESC,
        '*GetRootSignatureDesc',
    ),
]

IID_ID3D12VersionedRootSignatureDeserializer = MIDL_INTERFACE(
    "{7F91CE67-090C-4BB7-B78E-ED8FF2E31DA0}"
)
ID3D12VersionedRootSignatureDeserializer._iid_ = IID_ID3D12VersionedRootSignatureDeserializer


ID3D12VersionedRootSignatureDeserializer._methods_ = [
    COMMETHOD(
        [helpstring('Method GetRootSignatureDescAtVersion')],
        HRESULT,
        'GetRootSignatureDescAtVersion',
        ([], D3D_ROOT_SIGNATURE_VERSION, 'convertToVersion'),
        (
            ['out'],
            POINTER(POINTER(D3D12_VERSIONED_ROOT_SIGNATURE_DESC)),
            'ppDesc'
        ),
    ),
    COMMETHOD(
        [helpstring('Method *GetUnconvertedRootSignatureDesc')],
        D3D12_VERSIONED_ROOT_SIGNATURE_DESC,
        '*GetUnconvertedRootSignatureDesc',
    ),
]

# HRESULT (WINAPI* PFN_D3D12_SERIALIZE_ROOT_SIGNATURE)( _In_ D3D12_ROOT_SIGNATURE_DESC* pRootSignature, _In_ D3D_ROOT_SIGNATURE_VERSION Version, _Out_ ID3DBlob** ppBlob, _Always_(_Outptr_opt_result_maybenull_) ID3DBlob** ppErrorBlob);
PFN_D3D12_SERIALIZE_ROOT_SIGNATURE = ctypes.WINFUNCTYPE(
    HRESULT,
    POINTER(D3D12_ROOT_SIGNATURE_DESC),
    D3D_ROOT_SIGNATURE_VERSION,
    POINTER(POINTER(ID3DBlob)),
    POINTER(POINTER(ID3DBlob)),
)


d3d12 = ctypes.windll.D3D12


# HRESULT WINAPI D3D12SerializeRootSignature(
# _In_ D3D12_ROOT_SIGNATURE_DESC* pRootSignature,
# _In_ D3D_ROOT_SIGNATURE_VERSION Version,
# _Out_ ID3DBlob** ppBlob,
# _Always_(_Outptr_opt_result_maybenull_) ID3DBlob** ppErrorBlob);
D3D12SerializeRootSignature = d3d12.D3D12SerializeRootSignature
D3D12SerializeRootSignature.restype = HRESULT


# HRESULT (WINAPI* PFN_D3D12_CREATE_ROOT_SIGNATURE_DESERIALIZER)( _In_reads_bytes_(SrcDataSizeInBytes) LPCVOID pSrcData, _In_ SIZE_T SrcDataSizeInBytes, _In_ REFIID pRootSignatureDeserializerInterface, _Out_ VOID** ppRootSignatureDeserializer);
PFN_D3D12_CREATE_ROOT_SIGNATURE_DESERIALIZER = ctypes.WINFUNCTYPE(
    HRESULT,
    LPCVOID,
    SIZE_T,
    REFIID,
    POINTER(POINTER(VOID)),
)


# HRESULT WINAPI D3D12CreateRootSignatureDeserializer(
# _In_reads_bytes_(SrcDataSizeInBytes) LPCVOID pSrcData,
# _In_ SIZE_T SrcDataSizeInBytes,
# _In_ REFIID pRootSignatureDeserializerInterface,
# _Out_ VOID** ppRootSignatureDeserializer);
D3D12CreateRootSignatureDeserializer = (
    d3d12.D3D12CreateRootSignatureDeserializer
)
D3D12CreateRootSignatureDeserializer.restype = HRESULT

# HRESULT (WINAPI* PFN_D3D12_SERIALIZE_VERSIONED_ROOT_SIGNATURE)( _In_ D3D12_VERSIONED_ROOT_SIGNATURE_DESC* pRootSignature, _Out_ ID3DBlob** ppBlob, _Always_(_Outptr_opt_result_maybenull_) ID3DBlob** ppErrorBlob);
PFN_D3D12_SERIALIZE_VERSIONED_ROOT_SIGNATURE = ctypes.WINFUNCTYPE(
    HRESULT,
    POINTER(D3D12_VERSIONED_ROOT_SIGNATURE_DESC),
    POINTER(POINTER(ID3DBlob)),
    POINTER(POINTER(ID3DBlob)),
)


d3d12 = ctypes.windll.D3D12


# HRESULT WINAPI D3D12SerializeVersionedRootSignature(
# _In_ D3D12_VERSIONED_ROOT_SIGNATURE_DESC* pRootSignature,
# _Out_ ID3DBlob** ppBlob,
# _Always_(_Outptr_opt_result_maybenull_) ID3DBlob** ppErrorBlob);
D3D12SerializeVersionedRootSignature = (
    d3d12.D3D12SerializeVersionedRootSignature
)
D3D12SerializeVersionedRootSignature.restype = HRESULT


# HRESULT (WINAPI* PFN_D3D12_CREATE_VERSIONED_ROOT_SIGNATURE_DESERIALIZER)( _In_reads_bytes_(SrcDataSizeInBytes) LPCVOID pSrcData, _In_ SIZE_T SrcDataSizeInBytes, _In_ REFIID pRootSignatureDeserializerInterface, _Out_ VOID** ppRootSignatureDeserializer);
PFN_D3D12_CREATE_VERSIONED_ROOT_SIGNATURE_DESERIALIZER = ctypes.WINFUNCTYPE(
    HRESULT,
    LPCVOID,
    SIZE_T,
    REFIID,
    POINTER(POINTER(VOID)),
)


# HRESULT WINAPI D3D12CreateVersionedRootSignatureDeserializer(
# _In_reads_bytes_(SrcDataSizeInBytes) LPCVOID pSrcData,
# _In_ SIZE_T SrcDataSizeInBytes,
# _In_ REFIID pRootSignatureDeserializerInterface,
# _Out_ VOID** ppRootSignatureDeserializer);
D3D12CreateVersionedRootSignatureDeserializer = (
    d3d12.D3D12CreateVersionedRootSignatureDeserializer
)
D3D12CreateVersionedRootSignatureDeserializer.restype = HRESULT


D3D12_CPU_DESCRIPTOR_HANDLE._fields_ = [
    ('ptr', SIZE_T),
]

D3D12_GPU_DESCRIPTOR_HANDLE._fields_ = [
    ('ptr', UINT64),
]

# If rects are supplied in D3D12_DISCARD_REGION, below, the resource
# must have 2D subresources with all specified subresources the same
# dimension.
D3D12_DISCARD_REGION._fields_ = [
    ('NumRects', UINT),
    ('pRects', POINTER(D3D12_RECT)),
    ('FirstSubresource', UINT),
    ('NumSubresources', UINT),
]


class D3D12_QUERY_HEAP_TYPE(ENUM):
    D3D12_QUERY_HEAP_TYPE_OCCLUSION = 0
    D3D12_QUERY_HEAP_TYPE_TIMESTAMP = 1
    D3D12_QUERY_HEAP_TYPE_PIPELINE_STATISTICS = 2
    D3D12_QUERY_HEAP_TYPE_SO_STATISTICS = 3
    D3D12_QUERY_HEAP_TYPE_VIDEO_DECODE_STATISTICS = 4
    D3D12_QUERY_HEAP_TYPE_COPY_QUEUE_TIMESTAMP = 5

D3D12_QUERY_HEAP_DESC._fields_ = [
    ('Type', D3D12_QUERY_HEAP_TYPE),
    ('Count', UINT),
    ('NodeMask', UINT),
]


class D3D12_QUERY_TYPE(ENUM):
    D3D12_QUERY_TYPE_OCCLUSION = 0
    D3D12_QUERY_TYPE_BINARY_OCCLUSION = 1
    D3D12_QUERY_TYPE_TIMESTAMP = 2
    D3D12_QUERY_TYPE_PIPELINE_STATISTICS = 3
    D3D12_QUERY_TYPE_SO_STATISTICS_STREAM0 = 4
    D3D12_QUERY_TYPE_SO_STATISTICS_STREAM1 = 5
    D3D12_QUERY_TYPE_SO_STATISTICS_STREAM2 = 6
    D3D12_QUERY_TYPE_SO_STATISTICS_STREAM3 = 7
    D3D12_QUERY_TYPE_VIDEO_DECODE_STATISTICS = 8


class D3D12_PREDICATION_OP(ENUM):
    D3D12_PREDICATION_OP_EQUAL_ZERO = 0
    D3D12_PREDICATION_OP_NOT_EQUAL_ZERO = 1

D3D12_QUERY_DATA_PIPELINE_STATISTICS._fields_ = [
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

D3D12_QUERY_DATA_SO_STATISTICS._fields_ = [
    ('NumPrimitivesWritten', UINT64),
    ('PrimitivesStorageNeeded', UINT64),
]

D3D12_STREAM_OUTPUT_BUFFER_VIEW._fields_ = [
    ('BufferLocation', D3D12_GPU_VIRTUAL_ADDRESS),
    ('SizeInBytes', UINT64),
    ('BufferFilledSizeLocation', D3D12_GPU_VIRTUAL_ADDRESS),
]

D3D12_DRAW_ARGUMENTS._fields_ = [
    ('VertexCountPerInstance', UINT),
    ('InstanceCount', UINT),
    ('StartVertexLocation', UINT),
    ('StartInstanceLocation', UINT),
]

D3D12_DRAW_INDEXED_ARGUMENTS._fields_ = [
    ('IndexCountPerInstance', UINT),
    ('InstanceCount', UINT),
    ('StartIndexLocation', UINT),
    ('BaseVertexLocation', INT),
    ('StartInstanceLocation', UINT),
]

D3D12_DISPATCH_ARGUMENTS._fields_ = [
    ('ThreadGroupCountX', UINT),
    ('ThreadGroupCountY', UINT),
    ('ThreadGroupCountZ', UINT),
]

D3D12_VERTEX_BUFFER_VIEW._fields_ = [
    ('BufferLocation', D3D12_GPU_VIRTUAL_ADDRESS),
    ('SizeInBytes', UINT),
    ('StrideInBytes', UINT),
]

D3D12_INDEX_BUFFER_VIEW._fields_ = [
    ('BufferLocation', D3D12_GPU_VIRTUAL_ADDRESS),
    ('SizeInBytes', UINT),
    ('Format', DXGI_FORMAT),
]


class D3D12_INDIRECT_ARGUMENT_TYPE(ENUM):
    D3D12_INDIRECT_ARGUMENT_TYPE_DRAW = 0
    D3D12_INDIRECT_ARGUMENT_TYPE_DRAW_INDEXED = (
        D3D12_INDIRECT_ARGUMENT_TYPE_DRAW + 1
    )
    D3D12_INDIRECT_ARGUMENT_TYPE_DISPATCH = (
        D3D12_INDIRECT_ARGUMENT_TYPE_DRAW_INDEXED + 1
    )
    D3D12_INDIRECT_ARGUMENT_TYPE_VERTEX_BUFFER_VIEW = (
        D3D12_INDIRECT_ARGUMENT_TYPE_DISPATCH + 1
    )
    D3D12_INDIRECT_ARGUMENT_TYPE_INDEX_BUFFER_VIEW = (
        D3D12_INDIRECT_ARGUMENT_TYPE_VERTEX_BUFFER_VIEW + 1
    )
    D3D12_INDIRECT_ARGUMENT_TYPE_CONSTANT = (
        D3D12_INDIRECT_ARGUMENT_TYPE_INDEX_BUFFER_VIEW + 1
    )
    D3D12_INDIRECT_ARGUMENT_TYPE_CONSTANT_BUFFER_VIEW = (
        D3D12_INDIRECT_ARGUMENT_TYPE_CONSTANT + 1
    )
    D3D12_INDIRECT_ARGUMENT_TYPE_SHADER_RESOURCE_VIEW = (
        D3D12_INDIRECT_ARGUMENT_TYPE_CONSTANT_BUFFER_VIEW + 1
    )
    D3D12_INDIRECT_ARGUMENT_TYPE_UNORDERED_ACCESS_VIEW = (
        D3D12_INDIRECT_ARGUMENT_TYPE_SHADER_RESOURCE_VIEW + 1
    )


class _Union_11(ctypes.Union):
    pass


class VertexBuffer(ctypes.Structure):
    pass


VertexBuffer._fields_ = [
    ('Slot', UINT),
]
_Union_11.VertexBuffer = VertexBuffer


class Constant(ctypes.Structure):
    pass


Constant._fields_ = [
    ('RootParameterIndex', UINT),
    ('DestOffsetIn32BitValues', UINT),
    ('Num32BitValuesToSet', UINT),
]
_Union_11.Constant = Constant


class ConstantBufferView(ctypes.Structure):
    pass


ConstantBufferView._fields_ = [
    ('RootParameterIndex', UINT),
]
_Union_11.ConstantBufferView = ConstantBufferView


class ShaderResourceView(ctypes.Structure):
    pass


ShaderResourceView._fields_ = [
    ('RootParameterIndex', UINT),
]
_Union_11.ShaderResourceView = ShaderResourceView


class UnorderedAccessView(ctypes.Structure):
    pass


UnorderedAccessView._fields_ = [
    ('RootParameterIndex', UINT),
]
_Union_11.UnorderedAccessView = UnorderedAccessView


_Union_11._fields_ = [
    ('VertexBuffer', _Union_11.VertexBuffer),
    ('Constant', _Union_11.Constant),
    ('ConstantBufferView', _Union_11.ConstantBufferView),
    ('ShaderResourceView', _Union_11.ShaderResourceView),
    ('UnorderedAccessView', _Union_11.UnorderedAccessView),
]
D3D12_INDIRECT_ARGUMENT_DESC._Union_11 = _Union_11

D3D12_INDIRECT_ARGUMENT_DESC._anonymous_ = (
    '_Union_11',
)

D3D12_INDIRECT_ARGUMENT_DESC._fields_ = [
    ('Type', D3D12_INDIRECT_ARGUMENT_TYPE),
    ('_Union_11', D3D12_INDIRECT_ARGUMENT_DESC._Union_11),
]

D3D12_COMMAND_SIGNATURE_DESC._fields_ = [
    ('ByteStride', UINT),
    ('NumArgumentDescs', UINT),
    ('pArgumentDescs', POINTER(D3D12_INDIRECT_ARGUMENT_DESC)),
    ('NodeMask', UINT),
]


IID_ID3D12Pageable = MIDL_INTERFACE(
    "{63EE58FB-1268-4835-86DA-F008CE62F0D6}"
)
ID3D12Pageable._iid_ = IID_ID3D12Pageable


ID3D12Pageable._methods_ = []


IID_ID3D12Heap = MIDL_INTERFACE(
    "{6B3B2502-6E51-45B3-90EE-9884265E8DF3}"
)
ID3D12Heap._iid_ = IID_ID3D12Heap


ID3D12Heap._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        D3D12_HEAP_DESC,
        'GetDesc',
    ),
]

IID_ID3D12Resource = MIDL_INTERFACE(
    "{696442BE-A72E-4059-BC79-5B5C98040FAD}"
)
ID3D12Resource._iid_ = IID_ID3D12Resource


ID3D12Resource._methods_ = [
    COMMETHOD(
        [helpstring('Method Map')],
        HRESULT,
        'Map',
        ([], UINT, 'Subresource'),
        (['in'], POINTER(D3D12_RANGE), 'pReadRange'),
        (['out', 'in'], POINTER(POINTER(VOID)), 'ppData'),
    ),
    COMMETHOD(
        [helpstring('Method Unmap')],
        VOID,
        'Unmap',
        ([], UINT, 'Subresource'),
        (['in'], POINTER(D3D12_RANGE), 'pWrittenRange'),
    ),
    COMMETHOD(
        [helpstring('Method GetDesc')],
        D3D12_RESOURCE_DESC,
        'GetDesc',
    ),
    COMMETHOD(
        [helpstring('Method GetGPUVirtualAddress')],
        D3D12_GPU_VIRTUAL_ADDRESS,
        'GetGPUVirtualAddress',
    ),
    COMMETHOD(
        [helpstring('Method WriteToSubresource')],
        HRESULT,
        'WriteToSubresource',
        ([], UINT, 'DstSubresource'),
        (['in'], POINTER(D3D12_BOX), 'pDstBox'),
        (['in'], POINTER(VOID), 'pSrcData'),
        ([], UINT, 'SrcRowPitch'),
        ([], UINT, 'SrcDepthPitch'),
    ),
    COMMETHOD(
        [helpstring('Method ReadFromSubresource')],
        HRESULT,
        'ReadFromSubresource',
        (['out'], POINTER(VOID), 'pDstData'),
        ([], UINT, 'DstRowPitch'),
        ([], UINT, 'DstDepthPitch'),
        ([], UINT, 'SrcSubresource'),
        (['in'], POINTER(D3D12_BOX), 'pSrcBox'),
    ),
    COMMETHOD(
        [helpstring('Method GetHeapProperties')],
        HRESULT,
        'GetHeapProperties',
        (
            ['out'],
            POINTER(D3D12_HEAP_PROPERTIES),
            'pHeapProperties'
        ),
        (['out'], POINTER(D3D12_HEAP_FLAGS), 'pHeapFlags'),
    ),
]

IID_ID3D12CommandAllocator = MIDL_INTERFACE(
    "{6102DEE4-AF59-4B09-B999-B44D73F09B24}"
)
ID3D12CommandAllocator._iid_ = IID_ID3D12CommandAllocator


ID3D12CommandAllocator._methods_ = [
    COMMETHOD(
        [helpstring('Method Reset')],
        HRESULT,
        'Reset',
    ),
]

IID_ID3D12Fence = MIDL_INTERFACE(
    "{0A753DCF-C4D8-4B91-ADF6-BE5A60D95A76}"
)
ID3D12Fence._iid_ = IID_ID3D12Fence


ID3D12Fence._methods_ = [
    COMMETHOD(
        [helpstring('Method GetCompletedValue')],
        UINT64,
        'GetCompletedValue',
    ),
    COMMETHOD(
        [helpstring('Method SetEventOnCompletion')],
        HRESULT,
        'SetEventOnCompletion',
        ([], UINT64, 'Value'),
        ([], HANDLE, 'hEvent'),
    ),
    COMMETHOD(
        [helpstring('Method Signal')],
        HRESULT,
        'Signal',
        ([], UINT64, 'Value'),
    ),
]

IID_ID3D12Fence1 = MIDL_INTERFACE(
    "{433685FE-E22B-4CA0-A8DB-B5B4F4DD0E4A}"
)
ID3D12Fence1._iid_ = IID_ID3D12Fence1


ID3D12Fence1._methods_ = [
    COMMETHOD(
        [helpstring('Method GetCreationFlags')],
        D3D12_FENCE_FLAGS,
        'GetCreationFlags',
    ),
]

IID_ID3D12PipelineState = MIDL_INTERFACE(
    "{765A30F3-F624-4C6F-A828-ACE948622445}"
)
ID3D12PipelineState._iid_ = IID_ID3D12PipelineState


ID3D12PipelineState._methods_ = [
    COMMETHOD(
        [helpstring('Method GetCachedBlob')],
        HRESULT,
        'GetCachedBlob',
        (['out'], POINTER(POINTER(ID3DBlob)), 'ppBlob'),
    ),
]

IID_ID3D12DescriptorHeap = MIDL_INTERFACE(
    "{8EFB471D-616C-4F49-90F7-127BB763FA51}"
)
ID3D12DescriptorHeap._iid_ = IID_ID3D12DescriptorHeap


ID3D12DescriptorHeap._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        D3D12_DESCRIPTOR_HEAP_DESC,
        'GetDesc',
    ),
    COMMETHOD(
        [helpstring('Method GetCPUDescriptorHandleForHeapStart')],
        D3D12_CPU_DESCRIPTOR_HANDLE,
        'GetCPUDescriptorHandleForHeapStart',
    ),
    COMMETHOD(
        [helpstring('Method GetGPUDescriptorHandleForHeapStart')],
        D3D12_GPU_DESCRIPTOR_HANDLE,
        'GetGPUDescriptorHandleForHeapStart',
    ),
]

IID_ID3D12QueryHeap = MIDL_INTERFACE(
    "{0D9658AE-ED45-469E-A61D-970EC583CAB4}"
)
ID3D12QueryHeap._iid_ = IID_ID3D12QueryHeap


ID3D12QueryHeap._methods_ = []


IID_ID3D12CommandSignature = MIDL_INTERFACE(
    "{C36A797C-EC80-4F0A-8985-A7B2475082D1}"
)
ID3D12CommandSignature._iid_ = IID_ID3D12CommandSignature


ID3D12CommandSignature._methods_ = []

IID_ID3D12CommandList = MIDL_INTERFACE(
    "{7116D91C-E7E4-47CE-B8C6-EC8168F437E5}"
)
ID3D12CommandList._iid_ = IID_ID3D12CommandList


ID3D12CommandList._methods_ = [
    COMMETHOD(
        [helpstring('Method GetType')],
        D3D12_COMMAND_LIST_TYPE,
        'GetType',
    ),
]

IID_ID3D12GraphicsCommandList = MIDL_INTERFACE(
    "{5B160D0F-AC1B-4185-8BA8-B3AE42A5A455}"
)
ID3D12GraphicsCommandList._iid_ = IID_ID3D12GraphicsCommandList


ID3D12GraphicsCommandList._methods_ = [
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
        (
            ['in'],
            POINTER(ID3D12PipelineState),
            'pInitialState'
        ),
    ),
    COMMETHOD(
        [helpstring('Method ClearState')],
        VOID,
        'ClearState',
        (
            ['in'],
            POINTER(ID3D12PipelineState),
            'pPipelineState'
        ),
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
        [helpstring('Method Dispatch')],
        VOID,
        'Dispatch',
        (['in'], UINT, 'ThreadGroupCountX'),
        (['in'], UINT, 'ThreadGroupCountY'),
        (['in'], UINT, 'ThreadGroupCountZ'),
    ),
    COMMETHOD(
        [helpstring('Method CopyBufferRegion')],
        VOID,
        'CopyBufferRegion',
        (['in'], POINTER(ID3D12Resource), 'pDstBuffer'),
        ([], UINT64, 'DstOffset'),
        (['in'], POINTER(ID3D12Resource), 'pSrcBuffer'),
        ([], UINT64, 'SrcOffset'),
        ([], UINT64, 'NumBytes'),
    ),
    COMMETHOD(
        [helpstring('Method CopyTextureRegion')],
        VOID,
        'CopyTextureRegion',
        (
            ['in'],
            POINTER(D3D12_TEXTURE_COPY_LOCATION),
            'pDst'
        ),
        ([], UINT, 'DstX'),
        ([], UINT, 'DstY'),
        ([], UINT, 'DstZ'),
        (
            ['in'],
            POINTER(D3D12_TEXTURE_COPY_LOCATION),
            'pSrc'
        ),
        (['in'], POINTER(D3D12_BOX), 'pSrcBox'),
    ),
    COMMETHOD(
        [helpstring('Method CopyResource')],
        VOID,
        'CopyResource',
        (['in'], POINTER(ID3D12Resource), 'pDstResource'),
        (['in'], POINTER(ID3D12Resource), 'pSrcResource'),
    ),
    COMMETHOD(
        [helpstring('Method CopyTiles')],
        VOID,
        'CopyTiles',
        (['in'], POINTER(ID3D12Resource), 'pTiledResource'),
        (
            ['in'],
            POINTER(D3D12_TILED_RESOURCE_COORDINATE),
            'pTileRegionStartCoordinate'
        ),
        (
            ['in'],
            POINTER(D3D12_TILE_REGION_SIZE),
            'pTileRegionSize'
        ),
        (['in'], POINTER(ID3D12Resource), 'pBuffer'),
        ([], UINT64, 'BufferStartOffsetInBytes'),
        ([], D3D12_TILE_COPY_FLAGS, 'Flags'),
    ),
    COMMETHOD(
        [helpstring('Method ResolveSubresource')],
        VOID,
        'ResolveSubresource',
        (['in'], POINTER(ID3D12Resource), 'pDstResource'),
        (['in'], UINT, 'DstSubresource'),
        (['in'], POINTER(ID3D12Resource), 'pSrcResource'),
        (['in'], UINT, 'SrcSubresource'),
        (['in'], DXGI_FORMAT, 'Format'),
    ),
    COMMETHOD(
        [helpstring('Method IASetPrimitiveTopology')],
        VOID,
        'IASetPrimitiveTopology',
        (
            ['in'],
            D3D12_PRIMITIVE_TOPOLOGY,
            'PrimitiveTopology'
        ),
    ),
    COMMETHOD(
        [helpstring('Method RSSetViewports')],
        VOID,
        'RSSetViewports',
        (['in'], UINT, 'NumViewports'),
        (['in'], POINTER(D3D12_VIEWPORT), 'pViewports'),
    ),
    COMMETHOD(
        [helpstring('Method RSSetScissorRects')],
        VOID,
        'RSSetScissorRects',
        (['in'], UINT, 'NumRects'),
        (['in'], POINTER(D3D12_RECT), 'pRects'),
    ),
    COMMETHOD(
        [helpstring('Method OMSetBlendFactor')],
        VOID,
        'OMSetBlendFactor',
        (['in'], 4, ']'),
    ),

    COMMETHOD(
        [helpstring('Method OMSetStencilRef')],
        VOID,
        'OMSetStencilRef',
        (['in'], UINT, 'StencilRef'),
    ),

    COMMETHOD(
        [helpstring('Method SetPipelineState')],
        VOID,
        'SetPipelineState',
        (
            ['in'],
            POINTER(ID3D12PipelineState),
            'pPipelineState'
        ),
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
        [helpstring('Method ExecuteBundle')],
        VOID,
        'ExecuteBundle',
        (
            ['in'],
            POINTER(ID3D12GraphicsCommandList),
            'pCommandList'
        ),
    ),

    COMMETHOD(
        [helpstring('Method SetDescriptorHeaps')],
        VOID,
        'SetDescriptorHeaps',
        (['in'], UINT, 'NumDescriptorHeaps'),
        (['in'], POINTER(POINTER(ID3D12DescriptorHeap)), 'ppDescriptorHeaps'),
    ),

    COMMETHOD(
        [helpstring('Method SetComputeRootSignature')],
        VOID,
        'SetComputeRootSignature',
        (
            ['in'],
            POINTER(ID3D12RootSignature),
            'pRootSignature'
        ),
    ),

    COMMETHOD(
        [helpstring('Method SetGraphicsRootSignature')],
        VOID,
        'SetGraphicsRootSignature',
        (
            ['in'],
            POINTER(ID3D12RootSignature),
            'pRootSignature'
        ),
    ),

    COMMETHOD(
        [helpstring('Method SetComputeRootDescriptorTable')],
        VOID,
        'SetComputeRootDescriptorTable',
        (['in'], UINT, 'RootParameterIndex'),
        (
            ['in'],
            D3D12_GPU_DESCRIPTOR_HANDLE,
            'BaseDescriptor'
        ),
    ),

    COMMETHOD(
        [helpstring('Method SetGraphicsRootDescriptorTable')],
        VOID,
        'SetGraphicsRootDescriptorTable',
        (['in'], UINT, 'RootParameterIndex'),
        (
            ['in'],
            D3D12_GPU_DESCRIPTOR_HANDLE,
            'BaseDescriptor'
        ),
    ),

    COMMETHOD(
        [helpstring('Method SetComputeRoot32BitConstant')],
        VOID,
        'SetComputeRoot32BitConstant',
        (['in'], UINT, 'RootParameterIndex'),
        (['in'], UINT, 'SrcData'),
        (['in'], UINT, 'DestOffsetIn32BitValues'),
    ),

    COMMETHOD(
        [helpstring('Method SetGraphicsRoot32BitConstant')],
        VOID,
        'SetGraphicsRoot32BitConstant',
        (['in'], UINT, 'RootParameterIndex'),
        (['in'], UINT, 'SrcData'),
        (['in'], UINT, 'DestOffsetIn32BitValues'),
    ),

    COMMETHOD(
        [helpstring('Method SetComputeRoot32BitConstants')],
        VOID,
        'SetComputeRoot32BitConstants',
        (['in'], UINT, 'RootParameterIndex'),
        (['in'], UINT, 'Num32BitValuesToSet'),
        (['in'], POINTER(VOID), 'pSrcData'),
        (['in'], UINT, 'DestOffsetIn32BitValues'),
    ),

    COMMETHOD(
        [helpstring('Method SetGraphicsRoot32BitConstants')],
        VOID,
        'SetGraphicsRoot32BitConstants',
        (['in'], UINT, 'RootParameterIndex'),
        (['in'], UINT, 'Num32BitValuesToSet'),
        (['in'], POINTER(VOID), 'pSrcData'),
        (['in'], UINT, 'DestOffsetIn32BitValues'),
    ),

    COMMETHOD(
        [helpstring('Method SetComputeRootConstantBufferView')],
        VOID,
        'SetComputeRootConstantBufferView',
        (['in'], UINT, 'RootParameterIndex'),
        (['in'], D3D12_GPU_VIRTUAL_ADDRESS, 'BufferLocation'),
    ),

    COMMETHOD(
        [helpstring('Method SetGraphicsRootConstantBufferView')],
        VOID,
        'SetGraphicsRootConstantBufferView',
        (['in'], UINT, 'RootParameterIndex'),
        (['in'], D3D12_GPU_VIRTUAL_ADDRESS, 'BufferLocation'),
    ),

    COMMETHOD(
        [helpstring('Method SetComputeRootShaderResourceView')],
        VOID,
        'SetComputeRootShaderResourceView',
        (['in'], UINT, 'RootParameterIndex'),
        (['in'], D3D12_GPU_VIRTUAL_ADDRESS, 'BufferLocation'),
    ),

    COMMETHOD(
        [helpstring('Method SetGraphicsRootShaderResourceView')],
        VOID,
        'SetGraphicsRootShaderResourceView',
        (['in'], UINT, 'RootParameterIndex'),
        (['in'], D3D12_GPU_VIRTUAL_ADDRESS, 'BufferLocation'),
    ),

    COMMETHOD(
        [helpstring('Method SetComputeRootUnorderedAccessView')],
        VOID,
        'SetComputeRootUnorderedAccessView',
        (['in'], UINT, 'RootParameterIndex'),
        (['in'], D3D12_GPU_VIRTUAL_ADDRESS, 'BufferLocation'),
    ),

    COMMETHOD(
        [helpstring('Method SetGraphicsRootUnorderedAccessView')],
        VOID,
        'SetGraphicsRootUnorderedAccessView',
        (['in'], UINT, 'RootParameterIndex'),
        (['in'], D3D12_GPU_VIRTUAL_ADDRESS, 'BufferLocation'),
    ),

    COMMETHOD(
        [helpstring('Method IASetIndexBuffer')],
        VOID,
        'IASetIndexBuffer',
        (['in'], POINTER(D3D12_INDEX_BUFFER_VIEW), 'pView'),
    ),

    COMMETHOD(
        [helpstring('Method IASetVertexBuffers')],
        VOID,
        'IASetVertexBuffers',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumViews'),
        (['in'], POINTER(D3D12_VERTEX_BUFFER_VIEW), 'pViews'),
    ),

    COMMETHOD(
        [helpstring('Method SOSetTargets')],
        VOID,
        'SOSetTargets',
        (['in'], UINT, 'StartSlot'),
        (['in'], UINT, 'NumViews'),
        (
            ['in'],
            POINTER(D3D12_STREAM_OUTPUT_BUFFER_VIEW),
            'pViews'
        ),
    ),

    COMMETHOD(
        [helpstring('Method OMSetRenderTargets')],
        VOID,
        'OMSetRenderTargets',
        (['in'], UINT, 'NumRenderTargetDescriptors'),
        (
            ['in'],
            POINTER(D3D12_CPU_DESCRIPTOR_HANDLE),
            'pRenderTargetDescriptors'
        ),
        (['in'], BOOL, 'RTsSingleHandleToDescriptorRange'),
        (
            ['in'],
            POINTER(D3D12_CPU_DESCRIPTOR_HANDLE),
            'pDepthStencilDescriptor'
        ),
    ),

    COMMETHOD(
        [helpstring('Method ClearDepthStencilView')],
        VOID,
        'ClearDepthStencilView',
        (
            ['in'],
            D3D12_CPU_DESCRIPTOR_HANDLE,
            'DepthStencilView'
        ),
        (['in'], D3D12_CLEAR_FLAGS, 'ClearFlags'),
        (['in'], FLOAT, 'Depth'),
        (['in'], UINT8, 'Stencil'),
        (['in'], UINT, 'NumRects'),
        (['in'], POINTER(D3D12_RECT), 'pRects'),
    ),

    COMMETHOD(
        [helpstring('Method ClearRenderTargetView')],
        VOID,
        'ClearRenderTargetView',
        (
            ['in'],
            D3D12_CPU_DESCRIPTOR_HANDLE,
            'RenderTargetView'
        ),
        (['in'], 4, ']'),
        (['in'], UINT, 'NumRects'),
        (['in'], POINTER(D3D12_RECT), 'pRects'),
    ),
    COMMETHOD(
        [helpstring('Method ClearUnorderedAccessViewUint')],
        VOID,
        'ClearUnorderedAccessViewUint',
        (
            ['in'],
            D3D12_GPU_DESCRIPTOR_HANDLE,
            'ViewGPUHandleInCurrentHeap'
        ),
        (
            ['in'],
            D3D12_CPU_DESCRIPTOR_HANDLE,
            'ViewCPUHandle'
        ),
        (['in'], POINTER(ID3D12Resource), 'pResource'),
        (['in'], 4, ']'),
        (['in'], UINT, 'NumRects'),
        (['in'], POINTER(D3D12_RECT), 'pRects'),
    ),
    COMMETHOD(
        [helpstring('Method ClearUnorderedAccessViewFloat')],
        VOID,
        'ClearUnorderedAccessViewFloat',
        (
            ['in'],
            D3D12_GPU_DESCRIPTOR_HANDLE,
            'ViewGPUHandleInCurrentHeap'
        ),
        (
            ['in'],
            D3D12_CPU_DESCRIPTOR_HANDLE,
            'ViewCPUHandle'
        ),
        (['in'], POINTER(ID3D12Resource), 'pResource'),
        (['in'], 4, ']'),
        (['in'], UINT, 'NumRects'),
        (['in'], POINTER(D3D12_RECT), 'pRects'),
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
        [helpstring('Method ExecuteIndirect')],
        VOID,
        'ExecuteIndirect',
        (
            ['in'],
            POINTER(ID3D12CommandSignature),
            'pCommandSignature'
        ),
        (['in'], UINT, 'MaxCommandCount'),
        (['in'], POINTER(ID3D12Resource), 'pArgumentBuffer'),
        (['in'], UINT64, 'ArgumentBufferOffset'),
        (['in'], POINTER(ID3D12Resource), 'pCountBuffer'),
        (['in'], UINT64, 'CountBufferOffset'),
    ),
]

IID_ID3D12GraphicsCommandList1 = MIDL_INTERFACE(
    "{553103FB-1FE7-4557-BB38-946D7D0E7CA7}"
)
ID3D12GraphicsCommandList1._iid_ = IID_ID3D12GraphicsCommandList1


ID3D12GraphicsCommandList1._methods_ = [
    COMMETHOD(
        [helpstring('Method AtomicCopyBufferUINT')],
        VOID,
        'AtomicCopyBufferUINT',
        (['in'], POINTER(ID3D12Resource), 'pDstBuffer'),
        ([], UINT64, 'DstOffset'),
        (['in'], POINTER(ID3D12Resource), 'pSrcBuffer'),
        ([], UINT64, 'SrcOffset'),
        ([], UINT, 'Dependencies'),
        (['in'], POINTER(POINTER(ID3D12Resource)), 'ppDependentResources'),
        (
            ['in'],
            POINTER(D3D12_SUBRESOURCE_RANGE_UINT64),
            'pDependentSubresourceRanges'
        ),
    ),
    COMMETHOD(
        [helpstring('Method AtomicCopyBufferUINT64')],
        VOID,
        'AtomicCopyBufferUINT64',
        (['in'], POINTER(ID3D12Resource), 'pDstBuffer'),
        ([], UINT64, 'DstOffset'),
        (['in'], POINTER(ID3D12Resource), 'pSrcBuffer'),
        ([], UINT64, 'SrcOffset'),
        ([], UINT, 'Dependencies'),
        (['in'], POINTER(POINTER(ID3D12Resource)), 'ppDependentResources'),
        (
            ['in'],
            POINTER(D3D12_SUBRESOURCE_RANGE_UINT64),
            'pDependentSubresourceRanges'
        ),
    ),
    COMMETHOD(
        [helpstring('Method OMSetDepthBounds')],
        VOID,
        'OMSetDepthBounds',
        (['in'], FLOAT, 'Min'),
        (['in'], FLOAT, 'Max'),
    ),
    COMMETHOD(
        [helpstring('Method SetSamplePositions')],
        VOID,
        'SetSamplePositions',
        (['in'], UINT, 'NumSamplesPerPixel'),
        (['in'], UINT, 'NumPixels'),
        (
            ['in'],
            POINTER(D3D12_SAMPLE_POSITION),
            'pSamplePositions'
        ),
    ),
    COMMETHOD(
        [helpstring('Method ResolveSubresourceRegion')],
        VOID,
        'ResolveSubresourceRegion',
        (['in'], POINTER(ID3D12Resource), 'pDstResource'),
        (['in'], UINT, 'DstSubresource'),
        (['in'], UINT, 'DstX'),
        (['in'], UINT, 'DstY'),
        (['in'], POINTER(ID3D12Resource), 'pSrcResource'),
        (['in'], UINT, 'SrcSubresource'),
        (['in'], POINTER(D3D12_RECT), 'pSrcRect'),
        (['in'], DXGI_FORMAT, 'Format'),
        (['in'], D3D12_RESOLVE_MODE, 'ResolveMode'),
    ),
    COMMETHOD(
        [helpstring('Method SetViewInstanceMask')],
        VOID,
        'SetViewInstanceMask',
        (['in'], UINT, 'Mask'),
    ),
]

D3D12_WRITEBUFFERIMMEDIATE_PARAMETER._fields_ = [
    ('Dest', D3D12_GPU_VIRTUAL_ADDRESS),
    ('Value', UINT32),
]


class D3D12_WRITEBUFFERIMMEDIATE_MODE(ENUM):
    D3D12_WRITEBUFFERIMMEDIATE_MODE_DEFAULT = 0
    D3D12_WRITEBUFFERIMMEDIATE_MODE_MARKER_IN = 0x1
    D3D12_WRITEBUFFERIMMEDIATE_MODE_MARKER_OUT = 0x2


IID_ID3D12GraphicsCommandList2 = MIDL_INTERFACE(
    "{38C3E585-FF17-412C-9150-4FC6F9D72A28}"
)
ID3D12GraphicsCommandList2._iid_ = IID_ID3D12GraphicsCommandList2


ID3D12GraphicsCommandList2._methods_ = [
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

IID_ID3D12CommandQueue = MIDL_INTERFACE(
    "{0EC870A6-5D7E-4C22-8CFC-5BAAE07616ED}"
)
ID3D12CommandQueue._iid_ = IID_ID3D12CommandQueue


ID3D12CommandQueue._methods_ = [
    COMMETHOD(
        [helpstring('Method UpdateTileMappings')],
        VOID,
        'UpdateTileMappings',
        (['in'], POINTER(ID3D12Resource), 'pResource'),
        ([], UINT, 'NumResourceRegions'),
        (
            ['in'],
            POINTER(D3D12_TILED_RESOURCE_COORDINATE),
            'pResourceRegionStartCoordinates'
        ),
        (
            ['in'],
            POINTER(D3D12_TILE_REGION_SIZE),
            'pResourceRegionSizes'
        ),
        (['in'], POINTER(ID3D12Heap), 'pHeap'),
        ([], UINT, 'NumRanges'),
        (
            ['in'],
            POINTER(D3D12_TILE_RANGE_FLAGS),
            'pRangeFlags'
        ),
        (['in'], POINTER(UINT), 'pHeapRangeStartOffsets'),
        (['in'], POINTER(UINT), 'pRangeTileCounts'),
        ([], D3D12_TILE_MAPPING_FLAGS, 'Flags'),
    ),
    COMMETHOD(
        [helpstring('Method CopyTileMappings')],
        VOID,
        'CopyTileMappings',
        (['in'], POINTER(ID3D12Resource), 'pDstResource'),
        (
            ['in'],
            POINTER(D3D12_TILED_RESOURCE_COORDINATE),
            'pDstRegionStartCoordinate'
        ),
        (['in'], POINTER(ID3D12Resource), 'pSrcResource'),
        (
            ['in'],
            POINTER(D3D12_TILED_RESOURCE_COORDINATE),
            'pSrcRegionStartCoordinate'
        ),
        (
            ['in'],
            POINTER(D3D12_TILE_REGION_SIZE),
            'pRegionSize'
        ),
        ([], D3D12_TILE_MAPPING_FLAGS, 'Flags'),
    ),
    COMMETHOD(
        [helpstring('Method ExecuteCommandLists')],
        VOID,
        'ExecuteCommandLists',
        (['in'], UINT, 'NumCommandLists'),
        (['in'], POINTER(POINTER(ID3D12CommandList)), 'ppCommandLists'),
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
        [helpstring('Method Signal')],
        HRESULT,
        'Signal',
        ([], POINTER(ID3D12Fence), 'pFence'),
        ([], UINT64, 'Value'),
    ),
    COMMETHOD(
        [helpstring('Method Wait')],
        HRESULT,
        'Wait',
        ([], POINTER(ID3D12Fence), 'pFence'),
        ([], UINT64, 'Value'),
    ),
    COMMETHOD(
        [helpstring('Method GetTimestampFrequency')],
        HRESULT,
        'GetTimestampFrequency',
        (['out'], POINTER(UINT64), 'pFrequency'),
    ),
    COMMETHOD(
        [helpstring('Method GetClockCalibration')],
        HRESULT,
        'GetClockCalibration',
        (['out'], POINTER(UINT64), 'pGpuTimestamp'),
        (['out'], POINTER(UINT64), 'pCpuTimestamp'),
    ),
    COMMETHOD(
        [helpstring('Method GetDesc')],
        D3D12_COMMAND_QUEUE_DESC,
        'GetDesc',
    ),
]

__LUID._fields_ = [
    ('LowPart', DWORD),
    ('HighPart', LONG),
]
PLUID = POINTER(__LUID)

IID_ID3D12Device = MIDL_INTERFACE(
    "{189819F1-1DB6-4B57-BE54-1821339B85F7}"
)
ID3D12Device._iid_ = IID_ID3D12Device


ID3D12Device._methods_ = [
    COMMETHOD(
        [helpstring('Method GetNodeCount')],
        UINT,
        'GetNodeCount',
    ),
    COMMETHOD(
        [helpstring('Method CreateCommandQueue')],
        HRESULT,
        'CreateCommandQueue',
        (['in'], POINTER(D3D12_COMMAND_QUEUE_DESC), 'pDesc'),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppCommandQueue'),
    ),
    COMMETHOD(
        [helpstring('Method CreateCommandAllocator')],
        HRESULT,
        'CreateCommandAllocator',
        (['in'], D3D12_COMMAND_LIST_TYPE, 'type'),
        ([], REFIID, 'riid'),
        (
            ['out'],
            POINTER(POINTER(VOID)),
            'ppCommandAllocator'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateGraphicsPipelineState')],
        HRESULT,
        'CreateGraphicsPipelineState',
        (
            ['in'],
            POINTER(D3D12_GRAPHICS_PIPELINE_STATE_DESC),
            'pDesc'
        ),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppPipelineState'),
    ),
    COMMETHOD(
        [helpstring('Method CreateComputePipelineState')],
        HRESULT,
        'CreateComputePipelineState',
        (
            ['in'],
            POINTER(D3D12_COMPUTE_PIPELINE_STATE_DESC),
            'pDesc'
        ),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppPipelineState'),
    ),
    COMMETHOD(
        [helpstring('Method CreateCommandList')],
        HRESULT,
        'CreateCommandList',
        (['in'], UINT, 'nodeMask'),
        (['in'], D3D12_COMMAND_LIST_TYPE, 'type'),
        (
            ['in'],
            POINTER(ID3D12CommandAllocator),
            'pCommandAllocator'
        ),
        (
            ['in'],
            POINTER(ID3D12PipelineState),
            'pInitialState'
        ),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppCommandList'),
    ),
    COMMETHOD(
        [helpstring('Method CheckFeatureSupport')],
        HRESULT,
        'CheckFeatureSupport',
        ([], D3D12_FEATURE, 'Feature'),
        (['out', 'in'], POINTER(VOID), 'pFeatureSupportData'),
        ([], UINT, 'FeatureSupportDataSize'),
    ),
    COMMETHOD(
        [helpstring('Method CreateDescriptorHeap')],
        HRESULT,
        'CreateDescriptorHeap',
        (
            ['in'],
            POINTER(D3D12_DESCRIPTOR_HEAP_DESC),
            'pDescriptorHeapDesc'
        ),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvHeap'),
    ),
    COMMETHOD(
        [helpstring('Method GetDescriptorHandleIncrementSize')],
        UINT,
        'GetDescriptorHandleIncrementSize',
        (
            ['in'],
            D3D12_DESCRIPTOR_HEAP_TYPE,
            'DescriptorHeapType'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateRootSignature')],
        HRESULT,
        'CreateRootSignature',
        (['in'], UINT, 'nodeMask'),
        (['in'], POINTER(VOID), 'pBlobWithRootSignature'),
        (['in'], SIZE_T, 'blobLengthInBytes'),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvRootSignature'),
    ),
    COMMETHOD(
        [helpstring('Method CreateConstantBufferView')],
        VOID,
        'CreateConstantBufferView',
        (
            ['in'],
            POINTER(D3D12_CONSTANT_BUFFER_VIEW_DESC),
            'pDesc'
        ),
        (
            ['in'],
            D3D12_CPU_DESCRIPTOR_HANDLE,
            'DestDescriptor'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateShaderResourceView')],
        VOID,
        'CreateShaderResourceView',
        (['in'], POINTER(ID3D12Resource), 'pResource'),
        (
            ['in'],
            POINTER(D3D12_SHADER_RESOURCE_VIEW_DESC),
            'pDesc'
        ),
        (
            ['in'],
            D3D12_CPU_DESCRIPTOR_HANDLE,
            'DestDescriptor'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateUnorderedAccessView')],
        VOID,
        'CreateUnorderedAccessView',
        (['in'], POINTER(ID3D12Resource), 'pResource'),
        (['in'], POINTER(ID3D12Resource), 'pCounterResource'),
        (
            ['in'],
            POINTER(D3D12_UNORDERED_ACCESS_VIEW_DESC),
            'pDesc'
        ),
        (
            ['in'],
            D3D12_CPU_DESCRIPTOR_HANDLE,
            'DestDescriptor'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateRenderTargetView')],
        VOID,
        'CreateRenderTargetView',
        (['in'], POINTER(ID3D12Resource), 'pResource'),
        (
            ['in'],
            POINTER(D3D12_RENDER_TARGET_VIEW_DESC),
            'pDesc'
        ),
        (
            ['in'],
            D3D12_CPU_DESCRIPTOR_HANDLE,
            'DestDescriptor'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateDepthStencilView')],
        VOID,
        'CreateDepthStencilView',
        (['in'], POINTER(ID3D12Resource), 'pResource'),
        (
            ['in'],
            POINTER(D3D12_DEPTH_STENCIL_VIEW_DESC),
            'pDesc'
        ),
        (
            ['in'],
            D3D12_CPU_DESCRIPTOR_HANDLE,
            'DestDescriptor'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateSampler')],
        VOID,
        'CreateSampler',
        (['in'], POINTER(D3D12_SAMPLER_DESC), 'pDesc'),
        (
            ['in'],
            D3D12_CPU_DESCRIPTOR_HANDLE,
            'DestDescriptor'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CopyDescriptors')],
        VOID,
        'CopyDescriptors',
        (['in'], UINT, 'NumDestDescriptorRanges'),
        (
            ['in'],
            POINTER(D3D12_CPU_DESCRIPTOR_HANDLE),
            'pDestDescriptorRangeStarts'
        ),
        (['in'], POINTER(UINT), 'pDestDescriptorRangeSizes'),
        (['in'], UINT, 'NumSrcDescriptorRanges'),
        (
            ['in'],
            POINTER(D3D12_CPU_DESCRIPTOR_HANDLE),
            'pSrcDescriptorRangeStarts'
        ),
        (['in'], POINTER(UINT), 'pSrcDescriptorRangeSizes'),
        (
            ['in'],
            D3D12_DESCRIPTOR_HEAP_TYPE,
            'DescriptorHeapsType'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CopyDescriptorsSimple')],
        VOID,
        'CopyDescriptorsSimple',
        (['in'], UINT, 'NumDescriptors'),
        (
            ['in'],
            D3D12_CPU_DESCRIPTOR_HANDLE,
            'DestDescriptorRangeStart'
        ),
        (
            ['in'],
            D3D12_CPU_DESCRIPTOR_HANDLE,
            'SrcDescriptorRangeStart'
        ),
        (
            ['in'],
            D3D12_DESCRIPTOR_HEAP_TYPE,
            'DescriptorHeapsType'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetResourceAllocationInfo')],
        D3D12_RESOURCE_ALLOCATION_INFO,
        'GetResourceAllocationInfo',
        (['in'], UINT, 'visibleMask'),
        (['in'], UINT, 'numResourceDescs'),
        (
            ['in'],
            POINTER(D3D12_RESOURCE_DESC),
            'pResourceDescs'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetCustomHeapProperties')],
        D3D12_HEAP_PROPERTIES,
        'GetCustomHeapProperties',
        (['in'], UINT, 'nodeMask'),
        ([], D3D12_HEAP_TYPE, 'heapType'),
    ),
    COMMETHOD(
        [helpstring('Method CreateCommittedResource')],
        HRESULT,
        'CreateCommittedResource',
        (
            ['in'],
            POINTER(D3D12_HEAP_PROPERTIES),
            'pHeapProperties'
        ),
        ([], D3D12_HEAP_FLAGS, 'HeapFlags'),
        (['in'], POINTER(D3D12_RESOURCE_DESC), 'pDesc'),
        ([], D3D12_RESOURCE_STATES, 'InitialResourceState'),
        (
            ['in'],
            POINTER(D3D12_CLEAR_VALUE),
            'pOptimizedClearValue'
        ),
        ([], REFIID, 'riidResource'),
        (['out'], POINTER(POINTER(VOID)), 'ppvResource'),
    ),
    COMMETHOD(
        [helpstring('Method CreateHeap')],
        HRESULT,
        'CreateHeap',
        (['in'], POINTER(D3D12_HEAP_DESC), 'pDesc'),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvHeap'),
    ),
    COMMETHOD(
        [helpstring('Method CreatePlacedResource')],
        HRESULT,
        'CreatePlacedResource',
        (['in'], POINTER(ID3D12Heap), 'pHeap'),
        ([], UINT64, 'HeapOffset'),
        (['in'], POINTER(D3D12_RESOURCE_DESC), 'pDesc'),
        ([], D3D12_RESOURCE_STATES, 'InitialState'),
        (
            ['in'],
            POINTER(D3D12_CLEAR_VALUE),
            'pOptimizedClearValue'
        ),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvResource'),
    ),
    COMMETHOD(
        [helpstring('Method CreateReservedResource')],
        HRESULT,
        'CreateReservedResource',
        (['in'], POINTER(D3D12_RESOURCE_DESC), 'pDesc'),
        ([], D3D12_RESOURCE_STATES, 'InitialState'),
        (
            ['in'],
            POINTER(D3D12_CLEAR_VALUE),
            'pOptimizedClearValue'
        ),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvResource'),
    ),
    COMMETHOD(
        [helpstring('Method CreateSharedHandle')],
        HRESULT,
        'CreateSharedHandle',
        (['in'], POINTER(ID3D12DeviceChild), 'pObject'),
        # SECURITY_ATTRIBUTES
        (['in'], POINTER(VOID), 'pAttributes'),
        ([], DWORD, 'Access'),
        (['in'], LPCWSTR, 'Name'),
        (['out'], POINTER(HANDLE), 'pHandle'),
    ),
    COMMETHOD(
        [helpstring('Method OpenSharedHandle')],
        HRESULT,
        'OpenSharedHandle',
        (['in'], HANDLE, 'NTHandle'),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvObj'),
    ),
    COMMETHOD(
        [helpstring('Method OpenSharedHandleByName')],
        HRESULT,
        'OpenSharedHandleByName',
        (['in'], LPCWSTR, 'Name'),
        ([], DWORD, 'Access'),
        (['out'], POINTER(HANDLE), 'pNTHandle'),
    ),
    COMMETHOD(
        [helpstring('Method MakeResident')],
        HRESULT,
        'MakeResident',
        ([], UINT, 'NumObjects'),
        (['in'], POINTER(POINTER(ID3D12Pageable)), 'ppObjects'),
    ),
    COMMETHOD(
        [helpstring('Method Evict')],
        HRESULT,
        'Evict',
        ([], UINT, 'NumObjects'),
        (['in'], POINTER(POINTER(ID3D12Pageable)), 'ppObjects'),
    ),
    COMMETHOD(
        [helpstring('Method CreateFence')],
        HRESULT,
        'CreateFence',
        ([], UINT64, 'InitialValue'),
        ([], D3D12_FENCE_FLAGS, 'Flags'),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppFence'),
    ),
    COMMETHOD(
        [helpstring('Method GetDeviceRemovedReason')],
        HRESULT,
        'GetDeviceRemovedReason',
    ),
    COMMETHOD(
        [helpstring('Method GetCopyableFootprints')],
        VOID,
        'GetCopyableFootprints',
        (
            ['in'],
            POINTER(D3D12_RESOURCE_DESC),
            'pResourceDesc'
        ),
        (['in'], UINT, 'FirstSubresource'),
        (['in'], UINT, 'NumSubresources'),
        ([], UINT64, 'BaseOffset'),
        (
            ['out'],
            POINTER(D3D12_PLACED_SUBRESOURCE_FOOTPRINT),
            'pLayouts'
        ),
        (['out'], POINTER(UINT), 'pNumRows'),
        (['out'], POINTER(UINT64), 'pRowSizeInBytes'),
        (['out'], POINTER(UINT64), 'pTotalBytes'),
    ),
    COMMETHOD(
        [helpstring('Method CreateQueryHeap')],
        HRESULT,
        'CreateQueryHeap',
        (['in'], POINTER(D3D12_QUERY_HEAP_DESC), 'pDesc'),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvHeap'),
    ),
    COMMETHOD(
        [helpstring('Method SetStablePowerState')],
        HRESULT,
        'SetStablePowerState',
        ([], BOOL, 'Enable'),
    ),
    COMMETHOD(
        [helpstring('Method CreateCommandSignature')],
        HRESULT,
        'CreateCommandSignature',
        (
            ['in'],
            POINTER(D3D12_COMMAND_SIGNATURE_DESC),
            'pDesc'
        ),
        (
            ['in'],
            POINTER(ID3D12RootSignature),
            'pRootSignature'
        ),
        ([], REFIID, 'riid'),
        (
            ['out'],
            POINTER(POINTER(VOID)),
            'ppvCommandSignature'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetResourceTiling')],
        VOID,
        'GetResourceTiling',
        (['in'], POINTER(ID3D12Resource), 'pTiledResource'),
        (
            ['out'],
            POINTER(UINT),
            'pNumTilesForEntireResource'
        ),
        (
            ['out'],
            POINTER(D3D12_PACKED_MIP_INFO),
            'pPackedMipDesc'
        ),
        (
            ['out'],
            POINTER(D3D12_TILE_SHAPE),
            'pStandardTileShapeForNonPackedMips'
        ),
        (
            ['out', 'in'],
            POINTER(UINT),
            'pNumSubresourceTilings'
        ),
        (['in'], UINT, 'FirstSubresourceTilingToGet'),
        (
            ['out', 'in'],
            POINTER(D3D12_SUBRESOURCE_TILING),
            'pSubresourceTilingsForNonPackedMips'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetAdapterLuid')],
        LUID,
        'GetAdapterLuid',
    ),
]

IID_ID3D12PipelineLibrary = MIDL_INTERFACE(
    "{C64226A8-9201-46AF-B4CC-53FB9FF7414F}"
)
ID3D12PipelineLibrary._iid_ = IID_ID3D12PipelineLibrary


ID3D12PipelineLibrary._methods_ = [
    COMMETHOD(
        [helpstring('Method StorePipeline')],
        HRESULT,
        'StorePipeline',
        (['in'], LPCWSTR, 'pName'),
        (['in'], POINTER(ID3D12PipelineState), 'pPipeline'),
    ),
    COMMETHOD(
        [helpstring('Method LoadGraphicsPipeline')],
        HRESULT,
        'LoadGraphicsPipeline',
        (['in'], LPCWSTR, 'pName'),
        (
            ['in'],
            POINTER(D3D12_GRAPHICS_PIPELINE_STATE_DESC),
            'pDesc'
        ),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppPipelineState'),
    ),
    COMMETHOD(
        [helpstring('Method LoadComputePipeline')],
        HRESULT,
        'LoadComputePipeline',
        (['in'], LPCWSTR, 'pName'),
        (
            ['in'],
            POINTER(D3D12_COMPUTE_PIPELINE_STATE_DESC),
            'pDesc'
        ),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppPipelineState'),
    ),
    COMMETHOD(
        [helpstring('Method GetSerializedSize')],
        SIZE_T,
        'GetSerializedSize',
    ),
    COMMETHOD(
        [helpstring('Method Serialize')],
        HRESULT,
        'Serialize',
        (['out', 'in'], POINTER(VOID), 'pData'),
        ([], SIZE_T, 'DataSizeInBytes'),
    ),
]

IID_ID3D12PipelineLibrary1 = MIDL_INTERFACE(
    "{80EABF42-2568-4E5E-BD82-C37F86961DC3}"
)
ID3D12PipelineLibrary1._iid_ = IID_ID3D12PipelineLibrary1


ID3D12PipelineLibrary1._methods_ = [
    COMMETHOD(
        [helpstring('Method LoadPipeline')],
        HRESULT,
        'LoadPipeline',
        (['in'], LPCWSTR, 'pName'),
        (
            ['in'],
            POINTER(D3D12_PIPELINE_STATE_STREAM_DESC),
            'pDesc'
        ),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppPipelineState'),
    ),
]

class D3D12_MULTIPLE_FENCE_WAIT_FLAGS(ENUM):
    D3D12_MULTIPLE_FENCE_WAIT_FLAG_NONE = 0
    D3D12_MULTIPLE_FENCE_WAIT_FLAG_ANY = 0x1
    D3D12_MULTIPLE_FENCE_WAIT_FLAG_ALL = 0


class D3D12_RESIDENCY_PRIORITY(ENUM):
    D3D12_RESIDENCY_PRIORITY_MINIMUM = 0x28000000
    D3D12_RESIDENCY_PRIORITY_LOW = 0x50000000
    D3D12_RESIDENCY_PRIORITY_NORMAL = 0x78000000
    D3D12_RESIDENCY_PRIORITY_HIGH = 0xA0010000
    D3D12_RESIDENCY_PRIORITY_MAXIMUM = 0xC8000000


IID_ID3D12Device1 = MIDL_INTERFACE(
    "{77ACCE80-638E-4E65-8895-C1F23386863E}"
)
ID3D12Device1._iid_ = IID_ID3D12Device1


ID3D12Device1._methods_ = [
    COMMETHOD(
        [helpstring('Method CreatePipelineLibrary')],
        HRESULT,
        'CreatePipelineLibrary',
        (['in'], POINTER(VOID), 'pLibraryBlob'),
        ([], SIZE_T, 'BlobLength'),
        ([], REFIID, 'riid'),
        (
            ['out'],
            POINTER(POINTER(VOID)),
            'ppPipelineLibrary'
        ),
    ),
    COMMETHOD(
        [helpstring('Method SetEventOnMultipleFenceCompletion')],
        HRESULT,
        'SetEventOnMultipleFenceCompletion',
        (['in'], POINTER(POINTER(ID3D12Fence)), 'ppFences'),
        (['in'], POINTER(UINT64), 'pFenceValues'),
        ([], UINT, 'NumFences'),
        ([], D3D12_MULTIPLE_FENCE_WAIT_FLAGS, 'Flags'),
        ([], HANDLE, 'hEvent'),
    ),
    COMMETHOD(
        [helpstring('Method SetResidencyPriority')],
        HRESULT,
        'SetResidencyPriority',
        ([], UINT, 'NumObjects'),
        (['in'], POINTER(POINTER(ID3D12Pageable)), 'ppObjects'),
        (
            ['in'],
            POINTER(D3D12_RESIDENCY_PRIORITY),
            'pPriorities'
        ),
    ),
]

IID_ID3D12Device2 = MIDL_INTERFACE(
    "{30BAA41E-B15B-475C-A0BB-1AF5C5B64328}"
)
ID3D12Device2._iid_ = IID_ID3D12Device2


ID3D12Device2._methods_ = [
    COMMETHOD(
        [helpstring('Method CreatePipelineState')],
        HRESULT,
        'CreatePipelineState',
        (
            [],
            POINTER(D3D12_PIPELINE_STATE_STREAM_DESC),
            'pDesc'
        ),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppPipelineState'),
    ),
]

class D3D12_RESIDENCY_FLAGS(ENUM):
    D3D12_RESIDENCY_FLAG_NONE = 0
    D3D12_RESIDENCY_FLAG_DENY_OVERBUDGET = 0x1


IID_ID3D12Device3 = MIDL_INTERFACE(
    "{81DADC15-2BAD-4392-93C5-101345C4AA98}"
)
ID3D12Device3._iid_ = IID_ID3D12Device3


ID3D12Device3._methods_ = [
    COMMETHOD(
        [helpstring('Method OpenExistingHeapFromAddress')],
        HRESULT,
        'OpenExistingHeapFromAddress',
        (['in'], POINTER(VOID), 'pAddress'),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvHeap'),
    ),
    COMMETHOD(
        [helpstring('Method OpenExistingHeapFromFileMapping')],
        HRESULT,
        'OpenExistingHeapFromFileMapping',
        (['in'], HANDLE, 'hFileMapping'),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvHeap'),
    ),
    COMMETHOD(
        [helpstring('Method EnqueueMakeResident')],
        HRESULT,
        'EnqueueMakeResident',
        ([], D3D12_RESIDENCY_FLAGS, 'Flags'),
        ([], UINT, 'NumObjects'),
        (['in'], POINTER(POINTER(ID3D12Pageable)), 'ppObjects'),
        (['in'], POINTER(ID3D12Fence), 'pFenceToSignal'),
        ([], UINT64, 'FenceValueToSignal'),
    ),
]

class D3D12_COMMAND_LIST_FLAGS(ENUM):
    D3D12_COMMAND_LIST_FLAG_NONE = 0


class D3D12_COMMAND_POOL_FLAGS(ENUM):
    D3D12_COMMAND_POOL_FLAG_NONE = 0


class D3D12_COMMAND_RECORDER_FLAGS(ENUM):
    D3D12_COMMAND_RECORDER_FLAG_NONE = 0


class D3D12_PROTECTED_SESSION_STATUS(ENUM):
    D3D12_PROTECTED_SESSION_STATUS_OK = 0
    D3D12_PROTECTED_SESSION_STATUS_INVALID = 1


IID_ID3D12ProtectedSession = MIDL_INTERFACE(
    "{A1533D18-0AC1-4084-85B9-89A96116806B}"
)
ID3D12ProtectedSession._iid_ = IID_ID3D12ProtectedSession


ID3D12ProtectedSession._methods_ = [
    COMMETHOD(
        [helpstring('Method GetStatusFence')],
        HRESULT,
        'GetStatusFence',
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppFence'),
    ),
    COMMETHOD(
        [helpstring('Method GetSessionStatus')],
        D3D12_PROTECTED_SESSION_STATUS,
        'GetSessionStatus',
    ),
]

class D3D12_PROTECTED_RESOURCE_SESSION_SUPPORT_FLAGS(ENUM):
    D3D12_PROTECTED_RESOURCE_SESSION_SUPPORT_FLAG_NONE = 0
    D3D12_PROTECTED_RESOURCE_SESSION_SUPPORT_FLAG_SUPPORTED = 0x1

D3D12_FEATURE_DATA_PROTECTED_RESOURCE_SESSION_SUPPORT._fields_ = [
    ('NodeIndex', UINT),
    ('Support', D3D12_PROTECTED_RESOURCE_SESSION_SUPPORT_FLAGS),
]


class D3D12_PROTECTED_RESOURCE_SESSION_FLAGS(ENUM):
    D3D12_PROTECTED_RESOURCE_SESSION_FLAG_NONE = 0

D3D12_PROTECTED_RESOURCE_SESSION_DESC._fields_ = [
    ('NodeMask', UINT),
    ('Flags', D3D12_PROTECTED_RESOURCE_SESSION_FLAGS),
]


IID_ID3D12ProtectedResourceSession = MIDL_INTERFACE(
    "{6CD696F4-F289-40CC-8091-5A6C0A099C3D}"
)
ID3D12ProtectedResourceSession._iid_ = IID_ID3D12ProtectedResourceSession


ID3D12ProtectedResourceSession._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        D3D12_PROTECTED_RESOURCE_SESSION_DESC,
        'GetDesc',
    ),
]

IID_ID3D12Device4 = MIDL_INTERFACE(
    "{E865DF17-A9EE-46F9-A463-3098315AA2E5}"
)
ID3D12Device4._iid_ = IID_ID3D12Device4


ID3D12Device4._methods_ = [
    COMMETHOD(
        [helpstring('Method CreateCommandList1')],
        HRESULT,
        'CreateCommandList1',
        (['in'], UINT, 'nodeMask'),
        (['in'], D3D12_COMMAND_LIST_TYPE, 'type'),
        (['in'], D3D12_COMMAND_LIST_FLAGS, 'flags'),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppCommandList'),
    ),
    COMMETHOD(
        [helpstring('Method CreateProtectedResourceSession')],
        HRESULT,
        'CreateProtectedResourceSession',
        (
            ['in'],
            POINTER(D3D12_PROTECTED_RESOURCE_SESSION_DESC),
            'pDesc'
        ),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppSession'),
    ),
    COMMETHOD(
        [helpstring('Method CreateCommittedResource1')],
        HRESULT,
        'CreateCommittedResource1',
        (
            ['in'],
            POINTER(D3D12_HEAP_PROPERTIES),
            'pHeapProperties'
        ),
        ([], D3D12_HEAP_FLAGS, 'HeapFlags'),
        (['in'], POINTER(D3D12_RESOURCE_DESC), 'pDesc'),
        ([], D3D12_RESOURCE_STATES, 'InitialResourceState'),
        (
            ['in'],
            POINTER(D3D12_CLEAR_VALUE),
            'pOptimizedClearValue'
        ),
        (
            ['in'],
            POINTER(ID3D12ProtectedResourceSession),
            'pProtectedSession'
        ),
        ([], REFIID, 'riidResource'),
        (['out'], POINTER(POINTER(VOID)), 'ppvResource'),
    ),
    COMMETHOD(
        [helpstring('Method CreateHeap1')],
        HRESULT,
        'CreateHeap1',
        (['in'], POINTER(D3D12_HEAP_DESC), 'pDesc'),
        (
            ['in'],
            POINTER(ID3D12ProtectedResourceSession),
            'pProtectedSession'
        ),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvHeap'),
    ),
    COMMETHOD(
        [helpstring('Method CreateReservedResource1')],
        HRESULT,
        'CreateReservedResource1',
        (['in'], POINTER(D3D12_RESOURCE_DESC), 'pDesc'),
        ([], D3D12_RESOURCE_STATES, 'InitialState'),
        (
            ['in'],
            POINTER(D3D12_CLEAR_VALUE),
            'pOptimizedClearValue'
        ),
        (
            ['in'],
            POINTER(ID3D12ProtectedResourceSession),
            'pProtectedSession'
        ),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvResource'),
    ),
    COMMETHOD(
        [helpstring('Method GetResourceAllocationInfo1')],
        D3D12_RESOURCE_ALLOCATION_INFO,
        'GetResourceAllocationInfo1',
        ([], UINT, 'visibleMask'),
        ([], UINT, 'numResourceDescs'),
        (
            ['in'],
            POINTER(D3D12_RESOURCE_DESC),
            'pResourceDescs'
        ),
        (
            ['out'],
            POINTER(D3D12_RESOURCE_ALLOCATION_INFO1),
            'pResourceAllocationInfo1'
        ),
    ),
]

IID_ID3D12Resource1 = MIDL_INTERFACE(
    "{9D5E227A-4430-4161-88B3-3ECA6BB16E19}"
)
ID3D12Resource1._iid_ = IID_ID3D12Resource1


ID3D12Resource1._methods_ = [
    COMMETHOD(
        [helpstring('Method GetProtectedResourceSession')],
        HRESULT,
        'GetProtectedResourceSession',
        ([], REFIID, 'riid'),
        (
            ['out'],
            POINTER(POINTER(VOID)),
            'ppProtectedSession'
        ),
    ),
]

IID_ID3D12Heap1 = MIDL_INTERFACE(
    "{572F7389-2168-49E3-9693-D6DF5871BF6D}"
)
ID3D12Heap1._iid_ = IID_ID3D12Heap1


ID3D12Heap1._methods_ = [
    COMMETHOD(
        [helpstring('Method GetProtectedResourceSession')],
        HRESULT,
        'GetProtectedResourceSession',
        ([], REFIID, 'riid'),
        (
            ['out'],
            POINTER(POINTER(VOID)),
            'ppProtectedSession'
        ),
    ),
]

IID_ID3D12GraphicsCommandList3 = MIDL_INTERFACE(
    "{6FDA83A7-B84C-4E38-9AC8-C7BD22016B3D}"
)
ID3D12GraphicsCommandList3._iid_ = IID_ID3D12GraphicsCommandList3


ID3D12GraphicsCommandList3._methods_ = [
    COMMETHOD(
        [helpstring('Method SetProtectedResourceSession')],
        VOID,
        'SetProtectedResourceSession',
        (
            ['in'],
            POINTER(ID3D12ProtectedResourceSession),
            'pProtectedResourceSession'
        ),
    ),
]

IID_ID3D12Tools = MIDL_INTERFACE(
    "{7071E1F0-E84B-4B33-974F-12FA49DE65C5}"
)
ID3D12Tools._iid_ = IID_ID3D12Tools


ID3D12Tools._methods_ = [
    COMMETHOD(
        [helpstring('Method EnableShaderInstrumentation')],
        VOID,
        'EnableShaderInstrumentation',
        ([], BOOL, 'bEnable'),
    ),
    COMMETHOD(
        [helpstring('Method ShaderInstrumentationEnabled')],
        BOOL,
        'ShaderInstrumentationEnabled',
    ),
]


D3D12_SUBRESOURCE_DATA._fields_ = [
    ('pData', POINTER(VOID)),
    ('RowPitch', LONG_PTR),
    ('SlicePitch', LONG_PTR),
]

D3D12_MEMCPY_DEST._fields_ = [
    ('pData', POINTER(VOID)),
    ('RowPitch', SIZE_T),
    ('SlicePitch', SIZE_T),
]
     
from .d3d12sdklayers_h import * # NOQA


# ///////////////////////////////////////////////////////////////
# D3D12CreateDevice
# ------------------
# pAdapter
# If NULL, D3D12CreateDevice will choose the primary adapter.
# If non-NULL, D3D12CreateDevice will use the provided adapter.
# MinimumFeatureLevel
# The minimum feature level required for successful device creation.
# riid
# The interface IID of the device to be returned. Expected:
# ID3D12Device.
# ppDevice
# Pointer to returned interface. May be NULL.
# Return Values
# Any of those documented for
# CreateDXGIFactory1
# IDXGIFactory::EnumAdapters
# D3D12CreateDevice
# ///////////////////////////////////////////////////////////////
# HRESULT (WINAPI* PFN_D3D12_CREATE_DEVICE)( _In_opt_ IUnknown*, D3D_FEATURE_LEVEL, _In_ REFIID, _COM_Outptr_opt_ VOID** );
PFN_D3D12_CREATE_DEVICE = ctypes.WINFUNCTYPE(
    HRESULT,
    POINTER(comtypes.IUnknown),
    D3D_FEATURE_LEVEL,
    REFIID,
    POINTER(POINTER(VOID)),
)


# HRESULT WINAPI D3D12CreateDevice(
# _In_opt_ IUnknown* pAdapter,
# D3D_FEATURE_LEVEL MinimumFeatureLevel,
# _In_ REFIID riid, // Expected: ID3D12Device
# _COM_Outptr_opt_ VOID** ppDevice );
D3D12CreateDevice = d3d12.D3D12CreateDevice
D3D12CreateDevice.restype = HRESULT

# HRESULT (WINAPI* PFN_D3D12_GET_DEBUG_INTERFACE)( _In_ REFIID, _COM_Outptr_opt_ VOID** );
PFN_D3D12_GET_DEBUG_INTERFACE = ctypes.WINFUNCTYPE(
    HRESULT,
    REFIID,
    POINTER(POINTER(VOID)),
)


# HRESULT WINAPI D3D12GetDebugInterface( _In_ REFIID riid, _COM_Outptr_opt_ VOID** ppvDebug );
D3D12GetDebugInterface = d3d12.D3D12GetDebugInterface
D3D12GetDebugInterface.restype = HRESULT

# ----------------------------------------------------------------------------------------------------------------------
# D3D12EnableExperimentalFeatures
# Pass in a list of feature GUIDs to be enabled together.
# If a particular feature requires some configuration information on
# enablement, it will have
# a configuration struct that can be passed alongside the GUID.
# Some features might use an interface IID as the GUID. For these,
# once the feature is enabled via
# D3D12EnableExperimentalFeatures, D3D12GetDebugInterface can then be
# called with the IID to retrieve the interface
# for manipulating the feature. This allows for control that might not
# cleanly be expressed by just
# the configuration struct that D3D12EnableExperimentalFeatures
# provides.
# If this method is called and a change to existing feature enablement
# is made,
# all current D3D12 devices are set to DEVICE_REMOVED state, since
# under the covers there is really only one
# singleton device for a process. Removing the devices when
# configuration changes prevents
# mismatched expectations of how a device is supposed to work after it
# has been created from the app's point of view.
# The call returns E_NOINTERFACE if an unrecognized feature is passed
# in or Windows Developer mode is not on.
# The call returns E_INVALIDARG if the configuration of a feature is
# incorrect, the set of features passed
# in are known to be incompatible with each other, or other errors.
# Returns S_OK otherwise.
# ----------------------------------------------------------------------------------------------------------------------
# HRESULT WINAPI D3D12EnableExperimentalFeatures(
# UINT                                    NumFeatures,
# __in_ecount(NumFeatures) IID*     pIIDs,
# __in_ecount_opt(NumFeatures) VOID*      pConfigurationStructs,
# __in_ecount_opt(NumFeatures) UINT*      pConfigurationStructSizes);
D3D12EnableExperimentalFeatures = d3d12.D3D12EnableExperimentalFeatures
D3D12EnableExperimentalFeatures.restype = HRESULT

# ----------------------------------------------------------------------------------------------------------------------
# Experimental Feature: D3D12ExperimentalShaderModels
# Use with D3D12EnableExperimentalFeatures to enable experimental
# shader model support,
# meaning shader models that haven't been finalized for use in retail.
# Enabling D3D12ExperimentalShaderModels needs no configuration
# struct, pass NULL in the pConfigurationStructs array.
# ----------------------------------------------------------------------------------------------------------------------        # 76f5573e-f13a-40f5-b297-81ce9e18933f
# ----------------------------------------------------------------------------------------------------------------------
# Experimental Feature: D3D12TiledResourceTier4
# Use with D3D12EnableExperimentalFeatures to enable tiled resource
# tier 4 support,
# meaning texture tile data-inheritance is allowed.
# Enabling D3D12TiledResourceTier4 needs no configuration struct, pass
# NULL in the pConfigurationStructs array.
# ----------------------------------------------------------------------------------------------------------------------        # c9c4725f-a81a-4f56-8c5b-c51039d694fb
# ----------------------------------------------------------------------------------------------------------------------
# Experimental Feature: D3D12MetaCommand
# Use with D3D12EnableExperimentalFeatures to enable the D3D12 Meta
# Command.
# Enabling D3D12MetaCommand needs no configuration struct, pass NULL
# in the pConfigurationStructs array.

IID_ID3D12Object = GUID('{C4FEC28F-7966-4E95-9F94-F431CB56C3B8}')

IID_ID3D12DeviceChild = GUID('{905DB94B-A00C-4140-9DF5-2B64CA9EA357}')

IID_ID3D12RootSignature = GUID('{C54A6B66-72DF-4EE8-8BE5-A946A1429214}')

IID_ID3D12RootSignatureDeserializer = GUID('{34AB647B-3CC8-46AC-841B-C0965645C046}')

IID_ID3D12VersionedRootSignatureDeserializer = GUID('{7F91CE67-90C-4BB7-B78E-ED8FF2E31DA0}')

IID_ID3D12Pageable = GUID('{63EE58FB-1268-4835-86DA-F008CE62F0D6}')

IID_ID3D12Heap = GUID('{6B3B2502-6E51-45B3-90EE-9884265E8DF3}')

IID_ID3D12Resource = GUID('{696442BE-A72E-4059-BC79-5B5C98040FAD}')

IID_ID3D12CommandAllocator = GUID('{6102DEE4-AF59-4B09-B999-B44D73F09B24}')

IID_ID3D12Fence = GUID('{A753DCF-C4D8-4B91-ADF6-BE5A60D95A76}')

IID_ID3D12Fence1 = GUID('{433685FE-E22B-4CA0-A8DB-B5B4F4DD0E4A}')

IID_ID3D12PipelineState = GUID('{765A30F3-F624-4C6F-A828-ACE948622445}')

IID_ID3D12DescriptorHeap = GUID('{8EFB471D-616C-4F49-90F7-127BB763FA51}')

IID_ID3D12QueryHeap = GUID('{D9658AE-ED45-469E-A61D-970EC583CAB4}')

IID_ID3D12CommandSignature = GUID('{C36A797C-EC80-4F0A-8985-A7B2475082D1}')

IID_ID3D12CommandList = GUID('{7116D91C-E7E4-47CE-B8C6-EC8168F437E5}')

IID_ID3D12GraphicsCommandList = GUID('{5B160D0F-AC1B-4185-8BA8-B3AE42A5A455}')

IID_ID3D12GraphicsCommandList1 = GUID('{553103FB-1FE7-4557-BB38-946D7D0E7CA7}')

IID_ID3D12GraphicsCommandList2 = GUID('{38C3E585-FF17-412C-9150-4FC6F9D72A28}')

IID_ID3D12CommandQueue = GUID('{EC870A6-5D7E-4C22-8CFC-5BAAE07616ED}')

IID_ID3D12Device = GUID('{189819F1-1DB6-4B57-BE54-1821339B85F7}')

IID_ID3D12PipelineLibrary = GUID('{C64226A8-9201-46AF-B4CC-53FB9FF7414F}')

IID_ID3D12PipelineLibrary1 = GUID('{80EABF42-2568-4E5E-BD82-C37F86961DC3}')

IID_ID3D12Device1 = GUID('{77ACCE80-638E-4E65-8895-C1F23386863E}')

IID_ID3D12Device2 = GUID('{30BAA41E-B15B-475C-A0BB-1AF5C5B64328}')

IID_ID3D12Device3 = GUID('{81DADC15-2BAD-4392-93C5-101345C4AA98}')

IID_ID3D12ProtectedSession = GUID('{A1533D18-AC1-4084-85B9-89A96116806B}')

IID_ID3D12ProtectedResourceSession = GUID('{6CD696F4-F289-40CC-8091-5A6C0A099C3D}')

IID_ID3D12Device4 = GUID('{E865DF17-A9EE-46F9-A463-3098315AA2E5}')

IID_ID3D12Resource1 = GUID('{9D5E227A-4430-4161-88B3-3ECA6BB16E19}')

IID_ID3D12Heap1 = GUID('{572F7389-2168-49E3-9693-D6DF5871BF6D}')

IID_ID3D12GraphicsCommandList3 = GUID('{6FDA83A7-B84C-4E38-9AC8-C7BD22016B3D}')

IID_ID3D12Tools = GUID('{7071E1F0-E84B-4B33-974F-12FA49DE65C5}')
