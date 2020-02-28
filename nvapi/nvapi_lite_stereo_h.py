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


from .nvapi_lite_common_h import *  # NOQA


# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_Enable
# not DESCRIPTION: This APU enables stereo mode in the registry.
# not    Calls to this function affect the entire system.
# not    If stereo is not enabled, then calls to functions that require that
# stereo is enabled have no effect,
# not    and will return the appropriate error code.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \retval ::NVAPI_OK    Stereo is now enabled.
# not \retval ::NVAPI_API_NOT_INTIALIZED
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR
# not
# not \ingroup stereoapi
# /////////////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_Stereo_Enable(void);
NvAPI_Stereo_Enable = hDll.Stereo_Enable
NvAPI_Stereo_Enable.restype = NVAPI_INTERFACE

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_Disable
# not DESCRIPTION: This API disables stereo mode in the registry.
# not    Calls to this function affect the entire system.
# not    If stereo is not enabled, then calls to functions that require that
# stereo is enabled have no effect,
# not    and will return the appropriate error code.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \retval ::NVAPI_OK    Stereo is now disabled.
# not \retval ::NVAPI_API_NOT_INTIALIZED
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR
# not
# not \ingroup stereoapi
# /////////////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_Stereo_Disable(void);
NvAPI_Stereo_Disable = hDll.Stereo_Disable
NvAPI_Stereo_Disable.restype = NVAPI_INTERFACE

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_IsEnabled
# not DESCRIPTION: This API checks if stereo mode is enabled in the registry.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [out]  pIsStereoEnabled Address where the result of the inquiry
# will be placed.
# not
# not \retval ::NVAPI_OK     Check was sucessfully completed and result
# reflects current state of stereo availability.
# not \retval ::NVAPI_API_NOT_INTIALIZED
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR
# not
# not \ingroup stereoapi
# /////////////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_Stereo_IsEnabled(NvU8 *pIsStereoEnabled);
NvAPI_Stereo_IsEnabled = hDll.Stereo_IsEnabled
NvAPI_Stereo_IsEnabled.restype = NVAPI_INTERFACE

