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

from .dxgi1_3_h import *
from ..utils import *


class DXGI_QUERY_VIDEO_MEMORY_INFO(ctypes.Structure):
    pass


class IDXGISwapChain3(IDXGISwapChain2):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = None

   
class IDXGIOutput4(IDXGIOutput3):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIFactory4(IDXGIFactory3):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIAdapter3(IDXGIAdapter2):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class DXGI_SWAP_CHAIN_COLOR_SPACE_SUPPORT_FLAG(ENUM):
    DXGI_SWAP_CHAIN_COLOR_SPACE_SUPPORT_FLAG_PRESENT = 0x1
    DXGI_SWAP_CHAIN_COLOR_SPACE_SUPPORT_FLAG_OVERLAY_PRESENT = 0x2


IID_IDXGISwapChain3 = MIDL_INTERFACE(
    "{94D99BDB-F1F8-4AB0-B236-7DA0170EDAB1}"
)
IDXGISwapChain3._iid_ = IID_IDXGISwapChain3

IDXGISwapChain3._methods_ = [
    COMMETHOD(
        [helpstring('Method GetCurrentBackBufferIndex')],
        UINT,
        'GetCurrentBackBufferIndex',
    ),
    COMMETHOD(
        [helpstring('Method CheckColorSpaceSupport')],
        HRESULT,
        'CheckColorSpaceSupport',
        (['in'], DXGI_COLOR_SPACE_TYPE, 'ColorSpace'),
        (['out'], POINTER(UINT), 'pColorSpaceSupport'),
    ),
    COMMETHOD(
        [helpstring('Method SetColorSpace1')],
        HRESULT,
        'SetColorSpace1',
        (['in'], DXGI_COLOR_SPACE_TYPE, 'ColorSpace'),
    ),
    COMMETHOD(
        [helpstring('Method ResizeBuffers1')],
        HRESULT,
        'ResizeBuffers1',
        (['in'], UINT, 'BufferCount'),
        (['in'], UINT, 'Width'),
        (['in'], UINT, 'Height'),
        (['in'], DXGI_FORMAT, 'Format'),
        (['in'], UINT, 'SwapChainFlags'),
        (['in'], POINTER(UINT), 'pCreationNodeMask'),
        (['in'], POINTER(comtypes.IUnknown), 'ppPresentQueue'),
    ),
]


class DXGI_OVERLAY_COLOR_SPACE_SUPPORT_FLAG(ENUM):
    DXGI_OVERLAY_COLOR_SPACE_SUPPORT_FLAG_PRESENT = 0x1


IID_IDXGIOutput4 = MIDL_INTERFACE(
    "{DC7DCA35-2196-414D-9F53-617884032A60}"
)
IDXGIOutput4._iid_ = IID_IDXGIOutput4

IDXGIOutput4._methods_ = [
    COMMETHOD(
        [helpstring('Method CheckOverlayColorSpaceSupport')],
        HRESULT,
        'CheckOverlayColorSpaceSupport',
        (['in'], DXGI_FORMAT, 'Format'),
        (['in'], DXGI_COLOR_SPACE_TYPE, 'ColorSpace'),
        (
            ['in'],
            POINTER(comtypes.IUnknown),
            'pConcernedDevice'
        ),
        (['out'], POINTER(UINT), 'pFlags'),
    ),
]

IID_IDXGIFactory4 = MIDL_INTERFACE(
    "{1BC6EA02-EF36-464F-BF0C-21CA39E5168A}"
)
IDXGIFactory4._iid_ = IID_IDXGIFactory4

IDXGIFactory4._methods_ = [
    COMMETHOD(
        [helpstring('Method EnumAdapterByLuid')],
        HRESULT,
        'EnumAdapterByLuid',
        (['in'], LUID, 'AdapterLuid'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvAdapter'),
    ),
    COMMETHOD(
        [helpstring('Method EnumWarpAdapter')],
        HRESULT,
        'EnumWarpAdapter',
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppvAdapter'),
    ),
]

class DXGI_MEMORY_SEGMENT_GROUP(ENUM):
    DXGI_MEMORY_SEGMENT_GROUP_LOCAL = 0
    DXGI_MEMORY_SEGMENT_GROUP_NON_LOCAL = 1


DXGI_QUERY_VIDEO_MEMORY_INFO._fields_ = [
    ('Budget', UINT64),
    ('CurrentUsage', UINT64),
    ('AvailableForReservation', UINT64),
    ('CurrentReservation', UINT64),
]

IID_IDXGIAdapter3 = MIDL_INTERFACE(
    "{645967A4-1392-4310-A798-8053CE3E93FD}"
)
IDXGIAdapter3._iid_ = IID_IDXGIAdapter3

IDXGIAdapter3._methods_ = [
    COMMETHOD(
        [helpstring('Method RegisterHardwareContentProtectionTeardownStatusEvent')],
        HRESULT,
        'RegisterHardwareContentProtectionTeardownStatusEvent',
        (['in'], HANDLE, 'hEvent'),
        (['out'], POINTER(DWORD), 'pdwCookie'),
    ),
    COMMETHOD(
        [helpstring('Method UnregisterHardwareContentProtectionTeardownStatus')],
        VOID,
        'UnregisterHardwareContentProtectionTeardownStatus',
        (['in'], DWORD, 'dwCookie'),
    ),
    COMMETHOD(
        [helpstring('Method QueryVideoMemoryInfo')],
        HRESULT,
        'QueryVideoMemoryInfo',
        (['in'], UINT, 'NodeIndex'),
        (
            ['in'],
            DXGI_MEMORY_SEGMENT_GROUP,
            'MemorySegmentGroup'
        ),
        (
            ['out'],
            POINTER(DXGI_QUERY_VIDEO_MEMORY_INFO),
            'pVideoMemoryInfo'
        ),
    ),
    COMMETHOD(
        [helpstring('Method SetVideoMemoryReservation')],
        HRESULT,
        'SetVideoMemoryReservation',
        (['in'], UINT, 'NodeIndex'),
        (
            ['in'],
            DXGI_MEMORY_SEGMENT_GROUP,
            'MemorySegmentGroup'
        ),
        (['in'], UINT64, 'Reservation'),
    ),
    COMMETHOD(
        [helpstring('Method RegisterVideoMemoryBudgetChangeNotificationEvent')],
        HRESULT,
        'RegisterVideoMemoryBudgetChangeNotificationEvent',
        (['in'], HANDLE, 'hEvent'),
        (['out'], POINTER(DWORD), 'pdwCookie'),
    ),
    COMMETHOD(
        [helpstring('Method UnregisterVideoMemoryBudgetChangeNotification')],
        VOID,
        'UnregisterVideoMemoryBudgetChangeNotification',
        (['in'], DWORD, 'dwCookie'),
    ),
]

IID_IDXGISwapChain3 = GUID('{94D99BDB-F1F8-4AB0-B236-7DA0170EDAB1}')

IID_IDXGIOutput4 = GUID('{DC7DCA35-2196-414D-9F53-617884032A60}')

IID_IDXGIFactory4 = GUID('{1BC6EA02-EF36-464F-BF0C-21CA39E5168A}')

IID_IDXGIAdapter3 = GUID('{645967A4-1392-4310-A798-8053CE3E93FD}')



