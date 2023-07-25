from flask import Flask
from flask import request

import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to the hello web service"

@app.route("/hello")
def helloanon():
   return "Hello anonymous user"

@app.route('/hello/<username>')
def helloname(username):
    if username == 'Jack' :
        return "HIT THE ROAD JACK!!!"
    else :
     return 'Hello {}'.format(username)

@app.route('/hello/<int:userid>')
def hellouserid(userid):	
    return 'Hello user unit number {:d}'.format(userid)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
