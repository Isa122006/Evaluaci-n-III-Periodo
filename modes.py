from modes.agregar_producto import agregar_producto
from modes.eliminar_producto import eliminar_producto
from modes.mostrar_inventario import mostrar_inventario
from modes.mostrar_valor_total import mostrar_valor_total
from modes.actualizar_nombre import actualizar_nombre
from modes.actualizar_cantidad import actualizar_cantidad
from modes.actualizar_precio import actualizar_precio

def mostrar_menu():
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar inventario")
        print("4. Mostrar valor total del inventario")
        print("5. Actualizar nombre de producto")
        print("6. Actualizar cantidad de producto")
print("7. Actualizar precio de producto")
print("8. Salir")

opcion = input("Seleccione una opción: ")
if opcion == '1':
            agregar_producto()
elif opcion == '2':
 eliminar_producto()
elif opcion == '3':
    mostrar_inventario()
elif opcion == '4':
    mostrar_valor_total()
elif opcion == '5':
            actualizar_nombre()
elif opcion == '6':
            actualizar_cantidad()
elif opcion == '7':
            actualizar_precio()
elif opcion == '8':
            print("Saliendo del sistema.")
            'break'
else:
 print("Opción no válida. Intente de nuevo.")






        