# ///////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_CreateHandleFromIUnknown
# not DESCRIPTION: This API creates a stereo handle that is used in
# subsequent calls related to a given device interface.
# not    This must be called before any other NvAPI_Stereo_ function for
# that handle.
# not    Multiple devices can be used at one time using multiple calls to
# this function (one per each device).
# not
# not HOW TO USE: After the Direct3D device is created, create the stereo
# handle.
# not    On call success:
# not    - Use all other NvAPI_Stereo_ functions that have stereo handle
# as first parameter.
# not    - After the device interface that corresponds to the the stereo
# handle is destroyed,
# not    the application should call NvAPI_DestroyStereoHandle() for that
# stereo handle.
# not
# not WHEN TO USE: After the stereo handle for the device interface is
# created via successfull call to the appropriate
# NvAPI_Stereo_CreateHandleFrom() function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in]  pDevice  Pointer to IUnknown interface that is
# IDirect3DDevice9* in DX9, ID3D10Device*.
# not \param [out] pStereoHandle Pointer to the newly created stereo
# handle.
# not
# not \retval ::NVAPI_OK     Stereo handle is created for given device
# interface.
# not \retval ::NVAPI_INVALID_ARGUMENT  Provided device interface is
# invalid.
# not \retval ::NVAPI_API_NOT_INTIALIZED
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR
# not
# not \ingroup stereoapi
# ///////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_Stereo_CreateHandleFromIUnknown(IUnknown *pDevice, StereoHandle *pStereoHandle);
NvAPI_Stereo_CreateHandleFromIUnknown = hDll.Stereo_CreateHandleFromIUnknown
NvAPI_Stereo_CreateHandleFromIUnknown.restype = NVAPI_INTERFACE

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_DestroyHandle
# not DESCRIPTION: This API destroys the stereo handle created with one of the
# NvAPI_Stereo_CreateHandleFrom() functions.
# not    This should be called after the device corresponding to the handle
# has been destroyed.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in]  stereoHandle Stereo handle that is to be destroyed.
# not
# not \retval ::NVAPI_OK    Stereo handle is destroyed.
# not \retval ::NVAPI_API_NOT_INTIALIZED
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR
# not
# not \ingroup stereoapi
# /////////////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_Stereo_DestroyHandle(StereoHandle stereoHandle);
NvAPI_Stereo_DestroyHandle = hDll.Stereo_DestroyHandle
NvAPI_Stereo_DestroyHandle.restype = NVAPI_INTERFACE

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_Activate
# not DESCRIPTION: This API activates stereo for the device interface
# corresponding to the given stereo handle.
# not    Activating stereo is possible only if stereo was enabled previously
# in the registry.
# not    If stereo is not activated, then calls to functions that require that
# stereo is activated have no effect,
# not    and will return the appropriate error code.
# not
# not WHEN TO USE: After the stereo handle for the device interface is created
# via successfull call to the appropriate NvAPI_Stereo_CreateHandleFrom()
# function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in] stereoHandle Stereo handle corresponding to the device
# interface.
# not
# not \retval ::NVAPI_OK      Stereo is turned on.
# not \retval ::NVAPI_STEREO_INVALID_DEVICE_INTERFACE Device interface is not
# valid. Create again, then attach again.
# not \retval ::NVAPI_API_NOT_INTIALIZED
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED  Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR
# not
# not \ingroup stereoapi
# /////////////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_Stereo_Activate(StereoHandle stereoHandle);
NvAPI_Stereo_Activate = hDll.Stereo_Activate
NvAPI_Stereo_Activate.restype = NVAPI_INTERFACE

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_Deactivate
# not DESCRIPTION: This API deactivates stereo for the given device interface.
# not    If stereo is not activated, then calls to functions that require that
# stereo is activated have no effect,
# not    and will return the appropriate error code.
# not
# not WHEN TO USE: After the stereo handle for the device interface is created
# via successfull call to the appropriate NvAPI_Stereo_CreateHandleFrom()
# function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in]  stereoHandle Stereo handle that corresponds to the device
# interface.
# not
# not \retval ::NVAPI_OK      Stereo is turned off.
# not \retval ::NVAPI_STEREO_INVALID_DEVICE_INTERFACE Device interface is not
# valid. Create again, then attach again.
# not \retval ::NVAPI_API_NOT_INTIALIZED
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED   Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR
# not
# not \ingroup stereoapi
# /////////////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_Stereo_Deactivate(StereoHandle stereoHandle);
NvAPI_Stereo_Deactivate = hDll.Stereo_Deactivate
NvAPI_Stereo_Deactivate.restype = NVAPI_INTERFACE

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_IsActivated
# not DESCRIPTION: This API checks if stereo is activated for the given device
# interface.
# not
# not WHEN TO USE: After the stereo handle for the device interface is created
# via successfull call to the appropriate NvAPI_Stereo_CreateHandleFrom()
# function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in] stereoHandle Stereo handle that corresponds to the device
# interface.
# not \param [in] pIsStereoOn Address where result of the inquiry will be
# placed.
# not
# not \retval ::NVAPI_OK - Check was sucessfully completed and result reflects
# current state of stereo (on/off).
# not \retval ::NVAPI_STEREO_INVALID_DEVICE_INTERFACE - Device interface is
# not valid. Create again, then attach again.
# not \retval ::NVAPI_API_NOT_INTIALIZED - NVAPI not initialized.
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED - Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR - Something is wrong (generic error).
# not
# not \ingroup stereoapi
# /////////////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_Stereo_IsActivated(StereoHandle stereoHandle, NvU8 *pIsStereoOn);
NvAPI_Stereo_IsActivated = hDll.Stereo_IsActivated
NvAPI_Stereo_IsActivated.restype = NVAPI_INTERFACE

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_GetSeparation
# not DESCRIPTION: This API gets current separation value (in percents).
# not
# not WHEN TO USE: After the stereo handle for the device interface is created
# via successfull call to the appropriate NvAPI_Stereo_CreateHandleFrom()
# function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in]  stereoHandle   Stereo handle that corresponds to the device
# interface.
# not \param [out] pSeparationPercentage Address of @c FLOAT type variable to
# store current separation percentage in.
# not
# not \retval ::NVAPI_OK      Retrieval of separation percentage was
# successfull.
# not \retval ::NVAPI_STEREO_INVALID_DEVICE_INTERFACE Device interface is not
# valid. Create again, then attach again.
# not \retval ::NVAPI_API_NOT_INTIALIZED
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED  Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR
# not
# not \ingroup stereoapi
# /////////////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_Stereo_GetSeparation(StereoHandle stereoHandle, float *pSeparationPercentage);
NvAPI_Stereo_GetSeparation = hDll.Stereo_GetSeparation
NvAPI_Stereo_GetSeparation.restype = NVAPI_INTERFACE

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_SetSeparation
# not DESCRIPTION: This API sets separation to given percentage.
# not
# not WHEN TO USE: After the stereo handle for the device interface is created
# via successfull call to appropriate NvAPI_Stereo_CreateHandleFrom() function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in]  stereoHandle   Stereo handle that corresponds to the device
# interface.
# not \param [in]  newSeparationPercentage New value for separation percentage.
# not
# not \retval ::NVAPI_OK      Setting of separation percentage was successfull.
# not \retval ::NVAPI_STEREO_INVALID_DEVICE_INTERFACE Device interface is not
# valid. Create again, then attach again.
# not \retval ::NVAPI_API_NOT_INTIALIZED   NVAPI not initialized.
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED   Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_STEREO_PARAMETER_OUT_OF_RANGE Given separation
# percentage is out of [0..100] range.
# not \retval ::NVAPI_ERROR
# not
# not \ingroup stereoapi
# /////////////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_Stereo_SetSeparation(StereoHandle stereoHandle, float newSeparationPercentage);
NvAPI_Stereo_SetSeparation = hDll.Stereo_SetSeparation
NvAPI_Stereo_SetSeparation.restype = NVAPI_INTERFACE

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_GetConvergence
# not DESCRIPTION: This API gets the current convergence value.
# not
# not WHEN TO USE: After the stereo handle for the device interface is created
# via successfull call to the appropriate NvAPI_Stereo_CreateHandleFrom()
# function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in]  stereoHandle Stereo handle that corresponds to the device
# interface.
# not \param [out] pConvergence Address of @c FLOAT type variable to store
# current convergence value in.
# not
# not \retval ::NVAPI_OK      Retrieval of convergence value was successfull.
# not \retval ::NVAPI_STEREO_INVALID_DEVICE_INTERFACE Device interface is not
# valid. Create again, then attach again.
# not \retval ::NVAPI_API_NOT_INTIALIZED
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED   Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR
# not
# not \ingroup stereoapi
# /////////////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_Stereo_GetConvergence(StereoHandle stereoHandle, float *pConvergence);
NvAPI_Stereo_GetConvergence = hDll.Stereo_GetConvergence
NvAPI_Stereo_GetConvergence.restype = NVAPI_INTERFACE

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_SetConvergence
# not DESCRIPTION: This API sets convergence to the given value.
# not
# not WHEN TO USE: After the stereo handle for the device interface is created
# via successfull call to the appropriate NvAPI_Stereo_CreateHandleFrom()
# function.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \since Release: 180
# not
# not \param [in]  stereoHandle   Stereo handle that corresponds to the device
# interface.
# not \param [in]  newConvergence  New value for convergence.
# not
# not \retval ::NVAPI_OK      Setting of convergence value was successfull.
# not \retval ::NVAPI_STEREO_INVALID_DEVICE_INTERFACE Device interface is not
# valid. Create again, then attach again.
# not \retval ::NVAPI_API_NOT_INTIALIZED
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED  Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR
# not
# not \ingroup stereoapi
# /////////////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_Stereo_SetConvergence(StereoHandle stereoHandle, float newConvergence);
NvAPI_Stereo_SetConvergence = hDll.Stereo_SetConvergence
NvAPI_Stereo_SetConvergence.restype = NVAPI_INTERFACE

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_SetActiveEye
# not \fn
# NvAPI_Stereo_SetActiveEye(StereoHandle hStereoHandle, NV_STEREO_ACTIVE_EYE StereoEye);
# 
# not DESCRIPTION: This API sets the back buffer to left or right in Direct
# stereo mode.
# not
# not HOW TO USE: After the stereo handle for device interface is created via
# successfull call to appropriate
# not    NvAPI_Stereo_CreateHandleFrom function.
# not
# not \since Release: 285
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] stereoHandle Stereo handle that corresponds to the device
# interface.
# not \param [in] StereoEye  Defines active eye in Direct stereo mode
# not
# not \retval ::NVAPI_OK - Active eye is set.
# not \retval ::NVAPI_STEREO_INVALID_DEVICE_INTERFACE - Device interface is
# not valid. Create again, then attach again.
# not \retval ::NVAPI_API_NOT_INTIALIZED - NVAPI not initialized.
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED - Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_INVALID_ARGUMENT - StereoEye parameter has not allowed
# value.
# not \retval ::NVAPI_SET_NOT_ALLOWED - Current stereo mode is not Direct
# not \retval ::NVAPI_ERROR - Something is wrong (generic error).
# /////////////////////////////////////////////////////////////////////////////


