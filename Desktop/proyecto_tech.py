#@Author Matias Tomas Del Pup
#Programa hecho para la pre-entrega de Talento Tech
#Ya cuento con conocimientos en Python ya que estoy cursando Tecnicatura Universitaria en Programacion asi que aplique lo que ya conocia mas lo que vimos en las clases. Desde ya tenga buen dia y cualquier error me avisan :).

productos = []

#El menu que el usuario vera
def mostrar_menu():
    print("\nSistema de Gestión Básica De Productos")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

#Para agregar productos a la lista
def agregar_producto():
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacío.")

    
    while True:
        categoria = input("Ingrese la categoría del producto: ").strip()
        if categoria:
            break
        print("La categoría no puede estar vacía.")

    
    while True:
        precio_input = input("Ingrese el precio del producto (sin centavos): ").strip()
        if precio_input.isdigit():
            precio = int(precio_input)
            break
        print("El precio debe ser un número entero.")

    # Agregar a la lista
    productos.append([nombre, categoria, precio])
    print("Producto agregado con éxito.")

#Para mostrar productos en la lista
def mostrar_productos():
    if not productos:
        print("No hay productos registrados.")
        return
    print("\nLista de productos registrados: ")
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: ${producto[2]}")

#Para buscar productos en la lista
def buscar_producto():
    termino = input("Ingrese el nombre del producto: ").strip().lower()
    encontrados = []
    for producto in productos:
        if termino in producto[0].lower():
            encontrados.append(producto)
    if encontrados:
        print("\nProductos encontrados:")
        for i, prod in enumerate(encontrados, start=1):
            print(f"{i}. Nombre: {prod[0]}, Categoría: {prod[1]}, Precio: ${prod[2]}")
    else:
        print("No se encontraron productos con ese nombre.")

#Para eliminar productos de la lista
def eliminar_producto():
    mostrar_productos()
    if not productos:
        return
    while True:
        indice_input = input("Ingrese el número del producto a eliminar: ").strip()
        if not indice_input.isdigit():
            print("Debe ingresar un número válido.")
            continue
        indice = int(indice_input)
        if 1 <= indice <= len(productos):
            eliminado = productos.pop(indice - 1)
            print(f"Producto '{eliminado[0]}' eliminado con éxito.")
            break
        else:
            print("Número fuera de rango. Intente nuevamente.")

# Donde el usuario elije una opción
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ").strip()
    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        mostrar_productos()
    elif opcion == '3':
        buscar_producto()
    elif opcion == '4':
        eliminar_producto()
    elif opcion == '5':
        print("***********************************************")
        print("Gracias por usar el sistema. ¡Vuelva pronto :)!")
        print("***********************************************")
        break
    else:
        print("Por favor, elija una opción del 1 al 5.")
