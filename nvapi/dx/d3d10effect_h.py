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
from ctypes.wintypes import (
    INT,
    LPCSTR,
    BOOL,
    FLOAT,
    UINT,
    BYTE,
)

from comtypes.GUID import GUID

COMMETHOD = comtypes.COMMETHOD
POINTER = ctypes.POINTER
helpstring = comtypes.helpstring
HRESULT = ctypes.c_long
VOID = ctypes.c_void_p


class ENUM(INT):
    pass


class _D3D10_STATE_BLOCK_MASK(ctypes.Structure):
    pass


D3D10_STATE_BLOCK_MASK = _D3D10_STATE_BLOCK_MASK


class _D3D10_EFFECT_TYPE_DESC(ctypes.Structure):
    pass


D3D10_EFFECT_TYPE_DESC = _D3D10_EFFECT_TYPE_DESC


class _D3D10_EFFECT_VARIABLE_DESC(ctypes.Structure):
    pass


D3D10_EFFECT_VARIABLE_DESC = _D3D10_EFFECT_VARIABLE_DESC


class _D3D10_EFFECT_SHADER_DESC(ctypes.Structure):
    pass


D3D10_EFFECT_SHADER_DESC = _D3D10_EFFECT_SHADER_DESC


class _D3D10_PASS_DESC(ctypes.Structure):
    pass


D3D10_PASS_DESC = _D3D10_PASS_DESC


class _D3D10_PASS_SHADER_DESC(ctypes.Structure):
    pass


D3D10_PASS_SHADER_DESC = _D3D10_PASS_SHADER_DESC


class _D3D10_TECHNIQUE_DESC(ctypes.Structure):
    pass


D3D10_TECHNIQUE_DESC = _D3D10_TECHNIQUE_DESC


class _D3D10_EFFECT_DESC(ctypes.Structure):
    pass


D3D10_EFFECT_DESC = _D3D10_EFFECT_DESC


# ////////////////////////////////////////////////////////////////////////////
# Copyright (c) Microsoft Corporation. All rights reserved.
# File:  D3D10Effect.h
# Content: D3D10 Stateblock/Effect Types & APIs
# ////////////////////////////////////////////////////////////////////////////
from .d3d10_h import * # NOQA

# //////////////////////////////////////////////////////////////////
# File contents:
# 1) Stateblock enums, structs, interfaces, flat APIs
# 2) Effect enums, structs, interfaces, flat APIs
# //////////////////////////////////////////////////////////////////
# ------------------------------------------------------------------
# D3D10_DEVICE_STATE_TYPES:
# Used in ID3D10StateBlockMask function calls
# ------------------------------------------------------------------
class _D3D10_DEVICE_STATE_TYPES(ENUM):
    D3D10_DST_SO_BUFFERS = 1
    D3D10_DST_OM_RENDER_TARGETS = 2
    D3D10_DST_OM_DEPTH_STENCIL_STATE = 3
    D3D10_DST_OM_BLEND_STATE = 4
    D3D10_DST_VS = 5
    D3D10_DST_VS_SAMPLERS = 6
    D3D10_DST_VS_SHADER_RESOURCES = 7
    D3D10_DST_VS_CONSTANT_BUFFERS = 8
    D3D10_DST_GS = 9
    D3D10_DST_GS_SAMPLERS = 10
    D3D10_DST_GS_SHADER_RESOURCES = 11
    D3D10_DST_GS_CONSTANT_BUFFERS = 12
    D3D10_DST_PS = 13
    D3D10_DST_PS_SAMPLERS = 14
    D3D10_DST_PS_SHADER_RESOURCES = 15
    D3D10_DST_PS_CONSTANT_BUFFERS = 16
    D3D10_DST_IA_VERTEX_BUFFERS = 17
    D3D10_DST_IA_INDEX_BUFFER = 18
    D3D10_DST_IA_INPUT_LAYOUT = 19
    D3D10_DST_IA_PRIMITIVE_TOPOLOGY = 20
    D3D10_DST_RS_VIEWPORTS = 21
    D3D10_DST_RS_SCISSOR_RECTS = 22
    D3D10_DST_RS_RASTERIZER_STATE = 23
    D3D10_DST_PREDICATION = 24

D3D10_DEVICE_STATE_TYPES = _D3D10_DEVICE_STATE_TYPES

# ------------------------------------------------------------------
# D3D10_DEVICE_STATE_TYPES:
# Used in ID3D10StateBlockMask function calls
# ------------------------------------------------------------------
def D3D10_BYTES_FROM_BITS(x):
     return (x + 7) // 8


_D3D10_STATE_BLOCK_MASK._fields_ = [
    ('VS', BYTE),
    ('VSSamplers', BYTE * D3D10_BYTES_FROM_BITS(D3D10_COMMONSHADER_SAMPLER_SLOT_COUNT)),
    ('VSShaderResources', BYTE * D3D10_BYTES_FROM_BITS(D3D10_COMMONSHADER_INPUT_RESOURCE_SLOT_COUNT)),
    ('VSConstantBuffers', BYTE * D3D10_BYTES_FROM_BITS(D3D10_COMMONSHADER_CONSTANT_BUFFER_API_SLOT_COUNT)),
    ('GS', BYTE),
    ('GSSamplers', BYTE * D3D10_BYTES_FROM_BITS(D3D10_COMMONSHADER_SAMPLER_SLOT_COUNT)),
    ('GSShaderResources', BYTE * D3D10_BYTES_FROM_BITS(D3D10_COMMONSHADER_INPUT_RESOURCE_SLOT_COUNT)),
    ('GSConstantBuffers', BYTE * D3D10_BYTES_FROM_BITS(D3D10_COMMONSHADER_CONSTANT_BUFFER_API_SLOT_COUNT)),
    ('PS', BYTE),
    ('PSSamplers', BYTE * D3D10_BYTES_FROM_BITS(D3D10_COMMONSHADER_SAMPLER_SLOT_COUNT)),
    ('PSShaderResources', BYTE * D3D10_BYTES_FROM_BITS(D3D10_COMMONSHADER_INPUT_RESOURCE_SLOT_COUNT)),
    ('PSConstantBuffers', BYTE * D3D10_BYTES_FROM_BITS(D3D10_COMMONSHADER_CONSTANT_BUFFER_API_SLOT_COUNT)),
    ('IAVertexBuffers', BYTE * D3D10_BYTES_FROM_BITS(D3D10_IA_VERTEX_INPUT_RESOURCE_SLOT_COUNT)),
    ('IAIndexBuffer', BYTE),
    ('IAInputLayout', BYTE),
    ('IAPrimitiveTopology', BYTE),
    ('OMRenderTargets', BYTE),
    ('OMDepthStencilState', BYTE),
    ('OMBlendState', BYTE),
    ('RSViewports', BYTE),
    ('RSScissorRects', BYTE),
    ('RSRasterizerState', BYTE),
    ('SOBuffers', BYTE),
    ('Predication', BYTE),
]

