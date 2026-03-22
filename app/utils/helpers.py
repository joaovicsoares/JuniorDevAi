"""
General-purpose utility / helper functions.
"""

from datetime import datetime, timezone


def utc_now() -> datetime:
    """Return the current UTC datetime (timezone-aware)."""
    return datetime.now(timezone.utc)


def truncate(text: str, max_length: int = 100) -> str:
    """Truncate a string and append '…' if it exceeds *max_length*."""
    if len(text) <= max_length:
        return text
    return text[: max_length - 1] + "…"
