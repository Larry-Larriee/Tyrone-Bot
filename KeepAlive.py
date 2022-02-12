#This makes sure that our bot does not enter the AFK sleep stage & will run even if Replit is closed.

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "I'm staying awake."

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
