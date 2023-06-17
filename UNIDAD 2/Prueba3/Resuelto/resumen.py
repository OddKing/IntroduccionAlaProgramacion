#Carlos Campaña Diaz 18528298-8
#Ejercicio 1
#TI2011/V-IEI-N1-P1-C2/V La Granja IEI
import Ejercicio1
import Ejercicio1b
import Ejercicio2


while True:
    try:
        print("Menu para ingreso a los ejercicios ")
        print("Si quiere ingresar a :")
        print("1- Ejercicio 1 _ temperatura")
        print("2- Ejercicio 2 _ Calcular ganancia cine")
        print("0- Salir")
        op=int(input(""))
        if(op==1):
            Ejercicio1.IngresoTemperaturadia()
        elif op==2:
            Ejercicio2.inicio()
        elif op==0:
            break
        else:
            print("ingrese opcion valida")
    except ValueError:
        print("Ingrese Opcion valida")