# not \ingroup stereoapi
class _NV_StereoActiveEye(ENUM):
    NVAPI_STEREO_EYE_RIGHT = EnumItem(1).set_string('Right')
    NVAPI_STEREO_EYE_LEFT = EnumItem(2).set_string('Left')
    NVAPI_STEREO_EYE_MONO = EnumItem(3).set_string('Mono')


NV_STEREO_ACTIVE_EYE = _NV_StereoActiveEye


# not \ingroup stereoapi
# NVAPI_INTERFACE NvAPI_Stereo_SetActiveEye(StereoHandle hStereoHandle, NV_STEREO_ACTIVE_EYE StereoEye);
NvAPI_Stereo_SetActiveEye = hDll.Stereo_SetActiveEye
NvAPI_Stereo_SetActiveEye.restype = NVAPI_INTERFACE

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_SetDriverMode
# not \fn NvAPI_Stereo_SetDriverMode( NV_STEREO_DRIVER_MODE mode );
# not DESCRIPTION: This API sets the 3D stereo driver mode: Direct or Automatic
# not
# not HOW TO USE: This API must be called before the device is created.
# not    Applies to DirectX 9 and higher.
# not
# not \since Release: 285
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] mode  Defines the 3D stereo driver mode: Direct or Automatic
# not
# not \retval ::NVAPI_OK    Active eye is set.
# not \retval ::NVAPI_API_NOT_INTIALIZED NVAPI not initialized.
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_INVALID_ARGUMENT  mode parameter has not allowed value.
# not \retval ::NVAPI_ERROR    Something is wrong (generic error).
# /////////////////////////////////////////////////////////////////////////////


