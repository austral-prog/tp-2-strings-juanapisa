def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    

    base = int(input("Base de un rectangulo: "))
    print("Base:",base)
    altura = int(input("Altura del rectangulo: "))
    print("Altura:",altura)
    area = base * altura
    print("Area:", area)
    perimetro = (base + altura) * 2
    print("Perimetro:",perimetro)


