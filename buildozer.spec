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
source.include_exts = py,png,jpg,jpeg,ttf,md,kv,json

# (list) List of inclusions using pattern matching
# source.include_patterns = assets/*
version = 0.1
# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]

# version.filename = blocknote 0.1

android.numeric_version = 1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy

requirements = python3,kivy,https://github.com/kivymd/KivyMD/archive/master.zip,sdl2_ttf==2.0.15,android.permissions,asynckivy,asyncgui,Pillow,requests,urllib3, certifi, openssl, android,charset-normalizer,idna,beautifulsoup4
requirements.source.kivymd = ../../kivymd


# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for new android toolchain)
android.presplash_color = #FFFFFF

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

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
