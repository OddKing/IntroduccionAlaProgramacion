#Carlos Campaña Diaz 18528298-8
#Ejercicio 1
#TI2011/V-IEI-N1-P1-C2/V La Granja IEI

def IngresoTemperaturadia():
    #se crea la solicitud de las de los datos correctos
    #ingresa variable
    tem=[]
    numero_dia=0
    tem_max=0
    suma_tem=0
    prom_tem=0
    i=0
    while True:
        try:
            while i<7:
                auxtem=float(input("Ingrese la temperatura del dia {}:".format(i+1)))
                #se valdia que la temperatura este dentro de los limites
                if(auxtem<-273):
                    print("ingrese valor valido")
                else:
                    tem.append(auxtem)
                    i+=1
                print
                suma_tem+=auxtem
           
        except ValueError:
            print ("Ingres un temperatura valida")
        else:
            a=1
            for j in tem:
                print("La temperatura del dia {} es de {} ° Celsius".format(a,j))
                a+=1

            prom_tem=suma_tem/7
            print("La temperatura promedio es de {:.2f} ° Celsisus en la semana".format(prom_tem))
            break
    
