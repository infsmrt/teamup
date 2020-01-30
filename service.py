import flask
from flask import request
from flask_cors import CORS

import team

app = flask.Flask(__name__)
CORS(app)

@app.route("/")
def find():
    return {
        'Names': team.find( int(request.args['branch']), int(request.args['position']) )
    }

app.run()