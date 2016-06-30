## Country information server
#   curl http://localhost:5000/countries?lookup_name=France
#   Returns the population of country
#   France, Paris, 64933400

from flask import Flask, request, render_template
import pg8000

app = Flask(__name__)
conn = pg8000.connect(database="mondial", user="Monica")

@app.route("/countries")
def country_info():
    cname = request.args['lookup_name']
    cursor = conn.cursor()
    cursor.execute(
    "SELECT name, capital, population FROM country WHERE name = %s", [cname]
    )
    response = cursor.fetchone()

    cinfo = {
    'name' : response[0],
    'capital' : response[1],
    'population' : response[2]
    }
    #perform a database search
    # format the rresults as text (html)
    # return that text
    return render_template("country_lookup.html", country=cinfo)

app.run()
