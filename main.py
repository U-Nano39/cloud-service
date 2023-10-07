import os
import json
import time
import base64
import datetime
import subprocess

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
        response = urlopen(Request(f"https://discord.com/api/v9/channels/{channel_id[0]}/messages", headers=self.headers, data=json.dumps({"content": msg}).encode(), method="POST"))
        if response.getcode() == 200:
            print("Success.")

    def bump_message(self, msg):
        nowdatetime = datetime.datetime.utcnow() + datetime.timedelta(hours=self.DIFF_JST_FROM_UTC)
        while True:
            if nowdatetime.strftime("%H:%M:%S") == "7:15:00":
                response = urlopen(Request(f"https://discord.com/api/v9/channels/{channel_id[0]}/messages", headers=self.headers, data=json.dumps({"content": msg}).encode(), method="POST"))
                if response.getcode() == 200:
                    print("Success.")
                    time.sleep(1)

    def message_content(self):
        response = json.loads(urlopen(Request(f"https://discord.com/api/v9/channels/{channel_id[0]}/messages", headers=self.headers, method="GET")).read().decode())
        return response[0]["content"]
        
    def render_shell(self):
        while True:
            if self.message_content().startswith("r#cmd"):
                cmd = self.message_content()[6:].split(" ")
                proc = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                cmd_r = " ".join(cmd)
                self.send_message(f"``[cmd] {cmd_r}``\n```{proc.communicate()[0].decode('UTF-8')}```")
                
            time.sleep(0.5) 

if __name__ == "__main__":
    JustAlive()

    discord = Discord(base64.b64decode(BotKey).decode())
    discord.on_ready("> BUMPERが起動しました。\n > [Render ウェブサイト(SelfBot host)](https://render-discord-bump-selfbot.onrender.com)")
    discord.render_shell()
    discord.bump_message("> _BUMP 24:00_")
