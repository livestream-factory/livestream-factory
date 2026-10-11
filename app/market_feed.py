"""Market data provider boundary. No unlicensed external feed is enabled by default."""
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Optional


@dataclass(frozen=True)
class Quote:
    symbol: str
    value: str
    change_pct: float
    observed_at: datetime
    source: str


def is_stale(observed_at: datetime, max_age_seconds: int = 300, now: Optional[datetime] = None) -> bool:
    """Fail closed when timestamps are missing timezone information or in the future."""
    if observed_at.tzinfo is None:
        return True
    current = now or datetime.now(timezone.utc)
    age = current - observed_at.astimezone(timezone.utc)
    return age < timedelta(0) or age > timedelta(seconds=max_age_seconds)


def serialize_quote(quote: Quote, now: Optional[datetime] = None) -> dict:
    return {
        "symbol": quote.symbol,
        "value": quote.value,
        "change_pct": quote.change_pct,
        "observed_at": quote.observed_at.isoformat(),
        "source": quote.source,
        "stale": is_stale(quote.observed_at, now=now),
    }
