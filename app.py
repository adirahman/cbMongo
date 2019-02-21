from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import json_util


app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/test")
userdb = mongo.db.users
roledb = mongo.db.roles

@app.route('/users', methods=["POST"])
def add():
    email = request.json["email"]
    name = request.json["name"]
    user = userdb.insert({'name': name, 'email': email})
    return json_util.dumps(user)


@app.route('/users', methods=["GET"])
def get():
    users = userdb.find()
    return json_util.dumps(users)


@app.route('/users/<email>', methods=["DELETE"])
def delete(email):
    try:
        user = userdb.delete_one({'email': email})
        if (user.deleted_count >= 1):
            return ('', 204)
        else:
            raise Exception("User not found")
    except:
        return (json_util.dumps({'message': 'User not found'}), 404)

## ROLE MANAGEMENT

@app.route("/role", methods=['POST'])
def addRole():
    roleId = request.json["roleId"]
    name = request.json["name"]
    inventory = request.json["inventory"]
    membership = request.json["membership"]
    promotion = request.json["promotion"]
    createdAt = request.json["createdAt"]
    updateAt = request.json["updateAt"]
    role = roledb.insert({'roleId': roleId, 'name': name, 'inventory': inventory, 'membership': membership, 'promotion': promotion, 'createdAt': createdAt, 'updateAt': updateAt})
    return json_util.dumps(role)

@app.route('/roles',methods=["GET"])
def getRole():
    roles = roledb.find()
    return json_util.dumps(roles)

@app.route('/role/<roleId>', methods=["DELETE"])
def deleteRole(roleId):
    try:
        role = roledb.delete_one({'roleId': roleId})
        if(role.deleted_count >= 1):
            return ('',204)
        else:
            raise Exception("Role not found")
    except:
        return (json_util.dumps({'message':'User not found'}), 404)



if __name__ == '__main__':
    app.run(debug=True)