
NVAPI_INTERFACE DISP_GetGDIPrimaryDisplayId(NvU32* displayId) {
    return NvAPI_DISP_GetGDIPrimaryDisplayId(displayId);
}

NVAPI_INTERFACE Mosaic_GetDisplayViewportsByResolution(NvU32 displayId, NvU32 srcWidth, NvU32 srcHeight, NV_RECT viewports[NV_MOSAIC_MAX_DISPLAYS], NvU8* bezelCorrected) {
    return NvAPI_Mosaic_GetDisplayViewportsByResolution(displayId, srcWidth, srcHeight, viewports, bezelCorrected);
}
