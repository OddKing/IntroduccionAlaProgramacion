Algoritmo ejercicio3
	//Carlos Campaña - 18528298-8 - TI2011/V-IEI-N1-P1-C2/V La Granja IEI
	definir variableX Como Real
	Definir variableY Como Real
	Definir variableJ Como Real
	Definir resultado Como Real
	definir opciones Como Caracter
	definir salida Como Logico
	salida<-Verdadero

	Mientras salida Hacer
		Escribir "Bienvenido  al sistema del matimatico"
		Escribir "a) Calculo de la ecuación 1: X+Y+J*0,32"
		Escribir "b) Calculo de la ecuación 2: X^2+2x+4"
		Escribir "c) Calculo de la ecuación 3: El 30% de X + 20% de Y"
		Escribir "d) Calculo de la ecuación 4: La raíz cuadrada de X"
		Escribir "e) Salir"
		Escribir "Ingrese la opcion"
		leer opciones
		si opciones = "A" o opciones = "a" o opciones = "B" o opciones = "b" o opciones = "C" o opciones = "c" o opciones = "D" o opciones = "d" o opciones="E" o opciones="e" Entonces
			opciones<-Minusculas(opciones)
			Segun opciones Hacer
				"a":
					Escribir "favor ingrese el valor de las variables en el orden que se indica por pantalla X+Y+J*0,32"
					Escribir " Ingrese valor de la varaible X"
					leer variableX
					Escribir " Ingrese valor de la variable Y"
					leer variableY
					Escribir " Ingrese valor de la variable J"
					leer variableJ
					resultado<-variableX+variableY+(variableJ*0.32)
					Escribir "Su resultado segun los valores guardados es: ",resultado
					Escribir "gracias por usar matitmatico"
					//salida<-Falso
					
				"b":
					Escribir" Favor ingresar los valores para esta ecuacion X^2+2x+4 en el orden solicitado "
					Escribir "Ingrese el valor de X"
					Leer variableX
					resultado<- (variableX^2)+(2*variableX)+4
					Escribir "Su resultado segun los valores guardados es: ",resultado
					Escribir "gracias por usar matitmatico"
					//salida<-Falso					
				"c":
					Escribir "calcularemoos esto  30% de X + 20% de Y favor ingresar los valores en el orden que se solicita"
					Escribir " Ingrese el valor de X"
					leer variableX
					Escribir " Ingrese el valor de  Y"
					leer variableY
					resultado<-(variableX*0.3)+(variableY*0.2)
					Escribir "Su resultado segun los valores guardados es: ",resultado
					Escribir "gracias por usar matitmatico"
					//salida<-Falso
				"d":
					Escribir "Calcularemos la raiz cuadrada de X favor ingresar el valor de X"
					Leer variableX
					resultado<-raiz(variableX)
					Escribir "Su resultado segun los valores guardados es: ",resultado
					Escribir "gracias por usar matitmatico"
					//salida<-Falso
				"e":
					Escribir "adios"
					salida<-Falso
			Fin Segun
		sino
			Escribir "Opcion no valida"
		FinSi
	Fin Mientras
	
	
	
FinAlgoritmo
