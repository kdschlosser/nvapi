#include "nvapi_lite_sli.h"


PY_NVAPI_INTERFACE D3D_GetCurrentSLIState(IUnknown* pDevice, NV_GET_CURRENT_SLI_STATE* pSliState) {
    return NvAPI_D3D_GetCurrentSLIState(pDevice, pSliState);
}

PY_NVAPI_INTERFACE D3D_SetResourceHint(IUnknown* pDev, NVDX_ObjectHandle obj, NVAPI_D3D_SETRESOURCEHINT_CATEGORY dwHintCategory, NvU32 dwHintName, NvU32* pdwHintValue) {
    return NvAPI_D3D_SetResourceHint(pDev, obj, dwHintCategory, dwHintName, pdwHintValue);
}

PY_NVAPI_INTERFACE D3D_BeginResourceRendering(IUnknown* pDeviceOrContext, NVDX_ObjectHandle obj, NvU32 Flags) {
    return NvAPI_D3D_BeginResourceRendering(pDeviceOrContext, obj, Flags);
}

PY_NVAPI_INTERFACE D3D_EndResourceRendering(IUnknown* pDeviceOrContext, NVDX_ObjectHandle obj, NvU32 Flags) {
    return NvAPI_D3D_EndResourceRendering(pDeviceOrContext, obj, Flags);
}
