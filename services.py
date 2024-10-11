inventario = {}

def agregar_producto(nombre, cantidad, precio):
    inventario[nombre] = {'cantidad': cantidad, 'precio': precio}

def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]

def mostrar_inventario():
    for nombre, detalles in inventario.items():
        print(f"Producto: {nombre}, Cantidad: {detalles['cantidad']}, Precio: {detalles['precio']}")

def mostrar_valor_total():
    total = sum(detalles['cantidad'] * detalles['precio'] for detalles in inventario.values())
    print(f"Valor total del inventario: {total}")

def actualizar_nombre(nombre_actual, nuevo_nombre):
    if nombre_actual in inventario:
        inventario[nuevo_nombre] = inventario.pop(nombre_actual)

def actualizar_cantidad(nombre, nueva_cantidad):
    if nombre in inventario:
        inventario[nombre]['cantidad'] = nueva_cantidad

def actualizar_precio(nombre, nuevo_precio):
    if nombre in inventario:
        inventario[nombre]['precio'] = nuevo_precio