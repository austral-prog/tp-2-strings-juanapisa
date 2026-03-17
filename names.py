def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass
    nombre = input("ingresa tu nombre")
    apellido = input("ingresa tu nombre")
    print(nombre.lower(), apellido.lower())
    print(nombre.title(), apellido.title())
    print(nombre.upper(), apellido.upper())
    mensaje = f"\t{nombre.lower()} {apellido.lower()}"
    print(mensaje)
