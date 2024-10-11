from services.inventario import actualizar_precio

def actualizar_precio():
    nombre = input("Ingrese el nombre del producto: ")
    nuevo_precio = float(input("Ingrese el nuevo precio: "))
    actualizar_precio(nombre, nuevo_precio)
    print(f"Precio del producto '{nombre}' actualizado a {nuevo_precio}.")
