import os
from pathlib import Path, PureWindowsPath
from shutil import rmtree


def pregunta():
    confirmar = input("Desea Eliminar Otro? Y/N: ").lower()
    while confirmar != "n":
        if confirmar == "y":
            eliminar_categoria()
        else:
            print("Opcion Invalida pruebe otra vez:")
            confirmar = input("Desea Eliminar Otro? Y/N: ").lower()



def leer_recetas():
    global cantidad
    name_receta = []
    print("===============================")
    print(" Leer Recetas")
    print("===============================")
    print("""
            Elige Categoria
                [1] Carnes
                [2] Ensaladas
                [3] Pastes
                [4] Postres
                [5] Volver al menu Principal
        """)
    opc = int(input("Digite Una Opcion: "))

    if opc == 1:
        print("""
    ======================
            Carnes
    ======================
        """)
        recetas = os.listdir("Recetas/Carnes/")
        # Listar el contenido Carpeta
        num = 0

        for lista in recetas:
            print(f"""{num}.- Receta de {lista}
            """)
            num = num + 1
            name_receta.append(lista)
            cantidad = len(name_receta)
        leer = int(input("Cual Desea Leer?: "))
        if leer <= cantidad:
            datos = name_receta[leer]
            print(f"La receta: {datos}")
            ruta = Path("Recetas/Carnes/") / datos
            archivo = open(ruta, "r")
            print(archivo.read())
            os.system("pause")
            archivo.close()
        else:
            print("Invalida")
    elif opc == 2:
        print("""
        ======================
             Ensaladas
        ======================
                """)
        recetas = os.listdir("Recetas/Ensaladas/")
        # Listar el contenido Carpeta
        num = 0

        for lista in recetas:
            print(f"""{num}.- Receta de {lista}
                    """)
            num = num + 1
            name_receta.append(lista)
            cantidad = len(name_receta)
        leer = int(input("Cual Desea Leer?: "))
        if leer <= cantidad:
            datos = name_receta[leer]
            print(f"La receta: {datos}")
            ruta = Path("Recetas/Ensaladas/") / datos
            archivo = open(ruta, "r")
            print(archivo.read())
            os.system("pause")
            archivo.close()
        else:
            print("Invalida")
    elif opc == 3:
        print("""
        ======================
                Pastas
        ======================
                """)
        recetas = os.listdir("Recetas/Pastas/")
        # Listar el contenido Carpeta
        num = 0
        for lista in recetas:
            print(f"""{num}.- Receta de {lista}
                    """)
            num = num + 1
            name_receta.append(lista)
            cantidad = len(name_receta)
        leer = int(input("Cual Desea Leer?: "))
        if leer <= cantidad:
            datos = name_receta[leer]
            print(f"La receta: {datos}")
            ruta = Path("Recetas/Pastas/") / datos
            archivo = open(ruta, "r")
            print(archivo.read())
            os.system("pause")
            archivo.close()
        else:
            print("Invalida")
    elif opc == 4:
        print("""
        ======================
                Postres
        ======================
                """)
        recetas = os.listdir("Recetas/Postres/")
        # Listar el contenido Carpeta
        num = 0
        for lista in recetas:
            print(f"""{num}.- Receta de {lista}
                    """)
            num = num + 1
            name_receta.append(lista)
            cantidad = len(name_receta)
        leer = int(input("Cual Desea Leer?: "))
        if leer <= cantidad:
            datos = name_receta[leer]
            print(f"La receta: {datos}")
            ruta = Path("Recetas/Postres/") / datos
            archivo = open(ruta, "r")
            print(archivo.read())
            os.system("pause")
            archivo.close()
        else:
            print("Invalida")
    elif opc == 5:
        main()
    else:
        print("Opcion Invalida")


