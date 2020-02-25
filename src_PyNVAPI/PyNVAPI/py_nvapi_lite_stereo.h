#include "nvapi_lite_stereo.h"


PY_NVAPI_INTERFACE Stereo_Enable(void) {
    return NvAPI_Stereo_Enable();
}

PY_NVAPI_INTERFACE Stereo_Disable(void) {
    return NvAPI_Stereo_Disable();
}

PY_NVAPI_INTERFACE Stereo_IsEnabled(NvU8* pIsStereoEnabled) {
    return NvAPI_Stereo_IsEnabled(pIsStereoEnabled);
}

PY_NVAPI_INTERFACE Stereo_CreateHandleFromIUnknown(IUnknown* pDevice, StereoHandle* pStereoHandle) {
    return NvAPI_Stereo_CreateHandleFromIUnknown(pDevice, pStereoHandle);
}

PY_NVAPI_INTERFACE Stereo_DestroyHandle(StereoHandle stereoHandle) {
    return NvAPI_Stereo_DestroyHandle(stereoHandle);
}

PY_NVAPI_INTERFACE Stereo_Activate(StereoHandle stereoHandle) {
    return NvAPI_Stereo_Activate(stereoHandle);
}

PY_NVAPI_INTERFACE Stereo_Deactivate(StereoHandle stereoHandle) {
    return NvAPI_Stereo_Deactivate(stereoHandle);
}

PY_NVAPI_INTERFACE Stereo_IsActivated(StereoHandle stereoHandle, NvU8* pIsStereoOn) {
    return NvAPI_Stereo_IsActivated(stereoHandle, pIsStereoOn);
}

PY_NVAPI_INTERFACE Stereo_GetSeparation(StereoHandle stereoHandle, float* pSeparationPercentage) {
    return NvAPI_Stereo_GetSeparation(stereoHandle, pSeparationPercentage);
}

PY_NVAPI_INTERFACE Stereo_SetSeparation(StereoHandle stereoHandle, float newSeparationPercentage) {
    return NvAPI_Stereo_SetSeparation(stereoHandle, newSeparationPercentage);
}

PY_NVAPI_INTERFACE Stereo_GetConvergence(StereoHandle stereoHandle, float* pConvergence) {
    return NvAPI_Stereo_GetConvergence(stereoHandle, pConvergence);
}

PY_NVAPI_INTERFACE Stereo_SetConvergence(StereoHandle stereoHandle, float newConvergence) {
    return NvAPI_Stereo_SetConvergence(stereoHandle, newConvergence);
}

PY_NVAPI_INTERFACE Stereo_SetActiveEye(StereoHandle hStereoHandle, NV_STEREO_ACTIVE_EYE StereoEye) {
    return NvAPI_Stereo_SetActiveEye(hStereoHandle, StereoEye);
}

PY_NVAPI_INTERFACE Stereo_SetDriverMode(NV_STEREO_DRIVER_MODE mode) {
    return NvAPI_Stereo_SetDriverMode(mode);
}

PY_NVAPI_INTERFACE Stereo_GetEyeSeparation(StereoHandle hStereoHandle, float* pSeparation) {
    return NvAPI_Stereo_GetEyeSeparation(hStereoHandle, pSeparation);
}

PY_NVAPI_INTERFACE Stereo_IsWindowedModeSupported(NvU8* bSupported) {
    return NvAPI_Stereo_IsWindowedModeSupported(bSupported);
}

PY_NVAPI_INTERFACE Stereo_SetSurfaceCreationMode(StereoHandle hStereoHandle, NVAPI_STEREO_SURFACECREATEMODE creationMode) {
    return NvAPI_Stereo_SetSurfaceCreationMode(hStereoHandle, creationMode);
}

PY_NVAPI_INTERFACE Stereo_GetSurfaceCreationMode(StereoHandle hStereoHandle, NVAPI_STEREO_SURFACECREATEMODE* pCreationMode) {
    return NvAPI_Stereo_GetSurfaceCreationMode(hStereoHandle, pCreationMode);
}

PY_NVAPI_INTERFACE Stereo_Debug_WasLastDrawStereoized(StereoHandle hStereoHandle, NvU8* pWasStereoized) {
    return NvAPI_Stereo_Debug_WasLastDrawStereoized(hStereoHandle, pWasStereoized);
}

PY_NVAPI_INTERFACE Stereo_SetDefaultProfile(const char* szProfileName) {
    return NvAPI_Stereo_SetDefaultProfile(szProfileName);
}

PY_NVAPI_INTERFACE Stereo_GetDefaultProfile(NvU32 cbSizeIn, char* szProfileName, NvU32* pcbSizeOut) {
    return NvAPI_Stereo_GetDefaultProfile(cbSizeIn, szProfileName, pcbSizeOut);
}