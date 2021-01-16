from flask import Flask, request, jsonify
from datamodel import app, db, ma, Shoe, Users, shoe_schema, shoes_schema, users_schema, users_schema



@app.route("/ping", methods =["GET"])
def ping():
    return jsonify("ping :)")


@app.route("/adduser", methods = ["POST"])
def adduser():
    username = request.json['username']
    length = request.json['length']
    width = request.json['width']
    gender = request.json['gender']

    new_user = Users(username, length, width, gender)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

# Get All Users
@app.route('/users', methods=['GET'])
def get_products():
  
  all_users = Users.query.all()
  result = users_schema.dump(all_users)
  return jsonify(result)  


if __name__ == 'main':
    app.run(debug = True)

