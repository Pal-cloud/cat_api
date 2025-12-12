from flask import Flask, jsonify, request

# 1. Crea la instancia de la aplicación Flask
app = Flask(__name__)

# 2. Define una ruta (endpoint) para la raíz (/) con el método GET
@app.route('/', methods=['GET'])
def home():
    # 3. Devuelve una respuesta JSON simple
    return jsonify({'mensaje': '¡Bienvenido a mi API con Flask!'})

# 4. Define otra ruta para recibir datos (POST)
@app.route('/saludar', methods=['POST'])
def saludar():
    # 5. Obtiene los datos JSON enviados en la petición
    datos = request.get_json()
    nombre = datos.get('nombre', 'Invitado') # Obtiene el nombre o usa 'Invitado' por defecto
    return jsonify({'saludo': f'Hola, {nombre}!'})

# 6. Ejecuta la aplicación si este script es el principal
if __name__ == '__main__':
    app.run(debug=True) # debug=True para ver errores en el navegador
