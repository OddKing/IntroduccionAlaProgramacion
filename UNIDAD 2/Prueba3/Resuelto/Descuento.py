#Carlos Campaña Diaz 18528298-8
#Ejercicio 1
#TI2011/V-IEI-N1-P1-C2/V La Granja IEI
#se crea moduko que calcule el precio
import Datos
def descuentoEntrada(cantidad,valorEntrada):
    #Se calcula los descuntos
    try:
        i=0
        con_bronce=0
        con_plata=0
        con_gold=0
        con_platinium=0
        while i<cantidad:
            edad=int(input("Ingrese la edad del aistente N°{} :".format(i+1)))
            #print(Datos.ValidadorValoresPositivos(edad) )
            if(Datos.ValidadorValoresPositivos(edad) and edad >= 6):
                i+=1
                if edad>=6 and edad<=17:
                    con_bronce+=1
                elif edad>=18 and edad<=27:
                    con_plata+=1 
                elif edad>=28 and edad<=49:
                    con_gold+=1
                else:
                    con_platinium+=1
            else:
                print("Ingrese valor valido")

    except ValueError:
        print("Ingrese valor valido")
    else:
        ganado_bronce=(con_bronce*valorEntrada)*0.75
        ganado_plata=(con_plata*valorEntrada)*0.78
        ganado_gold=(con_gold*valorEntrada)*0.89
        ganado_platinium=(con_platinium*valorEntrada)*0.45

        print(" Lo que se gano con la categoria bronce es: ${} \n Lo que se gano con la categoria plata es: ${} \n Lo que se gano con la categoria gold es: ${} \n Lo que se gano con la categoria Platinum es: ${} \n".format(ganado_bronce,ganado_plata,ganado_gold,ganado_platinium))
