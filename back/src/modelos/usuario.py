from bson.objectid import ObjectId
from flask import Blueprint, request
from werkzeug.wrappers import Response
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from flask_cors import  CORS


from configuracion import mongo

usuario = Blueprint('usuario', __name__)

CORS(usuario)

@usuario.route('/usuario')
def obtenerUsuario():
    usuarios = mongo.db.usuario.find()        
    respuesta = json_util.dumps(usuarios)
    return Response(respuesta, mimetype='application/json')

@usuario.route('/usuario/<nombre>')
def obtenerUsuarioPorId(nombre):
    usuario = mongo.db.usuario.find_one({'nombre': nombre})
    respuesta = json_util.dumps(usuario)
    return Response(respuesta, mimetype='application/json')

@usuario.route('/usuario', methods=['POST'])
def crearUsuario():
    nombre = request.json['nombre']
    password = request.json['password']
    
    if nombre and password:
        passwordCifrado = generate_password_hash(password)
        id = mongo.db.usuario.insert({
            'nombre': nombre,
            'password': passwordCifrado
        })
        
        respuesta = {
            'id': str(id),
            'nombre': nombre,
            'password': password
        }
        
        return respuesta
    
