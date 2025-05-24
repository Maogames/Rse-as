from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

reseñas = []

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/registro')
def formulario_reseña():
    return render_template('registro.html')

@app.route('/lista')
def lista_reseñas():
    return render_template('lista.html', reseñas=reseñas)

@app.route('/reseña', methods=['POST'])
def registrar_reseña():
    data = request.get_json()
    titulo = data.get('titulo')
    usuario = data.get('usuario')
    puntuacion = data.get('puntuacion')
    comentario = data.get('comentario')

    if not all([titulo, usuario, puntuacion, comentario]):
        return jsonify({'error': 'Faltan datos'}), 400

    reseñas.append({
        'titulo': titulo,
        'usuario': usuario,
        'puntuacion': puntuacion,
        'comentario': comentario
    })
    return jsonify({'mensaje': 'Reseña registrada con éxito'}), 200

@app.route('/api/reseñas')
def api_reseñas():
    return jsonify(reseñas)

if __name__ == '__main__':
    app.run(debug=True)