define phoneModels = {
    # Basic smartphone
    'smartphone' :
        {
            'name':         "smartphone",       # Human readable name
            'prefix':       'smartphone-',      # Prefix for images, audio, and styles
            'dims':         (356, 750),         # Dimensions of phone image
            'padding':      (14, 14, 14, 14),   # Opaque part: left, top, right, bottom
            'ysize':        0.68,               # Default vertical size on screen
            'bootApp':      'AppBoot',          # Boot application class name, or None
            'homeApp':      'AppHome',          # Home application class name
        },
}