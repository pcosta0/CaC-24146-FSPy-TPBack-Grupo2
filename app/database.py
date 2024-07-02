import os
import mysql.connector
import sqlite3
from flask import g
from dotenv import load_dotenv

# Determina si se usa una base de datos local SQLite (True) o remota MySQL (False)
# DB_LOCAL = False
DB_LOCAL = True

# Determina el placeholder de los parámetros para SQLite (?) o MySQL (%.)
PH_PAR = "?" if DB_LOCAL else "%s"

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Define los parámetros de configuracion para conectarse a MySQL
DATABASE_CONFIG = {
    "user": os.getenv("DB_USERNAME"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "port": os.getenv("DB_PORT", 3306),
}

# Inicializa la bd local SQLite
def init_db_local():
    # crea una conexion a la bd, si no existe se crea automaticamente
    conn = sqlite3.connect("datos.db")
    # crea un cursor en la coneccion
    c = conn.cursor()
    # crea la tabla categorias
    c.execute(
        """CREATE TABLE IF NOT EXISTS categorias
                 (id_categoria INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, descripcion TEXT, activo BOOLEAN)"""
    )
    conn.commit()  # confirma los cambios de la transaccion sql
    conn.close()  # cierra la conexión


# Función para obtener la conexión a la base de datos
def get_db():
    # Si 'db' no está en el contexto global de Flask 'g'
    if "db" not in g:
        # Crear una nueva conexión a la base de datos y guardarla en 'g'
        if DB_LOCAL: # local o remota?
            init_db_local() # inicializa la bd sqlite
            g.db = sqlite3.connect("datos.db")
        else:
            g.db = mysql.connector.connect(**DATABASE_CONFIG)
    return g.db # Retornar la conexión a la base de datos


# Función para cerrar la conexión a la base de datos
def close_db(e=None):
    # Extraer la conexión a la base de datos de 'g' y eliminarla
    db = g.pop("db", None)
    # Si la conexión existe, cerrarla
    if db is not None:
        db.close()


# Función para inicializar la aplicación con el manejo de la base de datos
def init_app(app):
    # Registrar 'close_db' para que se ejecute al final del contexto de la aplicación
    app.teardown_appcontext(close_db)