# //////////////////////////////////////////////////////////////////
# ID3D10StateBlock
# //////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////


# {0803425A-57F5-4dd6-9465-A87570834A08}
IID_ID3D10StateBlock = GUID(
    '{0803425A-57F5-4DD6-9465-A87570834A08}'
)


class ID3D10StateBlock(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10StateBlock
    _idlflags_ = []


LPD3D10STATEBLOCK = POINTER(ID3D10StateBlock)

ID3D10StateBlock._methods_ = [
    comtypes.STDMETHOD(
        VOID,
        'Capture',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'Apply',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'ReleaseAllDeviceObjects',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDevice',
        (POINTER(POINTER(ID3D10Device)),)
    ),
]

# ------------------------------------------------------------------
# D3D10_STATE_BLOCK_MASK and manipulation functions
# -------------------------------------------------
# These functions exist to facilitate working with the
# D3D10_STATE_BLOCK_MASK
# structure.
# D3D10_STATE_BLOCK_MASK *pResult or *pMask
# The state block mask to operate on
# D3D10_STATE_BLOCK_MASK *pA, *pB
# The source state block masks for the binary
# union/intersect/difference
# operations.
# D3D10_DEVICE_STATE_TYPES StateType
# The specific state type to enable/disable/query
# UINT RangeStart, RangeLength, Entry
# The specific bit or range of bits for a given state type to operate
# on.
# Consult the comments for D3D10_DEVICE_STATE_TYPES and
# D3D10_STATE_BLOCK_MASK for information on the valid bit ranges for
# each state.
# ------------------------------------------------------------------
d3d10 = ctypes.windll.D3D10


# HRESULT WINAPI D3D10StateBlockMaskUnion(_In_ D3D10_STATE_BLOCK_MASK *pA, _In_ D3D10_STATE_BLOCK_MASK *pB, _Out_ D3D10_STATE_BLOCK_MASK *pResult);
D3D10StateBlockMaskUnion = d3d10.D3D10StateBlockMaskUnion
D3D10StateBlockMaskUnion.restype = HRESULT


# HRESULT WINAPI D3D10StateBlockMaskIntersect(_In_ D3D10_STATE_BLOCK_MASK *pA, _In_ D3D10_STATE_BLOCK_MASK *pB, _Out_ D3D10_STATE_BLOCK_MASK *pResult);
D3D10StateBlockMaskIntersect = d3d10.D3D10StateBlockMaskIntersect
D3D10StateBlockMaskIntersect.restype = HRESULT


# HRESULT WINAPI D3D10StateBlockMaskDifference(_In_ D3D10_STATE_BLOCK_MASK *pA, _In_ D3D10_STATE_BLOCK_MASK *pB, _Out_ D3D10_STATE_BLOCK_MASK *pResult);
D3D10StateBlockMaskDifference = d3d10.D3D10StateBlockMaskDifference
D3D10StateBlockMaskDifference.restype = HRESULT


# HRESULT WINAPI D3D10StateBlockMaskEnableCapture(_Inout_ D3D10_STATE_BLOCK_MASK *pMask, D3D10_DEVICE_STATE_TYPES StateType, UINT RangeStart, UINT RangeLength);
D3D10StateBlockMaskEnableCapture = (
    d3d10.D3D10StateBlockMaskEnableCapture
)
D3D10StateBlockMaskEnableCapture.restype = HRESULT


# HRESULT WINAPI D3D10StateBlockMaskDisableCapture(_Inout_ D3D10_STATE_BLOCK_MASK *pMask, D3D10_DEVICE_STATE_TYPES StateType, UINT RangeStart, UINT RangeLength);
D3D10StateBlockMaskDisableCapture = (
    d3d10.D3D10StateBlockMaskDisableCapture
)
D3D10StateBlockMaskDisableCapture.restype = HRESULT


# HRESULT WINAPI D3D10StateBlockMaskEnableAll(_Out_ D3D10_STATE_BLOCK_MASK *pMask);
D3D10StateBlockMaskEnableAll = d3d10.D3D10StateBlockMaskEnableAll
D3D10StateBlockMaskEnableAll.restype = HRESULT


# HRESULT WINAPI D3D10StateBlockMaskDisableAll(_Out_ D3D10_STATE_BLOCK_MASK *pMask);
D3D10StateBlockMaskDisableAll = d3d10.D3D10StateBlockMaskDisableAll
D3D10StateBlockMaskDisableAll.restype = HRESULT


# BOOL    WINAPI D3D10StateBlockMaskGetSetting(_In_ D3D10_STATE_BLOCK_MASK *pMask, D3D10_DEVICE_STATE_TYPES StateType, UINT Entry);
D3D10StateBlockMaskGetSetting = d3d10.D3D10StateBlockMaskGetSetting
D3D10StateBlockMaskGetSetting.restype = HRESULT

# ------------------------------------------------------------------
# D3D10CreateStateBlock
# ---------------------
# Creates a state block object based on the mask settings specified
# in a D3D10_STATE_BLOCK_MASK structure.
# ID3D10Device *pDevice
# The device interface to associate with this state block
# D3D10_STATE_BLOCK_MASK *pStateBlockMask
# A bit mask whose settings are used to generate a state block
# object.
# ID3D10StateBlock **ppStateBlock
# The resulting state block object. This object will save/restore
# only those pieces of state that were set in the state block
# bit mask
# ------------------------------------------------------------------
# HRESULT WINAPI D3D10CreateStateBlock(_In_ ID3D10Device *pDevice, _In_ D3D10_STATE_BLOCK_MASK *pStateBlockMask, _Out_ ID3D10StateBlock **ppStateBlock);
D3D10CreateStateBlock = d3d10.D3D10CreateStateBlock
D3D10CreateStateBlock.restype = HRESULT

# ------------------------------------------------------------------
# D3D10_COMPILE & D3D10_EFFECT flags:
# -------------------------------------
# These flags are passed in when creating an effect, and affect
# either compilation behavior or runtime effect behavior
# D3D10_EFFECT_COMPILE_CHILD_EFFECT
# Compile this .fx file to a child effect. Child effects have no
# initializers
# for any shared values as these are initialied in the master effect
# (pool).
# D3D10_EFFECT_COMPILE_ALLOW_SLOW_OPS
# By default, performance mode is enabled. Performance mode disallows
# mutable state objects by preventing non-literal expressions from
# appearing in
# state object definitions. Specifying this flag will disable the mode
# and allow
# for mutable state objects.
# D3D10_EFFECT_SINGLE_THREADED
# Do not attempt to synchronize with other threads loading effects
# into the
# same pool.
# ------------------------------------------------------------------
D3D10_EFFECT_COMPILE_CHILD_EFFECT = 1 << 0
D3D10_EFFECT_COMPILE_ALLOW_SLOW_OPS = 1 << 1
D3D10_EFFECT_SINGLE_THREADED = 1 << 3

# ------------------------------------------------------------------
# D3D10_EFFECT_VARIABLE flags:
# ----------------------------
# These flags describe an effect variable (global or annotation),
# and are returned in D3D10_EFFECT_VARIABLE_DESC::Flags.
# D3D10_EFFECT_VARIABLE_POOLED
# Indicates that the this variable or constant buffer resides
# in an effect pool. If this flag is not set, then the variable resides
# in a standalone effect (if ID3D10Effect::GetPool returns NULL)
# or a child effect (if ID3D10Effect::GetPool returns non-NULL)
# D3D10_EFFECT_VARIABLE_ANNOTATION
# Indicates that this is an annotation on a technique, pass, or global
# variable. Otherwise, this is a global variable. Annotations cannot
# be shared.
# D3D10_EFFECT_VARIABLE_EXPLICIT_BIND_POINT
# Indicates that the variable has been explicitly bound using the
# register keyword.
# ------------------------------------------------------------------
D3D10_EFFECT_VARIABLE_POOLED = 1 << 0
D3D10_EFFECT_VARIABLE_ANNOTATION = 1 << 1
D3D10_EFFECT_VARIABLE_EXPLICIT_BIND_POINT = 1 << 2


D3D10_SHADER_VARIABLE_CLASS = D3D_SHADER_VARIABLE_CLASS

D3D10_SHADER_VARIABLE_TYPE = D3D_SHADER_VARIABLE_TYPE
# //////////////////////////////////////////////////////////////////
# ID3D10EffectType
# //////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////
# ------------------------------------------------------------------
# D3D10_EFFECT_TYPE_DESC:
# Retrieved by ID3D10EffectType::GetDesc()
# ------------------------------------------------------------------
_D3D10_EFFECT_TYPE_DESC._fields_ = [
    # Name of the type
    ('TypeName', LPCSTR),
    # (e.g. scalar, vector, object, etc.)
    ('Class', D3D10_SHADER_VARIABLE_CLASS),
    # (e.g. float, texture, vertexshader, etc.)
    ('Type', D3D10_SHADER_VARIABLE_TYPE),
    # Number of elements in this type
    ('Elements', UINT),
    # Number of members
    ('Members', UINT),
    # Number of rows in this type
    ('Rows', UINT),
    # Number of columns in this type
    ('Columns', UINT),
    # Number of bytes required to represent
    ('PackedSize', UINT),
    # Number of bytes occupied by this data
    ('UnpackedSize', UINT),
    # Number of bytes to seek between elements,
    ('Stride', UINT),
]

# {4E9E1DDC-CD9D-4772-A837-00180B9B88FD}
IID_ID3D10EffectType = GUID(
    '{4E9E1DDC-CD9D-4772-A837-00180B9B88FD}'
)

class ID3D10EffectType(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10EffectType
    _idlflags_ = []


LPD3D10EFFECTTYPE = POINTER(ID3D10EffectType)

ID3D10EffectType._methods_ = [
    comtypes.STDMETHOD(
        BOOL,
        'IsValid',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_EFFECT_TYPE_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectType),
        'GetMemberTypeByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectType),
        'GetMemberTypeByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectType),
        'GetMemberTypeBySemantic',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        LPCSTR,
        'GetMemberName',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        LPCSTR,
        'GetMemberSemantic',
        (UINT,)
    ),
]

# //////////////////////////////////////////////////////////////////
# ID3D10EffectVariable
# //////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////
# ------------------------------------------------------------------
# D3D10_EFFECT_VARIABLE_DESC:
# Retrieved by ID3D10EffectVariable::GetDesc()
# ------------------------------------------------------------------
_D3D10_EFFECT_VARIABLE_DESC._fields_ = [
    # Name of this variable, annotation,
    ('Name', LPCSTR),
    # Semantic string of this variable
    ('Semantic', LPCSTR),
    # D3D10_EFFECT_VARIABLE_* flags
    ('Flags', UINT),
    # Number of annotations on this variable
    ('Annotations', UINT),
    # Offset into containing cbuffer or tbuffer
    ('BufferOffset', UINT),
    # Used if the variable has been explicitly bound
    ('ExplicitBindPoint', UINT),
]


# {AE897105-00E6-45bf-BB8E-281DD6DB8E1B}
IID_ID3D10EffectVariable = GUID(
    '{AE897105-00E6-45bf-BB8E-281DD6DB8E1B}'
)


class ID3D10EffectVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10EffectVariable
    _idlflags_ = []


LPD3D10EFFECTVARIABLE = POINTER(ID3D10EffectVariable)


# Forward defines
class ID3D10EffectScalarVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10EffectVectorVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10EffectMatrixVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10EffectStringVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10EffectShaderResourceVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10EffectRenderTargetViewVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10EffectDepthStencilViewVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10EffectConstantBuffer(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10EffectShaderVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10EffectBlendVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10EffectDepthStencilVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10EffectRasterizerVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class ID3D10EffectSamplerVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


ID3D10EffectVariable._methods_ = [
    comtypes.STDMETHOD(
        BOOL,
        'IsValid',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectType),
        'GetType',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_EFFECT_VARIABLE_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberBySemantic',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetElement',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'GetParentConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectScalarVariable),
        'AsScalar',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVectorVariable),
        'AsVector',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectMatrixVariable),
        'AsMatrix',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectStringVariable),
        'AsString',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderResourceVariable),
        'AsShaderResource',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRenderTargetViewVariable),
        'AsRenderTargetView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilViewVariable),
        'AsDepthStencilView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'AsConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderVariable),
        'AsShader',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectBlendVariable),
        'AsBlend',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilVariable),
        'AsDepthStencil',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRasterizerVariable),
        'AsRasterizer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectSamplerVariable),
        'AsSampler',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
]

