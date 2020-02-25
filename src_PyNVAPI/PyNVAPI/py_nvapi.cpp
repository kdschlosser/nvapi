
#include"nvapi.h"
#include"py_nvapi_lite_common.h"
#include"py_nvapi_lite_sli.h"
#include"py_nvapi_lite_surround.h"
#include"py_nvapi_lite_stereo.h"
#include"py_nvapi_lite_d3dext.h"

NVAPI_INTERFACE Initialize() {
    return NvAPI_Initialize();
}

NVAPI_INTERFACE Unload() {
    return NvAPI_Unload();
}

NVAPI_INTERFACE GetErrorMessage(NvAPI_Status nr, NvAPI_ShortString szDesc) {
    return NvAPI_GetErrorMessage(nr, szDesc);
}

NVAPI_INTERFACE GetInterfaceVersionString(NvAPI_ShortString szDesc) {
    return NvAPI_GetInterfaceVersionString(szDesc);
}

NVAPI_INTERFACE GPU_GetEDID(NvPhysicalGpuHandle hPhysicalGpu, NvU32 displayOutputId, NV_EDID *pEDID) {
    return NvAPI_GPU_GetEDID(hPhysicalGpu, displayOutputId, pEDID);
}

NVAPI_INTERFACE SetView(NvDisplayHandle hNvDisplay, NV_VIEW_TARGET_INFO *pTargetInfo, NV_TARGET_VIEW_MODE targetView) {
    return NvAPI_SetView(hNvDisplay, pTargetInfo, targetView);
}

NVAPI_INTERFACE SetViewEx(NvDisplayHandle hNvDisplay, NV_DISPLAY_PATH_INFO *pPathInfo, NV_TARGET_VIEW_MODE displayView) {
    return NvAPI_SetViewEx(hNvDisplay, pPathInfo, displayView);
}

NVAPI_INTERFACE GetDisplayDriverVersion(NvDisplayHandle hNvDisplay, NV_DISPLAY_DRIVER_VERSION *pVersion) {
    return NvAPI_GetDisplayDriverVersion(hNvDisplay, pVersion);
}

NVAPI_INTERFACE OGL_ExpertModeSet(NvU32 expertDetailLevel, NvU32 expertReportMask, NvU32 expertOutputMask, NVAPI_OGLEXPERT_CALLBACK expertCallback) {
    return NvAPI_OGL_ExpertModeSet(expertDetailLevel, expertReportMask, expertOutputMask, expertCallback);
}

NVAPI_INTERFACE OGL_ExpertModeGet(NvU32 *pExpertDetailLevel, NvU32 *pExpertReportMask, NvU32 *pExpertOutputMask, NVAPI_OGLEXPERT_CALLBACK *pExpertCallback) {
    return NvAPI_OGL_ExpertModeGet(*pExpertDetailLevel, pExpertReportMask, pExpertOutputMask, pExpertCallback);
}

NVAPI_INTERFACE OGL_ExpertModeDefaultsSet(NvU32 expertDetailLevel, NvU32 expertReportMask, NvU32 expertOutputMask) {
    return NvAPI_OGL_ExpertModeDefaultsSet(expertDetailLevel, expertReportMask, expertOutputMask);
}

NVAPI_INTERFACE OGL_ExpertModeDefaultsGet(NvU32 *pExpertDetailLevel, NvU32 *pExpertReportMask, NvU32 *pExpertOutputMask) {
    return NvAPI_OGL_ExpertModeDefaultsGet(pExpertDetailLevel, pExpertReportMask, pExpertOutputMask);
}

NVAPI_INTERFACE EnumTCCPhysicalGPUs(NvPhysicalGpuHandle nvGPUHandle[NVAPI_MAX_PHYSICAL_GPUS], NvU32 *pGpuCount) {
    return NvAPI_EnumTCCPhysicalGPUs(nvGPUHandle, pGpuCount);
}

NVAPI_INTERFACE EnumLogicalGPUs(NvLogicalGpuHandle nvGPUHandle[NVAPI_MAX_LOGICAL_GPUS], NvU32 *pGpuCount) {
    return NvAPI_EnumLogicalGPUs(nvGPUHandle, pGpuCount);
}

NVAPI_INTERFACE GetPhysicalGPUsFromDisplay(NvDisplayHandle hNvDisp, NvPhysicalGpuHandle nvGPUHandle[NVAPI_MAX_PHYSICAL_GPUS], NvU32 *pGpuCount) {
    return NvAPI_GetPhysicalGPUsFromDisplay(hNvDisp, nvGPUHandle, pGpuCount);
}

NVAPI_INTERFACE GetPhysicalGPUFromUnAttachedDisplay(NvUnAttachedDisplayHandle hNvUnAttachedDisp, NvPhysicalGpuHandle *pPhysicalGpu) {
    return NvAPI_GetPhysicalGPUFromUnAttachedDisplay(hNvUnAttachedDisp, pPhysicalGpu);
}

NVAPI_INTERFACE GetLogicalGPUFromDisplay(NvDisplayHandle hNvDisp, NvLogicalGpuHandle *pLogicalGPU) {
    return NvAPI_GetLogicalGPUFromDisplay(hNvDisp, pLogicalGPU);
}

NVAPI_INTERFACE GetLogicalGPUFromPhysicalGPU(NvPhysicalGpuHandle hPhysicalGPU, NvLogicalGpuHandle *pLogicalGPU) {
    return NvAPI_GetLogicalGPUFromPhysicalGPU(hPhysicalGPU, pLogicalGPU);
}

NVAPI_INTERFACE GetPhysicalGPUsFromLogicalGPU(NvLogicalGpuHandle hLogicalGPU,NvPhysicalGpuHandle hPhysicalGPU[NVAPI_MAX_PHYSICAL_GPUS], NvU32 *pGpuCount) {
    return NvAPI_GetPhysicalGPUsFromLogicalGPU(hLogicalGPU, hPhysicalGPU, pGpuCount);
}

NVAPI_INTERFACE GPU_GetShaderSubPipeCount(NvPhysicalGpuHandle hPhysicalGpu,NvU32 *pCount) {
    return NvAPI_GPU_GetShaderSubPipeCount(hPhysicalGpu, pCount);
}

NVAPI_INTERFACE GPU_GetGpuCoreCount(NvPhysicalGpuHandle hPhysicalGpu,NvU32 *pCount) {
    return NvAPI_GPU_GetGpuCoreCount(hPhysicalGpu, pCount);
}

NVAPI_INTERFACE GPU_GetAllOutputs(NvPhysicalGpuHandle hPhysicalGpu,NvU32 *pOutputsMask) {
    return NvAPI_GPU_GetAllOutputs(hPhysicalGpu, pOutputsMask);
}

NVAPI_INTERFACE GPU_GetConnectedOutputs(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pOutputsMask) {
    return NvAPI_GPU_GetConnectedOutputs(hPhysicalGpu, pOutputsMask);
}

NVAPI_INTERFACE GPU_GetConnectedSLIOutputs(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pOutputsMask) {
    return NvAPI_GPU_GetConnectedSLIOutputs(hPhysicalGpu, pOutputsMask);
}

NVAPI_INTERFACE GPU_GetConnectedDisplayIds(NvPhysicalGpuHandle hPhysicalGpu,  NV_GPU_DISPLAYIDS* pDisplayIds, NvU32* pDisplayIdCount, NvU32 flags) {
    return NvAPI_GPU_GetConnectedDisplayIds(hPhysicalGpu, pDisplayIds, pDisplayIdCount, flags);
}

NVAPI_INTERFACE GPU_GetAllDisplayIds(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_DISPLAYIDS* pDisplayIds, NvU32* pDisplayIdCount) {
    return NvAPI_GPU_GetAllDisplayIds(hPhysicalGpu, pDisplayIds, pDisplayIdCount);
}

NVAPI_INTERFACE GPU_GetConnectedOutputsWithLidState(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pOutputsMask) {
    return NvAPI_GPU_GetConnectedOutputsWithLidState(hPhysicalGpu, pOutputsMask);
}

NVAPI_INTERFACE GPU_GetConnectedSLIOutputsWithLidState(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pOutputsMask) {
    return NvAPI_GPU_GetConnectedSLIOutputsWithLidState(hPhysicalGpu, pOutputsMask);
}

NVAPI_INTERFACE GPU_GetSystemType(NvPhysicalGpuHandle hPhysicalGpu, NV_SYSTEM_TYPE *pSystemType) {
    return NvAPI_GPU_GetSystemType(hPhysicalGpu, pSystemType);
}

NVAPI_INTERFACE GPU_GetActiveOutputs(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pOutputsMask) {
    return NvAPI_GPU_GetActiveOutputs(hPhysicalGpu, pOutputsMask);
}

NVAPI_INTERFACE GPU_SetEDID(NvPhysicalGpuHandle hPhysicalGpu, NvU32 displayOutputId, NV_EDID *pEDID) {
    return NvAPI_GPU_SetEDID(hPhysicalGpu, displayOutputId, pEDID);
}

NVAPI_INTERFACE GPU_GetOutputType(NvPhysicalGpuHandle hPhysicalGpu, NvU32 outputId, NV_GPU_OUTPUT_TYPE *pOutputType) {
    return NvAPI_GPU_GetOutputType(hPhysicalGpu, outputId, pOutputType);
}

NVAPI_INTERFACE GPU_ValidateOutputCombination(NvPhysicalGpuHandle hPhysicalGpu, NvU32 outputsMask) {
    return NvAPI_GPU_ValidateOutputCombination(hPhysicalGpu, outputsMask);
}

NVAPI_INTERFACE GPU_GetFullName(NvPhysicalGpuHandle hPhysicalGpu, NvAPI_ShortString szName) {
    return NvAPI_GPU_GetFullName(hPhysicalGpu, szName);
}

NVAPI_INTERFACE GPU_GetPCIIdentifiers(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pDeviceId,NvU32 *pSubSystemId, NvU32 *pRevisionId, NvU32 *pExtDeviceId) {
    return NvAPI_GPU_GetPCIIdentifiers(hPhysicalGpu, pDeviceId, pSubSystemId, pRevisionId, pExtDeviceId);
}

NVAPI_INTERFACE GPU_GetGPUType(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_TYPE *pGpuType) {
    return NvAPI_GPU_GetGPUType(hPhysicalGpu, pGpuType);
}

NVAPI_INTERFACE GPU_GetBusType(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_BUS_TYPE *pBusType) {
    return NvAPI_GPU_GetBusType(hPhysicalGpu, pBusType);
}

NVAPI_INTERFACE GPU_GetBusId(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pBusId) {
    return NvAPI_GPU_GetBusId(hPhysicalGpu, pBusId);
}

NVAPI_INTERFACE GPU_GetBusSlotId(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pBusSlotId) {
    return NvAPI_GPU_GetBusSlotId(hPhysicalGpu, pBusSlotId);
}

NVAPI_INTERFACE GPU_GetIRQ(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pIRQ) {
    return NvAPI_GPU_GetIRQ(hPhysicalGpu, pIRQ);
}

NVAPI_INTERFACE GPU_GetVbiosRevision(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pBiosRevision) {
    return NvAPI_GPU_GetVbiosRevision(hPhysicalGpu, pBiosRevision);
}

NVAPI_INTERFACE GPU_GetVbiosOEMRevision(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pBiosRevision) {
    return NvAPI_GPU_GetVbiosOEMRevision(hPhysicalGpu, pBiosRevision);
}

NVAPI_INTERFACE GPU_GetVbiosVersionString(NvPhysicalGpuHandle hPhysicalGpu, NvAPI_ShortString szBiosRevision) {
    return NvAPI_GPU_GetVbiosVersionString(hPhysicalGpu, szBiosRevision);
}

NVAPI_INTERFACE GPU_GetAGPAperture(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pSize) {
    return NvAPI_GPU_GetAGPAperture(hPhysicalGpu, pSize);
}

NVAPI_INTERFACE GPU_GetCurrentAGPRate(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pRate) {
    return NvAPI_GPU_GetCurrentAGPRate(hPhysicalGpu, pRate);
}

NVAPI_INTERFACE GPU_GetCurrentPCIEDownstreamWidth(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pWidth) {
    return NvAPI_GPU_GetCurrentPCIEDownstreamWidth(hPhysicalGpu, pWidth);
}

