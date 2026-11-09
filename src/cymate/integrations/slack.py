"""Minimal Slack Web API client."""

import requests

from cymate.config import require, settings

BASE_URL = "https://slack.com/api"


class Slack:
    def __init__(self, token: str | None = None, timeout: int = 30):
        self.token = require(token or settings.slack_bot_token, "SLACK_BOT_TOKEN")
        self.timeout = timeout

    def post_message(self, channel: str, text: str):
        resp = requests.post(
            f"{BASE_URL}/chat.postMessage",
            headers={"Authorization": f"Bearer {self.token}"},
            json={"channel": channel, "text": text},
            timeout=self.timeout,
        )
        resp.raise_for_status()
        data = resp.json()
        if not data.get("ok"):
            raise RuntimeError(f"Slack error: {data.get('error')}")
        return data
