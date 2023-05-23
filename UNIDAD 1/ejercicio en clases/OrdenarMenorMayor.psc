Algoritmo OrdenarMenorMayor
	Definir n1 Como Entero
	definir n2 Como Entero
	definir n3 Como Entero
	definir p1 Como Entero
	definir p2 Como Entero
	definir p3 Como Entero

	Para i<-1 Hasta 3 Con Paso 1 Hacer
		Escribir "Ingrese el ",i,"° Numero :"
		si i==1 Entonces
			leer n1
		FinSi
		si i==2 Entonces
			leer n2
		FinSi
		si i==3 Entonces
			leer n3
		FinSi
	Fin Para
	
	si n1 < n2 y n1 < n3 Entonces
		Escribir "primer numero es el menor"
		p1<-n1
	sino 
		si	n2 < n1 y n2 < n3 Entonces
			Escribir "Segundo numero es el menor"
			p1<-n2
		sino 
			si n3<n1 y n3 <n2 Entonces
				Escribir "Tercer numero es el menor"
				p1<-n3
			FinSi
		FinSi
	FinSi
	
	si n1 >n2 y n1 >n3 Entonces
		Escribir "primer numero es el mayor"
		p3<-n1
	SiNo
		si	n2 > n1 y n2 > n3 Entonces
			Escribir "Segundo numero es el menor"
			p3<-n2
		sino 
			si n3>n1 y n3 >n2 Entonces
			Escribir "Tercer numero es el menor"
			p3<-n3
			FinSi
		FinSi
	FinSi
	
	si (p1 == n1 y p3 == n3) o (p1==n3 y p3 == n1)  Entonces
		p2<-n2
	sino
		si (p1 == n2 y p3 == n3) o (p1== n3 y p3 == n2 ) Entonces
			p2<- n1
		SiNo
			p2<-n3
		FinSi
	FinSi
	escribir p1," - ",p2," - ",p3
	
FinAlgoritmo
