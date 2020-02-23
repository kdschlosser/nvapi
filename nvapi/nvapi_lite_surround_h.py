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
NvAPI_DISP_GetGDIPrimaryDisplayId = hDll.NvAPI_DISP_GetGDIPrimaryDisplayId
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
NvAPI_Mosaic_GetDisplayViewportsByResolution = hDll.NvAPI_Mosaic_GetDisplayViewportsByResolution
NvAPI_Mosaic_GetDisplayViewportsByResolution.restype = NVAPI_INTERFACE

