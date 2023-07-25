#[Carlos Campaña][18528298-8]
#[Ejercicio 1]
#[TI2011/V-IEI-N1-P1-C2/V La Granja IEI]
import Ejercicio1a


def Tragamoneda():
    lista_fruta=["Plátano", "Limón", "Manzana", "Pera", "Uva","Frutilla"]
    lista_resultado=[]
    while True:
        try:
            #print("ingresa la cantidad de creditos que va jugar:")
            creditos=int(input("ingrese los creditos que va jugar: "))
        except ValueError:
            print("ingrese valor valido!!!(numero entero)")
        else:
            break

    while True:
        lista_resultado=[]
        if Ejercicio1a.validarCreditos(creditos):
            for i in range(3):
                lista_resultado=Ejercicio1a.lanzamiento(creditos, lista_fruta)
    
            creditos=Ejercicio1a.descontarCreditos(creditos)
            if Ejercicio1a.revisarLista(lista_resultado):
                print("Usted a ganado el premio mayor sus creditos se han multiplicado por 100")
                creditos=Ejercicio1a.granpremio(creditos)
                print("el resultado fue {}".format(lista_resultado))
                print("sus creditos son {}.".format(creditos))
            else:
                print("para proxima siga participando !!!! la proxima puedes ganar :D")
                print("el resultado fue {}".format(lista_resultado))
                print("sus creditos son {}.".format(creditos))
        else:
            print("Te quedaste sin creditos gracias por participar")
            print("Gracias por participar!!!!!")
            break
#aqui se testio el traga monedas 
#Tragamoneda()