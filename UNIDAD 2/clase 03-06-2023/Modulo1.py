#Contar la cantidad de alumnos atrasados en la clase
#En cleses el ciclo fue con un while para que funcione con while hay que comentar la linea 10 - 12 -18 y descomentar 9 - 11 - 19 - 23 - 25 - 26 - 27
from mates import castigo
curso = 10
contador=0
contador_curso=0

#while True:
for i in range(curso):
    #cantidad=input("El Alumno  llego atrasado? (S/N)")
    cantidad=input("El Alumno {} llego atrasado? (S/N)".format(i+1))
    cantidad= cantidad.upper().strip()
    while True:
        if cantidad =='S' or cantidad=='N':
            break
        else:
            cantidad=input("El Alumno {} llego atrasado? (S/N) ".format(i+1))
            #cantidad=input("El Alumno  llego atrasado? (S/N)")
            cantidad= cantidad.upper().strip()

    if(cantidad == 'S'):
        contador+=1
        

#    contador_curso+=1
#    if contador_curso == curso:
#        break


print("los atrasados son: ",contador)
print("los puntuales :",curso-contador)
print("el total del curso: ",curso)

castigo(contador)