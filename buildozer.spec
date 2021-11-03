[app]

# (str) Title of your application
title = BLOCKnote

# (str) Package name
package.name = blocknote

# (str) Package domain (needed for android/ios packaging)
package.domain = dev.dEN5

# (str) Source code where the main.py live
source.dir = src/

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,ttf,kv,json,txt

# (list) List of inclusions using pattern matching
# source.include_patterns = assets/*
version = 0.1
# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]

# version.filename = blocknote 0.1

android.numeric_version = 1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy

requirements = android==1.0, astroid==2.8.0, asyncgui==0.5.2, asyncio==3.4.3, asynckivy==0.5.2, audiostream==0.2, beautifulsoup4==4.10.0, bs4==0.0.1, certifi==2021.10.8, cffi==1.15.0, charset-normalizer==2.0.7, distro==1.6.0, docutils==0.18, idna==3.3, install==1.3.4, isort==5.9.3, jedi==0.18.0, Kivy==2.0.0, https://github.com/kivymd/KivyMD/archive/master.zip, lazy-object-proxy==1.6.0, lxml==4.6.3, mccabe==0.6.1, packaging==21.0, parso==0.8.2, Pillow==8.4.0, pkgconfig==1.5.5, platformdirs==2.4.0, pybind11==2.8.0, pycparser==2.20, pygame==2.0.1, Pygments==2.10.0, pyjnius==1.3.0, pylint==2.11.1, pyparsing==2.4.7, PySDL2==0.9.7, requests==2.26.0, scikit-build==0.12.0, six==1.16.0, soupsieve==2.2.1, toml==0.10.2, typed-ast==1.4.3, typing-extensions==3.10.0.2, urllib3==1.26.7, wrapt==1.13.1
requirements.source.kivymd = ../../kivymd


# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for new android toolchain)
android.presplash_color = #FFFFFF

# (list) Permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (int) Target Androi

# (int) Target Android API, should be as high as possible.
android.api = 28

# (int) Minimum API 
your APK will support.
android.minapi = 21
# (str) Android NDK version to use
android.ndk = 19b

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
android.accept_sdk_license = True

# (str) Android logcat filters to use
# android.logcat_filters = *:S python:D

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
# bin_dir = ./bin

#    -----------------------------------------------------------------------------
#    List as sections
#
#    You can define all the "list" as [section:key].
#    Each line will be considered as a option to the list.
#    Let's take [app] / source.exclude_patterns.
#    Instead of doing:
#
#[app]
#source.exclude_patterns = license,data/audio/*.wav,data/images/original/*
#
#    This can be translated into:
#
#[app:source.exclude_patterns]
#license
#data/audio/*.wav
#data/images/original/*
#


#    -----------------------------------------------------------------------------
#    Profiles
#
#    You can extend section / key with a profile
#    For example, you want to deploy a demo version of your application without
#    HD content. You could first change the title to add "(demo)" in the name
#    and extend the excluded directories to remove the HD content.
#
#[app@demo]
#title = My Application (demo)
#
#[app:source.exclude_patterns@demo]
#images/hd/*
#
#    Then, invoke the command line with the "demo" profile:
#
#buildozer --profile demo android debug
