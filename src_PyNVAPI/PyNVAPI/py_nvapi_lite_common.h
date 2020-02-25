
#include "nvapi_lite_common.h"


PY_NVAPI_INTERFACE SYS_GetDriverAndBranchVersion(NvU32* pDriverVersion, NvAPI_ShortString szBuildBranchString) {
    return NvAPI_SYS_GetDriverAndBranchVersion(pDriverVersion, szBuildBranchString);
}

PY_NVAPI_INTERFACE GPU_GetMemoryInfo(NvPhysicalGpuHandle hPhysicalGpu, NV_DISPLAY_DRIVER_MEMORY_INFO* pMemoryInfo) {
    return NvAPI_GPU_GetMemoryInfo(hPhysicalGpu, pMemoryInfo);
}

PY_NVAPI_INTERFACE EnumPhysicalGPUs(NvPhysicalGpuHandle nvGPUHandle[NVAPI_MAX_PHYSICAL_GPUS], NvU32* pGpuCount) {
    return NvAPI_EnumPhysicalGPUs(nvGPUHandle, pGpuCount);
}

PY_NVAPI_INTERFACE D3D_GetObjectHandleForResource(IUnknown* pDevice, IUnknown* pResource, NVDX_ObjectHandle* pHandle) {
    return NvAPI_D3D_GetObjectHandleForResource(pDevice, pResource, pHandle);
}
