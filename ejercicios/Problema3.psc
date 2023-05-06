Algoritmo Problema3
	Definir gastos Como Entero
	definir ingresos Como Entero
	definir margen Como Real
	Escribir "hola, buen dia"
	Escribir "Bienvenido al ssitema que le dira si su empresa es rentable"
	Escribir "Ingrese su total de Ingresos: "
	leer ingresos
	Escribir "Ingrese su total de gastos"
	leer gastos
	si gastos>ingresos entonces 
		margen<-ingresos-gastos
		Escribir "Su empresa NO es rentable tiene un exceso de gastos del: ",margen
	sino 
		margen<-ingresos-gastos
		escribir " Su empresa es rentable, su margen de ganacia es : ",margen
	FinSi
	Escribir "Gracias :) por preferirnos"
	
FinAlgoritmo
