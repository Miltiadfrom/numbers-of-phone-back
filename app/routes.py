from flask import Flask, json, Response, request
from app.helpers import (find_users,
                         find_phones_by_sub,
                         to_add_phone_by_sub,
                         to_delete_phone_by_name,
                         to_delete_subscriber,
                         to_add_new_subscriber,
                         find_user_by_id,
                         to_change_user_by_id,
                         to_add_new_payment,
                         find_payments_by_sub)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

def _response_func(data):
    json_string = json.dumps({"result": data}, ensure_ascii=False)
    response = Response(json_string, content_type="application/json; charset=utf-8")
    return response, 200

@app.route('/users', methods=['GET', "POST"])
def hook_users():
    if request.method == "GET":
        result = find_users()
    elif request.method == "POST":
        data = request.get_json()
        result = to_add_new_subscriber(data)
    return _response_func(result)

@app.route('/users/<sub_id>', methods=["GET", "DELETE", "PUT"])
def hook_user_by_id(sub_id):
    if request.method == "DELETE":
        result = to_delete_subscriber(sub_id)
    elif request.method == "GET":
        result = find_user_by_id(sub_id)
    elif request.method == "PUT":
        data = request.get_json()
        result = to_change_user_by_id(sub_id, data)

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


@app.route('/payments/<sub_id>', methods=["GET"])
def get_payments_by_sub_id(sub_id):
    result = find_payments_by_sub(sub_id)
    return _response_func(result)

@app.route('/payments', methods=["POST"])
def add_new_payment_by_sub_id():
    data = request.get_json()
    result = to_add_new_payment(data)
    return _response_func(result)