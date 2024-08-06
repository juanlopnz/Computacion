#!/bin/bash

# Iniciar Consul en segundo plano
nohup consul agent -ui -dev -bind=192.168.80.3 -client=0.0.0.0 -data-dir=. &
echo "Consul is running in the background."

# Esperar unos segundos para asegurarse de que Consul se inicie correctamente
sleep 5

# Cambiar al directorio de la aplicación Flask frontend
cd /home/vagrant/frontend

# Establecer la variable de entorno FLASK_APP
export FLASK_APP=run.py

# Iniciar la aplicación Flask frontend en segundo plano
nohup /usr/local/bin/flask run --host=0.0.0.0 --port 5001 &
echo "Flask frontend app is running in the background."

# Cambiar al directorio de la aplicación Flask microUsers
cd /home/vagrant/microUsers

# Establecer la variable de entorno FLASK_APP
export FLASK_APP=run.py

# Iniciar la aplicación Flask microUsers en segundo plano
nohup /usr/local/bin/flask run --host=0.0.0.0 --port 5002 &
echo "Flask microUsers app is running in the background."

# Cambiar al directorio de la aplicación Flask microProducts
cd /home/vagrant/microProducts

# Establecer la variable de entorno FLASK_APP
export FLASK_APP=run.py

# Iniciar la aplicación Flask microProducts en segundo plano
nohup /usr/local/bin/flask run --host=0.0.0.0 --port 5003 &
echo "Flask microProducts app is running in the background."
