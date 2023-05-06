Algoritmo CajeroBanco
	//se declaran variables
    Definir cPass, cDigito Como Caracter;
	definir pass Como Entero
	definir i como entero
	definir opciones Como Entero
	definir movimientos Como Entero
	definir salir1 Como logico
	definir salir2 Como Logico
	//seinicializan las necesarias
	salir1 <- Verdadero
	salir2 <- Verdadero
	saldoIncial<-5000
	
	Escribir "Hola Bienvenido  al cajero su banquito"
	mientras salir1 hacer 
		Escribir 'Introduzca un número: ' sin saltar;
        leer cPass;
        lNumero <- verdadero;
		si  Longitud(cPass)  == 4 Entonces
			Para i <- 0 hasta Longitud(cPass)-1 Hacer
				cDigito <- SubCadena(cPass,i,i);
				si cDigito < '0' | cDigito > '9' Entonces
					lNumero <- Falso;
				FinSi
			FinPara
			Si ~lNumero Entonces
				Escribir "Ingrese clave valida"
				Escribir '';
			SiNo
				Mientras salir2 Hacer
					Escribir "que operacion desea realizar?"
					Escribir "1- Consultar Saldo"
					Escribir "2- Girar de su cuenta"
					Escribir "3- Quiere Depositar a su cuenta"
					Escribir "4-Salir"
					leer opciones
					Segun opciones Hacer
						1:
							Escribir "Su saldo es: $",saldoIncial
						2:
							movimientos<-0
							Escribir "cuanto es el monto que desea girar: "
							leer movimientos
							si saldoIncial>movimientos entonces
								saldoIncial=saldoIncial-movimientos
								Escribir "Su saldo despues de girar es: ",saldoIncial
							sino
								Escribir "su saldo es insuficiente para realizar el giro"
							finsi
						3:
							movimientos<-0
							Escribir "Ingrese el monto depositado: "
							leer movimientos
							saldoIncial=saldoIncial+movimientos
							Escribir "Su saldo luego del deposito es: ",saldoIncial
						4:
							salir1<-Falso
							salir2<-Falso
							Escribir "Adios!!!"
						De Otro Modo:
							Escribir "ingre opcion valida"
					Fin Segun
				Fin Mientras
			FinSi
		SiNo
			escribir "Ingrese clave valida"
		FinSi
	FinMientras
FinAlgoritmo