# //////////////////////////////////////////////////////////////////
# ID3D10EffectScalarVariable
# ////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////
class ID3D10EffectScalarVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


LPD3D10EFFECTSCALARVARIABLE = POINTER(ID3D10EffectScalarVariable)


# {00E48F7B-D2C8-49e8-A86C-022DEE53431F}
IID_ID3D10EffectScalarVariable = GUID(
    '{00E48F7B-D2C8-49e8-A86C-022DEE53431F}'
)
ID3D10EffectScalarVariable._methods_ = [
    comtypes.STDMETHOD(
        BOOL,
        'IsValid',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectType),
        'GetType',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_EFFECT_VARIABLE_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberBySemantic',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetElement',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'GetParentConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectScalarVariable),
        'AsScalar',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVectorVariable),
        'AsVector',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectMatrixVariable),
        'AsMatrix',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectStringVariable),
        'AsString',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderResourceVariable),
        'AsShaderResource',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRenderTargetViewVariable),
        'AsRenderTargetView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilViewVariable),
        'AsDepthStencilView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'AsConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderVariable),
        'AsShader',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectBlendVariable),
        'AsBlend',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilVariable),
        'AsDepthStencil',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRasterizerVariable),
        'AsRasterizer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectSamplerVariable),
        'AsSampler',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetFloat',
        (FLOAT,)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetFloat',
        (POINTER(FLOAT),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetFloatArray',
        (POINTER(FLOAT), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetFloatArray',
        (POINTER(FLOAT), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetInt',
        (INT,)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetInt',
        (POINTER(INT),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetIntArray',
        (POINTER(INT), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetIntArray',
        (POINTER(INT), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetBool',
        (BOOL,)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetBool',
        (POINTER(BOOL),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetBoolArray',
        (POINTER(BOOL), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetBoolArray',
        (POINTER(BOOL), UINT, UINT)
    ),
]

# //////////////////////////////////////////////////////////////////
# ID3D10EffectVectorVariable
# ////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////

# {62B98C44-1F82-4c67-BCD0-72CF8F217E81}
IID_ID3D10EffectVectorVariable = GUID(
    '{62B98C44-1F82-4c67-BCD0-72CF8F217E81}'
)

class ID3D10EffectVectorVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10EffectVectorVariable
    _idlflags_ = []


LPD3D10EFFECTVECTORVARIABLE = POINTER(ID3D10EffectVectorVariable)


ID3D10EffectVectorVariable._methods_ = [
    comtypes.STDMETHOD(
        BOOL,
        'IsValid',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectType),
        'GetType',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_EFFECT_VARIABLE_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberBySemantic',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetElement',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'GetParentConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectScalarVariable),
        'AsScalar',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVectorVariable),
        'AsVector',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectMatrixVariable),
        'AsMatrix',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectStringVariable),
        'AsString',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderResourceVariable),
        'AsShaderResource',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRenderTargetViewVariable),
        'AsRenderTargetView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilViewVariable),
        'AsDepthStencilView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'AsConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderVariable),
        'AsShader',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectBlendVariable),
        'AsBlend',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilVariable),
        'AsDepthStencil',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRasterizerVariable),
        'AsRasterizer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectSamplerVariable),
        'AsSampler',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetBoolVector',
        (POINTER(BOOL),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetIntVector',
        (POINTER(INT),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetFloatVector',
        (POINTER(FLOAT),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetBoolVector',
        (POINTER(BOOL),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetIntVector',
        (POINTER(INT),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetFloatVector',
        (POINTER(FLOAT),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetBoolVectorArray',
        (POINTER(BOOL), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetIntVectorArray',
        (POINTER(INT), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetFloatVectorArray',
        (POINTER(FLOAT), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetBoolVectorArray',
        (POINTER(BOOL), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetIntVectorArray',
        (POINTER(INT), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetFloatVectorArray',
        (POINTER(FLOAT), UINT, UINT)
    ),
]

# //////////////////////////////////////////////////////////////////
# ID3D10EffectMatrixVariable
# ////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////

# {50666C24-B82F-4eed-A172-5B6E7E8522E0}
IID_ID3D10EffectMatrixVariable = GUID(
    '{50666C24-B82F-4eed-A172-5B6E7E8522E0}'
)

class ID3D10EffectMatrixVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10EffectMatrixVariable
    _idlflags_ = []


LPD3D10EFFECTMATRIXVARIABLE = POINTER(ID3D10EffectMatrixVariable)

ID3D10EffectMatrixVariable._methods_ = [
    comtypes.STDMETHOD(
        BOOL,
        'IsValid',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectType),
        'GetType',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_EFFECT_VARIABLE_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberBySemantic',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetElement',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'GetParentConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectScalarVariable),
        'AsScalar',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVectorVariable),
        'AsVector',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectMatrixVariable),
        'AsMatrix',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectStringVariable),
        'AsString',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderResourceVariable),
        'AsShaderResource',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRenderTargetViewVariable),
        'AsRenderTargetView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilViewVariable),
        'AsDepthStencilView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'AsConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderVariable),
        'AsShader',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectBlendVariable),
        'AsBlend',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilVariable),
        'AsDepthStencil',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRasterizerVariable),
        'AsRasterizer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectSamplerVariable),
        'AsSampler',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetMatrix',
        (POINTER(FLOAT),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetMatrix',
        (POINTER(FLOAT),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetMatrixArray',
        (POINTER(FLOAT), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetMatrixArray',
        (POINTER(FLOAT), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetMatrixTranspose',
        (POINTER(FLOAT),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetMatrixTranspose',
        (POINTER(FLOAT),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetMatrixTransposeArray',
        (POINTER(FLOAT), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetMatrixTransposeArray',
        (POINTER(FLOAT), UINT, UINT)
    ),
]

# //////////////////////////////////////////////////////////////////
# ID3D10EffectStringVariable
# ////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////
# {71417501-8DF9-4e0a-A78A-255F9756BAFF}
IID_ID3D10EffectStringVariable = GUID(
    '{71417501-8DF9-4e0a-A78A-255F9756BAFF}'
)

class ID3D10EffectStringVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10EffectStringVariable
    _idlflags_ = []


LPD3D10EFFECTSTRINGVARIABLE = POINTER(ID3D10EffectStringVariable)


ID3D10EffectStringVariable._methods_ = [
    comtypes.STDMETHOD(
        BOOL,
        'IsValid',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectType),
        'GetType',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_EFFECT_VARIABLE_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberBySemantic',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetElement',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'GetParentConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectScalarVariable),
        'AsScalar',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVectorVariable),
        'AsVector',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectMatrixVariable),
        'AsMatrix',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectStringVariable),
        'AsString',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderResourceVariable),
        'AsShaderResource',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRenderTargetViewVariable),
        'AsRenderTargetView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilViewVariable),
        'AsDepthStencilView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'AsConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderVariable),
        'AsShader',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectBlendVariable),
        'AsBlend',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilVariable),
        'AsDepthStencil',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRasterizerVariable),
        'AsRasterizer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectSamplerVariable),
        'AsSampler',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetString',
        (POINTER(LPCSTR),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetStringArray',
        (POINTER(LPCSTR), UINT, UINT)
    ),
]

