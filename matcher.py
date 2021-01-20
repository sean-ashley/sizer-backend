
import pandas as pd
from datamodels import Shoe, Users,db
from read_data import *
import numpy as np
from json import loads

def add_width_measurment(shoes):

    """
    add an exact width measurement (in cm) to the shoes dataframe
    """
    # create the width conversion dictionary
    width_conversion = {  "xn": "D", "n": "D", "r": "D", "w": "EE", "xw": "EE" }

    width_df = pd.read_csv("data/shoe_width.csv")


    #map values
    shoes["width_fitting"] = shoes["width_fitting"].map(width_conversion)
    
    width_df.index = width_df["US Size"]
    width_df = width_df.drop(columns = ["US Size"])
    print(width_df)

    
    lst = []
    for width,size in zip(shoes["width_fitting"],shoes["US Size"]):
        val = width_df.loc[size][width]
        lst.append(val)

    shoes["width_measurement"] = lst 


    return shoes
 

def best_shoe_size(shoe_size_cm, dataframe, foot_size_cm, gender_size):
    """
    Find the shoe size that fits the users foot the best score
    """

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

def best_shoe_width(dataframe,foot_width):
    """
    find the shoe width that fits the users foot the best
    """
    
    series = dataframe["width_measurement"]

    #convert to numpy array
    arr = series.to_numpy()

    #subtract our size and take the absolute value

    sub_arr = abs(arr - foot_width)

    #take the minimum index
    min_index = np.argmin(sub_arr)

    #retrieve what size that is associated with

    #get original length value back
    original_width = arr[min_index]

    return original_width



def generate_recommendations(username):
    """
    read in sql query containing user, and generate a list of shoes to recommend them
    """
    
    #get username out of json
 
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

    #print(best_shoes)

    #add width_measurement to the df
    best_shoes = add_width_measurment(best_shoes)


    #filter for best width shoes
    best_width = best_shoe_width(best_shoes,query.width)

    best_shoes = best_shoes[best_shoes["width_measurement"] == best_width]

    best_shoes.drop(columns = ["id","inches_per_size","width_fitting","width_measurement"],inplace=True)
    best_shoes.reset_cindex(inplace = True)
    return best_shoes


        


















    







    








