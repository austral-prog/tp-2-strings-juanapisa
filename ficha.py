from idlelib.replace import replace
from itertools import count
from urllib.parse import uses_query


def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass

    titulo = """=======================================
    FICHA DEL ALUMNO
    ======================================="""
    print(titulo)
    nombre= input("Nombre:").title()
    print(nombre)
    mail = input("mail: ").lower()
    print(mail)
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))
    print("Caracteres en nombre:",len(nombre))
    inicial_nombre = nombre[0]
    espacio = nombre.find(" ")
    ini_apellido = nombre[espacio + 1]
    print("Iniciales:",inicial_nombre,ini_apellido)
    usuario = print(f"Usuario:{nombre.lower()[0:espacio]}.{nombre.lower()[espacio+1:-1]}")
    arroba = "@" in mail
    print("Email valido:",arroba)
    dominio = mail[arroba + 1 : -1]
    print("Dominio:",dominio)
    print("Nombre para archivo:", nombre.replace(" ", "_"))
    print("Cantidad de a:",nombre.count('a'))
    print("Codigo secreto: AICRAG AIRAM")
    print("Nota1:",nota1)
    print("Nota2:",nota2)
    print("Nota3:",nota3)
    suma = nota1 + nota2 + nota3
    print("Suma:",suma)
    promedio = suma / 3
    print(promedio)
    print(int(promedio))
