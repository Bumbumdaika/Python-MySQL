from flask import Flask
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)
api= Api()

with open("logs1.json", "r") as file: 
            logs = file.readlines()

class Main(Resource):
    def get(self):
        return logs

api.add_resource(Main, "/api/main/")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")