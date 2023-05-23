Algoritmo CalcularPrecioTotal
	Definir total Como Entero
	Definir valor1 Como Entero
	definir i Como Entero
	
	Para i <- 1 Hasta 10 Con Paso 1 Hacer
		escribir 'ingrese el valor del ',i, ' producto :'
		leer valor1
		total=total+valor1
		
	Fin Para
	
	escribir 'el precio total de los 10 productos es: ',redon(total*1.19)
	
FinAlgoritmo
