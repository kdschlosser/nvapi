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
    RECT
)


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

from .d3dcommon_h import *  # NOQA
from .d3d11_1_h import *  # NOQA
from .d3d11_h import *


class ID3D11DeviceContext2(ID3D11DeviceContext1):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = None


class D3D11_TILED_RESOURCE_COORDINATE(ctypes.Structure):
    pass


class D3D11_TILE_REGION_SIZE(ctypes.Structure):
    pass


class D3D11_SUBRESOURCE_TILING(ctypes.Structure):
    pass


class D3D11_TILE_SHAPE(ctypes.Structure):
    pass


class D3D11_PACKED_MIP_DESC(ctypes.Structure):
    pass


class ID3D11Device2(ID3D11Device1):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


D3D11_TILED_RESOURCE_COORDINATE._fields_ = [
    ('X', UINT),
    ('Y', UINT),
    ('Z', UINT),
    ('Subresource', UINT),
]

D3D11_TILE_REGION_SIZE._fields_ = [
    ('NumTiles', UINT),
    ('bUseBox', BOOL),
    ('Width', UINT),
    ('Height', UINT16),
    ('Depth', UINT16),
]


class D3D11_TILE_MAPPING_FLAG(ENUM):
    D3D11_TILE_MAPPING_NO_OVERWRITE = 0x1


class D3D11_TILE_RANGE_FLAG(ENUM):
    D3D11_TILE_RANGE_NULL = 0x1
    D3D11_TILE_RANGE_SKIP = 0x2
    D3D11_TILE_RANGE_REUSE_SINGLE_TILE = 0x4


D3D11_SUBRESOURCE_TILING._fields_ = [
    ('WidthInTiles', UINT),
    ('HeightInTiles', UINT16),
    ('DepthInTiles', UINT16),
    ('StartTileIndexInOverallResource', UINT),
]

D3D11_TILE_SHAPE._fields_ = [
    ('WidthInTexels', UINT),
    ('HeightInTexels', UINT),
    ('DepthInTexels', UINT),
]

D3D11_PACKED_MIP_DESC._fields_ = [
    ('NumStandardMips', UINT8),
    ('NumPackedMips', UINT8),
    ('NumTilesForPackedMips', UINT),
    ('StartTileIndexInOverallResource', UINT),
]


class D3D11_CHECK_MULTISAMPLE_QUALITY_LEVELS_FLAG(ENUM):
    D3D11_CHECK_MULTISAMPLE_QUALITY_LEVELS_TILED_RESOURCE = 0x1


class D3D11_TILE_COPY_FLAG(ENUM):
    D3D11_TILE_COPY_NO_OVERWRITE = 0x1
    D3D11_TILE_COPY_LINEAR_BUFFER_TO_SWIZZLED_TILED_RESOURCE = 0x2
    D3D11_TILE_COPY_SWIZZLED_TILED_RESOURCE_TO_LINEAR_BUFFER = 0x4


IID_ID3D11DeviceContext2 = MIDL_INTERFACE(
    "{420D5B32-B90C-4DA4-BEF0-359F6A24A83A}"
)
ID3D11DeviceContext2._iid_ = IID_ID3D11DeviceContext2


