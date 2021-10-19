from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Efetivo(Resource):
    def get(self):
        return 'teste'


api.add_resource(Efetivo, '/dev')

if __name__ == '__main__':
    app.run(debug=True)