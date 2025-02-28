from flask import Blueprint, jsonify, request
from database import conexion

citas_bp = Blueprint('citas', __name__)

@citas_bp.route('/cita', methods=['POST'])
def registrar_cita():
    datos = request.json
    try:
        cursor = conexion.connection.cursor()
        
        sql = """INSERT INTO cita (inicio, fin, cod_paciente, cod_medico, cod_tipo_cita, cod_estado) 
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (
            datos['inicio'], datos['fin'], datos['cod_paciente'], 
            datos['cod_medico'], datos['cod_tipo_cita'], datos['cod_estado']
        ))
        conexion.connection.commit()

        return jsonify({
            'mensaje': "Cita registrada exitosamente.",
            'exito': True
        })

    except Exception as ex:
        return jsonify({'mensaje': f"Error en el registro: {str(ex)}", 'exito': False})


@citas_bp.route('/cita/<int:codigo>', methods=['DELETE'])
def eliminar_cita(codigo):
    try:
        cursor = conexion.connection.cursor()

        # Verificar si la cita existe
        cursor.execute("SELECT * FROM cita WHERE id = %s", (codigo,))
        cita = cursor.fetchone()

        if not cita:
            return jsonify({'mensaje': 'Cita no encontrada.', 'exito': False}), 404

        # Eliminar la cita
        cursor.execute("DELETE FROM cita WHERE id = %s", (codigo,))
        conexion.connection.commit()

        return jsonify({'mensaje': 'Cita eliminada exitosamente.', 'exito': True})

    except Exception as e:
        return jsonify({'mensaje': f'Error al eliminar la cita: {str(e)}', 'exito': False}), 500


@citas_bp.route('/cita/<int:codigo>', methods=['PUT'])
def actualizar_cita(codigo):
    datos = request.json
    try:
        cursor = conexion.connection.cursor()

        # Verificar si la cita existe
        cursor.execute("SELECT * FROM cita WHERE id = %s", (codigo,))
        cita = cursor.fetchone()

        if not cita:
            return jsonify({'mensaje': 'Cita no encontrada.', 'exito': False}), 404

        # Actualizar la cita
        sql = """UPDATE cita SET inicio = %s, fin = %s, cod_paciente = %s, cod_medico = %s, 
                 cod_tipo_cita = %s, cod_estado = %s WHERE id = %s"""
        cursor.execute(sql, (
            datos['inicio'], datos['fin'], datos['cod_paciente'],
            datos['cod_medico'], datos['cod_tipo_cita'], datos['cod_estado'], codigo
        ))
        conexion.connection.commit()

        return jsonify({'mensaje': 'Cita actualizada exitosamente.', 'exito': True})

    except Exception as e:
        return jsonify({'mensaje': f'Error al actualizar la cita: {str(e)}', 'exito': False}), 500
