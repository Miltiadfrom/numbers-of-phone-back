from flask import Flask, json, Response, request
from app.helpers import find_users, find_phones_by_sub, to_add_phone_by_sub, to_delete_phone_by_name

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/users', methods=['GET'])
def get_users():
    result = find_users()
    json_string = json.dumps({"result": result}, ensure_ascii=False)
    response = Response(json_string, content_type="application/json; charset=utf-8")
    return response, 200

@app.route('/phones/<sub_id>', methods=['GET'])
def get_phones_by_sub_id(sub_id):
    result = find_phones_by_sub(sub_id)
    json_string = json.dumps({"result": result}, ensure_ascii=False)
    response = Response(json_string, content_type="application/json; charset=utf-8")
    return response, 200

@app.route('/phones', methods=['POST'])
def add_phone_by_sub_id():
    data = request.get_json()
    result = to_add_phone_by_sub(data)
    json_string = json.dumps({"result": result}, ensure_ascii=False)
    response = Response(json_string, content_type="application/json; charset=utf-8")
    return response, 200


@app.route('/phones/<phone_number>', methods=['DELETE'])
def delete_phone_by_name(phone_number):
    result = to_delete_phone_by_name(phone_number)
    json_string = json.dumps({"result": result}, ensure_ascii=False)
    response = Response(json_string, content_type="application/json; charset=utf-8")
    return response, 200
