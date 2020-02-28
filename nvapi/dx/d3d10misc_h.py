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

GUID_DeviceType = GUID(
    '{D722FB4D-7A68-437A-B20C-5804EE2494A6}'
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
D3D10CreateDevice.restype = HRESULT


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
D3D10CreateDeviceAndSwapChain.restype = HRESULT

# ///////////////////////////////////////////////////////////////
# D3D10CreateBlob:
# -----------------
# Creates a Buffer of n Bytes
# //////////////////////////////////////////////////////////////
# HRESULT WINAPI D3D10CreateBlob(SIZE_T NumBytes, _Out_ LPD3D10BLOB *ppBuffer);
D3D10CreateBlob = d3d10.D3D10CreateBlob
D3D10CreateBlob.restype = HRESULT
# END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

