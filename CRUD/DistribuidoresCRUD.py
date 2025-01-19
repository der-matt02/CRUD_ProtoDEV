from bson import ObjectId
from Database import Database

class DistribuidoresCRUD:
    def __init__(self, db: Database):
        self.db = db
        self.collection = self.db.get_collection('distribuidores')

    # Create - Crear
    def create(self, usuario_id, nombre_distribuidor, ruc, telefono):

        # Creacion de un nuevo usuario
        distribuidor = {
            'usuario_id': usuario_id,
            'nombre_distribuidor': nombre_distribuidor,
            'ruc': ruc,
            'telefono': telefono
        }

        result = self.collection.insert_one(distribuidor)
        return str(result.inserted_id)

    # Read - Leer
    def read(self, distribuidor_id):

        # Leer distribuidor por Object_id
        try:
            distribuidor = self.collection.find_one({'_id': ObjectId(distribuidor_id)})
            if distribuidor:
                return distribuidor
            else:
                return None
        except Exception as e:
            print(f'Error al leer el distribuidor: {e}')
            return None

    # Update - Actualizar
    def update(self, distribuidor_id, update_data):

        # Actualizar un distribuidor
        try:
            result = self.collection.update_one(
                {'_id': ObjectId(distribuidor_id)},
                {'$set': update_data}
            )
            return result.modified_count
        except Exception as e:
            print(f'Error al actualizar el distribuidor: {e}')
            return None
            # return 0

    # Delete - Eliminar
    def delete(self, distribuidor_id):

        # Eliminar un cliente
        try:
            result = self.collection.delete_one({'_id': ObjectId(distribuidor_id)})
            return result.deleted_count
        except Exception as e:
            print(f'Error al eliminar el distribuidor: {e}')
            return None
            # return 0

    # Listar todos los distribuidor
    def list_all(self):

        # Listar todos los distribuidor
        try:
            distribuidores = self.collection.find()
            return distribuidores
        except Exception as e:
            print(f'Error al obtener el distribuidores: {e}')
            return []
            # return None
            # return 0
