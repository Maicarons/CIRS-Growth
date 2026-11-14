#!python

import os
import re
import argparse
import platform
from shutil import copy2, rmtree, copytree
from glob import iglob
import tarfile
from pathlib import Path

# Generate settings_text.nut for the requested language before packing.
# OpenTTD reads GS settings descriptions/labels at SCAN time, before it loads
# any translation, so the settings menu language must be fixed when the .tar
# is built.  All lang/*.txt files still ship for runtime GSText strings.
from tools.gen_settings import generate as generate_settings

# ----------------------------------
# Definitions:
# ----------------------------------

# Game Script name
gs_name = "CIRS_Growth"

# Language basenames in lang/ (english is the default / BaNaNaS build).
LANGS = [
    "english", "czech", "french", "galician", "german", "japanese",
    "polish", "russian", "simplified_chinese", "slovak",
    "traditional_chinese", "ukrainian",
]

# ----------------------------------

p = argparse.ArgumentParser(description="Build a CIRS Growth Game Script .tar")
p.add_argument("--lang", default="english", choices=LANGS,
               help="language for the GS settings menu (default: english)")
p.add_argument("--all-langs", action="store_true",
               help="build one .tar per language instead of just --lang")
args = p.parse_args()


def build(lang):
    mainversion = -1
    subversion = -1
    with open("version.nut", 'r+') as file:
        for line in file:
            r = re.search(r'SELF_MAJORVERSION\s+<-\s+([0-9]+)', line)
            if(r != None):
                mainversion = r.group(1)
            r2 = re.search(r'SELF_MINORVERSION\s+<-\s+([0-9]+)', line)
            if(r2 != None):
                subversion = r2.group(1)

    if(mainversion == -1 or subversion == -1):
        print("Couldn't find " + gs_name + " version in version.nut!")
        exit(-1)

    # Non-English builds get a language suffix so all tars can coexist and are
    # identifiable in Online Content / on the releases page.
    suffix = "" if lang == "english" else "-" + lang
    tmp_dir = gs_name + "-" + str(mainversion) + "." + str(subversion) + suffix
    tar_name = tmp_dir + ".tar"

    if os.path.exists(tmp_dir):
        rmtree(tmp_dir)
    os.mkdir(tmp_dir)

    files = iglob("*.nut")
    for file in files:
        if os.path.isfile(file):
            copy2(file, tmp_dir)
    copy2('readme.txt', tmp_dir)
    #copy2('license.txt', tmp_dir)
    copy2('changelog.txt', tmp_dir)
    copytree('lang', os.path.join(tmp_dir, 'lang'))

    # Generate the settings menu table LAST so it overwrites the checked-in
    # English default settings_text.nut copied above. Otherwise --lang with a
    # non-English language would silently ship an English settings menu.
    generate_settings(lang, os.path.join(tmp_dir, "settings_text.nut"))

    with tarfile.open(tar_name, "w:") as tar_handle:
        for root, dirs, files in os.walk(tmp_dir):
            for file in files:
                tar_handle.add(os.path.join(root, file))

    rmtree(tmp_dir)
    print("[MAKE TAR] %s  (settings menu: %s)" % (tar_name, lang))
    return tar_name


if args.all_langs:
    for lang in LANGS:
        build(lang)
else:
    build(args.lang)
