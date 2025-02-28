from flask import Blueprint, jsonify, request
from database import conexion

medicos_bp = Blueprint('medicos', __name__)  # Corrección del Blueprint

@medicos_bp.route('/medico', methods=['POST'])  # Ajustado a la acción correcta
def registrar_medico():
    datos = request.json
    try:
        cursor = conexion.connection.cursor()

        sql = """INSERT INTO medico (nombre, apellido, numero_documento, celular, cod_tipo_documento, 
                 cod_especialidad) 
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (
            datos.get('nombre'), datos.get('apellido'), datos.get('numero_documento'), 
            datos.get('celular'), datos.get('cod_tipo_documento'), datos.get('cod_especialidad')
        ))
        conexion.connection.commit()
        cursor.close()

        return jsonify({
            'mensaje': "Medico registrado exitosamente.",
            'exito': True
        })

    except Exception as ex:
        return jsonify({'mensaje': f"Error en el registro: {str(ex)}", 'exito': False}), 500