NVAPI_INTERFACE GPU_GetPhysicalFrameBufferSize(NvPhysicalGpuHandle hPhysicalGpu,NvU32 *pSize) {
    return NvAPI_GPU_GetPhysicalFrameBufferSize(hPhysicalGpu, pSize);
}

NVAPI_INTERFACE GPU_GetVirtualFrameBufferSize(NvPhysicalGpuHandle hPhysicalGpu,NvU32 *pSize) {
    return NvAPI_GPU_GetVirtualFrameBufferSize(hPhysicalGpu, pSize);
}

NVAPI_INTERFACE GPU_GetQuadroStatus(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pStatus) {
    return NvAPI_GPU_GetQuadroStatus(hPhysicalGpu, pStatus);
}

NVAPI_INTERFACE GPU_GetBoardInfo(NvPhysicalGpuHandle hPhysicalGpu, NV_BOARD_INFO *pBoardInfo) {
    return NvAPI_GPU_GetBoardInfo(hPhysicalGpu, pBoardInfo);
}

NVAPI_INTERFACE I2CRead(NvPhysicalGpuHandle hPhysicalGpu, NV_I2C_INFO *pI2cInfo) {
    return NvAPI_I2CRead(hPhysicalGpu, pI2cInfo);
}

NVAPI_INTERFACE I2CWrite(NvPhysicalGpuHandle hPhysicalGpu, NV_I2C_INFO *pI2cInfo) {
    return NvAPI_I2CWrite(hPhysicalGpu, pI2cInfo);
}

NVAPI_INTERFACE GPU_WorkstationFeatureSetup(NvPhysicalGpuHandle hPhysicalGpu, NvU32 featureEnableMask, NvU32 featureDisableMask) {
    return NvAPI_GPU_WorkstationFeatureSetup(hPhysicalGpu, featureEnableMask, featureDisableMask);
}

NVAPI_INTERFACE GPU_WorkstationFeatureQuery(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pConfiguredFeatureMask, NvU32 *pConsistentFeatureMask) {
    return NvAPI_GPU_WorkstationFeatureQuery(hPhysicalGpu, pConfiguredFeatureMask, pConsistentFeatureMask);
}

NVAPI_INTERFACE GPU_GetHDCPSupportStatus(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_GET_HDCP_SUPPORT_STATUS *pGetHDCPSupportStatus) {
    return NvAPI_GPU_GetHDCPSupportStatus(hPhysicalGpu, pGetHDCPSupportStatus);
}

NVAPI_INTERFACE GPU_GetTachReading(NvPhysicalGpuHandle hPhysicalGPU, NvU32 *pValue) {
    return NvAPI_GPU_GetTachReading(hPhysicalGPU, pValue);
}

NVAPI_INTERFACE GPU_GetECCStatusInfo(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_ECC_STATUS_INFO *pECCStatusInfo) {
    return NvAPI_GPU_GetECCStatusInfo(hPhysicalGpu, pECCStatusInfo);
}

NVAPI_INTERFACE GPU_GetECCErrorInfo(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_ECC_ERROR_INFO *pECCErrorInfo) {
    return NvAPI_GPU_GetECCErrorInfo(hPhysicalGpu, pECCErrorInfo);
}

NVAPI_INTERFACE GPU_ResetECCErrorInfo(NvPhysicalGpuHandle hPhysicalGpu, NvU8 bResetCurrent, NvU8 bResetAggregate) {
    return NvAPI_GPU_ResetECCErrorInfo(hPhysicalGpu, bResetCurrent, bResetAggregate);
}

NVAPI_INTERFACE GPU_GetECCConfigurationInfo(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_ECC_CONFIGURATION_INFO *pECCConfigurationInfo) {
    return NvAPI_GPU_GetECCConfigurationInfo(hPhysicalGpu, pECCConfigurationInfo);
}

NVAPI_INTERFACE GPU_SetECCConfiguration(NvPhysicalGpuHandle hPhysicalGpu, NvU8 bEnable, NvU8 bEnableImmediately) {
    return NvAPI_GPU_SetECCConfiguration(hPhysicalGpu, bEnable, bEnableImmediately);
}

NVAPI_INTERFACE GPU_QueryWorkstationFeatureSupport(NvPhysicalGpuHandle physicalGpu, NV_GPU_WORKSTATION_FEATURE_TYPE gpuWorkstationFeature) {
    return NvAPI_GPU_QueryWorkstationFeatureSupport(physicalGpu, gpuWorkstationFeature);
}

NVAPI_INTERFACE GPU_SetScanoutIntensity(NvU32 displayId, NV_SCANOUT_INTENSITY_DATA* scanoutIntensityData, int *pbSticky) {
    return NvAPI_GPU_SetScanoutIntensity(displayId, scanoutIntensityData, pbSticky);
}

NVAPI_INTERFACE GPU_GetScanoutIntensityState(NvU32 displayId, NV_SCANOUT_INTENSITY_STATE_DATA* scanoutIntensityStateData) {
    return NvAPI_GPU_GetScanoutIntensityState(displayId, scanoutIntensityStateData);
}

NVAPI_INTERFACE GPU_SetScanoutWarping(NvU32 displayId, NV_SCANOUT_WARPING_DATA* scanoutWarpingData, int* piMaxNumVertices, int* pbSticky) {
    return NvAPI_GPU_SetScanoutWarping(displayId, scanoutWarpingData, piMaxNumVertices, pbSticky);
}

NVAPI_INTERFACE GPU_GetScanoutWarpingState(NvU32 displayId, NV_SCANOUT_WARPING_STATE_DATA* scanoutWarpingStateData) {
    return NvAPI_GPU_GetScanoutWarpingState(displayId, scanoutWarpingStateData);
}

NVAPI_INTERFACE GPU_SetScanoutCompositionParameter(NvU32 displayId, NV_GPU_SCANOUT_COMPOSITION_PARAMETER parameter, NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE parameterValue, float *pContainer) {
    return NvAPI_GPU_SetScanoutCompositionParameter(displayId, parameter, parameterValue, pContainer);
}

NVAPI_INTERFACE GPU_GetScanoutCompositionParameter(NvU32 displayId, NV_GPU_SCANOUT_COMPOSITION_PARAMETER parameter, NV_GPU_SCANOUT_COMPOSITION_PARAMETER_VALUE *parameterData, float *pContainer) {
    return NvAPI_GPU_GetScanoutCompositionParameter(displayId, parameter, parameterData, pContainer);
}

NVAPI_INTERFACE GPU_GetScanoutConfiguration(NvU32 displayId, NvSBox* desktopRect, NvSBox* scanoutRect) {
    return NvAPI_GPU_GetScanoutConfiguration(displayId, desktopRect, scanoutRect);
}

NVAPI_INTERFACE GPU_GetScanoutConfigurationEx(NvU32 displayId, NV_SCANOUT_INFORMATION *pScanoutInformation) {
    return NvAPI_GPU_GetScanoutConfigurationEx(displayId, pScanoutInformation);
}

NVAPI_INTERFACE GPU_GetLogicalGpuInfo(NvLogicalGpuHandle hLogicalGpu, NV_LOGICAL_GPU_DATA *pLogicalGpuData) {
    return NvAPI_GPU_GetLogicalGpuInfo(hLogicalGpu, pLogicalGpuData);
}

NVAPI_INTERFACE GPU_GetPerfDecreaseInfo(NvPhysicalGpuHandle hPhysicalGpu, NvU32 *pPerfDecrInfo) {
    return NvAPI_GPU_GetPerfDecreaseInfo(hPhysicalGpu, pPerfDecrInfo);
}

NVAPI_INTERFACE GPU_GetPstatesInfoEx(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_PERF_PSTATES_INFO *pPerfPstatesInfo, NvU32 inputFlags) {
    return NvAPI_GPU_GetPstatesInfoEx(hPhysicalGpu, pPerfPstatesInfo, inputFlags);
}

NVAPI_INTERFACE GPU_GetPstates20(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_PERF_PSTATES20_INFO *pPstatesInfo) {
    return NvAPI_GPU_GetPstates20(hPhysicalGpu, pPstatesInfo);
}

NVAPI_INTERFACE GPU_GetCurrentPstate(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_PERF_PSTATE_ID *pCurrentPstate) {
    return NvAPI_GPU_GetCurrentPstate(hPhysicalGpu, pCurrentPstate);
}

NVAPI_INTERFACE GPU_GetDynamicPstatesInfoEx(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_DYNAMIC_PSTATES_INFO_EX *pDynamicPstatesInfoEx) {
    return NvAPI_GPU_GetDynamicPstatesInfoEx(hPhysicalGpu, pDynamicPstatesInfoEx);
}

NVAPI_INTERFACE GPU_GetThermalSettings(NvPhysicalGpuHandle hPhysicalGpu, NvU32 sensorIndex, NV_GPU_THERMAL_SETTINGS *pThermalSettings) {
    return NvAPI_GPU_GetThermalSettings(hPhysicalGpu, sensorIndex, pThermalSettings);
}

NVAPI_INTERFACE GPU_GetAllClockFrequencies(NvPhysicalGpuHandle hPhysicalGPU, NV_GPU_CLOCK_FREQUENCIES *pClkFreqs) {
    return NvAPI_GPU_GetAllClockFrequencies(hPhysicalGPU, pClkFreqs);
}

NVAPI_INTERFACE GPU_QueryIlluminationSupport(NV_GPU_QUERY_ILLUMINATION_SUPPORT_PARM *pIlluminationSupportInfo) {
    return NvAPI_GPU_QueryIlluminationSupport(pIlluminationSupportInfo);
}

NVAPI_INTERFACE GPU_GetIllumination(NV_GPU_GET_ILLUMINATION_PARM *pIlluminationInfo) {
    return NvAPI_GPU_GetIllumination(pIlluminationInfo);
}

NVAPI_INTERFACE GPU_SetIllumination(NV_GPU_SET_ILLUMINATION_PARM *pIlluminationInfo) {
    return NvAPI_GPU_SetIllumination(pIlluminationInfo);
}

NVAPI_INTERFACE GPU_ClientIllumDevicesGetInfo(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_CLIENT_ILLUM_DEVICE_INFO_PARAMS *pIllumDevicesInfo) {
    return NvAPI_GPU_ClientIllumDevicesGetInfo(hPhysicalGpu, pIllumDevicesInfo);
}

NVAPI_INTERFACE GPU_ClientIllumDevicesGetControl(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_PARAMS *pClientIllumDevicesControl) {
    return NvAPI_GPU_ClientIllumDevicesGetControl(hPhysicalGpu, pClientIllumDevicesControl);
}

NVAPI_INTERFACE GPU_ClientIllumDevicesSetControl(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_CLIENT_ILLUM_DEVICE_CONTROL_PARAMS *pClientIllumDevicesControl) {
    return NvAPI_GPU_ClientIllumDevicesSetControl(hPhysicalGpu, pClientIllumDevicesControl);
}

NVAPI_INTERFACE GPU_ClientIllumZonesGetInfo(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_CLIENT_ILLUM_ZONE_INFO_PARAMS *pIllumZonesInfo) {
    return NvAPI_GPU_ClientIllumZonesGetInfo(hPhysicalGpu, pIllumZonesInfo);
}

NVAPI_INTERFACE GPU_ClientIllumZonesGetControl(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_PARAMS *pIllumZonesControl) {
    return NvAPI_GPU_ClientIllumZonesGetControl(hPhysicalGpu, pIllumZonesControl);
}

NVAPI_INTERFACE GPU_ClientIllumZonesSetControl(NvPhysicalGpuHandle hPhysicalGpu, NV_GPU_CLIENT_ILLUM_ZONE_CONTROL_PARAMS *pIllumZonesControl) {
    return NvAPI_GPU_ClientIllumZonesSetControl(hPhysicalGpu, pIllumZonesControl);
}

NVAPI_INTERFACE EnumNvidiaDisplayHandle(NvU32 thisEnum, NvDisplayHandle *pNvDispHandle) {
    return NvAPI_EnumNvidiaDisplayHandle(thisEnum, pNvDispHandle);
}

