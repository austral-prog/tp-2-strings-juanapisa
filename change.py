def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass

    print("Ingresar gasto:")
    gasto = float(input(""))
    print(gasto)

    print("Dinero recibido")
    dinero_recibido = int(input(""))
    print(dinero_recibido)

    print()
    print("Vuelto")
    print()

    vuelto = dinero_recibido - gasto
    vuelto_pesos = int(vuelto)
    print(f"Pesos:\n{vuelto_pesos}")

    vuelto_centavos = round((vuelto - vuelto_pesos)*100)
    print(f"Centavos:\n{vuelto_centavos}")

