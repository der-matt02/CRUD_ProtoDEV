from bson import ObjectId
from Database import Database


class ClientesCRUD:
    def __init__(self, db: Database):
        self.db = db
        self.collection = self.db.get_collection('clientes')

    # Create - Crear
    def create(self, usuario_id, nombre, apellido, direccion, telefono):

        # Creacion de un nuevo usuario
        cliente = {
            'usuario_id': usuario_id,
            'nombre': nombre,
            'apellido': apellido,
            'direccion': direccion,
            'telefono': telefono
        }

        result = self.collection.insert_one(cliente)
        return str(result.inserted_id)

    # Read - Leer
    def read(self, cliente_id):

        # Leer cliente por Object_id
        try:
            cliente = self.collection.find_one({'_id': ObjectId(cliente_id)})
            if cliente:
                return cliente
            else:
                return None
        except Exception as e:
            print(f'Error al leer el cliente: {e}')
            return None

    # Update - Actualizar
    def update(self, cliente_id, update_data):

        # Actualizar un cliente
        try:
            result = self.collection.update_one(
                {'_id': ObjectId(cliente_id)},
                {'$set': update_data}
            )
            return result.modified_count
        except Exception as e:
            print(f'Error al actualizar el cliente: {e}')
            return None
            # return 0

    # Delete - Eliminar
    def delete(self, usuario_id):

        # Eliminar un cliente
        try:
            result = self.collection.delete_one({'_id': ObjectId(usuario_id)})
            return result.deleted_count
        except Exception as e:
            print(f'Error al eliminar el cliente: {e}')
            return None
            # return 0

    # Listar todos los usuarios
    def list_all(self):

        # Listar todos los usuarios
        try:
            clientes = self.collection.find()
            return clientes
        except Exception as e:
            print(f'Error al obtener el cliente: {e}')
            return []
            # return None
            # return 0