NVAPI_INTERFACE EnumNvidiaUnAttachedDisplayHandle(NvU32 thisEnum, NvUnAttachedDisplayHandle *pNvUnAttachedDispHandle) {
    return NvAPI_EnumNvidiaUnAttachedDisplayHandle(thisEnum, pNvUnAttachedDispHandle);
}

NVAPI_INTERFACE CreateDisplayFromUnAttachedDisplay(NvUnAttachedDisplayHandle hNvUnAttachedDisp, NvDisplayHandle *pNvDisplay) {
    return NvAPI_CreateDisplayFromUnAttachedDisplay(hNvUnAttachedDisp, pNvDisplay);
}

NVAPI_INTERFACE GetAssociatedNvidiaDisplayHandle(const char *szDisplayName, NvDisplayHandle *pNvDispHandle) {
    return NvAPI_GetAssociatedNvidiaDisplayHandle(szDisplayName, pNvDispHandle);
}

NVAPI_INTERFACE DISP_GetAssociatedUnAttachedNvidiaDisplayHandle(const char *szDisplayName, NvUnAttachedDisplayHandle *pNvUnAttachedDispHandle) {
    return NvAPI_DISP_GetAssociatedUnAttachedNvidiaDisplayHandle(szDisplayName, pNvUnAttachedDispHandle);
}

NVAPI_INTERFACE GetAssociatedNvidiaDisplayName(NvDisplayHandle NvDispHandle, NvAPI_ShortString szDisplayName) {
    return NvAPI_GetAssociatedNvidiaDisplayName(NvDispHandle, szDisplayName);
}

NVAPI_INTERFACE GetUnAttachedAssociatedDisplayName(NvUnAttachedDisplayHandle hNvUnAttachedDisp, NvAPI_ShortString szDisplayName) {
    return NvAPI_GetUnAttachedAssociatedDisplayName(hNvUnAttachedDisp, szDisplayName);
}

NVAPI_INTERFACE EnableHWCursor(NvDisplayHandle hNvDisplay) {
    return NvAPI_EnableHWCursor(hNvDisplay);
}

NVAPI_INTERFACE DisableHWCursor(NvDisplayHandle hNvDisplay) {
    return NvAPI_DisableHWCursor(hNvDisplay);
}

NVAPI_INTERFACE GetVBlankCounter(NvDisplayHandle hNvDisplay, NvU32 *pCounter) {
    return NvAPI_GetVBlankCounter(hNvDisplay, pCounter);
}

NVAPI_INTERFACE SetRefreshRateOverride(NvDisplayHandle hNvDisplay, NvU32 outputsMask, float refreshRate, NvU32 bSetDeferred) {
    return NvAPI_SetRefreshRateOverride(hNvDisplay, outputsMask, refreshRate, bSetDeferred);
}

NVAPI_INTERFACE GetAssociatedDisplayOutputId(NvDisplayHandle hNvDisplay, NvU32 *pOutputId) {
    return NvAPI_GetAssociatedDisplayOutputId(hNvDisplay, pOutputId);
}

NVAPI_INTERFACE GetDisplayPortInfo(NvDisplayHandle hNvDisplay, NvU32 outputId, NV_DISPLAY_PORT_INFO *pInfo) {
    return NvAPI_GetDisplayPortInfo(hNvDisplay, outputId, pInfo);
}

NVAPI_INTERFACE SetDisplayPort(NvDisplayHandle hNvDisplay, NvU32 outputId, NV_DISPLAY_PORT_CONFIG *pCfg) {
    return NvAPI_SetDisplayPort(hNvDisplay, outputId, pCfg);
}

NVAPI_INTERFACE GetHDMISupportInfo(NvDisplayHandle hNvDisplay, NvU32 outputId, NV_HDMI_SUPPORT_INFO *pInfo) {
    return NvAPI_GetHDMISupportInfo(hNvDisplay, outputId, pInfo);
}

NVAPI_INTERFACE Disp_InfoFrameControl(NvU32 displayId, NV_INFOFRAME_DATA *pInfoframeData) {
    return NvAPI_Disp_InfoFrameControl(displayId, pInfoframeData);
}

NVAPI_INTERFACE Disp_ColorControl(NvU32 displayId, NV_COLOR_DATA *pColorData) {
    return NvAPI_Disp_ColorControl(displayId, pColorData);
}

NVAPI_INTERFACE Disp_GetHdrCapabilities(NvU32 displayId, NV_HDR_CAPABILITIES *pHdrCapabilities) {
    return NvAPI_Disp_GetHdrCapabilities(displayId, pHdrCapabilities);
}

NVAPI_INTERFACE Disp_HdrColorControl(NvU32 displayId, NV_HDR_COLOR_DATA *pHdrColorData) {
    return NvAPI_Disp_HdrColorControl(displayId, pHdrColorData);
}

NVAPI_INTERFACE DISP_GetTiming(NvU32 displayId, NV_TIMING_INPUT *timingInput, NV_TIMING *pTiming) {
    return NvAPI_DISP_GetTiming(displayId, timingInput, pTiming);
}

NVAPI_INTERFACE DISP_GetMonitorCapabilities(NvU32 displayId, NV_MONITOR_CAPABILITIES *pMonitorCapabilities) {
    return NvAPI_DISP_GetMonitorCapabilities(displayId, pMonitorCapabilities);
}

NVAPI_INTERFACE DISP_GetMonitorColorCapabilities(NvU32 displayId, NV_MONITOR_COLOR_CAPS *pMonitorColorCapabilities, NvU32 *pColorCapsCount) {
    return NvAPI_DISP_GetMonitorColorCapabilities(displayId, pMonitorColorCapabilities, pColorCapsCount);
}

NVAPI_INTERFACE DISP_EnumCustomDisplay(NvU32 displayId, NvU32 index, NV_CUSTOM_DISPLAY *pCustDisp) {
    return NvAPI_DISP_EnumCustomDisplay(displayId, index, pCustDisp);
}

NVAPI_INTERFACE DISP_TryCustomDisplay(NvU32 *pDisplayIds, NvU32 count, NV_CUSTOM_DISPLAY *pCustDisp) {
    return NvAPI_DISP_TryCustomDisplay(pDisplayIds, count, pCustDisp);
}

NVAPI_INTERFACE DISP_DeleteCustomDisplay(NvU32 *pDisplayIds, NvU32 count, NV_CUSTOM_DISPLAY *pCustDisp) {
    return NvAPI_DISP_DeleteCustomDisplay(pDisplayIds, count, pCustDisp);
}

NVAPI_INTERFACE DISP_SaveCustomDisplay(NvU32 *pDisplayIds, NvU32 count, NvU32 isThisOutputIdOnly, NvU32 isThisMonitorIdOnly) {
    return NvAPI_DISP_SaveCustomDisplay(pDisplayIds, count, isThisOutputIdOnly, isThisMonitorIdOnly);
}

NVAPI_INTERFACE DISP_RevertCustomDisplayTrial(NvU32* pDisplayIds, NvU32 count) {
    return NvAPI_DISP_RevertCustomDisplayTrial(pDisplayIds, count);
}

NVAPI_INTERFACE GetView(NvDisplayHandle hNvDisplay, NV_VIEW_TARGET_INFO *pTargets, NvU32 *pTargetMaskCount, NV_TARGET_VIEW_MODE *pTargetView) {
    return NvAPI_GetView(hNvDisplay, pTargets, pTargetMaskCount, pTargetView);
}

NVAPI_INTERFACE GetViewEx(NvDisplayHandle hNvDisplay, NV_DISPLAY_PATH_INFO *pPathInfo, NvU32 *pPathCount, NV_TARGET_VIEW_MODE *pTargetViewMode) {
    return NvAPI_GetViewEx(hNvDisplay, pPathInfo, pPathCount, pTargetViewMode);
}

NVAPI_INTERFACE GetSupportedViews(NvDisplayHandle hNvDisplay, NV_TARGET_VIEW_MODE *pTargetViews, NvU32 *pViewCount) {
    return NvAPI_GetSupportedViews(hNvDisplay, pTargetViews, pViewCount);
}

NVAPI_INTERFACE DISP_GetDisplayIdByDisplayName(const char *displayName, NvU32* displayId) {
    return NvAPI_DISP_GetDisplayIdByDisplayName(displayName, displayId);
}

NVAPI_INTERFACE DISP_GetDisplayConfig(NvU32 *pathInfoCount, NV_DISPLAYCONFIG_PATH_INFO *pathInfo) {
    return NvAPI_DISP_GetDisplayConfig(pathInfoCount, pathInfo);
}

NVAPI_INTERFACE DISP_SetDisplayConfig(NvU32 pathInfoCount, NV_DISPLAYCONFIG_PATH_INFO* pathInfo, NvU32 flags) {
    return NvAPI_DISP_SetDisplayConfig(pathInfoCount, pathInfo, flags);
}

NVAPI_INTERFACE Mosaic_GetSupportedTopoInfo(NV_MOSAIC_SUPPORTED_TOPO_INFO *pSupportedTopoInfo, NV_MOSAIC_TOPO_TYPE type) {
    return NvAPI_Mosaic_GetSupportedTopoInfo(pSupportedTopoInfo, type);
}

NVAPI_INTERFACE Mosaic_GetTopoGroup(NV_MOSAIC_TOPO_BRIEF *pTopoBrief, NV_MOSAIC_TOPO_GROUP *pTopoGroup) {
    return NvAPI_Mosaic_GetTopoGroup(pTopoBrief, pTopoGroup);
}

NVAPI_INTERFACE Mosaic_GetOverlapLimits(NV_MOSAIC_TOPO_BRIEF *pTopoBrief, NV_MOSAIC_DISPLAY_SETTING *pDisplaySetting, NvS32 *pMinOverlapX, NvS32 *pMaxOverlapX, NvS32 *pMinOverlapY, NvS32 *pMaxOverlapY) {
    return NvAPI_Mosaic_GetOverlapLimits(pTopoBrief, pDisplaySetting, pMinOverlapX, pMaxOverlapX, pMinOverlapY, pMaxOverlapY);
}

NVAPI_INTERFACE Mosaic_SetCurrentTopo(NV_MOSAIC_TOPO_BRIEF *pTopoBrief, NV_MOSAIC_DISPLAY_SETTING *pDisplaySetting, NvS32 overlapX, NvS32 overlapY, NvU32 enable) {
    return NvAPI_Mosaic_SetCurrentTopo(pTopoBrief, pDisplaySetting, overlapX, overlapY, enable);
}

NVAPI_INTERFACE Mosaic_GetCurrentTopo(NV_MOSAIC_TOPO_BRIEF *pTopoBrief, NV_MOSAIC_DISPLAY_SETTING *pDisplaySetting, NvS32 *pOverlapX, NvS32 *pOverlapY) {
    return NvAPI_Mosaic_GetCurrentTopo(pTopoBrief, pDisplaySetting, pOverlapX, pOverlapY);
}

NVAPI_INTERFACE Mosaic_EnableCurrentTopo(NvU32 enable) {
    return NvAPI_Mosaic_EnableCurrentTopo(enable);
}

NVAPI_INTERFACE Mosaic_SetDisplayGrids(NV_MOSAIC_GRID_TOPO *pGridTopologies, NvU32 gridCount, NvU32 setTopoFlags) {
    return NvAPI_Mosaic_SetDisplayGrids(pGridTopologies, gridCount, setTopoFlags);
}

NVAPI_INTERFACE Mosaic_ValidateDisplayGrids(NvU32 setTopoFlags, NV_MOSAIC_GRID_TOPO *pGridTopologies, NV_MOSAIC_DISPLAY_TOPO_STATUS *pTopoStatus, NvU32 gridCount) {
    return NvAPI_Mosaic_ValidateDisplayGrids(setTopoFlags, pGridTopologies, pTopoStatus, gridCount);
}

NVAPI_INTERFACE Mosaic_EnumDisplayModes(NV_MOSAIC_GRID_TOPO *pGridTopology, NV_MOSAIC_DISPLAY_SETTING *pDisplaySettings, NvU32 *pDisplayCount) {
    return NvAPI_Mosaic_EnumDisplayModes(pGridTopology, pDisplaySettings, pDisplayCount);
}

NVAPI_INTERFACE Mosaic_EnumDisplayGrids(NV_MOSAIC_GRID_TOPO *pGridTopologies, NvU32 *pGridCount) {
    return NvAPI_Mosaic_EnumDisplayGrids(pGridTopologies, pGridCount);
}

