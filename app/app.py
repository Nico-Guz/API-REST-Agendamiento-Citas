from flask import Flask
from flask_mysqldb import MySQL
from config import config

from routes.pacientes import pacientes_bp
from routes.index import index_bp
from routes.citas import citas_bp
from routes.medico import medicos_bp

app = Flask(__name__)
app.config.from_object(config['development'])

# Configurar la base de datos
mysql = MySQL(app)

# Registrar Blueprints
app.register_blueprint(pacientes_bp)
app.register_blueprint(index_bp)
app.register_blueprint(citas_bp)
app.register_blueprint(medicos_bp)

# Manejo de errores
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "Página no encontrada", 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
