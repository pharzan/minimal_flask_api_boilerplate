from flask import Flask, render_template, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from flask import jsonify

from db import DB
import variables, queries


app = Flask(__name__, static_folder="./static",
            template_folder="./templates/")
api = Api(app)


db_filename = variables.db_filename
db = DB(db_filename, queries.users_table)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
