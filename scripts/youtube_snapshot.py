import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

KEY = os.environ["YOUTUBE_API_KEY"]
CHANNEL_ID = os.environ["YOUTUBE_CHANNEL_ID"]

params = urlencode({"part": "snippet,statistics", "id": CHANNEL_ID, "key": KEY})
url = "https://www.googleapis.com/youtube/v3/channels?" + params
with urlopen(url, timeout=30) as response:
    payload = json.load(response)

items = payload.get("items", [])
if not items:
    raise SystemExit("Channel not found")

item = items[0]
stats = item.get("statistics", {})
snippet = item.get("snippet", {})
now = datetime.now(timezone.utc)
record = {
    "snapshot_at": now.isoformat(),
    "channel_id": CHANNEL_ID,
    "title": snippet.get("title"),
    "country": snippet.get("country"),
    "default_language": snippet.get("defaultLanguage"),
    "statistics": {
        "subscribers": int(stats.get("subscriberCount", 0)),
        "views": int(stats.get("viewCount", 0)),
        "videos": int(stats.get("videoCount", 0))
    },
    "source": "YouTube Data API"
}

out = Path("data/youtube")
out.mkdir(parents=True, exist_ok=True)
(out / "channel-api.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
history = out / "history"
history.mkdir(exist_ok=True)
(history / f"{now.date().isoformat()}.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(record, ensure_ascii=False, indent=2))
