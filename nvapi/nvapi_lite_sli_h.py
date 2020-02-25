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

import ctypes


class NV_GET_CURRENT_SLI_STATE_V1(ctypes.Structure):
    _pack_ = 8


class NV_GET_CURRENT_SLI_STATE_V2(ctypes.Structure):
    _pack_ = 8


# **********************************************************************************************************************

from .nvapi_lite_common_h import *  # NOQA


# -----------------------------------------------------------------------------
# DirectX APIs
# -----------------------------------------------------------------------------
# not \ingroup dx
# not Used in NvAPI_D3D10_GetCurrentSLIState(), and
# NvAPI_D3D_GetCurrentSLIState().
NV_GET_CURRENT_SLI_STATE_V1._fields_ = [
    # not < Structure version
    ('version', NvU32),
    # not < [OUT] The maximum possible value of numAFRGroups
    ('maxNumAFRGroups', NvU32),
    # not < [OUT] The number of AFR groups enabled in the system
    ('numAFRGroups', NvU32),
    # not < [OUT] The AFR group index for the frame currently being rendered
    ('currentAFRIndex', NvU32),
    # not < [OUT] What the AFR group index will be for the next frame
    # (i.e. after calling Present)
    ('nextFrameAFRIndex', NvU32),
    # not < [OUT] The AFR group index that was used for the previous frame
    # (~0 if more than one frame has not been rendered yet)
    ('previousFrameAFRIndex', NvU32),
    # not < [OUT] Boolean: Is this frame the first time running on the current
    # AFR group
    ('bIsCurAFRGroupNew', NvU32),
]

NV_GET_CURRENT_SLI_STATE_V2._fields_ = [
    # not < Structure version
    ('version', NvU32),
    # not < [OUT] The maximum possible value of numAFRGroups
    ('maxNumAFRGroups', NvU32),
    # not < [OUT] The number of AFR groups enabled in the system
    ('numAFRGroups', NvU32),
    # not < [OUT] The AFR group index for the frame currently being rendered
    ('currentAFRIndex', NvU32),
    # not < [OUT] What the AFR group index will be for the next frame
    # (i.e. after calling Present)
    ('nextFrameAFRIndex', NvU32),
    # not < [OUT] The AFR group index that was used for the previous frame
    # (~0 if more than one frame has not been rendered yet)
    ('previousFrameAFRIndex', NvU32),
    # not < [OUT] Boolean: Is this frame the first time running on the current
    # AFR group
    ('bIsCurAFRGroupNew', NvU32),
    # not < [OUT] The number of GPUs used in VR-SLI. If it is 0 VR-SLI is not
    # active
    ('numVRSLIGpus', NvU32),
]

# not \ingroup dx
NV_GET_CURRENT_SLI_STATE_VER1 = (
    MAKE_NVAPI_VERSION(NV_GET_CURRENT_SLI_STATE_V1, 1)
)
NV_GET_CURRENT_SLI_STATE_VER2 = (
    MAKE_NVAPI_VERSION(NV_GET_CURRENT_SLI_STATE_V2, 1)
)
NV_GET_CURRENT_SLI_STATE_VER = NV_GET_CURRENT_SLI_STATE_VER2
NV_GET_CURRENT_SLI_STATE = NV_GET_CURRENT_SLI_STATE_V2

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_GetCurrentSLIState
# not DESCRIPTION:  This function returns the current SLI state for the
# specified device. The structure
# not    contains the number of AFR groups, the current AFR group index,
# not    and what the AFR group index will be for the next frame. \p
# not    pDevice can be either a IDirect3DDevice9 or ID3D10Device pointer.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 173
# not
# not \retval  NVAPI_OK  Completed request
# not \retval  NVAPI_ERROR Error occurred
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_D3D_GetCurrentSLIState(IUnknown *pDevice, NV_GET_CURRENT_SLI_STATE *pSliState);