NVAPI_INTERFACE GetSupportedMosaicTopologies(NV_MOSAIC_SUPPORTED_TOPOLOGIES *pMosaicTopos) {
    return NvAPI_GetSupportedMosaicTopologies(pMosaicTopos);
}

NVAPI_INTERFACE GetCurrentMosaicTopology(NV_MOSAIC_TOPOLOGY *pMosaicTopo, NvU32 *pEnabled) {
    return NvAPI_GetCurrentMosaicTopology(pMosaicTopo, pEnabled);
}

NVAPI_INTERFACE SetCurrentMosaicTopology(NV_MOSAIC_TOPOLOGY *pMosaicTopo) {
    return NvAPI_SetCurrentMosaicTopology(pMosaicTopo);
}

NVAPI_INTERFACE EnableCurrentMosaicTopology(NvU32 enable) {
    return NvAPI_EnableCurrentMosaicTopology(enable);
}

NVAPI_INTERFACE GSync_EnumSyncDevices(NvGSyncDeviceHandle nvGSyncHandles[NVAPI_MAX_GSYNC_DEVICES], NvU32 *gsyncCount) {
    return NvAPI_GSync_EnumSyncDevices(nvGSyncHandle, gsyncCount);
}

NVAPI_INTERFACE GSync_QueryCapabilities(NvGSyncDeviceHandle hNvGSyncDevice, NV_GSYNC_CAPABILITIES *pNvGSyncCapabilities) {
    return NvAPI_GSync_QueryCapabilities(hNvGSyncDevice, pNvGSyncCapabilities);
}

NVAPI_INTERFACE GSync_GetTopology(NvGSyncDeviceHandle hNvGSyncDevice, NvU32 *gsyncGpuCount,  NV_GSYNC_GPU *gsyncGPUs, NvU32 *gsyncDisplayCount, NV_GSYNC_DISPLAY *gsyncDisplays) {
    return NvAPI_GSync_GetTopology(hNvGSyncDevice, gsyncGpuCount, gsyncGPUs, gsyncDisplayCount, gsyncDisplays);
}

NVAPI_INTERFACE GSync_SetSyncStateSettings(NvU32 gsyncDisplayCount, NV_GSYNC_DISPLAY *pGsyncDisplays, NvU32 flags) {
    return NvAPI_GSync_SetSyncStateSettings(gsyncDisplayCount, pGsyncDisplays, flags);
}

NVAPI_INTERFACE GSync_GetControlParameters(NvGSyncDeviceHandle hNvGSyncDevice, NV_GSYNC_CONTROL_PARAMS *pGsyncControls) {
    return NvAPI_GSync_GetControlParameters(hNvGSyncDevice, pGsyncControls);
}

NVAPI_INTERFACE GSync_SetControlParameters(NvGSyncDeviceHandle hNvGSyncDevice, NV_GSYNC_CONTROL_PARAMS *pGsyncControls) {
    return NvAPI_GSync_SetControlParameters(hNvGSyncDevice, pGsyncControls);
}

NVAPI_INTERFACE GSync_AdjustSyncDelay(NvGSyncDeviceHandle hNvGSyncDevice, NVAPI_GSYNC_DELAY_TYPE delayType, NV_GSYNC_DELAY *pGsyncDelay, NvU32* syncSteps) {
    return NvAPI_GSync_AdjustSyncDelay(hNvGSyncDevice, delayType, pGsyncDelay, syncSteps);
}

NVAPI_INTERFACE GSync_GetSyncStatus(NvGSyncDeviceHandle hNvGSyncDevice, NvPhysicalGpuHandle hPhysicalGpu, NV_GSYNC_STATUS *status) {
    return NvAPI_GSync_GetSyncStatus(hNvGSyncDevice, hPhysicalGpu, status);
}

NVAPI_INTERFACE GSync_GetStatusParameters(NvGSyncDeviceHandle hNvGSyncDevice, NV_GSYNC_STATUS_PARAMS *pStatusParams) {
    return NvAPI_GSync_GetStatusParameters(hNvGSyncDevice, pStatusParams);
}

NVAPI_INTERFACE D3D9_AliasSurfaceAsTexture(IDirect3DDevice9* pDev, IDirect3DSurface9* pSurface, IDirect3DTexture9 **ppTexture, DWORD dwFlag) {
    return NvAPI_D3D9_AliasSurfaceAsTexture(pDev, pSurface, ppTexture, dwFlag);
}

NVAPI_INTERFACE D3D9_StretchRectEx(IDirect3DDevice9 * pDevice, IDirect3DResource9 * pSourceResource, CONST RECT * pSourceRect, IDirect3DResource9 * pDestResource, CONST RECT * pDestRect, D3DTEXTUREFILTERTYPE Filter) {
    return NvAPI_D3D9_StretchRectEx(pDevice, pSourceResource, pSourceRect, pDestResource, pDestRect, Filter);
}

NVAPI_INTERFACE D3D9_ClearRT(IDirect3DDevice9 * pDevice, NvU32 dwNumRects, CONST RECT * pRects, float r, float g, float b, float a) {
    return NvAPI_D3D9_ClearRT(pDevice, dwNumRects, pRects, r, g, b, a);
}

NVAPI_INTERFACE D3D9_GetSurfaceHandle(IDirect3DSurface9 *pSurface,  NVDX_ObjectHandle *pHandle) {
    return NvAPI_D3D9_GetSurfaceHandle(pSurface, pHandle);
}

NVAPI_INTERFACE D3D9_VideoSetStereoInfo(IDirect3DDevice9 *pDev, NV_DX_VIDEO_STEREO_INFO *pStereoInfo) {
    return NvAPI_D3D9_VideoSetStereoInfo(pDev, pStereoInfo);
}

NVAPI_INTERFACE D3D10_SetDepthBoundsTest(ID3D10Device *pDev, NvU32 bEnable, float fMinDepth, float fMaxDepth) {
    return NvAPI_D3D10_SetDepthBoundsTest(pDev, bEnable, fMinDepth, fMaxDepth);
}

NVAPI_INTERFACE D3D11_IsNvShaderExtnOpCodeSupported(IUnknown *pDev, NvU32 opCode, bool *pSupported) {
    return NvAPI_D3D11_IsNvShaderExtnOpCodeSupported(pDev,  opCode, pSupported);
}

NVAPI_INTERFACE D3D11_SetNvShaderExtnSlot(IUnknown *pDev, NvU32 uavSlot) {
    return NvAPI_D3D11_SetNvShaderExtnSlot(pDev, uavSlot);
}

NVAPI_INTERFACE D3D12_SetNvShaderExtnSlotSpace(IUnknown *pDev, NvU32 uavSlot, NvU32 uavSpace) {
    return NvAPI_D3D12_SetNvShaderExtnSlotSpace(pDev, uavSlot, uavSpace);
}

NVAPI_INTERFACE D3D12_SetNvShaderExtnSlotSpaceLocalThread(IUnknown *pDev, NvU32 uavSlot, NvU32 uavSpace) {
    return NvAPI_D3D12_SetNvShaderExtnSlotSpaceLocalThread(pDev, uavSlot, uavSpace);
}

NVAPI_INTERFACE D3D11_SetNvShaderExtnSlotLocalThread(IUnknown *pDev, NvU32 uavSlot) {
    return NvAPI_D3D11_SetNvShaderExtnSlotLocalThread(pDev, uavSlot);
}

NVAPI_INTERFACE D3D11_BeginUAVOverlapEx(IUnknown *pDeviceOrContext, NvU32 insertWFIFlags) {
    return NvAPI_D3D11_BeginUAVOverlapEx(pDeviceOrContext, insertWFIFlags);
}

NVAPI_INTERFACE D3D11_BeginUAVOverlap(IUnknown *pDeviceOrContext) {
    return NvAPI_D3D11_BeginUAVOverlap(pDeviceOrContext);
}

NVAPI_INTERFACE D3D11_EndUAVOverlap(IUnknown *pDeviceOrContext) {
    return NvAPI_D3D11_EndUAVOverlap(pDeviceOrContext);
}

NVAPI_INTERFACE D3D_SetFPSIndicatorState(IUnknown *pDev, NvU8 doEnable) {
    return NvAPI_D3D_SetFPSIndicatorState(pDev, doEnable);
}

NVAPI_INTERFACE D3D9_Present(IDirect3DDevice9 *pDevice, IDirect3DSwapChain9 *pSwapChain, const RECT *pSourceRect, const RECT *pDestRect, HWND hDestWindowOverride, const RGNDATA *pDirtyRegion) {
    return NvAPI_D3D9_Present(pDevice, pSwapChain, pSourceRect, pDestRect, hDestWindowOverride, pDirtyRegion);
}

NVAPI_INTERFACE D3D9_QueryFrameCount(IDirect3DDevice9 *pDevice, NvU32 *pFrameCount) {
    return NvAPI_D3D9_QueryFrameCount(pDevice, pFrameCount);
}

NVAPI_INTERFACE D3D9_ResetFrameCount(IDirect3DDevice9 *pDevice) {
    return NvAPI_D3D9_ResetFrameCount(pDevice);
}

NVAPI_INTERFACE D3D9_QueryMaxSwapGroup(IDirect3DDevice9 *pDevice,  NvU32 *pMaxGroups, NvU32 *pMaxBarriers) {
    return NvAPI_D3D9_QueryMaxSwapGroup(pDevice, pMaxGroups, pMaxBarriers);
}

NVAPI_INTERFACE D3D9_QuerySwapGroup(IDirect3DDevice9 *pDevice,  IDirect3DSwapChain9 *pSwapChain, NvU32 *pSwapGroup, NvU32 *pSwapBarrier) {
    return NvAPI_D3D9_QuerySwapGroup(pDevice, pSwapChain, pSwapGroup, pSwapBarrier);
}

NVAPI_INTERFACE D3D9_JoinSwapGroup(IDirect3DDevice9 *pDevice,  IDirect3DSwapChain9 *pSwapChain, NvU32 group, BOOL blocking) {
    return NvAPI_D3D9_JoinSwapGroup(pDevice, pSwapChain, group, blocking);
}

NVAPI_INTERFACE D3D9_BindSwapBarrier(IDirect3DDevice9 *pDevice,  NvU32 group, NvU32 barrier) {
    return NvAPI_D3D9_BindSwapBarrier(pDevice, group, barrier);
}

NVAPI_INTERFACE D3D1x_Present(IUnknown *pDevice, IDXGISwapChain *pSwapChain, UINT SyncInterval, UINT Flags) {
    return NvAPI_D3D1x_Present(pDevice, pSwapChain, SyncInterval, Flags);
}

NVAPI_INTERFACE D3D1x_QueryFrameCount(IUnknown *pDevice, NvU32 *pFrameCount) {
    return NvAPI_D3D1x_QueryFrameCount(pDevice, pFrameCount);
}

NVAPI_INTERFACE D3D1x_ResetFrameCount(IUnknown *pDevice) {
    return NvAPI_D3D1x_ResetFrameCount(pDevice);
}

NVAPI_INTERFACE D3D1x_QueryMaxSwapGroup(IUnknown *pDevice,  NvU32 *pMaxGroups, NvU32 *pMaxBarriers) {
    return NvAPI_D3D1x_QueryMaxSwapGroup(pDevice, pMaxGroups, pMaxBarriers);
}

NVAPI_INTERFACE D3D1x_QuerySwapGroup(IUnknown *pDevice,  IDXGISwapChain  *pSwapChain, NvU32 *pSwapGroup, NvU32 *pSwapBarrier) {
    return NvAPI_D3D1x_QuerySwapGroup(pDevice,  pSwapChain, pSwapGroup, pSwapBarrier);
}

NVAPI_INTERFACE D3D1x_JoinSwapGroup(IUnknown *pDevice,  IDXGISwapChain  *pSwapChain, NvU32 group, BOOL blocking) {
    return NvAPI_D3D1x_JoinSwapGroup(pDevice,  pSwapChain, group, blocking);
}

NVAPI_INTERFACE D3D1x_BindSwapBarrier(IUnknown *pDevice,  NvU32 group, NvU32 barrier) {
    return NvAPI_D3D1x_BindSwapBarrier(pDevice, group, barrier);
}

