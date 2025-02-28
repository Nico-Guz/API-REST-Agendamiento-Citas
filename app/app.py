from flask import Flask
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)
app.config.from_object(config['development'])

# Configurar la base de datos
mysql = MySQL(app)

# Manejo de errores
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "Página no encontrada", 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
