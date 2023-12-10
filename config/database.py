import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Definición del nombre del archivo de la base de datos y el directorio base
sqlite_file_name = "../databasePedido.sqlite"

# Primero obtiene la ruta de este archivo y luego obtiene solo el nombre del directorio
base_dir = os.path.dirname(os.path.realpath(__file__))

# Creación de la URL de la base de datos utilizando SQLite en el directorio actual
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

# Creación del motor de la base de datos
engine = create_engine(database_url, echo=True)

# Configuración de la clase Session para manejar sesiones de base de datos
Session = sessionmaker(bind=engine)

# Creación de la clase base para definir las clases de modelo
Base = declarative_base()
