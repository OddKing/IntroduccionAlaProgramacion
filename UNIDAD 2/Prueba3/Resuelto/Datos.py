#Carlos Campaña Diaz 18528298-8
#Ejercicio 1
#TI2011/V-IEI-N1-P1-C2/V La Granja IEI
def ValidadorValoresPositivos(positivo):
    if(positivo>=0):
        return True
    else:
        return False
    
def SolictusAsistentes():
    while True:
        try:
            can_personas=int(input("Ingrese la cantidad de personas que asistentes: "))
            if ValidadorValoresPositivos(can_personas):
                return can_personas
            
        except ValueError:
            print("Ingrese Valor numerico que sea positivo")


def SolicitudPrecioEntrada():
    while True:
        try:
            precio_entrada=int(input("Ingrese valor de la entrada: "))
            if ValidadorValoresPositivos(precio_entrada):
                return precio_entrada
        except ValueError:
            print("Ingrese Valor Valido!!")