ID3D11DeviceContext2._methods_ = [
    COMMETHOD(
        [helpstring('Method UpdateTileMappings')],
        HRESULT,
        'UpdateTileMappings',
        (['in'], POINTER(ID3D11Resource), 'pTiledResource'),
        (['in'], UINT, 'NumTiledResourceRegions'),
        (
            ['in'],
            POINTER(D3D11_TILED_RESOURCE_COORDINATE),
            'pTiledResourceRegionStartCoordinates'
        ),
        (
            ['in'],
            POINTER(D3D11_TILE_REGION_SIZE),
            'pTiledResourceRegionSizes'
        ),
        (['in'], POINTER(ID3D11Buffer), 'pTilePool'),
        (['in'], UINT, 'NumRanges'),
        (['in'], POINTER(UINT), 'pRangeFlags'),
        (['in'], POINTER(UINT), 'pTilePoolStartOffsets'),
        (['in'], POINTER(UINT), 'pRangeTileCounts'),
        (['in'], UINT, 'Flags'),
    ),
    COMMETHOD(
        [helpstring('Method CopyTileMappings')],
        HRESULT,
        'CopyTileMappings',
        (['in'], POINTER(ID3D11Resource), 'pDestTiledResource'),
        (
            ['in'],
            POINTER(D3D11_TILED_RESOURCE_COORDINATE),
            'pDestRegionStartCoordinate'
        ),
        (['in'], POINTER(ID3D11Resource), 'pSourceTiledResource'),
        (
            ['in'],
            POINTER(D3D11_TILED_RESOURCE_COORDINATE),
            'pSourceRegionStartCoordinate'
        ),
        (
            ['in'],
            POINTER(D3D11_TILE_REGION_SIZE),
            'pTileRegionSize'
        ),
        (['in'], UINT, 'Flags'),
    ),
    COMMETHOD(
        [helpstring('Method CopyTiles')],
        VOID,
        'CopyTiles',
        (['in'], POINTER(ID3D11Resource), 'pTiledResource'),
        (
            ['in'],
            POINTER(D3D11_TILED_RESOURCE_COORDINATE),
            'pTileRegionStartCoordinate'
        ),
        (
            ['in'],
            POINTER(D3D11_TILE_REGION_SIZE),
            'pTileRegionSize'
        ),
        (['in'], POINTER(ID3D11Buffer), 'pBuffer'),
        (['in'], UINT64, 'BufferStartOffsetInBytes'),
        (['in'], UINT, 'Flags'),
    ),
    COMMETHOD(
        [helpstring('Method UpdateTiles')],
        VOID,
        'UpdateTiles',
        (['in'], POINTER(ID3D11Resource), 'pDestTiledResource'),
        (
            ['in'],
            POINTER(D3D11_TILED_RESOURCE_COORDINATE),
            'pDestTileRegionStartCoordinate'
        ),
        (
            ['in'],
            POINTER(D3D11_TILE_REGION_SIZE),
            'pDestTileRegionSize'
        ),
        (['in'], POINTER(VOID), 'pSourceTileData'),
        (['in'], UINT, 'Flags'),
    ),
    COMMETHOD(
        [helpstring('Method ResizeTilePool')],
        HRESULT,
        'ResizeTilePool',
        (['in'], POINTER(ID3D11Buffer), 'pTilePool'),
        (['in'], UINT64, 'NewSizeInBytes'),
    ),
    COMMETHOD(
        [helpstring('Method TiledResourceBarrier')],
        VOID,
        'TiledResourceBarrier',
        (
            ['in'],
            POINTER(ID3D11DeviceChild),
            'pTiledResourceOrViewAccessBeforeBarrier'
        ),
        (
            ['in'],
            POINTER(ID3D11DeviceChild),
            'pTiledResourceOrViewAccessAfterBarrier'
        ),
    ),
    COMMETHOD(
        [helpstring('Method IsAnnotationEnabled')],
        BOOL,
        'IsAnnotationEnabled',
    ),
    COMMETHOD(
        [helpstring('Method SetMarkerInt')],
        VOID,
        'SetMarkerInt',
        (['in'], LPCWSTR, 'pLabel'),
        ([], INT, 'Data'),
    ),
    COMMETHOD(
        [helpstring('Method BeginEventInt')],
        VOID,
        'BeginEventInt',
        (['in'], LPCWSTR, 'pLabel'),
        ([], INT, 'Data'),
    ),
    COMMETHOD(
        [helpstring('Method EndEvent')],
        VOID,
        'EndEvent',
    ),
]

IID_ID3D11Device2 = MIDL_INTERFACE(
    "{9D06DFFA-D1E5-4D07-83A8-1BB123F2F841}"
)
ID3D11Device2._iid_ = IID_ID3D11Device2


ID3D11Device2._methods_ = [
    COMMETHOD(
        [helpstring('Method GetImmediateContext2')],
        VOID,
        'GetImmediateContext2',
        (
            ['out'],
            POINTER(POINTER(ID3D11DeviceContext2)),
            'ppImmediateContext'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateDeferredContext2')],
        HRESULT,
        'CreateDeferredContext2',
        ([], UINT, 'ContextFlags'),
        (
            ['out'],
            POINTER(POINTER(ID3D11DeviceContext2)),
            'ppDeferredContext'
        ),
    ),
    COMMETHOD(
        [helpstring('Method GetResourceTiling')],
        VOID,
        'GetResourceTiling',
        (['in'], POINTER(ID3D11Resource), 'pTiledResource'),
        (['out'], POINTER(UINT), 'pNumTilesForEntireResource'),
        (
            ['out'],
            POINTER(D3D11_PACKED_MIP_DESC),
            'pPackedMipDesc'
        ),
        (
            ['out'],
            POINTER(D3D11_TILE_SHAPE),
            'pStandardTileShapeForNonPackedMips'
        ),
        (['out', 'in'], POINTER(UINT), 'pNumSubresourceTilings'),
        (['in'], UINT, 'FirstSubresourceTilingToGet'),
        (
            ['out', 'in'],
            POINTER(D3D11_SUBRESOURCE_TILING),
            'pSubresourceTilingsForNonPackedMips'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CheckMultisampleQualityLevels1')],
        HRESULT,
        'CheckMultisampleQualityLevels1',
        (['in'], DXGI_FORMAT, 'Format'),
        (['in'], UINT, 'SampleCount'),
        (['in'], UINT, 'Flags'),
        (['out'], POINTER(UINT), 'pNumQualityLevels'),
    ),
]


IID_ID3D11DeviceContext2 = GUID('{420D5B32-B90C-4DA4-BEF0-359F6A24A83A}')
IID_ID3D11Device2 = GUID('{9D06DFFA-D1E5-4D07-83A8-1BB123F2F841}')

