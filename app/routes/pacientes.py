from flask import Blueprint, jsonify, request
from database import conexion

pacientes_bp = Blueprint('pacientes', __name__)

@pacientes_bp.route('/paciente', methods=['POST'])
def registrar_paciente():
    datos = request.json
    try:
        cursor = conexion.connection.cursor()

        sql_paciente = """INSERT INTO paciente (nombre, apellido, numero_documento, celular, cod_tipo_documento) 
                          VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(sql_paciente, (
            datos['nombre'], datos['apellido'], datos['numero_documento'],
            datos['celular'], datos['cod_tipo_documento']
        ))
        conexion.connection.commit()

        cod_paciente = cursor.lastrowid

        sql_usuario = """INSERT INTO usuario (correo, contrasena, cod_rol, cod_paciente) 
                         VALUES (%s, %s, %s, %s)"""
        cursor.execute(sql_usuario, (
            datos['correo'], datos['contrasena'], datos['cod_rol'], cod_paciente
        ))
        conexion.connection.commit()

        return jsonify({
            'mensaje': "Paciente y usuario registrados.",
            'exito': True,
            'cod_paciente': cod_paciente
        })

    except Exception as ex:
        return jsonify({'mensaje': f"Error en el registro: {str(ex)}", 'exito': False})
