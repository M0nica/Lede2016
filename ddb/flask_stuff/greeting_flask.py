#default Flask port is 5000

from flask import Flask, request
app = Flask(__name__)


greets =  ["hello","hi","salutations","howdy","sup","hey"]

@app.route("/greeting")
def greet_generator():
    #generates a random greeting from the array of greetings
    greeting = random.choice(greets) + "!"
    return greeting

app.run()
