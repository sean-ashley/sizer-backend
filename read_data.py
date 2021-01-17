import pandas as pd
from datamodel import Shoe, Users
from database import connection

def load_shoe():
    """
    load in shoe data from cloud as dataframe
    """
    # check that the shoes are stored in the database
    shoes = pd.read_sql_table("shoe", connection)
    return shoes


def load_users():
    """
    load in user data from cloud as dataframe
    """
    # check that the users are stored in the database
    users = pd.read_sql_table("users", connection)
    return users


def shoe_conversions():
    """
        
    load in nike data from csv as dataframe
    """

    return pd.read_csv("shoe_conversion.csv")


def mens_shoe_width():

    return pd.read_csv("shoe_width.csv")


def womens_shoe_width():

    return pd.read_csv("womens_shoe_width.csv")



    