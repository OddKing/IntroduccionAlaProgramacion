Algoritmo problema1
	//Suponga que un individuo desea invertir su capital en un banco y desea saber cuanto dinero ganara despu�s de X meses.
	//El banco paga un inter�s del 2% mensual.
	//Realice un algoritmo que permita calcular la ganancia seg�n el numero de meses que el usuario ingrese.
	Definir montoInvertir Como Entero
	definir meses Como Entero
	definir ganancia Como Real
	Escribir "Ingrese el monto a invertir"
	leer montoInvertir
	Escribir "Ingrese la cantidad de meses que desea invertir"
	leer meses
	//calculare un interes simple
	ganancia<- montoInvertir*((0.02)*meses)
	Escribir "este el monto:",ganancia," que se genero en la cantidad de meses ",meses
FinAlgoritmo