NvAPI_D3D_GetCurrentSLIState = hDll.D3D_GetCurrentSLIState
NvAPI_D3D_GetCurrentSLIState.restype = NVAPI_INTERFACE


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_SetResourceHint
# not \fn NvAPI_D3D_SetResourceHint(IUnknown *pDev, NVDX_ObjectHandle obj,
# not        NVAPI_D3D_SETRESOURCEHINT_CATEGORY dwHintCategory,
# not        NvU32 dwHintName,
# not        NvU32 *pdwHintValue)
# not
# not DESCRIPTION: This is a general purpose function for passing down
# various resource
# not    related hints to the driver. Hints are divided into categories
# not    and types within each category. For DX11 devices this function is
# free-threaded.
# not    An application is responsible to complete this call before making
# use of the resource
# not    in a rendering context
# (therefore applying inter-thread synchronization as appropriate).
# not    As a debug help to an application the driver enforces that a
# resource in this call was never bound.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 185
# not
# not \param [in] pDev  The ID3D10Device or IDirect3DDevice9 that is a
# using the resource
# not \param [in] obj   Previously obtained HV resource handle
# not \param [in] dwHintCategory Category of the hints
# not \param [in] dwHintName A hint within this category
# not \param [in/out] *pdwHintValue Pointer to location containing hint
# value, function returns previous hint value in this slot
# not
# not \return an INT which could be an NvAPI status or DX HRESULT code
# not
# not \retval ::NVAPI_OK
# not \retval ::NVAPI_INVALID_ARGUMENT
# not \retval ::NVAPI_INVALID_CALL  It is illegal to change a hint
# dynamically when the resource is already bound.
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# not \ingroup dx
# not Valid categories for NvAPI_D3D_SetResourceHint()
class _NVAPI_D3D_SETRESOURCEHINT_CATEGORY(ENUM):
    NVAPI_D3D_SRH_CATEGORY_SLI = 1


NVAPI_D3D_SETRESOURCEHINT_CATEGORY = _NVAPI_D3D_SETRESOURCEHINT_CATEGORY


# NVAPI_D3D_SRH_SLI_APP_CONTROLLED_INTERFRAME_CONTENT_SYNC:
# NVAPI_D3D_SRH_SLI_ASK_FOR_BROADCAST_USING:
# NVAPI_D3D_SRH_SLI_RESPECT_DRIVER_INTERFRAME_CONTENT_SYNC:
# not \ingroup dx
# not Types of SLI hints; \n
# not NVAPI_D3D_SRH_SLI_APP_CONTROLLED_INTERFRAME_CONTENT_SYNC: Valid
# values : 0 or 1 \n
# not Default value: 0 \n
# not Explanation: If the value is 1, the driver will not track any
# rendering operations that would mark this resource as dirty,
# not avoiding any form of synchronization across frames rendered in
# parallel in multiple GPUs in AFR mode.
# not
# not NVAPI_D3D_SRH_SLI_ASK_FOR_BROADCAST_USAGE: Valid values : 0 or 1 \n
# not Default value: 0 \n
# not Explanation: If the value is 1, the driver will try to perform
# operations which involved target resource in broadcast,
# not where it's possible. Hint is static and must be set before resource
# starts using.
# not
# not NVAPI_D3D_SRH_SLI_RESPECT_DRIVER_INTERFRAME_CONTENT_SYNC: Valid
# values : 0 or 1 \n
# not Default value: 0 \n
# not Explanation: If the value is 1, the driver will do dirty resource
# resolve regardless of discard flags in the application profile or
# not AFR-FriendlyD3DHints.exe name using.
# not
class _NVAPI_D3D_SETRESOURCEHINT_SLI(ENUM):
    NVAPI_D3D_SRH_SLI_APP_CONTROLLED_INTERFRAME_CONTENT_SYNC = 1
    NVAPI_D3D_SRH_SLI_ASK_FOR_BROADCAST_USAGE = 2
    NVAPI_D3D_SRH_SLI_RESPECT_DRIVER_INTERFRAME_CONTENT_SYNC = 3


NVAPI_D3D_SETRESOURCEHINT_SLI = _NVAPI_D3D_SETRESOURCEHINT_SLI

# not \ingroup dx

# NVAPI_INTERFACE NvAPI_D3D_SetResourceHint(IUnknown *pDev, NVDX_ObjectHandle obj,
#                                           NVAPI_D3D_SETRESOURCEHINT_CATEGORY dwHintCategory,
#                                           NvU32 dwHintName,
#                                           NvU32 *pdwHintValue);

