Algoritmo Ejercicio2
	//Carlos Campaña - 18528298-8 - TI2011/V-IEI-N1-P1-C2/V La Granja IEI
	definir cds Como Entero
	definir total Como Entero
	definir ganacia Como Real
	
	Escribir "hola bienvenido a sistema de venta de cds"
	Escribir 'hola ingrese la cantidad de cd',"s desea comprar: "
	leer cds
	si cds <= 9 Entonces
		total<-10*cds
		ganacia<-total*0.0825
		escribir "el total a pagar: ",total," por haber comprado ",cds," CD"
		Escribir "la ganacia del vendedor es: ",ganacia
	sino
		si cds >= 10 y cds <= 99 Entonces
			total<-8*cds
			ganacia<-total*0.0825
			escribir "el total a pagar: ",total," por haber comprado ",cds," CD"
			Escribir "la ganacia del vendedor es: ",ganacia
		SiNo
			si cds >= 100 y cds <= 499 Entonces
				total<-7*cds
				ganacia<-total*0.0825
				escribir "el total a pagar: ",total," por haber comprado ",cds," CD"
				Escribir "la ganacia del vendedor es: ",ganacia
			SiNo
				total<-6*cds
				ganacia<-total*0.0825
				escribir "el total a pagar: ",total," por haber comprado ",cds," CD"
				Escribir "la ganacia del vendedor es: ",ganacia
			FinSi
		FinSi
	FinSi
FinAlgoritmo
