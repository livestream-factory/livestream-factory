# LiveStream Factory

A modular platform for automated 24/7 YouTube broadcasts.

## First milestone: Markets Live

This repository starts with a minimal Python service and a browser-based 1920×1080 broadcast scene. The scene uses **clearly labeled demo data**, not live market prices.

### Quick start (Python 3.10+)

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000 for the control page, http://127.0.0.1:8000/scene for the broadcast scene, and http://127.0.0.1:8000/api/health for health status.

### Safety and scope

- No YouTube broadcast is running yet.
- All sample market numbers are fictional and marked DEMO.
- Do not commit YouTube stream keys or API secrets.
- Market-data licensing, streaming output, monitoring, and persistent settings are later milestones.

## Roadmap

1. Runnable demo and broadcast scene
2. Licensed real market-data adapters with stale-data detection
3. FFmpeg/RTMP streaming, secret management, and restart monitoring
4. Operator dashboard, channel configurations, and multiple channels
