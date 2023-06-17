def promedio(promedios):
    resultado = promedios / 3
    return resultado

def promedio2(nota1,nota2,nota3):
    resultado= (nota1+nota2+nota3)/3
    return resultado

def promedio3():
    try:
        nota1 = float(input('Ingrese nota 1: '))
        nota2 = float(input('Ingrese nota 2: '))
        nota3 = float(input('Ingrese nota 2: '))
        resultado =(nota1+nota2+nota3)/3
    except ValueError:
        print("Solo Ingrese valores numericos")
    else:
        return resultado