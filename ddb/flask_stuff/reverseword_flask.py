#default Flask port is 5000

from flask import Flask, request
app = Flask(__name__)


#routing function
#this application only has one path

@app.route("/reverse")
def reverser():
    word = request.args.get('word', None) #evalates to whatever the value is for the key word
    if word:
        word_in_reverse = ''.join(reversed(word))
        return word_in_reverse
    else:
        return "you did not use the API correctly. happens to us all."

# can test with: http://localhost:5000/reverse?word=mammoth
# which should return mammoth reversed
# mammoth can be replaced with any word

app.run()
