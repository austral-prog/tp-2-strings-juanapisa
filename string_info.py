def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"
    print("Palabra:",palabra)
    print("Longitud:", len("Programacion"))
    print("Primera Letra:", palabra[0])
    print("Ultima Letra:", palabra[-1])
    print("Retetida:", palabra*3)
    print("Decorada:", f" ***{palabra}***" )
