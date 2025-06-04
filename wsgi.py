from flask import Flask 
from flask import jsonify


app  = Flask(__name__)

@app.route('/dice')
def hello():
    return jsonify({"roll": 0})