# //////////////////////////////////////////////////////////////////
# ID3D10EffectShaderResourceVariable
# ////////////////////////////////////////
# //////////////////////////////////////////////////////////////////

# {C0A7157B-D872-4b1d-8073-EFC2ACD4B1FC}
IID_ID3D10EffectShaderResourceVariable = GUID(
    '{C0A7157B-D872-4b1d-8073-EFC2ACD4B1FC}'
)


class ID3D10EffectShaderResourceVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10EffectShaderResourceVariable
    _idlflags_ = []


LPD3D10EFFECTSHADERRESOURCEVARIABLE = POINTER(ID3D10EffectShaderResourceVariable)


ID3D10EffectShaderResourceVariable._methods_ = [
    comtypes.STDMETHOD(
        BOOL,
        'IsValid',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectType),
        'GetType',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_EFFECT_VARIABLE_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberBySemantic',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetElement',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'GetParentConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectScalarVariable),
        'AsScalar',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVectorVariable),
        'AsVector',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectMatrixVariable),
        'AsMatrix',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectStringVariable),
        'AsString',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderResourceVariable),
        'AsShaderResource',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRenderTargetViewVariable),
        'AsRenderTargetView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilViewVariable),
        'AsDepthStencilView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'AsConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderVariable),
        'AsShader',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectBlendVariable),
        'AsBlend',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilVariable),
        'AsDepthStencil',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRasterizerVariable),
        'AsRasterizer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectSamplerVariable),
        'AsSampler',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetResource',
        (POINTER(ID3D10ShaderResourceView),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetResource',
        (POINTER(POINTER(ID3D10ShaderResourceView)),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetResourceArray',
        (POINTER(POINTER(ID3D10ShaderResourceView)), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetResourceArray',
        (POINTER(POINTER(ID3D10ShaderResourceView)), UINT, UINT)
    ),
]

# //////////////////////////////////////////////////////////////////
# ID3D10EffectRenderTargetViewVariable
# //////////////////////////////////////
# //////////////////////////////////////////////////////////////////

# {28CA0CC3-C2C9-40bb-B57F-67B737122B17}
IID_ID3D10EffectRenderTargetViewVariable = GUID(
    '{28CA0CC3-C2C9-40BB-B57F-67B737122B17}'
)


class ID3D10EffectRenderTargetViewVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10EffectRenderTargetViewVariable
    _idlflags_ = []


LPD3D10EFFECTRENDERTARGETVIEWVARIABLE = POINTER(ID3D10EffectRenderTargetViewVariable)


ID3D10EffectRenderTargetViewVariable._methods_ = [
    comtypes.STDMETHOD(
        BOOL,
        'IsValid',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectType),
        'GetType',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_EFFECT_VARIABLE_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberBySemantic',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetElement',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'GetParentConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectScalarVariable),
        'AsScalar',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVectorVariable),
        'AsVector',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectMatrixVariable),
        'AsMatrix',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectStringVariable),
        'AsString',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderResourceVariable),
        'AsShaderResource',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRenderTargetViewVariable),
        'AsRenderTargetView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilViewVariable),
        'AsDepthStencilView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'AsConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderVariable),
        'AsShader',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectBlendVariable),
        'AsBlend',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilVariable),
        'AsDepthStencil',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRasterizerVariable),
        'AsRasterizer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectSamplerVariable),
        'AsSampler',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetRenderTarget',
        (POINTER(ID3D10RenderTargetView),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetRenderTarget',
        (POINTER(POINTER(ID3D10RenderTargetView)),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetRenderTargetArray',
        (POINTER(POINTER(ID3D10RenderTargetView)), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetRenderTargetArray',
        (POINTER(POINTER(ID3D10RenderTargetView)), UINT, UINT)
    ),
]

# //////////////////////////////////////////////////////////////////
# ID3D10EffectDepthStencilViewVariable
# //////////////////////////////////////
# //////////////////////////////////////////////////////////////////

# {3E02C918-CC79-4985-B622-2D92AD701623}
IID_ID3D10EffectDepthStencilViewVariable = GUID(
    '{3E02C918-CC79-4985-B622-2D92AD701623}'
)

class ID3D10EffectDepthStencilViewVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10EffectDepthStencilViewVariable
    _idlflags_ = []


LPD3D10EFFECTDEPTHSTENCILVIEWVARIABLE = POINTER(ID3D10EffectDepthStencilViewVariable)


ID3D10EffectDepthStencilViewVariable._methods_ = [
    comtypes.STDMETHOD(
        BOOL,
        'IsValid',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectType),
        'GetType',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_EFFECT_VARIABLE_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberBySemantic',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetElement',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'GetParentConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectScalarVariable),
        'AsScalar',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVectorVariable),
        'AsVector',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectMatrixVariable),
        'AsMatrix',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectStringVariable),
        'AsString',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderResourceVariable),
        'AsShaderResource',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRenderTargetViewVariable),
        'AsRenderTargetView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilViewVariable),
        'AsDepthStencilView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'AsConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderVariable),
        'AsShader',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectBlendVariable),
        'AsBlend',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilVariable),
        'AsDepthStencil',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRasterizerVariable),
        'AsRasterizer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectSamplerVariable),
        'AsSampler',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetDepthStencil',
        (POINTER(ID3D10DepthStencilView),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDepthStencil',
        (POINTER(POINTER(ID3D10DepthStencilView)),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetDepthStencilArray',
        (POINTER(POINTER(ID3D10DepthStencilView)), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDepthStencilArray',
        (POINTER(POINTER(ID3D10DepthStencilView)), UINT, UINT)
    ),
]

# //////////////////////////////////////////////////////////////////
# ID3D10EffectConstantBuffer
# ////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////
# {56648F4D-CC8B-4444-A5AD-B5A3D76E91B3}
IID_ID3D10EffectConstantBuffer = GUID(
    '{56648F4D-CC8B-4444-A5AD-B5A3D76E91B3}'
)

class ID3D10EffectConstantBuffer(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10EffectConstantBuffer
    _idlflags_ = []


LPD3D10EFFECTCONSTANTBUFFER = POINTER(ID3D10EffectConstantBuffer)


ID3D10EffectConstantBuffer._methods_ = [
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectType),
        'GetType',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_EFFECT_VARIABLE_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberBySemantic',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetElement',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'GetParentConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectScalarVariable),
        'AsScalar',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVectorVariable),
        'AsVector',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectMatrixVariable),
        'AsMatrix',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectStringVariable),
        'AsString',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderResourceVariable),
        'AsShaderResource',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRenderTargetViewVariable),
        'AsRenderTargetView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilViewVariable),
        'AsDepthStencilView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'AsConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderVariable),
        'AsShader',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectBlendVariable),
        'AsBlend',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilVariable),
        'AsDepthStencil',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRasterizerVariable),
        'AsRasterizer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectSamplerVariable),
        'AsSampler',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetConstantBuffer',
        (POINTER(ID3D10Buffer),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetConstantBuffer',
        (POINTER(POINTER(ID3D10Buffer)),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetTextureBuffer',
        (POINTER(ID3D10ShaderResourceView),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetTextureBuffer',
        (POINTER(POINTER(ID3D10ShaderResourceView)),)
    ),
]

# //////////////////////////////////////////////////////////////////
# ID3D10EffectShaderVariable
# ////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////
# ------------------------------------------------------------------
# D3D10_EFFECT_SHADER_DESC:
# Retrieved by ID3D10EffectShaderVariable::GetShaderDesc()
# ------------------------------------------------------------------
_D3D10_EFFECT_SHADER_DESC._fields_ = [
    # Passed into CreateInputLayout,
    ('pInputSignature', POINTER(BYTE)),
    # Is this an anonymous shader variable
    ('IsInline', BOOL),
    # Shader bytecode
    ('pBytecode', POINTER(BYTE)),
    ('BytecodeLength', UINT),
    # Stream out declaration string (for GS with SO)
    ('SODecl', LPCSTR),
    # Number of entries in the input signature
    ('NumInputSignatureEntries', UINT),
    # Number of entries in the output signature
    ('NumOutputSignatureEntries', UINT),
]

# {80849279-C799-4797-8C33-0407A07D9E06}
IID_ID3D10EffectShaderVariable = GUID(
    '{80849279-C799-4797-8C33-0407A07D9E06}'
)

class ID3D10EffectShaderVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10EffectShaderVariable
    _idlflags_ = []


LPD3D10EFFECTSHADERVARIABLE = POINTER(ID3D10EffectShaderVariable)


ID3D10EffectShaderVariable._methods_ = [
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectType),
        'GetType',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_EFFECT_VARIABLE_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberBySemantic',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetElement',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'GetParentConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectScalarVariable),
        'AsScalar',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVectorVariable),
        'AsVector',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectMatrixVariable),
        'AsMatrix',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectStringVariable),
        'AsString',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderResourceVariable),
        'AsShaderResource',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRenderTargetViewVariable),
        'AsRenderTargetView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilViewVariable),
        'AsDepthStencilView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'AsConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderVariable),
        'AsShader',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectBlendVariable),
        'AsBlend',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilVariable),
        'AsDepthStencil',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRasterizerVariable),
        'AsRasterizer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectSamplerVariable),
        'AsSampler',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetShaderDesc',
        (UINT, POINTER(D3D10_EFFECT_SHADER_DESC))
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetVertexShader',
        (UINT, POINTER(POINTER(ID3D10VertexShader)))
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetGeometryShader',
        (UINT, POINTER(POINTER(ID3D10GeometryShader)))
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetPixelShader',
        (UINT, POINTER(POINTER(ID3D10PixelShader)))
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetInputSignatureElementDesc',
        (UINT, UINT, POINTER(D3D10_SIGNATURE_PARAMETER_DESC))
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetOutputSignatureElementDesc',
        (UINT, UINT, POINTER(D3D10_SIGNATURE_PARAMETER_DESC))
    ),
]

