def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass

    precio = input("ingrese el precio ")
    precio_int = int(precio)
    print("Precio:", precio)
    descuento = input("ingrese descuento ")
    descuento_int = int(descuento)
    print("Decuento: ",descuento)
    cantidad = input("ingrese la cantidad de entradas que quiere ")
    cantidad_int = int(cantidad)
    calcular_descuento = precio_int * (descuento_int / 100)
    precio_con_descuento = precio_int - calcular_descuento
    print("Precio con descuento:", precio_con_descuento)
    calcular_total = (precio_int * cantidad_int)- calcular_descuento
    print("Total:", calcular_total)
