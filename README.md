# Switch Game Patches

Game-specific patches for **Nintendo Switch and Switch 2 games**, tested with
Lichii on Windows. Each game has its own supported executable build, package
version, installation instructions, testing notes and credits.

## Available patches

| Game | Platform | Supported game version | Package | What it does |
| --- | --- | --- | --- | --- |
| [Fire Emblem: Fortune's Weave](games/Fire-Emblem-Fortunes-Weave) | Switch 2 | 1.1.0 | v1.0 | 60 FPS presentation unlock plus timing-rate adjustment. |
| [Fire Emblem: Fortune's Weave - ultrawide](games/Fire-Emblem-Fortunes-Weave/ULTRAWIDE.md) | Switch 2 | 1.1.0 | v1.0 | 3440x1440 camera, centered 16:9 UI/clipping and pillarboxed movies in one mod. |
| [Tomodachi Life: Living the Dream](games/Tomodachi-Life-Living-the-Dream) | Switch | 1.0.4 | v1.0 | Existing exact-build 60 FPS Max cheat from masagrator's FPSLocker-Warehouse, packaged unchanged. |

## Download ZIPs

- **[Fire Emblem - 60 FPS v1.0](https://github.com/Kompas9/Switch-Game-Patches/raw/refs/heads/main/downloads/Fire-Emblem-Fortunes-Weave-60FPS-v1.0.zip)** - game version 1.1.0.
- **[Fire Emblem - 3440x1440 ultrawide v1.0](https://github.com/Kompas9/Switch-Game-Patches/raw/refs/heads/main/downloads/Fire-Emblem-Fortunes-Weave-Ultrawide-3440x1440-v1.0.zip)** - camera, UI/clipping and movie fixes combined; game version 1.1.0.
- **[Tomodachi - 60 FPS v1.0](https://github.com/Kompas9/Switch-Game-Patches/raw/refs/heads/main/downloads/Tomodachi-Life-Living-the-Dream-60FPS-v1.0.zip)** - game version 1.0.4.
- [SHA256 checksums](downloads/Switch-Game-Patches-v1.2-SHA256.txt).

ZIPs are also available from [Releases](https://github.com/Kompas9/Switch-Game-Patches/releases).

Release `v1.2` adds the combined Fire Emblem ultrawide fix. Individual patch
packages remain v1.0. Earlier FPS releases remain available.

## Installation

Stop the game, right-click it in Lichii -> **Open Mod Data Location**, then copy
the selected ZIP's mod folder there. Enable it in **Properties / Add-Ons**.
Use **100% emulator speed** and normal clock settings. Read the per-game README
for supported Build IDs, exact folder layout and any conflicting test mods.
Install each patch only in its corresponding game's mod directory.

Higher limits do not guarantee 60 FPS. User testing is limited; every scene,
mechanic, hardware configuration and emulator has not been validated. Report
the game/update and Build ID, emulator build, scene, FPS and timing/sync issues.

## Credits and scope

- Fire Emblem patch: located and tested during Kompas9's local Lichii work.
- Tomodachi cheat: **masagrator/FPSLocker-Warehouse**, copied unchanged with
  source attribution. See the game's README and [third-party notes](THIRD-PARTY.md).
- Repository MIT license applies to original documentation/scripts, not to
  third-party cheat material or Nintendo game software.

Only patch data, metadata and documentation/tools are provided. No game
executables, game assets, keys, firmware, logs or saves are included.
