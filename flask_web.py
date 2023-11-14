import os
import json
import base64
import datetime

from PIL import Image

from urllib.request import Request, urlopen
from flask import Flask, render_template
from flask_socketio import SocketIO
from threading import Thread


app = Flask(__name__)
BotKey = os.getenv("DISCORD_BOT_TOKEN")

headers = {
        "Content-Type": "application/json",
        "User-Agent": "Discord V9APIBot Python-urllib/3.9",
        "Authorization": f"Bot {base64.b64decode(BotKey).decode()}"
        }

def USERDATA(USER_ID=None):
    if USER_ID is None:
        USER_ID = 441865412804870144
    
    JsonData = json.loads(urlopen(Request("https://discord.com/api/v9/users/"+str(USER_ID), headers=headers)).read().decode())
    return JsonData

USER = USERDATA()

def USERDICT(ID=None):
    if ID is None:
        USER = USERDATA()
        ID = USER["id"]
        CTX_D = {}
    
        CTX_D["id"] = USER["id"]
        CTX_D["uname"] = USER["username"]
        CTX_D["avatar"] = USER["avatar"]
        CTX_D["dscm"] = USER["discriminator"]
        CTX_D["banner"] = USER["banner"]

        binary = bin(int(ID))[2:]
        zzin = binary.zfill(64)
        excerpt = zzin[:42]
        unix = int(str(excerpt), 2) + 1420070400000

        CT_DATE = datetime.datetime.fromtimestamp(unix/1000).replace(microsecond=0).strftime("%Y %m/%d %H:%M:%S")
        CTX_D["ct_date"] = CT_DATE
        
        return CTX_D
    else:
        USER = USERDATA(ID)
        CTX_D = {}
    
        CTX_D["id"] = USER["id"]
        CTX_D["uname"] = USER["username"]
        CTX_D["avatar"] = USER["avatar"]
        CTX_D["dscm"] = USER["discriminator"]
        CTX_D["banner"] = USER["banner"]

        binary = bin(int(ID))[2:]
        zzin = binary.zfill(64)
        excerpt = zzin[:42]
        unix = int(str(excerpt), 2) + 1420070400000

        CT_DATE = datetime.datetime.fromtimestamp(unix/1000).replace(microsecond=0).strftime("%Y %m/%d %H:%M:%S")
        CTX_D["ct_date"] = CT_DATE
    
        return CTX_D

def setup():
    DEV = USERDICT()
    AVATAR = DEV.avatar
    
    with open("static/images/favicon.jpg", "wb") as fvi:
        fvi.write(urlopen(Request(f"https://cdn.discordapp.com/avatars/441865412804870144/{AVATAR}.jpg", headers=headers)).read())
        fvi.close()
    
    favicon = Image.open("static/images/favicon.jpg")
    favicon.save("static/favicon.ico")

@app.route("/")
def index():
    DEVELOPER = USERDICT()
    
    return render_template("index.html", message=DEVELOPER)

@app.route("/manage")
def manage():
    return render_template("LoginMethod.html")

@app.route("/userlookup/<int:user_id>")
def userlookup(user_id=0):
    if user_id == 0:
        return render_template("search.html")
    else:
        message = USERDICT(user_id)
            
        return render_template("DiscordUserLookUp.html", message=message)

def run():
    app.run(host="0.0.0.0", port="8000")

def Qvey():
    setup()
    
    thread = Thread(target=run)
    thread.start()
