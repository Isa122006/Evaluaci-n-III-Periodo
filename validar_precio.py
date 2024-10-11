def validar_precio(precio):
    if precio < 0:
        print("El precio no puede ser negativo.")
        return False
    return True