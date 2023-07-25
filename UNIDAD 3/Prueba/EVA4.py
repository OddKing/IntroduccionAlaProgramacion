#[Carlos Campaña][18528298-8]
#[Ejercicio 1]
#[TI2011/V-IEI-N1-P1-C2/V La Granja IEI]
import ejercicio1;
import ejercicio2;
import modulomenu

while True:
    #se genera un menu para entrar a los diferentes ejercicio y se crea un modulo
    opcion=modulomenu.menu()
    if opcion==3:
        break
    elif opcion==2:
        ejercicio2.CalculoDeTraceArray()
    elif opcion==1:
        ejercicio1.Tragamoneda()
