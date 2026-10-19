# Heavy Equipment Search

Search for used heavy-equipment listings (excavators, dozers, loaders, cranes) that understands meaning, not just keywords: so a search for "Caterpillar digger" also finds "CAT 320 Excavator".

> **Status: work in progress.** Built in public as part of my AI engineering learning path. The checklist below shows what is done and what is planned.

## The problem

Equipment listings written by different dealers are messy: the same brand appears as "CAT", "cat " or "CATERPILLAR"; prices appear as "$85,000", "USD 78500" or "POA". Keyword search misses relevant machines, and messy data breaks filtering and sorting. This project cleans the data first, then compares keyword search against embedding-based semantic search.

## Progress

- [x] Project setup: uv, Ruff (lint + format), pytest
- [x] Price parser: multiple formats ("$85,000", "USD 78500"), missing values and "POA"
- [x] Brand name normalisation: known aliases to canonical names; unknown brands preserved
- [x] Engine-hours parser: commas, unit labels ("6,200 HRS"), missing values
- [x] Consistent missing-value handling for pandas data (None, NaN, `<NA>`)
- [x] Full CSV loader: applies all cleaners, converts types, removes duplicate listings
- [ ] Data validation with Pydantic
- [ ] Keyword search baseline
- [ ] Semantic search with OpenAI embeddings (with caching to control API cost)
- [ ] Evaluation: keyword vs semantic vs hybrid search on the same queries

**Tests:** 46 passing (unit tests for each cleaning function, plus integration tests for the full loader).

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

- Defensive data-cleaning functions for inconsistent real-world formats (prices, brand names, engine hours)
- Data pipelines with pandas: typed columns, nullable integers, de-duplication
- Handling missing data correctly across Python and pandas (`None`, NaN, `pd.NA`)
- Unit and integration testing with pytest, including edge cases and regression tests for bugs found
- Verifying tests by breaking code on purpose
- Narrow, deliberate error handling (catching only expected errors)
- Modern Python project tooling: uv, Ruff, `src/` layout
- Git workflow and secret hygiene (`.env` excluded, `.env.example` committed)