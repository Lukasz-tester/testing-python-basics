from app import app
from db import db

db.init_app(app)  # it creates the app so that you can run it from deployment service


@app.before_first_request
def create_tables():
    db.create_all()
