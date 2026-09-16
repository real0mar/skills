# PC-to-console graphics equivalence

Use this note when translating console Quality/Performance modes into PC settings.

## Method

1. Verify the official mode targets and technologies first: frame-rate target, dynamic resolution, reconstruction method, and whether RT/Lumen/Nanite features remain enabled.
2. Use a measured technical analysis for actual internal-resolution ranges and per-setting comparisons. Console presets are often bespoke and may fall between or below PC menu levels.
3. Label mappings by confidence:
   - Exact/observed: directly measured or matched.
   - Approximate/custom: nearest PC setting to a bespoke console value.
   - Inferred: visual comparison only.
4. Compare the performance mode the user actually cares about; do not lead with 30 fps Quality when they asked for 60+ fps.
5. Translate internal resolution into the game's own scale labels. Do not assume standardized DLSS/FSR names when the game exposes custom percentages.
6. Separate real rendered FPS from frame-generated output. Recommend frame generation only after establishing an adequate base frame rate and enabling the matching low-latency mode.
7. Note fixed-rate content such as pre-rendered 30 fps cinematics separately from gameplay.

## Halo: Campaign Evolved example (August 2026)

Official console modes are 30 fps Quality and 60 fps Performance; there is no console 120 fps mode. All consoles use dynamic resolution. Digital Foundry measured Series X Performance near 1224p internal and found that it retains UE5 Nanite, VSM, and hardware Lumen GI/reflections.

Approximate Series X/base-PS5 Performance mapping:

- Effects Medium
- Geometry custom, nearest Medium
- Global Illumination High
- Lighting Low
- Textures High
- Reflections below PC Low; Low is the nearest selectable value
- Atmospherics Low
- Post-processing Medium

At 4K output, the game's 59% "High" upscaling level renders about 2266x1274, making it a close static-resolution analogue to the measured ~1224p console result. TSR at roughly 60% plus a 60 fps minimum target more closely imitates console-style dynamic resolution.

Digital Foundry's PC sweet spot raises Reflections to Medium while keeping the other values above; it is not a strict console match but offers a better fidelity/performance balance. PS5 Pro Performance approximately mirrors base-console Quality settings at 60 fps and uses PSSR2, so its reconstruction quality has no exact PC analogue.

Sources:
- Halo Support, console graphics modes: https://support.halowaypoint.com/hc/en-us/articles/50946691293716-Halo-Campaign-Evolved-Graphics-Modes-Overview
- Halo Support, PC technology: https://support.halowaypoint.com/hc/en-us/articles/50944000913684-PC-Technology-in-Halo-Campaign-Evolved
- Digital Foundry, console analysis: https://www.digitalfoundry.net/features/halo-campaign-evolved-scales-well-from-ps5-pro-to-xbox-series-s-despite-its-full-throated-unreal-engine-5-features
- Digital Foundry, PC optimized settings: https://www.digitalfoundry.net/features/halo-campaign-evolved-pc-looks-stunning-but-requires-further-optimisation
