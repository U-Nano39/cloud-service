import os
import json
import base64
import datetime
import unicodedata

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
        
def SNOWFLAKE(ID):
    binary = bin(int(ID))[2:]
    zzin = binary.zfill(64)
    excerpt = zzin[:42]
    unix = int(str(excerpt), 2) + 1420070400000

    try:
        CT_DATE = datetime.datetime.fromtimestamp(unix/1000).replace(microsecond=0).strftime("%Y %m/%d %H:%M:%S")
    except:
        CT_DATE = None
        
    return CT_DATE

def USERDATA(USER_ID=None):
    if USER_ID is None:
        USER_ID = 441865412804870144
        
    try:
        JsonData = json.loads(urlopen(Request("https://discord.com/api/v9/users/"+str(USER_ID), headers=headers)).read().decode())
    except:
        JsonData = None
        
    return JsonData

USER = USERDATA()

def USERDICT(ID=None):
    if ID is None:
        USER = USERDATA()
        ID = USER["id"]

        CT_DATE = SNOWFLAKE(ID)
        USER["ct_date"] = CT_DATE
        
        return USER
    else:
        USER = USERDATA(ID)
        
        if USER is None:
            return None
        else:
            ID = USER["id"]

        CT_DATE = SNOWFLAKE(ID)
        USER["ct_date"] = CT_DATE
    
        return USER

def setup():
    DEV = USERDICT()
    ID = DEV["id"]
    IMAGE_URL = "https://cdn.discordapp.com/avatars/"
    AVATAR = DEV["avatar"]
    
    if AVATAR != "None":
        if AVATAR.startswith("a_"):
            AVATAR = AVATAR+".gif"
        else:
            AVATAR = AVATAR+".jpg"
    else:
        #https://discordapp.com/assets/
        AVATAR = "5ccabf62108d5a8074ddd95af2211727"+".png"
        ID = "assets"
        IMAGE_URL = "https://discordapp.com/"
    
    with open("static/images/favicon.jpg", "wb") as fvi:
        fvi.write(urlopen(Request(IMAGE_URL+ID+"/"+AVATAR, headers=headers)).read())
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

@app.route("/userlookup/<uid>")
def userlookup(uid="0"):
    if uid == "0" or uid == "０":
        return render_template("search.html")
    elif uid.isdecimal() is True:
        for digit in uid:
            if unicodedata.east_asian_width(digit) in "F":
                uid = unicodedata.normalize("NFKC", uid)
                    
        USER = USERDICT(uid)
        
        if bool(USER) == True:
        
            DSCM = USER["discriminator"]
            AVATAR = USER["avatar"]
            AVATAR_DECO = USER["avatar_decoration_data"]

            if DSCM == "0":
                DSCM = DSCM + f" ({USER['username']})"
        
            if AVATAR != "None":
                if AVATAR[:2] == "a_":
                    AVATAR = AVATAR+".gif"
                else:
                    AVATAR = AVATAR+".jpg"
            else:
                #https://discordapp.com/assets/
                AVATAR = "5ccabf62108d5a8074ddd95af2211727"+".png"
            
        else:
            USER = "Not Found User."
        
        return render_template("DiscordUserLookUp.html", message=USER)
    else:
        return render_template("NotFound.html", message="ユーザーが見つかりませんでした。")

def run():
    app.run(host="0.0.0.0", port="8000")

def Qvey():
    setup()
    
    thread = Thread(target=run)
    thread.start()
