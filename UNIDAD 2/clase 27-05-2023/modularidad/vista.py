import modulo1 
import modulo2
from modulo3 import resta,mutiplicacion


while True:
    print('Menu')
    print('1.- Suma')
    print('2.- Saludo')
    print('3.- Resta')
    print('4.- multiplicacion')
    print('5.- Salir')
    op=input('Ingrese una opcion: ')

    if op == '1':
        try:
            print('Accedio a sumar')
            a=int(input('ingrese un numero:'))
            b=int(input('ingrese otro numero:'))
        except (ValueError, TypeError) :
            print('No ingrese valores distibntos de numeros XD')
        else:
            print(modulo1.suma2(a,b))
    elif op =='2':
        modulo2.saludo('')
    elif op == '3':
        print (resta(5,2))
    elif op=='4':
        print(mutiplicacion(5,6))
    elif op == '5':
        print('Adios!!')
        break
    else:
        print("ingre una opcion valida logi")