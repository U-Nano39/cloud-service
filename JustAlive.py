from flask import Flask, render_template
from threading import Thread

app = Flask("")

@app.route("/")
def index():
    return render_template("index.html")

def run():
    app.run(host="0.0.0.0", port="8000")

def JustAlive():
    thread = Thread(target=run)
    thread.start()
