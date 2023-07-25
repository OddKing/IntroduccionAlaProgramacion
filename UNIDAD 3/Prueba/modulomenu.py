#[Carlos Campaña][18528298-8]
#[Ejercicio 1]
#[TI2011/V-IEI-N1-P1-C2/V La Granja IEI]
def menu():
    try:
        print("Hola Bienvenido  al menu del aprueba EVA4")
        print("aqui puede selecionar a que ejercio entrar:")
        print("1.- El ejercio del traga moneadas")
        print("2.- El Ejecicio 2 traza de 2 array")
        print("3.- Salir")
        op=int(input("ingrese la opcion que quiere ingresar: "))
        if valdiarOpcion(op):
            return op
    except ValueError or not valdiarOpcion(op):
        print("Ingres un valor numerico valido ")


    
def valdiarOpcion(op):
    if op==1 or op == 2 or op== 3:
        return True
    else:
        return False