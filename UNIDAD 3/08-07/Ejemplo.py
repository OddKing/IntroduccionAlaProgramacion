#dato de frutas
#tipos de frutas
#color de fruta
#cantidad de frutas

listaFruta=[]

while True:
    print('\nMenus')
    print('1.- Ingresa Frutas: ')
    print('2.- Mostrar frutas: ')
    print('3.- Eliminar frutas por posicion: ')
    print('4.- Eliminar fruta con remove: ')
    print('5.- Eliminar frutas con pop: ')

    op=input('Seleccione una opcion: ')

    if op == '1':
        opcion=int(input('Cuantas frutas colocara en la canasta? '))
        for i in range(opcion):
            tipo = input('Ingrese un valor para tipo: ')
            color= input('Ingrese un valro para color: ')
            cantidad= input('Ingrese un valor para cantidad: ')

            listaFruta.append([tipo,color,cantidad])

    elif op == '2':
        print('en la canastas hay: ',listaFruta)

        for i in listaFruta:
            print(f'tipod de fruta : {i[0]} \nColor: {i[1]} \nCantidad:{i[2]} \n')
        
        for i in listaFruta:
            print(" ")
            for j in i:
                print(j)


    elif op == '3':
        print('vamos a eliminar  valores: ')
        for i,j in enumerate(listaFruta):
            print('Posicion: ',i, ' Valor: ',j)
        
        opcion1= int(input('que posicion desea eliminar ? '))
        listaFruta.pop(opcion1)

    elif op=='4':
        print("eliminar por tipo de fruta")
        print("frutas disponibles: " )

        for i in listaFruta:
            print(i[0])
        
        valorEliminar= input(' que fruta desea eliminar? ')

        for i in listaFruta:
            if i[0] == valorEliminar:
                listaFruta.remove(i[0],i[1],i[2])
                print(listaFruta)

    elif op=='5':
        print('borrar con pop por tipo de fruta:')
        valorEliminar= input('que fruta desea eliminar? ')

        for i in range(len(listaFruta)):
            if listaFruta[i][0]== valorEliminar:
                listaFruta.pop(i)
                print(listaFruta)
                break
    