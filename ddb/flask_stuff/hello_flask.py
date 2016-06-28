#default Flask port is 5000

from flask import Flask
app = Flask(__name__)

#routing function
@app.route("/hello")
#this function returns a string "Hello, world!"
def hello():
    return "Hello, world!"

@app.route("/blah")
def fun_response_yay():
    return "You went to /blah congratulations."

@app.route("/")
def index_resource():
    return "Welcome to Example Server. Welcome."

app.run()
