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
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM categorias"
        cursor.execute(query)
        rows = cursor.fetchall()  # Me devuelve un lista de tuplas
        categorias = [
            Categoria(
                id_categoria=row[0], nombre=row[1], descripcion=row[2], activo=row[3]
            )
            for row in rows
        ]
        cursor.close()
        return categorias

    # Obtener una categoria por su id
    @staticmethod
    def get_by_id(id_categoria):
        db = get_db()
        cursor = db.cursor()
        query = f"SELECT * FROM categorias WHERE id_categoria = {PH_PAR}"
        cursor.execute(query, (id_categoria,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Categoria(
                id_categoria=row[0], nombre=row[1], descripcion=row[2], activo=row[3]
            )
        return None

    # Insertar un registro si no existe el atributo id_categoria, de lo contrario actualizar
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_categoria:
            query = f"UPDATE categorias SET nombre = {PH_PAR}, descripcion = {PH_PAR}, activo = {PH_PAR} WHERE id_categoria = {PH_PAR}"
            cursor.execute(
                query, (self.nombre, self.descripcion, self.activo, self.id_categoria)
            )
        else:
            query = f"INSERT INTO categorias (nombre, descripcion, activo) VALUES ({PH_PAR}, {PH_PAR}, {PH_PAR})"
            cursor.execute(query, (self.nombre, self.descripcion, self.activo))
            self.id_categoria = cursor.lastrowid
        db.commit()
        cursor.close()

    # Eliminar una categoria por su id
    def delete(self):
        db = get_db()
        cursor = db.cursor()
        query = f"DELETE FROM categorias WHERE id_categoria = {PH_PAR}"
        cursor.execute(query, (self.id_categoria,))
        db.commit()
        cursor.close()
