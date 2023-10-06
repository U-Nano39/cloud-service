import os
import json
import time
import base64
import datetime

from urllib.request import Request, urlopen
from JustAlive import JustAlive


channel_id = [798566757101994015, 1114531313584709684]
#channel id list memo 0:main server 1:namek free channel  

BotKey = os.getenv("DISCORD_USER_TOKEN")

class Discord:
    def __init__(self, token) -> None:
        self.token = token
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Discord SelfBot Python-urllib/3.9",
            "Authorization": self.token
        }

        self.DIFF_JST_FROM_UTC = 9

    def on_ready(self, msg):
        boot_notice = urlopen(Request(f"https://discord.com/api/v9/channels/{channel_id[0]}/messages", headers=self.headers, data=json.dumps({"content": msg}).encode(), method="POST"))
        if boot_notice.getcode() == 200:
            print("Success.")

    def send_message(self, msg):
        while True:
            nowdatetime = datetime.datetime.utcnow() + datetime.timedelta(hours=self.DIFF_JST_FROM_UTC)
            if nowdatetime.strftime("%H:%M:%S") == "24:00:00":
                time.sleep(1)
                response = urlopen(Request(f"https://discord.com/api/v9/channels/{channel_id[1]}/messages", headers=self.headers, data=json.dumps({"content": msg}).encode(), method="POST"))
                if response.getcode() == 200:
                    print("Success.")

if __name__ == "__main__":
    JustAlive()

    nowdatetime = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
    discord = Discord(base64.b64decode(BotKey).decode())
    discord.on_ready("> DUMPERが起動しました。\n > [Render ウェブサイト(SelfBot host)](https://render-discord-dump-selfbot.onrender.com)")
    discord.send_message("> _DUMP 24:00_")
