import pandas as pd
from datamodels import app, db, ma, Shoe, Users
from database import connection
df = pd.read_csv("data/shoe_data.csv")
df.columns = ['shoe_name', 'brand', 'size_shift', 'price', 'width_fitting','picture']

def addshoes():
    """
    add in shoes from our local csv to the CockroachDB database
    """

    # iterate through shoes and add thenm to the database
    for i, record in df.iterrows():
        shoe = Shoe(record.shoe_name, record.brand, record.price, record.size_shift, None, record.width_fitting,record.picture)
        db.session.add(shoe)
        db.session.commit()

def get_db_shoes():
    """
    print out all the shoes in our db
    """
    # check that the shoes are stored in the database
    shoes = pd.read_sql_table("shoe", connection)
    print(shoes)

addshoes()
get_db_shoes()