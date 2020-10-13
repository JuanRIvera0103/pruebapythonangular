from flask import Flask
from flask_pymongo import PyMongo



configuracion = Flask(__name__)
configuracion.config['MONGO_URI'] = 'mongodb://localhost/pythonangular'

mongo = PyMongo(configuracion)