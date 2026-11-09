"""Minimal SmartLead API client."""

import requests

from cymate.config import require, settings

BASE_URL = "https://server.smartlead.ai/api/v1"


class SmartLead:
    def __init__(self, api_key: str | None = None, timeout: int = 30):
        self.api_key = require(api_key or settings.smartlead_api_key, "SMARTLEAD_API_KEY")
        self.timeout = timeout

    def _get(self, path: str, **params):
        params["api_key"] = self.api_key
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def list_campaigns(self):
        return self._get("/campaigns")
