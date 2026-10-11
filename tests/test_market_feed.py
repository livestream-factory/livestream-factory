from datetime import datetime, timedelta, timezone
from app.market_feed import Quote, is_stale, serialize_quote


def test_recent_quote_is_fresh():
    now = datetime(2026, 1, 1, tzinfo=timezone.utc)
    assert not is_stale(now - timedelta(seconds=120), now=now)


def test_old_quote_is_stale():
    now = datetime(2026, 1, 1, tzinfo=timezone.utc)
    assert is_stale(now - timedelta(seconds=301), now=now)


def test_future_quote_is_stale():
    now = datetime(2026, 1, 1, tzinfo=timezone.utc)
    assert is_stale(now + timedelta(seconds=1), now=now)


def test_naive_timestamp_is_stale():
    assert is_stale(datetime(2026, 1, 1))


def test_quote_includes_source_and_age_status():
    now = datetime(2026, 1, 1, tzinfo=timezone.utc)
    quote = Quote("TEST", "123", 1.2, now, "example-provider")
    result = serialize_quote(quote, now=now)
    assert result["source"] == "example-provider"
    assert result["stale"] is False
