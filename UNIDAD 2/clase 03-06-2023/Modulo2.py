from Modulo1 import Atrasados
def suma(parametro):
    contador=0
    while True:
        if parametro==0:
            break
        a = int(input('Ingrese un valor para a: '))
        b = int(input('Ingrese un valor para b: '))
        resultado= a+b

        print('Aca se resuelve a + b, cual cree que es el resultado?')
        respuesta = int(input('Ingrese la respuesta: '))

        if resultado==respuesta:
            print('Correcoto!!!!!!')
        else:
            print('Erroooooooooooor!!!! T.T')
        contador+=1

        if contador==parametro:
            break
        


suma(Atrasados())