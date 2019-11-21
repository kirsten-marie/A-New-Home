from flask import Flask, render__template
from flask_sqlalchemy import flask_sqlalchemy

app = Flask(__name__)

from newproj import routes

app.config['SQLALCHEMY_Database_URL'] = 'mysql://sqlservice:Flask3@localhost/ANewHome'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)