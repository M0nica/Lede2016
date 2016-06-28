#default Flask port is 5000

from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello, world!"

app.run()
