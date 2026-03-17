def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass

    precio = input("ingrese el precio ")
    precio_int = int(precio)
    print(precio)
    descuento = input("ingrese descuento ")
    descuento_int = int(descuento)
    print(descuento)
    cantidad = input("ingrese la cantidad de entradas que quiere ")
    cantidad_int = int(cantidad)
    calcular_descuento = precio_int * (descuento_int / 100)
    calcular_total = (precio_int * cantidad_int)- calcular_descuento
    print("tu total es:", calcular_total)
