import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


__D3D10MISC_H__ = None



# ////////////////////////////////////////////////////////////////////////////
# Copyright (c) Microsoft Corporation. All rights reserved.
# File:  D3D10Misc.h
# Content: D3D10 Device Creation APIs
# ////////////////////////////////////////////////////////////////////////////
if not defined(__D3D10MISC_H__):
    __D3D10MISC_H__ = VOID
    from pyWinAPI.um.d3d10_h import * # NOQA

    # ID3D10Blob has been made version-neutral and moved to d3dcommon.h.
    if defined(__cplusplus):
        pass
    # END IF  __cplusplus

    from pyWinAPI.shared.winapifamily_h import * # NOQA
    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # ///////////////////////////////////////////////////////////////
        # D3D10_DRIVER_TYPE
        # ----------------
        # This identifier is used to determine the implementation of Direct3D10
        # to be used.
        # Pass one of these values to D3D10CreateDevice
        # ///////////////////////////////////////////////////////////////
        class D3D10_DRIVER_TYPE(ENUM):
            D3D10_DRIVER_TYPE_HARDWARE = 0
            D3D10_DRIVER_TYPE_REFERENCE = 1
            D3D10_DRIVER_TYPE_NULL = 2
            D3D10_DRIVER_TYPE_SOFTWARE = 3
            D3D10_DRIVER_TYPE_WARP = 5

        GUID_DeviceType = DEFINE_GUID(
            0xD722FB4D,
            0x7A68,
            0x437A,
            0xB2,
            0x0C,
            0x58,
            0x04,
            0xEE,
            0x24,
            0x94,
            0xA6
        )

        # ///////////////////////////////////////////////////////////////
        # D3D10CreateDevice
        # ------------------
        # pAdapter
        # If NULL, D3D10CreateDevice will choose the primary adapter and
        # create a new instance from a temporarily created IDXGIFactory.
        # If non-NULL, D3D10CreateDevice will register the appropriate
        # device, if necessary (via IDXGIAdapter::RegisterDrver), before
        # creating the device.
        # DriverType
        # Specifies the driver type to be created: hardware, reference or
        # null.
        # Software
        # HMODULE of a DLL implementing a software rasterizer. Must be NULL for
        # non-Software driver types.
        # Flags
        # Any of those documented for D3D10CreateDevice.
        # SDKVersion
        # SDK version. Use the D3D10_SDK_VERSION macro.
        # ppDevice
        # Pointer to returned interface.
        # Return Values
        # Any of those documented for
        # CreateDXGIFactory
        # IDXGIFactory::EnumAdapters
        # IDXGIAdapter::RegisterDriver
        # D3D10CreateDevice
        # ///////////////////////////////////////////////////////////////
        d3d10 = ctypes.windll.D3D10


        # HRESULT WINAPI D3D10CreateDevice(
        # _In_opt_ IDXGIAdapter *pAdapter,
        # D3D10_DRIVER_TYPE DriverType,
        # HMODULE Software,
        # UINT Flags,
        # UINT SDKVersion,
        # _Out_opt_ ID3D10Device **ppDevice);
        D3D10CreateDevice = d3d10.D3D10CreateDevice
        D3D10CreateDevice.restype = WINAPI


        # ///////////////////////////////////////////////////////////////
        # D3D10CreateDeviceAndSwapChain
        # ------------------------------
        # ppAdapter
        # If NULL, D3D10CreateDevice will choose the primary adapter and
        # create a new instance from a temporarily created IDXGIFactory.
        # If non-NULL, D3D10CreateDevice will register the appropriate
        # device, if necessary (via IDXGIAdapter::RegisterDrver), before
        # creating the device.
        # DriverType
        # Specifies the driver type to be created: hardware, reference or
        # null.
        # Software
        # HMODULE of a DLL implementing a software rasterizer. Must be NULL for
        # non-Software driver types.
        # Flags
        # Any of those documented for D3D10CreateDevice.
        # SDKVersion
        # SDK version. Use the D3D10_SDK_VERSION macro.
        # pSwapChainDesc
        # Swap chain description, may be NULL.
        # ppSwapChain
        # Pointer to returned interface. May be NULL.
        # ppDevice
        # Pointer to returned interface.
        # Return Values
        # Any of those documented for
        # CreateDXGIFactory
        # IDXGIFactory::EnumAdapters
        # IDXGIAdapter::RegisterDriver
        # D3D10CreateDevice
        # IDXGIFactory::CreateSwapChain
        # ///////////////////////////////////////////////////////////////
        # HRESULT WINAPI D3D10CreateDeviceAndSwapChain(
        # _In_opt_ IDXGIAdapter *pAdapter,
        # D3D10_DRIVER_TYPE DriverType,
        # HMODULE Software,
        # UINT Flags,
        # UINT SDKVersion,
        # _In_opt_ DXGI_SWAP_CHAIN_DESC *pSwapChainDesc,
        # _Out_opt_ IDXGISwapChain **ppSwapChain,
        # _Out_opt_ ID3D10Device **ppDevice);
        D3D10CreateDeviceAndSwapChain = d3d10.D3D10CreateDeviceAndSwapChain
        D3D10CreateDeviceAndSwapChain.restype = WINAPI

        # ///////////////////////////////////////////////////////////////
        # D3D10CreateBlob:
        # -----------------
        # Creates a Buffer of n Bytes
        # //////////////////////////////////////////////////////////////
        # HRESULT WINAPI D3D10CreateBlob(SIZE_T NumBytes, _Out_ LPD3D10BLOB *ppBuffer);
        D3D10CreateBlob = d3d10.D3D10CreateBlob
        D3D10CreateBlob.restype = WINAPI
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    if defined(__cplusplus):
        pass
    # END IF  __cplusplus
# END IF  __D3D10EFFECT_H__


