"""Settings loaded from environment variables (and a local .env file)."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    smartlead_api_key: str = os.getenv("SMARTLEAD_API_KEY", "")
    airtable_api_key: str = os.getenv("AIRTABLE_API_KEY", "")
    airtable_base_id: str = os.getenv("AIRTABLE_BASE_ID", "")
    slack_bot_token: str = os.getenv("SLACK_BOT_TOKEN", "")


def require(value: str, name: str) -> str:
    """Return value, or raise a clear error if it is missing."""
    if not value:
        raise RuntimeError(f"{name} is not set. Add it to your .env file.")
    return value


settings = Settings()