def crear_receta():
    os.system("cls")
    print("===============================")
    print("Categorias")
    print("===============================")
    print("""
                Elige Categoria
                    [1] Carnes
                    [2] Ensaladas
                    [3] Pastes
                    [4] Postres
                    [5] Volver al menu Principal
            """)
    opc = int(input("Digite Una Opcion: "))
    if opc == 1:
        print("""
    ======================================
        Creando Nueva Receta de Carnes
    ======================================
        """)
        # rutas
        recetas = Path("Recetas/Carnes/")
        nueva_receta = input("Digite el nombre de la nueva receta: ")
        receta_nueva = recetas / nueva_receta
        # Creamos el File
        file = open(receta_nueva, "w")
        # escribimos en el file
        file.write(input("Escriba Receta: "))
        file.close()
        print("Receta Creada.....")


    elif opc == 2:
        print("""
    ========================================
         Creando Nueva Receta de Ensaladas
    ========================================
            """)
        # rutas
        recetas = Path("Recetas/Ensaladas/")
        nueva_receta = input("Digite el nombre de la nueva receta: ")
        receta_nueva = recetas / nueva_receta
        # Creamos el File
        file = open(receta_nueva, "w")
        # escribimos en el file
        file.write(input("Escriba Receta: "))
        file.close()
        print("Receta Creada.....")

    elif opc == 3:
        print("""
    =====================================
          Creando Nueva Receta de Pastas
    ======================================
            """)
        # rutas
        recetas = Path("Recetas/Pastas/")
        nueva_receta = input("Digite el nombre de la nueva receta: ")
        receta_nueva = recetas / nueva_receta
        # Creamos el File
        file = open(receta_nueva, "w")
        # escribimos en el file
        file.write(input("Escriba Receta: "))
        file.close()
        print("Receta Creada.....")

    elif opc == 4:
        print("""
    ===========================================
           Creando Nueva Receta de Postres
    ===========================================
            """)
        # rutas
        recetas = Path("Recetas/Postres/")
        nueva_receta = input("Digite el nombre de la nueva receta: ")
        receta_nueva = recetas / nueva_receta
        # Creamos el File
        file = open(receta_nueva, "w")
        # escribimos en el file
        file.write(input("Escriba Receta: "))
        file.close()
        print("Receta Creada.....")

    elif opc == 5:
        return main()
    else:
        print("Opcion Invalida")


def crear_categoria():
    print("""
    =================================
        Crear Nueva Categoria
    =================================
    """)
    # rutas
    base = Path("Recetas/")
    nueva_categoria = input("Digite el nombre de la nueva categoria: ")
    categoria_nueva = base / nueva_categoria
    # Creamos el directorio
    os.makedirs(categoria_nueva)
    print("Se ha creado correctamente el Directorio " + nueva_categoria)
    """ Se Oculta listar
    recetas = os.listdir("Recetas/")
    # Listar el contenido Carpeta
    num = 1
    for lista in recetas:
        #print(f\n{num}.- Receta de {lista})
        num = num + 1
    """
    os.system("pause")
    return main()


