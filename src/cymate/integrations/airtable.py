"""Minimal Airtable API client."""

import requests

from cymate.config import require, settings

BASE_URL = "https://api.airtable.com/v0"


class Airtable:
    def __init__(self, api_key: str | None = None, base_id: str | None = None, timeout: int = 30):
        self.api_key = require(api_key or settings.airtable_api_key, "AIRTABLE_API_KEY")
        self.base_id = require(base_id or settings.airtable_base_id, "AIRTABLE_BASE_ID")
        self.timeout = timeout

    @property
    def _headers(self):
        return {"Authorization": f"Bearer {self.api_key}"}

    def list_records(self, table: str, **params):
        """Return all records in a table, following pagination."""
        records, offset = [], None
        while True:
            if offset:
                params["offset"] = offset
            resp = requests.get(
                f"{BASE_URL}/{self.base_id}/{table}",
                headers=self._headers,
                params=params,
                timeout=self.timeout,
            )
            resp.raise_for_status()
            data = resp.json()
            records.extend(data.get("records", []))
            offset = data.get("offset")
            if not offset:
                return records
