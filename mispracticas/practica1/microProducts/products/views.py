from flask import Flask, render_template
from products.controllers.product_controller import product_controller
from db.db import db
from flask_cors import CORS
from flask_consulate import Consul	

app = Flask(__name__)
CORS(app)
app.config.from_object('config.Config')
db.init_app(app)

# Registrando el blueprint del controlador de usuarios
app.register_blueprint(product_controller)

@app.route('/healthcheck')
def health_check():
    """
    This function is used to say current status to the Consul.
    Format: https://www.consul.io/docs/agent/checks.html

    :return: Empty response with status 200, 429 or 500
    """
    # TODO: implement any other checking logic.
    return '', 200

# Consul
# This extension should be the first one if enabled:
consul = Consul(app=app)
# Fetch the conviguration:
consul.apply_remote_config(namespace='mynamespace/')
# Register Consul service:
consul.register_service(
    name='microProducts',
    interval='10s',
    tags=['microProducts', ],
    port=5002,
    httpcheck='http://192.168.80.3:5003/healthcheck'
)

if __name__ == '__main__':
    app.run()
