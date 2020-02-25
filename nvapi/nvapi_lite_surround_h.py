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
from .nvapi_lite_common_h import *  # NOQA

# not SUPPORTED OS: Windows 7 and higher
# not
# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_DISP_GetGDIPrimaryDisplayId
# not DESCRIPTION:  This API returns the Display ID of the GDI Primary.
# not
# not \param [out]  displayId Display ID of the GDI Primary display.
# not
# not \retval ::NVAPI_OK:     Capabilties have been returned.
# not \retval ::NVAPI_NVIDIA_DEVICE_NOT_FOUND:  GDI Primary not on an NVIDIA
# GPU.
# not \retval ::NVAPI_INVALID_ARGUMENT:  One or more args passed in are
# invalid.
# not \retval ::NVAPI_API_NOT_INTIALIZED:  The NvAPI API needs to be
# initialized first
# not \retval ::NVAPI_NO_IMPLEMENTATION:   This entrypoint not available
# not \retval ::NVAPI_ERROR:     Miscellaneous error occurred
# not
# not \ingroup dispcontrol
# /////////////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_DISP_GetGDIPrimaryDisplayId(NvU32* displayId);
NvAPI_DISP_GetGDIPrimaryDisplayId = hDll.DISP_GetGDIPrimaryDisplayId
NvAPI_DISP_GetGDIPrimaryDisplayId.restype = NVAPI_INTERFACE

NV_MOSAIC_MAX_DISPLAYS = 64

# not SUPPORTED OS: Windows 7 and higher
# not
# /////////////////////////////////////////////////////////////////////////////
# FUNCTION NAME: NvAPI_Mosaic_GetDisplayViewportsByResolution
# not DESCRIPTION:  This API returns the viewports that would be applied on
# not    the requested display.
# not
# not \param [in] displayId  Display ID of a single display in the active
# not       mosaic topology to query.
# not \param [in] srcWidth  Width of full display topology. If both
# not       width and height are 0, the current
# not       resolution is used.
# not \param [in] srcHeight  Height of full display topology. If both
# not       width and height are 0, the current
# not       resolution is used.
# not \param [out]  viewports  Array of NV_RECT viewports which represent
# not       the displays as identified in
# not       NvAPI_Mosaic_EnumGridTopologies. If the
# not       requested resolution is a single-wide
# not       resolution, only viewports[0] will
# not       contain the viewport details, regardless
# not       of which display is driving the display.
# not \param [out]  bezelCorrected Returns 1 if the requested resolution is
# not       bezel corrected. May be NULL.
# not
# not \retval ::NVAPI_OK     Capabilties have been returned.
# not \retval ::NVAPI_INVALID_ARGUMENT  One or more args passed in are invalid.
# not \retval ::NVAPI_API_NOT_INTIALIZED  The NvAPI API needs to be
# initialized first
# not \retval ::NVAPI_MOSAIC_NOT_ACTIVE   The display does not belong to an
# active Mosaic Topology
# not \retval ::NVAPI_NO_IMPLEMENTATION   This entrypoint not available
# not \retval ::NVAPI_ERROR     Miscellaneous error occurred
# not
# not \ingroup mosaicapi
# /////////////////////////////////////////////////////////////////////////////
# NVAPI_INTERFACE NvAPI_Mosaic_GetDisplayViewportsByResolution(
# NvU32 displayId,
# NvU32 srcWidth,
# NvU32 srcHeight,
# NV_RECT viewports[NV_MOSAIC_MAX_DISPLAYS],
# NvU8* bezelCorrected
# );
NvAPI_Mosaic_GetDisplayViewportsByResolution = hDll.Mosaic_GetDisplayViewportsByResolution
NvAPI_Mosaic_GetDisplayViewportsByResolution.restype = NVAPI_INTERFACE

