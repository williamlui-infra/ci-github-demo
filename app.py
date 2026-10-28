# app.py
import os
from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Flask

app = Flask(__name__)

# 預設時區，可用環境變數 TZ 覆寫（例如 TZ=UTC）
TIMEZONE = os.environ.get("TZ", "Asia/Taipei")


@app.route("/")
def index():
    now = datetime.now(ZoneInfo(TIMEZONE))
    return f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>現在時間</title>
  <!-- 每秒自動刷新 -->
  <meta http-equiv="refresh" content="1">
  <style>
    body {{
      margin: 0;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-family: system-ui, -apple-system, "Noto Sans TC", sans-serif;
      background: #0f172a;
      color: #e2e8f0;
    }}
    h1 {{ font-size: 1.25rem; font-weight: 400; letter-spacing: .2em; color: #94a3b8; }}
    .time {{ font-size: clamp(2rem, 10vw, 5rem); font-variant-numeric: tabular-nums; font-weight: 700; }}
    .meta {{ color: #64748b; font-size: .9rem; }}
  </style>
</head>
<body>
  <h1>現在時間</h1>
  <div class="time">{now:%H:%M:%S}</div>
  <div class="meta">{now:%Y-%m-%d} ・ {now.tzname()}</div>
</body>
</html>"""


@app.route("/healthz")
def healthz():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
