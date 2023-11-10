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
    
    with open("static/images/favicon.jpg", "wb") as fvi:
        fvi.write(urlopen(f"https://cdn.discordapp.com/avatars/441865412804870144/{avatar}.jpg", header=header).read())
        fvi.close()
        
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
