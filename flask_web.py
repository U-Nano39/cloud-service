from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/manage")
def manage():
    return render_template("LoginMethod.html")

def run():
    app.run(host="0.0.0.0", port="8000")

def Elphelt():
    thread = Thread(target=run)
    thread.start()
