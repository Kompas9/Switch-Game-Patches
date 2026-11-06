# Fire Emblem: Fortune's Weave — 60 FPS patch

Version **1.0** unlocks the presentation interval and adjusts the game's timing
rate from 30 to 60. The initial interval-only experiment caused faster battle
animations; this release includes the timing adjustment tested afterward.

## Supported game build

| Item | Supported value |
| --- | --- |
| Game | Fire Emblem: Fortune's Weave |
| Game version | 1.1.0 |
| Title ID | `04007EF01F8AE000` |
| Main Build ID, trailing zero bytes omitted | `DB93B0125F4850601D61C3EDDE012F8EB2ECFE77` |
| Patch version | 1.0 |

This patch is specific to this executable build. Other updates require checking
their executable and patch locations again. It is **not** a Three Houses patch.

## Install in Lichii

1. Download and extract **Fire-Emblem-Fortunes-Weave-60FPS-v1.0.zip** from
   [Releases](https://github.com/Kompas9/Switch-Game-Patches/releases).
2. Stop the game. Disable/remove previous Fortune's Weave FPS experiments,
   including `FE-Fortunes-Weave-Present-Interval-1-TEST` and
   `FE-Fortunes-Weave-60FPS-Timing-TEST2`. Use one FPS mod at a time.
3. Right-click the game in Lichii and select **Open Mod Data Location**.
4. Copy the entire **`60FPS-v1.0`** folder into that location. The layout should be:

   ```text
   <game mod data location>/
     60FPS-v1.0/
       exefs/
         DB93B0125F4850601D61C3EDDE012F8EB2ECFE77.ips
   ```

5. Enable **`60FPS-v1.0`** in the game's Properties / Add-Ons if necessary.
6. Launch with emulator speed at **100%**, normal guest clock settings and your
   usual graphics settings. No emulator rebuild is required.

To verify loading, look in `eden_log.txt` for:

```text
Applying IPS patch from mod "60FPS-v1.0"
```

To uninstall, stop the game and disable the mod in Properties / Add-Ons, or move
its folder out of the mod data location. Original game files are not changed.

## Testing and limitations

- Tested by the user on a custom Lichii PGO build based on commit
  `6b26d955f564da230366817a3f3c4d5b6c551625`, with the game version above.
- With the timing adjustment, the user reported normal-looking battle animation
  speed, video and audio, including gameplay running below 60 FPS.
- Logged 600-present windows ranged around **38–48 FPS** in one run and included
  **59.9–60 FPS** windows in another. The log does not identify the scene of every
  window; these are not a whole-game benchmark or a sustained 60 FPS battle claim.
- Animation durations were not measured precisely against an unmodified run.
  A full playthrough, every cinematic and all timing-sensitive mechanics have
  not been validated. Compatibility with other emulators/hardware is untested.
- The patch raises the game limit; it does not guarantee 60 FPS on your hardware.
  Report speed changes, stutter, audio/video drift or other regressions with the
  game/build version, emulator version, scene and FPS.

## What changes

The IPS patch replaces two ARM64 instructions in `main`:

| Module address | Original | Replacement | Purpose |
| --- | --- | --- | --- |
| `0x005D18C` | `mov w22, w4` | `mov w22, #1` | Use presentation interval 1 in the NVN presentation path. |
| `0x007BF1AC` | `mov w9, #30` | `mov w9, #60` | Initialize the timing-rate field to 60. |

Several timing consumers use `60 / rate`, including the application's time
manager. This was the reason for pairing the timing adjustment with the unlock.
It is not proof that every subsystem supports arbitrary frame rates correctly.
IPS offsets include the `0x100` NSO header: `0x005D28C` and `0x007BF2AC`.

No emulator clock, audio decoder or video decoder changes are included.
`patch-details.json` records the exact bytes and hashes. `tools/build_patch.py`
recreates the IPS and can optionally verify the matching decompressed NSO dump.
No game executable, game assets, keys, firmware or saves are distributed.

## Credits and license

Created and tested as part of Kompas9's local Lichii / Fortune's Weave work.
The [Three Houses 60 FPS patch by masagrator](https://github.com/masagrator/NXGraphicsPatches/tree/master/Fire%20Emblem%20Three%20Houses/exefs_patches/FireEmblem3Houses-60FPS)
was suggested as a reference. These patch locations were independently located
in the matching Fortune's Weave executable; Three Houses offsets were not used.

The original documentation and build script in this repository are MIT-licensed.
Game software and third-party projects retain their respective rights.
