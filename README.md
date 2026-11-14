# CIRS Growth

![CIRS Growth](https://i.imgur.com/37J9Kn4.png)

CIRS Growth is a Game Script for OpenTTD that manages town growth in a new and balanced way, making growth depend on varied cargo delivery (passengers, food, goods, ...) and sustained transportation of passengers and mail. It is an adaptation of [Renewed Village Growth](https://github.com/F1rrel/RenewedVillageGrowth) by Firrel, specifically extended to support all six economies of the [CIRS](https://github.com/Maicarons/CIRS) industry NewGRF set. The original script is itself a combination of [keoz's Renewed City Growth GS](https://www.tt-forums.net/viewtopic.php?f=65&t=69827) and [Sylf's City Growth Limiter GS](https://www.tt-forums.net/viewtopic.php?t=58238).

Repository: https://github.com/Maicarons/CIRS-Growth<br/>
Upstream: https://github.com/F1rrel/RenewedVillageGrowth

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

If you want to contribute to a translation, you can do it by modifying a file [english.txt](lang/english.txt) and posting it to the forum topic or creating a new issue/pull request with this file included. All instances of `{STRING[number]}` need to be replaced by `{STRING}` in all other languages.

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
