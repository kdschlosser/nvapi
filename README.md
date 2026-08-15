# nvapi

Nvidia (NVAPI) SDK Port to Python — management, monitoring, and display/GPU
information, not the 3D rendering pipeline.

Dispatch is done the way NVAPI actually works: `nvapi64.dll`/`nvapi.dll`
export almost nothing by name (`nvapi_QueryInterface` is the real entry
point); every `NvAPI_X` call in this package resolves its address at
runtime via that dispatch function using the numeric interface IDs NVIDIA
publishes in `nvapi_interface.h`. Live-tested against real hardware (a
2018 Quadro RTX 4000, TU104 die).

## Quick example

```python
import nvapi

for logical_gpu in nvapi.GPUs():
    for physical_gpu in logical_gpu.physical_gpus:
        print(physical_gpu.full_name, physical_gpu.short_name)

    # iterating a LogicalGPU yields Port (a physical connector), not
    # Display directly -- iterate a Port to get the display(s) actually
    # attached to it (zero, one, or more with a splitter/MST hub)
    for port in logical_gpu:
        print(port.connector_type, port.is_connected)
        for display in port:
            print(' ', display.edid_info.monitor_name if display.edid_info else display.display_id)

            # to enable HDR (if supported):
            # display.enable_hdr(True)
```

See [`example.py`](example.py) for a full sweep of every property exposed
by every class.

## Scope

In scope: GPU/display identification and capabilities, memory, clocks,
thermal/power, PCI/bus info, ECC, ports/connectors and EDID, HDR/color
management, adaptive sync/VRR, custom display modes, scanout composition
(projector edge-blending/warping), RGB illumination, I2C, and driver/system
info.

Explicitly out of scope: the 3D rendering pipeline (D3D11/D3D12/Vulkan/
CUDA/raytracing/NGX/Present Barrier/Reflex) and Stereo 3D. Nothing in this
package touches those.

## Object model

- `nvapi.GPUs()` — singleton; iterate it for `LogicalGPU`s.
- `LogicalGPU` — has `.physical_gpus` (one or more `PhysicalGPU`, e.g. SLI);
  iterate it for `Port`s.
- `Port` — a physical connector on a `PhysicalGPU` (e.g. one DisplayPort
  jack). Iterate it for the `Display`(s) actually attached — zero if
  nothing's plugged in, more than one behind a splitter/MST hub.
- `PhysicalGPU` — a single GPU die/board.
- `Display` — a single monitor/panel, keyed by its persistent `displayId`.

## What's exposed

### `GPUs` (system-wide)

`driver_info`, `chipset_info`, `display_config`/setter, `interface_version`,
`lid_and_dock_info`, `nv_managed_dedicated_displays`, `preferred_stereo_display`/
setter, `system_logical_gpus`, `system_physical_gpus`,
`try_custom_display()`, `delete_custom_display()`, `save_custom_display()`,
`revert_custom_display_trial()`.

### `LogicalGPU`

`os_adpater_id`, `physical_gpus`.

### `Port`

`connector_type`, `output_type`, `is_connected`, `is_active`,
`display_port_info`/setter, `hdmi_support_info`.

### `PhysicalGPU`

**Identification:** `full_name`, `short_name`, `physical_gpu_id`, `uuid`,
`architecture_info`, `gpu_info`, `gpu_type`, `system_type`, `quadro_status`,
`is_vr_ready`, `gsp_firmware_version`, `virtualization_mode`,
`licensable_features`, `adapter_luid`.

**PCI/bus:** `pci_device_id`, `pci_subsystem_id`, `pci_revision_id`,
`pci_ext_device_id`, `bus_type`, `bus_id`, `bus_slot_id`, `irq`,
`agp_aperture`, `current_agp_rate`, `current_pcie_downstream_width`.

**VBIOS:** `vbios_revision`, `oem_vbios_revision`, `vbios_version`.

**Memory:** `dedicated_memory`, `available_dedicated_memory`,
`system_memory`, `shared_system_memory`,
`current_available_dedicated_memory`, `dedicated_memory_eviction_size`,
`dedicated_memory_eviction_count`, `memory_info_ex`, `ram_bus_width`,
`ram_type`, `ram_maker`, `ram_bank_count`, `foundry`,
`framebuffer_width_and_location`, `physical_frame_buffer_size`,
`virtual_frame_buffer_size`.

**Clocks/perf/power:** `clock_frequencies`, `current_pstate`,
`perf_decrease_info`, `performance_monitor`, `thermal_sensors`,
`tach_reading`, `is_overclocking_detected`, `core_count`,
`shader_sub_pipe_count`, `shader_pipe_count`, `partition_count`,
`driver_model`.

