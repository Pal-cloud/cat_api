# Pequeña demo para levantar Flask en local y probarlo

## 1.- Instalar Imsomnia (Cliente de API)

Descargarlo de https://insomnia.rest/

## 2.- Instalar flask

        pip install flask

## 3.- Crear un fichero con extensión **py** con el siguiente código

        from flask import Flask, jsonify, request

        app = Flask(__name__)

        @app.route('/', methods=['GET'])
        def home():
            return jsonify({'mensaje': '¡Bienvenido a mi API con Flask!'})

        @app.route('/saludar', methods=['POST'])
        def saludar():
            datos = request.get_json()
            nombre = datos.get('nombre', 'Invitado') # Obtiene el nombre o usa 'Invitado' por defecto
            return jsonify({'saludo': f'Hola, {nombre}!'})


        if __name__ == '__main__':
            app.run(debug=True) # debug=True para ver errores en el navegador