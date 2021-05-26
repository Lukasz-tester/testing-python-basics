import os  # import operating system library from python that let's us access e.g. environment variables

from flask import Flask
from flask_restful import Api  # import flask extension

from resources.item import Item  # import Item from resources folder

app = Flask(__name__)  # create our app

# set configurations
app.config['DEBUG'] = True  # we can use it while testing for a few things

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
# get an environment variable that sets in my computer, it should be 'DATABASE_URL'
# the value of 'DATABASE_URL' is going to be assigned to 'SQLALCHEMY_DATABASE_URI'
# what 'get' does: if 'DATABASE_URL' environment variable is not set, it will use 'sqlite:///data.db' default value

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)  # create api - part of flask extension

api.add_resource(Item, '/item/<string:name>')  # add Item resource to the api
# we specify what the structure ot the endpoints is:
# we access a particular item in our api through "/item/the-item-name"

if __name__ == '__main__':  # when executing this file
    from db import db  # import the database connector

    db.init_app(app)  # initialise it with flask app

    if app.config['DEBUG']:  # if we are in debug mode
        @app.before_first_request  # we're gonna create tables only before the first request to the app
        def create_tables():
            db.create_all()  # create all the tables

    app.run(port=5000)  # run the app
