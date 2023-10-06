from flask import Flask
from threading import Thread

app = Flask("")

@app.route("/")
def home():
    return "<h1>Working.</h1><br /><p>その他情報: 44Ki44Kr44Km44Oz44OI44Ot44Kw44Kk44Oz5pa55rOVIC0gUmVuZGVyOiBHaXRIdWIgLyBVcHRpbWVSb2JvdDogW0VtYWlsXSByaWtpMDQyNTBAZ21haWwuY29tIFtQYXNzd29yZF0gcmlraTA0MjU=</p>"

def run():
    app.run(host="0.0.0.0", port="8000")

def JustAlive():
    thread = Thread(target=run)
    thread.start()
