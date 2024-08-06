from flask import Flask, render_template
from flask_consulate import Consul
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object('config.Config')

# Ruta para renderizar el template index.html
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para renderizar el template users.html
@app.route('/users')
def users():
    return render_template('users.html')

# Ruta para renderizar el template products.html
@app.route('/products')
def products():
    return render_template('products.html')

# Ruta para renderizar el template editUser.html

@app.route('/editUser/<string:id>')
def edit_user(id):
    print("id recibido",id)
    return render_template('editUser.html', id=id)

# Ruta para renderizar el template editProduct.html
@app.route('/editProduct/<string:id>')
def edit_product(id):
    print("id recibido",id)
    return render_template('editProduct.html', id=id)

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
    name='frontend',
    interval='10s',
    tags=['fronted', ],
    port=5001,
    httpcheck='http://192.168.80.3:5001/healthcheck'
)


if __name__ == '__main__':
    app.run()
