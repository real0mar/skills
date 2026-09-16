# Digital-wellbeing interventions: evidence and configuration notes

## Practical ranking by bypass resistance

1. **Externalized hard constraints:** trusted-person approval/PIN, device policy, timed lockbox, or physical separation. Best fit when the user already knows the limit but impulsively overrides it.
2. **Delayed overrides:** cooldowns that defer rule changes until the urge has passed. Use the principle “changes may affect tomorrow, never today.”
3. **Per-opening friction:** useful when an app still has legitimate uses and a complete block is too costly.
4. **Cue reduction:** grayscale, notification/badge removal, minimal launcher, and hiding apps. Helpful supplements, not primary controls.
5. **Awareness-only tools:** dashboards, reports, reminders, and instantly editable timers. Weak against motivated or habitual bypass.

The relevant design variable is not nominal strictness but **reversibility at the moment of temptation**.

## Evidence notes

### One Sec self-nudge app

Grüning, Riedel, and Lorenz-Spreen, PNAS (2023), DOI `10.1073/pnas.2213114120`; full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC9974409/

- Six-week field study, 280 participants.
- Participants abandoned 36% of intercepted target-app opening attempts.
- Opening attempts declined 37% over six weeks.
- Actual target-app openings declined 57% by week six.
- A separate preregistered online experiment (`N=500`) found that offering the option to dismiss was the strongest component; delay/friction also helped, while the deliberation message alone did not.
- Evidence caveat: the behavioral field portion was longitudinal rather than a standard randomized trial, and an author developed the app. Do not present 57% as guaranteed screen-time reduction.

### Three-week screen-time reduction RCT

Pieh et al., BMC Medicine (2025), DOI `10.1186/s12916-025-03944-z`; full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC11846175/

- 111 analyzed healthy students; baseline mean approximately 276 minutes/day.
- Intervention target was no more than two hours/day for three weeks.
- Reported small-to-medium improvements in well-being, depressive symptoms, sleep quality, and stress.
- Screen time rose rapidly after the intervention and approached baseline at follow-up.
- Lesson: a temporary target can work while actively enforced, but maintenance and rebound must be assessed separately.

### Grayscale

Holte and Ferraro, *The Social Science Journal* (2020), “True colors: Grayscale setting reduces screen time in college students,” DOI `10.1080/03623319.2020.1737461`.

- Frequently reported result: roughly 38 fewer minutes/day among college students assigned to grayscale.
- Later grayscale studies are mixed. Treat grayscale as low-cost cue reduction, not a robust commitment device.

## Android configuration pattern for impulsive timer overrides

Use an app blocker whose current official documentation confirms the required controls. As of the 2026-08 review, AppBlock Strict Mode documented:

- Approval by a trusted person
- Cooldown before an unlock takes effect
- Recurring schedule-following modes
- Locking edits, pauses, and deletion of blocking rules
- Uninstall protection
- Optional blocking of device Settings, recent apps, split screen, and reinstalled applications

Official guide: https://appblock.app/how-to-use-strict-mode-2/

Recommended pattern:

1. Block the small set of high-risk apps **and their web domains**.
2. Use a realistic recurring allowance plus complete blocks during sleep/focus windows.
3. Choose trusted-person approval when feasible; otherwise use a 12–24-hour cooldown.
4. Lock rule editing and uninstalling. Consider Settings/reinstallation blocking after testing.
5. Allowlist calls, messages, maps, authenticator, camera, banking, and other essentials.
6. Add per-opening friction to apps that remain legitimately useful.
7. Keep the phone physically outside the bedroom or work area when practical.
8. Pilot briefly before a critical day to avoid accidental lockout.

Do not recommend a user-known PIN as the main defense to someone who already overrides native limits; it merely adds steps to the same failure mode. No user-administered Android blocker is absolutely uncheatable, so external approval or physical separation remains stronger.