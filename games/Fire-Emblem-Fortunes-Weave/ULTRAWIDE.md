# Fire Emblem: Fortune's Weave - 3440x1440 ultrawide fix

Package **v1.0** combines the user-tested camera, UI/clipping and movie patches
into **one mod folder**. Target aspect ratio is **43:18 (3440x1440)**, commonly
called 21:9. This is not a universal patch for other ultrawide ratios.

## Included fixes

- **3D camera:** widens matching default perspective cameras from 16:9 to 43:18.
- **UI:** keeps matching HUD, text, portraits and dialogue projections centered
  at 16:9 proportions, with corresponding UI scissor correction for lists.
- **Prerendered movies:** fits the native-movie path into a centered 16:9 region,
  clears the side bars to opaque black, then restores the full viewport.

At 3440x1440, the intended UI/movie area is 2560x1440, with 440 pixels on each
side. The wider world remains visible behind the UI; movies have black bars.
Integer viewport rounding can cause a subpixel/one-pixel difference.

## Supported build

| Item | Value |
| --- | --- |
| Game version | 1.1.0 |
| Title ID | `04007EF01F8AE000` |
| Main Build ID, trailing zeros omitted | `DB93B0125F4850601D61C3EDDE012F8EB2ECFE77` |
| Package version | 1.0 |
| Output aspect | 3440x1440 / 43:18 |

Other game updates need a matching patch. Resolution scaling does not change
the intended output aspect, but not every scaling/emulator setting is tested.

## Download and install

1. Download [Fire-Emblem-Fortunes-Weave-Ultrawide-3440x1440-v1.0.zip](https://github.com/Kompas9/Switch-Game-Patches/raw/refs/heads/main/downloads/Fire-Emblem-Fortunes-Weave-Ultrawide-3440x1440-v1.0.zip).
2. Stop the game. **Disable/remove all earlier ultrawide test mods:**
   - `FE-Fortunes-Weave-3440x1440-TEST`
   - `FE-Fortunes-Weave-3440x1440-UI-TEST2`
   - `FE-Fortunes-Weave-3440x1440-UI-TEST3`
   - `FE-Fortunes-Weave-3440x1440-MOVIE-TEST1`
3. Right-click Fire Emblem in Lichii -> **Open Mod Data Location**.
4. Copy the entire **`Ultrawide-3440x1440-v1.0`** folder there and enable it in Properties / Add-Ons:

   ```text
   <game mod data location>/
     Ultrawide-3440x1440-v1.0/
       exefs/
         DB93B0125F4850601D61C3EDDE012F8EB2ECFE77.ips
   ```

5. Select **Graphics -> Aspect Ratio -> Stretch to Window** and use a
   **3440x1440 window/fullscreen output**. Restart the game.
6. Keep emulator speed at **100%** and normal guest clock settings.

**The FPS patch is separate:** `60FPS-v1.0` may remain enabled. This package
neither includes nor overwrites its two instruction changes. No emulator
rebuild is needed. Other aspect/FOV mods should be disabled.

The log should show `Applying IPS patch from mod "Ultrawide-3440x1440-v1.0"`.
To uninstall, stop the game, disable/remove this folder, then restart. Select
the normal 16:9 output setting if you no longer use the ultrawide camera patch.
Original game files and emulator binaries are not replaced.

## Testing and limitations

The user reported correct-looking wide gameplay, centered UI, corrected weapon
selection clipping, and movie proportions after testing the three components.
Tests used the exact game build above with Lichii build 88 and/or the project's
custom PGO/AV1 build. This is limited visual testing, not a full playthrough.

The merged patched executable image was verified **byte-for-byte identical**
to applying those three component patches separately. Offline ARM64 execution
checks cover six camera cases, nine UI projection cases, nine clipping cases,
and seven movie-clear/draw/viewport-restoration cases. The merged download has
not been separately played through. Gameplay timing and movie decoding are
unchanged by this package.

Some non-default camera/UI paths, unusual source-video shapes, fullscreen
effects, input hitboxes and other emulator/hardware combinations may still
need adjustments. Report the game Build ID, emulator build, scene, output
dimensions, screenshot and log for regressions. Higher FPS is not guaranteed.

## Implementation and credits

`ultrawide-patch-records.json` records exact original/replacement bytes and
provenance. `tools/build_ultrawide_patch.py` recreates the IPS32 and can verify
the supported decompressed NSO dump without changing it. The source dump,
captured frames, logs, game assets, keys, firmware and saves are not distributed.

Located and tested during Kompas9's local Lichii / Fortune's Weave work.
[Fl4sh9174's Three Houses ultrawide patch](https://github.com/Fl4sh9174/Switch-Emulator-Ultrawide-FPS-Mods)
was inspected as a reference; its offsets were not copied. The Fortune's Weave
camera, UI, scissor and movie hooks were located in the matching executable.
Original documentation and tools are covered by the repository MIT license;
game software retains its respective rights.
