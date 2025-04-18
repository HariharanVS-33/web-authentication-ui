from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your-secret-key'

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'HariSQL@2025'
    app.config['MYSQL_DB'] = 'user_auth_project'

    mysql.init_app(app)

    return app
