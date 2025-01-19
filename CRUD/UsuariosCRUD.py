from bson import ObjectId
from datetime import datetime
from Database import Database

class UsuariosCRUD:
    def __init__(self, db: Database):
        self.db = db
        self.collection = self.db.get_collection('usuarios')

    # Create - Crear
    def create(self, correo, contraseña, rol, estado='activo'):

        # Creacion de un nuevo usuario
        usuario = {
            'correo': correo,
            'contraseña': contraseña,
            'rol': rol,
            'fecha_registro': datetime.now(),
            'estado': estado
        }

        result = self.collection.insert_one(usuario)
        return str(result.inserted_id)

    # Read - Leer
    def read(self, usuario_id):

        # Leer usuario por Object_id
        try:
            usuario = self.collection.find_one({'_id': ObjectId(usuario_id)})
            if usuario:
                return usuario
            else:
                return None
        except Exception as e:
            print(f'Error al leer el usuario: {e}')
            return None

    # Update - Actualizar
    def update(self, usuario_id, update_data):

        # Actualizar un usuario
        try:
            result = self.collection.update_one(
                {'_id': ObjectId(usuario_id)},
                {'$set': update_data}
            )
            return result.modified_count
        except Exception as e:
            print(f'Error al actualizar el usuario: {e}')
            return None
            # return 0

    # Delete - Eliminar
    def delete(self, usuario_id):

        # Eliminar un usuario
        try:
            result = self.collection.delete_one({'_id': ObjectId(usuario_id)})
            return result.deleted_count
        except Exception as e:
            print(f'Error al eliminar el usuario: {e}')
            return None
            # return 0

    # Listar todos los usuarios
    def list_all(self):

        # Listar todos los usuarios
        try:
            usuarios = self.collection.find()
            return usuarios
        except Exception as e:
            print(f'Error al obtener el usuario: {e}')
            return []
            # return None
            # return 0