**Outputs/connectors (legacy bitmask):** `all_outputs`,
`connected_outputs`, `connected_sli_outputs`,
`connected_outputs_with_lid_state`, `connected_sli_outputs_with_lid_state`,
`active_outputs`, `output_type(output_id)`,
`validate_output_combination(mask)`, `connector_info(output_id)`.

**EDID (legacy, per-output):** `get_edid(output_id)`,
`set_edid(output_id, data)`.

**HDCP:** `hdcp_fuse_state`, `hdcp_key_source`, `hdcp_key_source_state`.

**NVLink:** `nvlink_caps`, `nvlink_status`.

**Encoder:** `encoder_statistics`, `encoder_sessions`.

**CUDA:** `is_cuda_compute_capable`.

**ECC:** `ecc_status_info`, `ecc_error_info`, `ecc_configuration_info`/
setter, `reset_ecc_error_info()`.

**Workstation features:** `workstation_feature_query`,
`workstation_feature_setup()`, `query_workstation_feature_support()`.

**RGB illumination:** `client_illum_devices_info`,
`client_illum_devices_control`/setter, `client_illum_zones_info`,
`client_illum_zones_control()`, `set_client_illum_zones_control()`,
`get_illumination()`, `set_illumination()`, `query_illumination_support()`.

**I2C:** `i2c_read()`, `i2c_write()`.

### `Display`

**Identity/state:** `is_primary`, `is_active`, `is_connected`,
`is_physically_connected`, `is_visible`, `is_cluster`, `is_dynamic`,
`is_multi_stream_root_node`, `is_wireless_display`, `connector_type`,
`display_id_info`, `grid_display_ids`.

**EDID:** `edid_data` (raw bytes), `edid_info` (decoded — see
[`nvapi/edid.py`](nvapi/edid.py); manufacturer, model, serial, timings,
etc.).

**HDR:** `hdr`/setter, `is_hdr_supported`, `hdr_dynamic_range`,
`hdr_color_format`, `hdr_primary_color_coordinates`,
`hdr_maximum_content_light_level`, `hdr_maximum_luminance`,
`hdr_minimum_luminance`, `hdr_maximum_frame_average_luminance`,
`hdr_supports_2160p60hz`, `hdr_supports_yuv422_12bit`,
`hdr_supports_global_dimming`, `hdr_colorimetry`,
`hdr_supports_backlight_control`, `hdr_backlight_minimum`,
`hdr_interface_supported_by_sink`, `hdr_supports_10b_12b_444`,
`hdr_minimum_sink_luminance`, `hdr_maximum_sink_luminance`,
`hdr_primary_chromaticity_coordinates`, `hdr_tone_mapping`/setter,
`is_st2048etof_supported`, `is_traditional_gamma_supported`,
`is_edr_supported`, `is_traditional_sdr_gamma_supported`,
`is_dolby_vision_supported`, `source_hdr_metadata`/setter.

**Color management:** `color_data`/setter, `colorimetry`,
`source_color_space`/setter, `output_mode`/setter,
`monitor_capabilities_vsdb`, `monitor_capabilities_vcdb`,
`monitor_color_capabilities`, `infoframe_control()`.

**Timing/config:** `get_timing()`, `scanout_configuration`,
`scanout_configuration_ex`, `get_scanout_composition_parameter()`,
`set_scanout_composition_parameter()`, `enum_custom_displays()`.

**Scanout intensity/warping** (projector edge-blending/geometric warping):
`scanout_intensity_enabled`, `set_scanout_intensity()`,
`scanout_warping_enabled`, `set_scanout_warping()`.

**Adaptive sync/VRR:** `adaptive_sync_data`/setter,
`virtual_refresh_rate_data`/setter, `vrr_info`.

**Dedicated display management:** `dedicated_display_metadata`/setter,
`acquire_dedicated_display()`, `release_dedicated_display()`.

**Legacy handle-based:** `enum_display_handles()`,
`enum_unattached_display_handles()`,
`create_display_from_unattached_display()`,
`get_associated_display_handle()`, `get_associated_unattached_display_handle()`,
`get_associated_display_name()`, `get_unattached_display_name()`,
`get_associated_display_output_id()`, `enable_hw_cursor()`,
`disable_hw_cursor()`, `get_vblank_counter()`, `set_refresh_rate_override()`.

## Reverse-engineered / undocumented functions

Every function above is declared in NVIDIA's own published `nvapi.h`
(current or archived), even where the struct/signature had to be
transcribed from a newer SDK snapshot than this port originally generated
against. The functions below are different: **NVIDIA has never published
their struct or signature at all**, in any SDK version, current or
archived. They were wired up anyway because their numeric interface IDs
and (for most of them) their real signatures are known from other sources,
and every one was verified against live hardware before being trusted.

