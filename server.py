from flask import Flask
from random import randint

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7527pa7qs9kCG78A/giphy.gif" width=200>'


@app.route('/<int:guess>')
def check_number(guess):
    if guess > random_number:
        return '<h1 style="color:blue">Too high</h1>' \
               '<img src="https://media.giphy.com/media/yoJC2COHSxjIqadyZW/giphy.gif" width=200>'
    elif guess < random_number:
        return '<h1 style="color:red">Too low</h1>' \
               '<img src="https://media.giphy.com/media/yoJC2COHSxjIqadyZW/giphy.gif" width=200>'
    else:
        return '<h1 style="color:green">good hehehhe</h1>' \
               '<img src="https://media.giphy.com/media/kiBcwEXegBTACmVOnE/giphy-downsized-large.gif" width=200>'


random_number = randint(0, 9)
if __name__ == "__main__":
    app.run(debug=True)
