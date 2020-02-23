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



IID_IDXGIObject = MIDL_INTERFACE(
    "{AEC22FB8-76F3-4639-9BE0-28EB43A67A2E}"
)


class IDXGIObject(comtypes.IUnknown):
    _case_insensitive_ = True
    _idlflags_ = []
    _iid_ = IID_IDXGIObject



class DXGI_FRAME_STATISTICS(ctypes.Structure):
    pass


class DXGI_MAPPED_RECT(ctypes.Structure):
    pass


class _LUID(ctypes.Structure):
    pass


LUID = _LUID


class DXGI_ADAPTER_DESC(ctypes.Structure):
    pass


class DXGI_OUTPUT_DESC(ctypes.Structure):
    pass


class DXGI_SHARED_RESOURCE(ctypes.Structure):
    pass


class DXGI_SURFACE_DESC(ctypes.Structure):
    pass


class DXGI_SWAP_CHAIN_DESC(ctypes.Structure):
    pass


class DXGI_ADAPTER_DESC1(ctypes.Structure):
    pass


class DXGI_DISPLAY_COLOR_SPACE(ctypes.Structure):
    pass



class IDXGIDeviceSubObject(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIResource(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIKeyedMutex(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGISurface(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGISurface1(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIAdapter(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIOutput(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []

   
class IDXGISwapChain(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIFactory(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []

   
class IDXGIDevice(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []



class IDXGIFactory1(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIAdapter1(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


class IDXGIDevice1(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = None
    _idlflags_ = []


from .dxgicommon_h import * # NOQA
from .dxgitype_h import * # NOQA


DXGI_USAGE = UINT

DXGI_FRAME_STATISTICS._fields_ = [
    ('PresentCount', UINT),
    ('PresentRefreshCount', UINT),
    ('SyncRefreshCount', UINT),
    ('SyncQPCTime', LARGE_INTEGER),
    ('SyncGPUTime', LARGE_INTEGER),
]

DXGI_MAPPED_RECT._fields_ = [
    ('Pitch', INT),
    ('pBits', POINTER(BYTE)),
]

_LUID._fields_ = [
    ('LowPart', DWORD),
    ('HighPart', LONG),
]
PLUID = POINTER(_LUID)

DXGI_ADAPTER_DESC._fields_ = [
    ('Description', WCHAR * 128),
    ('VendorId', UINT),
    ('DeviceId', UINT),
    ('SubSysId', UINT),
    ('Revision', UINT),
    ('DedicatedVideoMemory', SIZE_T),
    ('DedicatedSystemMemory', SIZE_T),
    ('SharedSystemMemory', SIZE_T),
    ('AdapterLuid', LUID),
]

HMONITOR = HANDLE


DXGI_OUTPUT_DESC._fields_ = [
    ('DeviceName', WCHAR * 32),
    ('DesktopCoordinates', RECT),
    ('AttachedToDesktop', BOOL),
    ('Rotation', DXGI_MODE_ROTATION),
    ('Monitor', HMONITOR),
]

DXGI_SHARED_RESOURCE._fields_ = [
    ('Handle', HANDLE),
]


class DXGI_RESIDENCY(ENUM):
    DXGI_RESIDENCY_FULLY_RESIDENT = 1
    DXGI_RESIDENCY_RESIDENT_IN_SHARED_MEMORY = 2
    DXGI_RESIDENCY_EVICTED_TO_DISK = 3

DXGI_SURFACE_DESC._fields_ = [
    ('Width', UINT),
    ('Height', UINT),
    ('Format', DXGI_FORMAT),
    ('SampleDesc', DXGI_SAMPLE_DESC),
]


class DXGI_SWAP_EFFECT(ENUM):
    DXGI_SWAP_EFFECT_DISCARD = 0
    DXGI_SWAP_EFFECT_SEQUENTIAL = 1
    DXGI_SWAP_EFFECT_FLIP_SEQUENTIAL = 3
    DXGI_SWAP_EFFECT_FLIP_DISCARD = 4


class DXGI_SWAP_CHAIN_FLAG(ENUM):
    DXGI_SWAP_CHAIN_FLAG_NONPREROTATED = 1
    DXGI_SWAP_CHAIN_FLAG_ALLOW_MODE_SWITCH = 2
    DXGI_SWAP_CHAIN_FLAG_GDI_COMPATIBLE = 4
    DXGI_SWAP_CHAIN_FLAG_RESTRICTED_CONTENT = 8
    DXGI_SWAP_CHAIN_FLAG_RESTRICT_SHARED_RESOURCE_DRIVER = 16
    DXGI_SWAP_CHAIN_FLAG_DISPLAY_ONLY = 32
    DXGI_SWAP_CHAIN_FLAG_FRAME_LATENCY_WAITABLE_OBJECT = 64
    DXGI_SWAP_CHAIN_FLAG_FOREGROUND_LAYER = 128
    DXGI_SWAP_CHAIN_FLAG_FULLSCREEN_VIDEO = 256
    DXGI_SWAP_CHAIN_FLAG_YUV_VIDEO = 512
    DXGI_SWAP_CHAIN_FLAG_HW_PROTECTED = 1024
    DXGI_SWAP_CHAIN_FLAG_ALLOW_TEARING = 2048
    DXGI_SWAP_CHAIN_FLAG_RESTRICTED_TO_ALL_HOLOGRAPHIC_DISPLAYS = 4096

DXGI_SWAP_CHAIN_DESC._fields_ = [
    ('BufferDesc', DXGI_MODE_DESC),
    ('SampleDesc', DXGI_SAMPLE_DESC),
    ('BufferUsage', DXGI_USAGE),
    ('BufferCount', UINT),
    ('OutputWindow', HWND),
    ('Windowed', BOOL),
    ('SwapEffect', DXGI_SWAP_EFFECT),
    ('Flags', UINT),
]

IID_IDXGIObject = MIDL_INTERFACE(
    "{AEC22FB8-76F3-4639-9BE0-28EB43A67A2E}"
)
IDXGIObject._iid_ = IID_IDXGIObject


IDXGIObject._methods_ = [
    COMMETHOD(
        [helpstring('Method SetPrivateData')],
        HRESULT,
        'SetPrivateData',
        (['in'], REFGUID, 'Name'),
        (['in'], UINT, 'DataSize'),
        (['in'], POINTER(VOID), 'pData'),
    ),
    COMMETHOD(
        [helpstring('Method SetPrivateDataInterface')],
        HRESULT,
        'SetPrivateDataInterface',
        (['in'], REFGUID, 'Name'),
        (['in'], POINTER(comtypes.IUnknown), 'pUnknown'),
    ),
    COMMETHOD(
        [helpstring('Method GetPrivateData')],
        HRESULT,
        'GetPrivateData',
        (['in'], REFGUID, 'Name'),
        (['out', 'in'], POINTER(UINT), 'pDataSize'),
        (['out'], POINTER(VOID), 'pData'),
    ),
    COMMETHOD(
        [helpstring('Method GetParent')],
        HRESULT,
        'GetParent',
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppParent'),
    ),
]

IID_IDXGIDeviceSubObject = MIDL_INTERFACE(
    "{3D3E0379-F9DE-4D58-BB6C-18D62992F1A6}"
)
IDXGIDeviceSubObject._iid_ = IID_IDXGIDeviceSubObject


IDXGIDeviceSubObject._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDevice')],
        HRESULT,
        'GetDevice',
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppDevice'),
    ),
]

IID_IDXGIResource = MIDL_INTERFACE(
    "{035F3AB4-482E-4E50-B41F-8A7F8BD8960B}"
)
IDXGIResource._iid_ = IID_IDXGIResource


IDXGIResource._methods_ = [
    COMMETHOD(
        [helpstring('Method GetSharedHandle')],
        HRESULT,
        'GetSharedHandle',
        (['out'], POINTER(HANDLE), 'pSharedHandle'),
    ),
    COMMETHOD(
        [helpstring('Method GetUsage')],
        HRESULT,
        'GetUsage',
        (['out'], POINTER(DXGI_USAGE), 'pUsage'),
    ),
    COMMETHOD(
        [helpstring('Method SetEvictionPriority')],
        HRESULT,
        'SetEvictionPriority',
        (['in'], UINT, 'EvictionPriority'),
    ),
    COMMETHOD(
        [helpstring('Method GetEvictionPriority')],
        HRESULT,
        'GetEvictionPriority',
        (['out'], POINTER(UINT), 'pEvictionPriority'),
    ),
]

IID_IDXGIKeyedMutex = MIDL_INTERFACE(
    "{9D8E1289-D7B3-465F-8126-250E349AF85D}"
)
IDXGIKeyedMutex._iid_ = IID_IDXGIKeyedMutex


IDXGIKeyedMutex._methods_ = [
    COMMETHOD(
        [helpstring('Method AcquireSync')],
        HRESULT,
        'AcquireSync',
        (['in'], UINT64, 'Key'),
        (['in'], DWORD, 'dwMilliseconds'),
    ),
    COMMETHOD(
        [helpstring('Method ReleaseSync')],
        HRESULT,
        'ReleaseSync',
        (['in'], UINT64, 'Key'),
    ),
]

IID_IDXGISurface = MIDL_INTERFACE(
    "{CAFCB56C-6AC3-4889-BF47-9E23BBD260EC}"
)
IDXGISurface._iid_ = IID_IDXGISurface


IDXGISurface._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        HRESULT,
        'GetDesc',
        (['out'], POINTER(DXGI_SURFACE_DESC), 'pDesc'),
    ),
    COMMETHOD(
        [helpstring('Method Map')],
        HRESULT,
        'Map',
        (['out'], POINTER(DXGI_MAPPED_RECT), 'pLockedRect'),
        (['in'], UINT, 'MapFlags'),
    ),
    COMMETHOD(
        [helpstring('Method Unmap')],
        HRESULT,
        'Unmap',
    ),
]

IID_IDXGISurface1 = MIDL_INTERFACE(
    "{4AE63092-6327-4C1B-80AE-BFE12EA32B86}"
)
IDXGISurface1._iid_ = IID_IDXGISurface1


IDXGISurface1._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDC')],
        HRESULT,
        'GetDC',
        (['in'], BOOL, 'Discard'),
        (['out'], POINTER(HDC), 'phdc'),
    ),
    COMMETHOD(
        [helpstring('Method ReleaseDC')],
        HRESULT,
        'ReleaseDC',
        (['in'], POINTER(RECT), 'pDirtyRect'),
    ),
]

IID_IDXGIAdapter = MIDL_INTERFACE(
    "{2411E7E1-12AC-4CCF-BD14-9798E8534DC0}"
)
IDXGIAdapter._iid_ = IID_IDXGIAdapter


IDXGIAdapter._methods_ = [
    COMMETHOD(
        [helpstring('Method EnumOutputs')],
        HRESULT,
        'EnumOutputs',
        (['in'], UINT, 'Output'),
        (['out'], POINTER(POINTER(IDXGIOutput)), 'ppOutput'),
    ),
    COMMETHOD(
        [helpstring('Method GetDesc')],
        HRESULT,
        'GetDesc',
        (['out'], POINTER(DXGI_ADAPTER_DESC), 'pDesc'),
    ),
    COMMETHOD(
        [helpstring('Method CheckInterfaceSupport')],
        HRESULT,
        'CheckInterfaceSupport',
        (['in'], REFGUID, 'InterfaceName'),
        (['out'], POINTER(LARGE_INTEGER), 'pUMDVersion'),
    ),
]

IID_IDXGIOutput = MIDL_INTERFACE(
    "{AE02EEDB-C735-4690-8D52-5A8DC20213AA}"
)
IDXGIOutput._iid_ = IID_IDXGIOutput


IDXGIOutput._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc')],
        HRESULT,
        'GetDesc',
        (['out'], POINTER(DXGI_OUTPUT_DESC), 'pDesc'),
    ),
    COMMETHOD(
        [helpstring('Method GetDisplayModeList')],
        HRESULT,
        'GetDisplayModeList',
        (['in'], DXGI_FORMAT, 'EnumFormat'),
        (['in'], UINT, 'Flags'),
        (['out', 'in'], POINTER(UINT), 'pNumModes'),
        (['out'], POINTER(DXGI_MODE_DESC), 'pDesc'),
    ),
    COMMETHOD(
        [helpstring('Method FindClosestMatchingMode')],
        HRESULT,
        'FindClosestMatchingMode',
        (['in'], POINTER(DXGI_MODE_DESC), 'pModeToMatch'),
        (['out'], POINTER(DXGI_MODE_DESC), 'pClosestMatch'),
        (['in'], POINTER(comtypes.IUnknown), 'pConcernedDevice'),
    ),
    COMMETHOD(
        [helpstring('Method WaitForVBlank')],
        HRESULT,
        'WaitForVBlank',
    ),
    COMMETHOD(
        [helpstring('Method TakeOwnership')],
        HRESULT,
        'TakeOwnership',
        (['in'], POINTER(comtypes.IUnknown), 'pDevice'),
        ([], BOOL, 'Exclusive'),
    ),
    COMMETHOD(
        [helpstring('Method ReleaseOwnership')],
        VOID,
        'ReleaseOwnership',
    ),
    COMMETHOD(
        [helpstring('Method GetGammaControlCapabilities')],
        HRESULT,
        'GetGammaControlCapabilities',
        (
            ['out'],
            POINTER(DXGI_GAMMA_CONTROL_CAPABILITIES),
            'pGammaCaps'
        ),
    ),
    COMMETHOD(
        [helpstring('Method SetGammaControl')],
        HRESULT,
        'SetGammaControl',
        (['in'], POINTER(DXGI_GAMMA_CONTROL), 'pArray'),
    ),
    COMMETHOD(
        [helpstring('Method GetGammaControl')],
        HRESULT,
        'GetGammaControl',
        (['out'], POINTER(DXGI_GAMMA_CONTROL), 'pArray'),
    ),
    COMMETHOD(
        [helpstring('Method SetDisplaySurface')],
        HRESULT,
        'SetDisplaySurface',
        (['in'], POINTER(IDXGISurface), 'pScanoutSurface'),
    ),
    COMMETHOD(
        [helpstring('Method GetDisplaySurfaceData')],
        HRESULT,
        'GetDisplaySurfaceData',
        (['in'], POINTER(IDXGISurface), 'pDestination'),
    ),
    COMMETHOD(
        [helpstring('Method GetFrameStatistics')],
        HRESULT,
        'GetFrameStatistics',
        (['out'], POINTER(DXGI_FRAME_STATISTICS), 'pStats'),
    ),
]

IID_IDXGISwapChain = MIDL_INTERFACE(
    "{310D36A0-D2E7-4C0A-AA04-6A9D23B8886A}"
)
IDXGISwapChain._iid_ = IID_IDXGISwapChain


IDXGISwapChain._methods_ = [
    COMMETHOD(
        [helpstring('Method Present')],
        HRESULT,
        'Present',
        (['in'], UINT, 'SyncInterval'),
        (['in'], UINT, 'Flags'),
    ),
    COMMETHOD(
        [helpstring('Method GetBuffer')],
        HRESULT,
        'GetBuffer',
        (['in'], UINT, 'Buffer'),
        (['in'], REFIID, 'riid'),
        (['out'], POINTER(POINTER(VOID)), 'ppSurface'),
    ),
    COMMETHOD(
        [helpstring('Method SetFullscreenState')],
        HRESULT,
        'SetFullscreenState',
        (['in'], BOOL, 'Fullscreen'),
        (['in'], POINTER(IDXGIOutput), 'pTarget'),
    ),
    COMMETHOD(
        [helpstring('Method GetFullscreenState')],
        HRESULT,
        'GetFullscreenState',
        (['out'], POINTER(BOOL), 'pFullscreen'),
        (['out'], POINTER(POINTER(IDXGIOutput)), 'ppTarget'),
    ),
    COMMETHOD(
        [helpstring('Method GetDesc')],
        HRESULT,
        'GetDesc',
        (['out'], POINTER(DXGI_SWAP_CHAIN_DESC), 'pDesc'),
    ),
    COMMETHOD(
        [helpstring('Method ResizeBuffers')],
        HRESULT,
        'ResizeBuffers',
        (['in'], UINT, 'BufferCount'),
        (['in'], UINT, 'Width'),
        (['in'], UINT, 'Height'),
        (['in'], DXGI_FORMAT, 'NewFormat'),
        (['in'], UINT, 'SwapChainFlags'),
    ),
    COMMETHOD(
        [helpstring('Method ResizeTarget')],
        HRESULT,
        'ResizeTarget',
        (['in'], POINTER(DXGI_MODE_DESC), 'pNewTargetParameters'),
    ),
    COMMETHOD(
        [helpstring('Method GetContainingOutput')],
        HRESULT,
        'GetContainingOutput',
        (['out'], POINTER(POINTER(IDXGIOutput)), 'ppOutput'),
    ),
    COMMETHOD(
        [helpstring('Method GetFrameStatistics')],
        HRESULT,
        'GetFrameStatistics',
        (['out'], POINTER(DXGI_FRAME_STATISTICS), 'pStats'),
    ),
    COMMETHOD(
        [helpstring('Method GetLastPresentCount')],
        HRESULT,
        'GetLastPresentCount',
        (['out'], POINTER(UINT), 'pLastPresentCount'),
    ),
]

IID_IDXGIFactory = MIDL_INTERFACE(
    "{7B7166EC-21C7-44AE-B21A-C9AE321AE369}"
)
IDXGIFactory._iid_ = IID_IDXGIFactory


IDXGIFactory._methods_ = [
    COMMETHOD(
        [helpstring('Method EnumAdapters')],
        HRESULT,
        'EnumAdapters',
        (['in'], UINT, 'Adapter'),
        (['out'], POINTER(POINTER(IDXGIAdapter)), 'ppAdapter'),
    ),
    COMMETHOD(
        [helpstring('Method MakeWindowAssociation')],
        HRESULT,
        'MakeWindowAssociation',
        (['in'], HWND, 'WindowHandle'),
        (['in'], UINT, 'Flags'),
    ),
    COMMETHOD(
        [helpstring('Method GetWindowAssociation')],
        HRESULT,
        'GetWindowAssociation',
        (['out'], POINTER(HWND), 'pWindowHandle'),
    ),
    COMMETHOD(
        [helpstring('Method CreateSwapChain')],
        HRESULT,
        'CreateSwapChain',
        (['in'], POINTER(comtypes.IUnknown), 'pDevice'),
        (['in'], POINTER(DXGI_SWAP_CHAIN_DESC), 'pDesc'),
        (
            ['out'],
            POINTER(POINTER(IDXGISwapChain)),
            'ppSwapChain'
        ),
    ),
    COMMETHOD(
        [helpstring('Method CreateSoftwareAdapter')],
        HRESULT,
        'CreateSoftwareAdapter',
        (['in'], HMODULE, 'Module'),
        (['out'], POINTER(POINTER(IDXGIAdapter)), 'ppAdapter'),
    ),
]

dxgi = ctypes.windll.DXGI

# HRESULT WINAPI CreateDXGIFactory(REFIID riid, _COM_Outptr_ VOID **ppFactory);
CreateDXGIFactory = dxgi.CreateDXGIFactory
CreateDXGIFactory.restype = HRESULT

# HRESULT WINAPI CreateDXGIFactory1(REFIID riid, _COM_Outptr_ VOID **ppFactory);
CreateDXGIFactory1 = dxgi.CreateDXGIFactory1
CreateDXGIFactory1.restype = HRESULT

IID_IDXGIDevice = MIDL_INTERFACE(
    "{54EC77FA-1377-44E6-8C32-88FD5F44C84C}"
)
IDXGIDevice._iid_ = IID_IDXGIDevice


IDXGIDevice._methods_ = [
    COMMETHOD(
        [helpstring('Method GetAdapter')],
        HRESULT,
        'GetAdapter',
        (['out'], POINTER(POINTER(IDXGIAdapter)), 'pAdapter'),
    ),
    COMMETHOD(
        [helpstring('Method CreateSurface')],
        HRESULT,
        'CreateSurface',
        (['in'], POINTER(DXGI_SURFACE_DESC), 'pDesc'),
        (['in'], UINT, 'NumSurfaces'),
        (['in'], DXGI_USAGE, 'Usage'),
        (
            ['in'],
            POINTER(DXGI_SHARED_RESOURCE),
            'pSharedResource'
        ),
        (['out'], POINTER(POINTER(IDXGISurface)), 'ppSurface'),
    ),
    COMMETHOD(
        [helpstring('Method QueryResourceResidency')],
        HRESULT,
        'QueryResourceResidency',
        (['in'], POINTER(comtypes.IUnknown), 'ppResources'),
        (['out'], POINTER(DXGI_RESIDENCY), 'pResidencyStatus'),
        (['in'], UINT, 'NumResources'),
    ),
    COMMETHOD(
        [helpstring('Method SetGPUThreadPriority')],
        HRESULT,
        'SetGPUThreadPriority',
        (['in'], INT, 'Priority'),
    ),
    COMMETHOD(
        [helpstring('Method GetGPUThreadPriority')],
        HRESULT,
        'GetGPUThreadPriority',
        (['out'], POINTER(INT), 'pPriority'),
    ),
]

class DXGI_ADAPTER_FLAG(ENUM):
    DXGI_ADAPTER_FLAG_NONE = 0
    DXGI_ADAPTER_FLAG_REMOTE = 1
    DXGI_ADAPTER_FLAG_SOFTWARE = 2
    DXGI_ADAPTER_FLAG_FORCE_DWORD = 0xFFFFFFFF

DXGI_ADAPTER_DESC1._fields_ = [
    ('Description', WCHAR * 128),
    ('VendorId', UINT),
    ('DeviceId', UINT),
    ('SubSysId', UINT),
    ('Revision', UINT),
    ('DedicatedVideoMemory', SIZE_T),
    ('DedicatedSystemMemory', SIZE_T),
    ('SharedSystemMemory', SIZE_T),
    ('AdapterLuid', LUID),
    ('Flags', UINT),
]

DXGI_DISPLAY_COLOR_SPACE._fields_ = [
    ('PrimaryCoordinates', (FLOAT * 8)(FLOAT * 2)),
    ('WhitePoints', (FLOAT * 16)(FLOAT * 2)),
]


IID_IDXGIFactory1 = MIDL_INTERFACE(
    "{770AAE78-F26F-4DBA-A829-253C83D1B387}"
)
IDXGIFactory1._iid_ = IID_IDXGIFactory1


IDXGIFactory1._methods_ = [
    COMMETHOD(
        [helpstring('Method EnumAdapters1')],
        HRESULT,
        'EnumAdapters1',
        (['in'], UINT, 'Adapter'),
        (['out'], POINTER(POINTER(IDXGIAdapter1)), 'ppAdapter'),
    ),
    COMMETHOD(
        [helpstring('Method IsCurrent')],
        BOOL,
        'IsCurrent',
    ),
]

IID_IDXGIAdapter1 = MIDL_INTERFACE(
    "{29038F61-3839-4626-91FD-086879011A05}"
)
IDXGIAdapter1._iid_ = IID_IDXGIAdapter1


IDXGIAdapter1._methods_ = [
    COMMETHOD(
        [helpstring('Method GetDesc1')],
        HRESULT,
        'GetDesc1',
        (['out'], POINTER(DXGI_ADAPTER_DESC1), 'pDesc'),
    ),
]

IID_IDXGIDevice1 = MIDL_INTERFACE(
    "{77DB970F-6276-48BA-BA28-070143B4392C}"
)
IDXGIDevice1._iid_ = IID_IDXGIDevice1


IDXGIDevice1._methods_ = [
    COMMETHOD(
        [helpstring('Method SetMaximumFrameLatency')],
        HRESULT,
        'SetMaximumFrameLatency',
        (['in'], UINT, 'MaxLatency'),
    ),
    COMMETHOD(
        [helpstring('Method GetMaximumFrameLatency')],
        HRESULT,
        'GetMaximumFrameLatency',
        (['out'], POINTER(UINT), 'pMaxLatency'),
    ),
]

IID_IDXGIObject = GUID('{AEC22FB8-76F3-4639-9BE0-28EB43A67A2E}')

IID_IDXGIDeviceSubObject = GUID('{3D3E0379-F9DE-4D58-BB6C-18D62992F1A6}')

IID_IDXGIResource = GUID('{35F3AB4-482E-4E50-B41F-8A7F8BD8960B}')

IID_IDXGIKeyedMutex = GUID('{9D8E1289-D7B3-465F-8126-250E349AF85D}')

IID_IDXGISurface = GUID('{CAFCB56C-6AC3-4889-BF47-9E23BBD260EC}')

IID_IDXGISurface1 = GUID('{4AE63092-6327-4C1B-80AE-BFE12EA32B86}')

IID_IDXGIAdapter = GUID('{2411E7E1-12AC-4CCF-BD14-9798E8534DC0}')

IID_IDXGIOutput = GUID('{AE02EEDB-C735-4690-8D52-5A8DC20213AA}')

IID_IDXGISwapChain = GUID('{310D36A0-D2E7-4C0A-AA04-6A9D23B8886A}')

IID_IDXGIFactory = GUID('{7B7166EC-21C7-44AE-B21A-C9AE321AE369}')

IID_IDXGIDevice = GUID('{54EC77FA-1377-44E6-8C32-88FD5F44C84C}')

IID_IDXGIFactory1 = GUID('{770AAE78-F26F-4DBA-A829-253C83D1B387}')

IID_IDXGIAdapter1 = GUID('{29038F61-3839-4626-91FD-086879011A05}')

IID_IDXGIDevice1 = GUID('{77DB970F-6276-48BA-BA28-070143B4392C}')
