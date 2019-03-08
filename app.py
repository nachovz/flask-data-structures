import os
from flask import Flask, jsonify, request

app = Flask(__name__)

person2 = {}

person1 = {}

family = {}


@app.route('/', methods=['GET'])
def hello():
  return 'family'
  
@app.route('/member/<int:id>')
def get_member(id):
  return 'member'
  

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))