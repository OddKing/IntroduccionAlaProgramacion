import numpy as np

datos=np.array([])

n=0

for i in range(0,3):
    x=input('Ingrese: ')
    datos=np.append(datos,x)

for i in range(0,1):
    print(datos)

while n<3:
    x=input('Ingrese: ')
    datos=np.append(datos,x)
    n=n+1
    
for i in range(0,2):
    print(datos)