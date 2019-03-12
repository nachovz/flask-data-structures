import os
from flask import Flask, jsonify, request

app = Flask(__name__)

person2 = {
  "id": 2,
  "name": "Jane",
  "lastname": "Doe",
  "age": 38,
  "gender": "female",
  "lucky_numbers": [ 2, 4, 6, 8]
}

person1 = {
  "id": 1,
  "name": "John",
  "lastname": "Doe",
  "age": 35,
  "gender": "male",
  "lucky_numbers": [ 7, 11, 13, 17]
}

family = {
  "lastname": "Doe",
  "members": [person1, person2]
}


@app.route('/', methods=['GET'])
def hello():
  lucky = []
  for m in family["members"]:
    lucky = lucky + m["lucky_numbers"]
  
  addAll = 0
  for l in lucky:
    addAll += l
  
  return jsonify({
    "code": 200,
    "data": {
      "title": "The "+family["lastname"]+" Family",
      "members": family["members"],
      "lucky_numbers": lucky,
      "sum_of_lucky": addAll
    }
  })
  
@app.route('/member/<int:id>')
def get_member(id):
  if id > 0:
    member = {}
    for m in family["members"]:
      if m["id"] == id:
        member = m
    
    if 'name' in member:
      return jsonify({"status_code": 200, "data": member})
    else:
      response = jsonify({"error": 400, "message":"no member found" })
      response.status_code = 400
      return response

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))