# not \ingroup stereoapi
class _NV_StereoDriverMode(ENUM):
    NVAPI_STEREO_DRIVER_MODE_AUTOMATIC = EnumItem(0).set_string('Automatic')
    NVAPI_STEREO_DRIVER_MODE_DIRECT = EnumItem(2).set_string('Direct')


NV_STEREO_DRIVER_MODE = _NV_StereoDriverMode

# not \ingroup stereoapi
# NVAPI_INTERFACE NvAPI_Stereo_SetDriverMode( NV_STEREO_DRIVER_MODE mode );
NvAPI_Stereo_SetDriverMode = hDll.Stereo_SetDriverMode
NvAPI_Stereo_SetDriverMode.restype = NVAPI_INTERFACE

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_GetEyeSeparation
# not DESCRIPTION: This API returns eye separation as a ratio of < between eye
# distance > / < physical screen width > .
# not
# not HOW TO USE: After the stereo handle for device interface is created via
# successfull call to appropriate API. Applies only to DirectX 9 and up.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [in] stereoHandle Stereo handle that corresponds to the device
# interface.
# not \param [out] pSeparation Eye separation.
# not
# not \retval ::NVAPI_OK      Active eye is set.
# not \retval ::NVAPI_STEREO_INVALID_DEVICE_INTERFACE Device interface is not
# valid. Create again, then attach again.
# not \retval ::NVAPI_API_NOT_INTIALIZED   NVAPI not initialized.
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED   Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR (generic error).
# not
# not \ingroup stereoapi
# /////////////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_Stereo_GetEyeSeparation(StereoHandle hStereoHandle,  float *pSeparation );
NvAPI_Stereo_GetEyeSeparation = hDll.Stereo_GetEyeSeparation
NvAPI_Stereo_GetEyeSeparation.restype = NVAPI_INTERFACE

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_IsWindowedModeSupported
# not DESCRIPTION: This API returns availability of windowed mode stereo
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not \param [out] bSupported(OUT) != 0 - supported, \n
# not      == 0 - is not supported
# not
# not
# not \retval ::NVAPI_OK    Retrieval of frustum adjust mode was successfull.
# not \retval ::NVAPI_API_NOT_INTIALIZED NVAPI not initialized.
# not \retval ::NVAPI_STEREO_NOT_INITIALIZED Stereo part of NVAPI not
# initialized.
# not \retval ::NVAPI_ERROR    Something is wrong (generic error).
# not
# not \ingroup stereoapi
# /////////////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_Stereo_IsWindowedModeSupported(NvU8* bSupported);
NvAPI_Stereo_IsWindowedModeSupported = hDll.Stereo_IsWindowedModeSupported
NvAPI_Stereo_IsWindowedModeSupported.restype = NVAPI_INTERFACE

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_SetSurfaceCreationMode
# not \function
# NvAPI_Stereo_SetSurfaceCreationMode(StereoHandle hStereoHandle, NVAPI_STEREO_SURFACECREATEMODE creationMode)
# 
# not \param [in] hStereoHandle Stereo handle that corresponds to the device
# interface.
# not \param [in] creationMode New surface creation mode for this device
# interface.
# not
# not \since Release: 285
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not DESCRIPTION: This API sets surface creation mode for this device
# interface.
# not
# not WHEN TO USE: After the stereo handle for device interface is created via
# successful call to appropriate NvAPI_Stereo_CreateHandleFrom function.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   There are no return error codes with specific meaning for this API.
# not
# /////////////////////////////////////////////////////////////////////////////


