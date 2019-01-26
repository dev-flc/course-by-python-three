from flask import Flask 
import jwt
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

@app.route('/')

class EncToken(Resource):
    def get(self):
        """ Example """
        encoded = jwt.encode( { 'some' : 'payload' }, 'secret', algorithm = 'HS256' )
        return encoded, 202
    
class DecToken(Resource):
    def get(self):
        """ Example """
        encoded = jwt.encode( { 'some' : 'payload' }, 'secret', algorithm = 'HS256' )
        decode = jwt.decode( encoded, 'secret', algorithms=['HS256'])
        return decode, 202


if __name__ == '__main__':
    #help(hello_world)
    api.add_resource(EncToken,'/token-enc')
    api.add_resource(DecToken,'/token-dec')
    app.run(host='127.0.0.1', port=8081)