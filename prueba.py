from bson import ObjectId
from Database import Database
from datetime import datetime
from CRUD.UsuariosCRUD import UsuariosCRUD
from CRUD.ProductosCRUD import ProductosCRUD
from CRUD.EmpleadosCRUD import EmpleadosCRUD
from CRUD.DistribuidoresCRUD import DistribuidoresCRUD
from CRUD.ClientesCRUD import ClientesCRUD
from CRUD.CategoriasCRUD import CategoriasCRUD


class Menu:
    def __init__(self):
        # Conectar a la base de datos MongoDB
        self.db = Database("mongodb://localhost:27017/", "ProtoDEVDB")  # Cambia la URI y nombre de la base de datos si es necesario
        self.db.connect()  # Conectar a la base de datos
        self.usuarios_crud = UsuariosCRUD(self.db)
        self.productos_crud = ProductosCRUD(self.db)
        self.empleados_crud = EmpleadosCRUD(self.db)
        self.distribuidores_crud = DistribuidoresCRUD(self.db)
        self.clientes_crud = ClientesCRUD(self.db)
        self.categorias_crud = CategoriasCRUD(self.db)

    def mostrar_menu(self):
        while True:
            print("\n--- Menú CRUD ---")
            print("1. CRUD Usuarios")
            print("2. CRUD Productos")
            print("3. CRUD Empleados")
            print("4. CRUD Distribuidores")
            print("5. CRUD Clientes")
            print("6. CRUD Categorias")
            print("7. Salir")

            choice = input("Selecciona una opción (1-7): ")

            if choice == '1':
                self.menu_usuarios()
            elif choice == '2':
                self.menu_productos()
            elif choice == '3':
                self.menu_empleados()
            elif choice == '4':
                self.menu_distribuidores()
            elif choice == '5':
                self.menu_clientes()
            elif choice == '6':
                self.menu_categorias()
            elif choice == '7':
                print("Saliendo del menú.")
                break
            else:
                print("Selección no válida. Intenta de nuevo.")

    # Menú para el CRUD de Usuarios
    def menu_usuarios(self):
        while True:
            print("\n--- Menú CRUD para Usuarios ---")
            print("1. Crear Usuario (Create)")
            print("2. Leer Usuario (Read)")
            print("3. Actualizar Usuario (Update)")
            print("4. Eliminar Usuario (Delete)")
            print("5. Listar Usuarios")
            print("6. Volver al menú principal")

            choice = input("Selecciona una opción (1-6): ")

            if choice == '1':
                self.create_usuario()
            elif choice == '2':
                self.read_usuario()
            elif choice == '3':
                self.update_usuario()
            elif choice == '4':
                self.delete_usuario()
            elif choice == '5':
                self.listar_usuarios()
            elif choice == '6':
                break
            else:
                print("Selección no válida. Intenta de nuevo.")

    def create_usuario(self):
        correo = input("Correo: ")
        contraseña = input("Contraseña: ")
        rol = input("Rol: ")
        estado = input("Estado: ")
        result = self.usuarios_crud.create(correo, contraseña, rol, estado)
        print(f"Usuario creado con ID: {result}")

    def read_usuario(self):
        usuario_id = input("Ingrese el ID del usuario a consultar: ")
        usuario = self.usuarios_crud.read(usuario_id)
        print(usuario if usuario else "Usuario no encontrado")

    def update_usuario(self):
        usuario_id = input("Ingrese el ID del usuario a actualizar: ")
        campo = input("Campo a actualizar (correo, contraseña, rol, estado): ")
        valor = input(f"Nuevo valor para {campo}: ")
        result = self.usuarios_crud.update(usuario_id, {campo: valor})
        print(f"{result} campo(s) actualizado(s)")

    def delete_usuario(self):
        usuario_id = input("Ingrese el ID del usuario a eliminar: ")
        result = self.usuarios_crud.delete(usuario_id)
        print(f"{result} usuario(s) eliminado(s)")

    def listar_usuarios(self):
        usuarios = self.usuarios_crud.list_all()
        for usuario in usuarios:
            print(usuario)

    # Menú para el CRUD de Productos
    def menu_productos(self):
        while True:
            print("\n--- Menú CRUD para Productos ---")
            print("1. Crear Producto (Create)")
            print("2. Leer Producto (Read)")
            print("3. Actualizar Producto (Update)")
            print("4. Eliminar Producto (Delete)")
            print("5. Listar Productos")
            print("6. Volver al menú principal")

            choice = input("Selecciona una opción (1-6): ")

            if choice == '1':
                self.create_producto()
            elif choice == '2':
                self.read_producto()
            elif choice == '3':
                self.update_producto()
            elif choice == '4':
                self.delete_producto()
            elif choice == '5':
                self.listar_productos()
            elif choice == '6':
                break
            else:
                print("Selección no válida. Intenta de nuevo.")

    def create_producto(self):
        nombre = input("Nombre: ")
        descripcion = input("Descripción: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        sku = input("SKU: ")
        estado_stock = input("Estado de stock: ")
        categoria_id = input("ID de categoría: ")
        distribuidor_id = input("ID de distribuidor: ")
        result = self.productos_crud.create(nombre, descripcion, precio, stock, sku, estado_stock, categoria_id, distribuidor_id)
        print(f"Producto creado con ID: {result}")

    def read_producto(self):
        producto_id = input("Ingrese el ID del producto a consultar: ")
        producto = self.productos_crud.read(producto_id)
        print(producto if producto else "Producto no encontrado")

    def update_producto(self):
        producto_id = input("Ingrese el ID del producto a actualizar: ")
        campo = input("Campo a actualizar (nombre, descripción, precio, stock, sku, estado_stock, categoria_id, distribuidor_id): ")
        valor = input(f"Nuevo valor para {campo}: ")
        result = self.productos_crud.update(producto_id, {campo: valor})
        print(f"{result} campo(s) actualizado(s)")

    def delete_producto(self):
        producto_id = input("Ingrese el ID del producto a eliminar: ")
        result = self.productos_crud.delete(producto_id)
        print(f"{result} producto(s) eliminado(s)")

    def listar_productos(self):
        productos = self.productos_crud.list_all()
        for producto in productos:
            print(producto)

    # Menú para el CRUD de Empleados
    def menu_empleados(self):
        while True:
            print("\n--- Menú CRUD para Empleados ---")
            print("1. Crear empleado (Create)")
            print("2. Leer empleado (Read)")
            print("3. Actualizar empleado (Update)")
            print("4. Eliminar empleado (Delete)")
            print("5. Listar empleados")
            print("6. Volver al menú principal")

            choice = input("Selecciona una opción (1-6): ")

            if choice == '1':
                self.create_empleado()
            elif choice == '2':
                self.read_empleado()
            elif choice == '3':
                self.update_empleado()
            elif choice == '4':
                self.delete_empleado()
            elif choice == '5':
                self.listar_empleados()
            elif choice == '6':
                break
            else:
                print("Selección no válida. Intenta de nuevo.")

    def create_empleado(self):
        usuario_id = input(f"usuario_id: ")
        nombre = input("nombre: ")
        apellido = input("apellido: ")
        tipo_empleado = input("tipo_empleado (Administrador, Ventas, Analisis): ")
        telefono = input("telefono: ")
        result = self.empleados_crud.create(ObjectId(usuario_id), nombre, apellido, tipo_empleado, telefono)
        print(f"Usuario creado con ID: {result}")

    def read_empleado(self):
        empleado_id = input("Ingrese el ID del empleado a consultar: ")
        empleado = self.empleados_crud.read(empleado_id)
        print(empleado if empleado else "Empleado no encontrado")

    def update_empleado(self):
        usuario_id = input("Ingrese el ID del empleado a actualizar: ")
        campo = input("Campo a actualizar (nombre, apellido, tipo_empleado, telefono): ")
        valor = input(f"Nuevo valor para {campo}: ")
        result = self.empleados_crud.update(usuario_id, {campo: valor})
        print(f"{result} campo(s) actualizado(s)")

    def delete_empleado(self):
        empleado_id = input("Ingrese el ID del empleado a eliminar: ")
        result = self.empleados_crud.delete(empleado_id)
        print(f"{result} empleado(s) eliminado(s)")

    def listar_empleados(self):
        empleados = self.empleados_crud.list_all()
        for empleado in empleados:
            print(empleado)

    # Menú para el CRUD de Distribuidores
    def menu_distribuidores(self):
        while True:
            print("\n--- Menú CRUD para Distribuidores ---")
            print("1. Crear distribuidor (Create)")
            print("2. Leer distribuidor (Read)")
            print("3. Actualizar distribuidor (Update)")
            print("4. Eliminar distribuidor (Delete)")
            print("5. Listar distribuidores")
            print("6. Volver al menú principal")

            choice = input("Selecciona una opción (1-6): ")

            if choice == '1':
                self.create_distribuidor()
            elif choice == '2':
                self.read_distribuidor()
            elif choice == '3':
                self.update_distribuidor()
            elif choice == '4':
                self.delete_distribuidor()
            elif choice == '5':
                self.listar_distribuidores()
            elif choice == '6':
                break
            else:
                print("Selección no válida. Intenta de nuevo.")

    def create_distribuidor(self):
        usuario_id = input(f"usuario_id: ")
        nombre_distribuidor = input("nombre_distribuidor: ")
        ruc = input("ruc: ")
        telefono = input("telefono: ")
        result = self.distribuidores_crud.create(ObjectId(usuario_id), nombre_distribuidor, ruc, telefono)
        print(f"Distribuidor creado con ID: {result}")

    def read_distribuidor(self):
        distribuidor_id = input("Ingrese el ID del distribuidor a consultar: ")
        distribuidor = self.distribuidores_crud.read(distribuidor_id)
        print(distribuidor if distribuidor else "Distribuidor no encontrado")

    def update_distribuidor(self):
        distribuidor_id = input("Ingrese el ID del distribuidor a actualizar: ")
        campo = input("Campo a actualizar (nombre_distribuidor, ruc, telefono): ")
        valor = input(f"Nuevo valor para {campo}: ")
        result = self.distribuidores_crud.update(distribuidor_id, {campo: valor})
        print(f"{result} campo(s) actualizado(s)")

    def delete_distribuidor(self):
        distribuidor_id = input("Ingrese el ID del distribuidor a eliminar: ")
        result = self.distribuidores_crud.delete(distribuidor_id)
        print(f"{result} distribuidor(es) eliminado(s)")

    def listar_distribuidores(self):
        distribuidores = self.distribuidores_crud.list_all()
        for distribuidor in distribuidores:
            print(distribuidor)

    # Menú para el CRUD de Clientes
    def menu_clientes(self):
        while True:
            print("\n--- Menú CRUD para Clientes ---")
            print("1. Crear cliente (Create)")
            print("2. Leer cliente (Read)")
            print("3. Actualizar cliente (Update)")
            print("4. Eliminar cliente (Delete)")
            print("5. Listar clientes")
            print("6. Volver al menú principal")

            choice = input("Selecciona una opción (1-6): ")

            if choice == '1':
                self.create_cliente()
            elif choice == '2':
                self.read_cliente()
            elif choice == '3':
                self.update_cliente()
            elif choice == '4':
                self.delete_cliente()
            elif choice == '5':
                self.listar_clientes()
            elif choice == '6':
                break
            else:
                print("Selección no válida. Intenta de nuevo.")

    def create_cliente(self):
        usuario_id = input(f"usuario_id: ")
        nombre = input("nombre: ")
        apellido = input("apellido: ")
        direccion = input("direccion: ")
        telefono = input("telefono: ")
        result = self.clientes_crud.create(ObjectId(usuario_id), nombre, apellido, direccion, telefono)
        print(f"Cliente creado con ID: {result}")

    def read_cliente(self):
        cliente_id = input("Ingrese el ID del cliente a consultar: ")
        cliente = self.clientes_crud.read(cliente_id)
        print(cliente if cliente else "Cliente no encontrado")

    def update_cliente(self):
        cliente_id = input("Ingrese el ID del cliente a actualizar: ")
        campo = input("Campo a actualizar (nombre, apellido, direccion, telefono): ")
        valor = input(f"Nuevo valor para {campo}: ")
        result = self.clientes_crud.update(cliente_id, {campo: valor})
        print(f"{result} campo(s) actualizado(s)")

    def delete_cliente(self):
        cliente_id = input("Ingrese el ID del cliente a eliminar: ")
        result = self.clientes_crud.delete(cliente_id)
        print(f"{result} cliente(s) eliminado(s)")

    def listar_clientes(self):
        clientes = self.clientes_crud.list_all()
        for cliente in clientes:
            print(cliente)

    # Menú para el CRUD de Categorias
    def menu_categorias(self):
        while True:
            print("\n--- Menú CRUD para Categorías ---")
            print("1. Crear categoría (Create)")
            print("2. Leer categoría (Read)")
            print("3. Actualizar categoría (Update)")
            print("4. Eliminar categoría (Delete)")
            print("5. Listar categorías")
            print("6. Volver al menú principal")

            choice = input("Selecciona una opción (1-6): ")

            if choice == '1':
                self.create_categoria()
            elif choice == '2':
                self.read_categoria()
            elif choice == '3':
                self.update_categoria()
            elif choice == '4':
                self.delete_categoria()
            elif choice == '5':
                self.listar_categorias()
            elif choice == '6':
                break
            else:
                print("Selección no válida. Intenta de nuevo.")

    def create_categoria(self):
        usuario_id = input(f"usuario_id: ")
        nombre = input("nombre: ")
        descripcion = input("descripcion: ")
        result = self.categorias_crud.create(usuario_id, nombre, descripcion)
        print(f"Categoría creada con ID: {result}")

    def read_categoria(self):
        categoria_id = input("Ingrese el ID de la categoría a consultar: ")
        categoria = self.categorias_crud.read(categoria_id)
        print(categoria if categoria else "Categoría no encontrada")

    def update_categoria(self):
        categoria_id = input("Ingrese el ID de la categoría a actualizar: ")
        campo = input("Campo a actualizar (nombre, descripcion): ")
        valor = input(f"Nuevo valor para {campo}: ")
        result = self.categorias_crud.update(categoria_id, {campo: valor})
        print(f"{result} campo(s) actualizado(s)")

    def delete_categoria(self):
        categoria_id = input("Ingrese el ID de la categoría a eliminar: ")
        result = self.categorias_crud.delete(categoria_id)
        print(f"{result} categoría(s) eliminada(s)")

    def listar_categorias(self):
        categorias = self.categorias_crud.list_all()
        for categoria in categorias:
            print(categoria)

# Para ejecutar el menú:
if __name__ == '__main__':
    menu = Menu()
    menu.mostrar_menu()
