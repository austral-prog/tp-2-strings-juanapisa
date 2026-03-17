def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass

    precio = input("ingrese el precio ")
    precio_int = float(precio)
    print("Precio:", precio)

    descuento = input("ingrese descuento ")
    descuento_int = float(descuento)
    print("Descuento:",descuento)

    cantidad = input("ingrese la cantidad de entradas: ")
    cantidad_int = int(cantidad)

    precio_con_descuento = precio_int - descuento_int
    print("Precio con descuento:", precio_con_descuento)

    precio_sin_descuento = (precio_int * cantidad_int)
    total = precio_sin_descuento - (descuento_int * cantidad_int)
    print("Total:", total)
