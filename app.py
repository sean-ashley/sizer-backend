from flask import Flask, request, jsonify
from datamodel import app, db, ma, Shoe, Users, shoe_schema, shoes_schema, user_schema, users_schema


#ping the network to make sure its working
@app.route("/ping", methods =["GET"])
def ping():
    return jsonify("ping :)")

#add user to the database
@app.route("/adduser", methods = ["POST"])
def adduser():
    username = request.json['username']
    length = request.json['length']
    width = request.json['width']
    gender = request.json['gender']
    like_bigger_fitting_shoes = request.json['like_bigger_fitting_shoes']
    like_smaller_fitting_shoes = request.json['like_smaller_fitting_shoes']
    min_price = request.json['min_price']
    max_price = requset.json['max_price']

    new_user = Users(username, length, width, gender, like_bigger_fitting_shoes, like_smaller_fitting_shoes, min_price, max_price)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

#add shoe to the database
@app.route("/addshoe", methods = ["POST"])
def addshoe():
    name = request.json['name']
    brand = request.json['brand']
    price = request.json['price']
    size_shift = request.json['size_shift']
    inches_per_size = request.json['inches_per_size']
    name = request.json['width_fitting']


    new_shoe = Shoe(name, brand, price, size_shift, inches_per_size, width_fitting)

    db.session.add(new_shoe)
    db.session.commit()

    return user_schema.jsonify(new_shoe)



# Get All Users
@app.route('/users', methods=['GET'])
def get_products():
    """
    get all the products from the database in json form
    """

  
  all_users = Users.query.all()
  result = users_schema.dump(all_users)
  return jsonify(result)  


if __name__ == 'main':
    app.run(debug = True)