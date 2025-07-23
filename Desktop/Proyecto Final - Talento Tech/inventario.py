#@Author Matias Tomas Del Pup
#Aplique mis conocimientos de los cursos de Python y videos que me vi, mas mis estudios de la carrera, espero le guste :)



import sqlite3
import os
from colorama import init, Fore, Style


init(autoreset=True)

#Tuve que usar este metodo porque me creaba la base de datos en el escritorio y queria que cuando lo mandara pudiera ejecutar la base de mi carpeta. Estuve probando otros metodos pero simplemente me seguia creando bases de datos en el Escritorio.
basedir = os.path.dirname(os.path.abspath(__file__))
ruta_db = os.path.join(basedir, "inventario.db")

con = sqlite3.connect(ruta_db)
cursor = con.cursor()

#Creo la tabla 
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    cantidad INTEGER NOT NULL,
    precio REAL NOT NULL,
    categoria TEXT
)
''')
con.commit()

#Todas las funciones del programa

def registrar_producto():
    print(Fore.CYAN + "\n[ Registrar nuevo producto ]")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    categoria = input("Categoría: ")
    cursor.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)",
                   (nombre, descripcion, cantidad, precio, categoria))
    con.commit()
    print(Fore.GREEN + "Producto registrado correctamente.\n")

def mostrar_productos():
    print(Fore.CYAN + "\n[ Lista de productos ]")
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    if productos:
        for p in productos:
            print(Fore.YELLOW + f"ID: {p[0]}, Nombre: {p[1]}, Cantidad: {p[3]}, Precio: ${p[4]}, Categoría: {p[5]}")
    else:
        print(Fore.RED + "No hay productos registrados.")

def actualizar_producto():
    print(Fore.CYAN + "\n[ Actualizar producto por ID ]")
    id_producto = input("ID del producto a actualizar: ")
    cursor.execute("SELECT * FROM productos WHERE id=?", (id_producto,))
    producto = cursor.fetchone()
    if producto:
        nombre = input(f"Nuevo nombre ({producto[1]}): ") or producto[1]
        descripcion = input(f"Nueva descripción ({producto[2]}): ") or producto[2]
        cantidad = input(f"Nueva cantidad ({producto[3]}): ") or producto[3]
        precio = input(f"Nuevo precio ({producto[4]}): ") or producto[4]
        categoria = input(f"Nueva categoría ({producto[5]}): ") or producto[5]

        cursor.execute('''
        UPDATE productos SET nombre=?, descripcion=?, cantidad=?, precio=?, categoria=? WHERE id=?
        ''', (nombre, descripcion, int(cantidad), float(precio), categoria, id_producto))
        con.commit()
        print(Fore.GREEN + "Producto actualizado correctamente.")
    else:
        print(Fore.RED + "Producto no encontrado.")

def eliminar_producto():
    print(Fore.CYAN + "\n[ Eliminar producto por ID ]")
    id_producto = input("ID del producto a eliminar: ")
    cursor.execute("SELECT * FROM productos WHERE id=?", (id_producto,))
    if cursor.fetchone():
        cursor.execute("DELETE FROM productos WHERE id=?", (id_producto,))
        con.commit()
        print(Fore.GREEN + "Producto eliminado.")
    else:
        print(Fore.RED + "Producto no encontrado.")

def buscar_producto():
    print(Fore.CYAN + "\n[ Buscar producto por ID ]")
    id_producto = input("ID del producto: ")
    cursor.execute("SELECT * FROM productos WHERE id=?", (id_producto,))
    producto = cursor.fetchone()
    if producto:
        print(Fore.YELLOW + f"\nID: {producto[0]}\nNombre: {producto[1]}\nDescripción: {producto[2]}\nCantidad: {producto[3]}\nPrecio: ${producto[4]}\nCategoría: {producto[5]}")
    else:
        print(Fore.RED + "Producto no encontrado.")

def reporte_bajo_stock():
    print(Fore.CYAN + "\n[ Reporte de productos con bajo stock ]")
    limite = int(input("Ingrese el límite de cantidad: "))
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    productos = cursor.fetchall()
    if productos:
        for p in productos:
            print(Fore.YELLOW + f"ID: {p[0]}, Nombre: {p[1]}, Cantidad: {p[3]}")
    else:
        print(Fore.GREEN + "No hay productos con cantidad igual o menor al límite.")


#Menu del programa, donde se ejecutan las funciones elegidas.
def menu():
    while True:
        print(Fore.BLUE + Style.BRIGHT + "\n=== SISTEMA DE INVENTARIO ===")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Reporte bajo stock")
        print("7. Salir")

        opcion = input(Fore.WHITE + "\nSeleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            print(Fore.MAGENTA + "\nSaliendo del sistema... ¡Hasta luego!")
            break
        else:
            print(Fore.RED + "Opción no válida. Intente de nuevo.")



if __name__ == "__main__":
    menu()
    con.close()