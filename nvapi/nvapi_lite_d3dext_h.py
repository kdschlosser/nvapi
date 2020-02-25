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


# **********************************************************************************************************************
# Copyright 2012 NVIDIA Corporation. All rights reserved.
# NOTICE TO USER:
# This software is subject to NVIDIA ownership rights under U.S. and international Copyright laws.
# This software and the information contained herein are PROPRIETARY and CONFIDENTIAL to NVIDIA
# and are being provided solely under the terms and conditions of an NVIDIA software license agreement.
# Otherwise, you have no rights to use or access this software in any manner.
#
# If not covered by the applicable NVIDIA software license agreement:
# NVIDIA MAKES NO REPRESENTATION ABOUT THE SUITABILITY OF THIS SOFTWARE FOR ANY PURPOSE.
# IT IS PROVIDED "AS IS" WITHOUT EXPRESS OR IMPLIED WARRANTY OF ANY KIND.
# NVIDIA DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY, NONINFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.
# IN NO EVENT SHALL NVIDIA BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL DAMAGES,
# OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOURCE CODE.
#
# U.S. Government End Users.
# This software is a "commercial item" as that term is defined at 48 C.F.R. 2.101 (OCT 1995),
# consisting of "commercial computer software" and "commercial computer software documentation"
# as such terms are used in 48 C.F.R. 12.212 (SEPT 1995) and is provided to the U.S. Government only as a commercial
# end item.
# Consistent with 48 C.F.R.12.212 and 48 C.F.R. 227.7202-1 through 227.7202-4 (JUNE 1995),
# all U.S. Government End Users acquire the software with only those rights set forth herein.
#
# Any use of this software in individual and commercial software must include,
# in the user documentation and internal comments to the code,
# the above Disclaimer (as applicable) and U.S. Government End Users Notice.
#
# **********************************************************************************************************************

from .nvapi_lite_common_h import * # NOQA


# not \ingroup dx
# not D3D_FEATURE_LEVEL supported - used in NvAPI_D3D11_CreateDevice() and
# NvAPI_D3D11_CreateDeviceAndSwapChain()
class NVAPI_DEVICE_FEATURE_LEVEL(ENUM):
    NVAPI_DEVICE_FEATURE_LEVEL_NULL = - 1
    NVAPI_DEVICE_FEATURE_LEVEL_10_0 = 0
    NVAPI_DEVICE_FEATURE_LEVEL_10_0_PLUS = 1
    NVAPI_DEVICE_FEATURE_LEVEL_10_1 = 2
    NVAPI_DEVICE_FEATURE_LEVEL_11_0 = 3


NVAPI_DEVICE_FEATURE_LEVEL_NULL = NVAPI_DEVICE_FEATURE_LEVEL.NVAPI_DEVICE_FEATURE_LEVEL_NULL
NVAPI_DEVICE_FEATURE_LEVEL_10_0 = NVAPI_DEVICE_FEATURE_LEVEL.NVAPI_DEVICE_FEATURE_LEVEL_10_0
NVAPI_DEVICE_FEATURE_LEVEL_10_0_PLUS = NVAPI_DEVICE_FEATURE_LEVEL.NVAPI_DEVICE_FEATURE_LEVEL_10_0_PLUS
NVAPI_DEVICE_FEATURE_LEVEL_10_1 = NVAPI_DEVICE_FEATURE_LEVEL.NVAPI_DEVICE_FEATURE_LEVEL_10_1
NVAPI_DEVICE_FEATURE_LEVEL_11_0 = NVAPI_DEVICE_FEATURE_LEVEL.NVAPI_DEVICE_FEATURE_LEVEL_11_0


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_CreateDevice
# not DESCRIPTION: This function tries to create a DirectX 11 device. If
# the call fails (if we are running
# not    on pre-DirectX 11
# hardware), depending on the type of hardware it will try to create a DirectX 10.1 OR DirectX 10.0 +
# 
# not    OR DirectX 10.0 device. The function call is the same as
# D3D11CreateDevice(), but with an extra
# not    argument (D3D_FEATURE_LEVEL supported by the device) that the
# function fills in. This argument
# not    can contain -1 (NVAPI_DEVICE_FEATURE_LEVEL_NULL), if the
# requested featureLevel is less than DirecX 10.0.
# not
# not   NOTE: When NvAPI_D3D11_CreateDevice is called with 10+ feature
# level we have an issue on few set of
# not    tesla hardware (G80/G84/G86/G92/G94/G96) which does not support
# all feature level 10+ functionality
# not    e.g. calling driver with mismatch between RenderTarget and Depth
# Buffer. App developers should
# not    take into consideration such limitation when using NVAPI on such
# tesla hardwares.
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 185
# not
# not \param [in] pAdapter
# not \param [in] DriverType
# not \param [in] Software
# not \param [in] Flags
# not \param [in] *pFeatureLevels
# not \param [in] FeatureLevels
# not \param [in] SDKVersion
# not \param [in] **ppDevice
# not \param [in] *pFeatureLevel
# not \param [in] **ppImmediateContext
# not \param [in] *pSupportedLevel D3D_FEATURE_LEVEL supported
# not
# not \return NVAPI_OK if the createDevice call succeeded.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_D3D11_CreateDevice(IDXGIAdapter* pAdapter,
#                                          D3D_DRIVER_TYPE DriverType,
#                                          HMODULE Software,
#                                          UINT Flags,
#                                          CONST D3D_FEATURE_LEVEL *pFeatureLevels,
#                                          UINT FeatureLevels,
#                                          UINT SDKVersion,
#                                          ID3D11Device **ppDevice,
#                                          D3D_FEATURE_LEVEL *pFeatureLevel,
#                                          ID3D11DeviceContext **ppImmediateContext,
#                                          NVAPI_DEVICE_FEATURE_LEVEL *pSupportedLevel);

