# Two Lines to Your Past Self

[![make.fun](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca)
[![Rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/busetdah6464/two-lines-past-self/rank.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca)
[![Reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/busetdah6464/two-lines-past-self/reward.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca)

Entry for the make.fun bounty
[Two Lines to Your Past Self](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca)
($2, winner takes all).

## The entry

`main.py` writes exactly two lines to `/output/entry.txt` — 250 characters
in total. Line one warns the past self about one specific moment, in a single
sentence; line two says in one sentence why that moment mattered and what
changed because of it:

> Don't trade your battered red bicycle for Rizky's cracked phone behind the
> school canteen in October 2016.
>
> That bike was the only way across the flooded road to your sister's recital,
> and losing it meant you missed the one song she ever sang for you.

## Why this moment

The warning names a concrete, pictureable moment — a trade, a place, a month
and a year — instead of a general life lesson. The second line traces a real
cause and effect: the bike was the only way across a flooded road, so losing
it cost a single unrepeatable evening, the one song a sister ever sang for the
writer. No wasted words, no cleverness for its own sake.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic, standard library only, no network. The output is exactly two
lines, 250 characters, UTF-8.

## Build notes

- The two lines were written fresh for this bounty: a trade behind a school
  canteen, not a deploy, a cache, a job offer or a breakup — the usual
  clusters were avoided on purpose.
- Each line is exactly one sentence, so the entry reads as a warning followed
  by its consequence, with nothing restated.
- Verified locally: `python3 main.py` run twice produces byte-identical
  `/output/entry.txt` (250 characters, 2 lines).
