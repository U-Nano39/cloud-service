import os
import json
import time
import base64
import datetime

from urllib.request import Request, urlopen
from JustAlive import JustAlive


channel_id = 1114531313584709684
BotKey = os.getenv("DISCORD_USER_TOKEN")

class Discord:
    def __init__(self, token) -> None:
        self.token = token
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Discord SelfBot Python-urllib/3.9",
            "Authorization": self.token
        }

    def send_message(self, msg):
        while True:
            nowdatetime = datetime.datetime.now().strftime("%H:%M:%S")
            if nowdatetime == "24:00:00":
                time.sleep(1)
                response = urlopen(Request(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=self.headers, data=json.dumps({"content": msg}).encode(), method="POST"))
                if response.getcode() == 200:
                    print("Success.")

if __name__ == "__main__":
    JustAlive()
    
    discord = Discord(base64.b64decode(BotKey).decode())
    discord.send_message("> _DUMP 24:00_")
