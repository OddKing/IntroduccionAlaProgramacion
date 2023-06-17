import modulopromedio

nota1 = float(input('Ingrese nota 1: '))
nota2 = float(input('Ingrese nota 2: '))
nota3 = float(input('Ingrese nota 2: '))
suma=nota1+nota2+nota3

print(modulopromedio.promedio(suma))#Recibe 1 parametro
print(modulopromedio.promedio2(nota1,nota2,nota3))#recibe 3 parametros
print(modulopromedio.promedio3())#solicita los parametros
