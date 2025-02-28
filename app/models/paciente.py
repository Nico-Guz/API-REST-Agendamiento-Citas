class Paciente:
    def __init__(self, id, nombre, apellido, num_documento, celular, cod_tipo_documento):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.num_documento = num_documento
        self.celular = celular
        self.cod_tipo_documento = cod_tipo_documento

    def to_dict(self):
        return {'id': self.id, 'nombre': self.nombre, 'apellido': self.apellido, 'num_documento':self.num_documento, 
                'celular':self.celular, 'cod_tipo_documento':self.cod_tipo_documento}
