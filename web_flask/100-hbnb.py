#!/usr/bin/python3
"""
Initiates a Flask web application.
Listens on 0.0.0.0 on port 5000.
Routes:
* /hbnb_filters: HTML page for HBnB filters.
"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
Shows the HTML page for HBnB filters.
    """
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    states = storage.all("State")
    return render_template("100-hbnb.html",
                           amenities=amenities,
                           places=places,
                           states=states)


@app.teardown_appcontext
def teardown(excpt=None):
    """Removes the existing SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
