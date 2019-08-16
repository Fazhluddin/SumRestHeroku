import sumfunction
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class sumNumbers(Resource):
    def get(self, first_number, second_number):
        return {'data': sumfunction.sumTwo(first_number,second_number)}

api.add_resource(sumNumbers, '/sum_twonumbers/<first_number>/<second_number>')

if __name__ == '__main__':
    app.run()