NVAPI_INTERFACE D3D11_CreateRasterizerState(ID3D11Device *pDevice, const NvAPI_D3D11_RASTERIZER_DESC_EX *pRasterizerDesc, ID3D11RasterizerState **ppRasterizerState) {
    return NvAPI_D3D11_CreateRasterizerState(pDevice, pRasterizerDesc, ppRasterizerState);
}

NVAPI_INTERFACE D3D_ConfigureAnsel(IUnknown *pDevice, NVAPI_ANSEL_CONFIGURATION_STRUCT *pNLSConfig) {
    return NvAPI_D3D_ConfigureAnsel(pDevice, pNLSConfig);
}

NVAPI_INTERFACE D3D11_CreateTiledTexture2DArray(ID3D11Device *pDevice, const D3D11_TEXTURE2D_DESC *pDesc, const D3D11_SUBRESOURCE_DATA *pInitialData, ID3D11Texture2D **ppTexture2D) {
    return NvAPI_D3D11_CreateTiledTexture2DArray(pDevice, pDesc, pInitialData, ppTexture2D);
}

NVAPI_INTERFACE D3D11_CheckFeatureSupport(ID3D11Device *pDevice, NV_D3D11_FEATURE Feature, void *pFeatureSupportData, UINT FeatureSupportDataSize) {
    return NvAPI_D3D11_CheckFeatureSupport(pDevice, Feature, pFeatureSupportData, FeatureSupportDataSize);
}

NVAPI_INTERFACE D3D11_CreateImplicitMSAATexture2D(ID3D11Device *pDevice, const D3D11_TEXTURE2D_DESC *pDesc, ID3D11Texture2D **ppTexture2D) {
    return NvAPI_D3D11_CreateImplicitMSAATexture2D(pDevice, pDesc, ppTexture2D);
}

NVAPI_INTERFACE D3D12_CreateCommittedImplicitMSAATexture2D(ID3D12Device* pDevice,  const D3D12_HEAP_PROPERTIES *pHeapProperties, D3D12_HEAP_FLAGS HeapFlags, const D3D12_RESOURCE_DESC *pDesc, D3D12_RESOURCE_STATES InitialResourceState, const D3D12_CLEAR_VALUE *pOptimizedClearValue, REFIID riidResource, void **ppvResource) {
    return NvAPI_D3D12_CreateCommittedImplicitMSAATexture2D(pDevice, pHeapProperties, HeapFlags,  pDesc, InitialResourceState,  pOptimizedClearValue, riidResource, ppvResource);
}

NVAPI_INTERFACE D3D11_ResolveSubresourceRegion(ID3D11Device *pDevice, ID3D11Texture2D  *pDstResource, UINT DstSubresource, UINT DstX, UINT  DstY, ID3D11Texture2D  *pSrcResource, UINT SrcSubresource, const RECT *pSrcRect, DXGI_FORMAT Format, NV_RESOLVE_MODE ResolveMode) {
    return NvAPI_D3D11_ResolveSubresourceRegion(pDevice, pDstResource, DstSubresource, DstX, DstY, pSrcResource, SrcSubresource, pSrcRect, Format, ResolveMode);
}

NVAPI_INTERFACE D3D12_ResolveSubresourceRegion(ID3D12GraphicsCommandList1* pCommandList, ID3D12Resource  *pDstResource, UINT DstSubresource, UINT DstX, UINT DstY, ID3D12Resource *pSrcResource, UINT SrcSubresource, RECT *pSrcRect, DXGI_FORMAT Format, NV_RESOLVE_MODE ResolveMode) {
    return NvAPI_D3D12_ResolveSubresourceRegion(pCommandList, pDstResource, DstSubresource, DstX, DstY, pSrcResource, SrcSubresource, pSrcRect, Format, ResolveMode);
}

NVAPI_INTERFACE D3D11_TiledTexture2DArrayGetDesc(ID3D11Texture2D *pTiledTexture2DArray, D3D11_TEXTURE2D_DESC *pDesc) {
    return NvAPI_D3D11_TiledTexture2DArrayGetDesc(pTiledTexture2DArray, pDesc);
}

NVAPI_INTERFACE D3D11_UpdateTileMappings(ID3D11DeviceContext2 *pDeviceContext, ID3D11Resource *pTiledResource, UINT NumTiledResourceRegions, const D3D11_TILED_RESOURCE_COORDINATE *pTiledResourceRegionStartCoordinates, const D3D11_TILE_REGION_SIZE *pTiledResourceRegionSizes, ID3D11Buffer *pTilePool, UINT NumRanges, const UINT *pRangeFlags, const UINT *pTilePoolStartOffsets, const UINT *pRangeTileCounts, UINT Flags) {
    return NvAPI_D3D11_UpdateTileMappings(pDeviceContext, pTiledResource, NumTiledResourceRegions, pTiledResourceRegionStartCoordinates, pTiledResourceRegionSizes, pTilePool, NumRanges, pRangeFlags, pTilePoolStartOffsets, pRangeTileCounts, Flags);
}

NVAPI_INTERFACE D3D11_CopyTileMappings(ID3D11DeviceContext *pDeviceContext, ID3D11Resource *pDestTiledResource, const D3D11_TILED_RESOURCE_COORDINATE *pDestRegionStartCoordinate, ID3D11Resource *pSourceTiledResource, const D3D11_TILED_RESOURCE_COORDINATE *pSourceRegionStartCoordinate, const D3D11_TILE_REGION_SIZE *pTileRegionSize, UINT Flags) {
    return NvAPI_D3D11_CopyTileMappings(pDeviceContext, pDestTiledResource, pDestRegionStartCoordinate, pSourceTiledResource, pSourceRegionStartCoordinate, pTileRegionSize, Flags);
}

NVAPI_INTERFACE D3D11_TiledResourceBarrier(ID3D11DeviceContext *pDeviceContext, ID3D11Resource *pTiledResourceAccessBeforeBarrier, ID3D11Resource *pTiledResourceAccessAfterBarrier) {
    return NvAPI_D3D11_TiledResourceBarrier(pDeviceContext, pTiledResourceAccessBeforeBarrier, pTiledResourceAccessAfterBarrier);
}

NVAPI_INTERFACE D3D11_AliasMSAATexture2DAsNonMSAA(ID3D11Device *pDevice, ID3D11Texture2D *pInputTex, ID3D11Texture2D **ppOutTex) {
    return NvAPI_D3D11_AliasMSAATexture2DAsNonMSAA(pDevice, pInputTex, ppOutTex);
}

NVAPI_INTERFACE D3D11_CreateGeometryShaderEx_2(ID3D11Device *pDevice, const void *pShaderBytecode,  SIZE_T BytecodeLength, ID3D11ClassLinkage *pClassLinkage, const NvAPI_D3D11_CREATE_GEOMETRY_SHADER_EX *pCreateGeometryShaderExArgs, ID3D11GeometryShader **ppGeometryShader) {
    return NvAPI_D3D11_CreateGeometryShaderEx_2(pDevice, pShaderBytecode, BytecodeLength, pClassLinkage, pCreateGeometryShaderExArgs, ppGeometryShader);
}

NVAPI_INTERFACE D3D11_CreateVertexShaderEx(ID3D11Device *pDevice, const void *pShaderBytecode, SIZE_T BytecodeLength, ID3D11ClassLinkage *pClassLinkage, const NvAPI_D3D11_CREATE_VERTEX_SHADER_EX *pCreateVertexShaderExArgs, ID3D11VertexShader **ppVertexShader) {
    return NvAPI_D3D11_CreateVertexShaderEx(pDevice, pShaderBytecode, BytecodeLength, pClassLinkage, pCreateVertexShaderExArgs, ppVertexShader);
}

NVAPI_INTERFACE D3D11_CreateHullShaderEx(ID3D11Device *pDevice, const void *pShaderBytecode,  SIZE_T BytecodeLength, ID3D11ClassLinkage *pClassLinkage, const NvAPI_D3D11_CREATE_HULL_SHADER_EX *pCreateHullShaderExArgs, ID3D11HullShader **ppHullShader) {
    return NvAPI_D3D11_CreateHullShaderEx(pDevice, pShaderBytecode, BytecodeLength, pClassLinkage, pCreateHullShaderExArgs, ppHullShader);
}

NVAPI_INTERFACE D3D11_CreateDomainShaderEx(ID3D11Device *pDevice, const void *pShaderBytecode, SIZE_T BytecodeLength, ID3D11ClassLinkage *pClassLinkage, const NvAPI_D3D11_CREATE_DOMAIN_SHADER_EX *pCreateDomainShaderExArgs, ID3D11DomainShader **ppDomainShader) {
    return NvAPI_D3D11_CreateDomainShaderEx(pDevice, pShaderBytecode, BytecodeLength, pClassLinkage, pCreateDomainShaderExArgs, ppDomainShader);
}

NVAPI_INTERFACE D3D11_CreatePixelShaderEx_2(ID3D11Device *pDevice, const void *pShaderBytecode,  SIZE_T BytecodeLength, ID3D11ClassLinkage *pClassLinkage, const NvAPI_D3D11_CREATE_PIXEL_SHADER_EX *pCreatePixelShaderExArgs, ID3D11PixelShader **ppPixelShader) {
    return NvAPI_D3D11_CreatePixelShaderEx_2(pDevice, pShaderBytecode, BytecodeLength, pClassLinkage, pCreatePixelShaderExArgs, ppPixelShader);
}

NVAPI_INTERFACE D3D11_CreateFastGeometryShaderExplicit(ID3D11Device *pDevice, const void *pShaderBytecode, SIZE_T BytecodeLength, ID3D11ClassLinkage *pClassLinkage, const NvAPI_D3D11_CREATE_FASTGS_EXPLICIT_DESC *pCreateFastGSArgs, ID3D11GeometryShader **ppGeometryShader) {
    return NvAPI_D3D11_CreateFastGeometryShaderExplicit(pDevice, pShaderBytecode, BytecodeLength, pClassLinkage, pCreateFastGSArgs, ppGeometryShader);
}

NVAPI_INTERFACE D3D11_CreateFastGeometryShader(ID3D11Device *pDevice, const void *pShaderBytecode,  SIZE_T BytecodeLength, ID3D11ClassLinkage *pClassLinkage, ID3D11GeometryShader **ppGeometryShader) {
    return NvAPI_D3D11_CreateFastGeometryShader(pDevice, pShaderBytecode, BytecodeLength, pClassLinkage, ppGeometryShader);
}

NVAPI_INTERFACE D3D11_DecompressView(ID3D11Device* pDevice, ID3D11DeviceContext *pDeviceContext, ID3D11View* pView) {
    return NvAPI_D3D11_DecompressView(pDevice, pDeviceContext, pView);
}

NVAPI_INTERFACE D3D12_CreateGraphicsPipelineState(ID3D12Device *pDevice, const D3D12_GRAPHICS_PIPELINE_STATE_DESC *pPSODesc, NvU32 numExtensions, const NVAPI_D3D12_PSO_EXTENSION_DESC** ppExtensions, ID3D12PipelineState **ppPSO) {
    return NvAPI_D3D12_CreateGraphicsPipelineState(pDevice, pPSODesc, numExtensions, ppExtensions, ppPSO);
}

NVAPI_INTERFACE D3D12_CreateComputePipelineState(ID3D12Device *pDevice, const D3D12_COMPUTE_PIPELINE_STATE_DESC *pPSODesc, NvU32 numExtensions, const NVAPI_D3D12_PSO_EXTENSION_DESC** ppExtensions, ID3D12PipelineState **ppPSO) {
    return NvAPI_D3D12_CreateComputePipelineState(pDevice, pPSODesc, numExtensions, ppExtensions, ppPSO);
}

NVAPI_INTERFACE D3D12_SetDepthBoundsTestValues(ID3D12GraphicsCommandList *pCommandList, const float minDepth, const float maxDepth) {
    return NvAPI_D3D12_SetDepthBoundsTestValues(pCommandList, minDepth, maxDepth);
}

