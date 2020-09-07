from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planes_database.db'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# For debugging purpouses
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret string that will be changed'
db = SQLAlchemy(app)