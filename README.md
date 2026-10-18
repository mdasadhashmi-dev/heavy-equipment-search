# Heavy Equipment Search

Search for used heavy-equipment listings (excavators, dozers, loaders, cranes) that understands meaning, not just keywords: so a search for "Caterpillar digger" also finds "CAT 320 Excavator".

> **Status: work in progress.** Built in public as part of my AI engineering learning path. The checklist below shows what is done and what is planned.

## The problem

Equipment listings written by different dealers are messy: the same brand appears as "CAT", "cat " or "CATERPILLAR"; prices appear as "$85,000", "USD 78500" or "POA". Keyword search misses relevant machines, and messy data breaks filtering and sorting. This project cleans the data first, then compares keyword search against embedding-based semantic search.

## Progress

- [x] Project setup: uv, Ruff (lint + format), pytest
- [x] Price parser handling multiple formats, missing values and "POA", with 11 unit tests
- [x] Brand name normalisation
- [ ] Full CSV loader with de-duplication
- [ ] Data validation with Pydantic
- [ ] Keyword search baseline
- [ ] Semantic search with OpenAI embeddings (with caching to control API cost)
- [ ] Evaluation: keyword vs semantic vs hybrid search on the same queries

## Tech stack

Python 3.12 · pandas · pytest · Ruff · uv

## Project structure

```
heavy-equipment-search/
├── data/listings.csv               # sample listings (synthetic, see note below)
├── src/heavy_equipment_search/
│   └── loader.py                   # data cleaning functions
├── tests/test_loader.py            # unit tests
└── pyproject.toml                  # dependencies and tool config
```

## Run it locally

Requires [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/mdasadhashmi-dev/heavy-equipment-search.git
cd heavy-equipment-search
uv sync
uv run pytest -v
```

## Data

`data/listings.csv` is a small **synthetic** dataset written for this project. It deliberately includes the inconsistencies found in real listings (brand spellings, price formats, missing values, duplicates). It does not contain real dealer or customer data.

## Skills demonstrated so far

- Writing defensive data-cleaning functions for inconsistent real-world formats
- Test-driven verification with pytest, including edge cases and regression tests for fixed bugs
- Narrow, deliberate error handling (catching only expected errors)
- Modern Python project tooling: uv, Ruff, `src/` layout
- Git workflow and secret hygiene (`.env` excluded, `.env.example` committed)