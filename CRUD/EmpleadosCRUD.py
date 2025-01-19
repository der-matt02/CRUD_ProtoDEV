from bson import ObjectId
from Database import Database

class EmpleadosCRUD:
    def __init__(self, db: Database):
        self.db = db
        self.collection = self.db.get_collection('empleados')


    # Create - Crear
    def create(self, usuario_id, nombre, apellido, tipo_empleado, telefono):

        # Creacion de un nuevo empleado
        empleado = {
            'usuario_id': usuario_id,
            'nombre': nombre,
            'apellido': apellido,
            'tipo_empleado': tipo_empleado,
            'telefono': telefono
        }

        result = self.collection.insert_one(empleado)
        return str(result.inserted_id)

    # Read - Leer
    def read(self, distribuidor_id):

        # Leer empleado por Object_id
        try:
            empleado = self.collection.find_one({'_id': ObjectId(distribuidor_id)})
            if empleado :
                return empleado
            else:
                return None
        except Exception as e:
            print(f'Error al leer el empleado : {e}')
            return None

    # Update - Actualizar
    def update(self, empleado_id, update_data):

        # Actualizar un empleado
        try:
            result = self.collection.update_one(
                {'_id': ObjectId(empleado_id)},
                {'$set': update_data}
            )
            return result.modified_count
        except Exception as e:
            print(f'Error al actualizar el distribuidor: {e}')
            return None
            # return 0

    # Delete - Eliminar
    def delete(self, empleado_id):

        # Eliminar un empleado
        try:
            result = self.collection.delete_one({'_id': ObjectId(empleado_id)})
            return result.deleted_count
        except Exception as e:
            print(f'Error al eliminar el empleado: {e}')
            return None
            # return 0

    # Listar todos los empleados
    def list_all(self):

        # Listar todos los empleados
        try:
            empleados = self.collection.find()
            return empleados
        except Exception as e:
            print(f'Error al obtener el empleados: {e}')
            return []
            # return None
            # return 0
