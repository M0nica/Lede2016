## Country information server
#   curl http://localhost:5000/countries?lookup_name=France
#   Returns the population of country
#   France, Paris, 64933400

# display info for all countries
# importing jsonify to transform python dictionaries into json
from flask import Flask, request, render_template, jsonify
import pg8000

app = Flask(__name__)
conn = pg8000.connect(database="mondial", user="Monica")

@app.route("/countries")
def get_countries():
    cursor = conn.cursor()
    # can set a population_gt to say how large the population may be .  
    pop_gt = int(request.args.get('population_gt', 0))
    cursor.execute(
        """SELECT name, capital, area, population
        FROM country
        WHERE population >= %s
        ORDER BY name""",
        [pop_gt])
    output = []
    for item in cursor.fetchall():
        output.append({'name': item[0],
                       'capital': item[1],
                       'area': int(item[2]),
                       'population': int(item[3])})
    # return all of the countries
    return jsonify(output)


app.run()
