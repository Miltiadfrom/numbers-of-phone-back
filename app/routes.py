from flask import Flask, json, Response, request
from app.helpers import (find_users,
                         find_phones_by_sub,
                         to_add_phone_by_sub,
                         to_delete_phone_by_name,
                         to_delete_subscriber )

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

def _response_func(data):
    json_string = json.dumps({"result": data}, ensure_ascii=False)
    response = Response(json_string, content_type="application/json; charset=utf-8")
    return response, 200

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/users', methods=['GET'])
def get_users():
    result = find_users()
    return _response_func(result)

@app.route('/users/<sub_id>', methods=["DELETE"])
def delete_user_by_id(sub_id):
    result = to_delete_subscriber(sub_id)
    return _response_func(result)

@app.route('/phones/<sub_id>', methods=['GET'])
def get_phones_by_sub_id(sub_id):
    result = find_phones_by_sub(sub_id)
    return _response_func(result)

@app.route('/phones', methods=['POST'])
def add_phone_by_sub_id():
    data = request.get_json()
    result = to_add_phone_by_sub(data)
    return _response_func(result)


@app.route('/phones/<phone_number>', methods=['DELETE'])
def delete_phone_by_name(phone_number):
    result = to_delete_phone_by_name(phone_number)
    return _response_func(result)
