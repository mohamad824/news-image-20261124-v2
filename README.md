# news-image-20261124-v2

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/mohamad824/news-image-20261124-v2/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/mohamad824/news-image-20261124-v2/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Tuesday 24 November 2026 — Early Edition: a broadsheet front page that sums up 24 November's world news in one image. 36 stories — COP31 collapses with no climate deal in Antalya, Jensen Huang is reinstated as Nvidia CEO as shares jump 31%, the ICJ rules Myanmar guilty of genocide — with a red sub-deck of the three leads, a six-number strip (+31% Nvidia, $2tn Anthropic debut, 24 dead in a Java factory fire, 12,000 evacuated in Manchester, $44bn CrowdStrike deal, 10,000 Rohingya killed), a UTC timeline, a grid of 10 story cards, 23 more stories in ALSO IN, a hand-drawn world map with 14 pins, and a DATE CHECK stating the honest coverage cutoff (02:30 UTC — the UTC day was not over at press time). The image is pre-rendered and held in this repository as `entry.png`; `main.py` (Python 3.13, standard library only) copies it to `/output/entry.png` — no third-party imports, no network, deterministic.

Why a copy: v1 drew the image with PIL, but the grader runs in the official `python:3.13-slim` image, which has no Pillow installed, so the import failed and the run exited before any drawing happened. This version keeps the same verified image and removes the dependency entirely, exactly as the competition rules bless: the simplest program copies an image the repository holds.

## Run it

```sh
python3 main.py
```

This writes `/output/entry.png` (1024×1024, deterministic — two runs produce identical bytes).

---

<sub>Entered on [make.fun](https://make.fun/?ref=196fg0bj&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
