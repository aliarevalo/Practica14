print('Hecho por Dimas Arevalo Alisson\ny Rivera Olivares Arely')
print('Programa de base de datos')
print('Nombre de la empresa: ALLYRE BEAUTY')
contraseña = ""
while contraseña != "12345":
    contraseña = input("Introduce la contraseña: ")
print("Contraseña correcta!")
base_datos = []
def menu():
    print("\n=== Menú Principal ===")
    print("1. Agregar (Insertar/Alta)")
    print("2. Consultar (Mostrar)")
    print("3. Modificar (Editar)")
    print("4. Eliminar (Borrar)")
    print("5. Salir del programa")
def agregar():
    print("\n=== Agregar Producto ===")
    producto = {}
    producto["Producto"] = input("Nombre del producto: ")
    producto["Duracion"] = input("Duracion: ")
    producto["Formula"] = input("Formula: ")
    producto["Resistencia"] = input("Resistencia: ")
    producto["Cobertura"] = input("Cobertura: ")
    producto["Variedad de tonos"] = input("Numero de tonos: ")
    producto["Textura"] = input("Textura: ")
    producto["Ideal para"] = input("Ideal para el tipo de piel: ")
    producto["Acabado"] = input("Acabado: ")
    producto["Libre de comedogenos"] = input("Libre de comedogenos: ")
    producto["Precio"] = input("Precio: ")
    base_datos.append(producto)
    print("Producto agregado exitosamente.")
def consultar():
    if not base_datos:
        print("\nLa base de datos está vacía.")
        return
    print("\n=== Productos en la Base de Datos ===")
    for i, producto in enumerate(base_datos, start=1):
        print(f"{i}. {producto}")
def modificar():
    consultar()
    if not base_datos:
        return
    index = int(input("\nIngrese el número del producto que desea modificar: ")) - 1
    if 0 <= index < len(base_datos):
        print("\n=== Modificar Producto ===")
        print("Deje en blanco para mantener el valor actual.")
        producto = base_datos[index]
        producto["Producto"] = input(f"Nombre del producto ({producto['Producto']}): ") or producto["Producto"]
        producto["Duracion"] = input(f"Duracion ({producto['Duracion']}): ") or producto["Duracion"]
        producto["Formula"] = input(f"Formula ({producto['Formula']}): ") or producto["Formula"]
        producto["Resistencia"] = input(f"Resistencia ({producto['Resistencia']}): ") or producto["Resistencia"]
        producto["Cobertura"] = input(f"Cobertura ({producto['Cobertura']}): ") or producto["Cobertura"]
        producto["Variedad de tonos"] = input(f"Numero de tonos ({producto['Variedad de tonos']}): ") or producto["Variedad de tonos"]
        producto["Textura"] = input(f"Textura ({producto['Textura']}): ") or producto["Textura"]
        producto["Ideal para"] = input(f"Ideal para el tipo de piel ({producto['Ideal para']}): ") or producto["Ideal para"]
        producto["Acabado"] = input(f"Acabado ({producto['Acabado']}): ") or producto["Acabado"]
        producto["Libre de comedogenos"] = input(f"Libre de comedogenos ({producto['Libre de comedogenos']}): ") or producto["Libre de comedogenos"]
        producto["Precio"] = input(f"Precio ({producto['Precio']}): ") or producto["Precio"]
        print("Producto modificado exitosamente.")
    else:
        print("Número inválido.")
def eliminar():
    consultar()
    if not base_datos:
        return
    index = int(input("\nIngrese el número del producto que desea eliminar: ")) - 1
    if 0 <= index < len(base_datos):
        eliminado = base_datos.pop(index)
        print(f"Producto eliminado: {eliminado}")
    else:
        print("Número inválido.")
while True:
    menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        agregar()
    elif opcion == "2":
        consultar()
    elif opcion == "3":
        modificar()
    elif opcion == "4":
        eliminar()
    elif opcion == "5":
        print("Fin del programa.")
        break
    else:
        print("Opción inválida. Intente nuevamente.")

