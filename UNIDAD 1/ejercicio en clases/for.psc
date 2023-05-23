Algoritmo SumarCincoNumeros
	Definir n Como Entero
	definir num Como Real
	Definir suma Como Real
	n<-1
	num <- 0.0
	suma <- 0.0
	Escribir 'Ingrese 5 numeros'
	Para n<-1 Hasta 5 Con Paso 1 Hacer
		Escribir 'numero ',n,' :'
		leer num
		suma <- suma+num
		//n<-n+1
	Fin Para
	escribir 'El resultado de la suma es: ',suma
FinAlgoritmo
