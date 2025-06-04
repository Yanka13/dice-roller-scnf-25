from flask import Flask 
from flask import jsonify
import random 


app  = Flask(__name__)

# A simple route that simulates rolling a dice
@app.route('/dice')
def dice():
    return jsonify({"roll": random.randint(1, 6)})