## Country information server
#   curl http://localhost:5000/countries?lookup_name=France
#   Returns the population of country
#   France, Paris, 64933400

# importing jsonify to transform python dictionaries into json
from flask import Flask, request, render_template, jsonify
import pg8000

app = Flask(__name__)
conn = pg8000.connect(database="mondial", user="Monica")

@app.route("/countries")
def country_info():
    cinfo = None
    #default value for lookup_name is None
    cname = request.args.get('lookup_name', None)

    #perform database lookup if a country name is specified
    if cname:
        cursor = conn.cursor()
        cursor.execute(
        "SELECT name, capital, population FROM country WHERE name = %s", [cname]
        )
        response = cursor.fetchone()

        if response:
            cinfo = {
            'name' : response[0],
            'capital' : response[1],
            # converted to integer, because decimals cannot be converted into json
            'population' : int(response[2])
            }
    #perform a database search
    # format the rresults as text (html)
    # return that text
    return jsonify(cinfo)

app.run()
