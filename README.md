# Codo a Codo 2024 - Curso Fullstack Python

Curso destinado a personas con experiencia previa en programación que aspiren a dominar uno de los lenguajes más demandados en el mercado. Durante el curso, se explorarán las mejores prácticas del diseño web adaptable, empleando HTML, CSS y Javascript. Además, se adquirirán competencias en el manejo de bases de datos y en el desarrollo de aplicaciones web sólidas, dinámicas y escalables. Al concluir el programa, se estará capacitado para desempeñarse como Desarrollador Full Stack en Python. El curso está dividido en dos estapas: Frontend y Backend.

## Proyecto Práctico: Fullstack Python (Backend)
En este proyecto práctico, se aplicarán los conocimientos adquiridos en desarrollo web para crear el backend de una plataforma de recetas de cocina utilizando Python y el framework Flask. Se trabajará en la implementación de una API RESTful que maneje las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) de las recetas. Además, se integrarán elementos dinámicos y de interacción en el frontend para mejorar la experiencia del usuario. Este trabajo permitirá demostrar habilidades en el desarrollo fullstack, combinando el backend en Python con el frontend para crear una aplicación web completa y funcional.

### Criterios de evaluación
- La base de datos debe desarrollarse en lenguaje SQL
- A través del front se debe poder realizar al menos un tipo de alta. (POST)
- De la misma forma se debe poder realizar modificaciones de los registros.
- Se debe poder acceder a los registros de la tabla (GET)
- Se debe poder realizar borrado físico de los datos. (DELETE)
- El trabajo práctico deberá subirse a un servidor online y compartirse mediante un repositorio de Git.
- La página deberá subirse a un servidor on-line para poder ser navegada por el Instructor.
- El backend debe estar integrado con un frontend

### Instrucciones
- Clonar el repositorio:  ```git clone https://github.com/pcosta0/CaC-24146-FSPy-TPBack-Grupo2.git```
- Crear y activar un entorno virtual
- Instalar librerias:  ```pip install -r requirements.txt```
- Iniciar servidor:  ```python run.py```

### Endpoints disponibles:
#### Raiz:  
- Saludo: ```/```, Método:```GET```

#### Categorias:
- Listar categorias:   ```/api/categorias/```, método ```GET```
- Listar una categoria especificando su id:   ```/api/categorias/<int:categoria_id>```, método:```GET```
- Crear una nueva categoria:    ```/api/categorias/```, método ```POST```, formato de datos en cuerpo de solicitud: ```JSON```

  Ejemplo:
```
{
  "nombre": "Nombre de categoria nueva",
  "descripcion": "Descripcion de categoria...",
  "activo": 1
}
```

- Modificar una categoria especificando su id:   ```/api/categorias/<int:categoria_id>```, método:```PUT```, formato de datos en cuerpo de solicitud: ```JSON```

  Ejemplo:
```
{
  "nombre": "Nombre modificado de categoria",
  "descripcion": "Descripcion modificada de categoria...",
  "activo": 0
}
```

- Eliminar una categoria especificando su id:   ```/api/categorias/<int:categoria_id>```, método:```DELETE```

### Integrantes
- Julio Cesar Garcia
- Lara Artaza
- Pablo Costa
- Diego Rodriguez Herlein
