from flask import Flask
from threading import Thread

app = Flask("")

@app.route("/")
def home():
    return "Just Alive."

def run():
    app.run(host="0.0.0.0", port="8000")

def JustAlive():
    thread = Thread(target=run)
    thread.start()