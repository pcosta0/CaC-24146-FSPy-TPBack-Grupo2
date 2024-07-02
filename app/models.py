# Importar funcion para obtener bd y "PlaceHolder _de PARametro"
from app.database import get_db, PH_PAR


class Categoria:

    # constuctor
    def __init__(self, id_categoria=None, nombre=None, descripcion=None, activo=None):
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.descripcion = descripcion
        self.activo = activo

    def serialize(self):
        return self.__dict__

    # Obtener todas las categorias
    @staticmethod
    def get_all():
        db = get_db() # obtiene una coneccion a la bd
        cursor = db.cursor() # obtiene un cursor
        # crea y ejecuta una consulta
        query = "SELECT * FROM categorias"
        cursor.execute(query)
        rows = cursor.fetchall()  # obtiene la lista de tuplas
        # crea una lista a partir de las tuplas
        categorias = [
            Categoria(
                id_categoria=row[0], nombre=row[1], descripcion=row[2], activo=row[3]
            )
            for row in rows
        ]
        cursor.close() # cierra el cursor
        return categorias # devuelve la lista

    # Obtener una categoria por su id
    @staticmethod
    def get_by_id(id_categoria):
        db = get_db() # obtiene una coneccion a la bd
        cursor = db.cursor() # obtiene un cursor
        # crea y ejecuta una consulta
        query = f"SELECT * FROM categorias WHERE id_categoria = {PH_PAR}"
        cursor.execute(query, (id_categoria,))
        # obtiene un solo elemento del resultado
        row = cursor.fetchone()
        cursor.close() #cierra el cursor
        if row: # hay un elemento de resultado? 
            # retorna ese elemento como una Categoria
            return Categoria(
                id_categoria=row[0], nombre=row[1], descripcion=row[2], activo=row[3]
            )
        return None

    # Insertar un registro si no existe el atributo id_categoria, de lo contrario actualizar
    def save(self):
        db = get_db() # obtiene una coneccion a la bd
        cursor = db.cursor() # obtiene un cursor
        # crea y ejecuta una consulta dependiendo de la existencia de id_categoria
        if self.id_categoria:
            query = f"UPDATE categorias SET nombre = {PH_PAR}, descripcion = {PH_PAR}, activo = {PH_PAR} WHERE id_categoria = {PH_PAR}"
            cursor.execute(
                query, (self.nombre, self.descripcion, self.activo, self.id_categoria)
            )
        else:
            query = f"INSERT INTO categorias (nombre, descripcion, activo) VALUES ({PH_PAR}, {PH_PAR}, {PH_PAR})"
            cursor.execute(query, (self.nombre, self.descripcion, self.activo))
            self.id_categoria = cursor.lastrowid
        db.commit() # al ser una modificacion o creación confirma los cambios
        cursor.close() # cierra el cursor

    # Eliminar una categoria por su id
    def delete(self):
        db = get_db() # obtiene una coneccion a la bd
        cursor = db.cursor() # obtiene un cursor
        # crea y ejecuta una consulta
        query = f"DELETE FROM categorias WHERE id_categoria = {PH_PAR}"
        cursor.execute(query, (self.id_categoria,))
        db.commit() # al ser una eliminacion confirma los cambios
        cursor.close() # cierra el cursor
