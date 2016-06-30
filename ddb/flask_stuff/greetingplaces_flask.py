import random
# remember to import render_template in order to import templates
from flask import Flask, request, render_template
app = Flask(__name__)

greets =  ["hello","hi","salutations","howdy","sup","hey"]
places = ["region", "continent", "world", " solar system", "galaxy" , "local cluster", "universe"]

@app.route("/greeting")

def greet_generator():
    x =  random.choice(greets)
    y =  random.choice(places)
    greeting = random.choice(greets) + " " + random.choice(places)
    return render_template("greeting.html", greet=x, place=y)

app.run()
