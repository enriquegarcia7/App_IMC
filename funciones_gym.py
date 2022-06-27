

def calcular_imc(peso, estatura):
    imc=peso/estatura**2
    return round(imc, 2)

def clasificar_imc(imc):
    if imc <=16:
        clasificacion = "Delgadez Severa"
    elif 16<=imc <=16.99:
        clasificacion = "Delgadez moderada"
    elif 17<=imc <=18.49:
        clasificacion = "Delgadez aceptable"
    elif 18.50<=imc <=24.99:
        clasificacion = "Peso Normal"
    elif 25<=imc <=29.99:
        clasificacion = "Sobre Peso"
    elif 30<=imc <=34.99:
        clasificacion = "Obeso Tipo I"
    elif 35<=imc <=40:
        clasificacion = "Obeso tipo II"
    else:
        clasificacion = "Obeso tipo III"
    
    return (clasificacion)
def imprimir_datos(nombre, clasificacion, edad, peso, estatura, imc):
    print(f''' 
    ================TICKET==================
    \tNombre:{nombre} \t \t Edad:{edad}\t 
    \tPeso:{peso} \t \t Altura:{estatura}\t
    \tIMC: {imc} \t \t Clasificación:{clasificacion}
    ''')