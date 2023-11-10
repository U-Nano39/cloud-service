import os

from PIL import Image

from urllib.request import Request, urlopen
from flask import Flask, render_template
from flask_socketio import SocketIO
from threading import Thread

app = Flask(__name__)

#favicon.ico
def favicon(avatar):
    BotKey = os.getenv("DISCORD_USER_TOKEN")
    header = {
            "Content-Type": "application/json",
            "User-Agent": "Discord SelfBot Python-urllib/3.9",
            "Authorization": BotKey
            }

    opener = urllib.request.build_opener()
    opener.addheaders = [("Content-Type", "application/json")]
    opener.addheaders = [("User-Agent", "Discord SelfBot Python-urllib/3.9")]
    opener.addheaders = [("Authorization", BotKey)]

    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(f"https://cdn.discordapp.com/avatars/441865412804870144/{avatar}.jpg", "static/images/favicon.jpg")
    
    favicon = Image.open("static/images/favicon.jpg")
    favicon.save("static/favicon.ico")
    

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/manage")
def manage():
    return render_template("LoginMethod.html")

def run():
    app.run(host="0.0.0.0", port="8000")

def Elphelt(devdata):
    favicon(devdata)
    
    thread = Thread(target=run)
    thread.start()