### `NvAPI_GPU_GetConnectorInfo`

Backs `Port.connector_type` / `PhysicalGPU.connector_info(output_id)`.

NVIDIA's own header comments point to
`NvAPI_GPU_GetConnectorInfo`/`GetConnectorInfoEx` as the authoritative
source for real connector type, but neither function is declared anywhere
public, and no community NVAPI port (checked: `arcnmx/nvapi-rs`,
`falahati/NvAPIWrapper`, a Pascal/FPC port, several interface-ID lists)
publishes its struct — only the numeric interface ID (`0x4ECA2C10`) is
known, from those same community ID lists.

The struct (`NV_GPU_CONNECTOR_INFO` in `nvapi/nvapi_gpu_info_ext_h.py`) was
reverse-engineered by black-box probing a live GPU, with the user's
explicit informed consent given the risk of calling an internal driver
code path: swept candidate `version` header values (every 4-byte size from
4-256, revisions 1-6) until the driver returned `NVAPI_OK` instead of the
safe `NVAPI_INCOMPATIBLE_STRUCT_VERSION` rejection every wrong guess
produced (no crash observed on any wrong guess), then decoded the returned
bytes. Resolved: `version = size(44) | revision(1)<<16`.

Verified multiple independent ways:
- Correctly decoded 3x DisplayPort External + 1x USB Type-C on the test
  GPU — a real Quadro RTX 4000 does have a USB-C/VirtualLink port, which
  no other function in this binding can detect.
- `connectorIndex` correctly groups multiple legacy output-mask bits onto
  one physical connector: the test GPU's `all_outputs` bitmask has 7 set
  bits but only 4 distinct `connectorIndex` values, matching its actual 4
  physical connectors.
- Cross-confirmed via static analysis of the real system driver
  (`C:\Windows\System32\nvapi64.dll`, the DLL actually loaded and called
  at runtime): its string table contains the MSVC-mangled RTTI name
  `.?AU_NV_ESC_NVAPI_GET_GPU_CONNECTOR_INFO@@`, sitting directly beside
  `.?AU_NV_ESC_NVAPI_GET_GPU_OUTPUT_TYPE@@` — the escape struct for
  `NvAPI_GPU_GetOutputType`, a function already fully understood — same
  struct family, same call shape.

`Port.__iter__` (marrying displays to a physical port) is a second,
related, undocumented-territory piece: since there's no published API for
"which display is on which connector" either, it correlates displays by
reading each port's EDID (`NvAPI_GPU_GetEDID`, itself a documented legacy
function) and matching it byte-for-byte against each display's modern EDID
(`Display.edid_data`). Verified live: all 3 of the test system's monitors
correctly and uniquely matched to their own connector, cross-checked
against each monitor's distinct serial number. Unverified against true
MST/splitter hardware — see the docstring on `Port.__iter__`.

### Undocumented single-out-param GPU info functions

`PhysicalGPU.ram_type`, `ram_maker`, `ram_bank_count`, `foundry`,
`shader_pipe_count`, `partition_count`, `driver_model`, `short_name`,
`framebuffer_width_and_location`.

None of these are declared in any published NVAPI header (current or
archived) or listed in NVIDIA's own published `nvapi_interface.h`. Unlike
`GetConnectorInfo`, both the function signatures and interface IDs for
these came from a real, mature open-source reverse-engineering project
(`arcnmx/nvapi-rs`'s `sys/src/gpu/mod.rs` `private` module for signatures/
enum tables, `sys/src/nvid.rs` for the numeric IDs) — no black-box probing
was needed, and none of these take a struct/version field, only a bare
scalar/enum/string out-param, so there's nothing to get wrong the way
`GetConnectorInfo`'s struct size could be wrong.

Verified live against the test GPU:
- `short_name` correctly returns `"TU104GL-A"` — TU104 is the real,
  publicly documented die used in the Quadro RTX 4000.
- `ram_maker` correctly decodes to Samsung.
- `ram_type` returned `14`, outside the source project's enum table (which
  tops out at 10/GDDR5X and predates GDDR6 driver support). Added as
  `NV_GPU_RAM_GDDR6 = 14` since it's independently verifiable — TU104
  cards are publicly documented to use GDDR6, and GDDR6X didn't exist
  until Ampere — not a guess; values 11-13 remain unlabeled since nothing
  pins down what they are.
- `shader_pipe_count` (5) returns a different value than the
  already-verified, documented `shader_sub_pipe_count` (18) on the same
  GPU, confirming these are two distinct real metrics, not the same call
  under two names.
- `foundry` returned `NVAPI_NOT_SUPPORTED` on the test GPU — a legitimate
  per-GPU "not supported" result (the call itself dispatches and returns a
  clean status), not a decode failure.
