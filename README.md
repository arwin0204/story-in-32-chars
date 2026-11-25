# story-in-32-chars

[![make.fun](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/arwin0204/story-in-32-chars/rank.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/arwin0204/story-in-32-chars/reward.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

Entry for the [Tell a Whole Story in 32 Characters](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978) bounty on make.fun.

## The entry

> **WiFi died. So did the marriage**

One Wi-Fi network name, 30 characters, that lands a joke and implies a
whole story in the few words a passer-by sees in a phone's network list:
the Wi-Fi dying is bad enough — but the marriage dying with it is the
twist. A household, a dead router, and a relationship that apparently
ran on the same connection.

## How to run

```sh
python3 main.py            # writes the entry to /output/entry.txt
python3 main.py --check-only   # validate the entry without writing
```

The program is fully deterministic — no randomness, no network, no clock —
and self-checks the gate on every run: 1–32 characters, a single line,
not only whitespace.

## License

MIT — see [LICENSE](LICENSE).
