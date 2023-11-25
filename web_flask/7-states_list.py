#!/usr/bin/python3
"""Start a Flask web application"""

from models import storage
from models.city import City
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    """Terminate the existing session in SQLAlchemy"""
    storage.close()


@app.route('/cities_by_states')
def cities_by_state():
    """Show an HTML page containing a list of all State objects in DBStorage,
    with the states sorted alphabetically by name."""
    states = storage.all(State).values()
    newStates = sorted(states, key=lambda s: s.name)
    return render_template('8-cities_by_states.html', states=newStates)


if __name__ == "__main__":
    storage.reload()
    app.run(host='0.0.0.0', port=5000)
