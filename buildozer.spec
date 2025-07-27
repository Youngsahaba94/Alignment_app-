[app] title = Alignment Report package.name = alignmentapp package.domain = org.masud source.include_exts = py,xlsx version = 1.0 requirements = python3,kivy,pandas,openpyxl orientation = portrait fullscreen = 0 android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE android.minapi = 23

[buildozer] log_level = 2 warn_on_root = 1

[hostpython]

[python]

[android] android.arch = arm64-v8a

[app.android] android.manifest_placeholders = appAuthRedirectScheme=org.masud.alignmentapp

