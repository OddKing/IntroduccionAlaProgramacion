Algoritmo tipoPrueba
	//TI2011/V-IEI-N1-P1-C2/V La Granja IEI
	//18528298-8
	//Carlos Alfonso Campaña Diaz
	Definir  cantidadZapatos como entero
	Definir valorPagar Como Real
	Escribir "Ingrese la cantidad de zapatos que va comprar para ver si obtiene descuento  y cuanto descuento"
	Leer cantidadZapatos
	si cantidadZapatos > 10  y cantidadZapatos <= 20 Entonces
		valorPagar=(cantidadZapatos*80)*0.90
		Escribir "usted compro ",cantidadZapatos," y su descuento es de 10% y total a pagar es ",valorPagar
	sino 
		si cantidadZapatos>20 y cantidadZapatos <30 Entonces
			valorPagar=(cantidadZapatos*80)*0.80
			Escribir "usted compro ",cantidadZapatos," y su descuento es de 20% y total a pagar es ",valorPagar
		SiNo
			si cantidadZapatos>=30 Entonces
				valorPagar=(cantidadZapatos*80)*0.60
				Escribir "usted compro ",cantidadZapatos," y su descuento es de 40% y total a pagar es ",valorPagar
			SiNo
				valorPagar=(cantidadZapatos*80)
				Escribir "usted compro ",cantidadZapatos," usted no tiene descuento y total a pagar es ",valorPagar
			FinSi
		FinSi
	FinSi
	
	
FinAlgoritmo
