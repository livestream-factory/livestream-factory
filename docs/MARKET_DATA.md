# Market data integration policy

The application currently uses **fictional demonstration values**.

Before switching to live quotes:
1. Select a provider with explicit permission for public YouTube display/redistribution.
2. Store credentials in environment variables or a secret manager; never in Git.
3. Normalize provider symbols, source names, observed timestamps, and price units.
4. Mark quotes stale after a configured threshold; never silently substitute demo quotes for live prices.
5. Handle exchange delays, market closures, API rate limits, and errors visibly.
6. Verify attribution requirements and the provider's commercial terms.

The `app.market_feed` module supplies a small tested quote contract and staleness checks. It does not yet fetch external data.
