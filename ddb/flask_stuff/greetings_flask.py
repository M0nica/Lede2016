#default Flask port is 5000

from flask import Flask, request
app = Flask(__name__)


greets =  ["hello","hi","salutations","howdy","sup","hey"]
punc = ["!", "!!", "?", ".", "..."]

@app.route("/greeting")
def greet_generator():
    thing = request.args['to_greet']
    #generates a random greeting from the array of greetings
    greeting = random.choice(greets) +  " " + thing + random.choice(punc)
    # you can return HTML, .json and more from a web API
    return "<h1>Welcome to Greet-O-Tron</h1>" + "<b>" + greeting + "</b>"

app.run()
