from bson import ObjectId
from Database import Database

class ProductosCRUD():
    def __init__(self, db: Database):
        self.db = db
        self.collection = self.db.get_collection('productos')

    # Create - Crear
    def create(self, nombre, descripcion, precio, stock, sku, estado_stock, categoria_id, distribuidor_id, activo=True):
        # Creación de un nuevo producto
        producto = {
            'nombre': nombre,
            'descripcion': descripcion,
            'precio': precio,
            'stock': stock,
            'sku': sku,
            'estado_stock': estado_stock,
            'categoria_id': ObjectId(categoria_id),  # Convertir a ObjectId
            'distribuidor_id': ObjectId(distribuidor_id),  # Convertir a ObjectId
            'activo': activo
        }

        result = self.collection.insert_one(producto)
        return str(result.inserted_id)

    # Read - Leer
    def read(self, producto_id):
        try:
            producto = self.collection.find_one({'_id': ObjectId(producto_id)})
            if producto:
                return producto
            else:
                return None
        except Exception as e:
            print(f'Error al leer el producto : {e}')
            return None

    # Update - Actualizar
    def update(self, producto_id, update_data):
        try:
            result = self.collection.update_one(
                {'_id': ObjectId(producto_id)},
                {'$set': update_data}
            )
            return result.modified_count
        except Exception as e:
            print(f'Error al actualizar el producto: {e}')
            return None

    # Delete - Eliminar
    def delete(self, producto_id):
        try:
            result = self.collection.delete_one({'_id': ObjectId(producto_id)})
            return result.deleted_count
        except Exception as e:
            print(f'Error al eliminar el producto: {e}')
            return None

    # Listar todos los productos
    def list_all(self):
        try:
            productos = self.collection.find()
            return productos
        except Exception as e:
            print(f'Error al obtener los productos: {e}')
            return []
