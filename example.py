import nvapi
import traceback


logical_gpus = nvapi.GPUs()
for attr_name in (
    'driver_info',
    'chipset_info',
    'display_config',
    'interface_version',
    'lid_and_dock_info',
    'nv_managed_dedicated_displays',
    'preferred_stereo_display',
    'system_logical_gpus',
    'system_physical_gpus',
):
    try:
        attr = getattr(logical_gpus, attr_name)
    except:
        continue

    print(attr_name + ':', attr)
print()

for logical_gpu in logical_gpus:
    print('Logical GPU:')
    for attr_name in ('os_adpater_id',):
        try:
            attr = getattr(logical_gpu, attr_name)
        except:
            continue

        print('', attr_name + ':', attr)

    print()
    
    for gpu in logical_gpu.physical_gpus:
        print('  GPU: ')

        for attr_name in (
            'hdcp_fuse_state',
            'hdcp_key_source',
            'hdcp_key_source_state',
            'shader_sub_pipe_count',
            'core_count',
            'all_outputs',
            'connected_outputs',
            'connected_sli_outputs',
            'connected_outputs_with_lid_state',
            'connected_sli_outputs_with_lid_state',
            'system_type',
            'active_outputs',
            'pci_device_id',
            'pci_subsystem_id',
            'pci_revision_id',
            'pci_ext_device_id',
            'gpu_type',
            'bus_type',
            'bus_id',
            'bus_slot_id',
            'irq',
            'vbios_revision',
            'oem_vbios_revision',
            'vbios_version',
            'agp_aperture',
            'current_agp_rate',
            'current_pcie_downstream_width',
            'physical_frame_buffer_size',
            'virtual_frame_buffer_size',
            'quadro_status',
            'serial_number',
            'tach_reading',
            'performance_monitor',
            'thermal_sensors',
            'clock_frequencies',
            'dedicated_memory',
            'available_dedicated_memory',
            'system_memory',
            'shared_system_memory',
            'current_available_dedicated_memory',
            'dedicated_memory_eviction_size',
            'dedicated_memory_eviction_count',
            'physical_gpu_id',
            'ram_bus_width',
            'architecture_info',
            'uuid',
            'virtualization_mode',
            'licensable_features',
            'gpu_info',
            'is_vr_ready',
            'gsp_firmware_version',
            'is_overclocking_detected',
            'memory_info_ex',
            'adapter_luid',
            'nvlink_caps',
            'nvlink_status',
            'encoder_statistics',
            'encoder_sessions',
            'is_cuda_compute_capable',
            'full_name',
            'perf_decrease_info',
            'current_pstate',
            'ecc_status_info',
            'ecc_error_info',
            'ecc_configuration_info',
            'workstation_feature_query',
            'client_illum_devices_info',
            'client_illum_devices_control',
            'client_illum_zones_info',
        ):
            try:
                attr = getattr(gpu, attr_name)
            except:
                continue

            print('   ', attr_name + ':', attr)
        print()
    
    for display in logical_gpu:
        print('    Display:')
        for attr_name in (
            'color_data',
            'monitor_capabilities_vsdb',
            'monitor_capabilities_vcdb',
            'monitor_color_capabilities',
            'display_port_info',
            'hdmi_support_info',
            'is_primary',
            'hdr',
            'connector_type',
            'is_dynamic',
            'is_multi_stream_root_node',
            'is_active',
            'is_cluster',
            'is_visible',
            'is_wireless_display',
            'is_connected',
            'is_physically_connected',
            'is_hdr_supported',
            'is_st2048etof_supported',
            'is_traditional_gamma_supported',
            'is_edr_supported',
            'is_traditional_sdr_gamma_supported',
            'is_dolby_vision_supported',
            'hdr_dynamic_range',
            'hdr_dynamic_range',
            'hdr_color_format',
            'hdr_primary_color_coordinates',
            'hdr_maximum_content_light_level',
            'hdr_maximum_luminance',
            'hdr_minimum_luminance',
            'hdr_maximum_frame_average_luminance',
            'hdr_supports_2160p60hz',
            'hdr_supports_yuv422_12bit',
            'hdr_supports_global_dimming',
            'hdr_colorimetry',
            'hdr_supports_backlight_control',
            'hdr_backlight_minimum',
            'hdr_interface_supported_by_sink',
            'hdr_supports_10b_12b_444',
            'hdr_minimum_sink_luminance',
            'hdr_maximum_sink_luminance',
            'hdr_primary_chromaticity_coordinates',
            'source_color_space',
            'source_hdr_metadata',
            'output_mode',
            'hdr_tone_mapping',
            'colorimetry',
            'edid_data',
            'adaptive_sync_data',
            'virtual_refresh_rate_data',
            'dedicated_display_metadata',
            'display_id_info',
            'grid_display_ids',
            'vrr_info',
            'edid_info',
            'scanout_configuration',
            'scanout_configuration_ex',
            'scanout_intensity_enabled',
            'scanout_warping_enabled',
        ):
            try:
                attr = getattr(display, attr_name)
            except:
                continue

            print('     ', attr_name + ':', attr)
        print()
