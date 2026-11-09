# cymatemerry

Python automation scripts for Cymate ops.

- Package code lives in `src/cymate/`; API clients in `src/cymate/integrations/`.
- Runnable tasks go in `scripts/`, one task per file, with a `main()` function.
- Secrets come from `.env` via `cymate.config.settings`. Never hardcode or commit keys.
- Run tests with `pytest`, lint with `ruff check .`.
