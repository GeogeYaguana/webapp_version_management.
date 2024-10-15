from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

@app.route('/registration', methods=['POST'])
def registration():
    data = request.get_json()
    
    if 'nombre' not in data or 'correo' not in data:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    nuevo_usuario = {
        "id": len(usuarios) + 1,
        "nombre": data['nombre'],
        "correo": data['correo']
    }

    usuarios.append(nuevo_usuario)

    return jsonify({"mensaje": "Usuario creado con éxito", "usuario": nuevo_usuario}), 201

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios), 200

if __name__ == '__main__':
    app.run(debug=True)
