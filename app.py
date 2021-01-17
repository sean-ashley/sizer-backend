from flask import Flask, request, jsonify
from datamodels import app, db, ma, Shoe, Users, shoe_schema, shoes_schema, user_schema, users_schema
from matcher import generate_recommendations

#ping the network to make sure its working
@app.route("/ping", methods =["GET"])
def ping():
    """
    quickly ping the server to make sure its working with
    """
    return jsonify("ping :)")

#add user to the database
@app.route("/adduser", methods = ["POST"])
def adduser():
    """
    add a user to our database
    """
    username = request.json['username']
    length = request.json['length']
#generate shoe recommendations
    width = request.json['width']
    gender = request.json['gender']
    like_bigger_fitting_shoes = request.json['like_bigger_fitting_shoes']
    like_smaller_fitting_shoes = request.json['like_smaller_fitting_shoes']
    min_price = request.json['min_price']
    max_price = request.json['max_price']

    new_user = Users(username, length, width, gender, like_bigger_fitting_shoes, like_smaller_fitting_shoes, min_price, max_price)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

#add shoe to the database
@app.route("/addshoe", methods = ["POST"])
def addshoe():
    """ 
    add a shoe to our database
    """
    #get requests from user
    name = request.json['name']
    brand = request.json['brand']
    price = request.json['price']
    size_shift = request.json['size_shift']
    inches_per_size = request.json['inches_per_size']
    name = request.json['width_fitting']

    #create data row
    new_shoe = Shoe(name, brand, price, size_shift, inches_per_size, width_fitting)

    #add that row to the database
    db.session.add(new_shoe)
    db.session.commit()

    #return the added shoe
    return shoe_schema.jsonify(new_shoe)



# Get All Users
@app.route('/users', methods=['GET'])
def get_products():
    """
    get all the products from the database in json form
    """

  
    all_users = Users.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)



#generate shoe recommendations
@app.route('/recommendshoes', methods = ['POST'])
def give_recommendations():
    """
    given a user, return all the shoes that fit them properly
    """

    username = request.json["username"]

    recommendation_df = generate_recommendations(username)




    return recommendation_df.to_json()




if __name__ == 'main':
    app.run(host="0.0.0.0", port=5000)

