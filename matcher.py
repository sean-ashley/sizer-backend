from database import connection
import pandas as pd
from datamodel import Shoe, Users
import numpy as np


def generate_profile(user):
    """
    read in JSON containing user preferences and foot size

        {
            username : string,
            width:float,
            length:float,
            gender:string,
            like_bigger_fitting_shoes: bool,
            like_smaller_fitting_shoes : bool,
            min_price : float,
            max_price : float
        }
    """
    
    #look up user in database
    