NVAPI_INTERFACE D3D12_CreateReservedResource(ID3D12Device *pDevice, const D3D12_RESOURCE_DESC *pDesc, D3D12_RESOURCE_STATES InitialState, const D3D12_CLEAR_VALUE *pOptimizedClearValue, REFIID riid, void **ppvResource, bool bTexture2DArrayMipPack, ID3D12Heap *pHeap) {
    return NvAPI_D3D12_CreateReservedResource(pDevice, pDesc, InitialState, pOptimizedClearValue, riid, ppvResource, bTexture2DArrayMipPack, pHeap);
}

NVAPI_INTERFACE D3D12_CreateHeap(ID3D12Device *pDevice, const D3D12_HEAP_DESC  *pDesc, REFIID riid, void **ppvHeap) {
    return NvAPI_D3D12_CreateHeap(pDevice, pDesc, riid, ppvHeap);
}

NVAPI_INTERFACE D3D12_ReservedResourceGetDesc(ID3D12Resource *pReservedResource, D3D12_RESOURCE_DESC *pDesc) {
    return NvAPI_D3D12_ReservedResourceGetDesc(pReservedResource, pDesc);
}

NVAPI_INTERFACE D3D12_UpdateTileMappings(ID3D12CommandQueue *pCommandQueue, ID3D12Resource *pResource, UINT NumResourceRegions, const D3D12_TILED_RESOURCE_COORDINATE *pResourceRegionStartCoordinates, const D3D12_TILE_REGION_SIZE *pResourceRegionSizes, ID3D12Heap *pHeap, UINT NumRanges, const D3D12_TILE_RANGE_FLAGS *pRangeFlags, const UINT *pHeapRangeStartOffsets, const UINT *pRangeTileCounts, D3D12_TILE_MAPPING_FLAGS Flags) {
    return NvAPI_D3D12_UpdateTileMappings(pCommandQueue, pResource, NumResourceRegions, pResourceRegionStartCoordinates, pResourceRegionSizes, pHeap, NumRanges, pRangeFlags, pHeapRangeStartOffsets, pRangeTileCounts, Flags);
}

NVAPI_INTERFACE D3D12_CopyTileMappings(ID3D12CommandQueue *pCommandQueue, ID3D12Resource *pDstResource, const D3D12_TILED_RESOURCE_COORDINATE *pDstRegionStartCoordinate, ID3D12Resource *pSrcResource, const D3D12_TILED_RESOURCE_COORDINATE *pSrcRegionStartCoordinate, const D3D12_TILE_REGION_SIZE *pRegionSize, D3D12_TILE_MAPPING_FLAGS Flags) {
    return NvAPI_D3D12_CopyTileMappings(pCommandQueue, pDstResource, pDstRegionStartCoordinate, pSrcResource, pSrcRegionStartCoordinate, pRegionSize, Flags);
}

NVAPI_INTERFACE D3D12_ResourceAliasingBarrier(ID3D12GraphicsCommandList *pCommandList, UINT NumBarriers, const D3D12_RESOURCE_BARRIER *pBarriers) {
    return NvAPI_D3D12_ResourceAliasingBarrier(pCommandList, NumBarriers, pBarriers);
}

NVAPI_INTERFACE D3D11_EnumerateMetaCommands(ID3D11Device *pDevice, NvU32 *pNumMetaCommands, NVAPI_META_COMMAND_DESC *pDescs) {
    return NvAPI_D3D11_EnumerateMetaCommands(pDevice, pNumMetaCommands, pDescs);
}

NVAPI_INTERFACE D3D11_CreateMetaCommand(ID3D11Device *pDevice, REFGUID CommandId, const void *pCreationParametersData, NvU32 CreationParametersDataSize, ID3D11NvMetaCommand    **ppMetaCommand) {
    return NvAPI_D3D11_CreateMetaCommand(pDevice, CommandId, pCreationParametersData, CreationParametersDataSize, ppMetaCommand);
}

NVAPI_INTERFACE D3D11_InitializeMetaCommand(ID3D11DeviceContext *pDeviceContext, ID3D11NvMetaCommand *pMetaCommand, const void *pInitializationParametersData, NvU32 InitializationParametersDataSize) {
    return NvAPI_D3D11_InitializeMetaCommandpDeviceContext, pMetaCommand, pInitializationParametersData, InitializationParametersDataSize);
}

NVAPI_INTERFACE D3D11_ExecuteMetaCommand(ID3D11DeviceContext *pDeviceContext, ID3D11NvMetaCommand *pMetaCommand, const void *pExecutionParametersData, ExecutionParametersDataSize) {
    return NvAPI_D3D11_ExecuteMetaCommand(pDeviceContext, pMetaCommand, pExecutionParametersData, ExecutionParametersDataSize);
}

NVAPI_INTERFACE D3D12_EnumerateMetaCommands(ID3D12Device *pDevice, NvU32 *pNumMetaCommands, NVAPI_META_COMMAND_DESC *pDescs) {
    return NvAPI_D3D12_EnumerateMetaCommands(pDevice, pNumMetaCommands, pDescs);
}

NVAPI_INTERFACE D3D12_CreateMetaCommand(ID3D12Device *pDevice, REFGUID CommandId, NvU32 NodeMask, const void *pCreationParametersData, NvU32 CreationParametersDataSize, ID3D12NvMetaCommand  **ppMetaCommand) {
    return NvAPI_D3D12_CreateMetaCommand(pDevice, CommandId, NodeMask, pCreationParametersData, CreationParametersDataSize, ppMetaCommand);
}

NVAPI_INTERFACE D3D12_InitializeMetaCommand(ID3D12GraphicsCommandList *pCommandlist, ID3D12NvMetaCommand *pMetaCommand, const void *pInitializationParametersData, NvU32 InitializationParametersDataSize) {
    return NvAPI_D3D12_InitializeMetaCommand(pCommandlist, pMetaCommand, pInitializationParametersData, InitializationParametersDataSize);
}

NVAPI_INTERFACE D3D12_ExecuteMetaCommand(ID3D12GraphicsCommandList *pCommandlist, ID3D12NvMetaCommand *pMetaCommand, const void  *pExecutionParametersData, NvU32 ExecutionParametersDataSize) {
    return NvAPI_D3D12_ExecuteMetaCommand(pCommandlist, pMetaCommand, pExecutionParametersData, ExecutionParametersDataSize);
}

NVAPI_INTERFACE D3D12_IsNvShaderExtnOpCodeSupported(ID3D12Device *pDevice, NvU32 opCode, bool *pSupported) {
    return NvAPI_D3D12_IsNvShaderExtnOpCodeSupported(pDevice,  opCode, pSupported);
}

NVAPI_INTERFACE D3D_IsGSyncCapable(IUnknown *pDeviceOrContext, NVDX_ObjectHandle primarySurface, BOOL *pIsGsyncCapable) {
    return NvAPI_D3D_IsGSyncCapable(pDeviceOrContext, primarySurface, pIsGsyncCapable);
}

NVAPI_INTERFACE D3D_IsGSyncActive(IUnknown *pDeviceOrContext, NVDX_ObjectHandle primarySurface, BOOL *pIsGsyncActive) {
    return NvAPI_D3D_IsGSyncActive(pDeviceOrContext, primarySurface, pIsGsyncActive);
}

NVAPI_INTERFACE D3D1x_DisableShaderDiskCache(IUnknown *pDevice) {
    return NvAPI_D3D1x_DisableShaderDiskCache(pDevice);
}

NVAPI_INTERFACE D3D11_MultiGPU_GetCaps(PNV_MULTIGPU_CAPS pMultiGPUCaps) {
    return NvAPI_D3D11_MultiGPU_GetCaps(pMultiGPUCaps);
}

NVAPI_INTERFACE D3D11_MultiGPU_Init(bool bEnable) {
    return NvAPI_D3D11_MultiGPU_Init(bEnable);
}

NVAPI_INTERFACE D3D11_CreateMultiGPUDevice(ID3D11Device *pDevice, ULONG version, ULONG *currentVersion, ID3D11MultiGPUDevice **ppD3D11MultiGPUDevice, UINT maxGpus=ALL_GPUS) {
    return NvAPI_D3D11_CreateMultiGPUDevice(pDevice, version, currentVersion, ppD3D11MultiGPUDevice, maxGpus);
}

NVAPI_INTERFACE D3D_QuerySinglePassStereoSupport(IUnknown *pDevice, NV_QUERY_SINGLE_PASS_STEREO_SUPPORT_PARAMS *pQuerySinglePassStereoSupportedParams) {
    return NvAPI_D3D_QuerySinglePassStereoSupport(pDevice, pQuerySinglePassStereoSupportedParams);
}

NVAPI_INTERFACE D3D_SetSinglePassStereoMode(IUnknown *pDevOrContext, NvU32 numViews, NvU32 renderTargetIndexOffset, NvU8 independentViewportMaskEnable) {
    return NvAPI_D3D_SetSinglePassStereoMode(pDevOrContext, numViews, renderTargetIndexOffset, independentViewportMaskEnable);
}

NVAPI_INTERFACE D3D12_QuerySinglePassStereoSupport(ID3D12Device *pDevice, NV_QUERY_SINGLE_PASS_STEREO_SUPPORT_PARAMS *pQuerySinglePassStereoSupportedParams) {
    return NvAPI_D3D12_QuerySinglePassStereoSupport(pDevice, pQuerySinglePassStereoSupportedParams);
}

NVAPI_INTERFACE D3D12_SetSinglePassStereoMode(ID3D12GraphicsCommandList* pCommandList, NvU32 numViews, NvU32 renderTargetIndexOffset, NvU8 independentViewportMaskEnable) {
    return NvAPI_D3D12_SetSinglePassStereoMode(pCommandList, numViews, renderTargetIndexOffset, independentViewportMaskEnable);
}

NVAPI_INTERFACE D3D_QueryMultiViewSupport(IUnknown *pDevice, NV_QUERY_MULTIVIEW_SUPPORT_PARAMS *pQueryMultiViewSupportedParams) {
    return NvAPI_D3D_QueryMultiViewSupport(pDevice, pQueryMultiViewSupportedParams);
}

NVAPI_INTERFACE D3D_SetMultiViewMode(IUnknown *pDevOrContext, NV_MULTIVIEW_PARAMS *pMultiViewParams) {
    return NvAPI_D3D_SetMultiViewMode(pDevOrContext, pMultiViewParams);
}

NVAPI_INTERFACE D3D_QueryModifiedWSupport(IUnknown *pDev, NV_QUERY_MODIFIED_W_SUPPORT_PARAMS *pQueryModifiedWSupportedParams) {
    return NvAPI_D3D_QueryModifiedWSupport(pDev, pQueryModifiedWSupportedParams);
}

NVAPI_INTERFACE D3D_SetModifiedWMode(IUnknown *pDevOrContext, NV_MODIFIED_W_PARAMS *psModifiedWParams) {
    return NvAPI_D3D_SetModifiedWMode(pDevOrContext, psModifiedWParams);
}

NVAPI_INTERFACE D3D12_QueryModifiedWSupport(ID3D12Device *pDevice, NV_QUERY_MODIFIED_W_SUPPORT_PARAMS *pQueryModifiedWSupportedParams) {
    return NvAPI_D3D12_QueryModifiedWSupport(pDevice, pQueryModifiedWSupportedParams);
}

NVAPI_INTERFACE D3D12_SetModifiedWMode(ID3D12GraphicsCommandList* pCommandList, NV_MODIFIED_W_PARAMS *pModifiedWParams) {
    return NvAPI_D3D12_SetModifiedWMode(pCommandList, pModifiedWParams);
}

NVAPI_INTERFACE D3D_CreateLateLatchObject(IUnknown *pDevice, NV_D3D_LATELATCH_OBJECT_DESC* pLateLatchObjectDesc) {
    return NvAPI_D3D_CreateLateLatchObject(pDevice, pLateLatchObjectDesc);
}

NVAPI_INTERFACE D3D_QueryLateLatchSupport(IUnknown *pDevice, NV_QUERY_LATELATCH_SUPPORT_PARAMS *pQueryLateLatchSupportParams) {
    return NvAPI_D3D_QueryLateLatchSupport(pDevice, pQueryLateLatchSupportParams);
}

NVAPI_INTERFACE D3D_RegisterDevice(IUnknown *pDev) {
    return NvAPI_D3D_RegisterDevice(pDev);
}

