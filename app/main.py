from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

ROOT = Path(__file__).resolve().parent.parent
app = FastAPI(title="LiveStream Factory", version="0.3.0-dev")


@app.get("/")
def dashboard():
    return FileResponse(ROOT / "web" / "index.html")


@app.get("/scene")
def scene():
    return FileResponse(ROOT / "web" / "scene.html")


@app.get("/api/health")
def health():
    return {"status": "ok", "service": "livestream-factory", "time_utc": datetime.now(timezone.utc).isoformat()}


@app.get("/api/markets")
def markets():
    return {
        "mode": "demo",
        "disclaimer": "FICTIONAL DEMO VALUES — NOT LIVE MARKET DATA",
        "instruments": [
            {"symbol": "S&P 500", "value": "5,240.00", "change_pct": 0.42},
            {"symbol": "NASDAQ", "value": "16,380.00", "change_pct": 0.68},
            {"symbol": "BTC/USD", "value": "64,250.00", "change_pct": -0.37},
            {"symbol": "GOLD", "value": "2,350.00", "change_pct": 0.21},
        ],
    }
