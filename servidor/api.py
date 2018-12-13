from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name" : "fer",
        "age"  : 23,
        "occupation" : "vendedor"
    },
    {
        "name" : "example",
        "age"  : 23,
        "occupation" : "vendedor"
    },
]

class User(Resource):

    def get(self, name):
        for user in users:
            if( name == user["name"]):
                return users, 200
        return "Unser  not found", 404


    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if ( name == user["name"]):
                return "User withname {} already exists".format(name), 404
        
        user = {
            "name" : name ,
            "age"  : args["age"],
            "occupation" : args["occupation"]
        }
        users.append(user)
        return user, 201


    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if ( name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        
        user = {
            "name" : name ,
            "age"  : args["age"],
            "occupation" : args["occupation"]
        }

        users.append(user)
        return user, 201


    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name ]
        return "{} is deleted.".format(name),200

    
api.add_resource(User, "/user/<string:name>")
app.run(debug=True)
    