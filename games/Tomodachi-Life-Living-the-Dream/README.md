# Tomodachi Life: Living the Dream - 60 FPS

Patch package **v1.0** contains the existing **60 FPS Max** cheat from
[masagrator's FPSLocker-Warehouse](https://github.com/masagrator/FPSLocker-Warehouse/blob/a86325bb0d298fb99293fa009c613dc71636d316/OTHER_WAYS.md), unchanged and credited.
This repository packages the cheat for Lichii; it does not claim authorship.

## Supported build

| Item | Value |
| --- | --- |
| Game version | 1.0.4 |
| Title ID | `010051F0207B2000` |
| Main Build ID prefix | `B39FEF373FB12154` |
| Main Build ID, full 32 bytes | `B39FEF373FB12154385D012AAB3BC99EF2944470000000000000000000000000` |

Other versions require a matching cheat; this file is specific to the build above.

## Install

1. Download **Tomodachi-Life-Living-the-Dream-60FPS-v1.0.zip** from
   [Releases](https://github.com/Kompas9/Switch-Game-Patches/releases).
2. Stop the game. Disable/remove previous Tomodachi FPS mods, including
   `Tomodachi-1.0.4-60FPS-FPSLocker-TEST`. Enable only one FPS mod.
3. Right-click Tomodachi in Lichii -> **Open Mod Data Location**.
4. Copy the whole **`Tomodachi-60FPS-v1.0`** folder into that location:

   ```text
   <game mod data location>/
     Tomodachi-60FPS-v1.0/
       cheats/
         B39FEF373FB12154.txt
   ```

5. Enable the mod in **Properties / Add-Ons**, then launch with emulator speed
   at **100%** and normal guest clock settings. No emulator rebuild is required.

Do not enable a 30 FPS cheat alongside this one. To uninstall, stop the game,
disable/remove this mod folder, then restart. Game files are not replaced.

## Testing and limits

- The user reported that this exact cheat worked correctly in their test on
  the custom Lichii build used for this project. They had previously observed
  that the unmodified painting mode already ran at 60 FPS.
- The cheat contents are byte-for-byte identical to the local test package;
  only the install folder name and documentation changed for release.
- A new patched gameplay log, precise timing comparison, full playthrough and
  all scenes have not been independently reviewed. Correct behavior below
  60 FPS and compatibility with other emulators/hardware are not guaranteed.
- This raises the configured limit; actual FPS depends on hardware/settings.
  Check animation/movement speed, painting mode, scene changes and audio sync.

## Implementation and attribution

The original cheat dereferences `main + 0x0390A8A0`, then writes:

| Object offset | Value |
| --- | --- |
| `0x00` | `1` |
| `0x20` | `60` |
| `0x44` | `1` |

The pointer and rate-control code were checked against the supplied 1.0.4
decompressed executable. The existing exact-build cheat was used rather than
creating a new executable patch. See `patch-details.json` for provenance/hash.

Source: **masagrator/FPSLocker-Warehouse**, commit
`a86325bb0d298fb99293fa009c613dc71636d316`, `OTHER_WAYS.md`.
No explicit license was declared in that source repository when checked.
This cheat is credited to its upstream source and is not covered by this
repository's MIT license for original documentation/scripts.
No game executables, assets, keys, firmware, logs or saves are distributed.
