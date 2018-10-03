
from flask import Flask, render_template, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from flask import jsonify

from db import DB
import variables
import queries


class User(Resource):
    def get(self, name):
        return "hello"
    



def create_app(config={}):
    app = Flask(__name__, static_folder="../static",
                template_folder="./templates/")
    api = Api(app)
    db_filename = variables.db_filename
    db = DB(db_filename, queries.users_table)
    return app,api

