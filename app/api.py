
from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_jwt_claims, jwt_optional
)

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

class Auth(Resource):
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

        auth_token = create_access_token(identity=name)
        self.db.execute(queries.update_token(name,auth_token))
        return self.db.execute(queries.get_token(name))

    @jwt_required
    def get(self):
        """ 
            is authorized test 
            the header must contain Authorization: Bearer AUTH_TOKEN
        """
        return "access granted"


    def post(self):
        payload = request.get_json()
        name = payload['name']
        password = payload['password']
        if self.user_exists(name):
            if self.check_password(password):
                token = self.update_token(name)[0][0]
                
                return jsonify({"token": token})
                

        return "user or pass not correct"

class my_app:
    def __init__(self,config={}):
        self.app = Flask(__name__, static_folder="../static",
                    template_folder="./templates/")
        self.api = Api(self.app)
        self.jwt = JWTManager(self.app)
        self.app.config['JWT_SECRET_KEY'] = variables.JWT_SECRET
        db_filename = variables.db_filename
        self.db = DB(db_filename, queries.users_table)
