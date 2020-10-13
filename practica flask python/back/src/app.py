from flask import  Flask, Blueprint, jsonify
from flask_cors import CORS

from modelos.usuario import usuario


app = Flask(__name__)
CORS(app)


@app.route('/')
def inicio():
    return jsonify({'mensaje': 'hola a todos'})

app.register_blueprint(usuario)

if __name__ == "__main__":
    app.run(debug=True)
