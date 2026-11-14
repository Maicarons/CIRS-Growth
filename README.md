# CIRS Growth

![CIRS Growth](https://i.imgur.com/37J9Kn4.png)

CIRS Growth is a Game Script for OpenTTD that manages town growth in a new and balanced way, making growth depend on varied cargo delivery (passengers, food, goods, ...) and sustained transportation of passengers and mail. It is an adaptation of [Renewed Village Growth](https://github.com/F1rrel/RenewedVillageGrowth) by Firrel, specifically extended to support all six economies of the [CIRS](https://github.com/Maicarons/CIRS) industry NewGRF set. The original script is itself a combination of [keoz's Renewed City Growth GS](https://www.tt-forums.net/viewtopic.php?f=65&t=69827) and [Sylf's City Growth Limiter GS](https://www.tt-forums.net/viewtopic.php?t=58238).

Repository: https://github.com/Maicarons/CIRS-Growth<br/>
Upstream: https://github.com/F1rrel/RenewedVillageGrowth<br/>
Documentation: https://maicarons.github.io/CIRS/cirs-growth.html (English) - https://maicarons.github.io/CIRS/zh/cirs-growth.html (简体中文)

## Requirements

- OpenTTD, v. 14.x or newer.
- GS SuperLib v. 40, ToyLib v. 2, Script Communication for GS v. 45 (you can find it on BaNaNaS, also accessible
  through OTTD's "Online Content").
- Industry sets: you can use any industry NewGRF
    - these are specifically supported industry NewGRF: CIRS (all six economies),
  Baseset (all climates), FIRS 1.4, 2, 3, 4.3, 5 (all economies), ECS 1.2 (any combination), YETI 0.1.6
  (all except Simplified), NAIS 1.0.6, ITI 1.6, 2.14, XIS 0.6, AXIS 2.2, OTIS 05, IOTC 0.1, LJI 0.1, WRBI 1200,
  Real Beta, Minimalist, PIRS 2022
    - using CIRS Growth with any other unsupported industry set will contain procedurally generated categories

## Translations
Currently available languages:
- English
- French (rmnvgr, Elarcis)
- Slovak
- Czech
- Simplified Chinese (SuperCirno, WenSimEHRP)
- Polish (qamil95)
- Galician (pvillaverde)
- German (pnkrtz)
- Japanese (fmang)
- Traditional Chinese (WenSimEHRP)
- Russian (Shkarlatov)
- Ukrainian (mortiy)

If you want to contribute to a translation, you can do it by modifying a file [english.txt](lang/english.txt) and posting it to the forum topic or creating a new issue/pull request with this file included. All instances of `{STRING[number]}` need to be replaced by `{STRING}` in all other languages. The settings-menu strings are the `STR_SETTINGS_*` keys at the end of each language file.

### Settings menu translations

OpenTTD captures Game Script setting descriptions and drop-down labels as plain strings when it **scans** the script, before any language is loaded, so the settings menu cannot be translated at runtime. CIRS Growth keeps these strings as `STR_SETTINGS_*` keys in `lang/*.txt` and bakes one language into each `.tar` at build time. `tools/gen_settings.py` generates `settings_text.nut` (loaded by `info.nut` via `require()`), and `make_tar.py` calls it before packing:

```sh
python make_tar.py --lang english              # CIRS_Growth-13.0.tar (default / BaNaNaS)
python make_tar.py --lang simplified_chinese  # CIRS_Growth-13.0-simplified_chinese.tar
python make_tar.py --all-langs                # one .tar per language (12 total)
```

The default archive (`CIRS_Growth-13.0.tar`) has an English settings menu and is the build published on BaNaNaS / *Online Content*. OpenTTD registers only one archive per script name and version, so the localized builds cannot be offered there separately; they are attached to the [GitHub Releases](https://github.com/Maicarons/CIRS-Growth/releases) instead. To use one, download the `.tar` matching your OpenTTD language, put it in your OpenTTD `game/` folder and remove any other `CIRS_Growth-13.0*.tar` there (two archives with the same name and version collide, and only the first is loaded).

All 12 language files are still included in every `.tar`, so in-game StoryBook, town signs and other `GSText` strings follow the game's language normally. The settings menu is the only text fixed at build time.

`settings_text.nut` is written with a UTF-8 BOM: OpenTTD's Squirrel loader selects its UTF-8 lexer only for files that start with a BOM. Without it, non-ASCII characters are read byte-by-byte and displayed as mojibake. The generator enforces this; `lang/*.txt` stays BOM-less because the game reads those with `fgets`, not Squirrel.

## License

CIRS Growth is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, version 2 of the License
(see file license.txt).

## Credits

Original author: Firrel (Renewed Village Growth)<br>
CIRS adaptation: Maicarons<br><br>
Thanks to:
- keoz for the Renewed City Growth GS
- Sylf for the City Growth Limiter GS

Thanks to contributors:
- rmnvgr
- pr0saic
- audunmaroey
- SuperCirno
- qamil95
- 2TallTyler
- pvillaverde
- pnkrtz
- fmang
- Elarcis
- lezzano000
- WenSimEHRP
- Shkarlatov
- JGRennison
- bigyihsuan
- rhoun
- skye0e
- mortiy
