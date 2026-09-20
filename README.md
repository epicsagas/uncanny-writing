# The Uncanny Valley of AI Writing / AI 글쓰기의 불쾌한 골짜기

Why do readers turn away from AI-generated text — and what does the evidence
actually support? A fact-checked research dossier: five cited sources
independently verified (two needed corrections), 86 papers collected from
arXiv and OpenAlex, an evidence map across seven themes, counter-evidence,
and a ledger of four open research gaps.

**[Read the dossier](https://epicsagas.github.io/uncanny-writing/)** — 한국어 · English (toggle in the top-right corner).

## How it was built

Papers were collected, classified by theme, and triage-rated with
[research-agent](https://github.com/epicsagas/research-agent) — a personal
long-term research assistant that indexes arXiv / OpenAlex papers into SQLite
with full-text search and runs LLM knowledge-gap analysis. The four gaps in
section 05 are the output of that gap analysis over the full corpus. Every
source cited in the originating analysis was checked against its primary
record (DOI, venue, exact title); the verification verdicts are in section 01.

## Stack

Static site — one self-contained HTML file (data embedded, ~94 KB). Language
toggle with `localStorage` persistence, theme-filtered paper browser with
expandable abstracts. No framework, no build step, no backend, no tracking.
