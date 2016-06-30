from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def display_form():
    return render_template("simplify_home.html")

# this invokes the post method which is used in the form
@app.route('/transformed', methods=["POST"])
def transformed():
    # this allows you get get parameters from the form
    text = request.form['text']
    words = [w for w in text.split() if len(w) <= 5]
    return render_template("simplify_transformed.html", output=' '.join(words))

app.run()
