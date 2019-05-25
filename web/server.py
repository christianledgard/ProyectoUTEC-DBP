from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)


@app.route('/')

def main():
    return render_template('index.html')

# - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - L O G I N - - - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - #

@app.route("/login", methods=['GET','POST'])

def login():
    return render_template('login.html')



@app.route("/inscripcion")

def inscripcion():
    return render_template('form1.html')





if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8020, threaded=True, host=('0.0.0.0'))