# //////////////////////////////////////////////////////////////////
# ID3D10EffectBlendVariable
# /////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////

# {1FCD2294-DF6D-4eae-86B3-0E9160CFB07B}
IID_ID3D10EffectBlendVariable = GUID(
    '{1FCD2294-DF6D-4EAE-86B3-0E9160CFB07B}'
)
class ID3D10EffectBlendVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10EffectBlendVariable
    _idlflags_ = []


LPD3D10EFFECTBLENDVARIABLE = POINTER(ID3D10EffectBlendVariable)


ID3D10EffectBlendVariable._methods_ = [
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectType),
        'GetType',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_EFFECT_VARIABLE_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberBySemantic',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetElement',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'GetParentConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectScalarVariable),
        'AsScalar',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVectorVariable),
        'AsVector',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectMatrixVariable),
        'AsMatrix',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectStringVariable),
        'AsString',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderResourceVariable),
        'AsShaderResource',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRenderTargetViewVariable),
        'AsRenderTargetView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilViewVariable),
        'AsDepthStencilView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'AsConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderVariable),
        'AsShader',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectBlendVariable),
        'AsBlend',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilVariable),
        'AsDepthStencil',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRasterizerVariable),
        'AsRasterizer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectSamplerVariable),
        'AsSampler',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetBlendState',
        (UINT, POINTER(POINTER(ID3D10BlendState)))
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetBackingStore',
        (UINT, POINTER(D3D10_BLEND_DESC))
    ),
]

