Guía de Instalación y Configuración del Proyecto Full-Stack

Este documento describe los pasos necesarios para instalar y ejecutar el proyecto, que consta de un backend en Python (FastAPI/PostgreSQL) y un frontend en React (Vite).

1. Requisitos Previos

Asegúrate de tener instalados los siguientes programas en tu sistema:

Python: Versión 3.13 (o superior). Nota: Las instrucciones asumen comandos estándar de Python 3.

PostgreSQL: Servidor PostgreSQL v17 en funcionamiento.

Node.js: (Recomendado v20+).

Yarn: Versión v22.21.0 (o compatible). Utilizaremos comandos yarn modernos.

2. Configuración del Backend (Carpeta /back)

El backend utiliza Python y FastAPI, conectado a una base de datos PostgreSQL.

2.1. Entorno Virtual e Instalación de Dependencias

Navega a la carpeta del backend:

cd back

Crea y activa un entorno virtual (esto es crucial para aislar las dependencias):

# Crear entorno virtual

python3 -m venv venv

# Activar entorno virtual (Linux/macOS)

source venv/bin/activate

# Activar entorno virtual (Windows - PowerShell)

# .\venv\Scripts\Activate

Instala las dependencias de Python (FastAPI, SQLAlchemy, psycopg2-binary/asyncpg, etc.):

pip install -r requirements.txt

2.2. Configuración de la Base de Datos

Crear la Base de Datos:
Accede a tu consola de PostgreSQL y crea la base de datos necesaria (ajusta el nombre si es necesario). Por ejemplo con psql:

-- Desde la terminal (puedes usar psql interactivo o una herramienta GUI)
psql -U [TU_USUARIO] -c "CREATE DATABASE mi_app_db;"

o dentro de psql:

CREATE DATABASE mi_app_db;

Cargar Datos Iniciales y Estáticos (insert.sql):
Este paso es obligatorio. El archivo insert.sql se encuentra al mismo nivel que la carpeta /back y contiene:

La creación de la tabla tipo_documentos (necesaria para el formulario de venta).

La inserción de los tipos de documento básicos (CC, Pasaporte, etc.).

Un registro inicial en la tabla eventos para que puedas realizar pruebas de venta inmediatamente.

Carga el script SQL en tu base de datos (ejemplo con psql):

psql -U [TU_USUARIO] -d mi_app_db -f ../insert.sql

Si tu servidor no está en localhost o usa un puerto distinto, añade -h [HOST] -p [PUERTO].

Nota: Asegúrate de reemplazar [TU_USUARIO] con tu usuario de PostgreSQL.

Configuración del Archivo .env:
Crea un archivo llamado .env en la carpeta /back y rellena las variables de conexión a la base de datos:

# .env en /back

DATABASE_URL="postgresql+psycopg2://[USUARIO]:[PASSWORD]@[HOST]:[PUERTO]/mi_app_db"

# Ejemplo:

# DATABASE_URL="postgresql+psycopg2://postgres:mi_secreto@localhost:5432/mi_app_db"

# Otras configuraciones del servidor

SECRET_KEY="tu_clave_secreta"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

2.3. Ejecución del Servidor

Una vez configurado, inicia el servidor FastAPI. Asumiremos que estás usando uvicorn:

```bash
uvicorn main:app --reload
```

o

```bash
fastapi dev main.py
```

El backend estará funcionando en http://127.0.0.1:8000.

Acceso a la Documentación (Opcional):
Puedes ver la documentación interactiva (Swagger UI) de la API en tu navegador mientras el servidor esté en ejecución:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

3. Configuración del Frontend (Carpeta /front)

El frontend utiliza React con Vite y yarn para la gestión de paquetes.

3.1. Instalación de Dependencias

Navega a la carpeta del frontend:

cd ../front

Instala las dependencias usando Yarn:

yarn install

3.2. Configuración del Archivo .env

Crea un archivo llamado .env en la carpeta /front para especificar la URL del API del backend:

# .env en /front

VITE_API_URL=[http://127.0.0.1:8000](http://127.0.0.1:8000)

Esta variable será accesible dentro de tu código React a través de import.meta.env.VITE_API_URL.

3.3. Ejecución de la Aplicación

Inicia el servidor de desarrollo de Vite:

yarn dev

La aplicación del frontend se abrirá en tu navegador (típicamente en http://localhost:5173 o similar).
