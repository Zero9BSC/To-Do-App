from flask import Blueprint, request, jsonify
from models import get_db_connection
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

task_routes = Blueprint('task_routes', __name__)

# Simulación de usuarios (sin base de datos por ahora)
users = {"admin": "admin123"}

@task_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    users[username] = password
    return jsonify(message="Usuario registrado"), 201

@task_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if users.get(data['username']) == data['password']:
        token = create_access_token(identity=data['username'])
        return jsonify(access_token=token), 200
    return jsonify(message="Credenciales inválidas"), 401

@task_routes.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    tasks = [{'id': row[0], 'description': row[1]} for row in rows]
    conn.close()
    return jsonify(tasks)

@task_routes.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description) VALUES (%s)", (data['description'],))
    conn.commit()
    conn.close()
    return jsonify(message="Tarea creada"), 201