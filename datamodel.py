
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import cockroachdb
import psycopg2

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "cockroachdb://sean:2afSGARmYXSQkEJ@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/snappy-bear-200.defaultdb?sslmode=verify-full&sslrootcert=cc-ca.crt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
#create shoe model

class Shoe(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    brand = db.Column(db.String(100))
    price = db.Column(db.Float)
    size_shift = db.Column(db.Float)
    #amount of inches of length per shoe size
    inches_per_size = db.Column(db.Float)
    #n for narrow , w for wide , r for regular , xn for extra narrow, xw for extra wide
    width_fitting = db.Column(db.String(2))


    def __init__(self, name, brand, price, size_shift, inches_per_size, width_fitting):
        self.name = name
        self.brand = brand
        self.price = price
        self.size_shift = size_shift
        self.inches_per_size = inches_per_size
        self.width_fitting = width_fitting
   



#create user data model
class Users(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    #email = db.db.Column(db.db.String(30))
    #password = db.db.Column(db.db.String(30))
    length = db.Column(db.Float)
    width = db.Column(db.Float)
    #m for male , f for female, n for non-binary
    gender = db.Column(db.String(1))

    def __init__(self, username, length, width, gender):
        self.username = username
        self.length = length
        self.width = width
        self.gender = gender
     






class ShoeSchema(ma.Schema):
  class Meta:
    fields = ("id", "name", "brand", "price", "size_shift", "inches_per_size", "width_fitting")

class UsersSchema(ma.Schema):
  class Meta:
    fields = ("id", "username", "length", "width", "gender")

shoe_schema = ShoeSchema()
shoes_schema = ShoeSchema(many=True)

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)