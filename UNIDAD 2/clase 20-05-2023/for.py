num = 0.0
suma = 0.0

for n in range(1,6):
    num= input(f"numero {n} : ")
    num= float(num)

    suma=suma+num

print (f"El resultado de la suma es: {suma}")


palabra=input("ingrese una palabra para deletriar: ")

for x in palabra:
    print(x)

print("")