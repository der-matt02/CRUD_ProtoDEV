from bson import ObjectId
from Database import Database

class CategoriasCRUD:
    def __init__(self, db: Database):
        self.db = db
        self.collection = self.db.get_collection('categorias')

    # Create - Crear
    def create(self, usuario_id, nombre, descripcion):

        # Creacion de una nueva categoria
        categoria = {
            'usuario_id': usuario_id,
            'nombre': nombre,
            'descripcion': descripcion
        }

        result = self.collection.insert_one(categoria)
        return str(result.inserted_id)

    # Read - Leer
    def read(self, categoria_id):

        # Leer categoria por Object_id
        try:
            categoria = self.collection.find_one({'_id': ObjectId(categoria_id)})
            if categoria :
                return categoria
            else:
                return None
        except Exception as e:
            print(f'Error al leer la categoria : {e}')
            return None

    # Update - Actualizar
    def update(self, categoria_id, update_data):

        # Actualizar una categoria
        try:
            result = self.collection.update_one(
                {'_id': ObjectId(categoria_id)},
                {'$set': update_data}
            )
            return result.modified_count
        except Exception as e:
            print(f'Error al actualizar el distribuidor: {e}')
            return None
            # return 0

    # Delete - Eliminar
    def delete(self, categoria_id):

        # Eliminar una categoria
        try:
            result = self.collection.delete_one({'_id': ObjectId(categoria_id)})
            return result.deleted_count
        except Exception as e:
            print(f'Error al eliminar la categoria: {e}')
            return None
            # return 0

    # Listar todas las categorias
    def list_all(self):

        # Listar todas las categorias
        try:
            categorias = self.collection.find()
            return categorias
        except Exception as e:
            print(f'Error al obtener la categoria: {e}')
            return []
            # return None
            # return 0
