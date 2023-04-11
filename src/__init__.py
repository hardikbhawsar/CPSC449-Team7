from http.client import INTERNAL_SERVER_ERROR
from flask import Flask, jsonify
import os
from src.user import user
from src.database import db
from flask_jwt_extended import JWTManager

#function to initialize flask application
def create_app(test_config=None):
    #Create instance of flask
    app = Flask(__name__,instance_relative_config=True,template_folder='template')

#Extracting values of these parameter from .flaskenv
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
            JWT_SECRET_KEY=os.environ.get("JWT_SECRET_KEY"),
            UPLOAD_FOLDER=os.environ.get("UPLOAD_FOLDER"),
            MAX_CONTENT_LENGTH=os.environ.get("MAX_CONTENT_LENGTH"),
        ) 

    else:
        app.config.from_mapping(test_config)
#Initialize the database
    db.app = app
    db.init_app(app)

#JWT configured
    JWTManager(app)
#Registeing the blueprint of User
    app.register_blueprint(user)
    app.register_error_handler(500, INTERNAL_SERVER_ERROR)
    return app
