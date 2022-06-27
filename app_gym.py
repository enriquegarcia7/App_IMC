import os
import numpy as np
import funciones_gym as fg

#-------------------VARIABLES-------------------
opcion_menu=""
tamaño=3
nombres=np.empty(tamaño, dtype=object)
edades=np.empty(tamaño, dtype=int)
pesos=np.empty(tamaño, dtype=int)
estaturas=np.empty(tamaño, dtype=float)
imcs=np.empty(tamaño, dtype=float)
clasificaciones=np.empty(tamaño, dtype=object)

#------------------CÓDIGO PRINCIPAL-----------------
while True:
    os.system("cls")
    opcion_menu=str(input('''
    ================APP GYM========================
    1.- Cargar datos y ver IMC
    2.- Listar usuario por sobre lo normal
    3.- Nombre e IMC del Max. Valor Registrado
    4.- Salir
    Elija una Opción:   '''))

    if opcion_menu == "1":
        os.system("cls")
        print("\n============CARGAR DATOS==============")
        for k in range(tamaño):
            nombres[k]=str(input("Ingrese nombre: ")).strip().capitalize()
            while not len(nombres[k])>0:
                print("Error no puede estar vacío")
                nombres[k]=str(input("Ingrese nombre: ")).strip()

            edades[k]=int(input("Ingrese Edad: "))
            while not (edades[k])>0:
                print("Error no puede estar vacío")
                edades[k]=int(input("Ingrese Edad: "))

            pesos[k]=int(input("Ingrese peso Kg: "))
            while not (pesos[k])>0:
                print("Error no puede estar vacío")
                pesos[k]=str(input("Ingrese peso Kg: "))

            estaturas[k]=float(input("Ingrese estatura: "))
            while not (estaturas[k])>0:
                print("Error no puede estar vacío")
                estaturas[k]=float(input("Ingrese estatura: "))
            imcs[k]=fg.calcular_imc(pesos[k], estaturas[k])
            clasificaciones[k]=fg.clasificar_imc(imcs[k])
            fg.imprimir_datos(nombres[k], clasificaciones[k], edades[k], pesos[k], estaturas[k], imcs[k])

            os.system("pause")

    if opcion_menu == "2":
        os.system("cls")
        print("\n============= USUARIOS POR SOBRE LO NORMAL ================")
        for k in range(tamaño):
            if imcs[k]>=25:
                print(f'''
                Nombre: {nombres[k]}  \t Clasificación: {clasificaciones[k]} 
                ''')
    
        os.system("pause")

    if opcion_menu == "3":
        os.system("cls")
        print("\n=================MAX IMCS==================")
        max_imc=imcs.max()
        for k in range (tamaño):
            if imcs[k] == max_imc:
                print(f'''
                Nombre: {nombres[k]} \t IMC: {imcs[k]} 
                ''')

        os.system("pause")

    if opcion_menu == "4":
        os.system("cls")
        op = str(input(f'''
        Está seguro de salir(S/N): ''')).strip().upper()
        if op == "S":
            break
        else:
            continue

        os.system("pause")
