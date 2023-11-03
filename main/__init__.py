import os
from flask import Flask
from dotenv import load_dotenv


#importar modulo necesario para crear la apí rest
from flask_restful import Api

#importo modulo necesario para conectarme con la base de datos
from flask_sqlalchemy import SQLAlchemy

api = Api()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    #se cargan las variables de entorno
    load_dotenv()

    db_location = os.getenv("DATA_BASE_LOCATION")
    db_name = os.getenv("DATA_BASE_LOCATION")

    if not os.path.exists(f'{db_location}{db_name}'):
        os.chdir(f'{db_location}')
        file = os.open(f'{db_name}  ', os.O_CREAT)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_location}{db_name}'
    db.init_app(app)

    import main.resource as resources
    api.add_resource(resources.Resoureclientes, '/clientes')
    api.add_resource(resources.Resourecliente, '/cliente/<id>')

    api.init_app(app)

    return app