def eliminar_receta():
    print("""
    ==========================
        Eliminar Receta
    ==========================
    """)
    # muestra Categorias
    recetas = os.listdir("Recetas/")
    num = 1
    print("Primero seleccione una de las siguientes Categorias: ")
    for lista in recetas:
        print(f"{num}.- Categoria de {lista}")
        num = num + 1
    opc = int(input("Seleccione Categoria: "))
    if opc == 1:
        print("""
    ======================
            Carnes
    ======================
        """)
        recetas = os.listdir("Recetas/Carnes/")
        # Listar el contenido Carpeta
        num = 0
        valor = []
        for lista in recetas:
            print(f"""{num}.- Receta de {lista}""")
            valor.append(lista)
            num = num + 1
        cant_recetas = len(recetas)

        delete_receta = int(input("Que receta desea Eliminar: "))
        if delete_receta <= cant_recetas:
            eliminar = valor[delete_receta]
            print(f"selecionaste la numero {delete_receta}.- {eliminar}")
            borrar = Path("Recetas/Carnes/") / eliminar
            print(borrar)
            os.remove(borrar)
            print("Archivo Eliminado")
            os.system("pause")
            return main()
        else:
            print("Opcion Invalida")
    elif opc == 2:
        print("""
    ======================
         Ensaladas
    ======================
                """)
        recetas = os.listdir("Recetas/Ensaladas/")
        # Listar el contenido Carpeta
        num = 0
        valor = []
        for lista in recetas:
            print(f"""{num}.- Receta de {lista}""")
            valor.append(lista)
            num = num + 1
        cant_recetas = len(recetas)

        delete_receta = int(input("Que receta desea Eliminar: "))
        if delete_receta <= cant_recetas:
            eliminar = valor[delete_receta]
            print(f"selecionaste la numero {delete_receta}.- {eliminar}")
            borrar = Path("Recetas/Ensaladas/") / eliminar
            print(borrar)
            os.remove(borrar)
            print("Archivo Eliminado")
            os.system("pause")
            return main()
        else:
            print("Opcion Invalida")
    elif opc == 3:
        print("""
    ======================
        Pastas
    ======================
                """)
        recetas = os.listdir("Recetas/Pastas/")
        # Listar el contenido Carpeta
        num = 0
        valor = []
        for lista in recetas:
            print(f"""{num}.- Receta de {lista}""")
            valor.append(lista)
            num = num + 1
        cant_recetas = len(recetas)

        delete_receta = int(input("Que receta desea Eliminar: "))
        if delete_receta <= cant_recetas:
            eliminar = valor[delete_receta]
            print(f"selecionaste la numero {delete_receta}.- {eliminar}")
            borrar = Path("Recetas/Pastas/") / eliminar
            print(borrar)
            os.remove(borrar)
            print("Archivo Eliminado")
            os.system("pause")
            return main()
        else:
            print("Opcion Invalida")
    elif opc == 4:
        print("""
    ======================
            Postres
    ======================
                """)
        recetas = os.listdir("Recetas/Postres/")
        # Listar el contenido Carpeta
        num = 0
        valor = []
        for lista in recetas:
            print(f"""{num}.- Receta de {lista}""")
            valor.append(lista)
            num = num + 1
        cant_recetas = len(recetas)

        delete_receta = int(input("Que receta desea Eliminar: "))
        if delete_receta <= cant_recetas:
            eliminar = valor[delete_receta]
            print(f"selecionaste la numero {delete_receta}.- {eliminar}")
            borrar = Path("Recetas/Postres/") / eliminar
            print(borrar)
            os.remove(borrar)
            print("Archivo Eliminado")
            os.system("pause")
            return main()
        else:
            print("Opcion Invalida")
    elif opc == 5:
        return main()
    else:
        print("Opcion Invalida")


def eliminar_categoria():
    print("""
    ==========================
        Eliminar Categoria
    ==========================
    """)
    # muestra Categorias
    categoria = os.listdir("Recetas/")
    num = 0
    print("Primero seleccione una de las siguientes Categorias: ")
    valor = []
    for lista in categoria:
        print(f"""{num}.- Categoria de {lista}""")
        valor.append(lista)
        num = num + 1
    cant_recetas = len(categoria)
    delete_categoria = int(input("Que Categoria desea Eliminar: "))
    if delete_categoria <= cant_recetas:
        eliminar = valor[delete_categoria]
        print(f"selecionaste la numero {delete_categoria}.- {eliminar}")
        borrar = Path("Recetas/") / eliminar
        print(borrar)
        rmtree(borrar)
        print("Archivo Eliminado")
        pregunta()

    else:
        print("Opcion Invalida")


def main():
    os.system("cls")

    opc = 0
    while opc != 6:
        print("===========================")
        print(f"Bienvenido al Recetario:")
        print("""
               ****Menu Principal****
               Por favor selecciona una opcion:
               [1] - Leer receta
               [2] - Crear receta
               [3] - Crear Categoria
               [4] - Eliminar Receta
               [5] - Eliminar Categoria
               [6] - Finalizar Programa
           """)
        print("===========================")
        opc = int(input("Seleccione una opcion: "))

        if opc == 1:
            leer_recetas()
        elif opc == 2:
            crear_receta()
        elif opc == 3:
            crear_categoria()
        elif opc == 4:
            eliminar_receta()
        elif opc == 5:
            eliminar_categoria()
        elif opc == 6:
            print("Muchas Gracias")
            break
        else:
            print("Opcion Invalida Intenta nuevamente")


main()