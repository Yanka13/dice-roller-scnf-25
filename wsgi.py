from flask import Flask 
from flask import jsonify
import random 


app  = Flask(__name__)

@app.route('/dice')
def dice():
    return jsonify({"roll": random.randint(1, 6)})