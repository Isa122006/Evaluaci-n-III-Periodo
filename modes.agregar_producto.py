from services.inventario import agregar_producto

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    agregar_producto(nombre, cantidad, precio)
    print(f"Producto '{nombre}' agregado al inventario.")