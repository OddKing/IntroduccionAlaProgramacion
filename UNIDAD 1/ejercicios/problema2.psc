Algoritmo problema2
	//se declaran variables
	definir pass Como Entero
	definir saldoIncial Como Entero
	definir opciones Como Entero
	definir movimientos Como Entero
	definir salir1 Como logico
	definir salir2 Como Logico
	//seinicializan las necesarias
	salir1 <- Verdadero
	salir2 <- Verdadero
	saldoIncial<-5000

	Escribir "Hola Bienvenido  al caajero su banquito"
	mientras salir1 hacer 
		Escribir "Recuerde Su clave no puede partir en 0"
		Escribir "ingrese su clave"
		leer pass
		si pass > 0  Entonces
			si pass >=1000 y pass <= 9999 Entonces
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
							saldoIncial=saldoIncial-movimientos
							Escribir "Su saldo despues de girar es: ",saldoIncial
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
		sino 
			Escribir "ingrese Clave valida"
		FinSi
		
	FinMientras
	
	
FinAlgoritmo
