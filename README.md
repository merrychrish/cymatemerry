# cymatemerry

Python automation scripts for Cymate operations (SmartLead, Airtable, Slack).

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env   # then fill in your keys
```

## Layout

```
src/cymate/
  config.py            # loads settings from .env
  integrations/        # thin API clients (SmartLead, Airtable, Slack)
scripts/               # runnable entry points, one task per file
tests/                 # pytest tests
```

## Running a script

```bash
python scripts/example.py
```

## Tests

```bash
pytest
```