NVAPI_INTERFACE D3D11_MultiDrawInstancedIndirect(ID3D11DeviceContext *pDevContext11, NvU32 drawCount, ID3D11Buffer *pBuffer, NvU32 alignedByteOffsetForArgs, NvU32 alignedByteStrideForArgs) {
    return NvAPI_D3D11_MultiDrawInstancedIndirect(pDevContext11, drawCount, pBuffer, alignedByteOffsetForArgs, alignedByteStrideForArgs);
}

NVAPI_INTERFACE D3D11_MultiDrawIndexedInstancedIndirect(ID3D11DeviceContext *pDevContext11, NvU32 drawCount, ID3D11Buffer *pBuffer, NvU32 alignedByteOffsetForArgs, NvU32 alignedByteStrideForArgs) {
    return NvAPI_D3D11_MultiDrawIndexedInstancedIndirect(pDevContext11, drawCount, pBuffer, alignedByteOffsetForArgs, alignedByteStrideForArgs);
}

NVAPI_INTERFACE D3D_ImplicitSLIControl(IMPLICIT_SLI_CONTROL implicitSLIControl) {
    return NvAPI_D3D_ImplicitSLIControl(implicitSLIControl);
}

NVAPI_INTERFACE D3D12_UseDriverHeapPriorities(ID3D12Device *pDevice) {
    return NvAPI_D3D12_UseDriverHeapPriorities(pDevice);
}

NVAPI_INTERFACE D3D12_Mosaic_GetCompanionAllocations(NV_D3D12_MOSAIC_GETCOMPANIONALLOCATIONS *params) {
    return NvAPI_D3D12_Mosaic_GetCompanionAllocations(params);
}

NVAPI_INTERFACE D3D12_Mosaic_GetViewportAndGpuPartitions(NV_D3D12_MOSAIC_GETVIEWPORTANDGPUPARTITIONS *params) {
    return NvAPI_D3D12_Mosaic_GetViewportAndGpuPartitions(params);
}

NVAPI_INTERFACE D3D1x_GetGraphicsCapabilities(IUnknown *pDevice, NvU32 structVersion, NV_D3D1x_GRAPHICS_CAPS *pGraphicsCaps) {
    return NvAPI_D3D1x_GetGraphicsCapabilities(pDevice, structVersion, pGraphicsCaps);
}

NVAPI_INTERFACE D3D11_RSSetExclusiveScissorRects(IUnknown *pContext, NV_D3D11_EXCLUSIVE_SCISSOR_RECTS_DESC *pExclusiveScissorRectsDesc) {
    return NvAPI_D3D11_RSSetExclusiveScissorRects(pContext, pExclusiveScissorRectsDesc);
}

NVAPI_INTERFACE D3D11_RSSetViewportsPixelShadingRates(IUnknown *pContext, NV_D3D11_VIEWPORTS_SHADING_RATE_DESC *pShadingRateDesc) {
    return NvAPI_D3D11_RSSetViewportsPixelShadingRates(pContext, pShadingRateDesc);
}

NVAPI_INTERFACE D3D11_CreateShadingRateResourceView(ID3D11Device *pDevice, ID3D11Resource *pShadingRateResource, NV_D3D11_SHADING_RATE_RESOURCE_VIEW_DESC *pShadingRateResourceViewDesc, ID3D11NvShadingRateResourceView **ppShadingRateResourceView) {
    return NvAPI_D3D11_CreateShadingRateResourceView(pDevice, pShadingRateResource, pShadingRateResourceViewDesc, ppShadingRateResourceView);
}

NVAPI_INTERFACE D3D11_RSSetShadingRateResourceView(IUnknown *pContext, ID3D11NvShadingRateResourceView *pShadingRateResourceView) {
    return NvAPI_D3D11_RSSetShadingRateResourceView(pContext, pShadingRateResourceView);
}

NVAPI_INTERFACE D3D11_RSGetPixelShadingRateSampleOrder(IUnknown *pContext, NV_PIXEL_SHADING_RATE_SAMPLE_ORDER_TABLE* pSampleOrderTable) {
    return NvAPI_D3D11_RSGetPixelShadingRateSampleOrder(pContext, pSampleOrderTable);
}

NVAPI_INTERFACE D3D11_RSSetPixelShadingRateSampleOrder(IUnknown *pContext, NV_PIXEL_SHADING_RATE_SAMPLE_ORDER_TABLE* pSampleOrderTable) {
    return NvAPI_D3D11_RSSetPixelShadingRateSampleOrder(pContext, pSampleOrderTable);
}

NVAPI_INTERFACE D3D_InitializeVRSHelper(IUnknown *pDevice, NV_VRS_HELPER_INIT_PARAMS *pInitializeVRSHelperParams) {
    return NvAPI_D3D_InitializeVRSHelper(pDevice, pInitializeVRSHelperParams);
}

NVAPI_INTERFACE D3D_InitializeNvGazeHandler(IUnknown *pDevice, NV_GAZE_HANDLER_INIT_PARAMS *pInitializeNvGazeHandlerParams) {
    return NvAPI_D3D_InitializeNvGazeHandler(pDevice, pInitializeNvGazeHandlerParams);
}

NVAPI_INTERFACE D3D_InitializeSMPAssist(IUnknown *pDevice, NV_SMP_ASSIST_INITIALIZE_PARAMS *pSMPAssistInitParams) {
    return NvAPI_D3D_InitializeSMPAssist(pDevice, pSMPAssistInitParams);
}

NVAPI_INTERFACE D3D_QuerySMPAssistSupport(IUnknown *pDev, NV_QUERY_SMP_ASSIST_SUPPORT_PARAMS *pQuerySMPAssistSupportParams) {
    return NvAPI_D3D_QuerySMPAssistSupport(pDev, pQuerySMPAssistSupportParams);
}

NVAPI_INTERFACE VIO_GetCapabilities(NvVioHandle hVioHandle, NVVIOCAPS *pAdapterCaps) {
    return NvAPI_VIO_GetCapabilities(hVioHandle, pAdapterCaps);
}

NVAPI_INTERFACE VIO_Open(NvVioHandle hVioHandle, NvU32 vioClass, NVVIOOWNERTYPE ownerType) {
    return NvAPI_VIO_Open(hVioHandle, vioClass, ownerType);
}

NVAPI_INTERFACE VIO_Close(NvVioHandle hVioHandle, NvU32 bRelease) {
    return NvAPI_VIO_Close(hVioHandle, bRelease);
}

NVAPI_INTERFACE VIO_Status(NvVioHandle hVioHandle, NVVIOSTATUS *pStatus) {
    return NvAPI_VIO_Status(hVioHandle, pStatus);
}

NVAPI_INTERFACE VIO_SyncFormatDetect(NvVioHandle hVioHandle, NvU32 *pWait) {
    return NvAPI_VIO_SyncFormatDetect(hVioHandle, pWait);
}

NVAPI_INTERFACE VIO_GetConfig(NvVioHandle hVioHandle, NVVIOCONFIG *pConfig) {
    return NvAPI_VIO_GetConfig(hVioHandle, pConfig);
}

NVAPI_INTERFACE VIO_SetConfig(NvVioHandle hVioHandle, const NVVIOCONFIG *pConfig) {
    return NvAPI_VIO_SetConfig(hVioHandle, pConfig);
}

NVAPI_INTERFACE VIO_SetCSC(NvVioHandle hVioHandle, NVVIOCOLORCONVERSION *pCSC) {
    return NvAPI_VIO_SetCSC(hVioHandle, pCSC);
}

NVAPI_INTERFACE VIO_GetCSC(NvVioHandle hVioHandle, NVVIOCOLORCONVERSION *pCSC) {
    return NvAPI_VIO_GetCSC(hVioHandle, pCSC);
}

NVAPI_INTERFACE VIO_SetGamma(NvVioHandle hVioHandle, NVVIOGAMMACORRECTION *pGamma) {
    return NvAPI_VIO_SetGamma(hVioHandle, pGamma);
}

NVAPI_INTERFACE VIO_GetGamma(NvVioHandle hVioHandle, NVVIOGAMMACORRECTION* pGamma) {
    return NvAPI_VIO_GetGamma(hVioHandle, pGamma);
}

NVAPI_INTERFACE VIO_SetSyncDelay(NvVioHandle hVioHandle, const NVVIOSYNCDELAY *pSyncDelay) {
    return NvAPI_VIO_SetSyncDelay(hVioHandle, pSyncDelay);
}

NVAPI_INTERFACE VIO_GetSyncDelay(NvVioHandle hVioHandle, NVVIOSYNCDELAY *pSyncDelay) {
    return NvAPI_VIO_GetSyncDelay(hVioHandle, pSyncDelay);
}

NVAPI_INTERFACE VIO_GetPCIInfo(NvVioHandle hVioHandle,  NVVIOPCIINFO* pVioPCIInfo) {
    return NvAPI_VIO_GetPCIInfo(hVioHandle, pVioPCIInfo);
}

NVAPI_INTERFACE VIO_IsRunning(NvVioHandle hVioHandle) {
    return NvAPI_VIO_IsRunning(hVioHandle);
}

NVAPI_INTERFACE VIO_Start(NvVioHandle hVioHandle) {
    return NvAPI_VIO_Start(hVioHandle);
}

NVAPI_INTERFACE VIO_Stop(NvVioHandle hVioHandle) {
    return NvAPI_VIO_Stop(hVioHandle);
}

NVAPI_INTERFACE VIO_IsFrameLockModeCompatible(NvVioHandle hVioHandle, NvU32 srcEnumIndex, NvU32 destEnumIndex, NvU32* pbCompatible) {
    return NvAPI_VIO_IsFrameLockModeCompatible(hVioHandle, srcEnumIndex, destEnumIndex, pbCompatible);
}

NVAPI_INTERFACE VIO_EnumDevices(NvVioHandle hVioHandle[NVAPI_MAX_VIO_DEVICES], NvU32 *vioDeviceCount) {
    return NvAPI_VIO_EnumDevices(hVioHandle, vioDeviceCount);
}

NVAPI_INTERFACE VIO_QueryTopology(NV_VIO_TOPOLOGY *pNvVIOTopology) {
    return NvAPI_VIO_QueryTopology(pNvVIOTopology);
}

NVAPI_INTERFACE VIO_EnumSignalFormats(NvVioHandle hVioHandle, NvU32 enumIndex, NVVIOSIGNALFORMATDETAIL *pSignalFormatDetail) {
    return NvAPI_VIO_EnumSignalFormats(hVioHandle, enumIndex, pSignalFormatDetail);
}

NVAPI_INTERFACE VIO_EnumDataFormats(NvVioHandle hVioHandle, NvU32 enumIndex, NVVIODATAFORMATDETAIL *pDataFormatDetail) {
    return NvAPI_VIO_EnumDataFormats(hVioHandle, enumIndex, pDataFormatDetail);
}

NVAPI_INTERFACE Stereo_CreateConfigurationProfileRegistryKey(NV_STEREO_REGISTRY_PROFILE_TYPE registryProfileType) {
    return NvAPI_Stereo_CreateConfigurationProfileRegistryKey(registryProfileType);
}

NVAPI_INTERFACE Stereo_DeleteConfigurationProfileRegistryKey(NV_STEREO_REGISTRY_PROFILE_TYPE registryProfileType) {
    return NvAPI_Stereo_DeleteConfigurationProfileRegistryKey(registryProfileType);
}

NVAPI_INTERFACE Stereo_SetConfigurationProfileValue(NV_STEREO_REGISTRY_PROFILE_TYPE registryProfileType, NV_STEREO_REGISTRY_ID valueRegistryID, void *pValue) {
    return NvAPI_Stereo_SetConfigurationProfileValue(registryProfileType, valueRegistryID, pValue);
}

NVAPI_INTERFACE Stereo_DeleteConfigurationProfileValue(NV_STEREO_REGISTRY_PROFILE_TYPE registryProfileType, NV_STEREO_REGISTRY_ID valueRegistryID) {
    return NvAPI_Stereo_DeleteConfigurationProfileValue(registryProfileType, valueRegistryID);
}

NVAPI_INTERFACE Stereo_GetStereoSupport(NvMonitorHandle hMonitor, NVAPI_STEREO_CAPS *pCaps) {
    return NvAPI_Stereo_GetStereoSupport(hMonitor, pCaps);
}

