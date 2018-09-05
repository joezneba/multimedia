# Multimedia
Sistema de video

Requerimientos:
  - Python 3.5+
  - PostgreSQL
  - Servidor Nginx
  - Gunicorn
  
## Instalación en Ubuntu Server

```
$ sudo apt-get update
$ sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx
$ sudo -H pip3 install --upgrade pip
$ sudo -H pip3 install virtualenv 
```

### Crear base de datos en Postgres

```
$ sudo -u postgres psql
postgres=# CREATE DATABASE myproject;
postgres=# \q
```

### Entorno Virtual
```
$ virtualenv myprojectenv
$ source myprojectenv/bin/activate
```
### Clonar el proyecto
```
$ sudo apt-get install git
$ git clone https://github.com/nadiapc128/Multimedia.git
```

Para instalar las dependencias:
`$ pip install -r requirements.txt`

Las configuraciones del proyecto se encuentran en: `/Multimedia/Multimedia/settings.py`
