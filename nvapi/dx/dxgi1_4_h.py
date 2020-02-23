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


from dxgi1_3_h import * # NOQA


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



