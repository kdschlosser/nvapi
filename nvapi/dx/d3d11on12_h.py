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
    HMODULE,
    LPCWSTR
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
INT8 = ctypes.c_int8
UINT32 = ctypes.c_uint32


class ENUM(INT):
    pass


class ID3D11On12Device(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = None


class D3D11_RESOURCE_FLAGS(ctypes.Structure):
    pass

    
from .d3d11_h import * # NOQA
from .d3d12_h import * # NOQA
  
# ///////////////////////////////////////////////////////////////
# D3D11On12CreateDevice
# ------------------
# pDevice
# Specifies a pre-existing D3D12 device to use for D3D11 interop.
# May not be NULL.
# Flags
# Any of those documented for D3D11CreateDeviceAndSwapChain.
# pFeatureLevels
# Array of any of the following:
# D3D_FEATURE_LEVEL_12_1
# D3D_FEATURE_LEVEL_12_0
# D3D_FEATURE_LEVEL_11_1
# D3D_FEATURE_LEVEL_11_0
# D3D_FEATURE_LEVEL_10_1
# D3D_FEATURE_LEVEL_10_0
# D3D_FEATURE_LEVEL_9_3
# D3D_FEATURE_LEVEL_9_2
# D3D_FEATURE_LEVEL_9_1
# The first feature level which is less than or equal to the
# D3D12 device's feature level will be used to perform D3D11
# validation.
# Creation will fail if no acceptable feature levels are provided.
# Providing NULL will default to the D3D12 device's feature level.
# FeatureLevels
# Size of feature levels array.
# ppCommandQueues
# Array of unique queues for D3D11On12 to use. Valid queue types:
# 3D command queue.
# Flags must be compatible with device flags, and its NodeMask must
# be a subset of the NodeMask provided to this API.
# NumQueues
# Size of command queue array.
# NodeMask
# Which node of the D3D12 device to use. Only 1 bit may be set.
# ppDevice
# Pointer to returned interface. May be NULL.
# ppImmediateContext
# Pointer to returned interface. May be NULL.
# pChosenFeatureLevel
# Pointer to returned feature level. May be NULL.
# Return Values
# Any of those documented for
# D3D11CreateDevice
# ///////////////////////////////////////////////////////////////
# HRESULT (WINAPI* PFN_D3D11ON12_CREATE_DEVICE)(
# _In_ IUnknown*,
# UINT, 
# _In_reads_opt_( FeatureLevels ) CONST D3D_FEATURE_LEVEL*, 
# UINT FeatureLevels, 
# _In_reads_opt_( NumQueues ) IUnknown* CONST*, 
# UINT NumQueues,
# UINT,
# _COM_Outptr_opt_ ID3D11Device**,
# _COM_Outptr_opt_ ID3D11DeviceContext**,
# _Out_opt_ D3D_FEATURE_LEVEL*
# );
PFN_D3D11ON12_CREATE_DEVICE = ctypes.WINFUNCTYPE(
    HRESULT,
    POINTER(comtypes.IUnknown),
    UINT,
    POINTER(D3D_FEATURE_LEVEL),
    UINT,
    POINTER(POINTER(comtypes.IUnknown)),
    UINT,
    UINT,
    POINTER(POINTER(ID3D11DeviceContext)),
    POINTER(POINTER(ID3D11DeviceContext)),
    POINTER(D3D_FEATURE_LEVEL),
)


D3D11_RESOURCE_FLAGS._fields_ = [
    ('BindFlags', UINT),
    ('MiscFlags', UINT),
    ('CPUAccessFlags', UINT),
    ('StructureByteStride', UINT),
]


IID_ID3D11On12Device = MIDL_INTERFACE(
    "{85611E73-70A9-490E-9614-A9E302777904}"
)
ID3D11On12Device._iid_ = IID_ID3D11On12Device


ID3D11On12Device._methods_ = [
    COMMETHOD(
        [helpstring('Method CreateWrappedResource')],
        HRESULT,
        'CreateWrappedResource',
        (['in'], POINTER(comtypes.IUnknown), 'pResource12'),
        (['in'], POINTER(D3D11_RESOURCE_FLAGS), 'pFlags11'),
        ([], D3D12_RESOURCE_STATES, 'InState'),
        ([], D3D12_RESOURCE_STATES, 'OutState'),
        ([], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppResource11'),
    ),
    COMMETHOD(
        [helpstring('Method ReleaseWrappedResources')],
        VOID,
        'ReleaseWrappedResources',
        (['in'], POINTER(POINTER(ID3D11Resource)), 'ppResources'),
        ([], UINT, 'NumResources'),
    ),
    COMMETHOD(
        [helpstring('Method AcquireWrappedResources')],
        VOID,
        'AcquireWrappedResources',
        (['in'], POINTER(POINTER(ID3D11Resource)), 'ppResources'),
        ([], UINT, 'NumResources'),
    ),
]

       
IID_ID3D11On12Device = GUID('{85611E73-70A9-490E-9614-A9E302777904}')
