lista=[]
lista2=[]


while True:
    a = input("Ingrese Valor lista 1: ")
    lista += [a] #lina 8 y linea 8 son lo mismo 
    #lista.append(a)

    b = input("Ingrese Valor lista 2: ")
    lista2 += [b] #lina 11 y linea 12 son lo mismo 
   #lista2.append(b)

    op= input("Desea Salir? s/n ")

    if op == 's':
        break


#imprimir cada elemento por seprado 
for i,j in zip(lista,lista2):
    print(i,' ',j)


#imprime la lista    
print(lista)