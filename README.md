# Switch Game Patches

Game-specific patches for **Nintendo Switch and Switch 2 games**, tested with
Lichii on Windows. Each game has its own supported executable build, package
version, installation instructions, testing notes and credits.

## Available patches

| Game | Platform | Supported game version | Package | What it does |
| --- | --- | --- | --- | --- |
| [Fire Emblem: Fortune's Weave](games/Fire-Emblem-Fortunes-Weave) | Switch 2 | 1.1.0 | v1.0 | 60 FPS presentation unlock plus timing-rate adjustment. |
| [Tomodachi Life: Living the Dream](games/Tomodachi-Life-Living-the-Dream) | Switch | 1.0.4 | v1.0 | Existing exact-build 60 FPS Max cheat from masagrator's FPSLocker-Warehouse, packaged unchanged. |

**Download individual game ZIPs from [Releases](https://github.com/Kompas9/Switch-Game-Patches/releases).**
Release `v1.1` adds Tomodachi and the shared repository layout. Each game package
remains v1.0. Historical release `v1.0` contains the original Fire Emblem package.

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
