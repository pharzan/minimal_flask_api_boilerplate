
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
    
    def user_exists(self,name):
        """ check if user exists """
        return len(self.db.execute(queries.get_user(name))) > 0

    def get(self, name):
        """ get user information """

        user_info = self.db.execute(queries.get_user(name))
        return user_info
    
    def post(self, name=None):
        """ create user """

        payload = request.get_json()
        name = payload['name']
        password = payload['password']
        if not self.user_exists(name):
            result = self.db.execute(queries.create_user(name,password))
            return "user created"

        return "user exits"

    def put(self, name=None):
        """ update user password """

        payload = request.get_json()
        name = payload['name']
        password = payload['password']

        if self.user_exists(name):
            result = self.db.execute(queries.update_user(name,password))
            return "user updated"
        return "user doesn't exist"

class Login(Resource):
    def __init__(self):
        my_app.__init__(self)

    def user_exists(self, name):
        """ check if user exists """
        return len(self.db.execute(queries.get_user(name))) > 0
    
    def check_password(self, password):
        """ check if password is correct """
        return len(self.db.execute(queries.check_password(password))) > 0

    def update_token(self, name):
        """ update users table with a random token """
        auth_token = "01234567890"
        self.db.execute(queries.update_token(name,auth_token))

    def post(self):
        payload = request.get_json()
        name = payload['name']
        password = payload['password']
        if self.user_exists(name):
            if self.check_password(password):
                self.update_token(name)
                return "logged in"

        return "user or pass not correct"

class my_app:
    def __init__(self,config={}):
        self.app = Flask(__name__, static_folder="../static",
                    template_folder="./templates/")
        self.api = Api(self.app)
        db_filename = variables.db_filename
        self.db = DB(db_filename, queries.users_table)
