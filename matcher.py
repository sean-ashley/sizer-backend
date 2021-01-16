
import pandas as pd
from datamodel import Shoe, Users,db
from read_data import load_users, load_shoe


def generate_recommenations(json_user):
    """
    read in sql query containing user, and generate a np array with their profile.
    """
    
    #get username out of json
    username = json_user["username"]
    #look up user in database
    query = Users.query.filter_by(username=username).first()
    #convert query to dict
    #(for reference)
    user_profile = {
    "username": query.username,
    "length": query.length,
    "width":query.width,
    "gender":query.gender,
    "like_bigger_fitting_shoes":query.like_bigger_fitting_shoes,
    "like_smaller_fitting_shoes":query.like_smaller_fitting_shoes,
    "min_price":query.min_price,
    "max_price":query.max_price
    }

    low_length_range = 

    #read in shoe data as a pd dataframe
    shoes = load_shoe()
    #load shoes that meet user critieria
    best_shoes = shoes[]



    






print(generate_profile("shivamsh"))

