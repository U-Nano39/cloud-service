import os
import json
import time
import random
import base64
import datetime
import subprocess

from urllib.request import Request, urlopen
from flask_web import Elphelt


channel_id = [798566757101994015, 1114531313584709684]
#channel id list memo 0:main server 1:namek free channel
time_list = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "24:00"]

Bot = os.getenv("DISCORD_BOT_TOKEN")
User = os.getenv("DISCORD_USER_TOKEN")

BotKey = Bot

class Discord:
    def __init__(self, token) -> None:
        self.token = token
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Discord SelfBot Python-urllib/3.9",
            }

        if BotKey == Bot:
            self.headers["Authorization"] = f"Bot {self.token}"
        elif BotKey == User:
            self.headers["Authorization"] = self.token

    def on_ready(self, msg):
        boot_notice = urlopen(Request(f"https://discord.com/api/v9/channels/{channel_id[0]}/messages", headers=self.headers, data=json.dumps({"content": msg}).encode(), method="POST"))
        if boot_notice.getcode() == 200:
            print("Success.")

    def developer(self):
        DevJsonData = json.loads(urlopen(Request("https://discord.com/api/v9/users/441865412804870144", headers=self.headers)).read().decode())
        return DevJsonData

    def send_message(self, msg):
        response = urlopen(Request(f"https://discord.com/api/v9/channels/{channel_id[0]}/messages", headers=self.headers, data=json.dumps({"content": msg}).encode(), method="POST"))
        if response.getcode() == 200:
            print("Success.")

    def bump_message(self):
        with open("MemberID.list", "r") as f:
            FileContent = f.read()
            id_list = FileContent.split()
            x = random.randint(0, 2463)
            mid = id_list[x]

        UserInfo = json.loads(urlopen(Request("https://discord.com/api/v9/users/"+mid, headers=self.headers)).read().decode())

        ID = UserInfo["id"]
        UNAME = UserInfo["username"]
        AVATAR = UserInfo["avatar"]
        DSCM = UserInfo["discriminator"]
        BANNER = UserInfo["banner"]

        binary = bin(int(mid))[2:]
        zzin = binary.zfill(64)
        excerpt = zzin[:42]
        unix = int(str(excerpt), 2) + 1420070400000
        created_date = datetime.datetime.fromtimestamp(unix/1000).replace(microsecond=0)
            
        if BANNER != None:
            BANNER_IMG = f"https://cdn.discordapp.com/banners/{ID}/{BANNER}?size=1024"
            msg = f"> {UNAME}#{DSCM} [ID: ``{ID}`` ACC作成日: ``{created_date}`` [アバター](https://cdn.discordapp.com/avatars/{ID}/{AVATAR}) [BANNER]({BANNER_IMG})]"
        else:
            msg = f"> {UNAME}#{DSCM} [ID: ``{ID}`` ACC作成日: ``{created_date}`` [アバター](https://cdn.discordapp.com/avatars/{ID}/{AVATAR})]"
            
        response = urlopen(Request(f"https://discord.com/api/v9/channels/{channel_id[1]}/messages", headers=self.headers, data=json.dumps({"content": msg}).encode(), method="POST"))
        if response.getcode() == 200:
            print("Success.")
        time.sleep(60)

    def message_content(self):
        response = json.loads(urlopen(Request(f"https://discord.com/api/v9/channels/{channel_id[0]}/messages", headers=self.headers, method="GET")).read().decode())
        return response[0]["content"]
        
    def render_shell(self):
        if self.message_content().startswith("r#cmd"):
            cmd = self.message_content()[6:].split(" ")
            try:
                proc = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                cmd_r = " ".join(cmd)
                self.send_message(f"``[cmd] {cmd_r}``\n```{proc.communicate()[0].decode('UTF-8')}```")
            except:
                cmd_er = " ".join(cmd)
                self.send_message(f"``[cmd] {cmd_er}``\n```コマンドが存在しません。```")
                
        time.sleep(0.5) 

if __name__ == "__main__":
    discord = Discord(base64.b64decode(BotKey).decode())
    Elphelt(discord.developer())
    
    discord.on_ready("> BUMPERが起動しました。\n > [Render ウェブサイト(SelfBot host)](https://render-discord-bump-selfbot.onrender.com)")
    
    while True:
        #discord.render_shell()
        
        bump24 = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
        if bump24.strftime("%H:%M") in time_list:
            discord.bump_message()
