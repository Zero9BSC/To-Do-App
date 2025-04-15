from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

task_routes = Blueprint('task_routes', __name__)

@task_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    users[username] = password
    return jsonify(message="Usuario registrado")

@task_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if users.get(data['username']) == data['password']:
        token = create_access_token(identity=data['username'])
        return jsonify(access_token=token)
    return jsonify(message="Credenciales inválidas"), 401
