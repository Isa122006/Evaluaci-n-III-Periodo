from services.inventario import actualizar_nombre

def actualizar_nombre():
    nombre_actual = input("Ingrese el nombre actual del producto: ")
    nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
    actualizar_nombre(nombre_actual, nuevo_nombre)
    print(f"Nombre del producto actualizado de '{nombre_actual}' a '{nuevo_nombre}'.")