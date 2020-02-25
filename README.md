# nvapi
Nvidia (NVAPI) SDK Port to Python

In Development
update:
Module imports without error, I am not able to test because I do not own an Nvidia video card

I had to compile a dynamic library that linked to the static library provided with NVAPI

ok so here is a basic code example of what I have going on so far. It is mostly get properties 
for collecting some information. There is a single method that allows you to turn on and off HDR.
I will be expanding the capabilities over the next few weeks. The API does not provide a whole lot
of code examples. So there is going to be quite a bit of trial and error.

    import nvapi
    import traceback
    
    for gpu in nvapi.GPUs():
        for display in gpu:
            for attr_name in (
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
                'primary_color_coordinates',
                'maximum_hdr_luminance',
                'minimum_hdr_luminance',
                'maximum_frame_average_hdr_luminance',
                'supports_2160p60hz',
                'supports_yuv422_12bit',
                'supports_global_dimming',
                'colorimetry',
                'supports_backlight_control',
                'backlight_minimum',
                'interface_supported_by_sink',
                'supports_10b_12b_444',
                'minimum_sink_luminance',
                'maximum_sink_luminance',
                'primary_chromaticity_coordinates'
            ):
                try:
                    attr = getattr(display, attr_name)
                except:
                    traceback.print_exc()
                    continue
                
                print(attr_name + ':', attr)
                
            # to enable HDR (if supported) uncomment line below
            # display.enable_hdr(True)
            
            # to disable HDR (if supported) uncomment line below
            # display.enable_hdr(False)