#!/usr/bin/python3
""" render template to return odd or even"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def function():
    """function"""
    return ("Hello HBNB!")


@app.route("/hbnb")
def function2():
    """function2"""
    return ("HBNB")


@app.route("/c/<text>")
def function3(text):
    """function2"""
    text = text.replace("_", " ")
    return ("C {}".format(text))


@app.route("/python")
@app.route("/python/<text>")
def function4(text):
    """function2"""
    if text is None:
        return ("Python is cool")
    text = text.replace("_", " ")
    return ("Python {}".format(text))


@app.route("/number/<int:n>")
def function_new(n):
    """function2"""
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>")
def function5(n):
    """function5"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def function6(n):
    """function6"""
    return render_template("6-number_odd_or_even.html", n=n)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """ def doc """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(error):
    """ def doc """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