# not \ingroup stereoapi
class _NVAPI_STEREO_SURFACECREATEMODE(ENUM):
    NVAPI_STEREO_SURFACECREATEMODE_AUTO = EnumItem(1).set_string('Auto')
    NVAPI_STEREO_SURFACECREATEMODE_FORCESTEREO = EnumItem(2).set_string('Force Stereo')
    NVAPI_STEREO_SURFACECREATEMODE_FORCEMONO = EnumItem(3).set_string('Force Mono')


NVAPI_STEREO_SURFACECREATEMODE = _NVAPI_STEREO_SURFACECREATEMODE

# not \ingroup stereoapi
# NVAPI_INTERFACE NvAPI_Stereo_SetSurfaceCreationMode(
# __in StereoHandle hStereoHandle,
# __in NVAPI_STEREO_SURFACECREATEMODE creationMode
# );
NvAPI_Stereo_SetSurfaceCreationMode = hDll.Stereo_SetSurfaceCreationMode
NvAPI_Stereo_SetSurfaceCreationMode.restype = NVAPI_INTERFACE

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_GetSurfaceCreationMode
# not \function
# NvAPI_Stereo_GetSurfaceCreationMode(StereoHandle hStereoHandle, NVAPI_STEREO_SURFACECREATEMODE* pCreationMode)
# 
# not \param [in] hStereoHandle Stereo handle that corresponds to the device
# interface.
# not \param [out] pCreationMode The current creation mode for this device
# interface.
# not
# not \since Release: 295
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not DESCRIPTION: This API gets surface creation mode for this device
# interface.
# not
# not WHEN TO USE: After the stereo handle for device interface is created via
# successful call to appropriate NvAPI_Stereo_CreateHandleFrom function.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   There are no return error codes with specific meaning for this API.
# not
# /////////////////////////////////////////////////////////////////////////////
# not \ingroup stereoapi
# NVAPI_INTERFACE NvAPI_Stereo_GetSurfaceCreationMode(
# __in StereoHandle hStereoHandle,
# __in NVAPI_STEREO_SURFACECREATEMODE* pCreationMode
# );
NvAPI_Stereo_GetSurfaceCreationMode = hDll.Stereo_GetSurfaceCreationMode
NvAPI_Stereo_GetSurfaceCreationMode.restype = NVAPI_INTERFACE

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_Debug_WasLastDrawStereoized
# not \param [in] hStereoHandle Stereo handle that corresponds to the device
# interface.
# not \param [out] pWasStereoized Address where result of the inquiry will be
# placed.
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not DESCRIPTION: This API checks if the last draw call was stereoized. It is
# a very expensive to call and should be used for debugging purpose *only*.
# not
# not WHEN TO USE: After the stereo handle for device interface is created via
# successful call to appropriate NvAPI_Stereo_CreateHandleFrom function.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   There are no return error codes with specific meaning for this API.
# not
# not \ingroup stereoapi
# /////////////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_Stereo_Debug_WasLastDrawStereoized(__in StereoHandle hStereoHandle, __out NvU8 *pWasStereoized);
NvAPI_Stereo_Debug_WasLastDrawStereoized = hDll.Stereo_Debug_WasLastDrawStereoized
NvAPI_Stereo_Debug_WasLastDrawStereoized.restype = NVAPI_INTERFACE

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_SetDefaultProfile
# not
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not DESCRIPTION: This API defines the stereo profile used by the driver in
# case the application has no associated profile.
# not
# not WHEN TO USE: To take effect, this API must be called before D3D device
# is created. Calling once a device has been created will not affect the
# current device.
# not
# not \param [in] szProfileName  Default profile name.
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   Error codes specific to this API are described below.
# not
# not \retval NVAPI_SUCCESS      - Default stereo profile name has been copied
# into szProfileName.
# not \retval NVAPI_INVALID_ARGUMENT    - szProfileName == NULL.
# not \retval NVAPI_DEFAULT_STEREO_PROFILE_DOES_NOT_EXIST - Default stereo
# profile does not exist
# not
# not \ingroup stereoapi
# /////////////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_Stereo_SetDefaultProfile(__in const char* szProfileName);
NvAPI_Stereo_SetDefaultProfile = hDll.Stereo_SetDefaultProfile
NvAPI_Stereo_SetDefaultProfile.restype = NVAPI_INTERFACE

# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Stereo_GetDefaultProfile
# not SUPPORTED OS: Windows 7 and higher
# not
# not
# not DESCRIPTION: This API retrieves the current default stereo profile.
# not
# not   After call cbSizeOut contain 0 if default profile is not set required
# buffer size cbSizeOut.
# not   To get needed buffer size this function can be called with
# szProfileName == 0 and cbSizeIn == 0.
# not
# not WHEN TO USE: This API can be called at any time.
# not
# not
# not \param [in] cbSizeIn   Size of buffer allocated for default stereo
# profile name.
# not \param [out] szProfileName  Default stereo profile name.
# not \param [out] pcbSizeOut   Required buffer size.
# not    == 0 - there is no default stereo profile name currently set
# not    != 0 - size of buffer required for currently set default stereo
# profile name including trailing '0'.
# not
# not
# not \return This API can return any of the error codes enumerated in
# NvAPI_Status.
# not   Error codes specific to this API are described below.
# not
# not \retval NVAPI_SUCCESS      - Default stereo profile name has been copied
# into szProfileName.
# not \retval NVAPI_DEFAULT_STEREO_PROFILE_IS_NOT_DEFINED - There is no
# default stereo profile set at this time.
# not \retval NVAPI_INVALID_ARGUMENT     - pcbSizeOut == 0 or cbSizeIn >=
# *pcbSizeOut and szProfileName == 0
# not \retval NVAPI_INSUFFICIENT_BUFFER    - cbSizeIn < *pcbSizeOut
# not
# not \ingroup stereoapi
# /////////////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_Stereo_GetDefaultProfile(
# __in NvU32 cbSizeIn,
# __out_bcount_part_opt(cbSizeIn, *pcbSizeOut) char* szProfileName,
# __out NvU32 *pcbSizeOut
# );
NvAPI_Stereo_GetDefaultProfile = hDll.Stereo_GetDefaultProfile
NvAPI_Stereo_GetDefaultProfile.restype = NVAPI_INTERFACE
