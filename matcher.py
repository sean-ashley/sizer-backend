
import pandas as pd
from datamodel import Shoe, Users,db
from read_data import *
import numpy as np


def best_shoe_size(shoe_size_cm, dataframe, foot_size_cm, gender_size):

    series = dataframe[shoe_size_cm]

    #convert to numpy array
    arr = series.to_numpy()

    #subtract our size and take the absolute value

    sub_arr = abs(arr - foot_size_cm)

    #take the minimum index
    min_index = np.argmin(sub_arr)

    #retrieve what size that is associated with

    #get original length value back
    original_length = arr[min_index]

    #get row with best size
    best_size = dataframe[dataframe[shoe_size_cm] == original_length][gender_size]

    #extract value
    best_fit = best_size.item()

    return best_fit

def generate_recommendations(json_user):
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

    #create proper fit for shoe
    foot_size = query.length + 1.5

    if query.like_bigger_fitting_shoes:
        size_pref = 0.5
    elif query.like_smaller_fitting_shoes:
        size_pref = -0.5
    else:
        size_pref = 0

    #modify foot_size by size_pref
    foot_size += size_pref

    #read in shoe data as a pd dataframe
    shoes = load_shoe()
    #load shoes that meet user critieria
  
    best_shoes = shoes[(shoes['price'] <= query.max_price) & (shoes['price'] >= query.min_price)]


    #import length conversion chart
    shoe_conversions_df = shoe_conversions()

    gender_size = "US Men" if query.gender == 'm' else "US Women"

    #grab the best shoe size 
    best_size = best_shoe_size("CM", shoe_conversions_df, foot_size, gender_size)
    
    #add the sizes associated with each shoe
    best_shoes["US Size"] = best_shoes["size_shift"] + best_size

    print(best_shoes)

    #import width conversion chart
    #width_chart = mens_shoe_width() if query.gender == 'm' else womens_shoe_width()
    

    #get correct size row
    #width_row = width_chart[width_chart["US SIZE"] == best_size]
    #print(width_row)
    
    #drop all cols not in width range
    #drop_cols = lambda col : width_row.drop(columns = [col.name], inplace=True, axis = 1) if (low_width_range <= width_row.col <= high_width_range) else NoneType
    
    #width_row.apply(func = drop_cols)
    #return "hi"
    #finally recommend shoes later



print(generate_recommendations({"username":"shivamsh"}))















    







    








