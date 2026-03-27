def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    pass

    base = int(input("Base de un rectangulo: "))
    altura = int(input("Altura del rectangulo: "))
    area = base * altura
    print("Area:", area)
    perimetro = (base + altura) * 2
    print("Perimetro:",perimetro)
