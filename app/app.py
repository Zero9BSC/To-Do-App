# To-Do App - RESTful API with Flask + MySQL + Docker
# Author: Franco Nicolás Jones
# Description: A simple task manager backend for demo/portfolio purposes

from flask import Flask
from routes import task_routes
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'supersecretkey'

jwt = JWTManager(app)

# Registrar rutas
app.register_blueprint(task_routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)