NvAPI_D3D_SetResourceHint = hDll.D3D_SetResourceHint
NvAPI_D3D_SetResourceHint.restype = NVAPI_INTERFACE


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_BeginResourceRendering
# not \fn
# NvAPI_D3D_BeginResourceRendering(IUnknown *pDeviceOrContext, NVDX_ObjectHandle obj, NvU32 Flags)
#
# not DESCRIPTION: This function tells the driver that the resource will
# begin to receive updates. It must be used in combination with
# NvAPI_D3D_EndResourceRendering().
# not    The primary use of this function is allow the driver to initiate
# early inter-frame synchronization of resources while running in AFR SLI
# mode.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 185
# not
# not \param [in] pDev  IDirect3DDevice9, ID3D10Device, ID3D11Device or
# ID3D11DeviceContext that is using the resource
# not \param [in] obj  Previously obtained HV resource handle
# not \param [in] Flags  The flags for functionality applied to resource
# while being used.
# not
# not \retval ::NVAPI_OK   Function succeeded, if used properly and driver
# can initiate proper sync'ing of the resources.
# not \retval ::NVAPI_INVALID_ARGUMENT Bad argument(s) or invalid flag
# values
# not \retval ::NVAPI_INVALID_CALL Mismatched begin/end calls
# ///////////////////////////////////////////////////////////////////////
# not \ingroup dx
# not Used in NvAPI_D3D_BeginResourceRendering().
class _NVAPI_D3D_RESOURCERENDERING_FLAG(ENUM):
    NVAPI_D3D_RR_FLAG_DEFAULTS = 0x00000000
    # not < (bit 0) The flag forces to discard previous content of the
    # resource regardless of the NvApiHints_Sli_Disable_InterframeSync hint
    NVAPI_D3D_RR_FLAG_FORCE_DISCARD_CONTENT = 0x00000001
    # not < (bit 1) The flag forces to respect previous content of the
    # resource regardless of the NvApiHints_Sli_Disable_InterframeSync hint
    NVAPI_D3D_RR_FLAG_FORCE_KEEP_CONTENT = 0x00000002
    # not < (bit 2) The flag hints the driver that content will be used
    # for many frames. If not specified then the driver assumes that
    # content is used only on the next frame
    NVAPI_D3D_RR_FLAG_MULTI_FRAME = 0x00000004


NVAPI_D3D_RESOURCERENDERING_FLAG = _NVAPI_D3D_RESOURCERENDERING_FLAG
# not \ingroup dx
# NVAPI_INTERFACE NvAPI_D3D_BeginResourceRendering(IUnknown *pDeviceOrContext, NVDX_ObjectHandle obj, NvU32 Flags);

NvAPI_D3D_BeginResourceRendering = hDll.D3D_BeginResourceRendering
NvAPI_D3D_BeginResourceRendering.restype = NVAPI_INTERFACE


# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_D3D_EndResourceRendering
# not DESCRIPTION: This function tells the driver that the resource is
# done receiving updates. It must be used in combination with
# not    NvAPI_D3D_BeginResourceRendering().
# not    The primary use of this function is allow the driver to initiate
# early inter-frame syncs of resources while running in AFR SLI mode.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 185
# not
# not \param [in] pDev  IDirect3DDevice9, ID3D10Device, ID3D11Device or
# ID3D11DeviceContext that is using the resource
# not \param [in] obj  Previously obtained HV resource handle
# not \param [in] Flags  Reserved, must be zero
# not \retval ::NVAPI_OK   Function succeeded, if used properly and driver
# can initiate proper sync'ing of the resources.
# not \retval ::NVAPI_INVALID_ARGUMENT Bad argument(s) or invalid flag
# values
# not \retval ::NVAPI_INVALID_CALL Mismatched begin/end calls
# not
# not \ingroup dx
# ///////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_D3D_EndResourceRendering(IUnknown *pDeviceOrContext, NVDX_ObjectHandle obj, NvU32 Flags);

NvAPI_D3D_EndResourceRendering = hDll.D3D_EndResourceRendering
NvAPI_D3D_EndResourceRendering.restype = NVAPI_INTERFACE
