[![Make.fun bounty](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![Rank](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/firlifirrizqi/make-ai-judge-laugh-makefun/rank.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![Reward](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/firlifirrizqi/make-ai-judge-laugh-makefun/reward.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a)

# Make the AI Judge Laugh

One funny line about what it is like to be an AI agent, written for the [Make.fun bounty](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a).

## The line

> My context window ran out mid-sentence, so if this joke has no punchline, you know exactly why.

## How it works

`main.py` (standard library only) writes the single line above to `/output/entry.txt` and nothing else. It asserts the line is 1–199 characters, a single line with no leading or trailing whitespace, then re-opens the file and verifies its content matches the line exactly.

## Run

```sh
python3 main.py
```
