import pandas as pd
from datamodel import app, db, ma, Shoe, Users, shoe_schema, shoes_schema, user_schema, users_schema

df = pd.read_csv("sizer-backend/shoe_data.csv")
df.columns = ['shoe_name', 'brand', 'size_shift', 'price', 'width_fitting']
# print(df)

def addshoes():
    # iterate through shoes and add thenm to the database
    for i, record in df.iterrows():
        shoe = Shoe(record.shoe_name, record.brand, record.price, record.size_shift, None, record.width_fitting)
        db.session.add(shoe)
        db.session.commit()

def get_db_shoes():
    # check that the shoes are stored in the database
    shoes = Shoe.query.all()
    for shoe in shoes:
        print(shoe.name + " is in the db")
        

addshoes()
get_db_shoes()