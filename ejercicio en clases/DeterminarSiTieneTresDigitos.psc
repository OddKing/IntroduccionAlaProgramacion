Algoritmo DeterminarSiTieneTresDigitos
	Definir valorIngresado Como Entero
	Escribir "por favor ingrese  un valor numerico"
	Leer valorIngresado
	escribir valorIngresado
	si valorIngresado >-1000 Y valorIngresado < -99 Entonces
		Escribir "El Numero ",valorIngresado," Tiene 3 digitos"
	SiNo
		si valorIngresado > 99 y valorIngresado < 1000 entonces 
			Escribir "el numero ",valorIngresado," Tiene 3 digitos"
			escribir valorIngresado
		SiNo
			Escribir "el numero ",valorIngresado," NO Tiene 3 digitos"
			escribir valorIngresado
		FinSi

	FinSi
	
	
	
FinAlgoritmo