# //////////////////////////////////////////////////////////////////
# ID3D10EffectDepthStencilVariable
# //////////////////////////////////////////
# //////////////////////////////////////////////////////////////////

# {AF482368-330A-46a5-9A5C-01C71AF24C8D}
IID_ID3D10EffectDepthStencilVariable = GUID(
    '{AF482368-330A-46A5-9A5C-01C71AF24C8D}'
)

class ID3D10EffectDepthStencilVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10EffectDepthStencilVariable
    _idlflags_ = []


LPD3D10EFFECTDEPTHSTENCILVARIABLE = POINTER(ID3D10EffectDepthStencilVariable)


ID3D10EffectDepthStencilVariable._methods_ = [
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectType),
        'GetType',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_EFFECT_VARIABLE_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberBySemantic',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetElement',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'GetParentConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectScalarVariable),
        'AsScalar',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVectorVariable),
        'AsVector',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectMatrixVariable),
        'AsMatrix',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectStringVariable),
        'AsString',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderResourceVariable),
        'AsShaderResource',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRenderTargetViewVariable),
        'AsRenderTargetView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilViewVariable),
        'AsDepthStencilView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'AsConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderVariable),
        'AsShader',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectBlendVariable),
        'AsBlend',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilVariable),
        'AsDepthStencil',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRasterizerVariable),
        'AsRasterizer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectSamplerVariable),
        'AsSampler',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDepthStencilState',
        (UINT, POINTER(POINTER(ID3D10DepthStencilState)))
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetBackingStore',
        (UINT, POINTER(D3D10_DEPTH_STENCIL_DESC))
    ),
]

