import pandas as pd
import numpy as np
# note - I changed the relative path
df = pd.read_csv("sizer-backend/data/shoe_data.csv")
df.columns = ['shoe_name', 'brand', 'size_shift', 'price', 'width_fitting','picture']

df2 = pd.read_csv("sizer-backend/data/shoe_conversion.csv")
# print(df2)

test_data = {
    "Nicolas": {
        "username": "Nicolas",
        "length": 26.2,
        "width": 9.4,
        "gender": 'M',
        "like_bigger_fitting_shoes": True,
        "like_smaller_fitting_shoes": False,
        "min_price": 80,
        "max_price": 150
    },

    "Sean": {
        "username": "Sean",
        "length": 26.5,
        "width": 9.7,
        "gender": 'M',
        "like_bigger_fitting_shoes": False,
        "like_smaller_fitting_shoes": True,
        "min_price": 140,
        "max_price": 200
    },

    "Shivam": {
        "username": "Shivam",
        "length": 26.5,
        "width": 9.7,
        "gender": 'M',
        "like_bigger_fitting_shoes": False,
        "like_smaller_fitting_shoes": False,
        "min_price": 50,
        "max_price": 90
    },

    "Joseph": {
        "username": "Joseph",
        "length": 26.5,
        "width": 9.7,
        "gender": 'M',
        "like_bigger_fitting_shoes": True,
        "like_smaller_fitting_shoes": False,
        "min_price": 100,
        "max_price": 135
    },

    "Oscar": {
        "username": "Oscar",
        "length": 25.5,
        "width": 10,
        "gender": 'M',
        "like_bigger_fitting_shoes": False,
        "like_smaller_fitting_shoes": False,
        "min_price": 60,
        "max_price": 120
    },
    "Andrew": {
        "username": "Andrew",
        "length": 26,
        "width": 10,
        "gender": 'M',
        "like_bigger_fitting_shoes": True,
        "like_smaller_fitting_shoes": False,
        "min_price": 100,
        "max_price": 200
    },
    "Nancy": {
        "username": "Nancy",
        "length": 24,
        "width": 8,
        "gender": 'F',
        "like_bigger_fitting_shoes": False,
        "like_smaller_fitting_shoes": False,
        "min_price": 100,
        "max_price": 200
    },
}

def generate_recommendcations(username):
    # test data is passed in as a dictionary
    user_data = test_data[username]
    shoe_length = user_data["length"]
    shoe_width = user_data["width"]

    # note: the size in cm matches exactly with the shoe size; do not apply any adjustement
    # adjust the length based on user's fit preferences
    if user_data["like_bigger_fitting_shoes"]:
        # increment based on half a size on the size chart
        shoe_length += 0.5
        shoe_width += 0.2
    elif user_data["like_smaller_fitting_shoes"]:
        # decrement based on half a size on the size chart
        shoe_length -= 0.5
        shoe_length -= 0.2

    # find the length to width ratio of the foot
    foot_ratio = shoe_length/shoe_width

    # based on calculated factors, determine the recommended widths
    # this is for narrow feet
    if foot_ratio >= 2.73:
        widths = ['xn', 'n']
    # this is for regular feet; most shoes in our data set are n or r
    elif foot_ratio >= 2.62:
        widths = ['n', 'r']
    # final one is for wide feet
    else:
        widths = ['r', 'w']
    
    # get the normalized shoe size of the user according to the length
    all_lengths = df2["CM"]

    normalized_length = normalize_length(all_lengths, shoe_length)

    # find the corresponding size
    index = all_lengths[all_lengths == normalized_length].index[0]
    if user_data["gender"] == "M":
        normalized_size = df2["US Men"][index]
    else:
        normalized_size = df2["US Women"][index]

    # get all shoes which correspond with acceptable width
    index_acceptable_width = np.where( ((df["width_fitting"] == widths[0]) | (df["width_fitting"] == widths[1])) & (df["price"] < user_data["max_price"]) & (df["price"] > user_data["min_price"]) )[0]
    accpetable_width_shoes = df.iloc[index_acceptable_width]
    accpetable_width_shoes["adjusted_size"] = accpetable_width_shoes["size_shift"] + normalized_size
    accpetable_width_shoes.drop(columns = ["size_shift"], inplace=True)
    print(accpetable_width_shoes)



def normalize_length(all_lengths, shoe_length): 
    # loop through the all_lengths series and find the correct normalized length
    for i, length in all_lengths.items():
        if i == 0 and length > shoe_length:
            return length
        elif i+1 == len(all_lengths):
            return length
        elif length > shoe_length:
            prev_length  = all_lengths[i-1]
            # check if the previous length is closer than the current length
            if (shoe_length - prev_length) < (length - shoe_length):
                return prev_length
            # if not, it must be closer to the current length being checked
            return length

# print("NICK'S RECCOMENDATIONS")
# generate_recommendcations("Nicolas")
# print("OSCAR'S RECOMMENDATIONS")
# generate_recommendcations("Oscar")
# print("ANDREW'S RECOMMENDATIONS")
# generate_recommendcations("Andrew")
# print(df2)
print("Nancy's recommendations")
generate_recommendcations("Nancy")

# run tests for normalize_length function: all passed

# all_lengths = df2["CM"]
# normal_len1 = normalize_length(all_lengths, 26.3)
# normal_len2 = normalize_length(all_lengths, 21)
# normal_len3 = normalize_length(all_lengths, 37)
# normal_len4 = normalize_length(all_lengths, 30)
# normal_len5 = normalize_length(all_lengths, 26.8)
# assert(normal_len1 == 26.416)
# assert(normal_len2 == 22.098)
# assert(normal_len3 == 35.560)
# assert(normal_len4 == 30.226)
# assert(normal_len5 == 26.670)