NvAPI_D3D11_CreateDevice = hDll.D3D11_CreateDevice
NvAPI_D3D11_CreateDevice.restype = NVAPI_INTERFACE

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_CreateDeviceAndSwapChain
# not DESCRIPTION: This function tries to create a DirectX 11 device and
# swap chain. If the call fails (if we are
# not    running on pre=DirectX 11
# hardware), depending on the type of hardware it will try to create a DirectX 10.1 OR
# 
# not    DirectX 10.0+ OR DirectX 10.0 device. The function call is the
# same as D3D11CreateDeviceAndSwapChain,
# not    but with an extra argument
# (D3D_FEATURE_LEVEL supported by the device) that the function fills
# not    in. This argument can contain -1
# (NVAPI_DEVICE_FEATURE_LEVEL_NULL), if the requested featureLevel
# not    is less than DirectX 10.0.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 185
# not
# not \param [in]  pAdapter
# not \param [in]  DriverType
# not \param [in]  Software
# not \param [in]  Flags
# not \param [in]  *pFeatureLevels
# not \param [in]  FeatureLevels
# not \param [in]  SDKVersion
# not \param [in]  *pSwapChainDesc
# not \param [in]  **ppSwapChain
# not \param [in]  **ppDevice
# not \param [in]  *pFeatureLevel
# not \param [in]  **ppImmediateContext
# not \param [in]  *pSupportedLevel D3D_FEATURE_LEVEL supported
# not
# not return NVAPI_OK if the createDevice with swap chain call succeeded.
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_D3D11_CreateDeviceAndSwapChain(IDXGIAdapter* pAdapter,
#                                          D3D_DRIVER_TYPE DriverType,
#                                          HMODULE Software,
#                                          UINT Flags,
#                                          CONST D3D_FEATURE_LEVEL *pFeatureLevels,
#                                          UINT FeatureLevels,
#                                          UINT SDKVersion,
#                                          CONST DXGI_SWAP_CHAIN_DESC *pSwapChainDesc,
#                                          IDXGISwapChain **ppSwapChain,
#                                          ID3D11Device **ppDevice,
#                                          D3D_FEATURE_LEVEL *pFeatureLevel,
#                                          ID3D11DeviceContext **ppImmediateContext,
#                                          NVAPI_DEVICE_FEATURE_LEVEL *pSupportedLevel);
NvAPI_D3D11_CreateDeviceAndSwapChain = hDll.D3D11_CreateDeviceAndSwapChain
NvAPI_D3D11_CreateDeviceAndSwapChain.restype = NVAPI_INTERFACE

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D11_SetDepthBoundsTest
# not DESCRIPTION: This function enables/disables the depth bounds test
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in]  pDeviceOrContext The device or device context to set
# depth bounds test
# not \param [in]  bEnable  Enable(non-zero)/disable(zero) the depth
# bounds test
# not \param [in]  fMinDepth  The minimum depth for depth bounds test
# not \param [in]  fMaxDepth  The maximum depth for depth bounds test
# not       The valid values for fMinDepth and fMaxDepth
# not       are such that 0 <= fMinDepth <= fMaxDepth <= 1
# not
# not \return ::NVAPI_OK if the depth bounds test was correcly enabled or
# disabled
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_D3D11_SetDepthBoundsTest(IUnknown* pDeviceOrContext,
#                                                NvU32 bEnable,
#                                                float fMinDepth,
#                                                float fMaxDepth);
NvAPI_D3D11_SetDepthBoundsTest = hDll.D3D11_SetDepthBoundsTest
NvAPI_D3D11_SetDepthBoundsTest.restype = NVAPI_INTERFACE




