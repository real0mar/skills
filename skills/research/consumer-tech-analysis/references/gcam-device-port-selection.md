# GCam Port Research Notes: OnePlus Examples

_Last verified: 2026-07-21. Treat exact versions as dated examples; re-check current compatibility before recommending._

## Durable method

- Verify the exact phone model and current OxygenOS/Android version.
- Use Celso Azevedo/GCam Hub for canonical APK variants and config files.
- Use XDA and device Telegram groups to confirm camera IDs, auxiliary-lens access, OS regressions, and practitioner consensus.
- Match the APK version to the config/library version named by its author. Do not assume a newer base is compatible.
- On many OnePlus devices, the `aweme` package name (`com.ss.android.ugc.aweme`) is required for access to all rear cameras under OxygenOS.
- Keep OEM camera for modes that depend on proprietary integration, especially high-frame-rate video and slow motion.

## OnePlus 11 example

A known simple, tuned combination was:

- BigKaka `AGC9.2.14_V7.0_aweme.apk`
- `Carlos_V1_AGC_9.2_OP11.agc`
- Config directory: `/Download/AGC.9.2/configs/`
- Config author designed it around HDRnet and advised leaving HDRnet enabled.

The value of this example is the exact matched pair, not that V7 should remain the recommendation forever. BigKaka continued active development on other AGC branches, but that does not make every old device config compatible with newer AGC releases.

## OnePlus 13 contrast case

Public reports identified BigKaka AGC 8.4 and 9.2 as working, but the highly tuned EGOIST setup depended on an older AGC 8.4 v9.6 build plus a custom library. It was more cumbersome, reported good on OxygenOS 15, and had OxygenOS 16 issues. This illustrates why “best IQ,” “easy,” and “currently maintained branch” must be answered separately.

## Pitfalls exposed by these cases

- Do not transfer a recommendation between OnePlus 11/11R/12/13/13R.
- Do not describe a frozen branch as actively updated merely because the modder is active elsewhere.
- Do not recommend a device config without naming its intended APK version when known.
- “Accepts auxiliary cameras” should be verified for the exact package variant and OS, not inferred from Snapdragon compatibility alone.
