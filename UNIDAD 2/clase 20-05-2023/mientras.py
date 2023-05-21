n = 1
num = 0.0
suma = 0.0

print("ingrese 5 numeros: ")

while n < 6:
    num = input(f"Numero {n}: ")
    num = float(num)
    suma = suma + num
    n = n + 1


print(f"El resultado de la suma es: {suma}")