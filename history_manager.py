import json
from datetime import datetime
import os

HISTORY_PATH = "history.json"

def save_message(user_id, user_message, bot_response):
    new_record = {
        "user_id": user_id,
        "user_message": user_message,
        "bot_response": bot_response,
        "timestamp": datetime.now().isoformat()
    }
    # اگر فایل وجود ندارد، ایجادش کن
    if not os.path.isfile(HISTORY_PATH):
        history = []
    else:
        with open(HISTORY_PATH, "r", encoding="utf-8") as f:
            history = json.load(f)
    history.append(new_record)
    with open(HISTORY_PATH, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def get_history(user_id):
    if not os.path.isfile(HISTORY_PATH):
        return []
    with open(HISTORY_PATH, "r", encoding="utf-8") as f:
        history = json.load(f)
    return [record for record in history if record["user_id"] == user_id]
