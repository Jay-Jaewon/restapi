from flask import Flask
from flask_restx import Api, Resource
from flask import jsonify

app = Flask(__name__)
api = Api(app)
app.config['JSON_AS_ASCII'] = False

@api.route('/myinfo')
class HelloWorld(Resource):
    def get(self):
        return jsonify({"이름" :"송재원","학번": "201812617"})


if __name__ == "__main__":
    app.run(host='127.0.0.1', port = 5000, debug = True)