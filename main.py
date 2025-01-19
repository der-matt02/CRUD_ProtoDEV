from Database import Database


class main:
    if __name__ == "__main__":
        db = Database()

        try:
            # Conectar a la base de datos
            db.connect()

            # Acceder a una colección
            usuarios_collection = db.get_collection("usuarios")

            # Consultar documentos
            print("Usuarios en la colección:")
            for usuario in usuarios_collection.find():
                print(usuario)

        finally:
            # Cerrar conexión
            db.close()
