import flask
from flask import request

import team

app = flask.Flask(__name__)

@app.route("/")
def find():
    return team.find( int(request.args['branch']), int(request.args['position']) )

app.run()