# //////////////////////////////////////////////////////////////////
# ID3D10EffectRasterizerVariable
# ////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////

# {21AF9F0E-4D94-4ea9-9785-2CB76B8C0B34}
IID_ID3D10EffectRasterizerVariable = GUID(
    '{21AF9F0E-4D94-4EA9-9785-2CB76B8C0B34}'
)

class ID3D10EffectRasterizerVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10EffectRasterizerVariable
    _idlflags_ = []


LPD3D10EFFECTRASTERIZERVARIABLE = POINTER(ID3D10EffectRasterizerVariable)


ID3D10EffectRasterizerVariable._methods_ = [
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectType),
        'GetType',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_EFFECT_VARIABLE_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberBySemantic',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetElement',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'GetParentConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectScalarVariable),
        'AsScalar',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVectorVariable),
        'AsVector',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectMatrixVariable),
        'AsMatrix',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectStringVariable),
        'AsString',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderResourceVariable),
        'AsShaderResource',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRenderTargetViewVariable),
        'AsRenderTargetView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilViewVariable),
        'AsDepthStencilView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'AsConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderVariable),
        'AsShader',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectBlendVariable),
        'AsBlend',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilVariable),
        'AsDepthStencil',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRasterizerVariable),
        'AsRasterizer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectSamplerVariable),
        'AsSampler',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetRasterizerState',
        (UINT, POINTER(POINTER(ID3D10RasterizerState)))
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetBackingStore',
        (UINT, POINTER(D3D10_RASTERIZER_DESC))
    ),
]

# //////////////////////////////////////////////////////////////////
# ID3D10EffectSamplerVariable
# ///////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////


# {6530D5C7-07E9-4271-A418-E7CE4BD1E480}
IID_ID3D10EffectSamplerVariable = GUID(
    '{6530D5C7-07E9-4271-A418-E7CE4BD1E480}'
)

class ID3D10EffectSamplerVariable(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10EffectSamplerVariable
    _idlflags_ = []


LPD3D10EFFECTSAMPLERVARIABLE = POINTER(ID3D10EffectSamplerVariable)


ID3D10EffectSamplerVariable._methods_ = [
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectType),
        'GetType',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_EFFECT_VARIABLE_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetMemberBySemantic',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetElement',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'GetParentConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectScalarVariable),
        'AsScalar',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVectorVariable),
        'AsVector',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectMatrixVariable),
        'AsMatrix',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectStringVariable),
        'AsString',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderResourceVariable),
        'AsShaderResource',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRenderTargetViewVariable),
        'AsRenderTargetView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilViewVariable),
        'AsDepthStencilView',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'AsConstantBuffer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectShaderVariable),
        'AsShader',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectBlendVariable),
        'AsBlend',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectDepthStencilVariable),
        'AsDepthStencil',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectRasterizerVariable),
        'AsRasterizer',
        ()
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectSamplerVariable),
        'AsSampler',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'SetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetRawValue',
        (POINTER(VOID), UINT, UINT)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetSampler',
        (UINT, POINTER(POINTER(ID3D10SamplerState)))
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetBackingStore',
        (UINT, POINTER(D3D10_SAMPLER_DESC))
    ),
]

# //////////////////////////////////////////////////////////////////
# ID3D10EffectPass
# //////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////
# ------------------------------------------------------------------
# D3D10_PASS_DESC:
# Retrieved by ID3D10EffectPass::GetDesc()
# ------------------------------------------------------------------
_D3D10_PASS_DESC._fields_ = [
    # Name of this pass (NULL if not anonymous)
    ('Name', LPCSTR),
    # Number of annotations on this pass
    ('Annotations', UINT),
    # Signature from VS or GS (if there is no VS)
    ('pIAInputSignature', POINTER(BYTE)),
    # Singature size in bytes
    ('IAInputSignatureSize', SIZE_T),
    # Specified in SetDepthStencilState()
    ('StencilRef', UINT),
    # Specified in SetBlendState()
    ('SampleMask', UINT),
    # Specified in SetBlendState()
    ('BlendFactor', FLOAT * 4),
]

# ------------------------------------------------------------------
# D3D10_PASS_SHADER_DESC:
# Retrieved by ID3D10EffectPass::Get**ShaderDesc()
# ------------------------------------------------------------------
_D3D10_PASS_SHADER_DESC._fields_ = [
    # The variable that this shader came from.
    ('pShaderVariable', POINTER(ID3D10EffectShaderVariable)),
    # The element of pShaderVariable (if an array)
    ('ShaderIndex', UINT),
]

# {5CFBEB89-1A06-46e0-B282-E3F9BFA36A54}
IID_ID3D10EffectPass = GUID(
    '{5CFBEB89-1A06-46E0-B282-E3F9BFA36A54}'
)

