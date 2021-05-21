# Tu Credito

Proyecto de la entrevista tecnica de Manuel Escalante para Darien Techonlogy en el que se desarrolló un CRUD básico de una entidad financiera en la que se maneja Bancos, Clientes y Creditos. Desarrollada en Django con conexion a PostgreSQL como base de datos.

# Instalación local

## Virtual environment

Para evitar conflictos con las paquetes instalados globalmente y en el home del usuario activo es recomendable el uso de un virtual environment. Por eso recomiendo usar [virtualenv](https://virtualenv.pypa.io/en/stable/).

Para instalar las dependencias del proyecto primero se debe activar el entorno virtual

```bash
# Si usas virtualenv con bash
source env/bin/activate
# Si usas virtualenv con fish (mi caso)
source env/bin/activate.fish
```

Se proceden a instalar los paquetes con pip

```bash
pip install -r requirements.txt
```

## Base de datos
Los datos para la conexión local en PostgreSQL son los siguientes:

```bash
NAME: tucredito
USER: tucredito
PASSWORD: tucredito_password123
HOST: localhost
PORT: 5432
```

También pueden ejecutar el script __installdb__, ubicado en la raiz del proyecto, para crear la base de datos sin ninguna complicación estando en Linux. (No funciona en Windows)

```bash
chmod +x installdb.sh

./installdb.sh
```

Teniendo nuestro entorno virtual habilitado procedemos a ejecutar:

```bash
python manage.py migrate

python manage.py runserver
```