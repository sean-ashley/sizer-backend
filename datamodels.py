from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import cockroachdb
import psycopg2

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "cockroachdb://sean:sizristhebest@dopey-bison-8cc.gcp-northamerica-northeast1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&sslrootcert=dopey-bison-ca.crt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
#create shoe model

class Shoe(db.Model):
    """
    SQL table modeling attributes about a shoe
    """
    __tablename__ = "shoe"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    brand = db.Column(db.String(100))
    price = db.Column(db.Float)
    size_shift = db.Column(db.Float)
    #amount of inches of length per shoe size
    inches_per_size = db.Column(db.Float)
    #n for narrow , w for wide , r for regular , xn for extra narrow, xw for extra wide
    width_fitting = db.Column(db.String(2))
    picture = db.Column(db.String(100))


    def __init__(self, name, brand, price, size_shift, inches_per_size, width_fitting, picture):
        self.name = name
        self.brand = brand
        self.price = price
        self.size_shift = size_shift
        self.inches_per_size = inches_per_size
        self.width_fitting = width_fitting
        self.picture = picture
        
   



#create user data model
class Users(db.Model):
    """
    SQL table modeling attributes about a user
    """

    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    #email = db.db.Column(db.db.String(30))
    #password = db.db.Column(db.db.String(30))
    length = db.Column(db.Float)
    width = db.Column(db.Float)
    #m for male , f for female, n for non-binary
    gender = db.Column(db.String(1))

    like_bigger_fitting_shoes = db.Column(db.Boolean)
    like_smaller_fitting_shoes = db.Column(db.Boolean)
    min_price = db.Column(db.Float)
    max_price = db.Column(db.Float)

    def __init__(self, username, length, width, gender, like_bigger_fitting_shoes, like_smaller_fitting_shoes, min_price, max_price):
        self.username = username
        self.length = length
        self.width = width
        self.gender = gender
        self.like_bigger_fitting_shoes = like_bigger_fitting_shoes
        self.like_smaller_fitting_shoes = like_smaller_fitting_shoes
        self.min_price = min_price
        self.max_price = max_price
     





#create schemas to easily return json data
class ShoeSchema(ma.Schema):
  class Meta:
    fields = ("id", "name", "brand", "price", "size_shift", "inches_per_size", "width_fitting")

class UsersSchema(ma.Schema):
  class Meta:
    fields = ("id", "username", "length", "width", "gender", "like_bigger_fitting_shoes", "like_smaller_fitting_shoes", "min_price", "max_price")

shoe_schema = ShoeSchema()
shoes_schema = ShoeSchema(many=True)

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)