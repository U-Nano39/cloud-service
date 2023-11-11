import os

from PIL import Image

from urllib.request import Request, urlopen
from flask import Flask, render_template
from flask_socketio import SocketIO
from threading import Thread

app = Flask(__name__)

#favicon.ico
def DevInfo(DJD):
    BotKey = os.getenv("DISCORD_BOT_TOKEN")
    headers = {
            "Content-Type": "application/json",
            "User-Agent": "Discord V9API Bot Python-urllib/3.9",
            "Authorization": BotKey
            }
    
    ID = DJD["id"]
    UNAME = DJD["username"]
    AVATAR = DJD["avatar"]
    DSCM = DJD["discriminator"]
    BANNER = DJD["banner"]
    
    with open("static/images/favicon.jpg", "wb") as fvi:
        fvi.write(urlopen(Request(f"https://cdn.discordapp.com/avatars/441865412804870144/{AVATAR}.jpg", headers=headers)).read())
        fvi.close()
    
    favicon = Image.open("static/images/favicon.jpg")
    favicon.save("static/favicon.ico")

@app.route("/")
def index(test):
    #CTX = DevInfo()
    
    #ID = CTX["id"]
    #UNAME = CTX["username"]
    #AVATAR = CTX["avatar"]
    #DSCM = CTX["discriminator"]
    #BANNER = CTX["banner"]
    
    message = test #UNAME+"#"+DSCM
    
    return render_template("index.html", message=message)

@app.route("/manage")
def manage():
    return render_template("LoginMethod.html")

def run():
    app.run(host="0.0.0.0", port="8000")

def Elphelt(DD):
    DevInfo(DD)
    index("hello")
    
    thread = Thread(target=run)
    thread.start()
