from flask import jsonify, request
from app.models import Categoria

# Hola mundo en raiz
def index():
    return '<h1>Hola mundo con flask 🐍</h1>'

# Obtener todas las categorias
def get_all_categorias():
    categorias = Categoria.get_all()
    list_categorias = [movie.serialize() for movie in categorias]
    return jsonify(list_categorias), 200

# Crear una categoria nueva
def create_categoria():
    # obtiene los datos del reques en formato json
    data = request.json
    # crea un objeto categoria con los datos recibidos
    new_categoria = Categoria(
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        activo=data['activo'],
    )
    # guarda la categoria creada
    new_categoria.save()
    # retorna un mensaje y un resultado 
    return jsonify({'message':'Categoria creada con exito'}), 201
    
# Actualiza una categoria
def update_categoria(categoria_id):
    # obtiene la categorias a modificar mediante su id
    categoria = Categoria.get_by_id(categoria_id)
    # si no se encuentra devuelve un mensaje y un código de error
    if not categoria:
        return jsonify({'message': 'Categoria no encontrada'}), 404
    # obtiene los datos de la categoria en formato json desde la peticion
    data = request.json
    # actualiza los campos de la categoria desde data
    categoria.nombre = data['nombre']
    categoria.descripcion = data['descripcion']
    categoria.activo = data['activo']
    # guarda los cambios
    categoria.save()
    # retorna un mensaje y un código de estado
    return jsonify({'message': 'Categoria actualizada exitosamente'})

# Obtiene una categoria pod su id
def get_categoria(categoria_id):
    # busca en la bd la categoria por su id
    categoria = Categoria.get_by_id(categoria_id)
    # si no se encuantra se retorna un mensaje y un código de error
    if not categoria:
        return jsonify({'message': 'categoria no encontrada'}), 404
    # si se encontró entonces se devuelve la categoria serializada y un código de estado ok
    return jsonify(categoria.serialize()), 200

# Elimina una categoria por su id
def delete_categoria(categoria_id):
    # obtiene la categorias desde la db mediante su id
    categoria = Categoria.get_by_id(categoria_id)
    # si no se encuantra se devuelve un mensaje y código de error
    if not categoria:
        return jsonify({'message': 'categoria no encontrada'}), 404
    # se elimina la categoria de la bd
    categoria.delete()
    # se devuelve un mensaje y un código ok
    return jsonify({'message': 'categoria eliminada exitosamente'}), 200