NVAPI_INTERFACE Stereo_DecreaseSeparation(StereoHandle stereoHandle) {
    return NvAPI_Stereo_DecreaseSeparation(stereoHandle);
}

NVAPI_INTERFACE Stereo_IncreaseSeparation(StereoHandle stereoHandle) {
    return NvAPI_Stereo_IncreaseSeparation(stereoHandle);
}

NVAPI_INTERFACE Stereo_DecreaseConvergence(StereoHandle stereoHandle) {
    return NvAPI_Stereo_DecreaseConvergence(stereoHandle);
}

NVAPI_INTERFACE Stereo_IncreaseConvergence(StereoHandle stereoHandle) {
    return NvAPI_Stereo_IncreaseConvergence(stereoHandle);
}

NVAPI_INTERFACE Stereo_GetFrustumAdjustMode(StereoHandle stereoHandle, NV_FRUSTUM_ADJUST_MODE *pFrustumAdjustMode) {
    return NvAPI_Stereo_GetFrustumAdjustMode(stereoHandle, pFrustumAdjustMode);
}

NVAPI_INTERFACE Stereo_SetFrustumAdjustMode(StereoHandle stereoHandle, NV_FRUSTUM_ADJUST_MODE newFrustumAdjustModeValue) {
    return NvAPI_Stereo_SetFrustumAdjustMode(stereoHandle, newFrustumAdjustModeValue);
}

NVAPI_INTERFACE Stereo_CaptureJpegImage(StereoHandle stereoHandle, NvU32 quality) {
    return NvAPI_Stereo_CaptureJpegImage(stereoHandle, quality);
}

NVAPI_INTERFACE Stereo_InitActivation(StereoHandle hStereoHandle, NVAPI_STEREO_INIT_ACTIVATION_FLAGS flags) {
    return NvAPI_Stereo_InitActivation(hStereoHandle, flags);
}

NVAPI_INTERFACE Stereo_Trigger_Activation(StereoHandle hStereoHandle) {
    return NvAPI_Stereo_Trigger_Activation(hStereoHandle);
}

NVAPI_INTERFACE Stereo_CapturePngImage(StereoHandle stereoHandle) {
    return NvAPI_Stereo_CapturePngImage(stereoHandle);
}

NVAPI_INTERFACE Stereo_ReverseStereoBlitControl(StereoHandle hStereoHandle, NvU8 TurnOn) {
    return NvAPI_Stereo_ReverseStereoBlitControl(hStereoHandle, TurnOn);
}

NVAPI_INTERFACE Stereo_SetNotificationMessage(StereoHandle hStereoHandle, NvU64 hWnd,NvU64 messageID) {
    return NvAPI_Stereo_SetNotificationMessage(hStereoHandle, hWnd, messageID);
}

NVAPI_INTERFACE D3D1x_CreateSwapChain(StereoHandle hStereoHandle, DXGI_SWAP_CHAIN_DESC* pDesc, IDXGISwapChain** ppSwapChain, NV_STEREO_SWAPCHAIN_MODE mode) {
    return NvAPI_D3D1x_CreateSwapChain(hStereoHandle, pDesc, ppSwapChain, mode);
}

NVAPI_INTERFACE D3D9_CreateSwapChain(StereoHandle hStereoHandle, D3DPRESENT_PARAMETERS *pPresentationParameters, IDirect3DSwapChain9 **ppSwapChain, NV_STEREO_SWAPCHAIN_MODE mode) {
    return NvAPI_D3D9_CreateSwapChain(hStereoHandle, pPresentationParameters, ppSwapChain, mode);
}

NVAPI_INTERFACE DRS_CreateSession(NvDRSSessionHandle *phSession) {
    return NvAPI_DRS_CreateSession(phSession);
}

NVAPI_INTERFACE DRS_DestroySession(NvDRSSessionHandle hSession) {
    return NvAPI_DRS_DestroySession(hSession);
}

NVAPI_INTERFACE DRS_LoadSettings(NvDRSSessionHandle hSession) {
    return NvAPI_DRS_LoadSettings(hSession);
}

NVAPI_INTERFACE DRS_SaveSettings(NvDRSSessionHandle hSession) {
    return NvAPI_DRS_SaveSettings(hSession);
}

NVAPI_INTERFACE DRS_LoadSettingsFromFile(NvDRSSessionHandle hSession, NvAPI_UnicodeString fileName) {
    return NvAPI_DRS_LoadSettingsFromFile(hSession, fileName);
}

NVAPI_INTERFACE DRS_SaveSettingsToFile(NvDRSSessionHandle hSession, NvAPI_UnicodeString fileName) {
    return NvAPI_DRS_SaveSettingsToFile(hSession, fileName);
}

NVAPI_INTERFACE DRS_CreateProfile(NvDRSSessionHandle hSession, NVDRS_PROFILE *pProfileInfo, NvDRSProfileHandle *phProfile) {
    return NvAPI_DRS_CreateProfile(hSession, pProfileInfo, phProfile);
}

NVAPI_INTERFACE DRS_DeleteProfile(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile) {
    return NvAPI_DRS_DeleteProfile(hSession, hProfile);
}

NVAPI_INTERFACE DRS_SetCurrentGlobalProfile(NvDRSSessionHandle hSession, NvAPI_UnicodeString wszGlobalProfileName) {
    return NvAPI_DRS_SetCurrentGlobalProfile(hSession, wszGlobalProfileName);
}

NVAPI_INTERFACE DRS_GetCurrentGlobalProfile(NvDRSSessionHandle hSession, NvDRSProfileHandle *phProfile) {
    return NvAPI_DRS_GetCurrentGlobalProfile(hSession, phProfile);
}

NVAPI_INTERFACE DRS_GetProfileInfo(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NVDRS_PROFILE *pProfileInfo) {
    return NvAPI_DRS_GetProfileInfo(hSession, hProfile, pProfileInfo);
}

NVAPI_INTERFACE DRS_SetProfileInfo(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NVDRS_PROFILE *pProfileInfo) {
    return NvAPI_DRS_SetProfileInfo(hSession, hProfile, pProfileInfo);
}

NVAPI_INTERFACE DRS_FindProfileByName(NvDRSSessionHandle hSession, NvAPI_UnicodeString profileName, NvDRSProfileHandle* phProfile) {
    return NvAPI_DRS_FindProfileByName(hSession, profileName, phProfile);
}

NVAPI_INTERFACE DRS_EnumProfiles(NvDRSSessionHandle hSession, NvU32 index, NvDRSProfileHandle *phProfile) {
    return NvAPI_DRS_EnumProfiles(hSession, index, phProfile);
}

NVAPI_INTERFACE DRS_GetNumProfiles(NvDRSSessionHandle hSession, NvU32 *numProfiles) {
    return NvAPI_DRS_GetNumProfiles(hSession, numProfiles);
}

NVAPI_INTERFACE DRS_CreateApplication(NvDRSSessionHandle hSession, NvDRSProfileHandle  hProfile, NVDRS_APPLICATION *pApplication) {
    return NvAPI_DRS_CreateApplication(hSession,  hProfile, pApplication);
}

NVAPI_INTERFACE DRS_DeleteApplicationEx(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NVDRS_APPLICATION *pApp) {
    return NvAPI_DRS_DeleteApplicationEx(hSession, hProfile, pApp);
}

NVAPI_INTERFACE DRS_DeleteApplication(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NvAPI_UnicodeString appName) {
    return NvAPI_DRS_DeleteApplication(hSession, hProfile, appName);
}

NVAPI_INTERFACE DRS_GetApplicationInfo(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NvAPI_UnicodeString appName, NVDRS_APPLICATION *pApplication) {
    return NvAPI_DRS_GetApplicationInfo(hSession, hProfile, appName, pApplication);
}

NVAPI_INTERFACE DRS_EnumApplications(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NvU32 startIndex, NvU32 *appCount, NVDRS_APPLICATION *pApplication) {
    return NvAPI_DRS_EnumApplications(hSession, hProfile, startIndex, appCount, pApplication);
}

NVAPI_INTERFACE DRS_FindApplicationByName(NvDRSSessionHandle hSession, NvAPI_UnicodeString appName, NvDRSProfileHandle *phProfile, NVDRS_APPLICATION *pApplication) {
    return NvAPI_DRS_FindApplicationByName(hSession, appName, phProfile, pApplication);
}

NVAPI_INTERFACE DRS_SetSetting(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NVDRS_SETTING *pSetting) {
    return NvAPI_DRS_SetSetting(hSession, hProfile, pSetting);
}

NVAPI_INTERFACE DRS_GetSetting(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NvU32 settingId, NVDRS_SETTING *pSetting) {
    return NvAPI_DRS_GetSetting(hSession, hProfile, settingId, pSetting);
}

NVAPI_INTERFACE DRS_EnumSettings(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NvU32 startIndex, NvU32 *settingsCount, NVDRS_SETTING *pSetting) {
    return NvAPI_DRS_EnumSettings(hSession, hProfile, startIndex, settingsCount, pSetting);
}

NVAPI_INTERFACE DRS_EnumAvailableSettingIds(NvU32 *pSettingIds, NvU32 *pMaxCount) {
    return NvAPI_DRS_EnumAvailableSettingIds(pSettingIds, pMaxCount);
}

NVAPI_INTERFACE DRS_EnumAvailableSettingValues(NvU32 settingId, NvU32 *pMaxNumValues, NVDRS_SETTING_VALUES *pSettingValues) {
    return NvAPI_DRS_EnumAvailableSettingValues(settingId, pMaxNumValues, pSettingValues);
}

NVAPI_INTERFACE DRS_GetSettingIdFromName(NvAPI_UnicodeString settingName, NvU32 *pSettingId) {
    return NvAPI_DRS_GetSettingIdFromName(settingName, pSettingId);
}

NVAPI_INTERFACE DRS_GetSettingNameFromId(NvU32 settingId, NvAPI_UnicodeString *pSettingName) {
    return NvAPI_DRS_GetSettingNameFromId(settingId, pSettingName);
}

NVAPI_INTERFACE DRS_DeleteProfileSetting(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NvU32 settingId) {
    return NvAPI_DRS_DeleteProfileSetting(hSession, hProfile, settingId);
}

NVAPI_INTERFACE DRS_RestoreAllDefaults(NvDRSSessionHandle hSession) {
    return NvAPI_DRS_RestoreAllDefaults(hSession);
}

NVAPI_INTERFACE DRS_RestoreProfileDefault(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile) {
    return NvAPI_DRS_RestoreProfileDefault(hSession, hProfile);
}

NVAPI_INTERFACE DRS_RestoreProfileDefaultSetting(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NvU32 settingId) {
    return NvAPI_DRS_RestoreProfileDefaultSetting(hSession, hProfile, settingId);
}

NVAPI_INTERFACE DRS_GetBaseProfile(NvDRSSessionHandle hSession, NvDRSProfileHandle *phProfile) {
    return NvAPI_DRS_GetBaseProfile(hSession, phProfile);
}

NVAPI_INTERFACE SYS_GetChipSetInfo(NV_CHIPSET_INFO *pChipSetInfo) {
    return NvAPI_SYS_GetChipSetInfo(pChipSetInfo);
}

NVAPI_INTERFACE SYS_GetLidAndDockInfo(NV_LID_DOCK_PARAMS *pLidAndDock) {
    return NvAPI_SYS_GetLidAndDockInfo(pLidAndDock);
}

NVAPI_INTERFACE SYS_GetDisplayIdFromGpuAndOutputId(NvPhysicalGpuHandle hPhysicalGpu, NvU32 outputId, NvU32* displayId) {
    return NvAPI_SYS_GetDisplayIdFromGpuAndOutputId(hPhysicalGpu, outputId, displayId);
}

NVAPI_INTERFACE SYS_GetGpuAndOutputIdFromDisplayId(NvU32 displayId, NvPhysicalGpuHandle *hPhysicalGpu, NvU32 *outputId) {
    return NvAPI_SYS_GetGpuAndOutputIdFromDisplayId(displayId, hPhysicalGpu, outputId);
}

NVAPI_INTERFACE SYS_GetPhysicalGpuFromDisplayId(NvU32 displayId, NvPhysicalGpuHandle *hPhysicalGpu) {
    return NvAPI_SYS_GetPhysicalGpuFromDisplayId(displayId, hPhysicalGpu);
}