class ID3D10EffectPass(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10EffectPass
    _idlflags_ = []


LPD3D10EFFECTPASS = POINTER(ID3D10EffectPass)

ID3D10EffectPass._methods_ = [
    comtypes.STDMETHOD(
        BOOL,
        'IsValid',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_PASS_DESC),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetVertexShaderDesc',
        (POINTER(D3D10_PASS_SHADER_DESC),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetGeometryShaderDesc',
        (POINTER(D3D10_PASS_SHADER_DESC),)
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetPixelShaderDesc',
        (POINTER(D3D10_PASS_SHADER_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        VOID,
        'Apply',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        VOID,
        'ComputeStateBlockMask',
        (POINTER(D3D10_STATE_BLOCK_MASK),)
    ),
]

# //////////////////////////////////////////////////////////////////
# ID3D10EffectTechnique
# /////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////
# ------------------------------------------------------------------
# D3D10_TECHNIQUE_DESC:
# Retrieved by ID3D10EffectTechnique::GetDesc()
# ------------------------------------------------------------------
_D3D10_TECHNIQUE_DESC._fields_ = [
    # Name of this technique (NULL if not anonymous)
    ('Name', LPCSTR),
    # Number of passes contained within
    ('Passes', UINT),
    # Number of annotations on this technique
    ('Annotations', UINT),
]

# {DB122CE8-D1C9-4292-B237-24ED3DE8B175}
IID_ID3D10EffectTechnique = GUID(
    '{DB122CE8-D1C9-4292-B237-24ED3DE8B175}'
)


class ID3D10EffectTechnique(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10EffectTechnique
    _idlflags_ = []


LPD3D10EFFECTTECHNIQUE = POINTER(ID3D10EffectTechnique)


ID3D10EffectTechnique._methods_ = [
    comtypes.STDMETHOD(
        BOOL,
        'IsValid',
        ()
    ),
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_TECHNIQUE_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetAnnotationByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectPass),
        'GetPassByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectPass),
        'GetPassByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        VOID,
        'ComputeStateBlockMask',
        (POINTER(D3D10_STATE_BLOCK_MASK),)
    ),
]

# //////////////////////////////////////////////////////////////////
# ID3D10Effect
# //////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////
# ------------------------------------------------------------------
# D3D10_EFFECT_DESC:
# Retrieved by ID3D10Effect::GetDesc()
# ------------------------------------------------------------------
_D3D10_EFFECT_DESC._fields_ = [
    # TRUE if this is a child effect,
    ('IsChildEffect', BOOL),
    # Number of constant buffers in this effect,
    ('ConstantBuffers', UINT),
    # Number of constant buffers shared in this
    ('SharedConstantBuffers', UINT),
    # Number of global variables in this effect,
    ('GlobalVariables', UINT),
    # Number of global variables shared in this
    ('SharedGlobalVariables', UINT),
    # Number of techniques in this effect,
    ('Techniques', UINT),
]


# {51B0CA8B-EC0B-4519-870D-8EE1CB5017C7}
IID_ID3D10Effect = GUID(
    '{51B0CA8B-EC0B-4519-870D-8EE1CB5017C7}'
)

class ID3D10Effect(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10Effect
    _idlflags_ = []


LPD3D10EFFECT = POINTER(ID3D10Effect)

ID3D10Effect._methods_ = [
    #  IUnknown
    comtypes.STDMETHOD(
        BOOL,
        'IsValid',
        ()
    ),
    comtypes.STDMETHOD(
        BOOL,
        'IsPool',
        ()
    ),
    #  Managing D3D Device
    comtypes.STDMETHOD(
        VOID,
        'GetDevice',
        (POINTER(POINTER(ID3D10Device)),)
    ),
    #  New Reflection APIs
    comtypes.STDMETHOD(
        VOID,
        'GetDesc',
        (POINTER(D3D10_EFFECT_DESC),)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'GetConstantBufferByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectConstantBuffer),
        'GetConstantBufferByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetVariableByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetVariableByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectVariable),
        'GetVariableBySemantic',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectTechnique),
        'GetTechniqueByIndex',
        (UINT,)
    ),
    comtypes.STDMETHOD(
        POINTER(ID3D10EffectTechnique),
        'GetTechniqueByName',
        (LPCSTR,)
    ),
    comtypes.STDMETHOD(
        VOID,
        'Optimize',
        ()
    ),
    comtypes.STDMETHOD(
        BOOL,
        'IsOptimized',
        ()
    ),
]

# //////////////////////////////////////////////////////////////////
# ID3D10EffectPool
# //////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////

# {9537AB04-3250-412e-8213-FCD2F8677933}
IID_ID3D10EffectPool = GUID(
    '{9537AB04-3250-412E-8213-FCD2F8677933}'
)

class ID3D10EffectPool(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_ID3D10EffectPool
    _idlflags_ = []


LPD3D10EFFECTPOOL = POINTER(ID3D10EffectPool)

ID3D10EffectPool._methods_ = [
    #  IUnknown
    comtypes.STDMETHOD(
        POINTER(ID3D10Effect),
        'AsEffect',
        ()
    ),
    #  No public methods
]

# //////////////////////////////////////////////////////////////////
# APIs
# ////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////

# ------------------------------------------------------------------
# D3D10CreateEffectFromXXXX:
# --------------------------
# Creates an effect from a binary effect or file
# Parameters:
# [in]
# pData
# Blob of effect data, either ASCII
# (uncompiled, for D3D10CompileEffectFromMemory) or binary
# (compiled, for D3D10CreateEffect*)
# DataLength
# Length of the data blob
# pSrcFileName
# Name of the ASCII Effect file pData was obtained from
# pDefines
# Optional NULL-terminated array of preprocessor macro definitions.
# pInclude
# Optional interface pointer to use for handling include directives.
# If this parameter is NULL, includes will be honored when compiling
# from file, and will error when compiling from resource or memory.
# HLSLFlags
# Compilation flags pertaining to shaders and data types, honored by
# the HLSL compiler
# FXFlags
# Compilation flags pertaining to Effect compilation, honored
# by the Effect compiler
# pDevice
# Pointer to the D3D10 device on which to create Effect resources
# pEffectPool
# Pointer to an Effect pool to share variables with or NULL
# [out]
# ppEffect
# Address of the newly created Effect interface
# ppEffectPool
# Address of the newly created Effect pool interface
# ppErrors
# If non-NULL, address of a buffer with error messages that occurred
# during parsing or compilation
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# D3D10DisassembleEffect:
# -----------------------
# Takes an effect interface, and returns a buffer containing text
# assembly.
# Parameters:
# pEffect
# Pointer to the runtime effect interface.
# EnableColorCode
# Emit HTML tags for color coding the output?
# ppDisassembly
# Returns a buffer containing the disassembled effect.
# ------------------------------------------------------------------
# HRESULT WINAPI D3D10DisassembleEffect(_In_ ID3D10Effect *pEffect, BOOL EnableColorCode, _Out_ ID3D10Blob **ppDisassembly);
D3D10DisassembleEffect = d3d10.D3D10DisassembleEffect
D3D10DisassembleEffect.restype = HRESULT


