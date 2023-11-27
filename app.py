from flask import Flask

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una ruta para la página de inicio
@app.route('/')
def hola_mundo():
    return '¡Hola Mundo!'

# Punto de entrada de la aplicación
if __name__ == '__main__':
    app.run()
