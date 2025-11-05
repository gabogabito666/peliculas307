from flask import Flask, render_template  # Importa Flask y la función para renderizar plantillas

app = Flask(__name__)  # Crea la aplicación Flask

# -----------------------------
# Datos de ejemplo para las películas
# -----------------------------
peliculas = {
    'suspenso': [
        {'titulo': 'El Silencio de los Inocentes',
         'sinopsis': 'Una joven agente del FBI busca la ayuda de un asesino encarcelado para atrapar a otro.'},
        {'titulo': 'Perdida',
         'sinopsis': 'Un hombre se convierte en el principal sospechoso cuando su esposa desaparece.'}
    ],
    'terror': [
        {'titulo': 'El Exorcista',
         'sinopsis': 'Una niña es poseída por una entidad demoníaca.'},
        {'titulo': 'Hereditary',
         'sinopsis': 'Una familia es atormentada tras la muerte de su matriarca.'}
    ],
    'romance': [
        {'titulo': 'Orgullo y Prejuicio',
         'sinopsis': 'Elizabeth Bennet se enfrenta al arrogante Sr. Darcy en la Inglaterra del siglo XIX.'},
        {'titulo': 'La La Land',
         'sinopsis': 'Un pianista de jazz y una aspirante a actriz persiguen sus sueños en Los Ángeles.'}
    ],
    'infantil': [
        {'titulo': 'Toy Story',
         'sinopsis': 'Un grupo de juguetes cobra vida cuando su dueño no está.'},
        {'titulo': 'Mi Vecino Totoro',
         'sinopsis': 'Dos hermanas se mudan al campo y se hacen amigas de un espíritu del bosque.'}
    ]
}

# -----------------------------
# Rutas de la aplicación
# -----------------------------

@app.route('/')
def index():
    # Renderiza la plantilla principal index.html
    return render_template('index.html')

@app.route('/suspenso')
def suspenso():
    # Pasa la lista de películas de la categoría 'suspenso' a la plantilla suspenso.html
    return render_template('suspenso.html', peliculas=peliculas['suspenso'])

@app.route('/terror')
def terror():
    # Pasa la lista de películas de la categoría 'terror' a la plantilla terror.html
    return render_template('terror.html', peliculas=peliculas['terror'])

@app.route('/romance')
def romance():
    # Pasa la lista de películas de la categoría 'romance' a la plantilla romance.html
    return render_template('romance.html', peliculas=peliculas['romance'])

@app.route('/infantil')
def infantil():
    # Pasa la lista de películas de la categoría 'infantil' a la plantilla infantil.html
    return render_template('infantil.html', peliculas=peliculas['infantil'])

# -----------------------------
# Ejecución de la aplicación
# -----------------------------
if __name__ == '__main__':
    # Inicia el servidor de desarrollo con recarga automática y modo debug activado
    app.run(debug=True)