from flask import Flask
from flask_cors import CORS
from app.views import *
from app.database import init_app

# Inicializacion del proyecto Flask
app = Flask(__name__)
init_app(app)

# Activacion de CORS para permitir operaciones desde otro dominio
CORS(app)

# Endpoint de saludo en raiz
app.route("/", methods=["GET"])(index)

# Definicion de endpoints para Categorias
app.route("/api/categorias/", methods=["GET"])(get_all_categorias)
app.route("/api/categorias/<int:categoria_id>", methods=["GET"])(get_categoria)
app.route("/api/categorias/", methods=["POST"])(create_categoria)
app.route("/api/categorias/<int:categoria_id>", methods=["PUT"])(update_categoria)
app.route("/api/categorias/<int:categoria_id>", methods=["DELETE"])(delete_categoria)

if __name__ == "__main__":
    app.run(debug=True)
