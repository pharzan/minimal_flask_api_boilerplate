
from flask import Flask, render_template, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from flask import jsonify

from db import DB
import variables
import queries


class User(Resource):
    def __init__(self):
        my_app.__init__(self)

    def get(self, name):
        """ get user information """
        user_info = self.db.execute(queries.get_user(name))
        return user_info
    
    def post(self, name=None):
        """ create user """
        payload = request.get_json()
        name = payload['name']
        password = payload['password']
        result = self.db.execute(queries.create_user(name,password))

        print(name,password,result)
        return ""

    def update(self, name):
        """ update user information """
        pass


class my_app:
    def __init__(self,config={}):
        self.app = Flask(__name__, static_folder="../static",
                    template_folder="./templates/")
        self.api = Api(self.app)
        db_filename = variables.db_filename
        self.db = DB(db_filename, queries.users_table)
        # return self.app,self.api

