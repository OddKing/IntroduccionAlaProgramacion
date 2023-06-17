#Carlos Campaña Diaz 18528298-8
#Ejercicio 1
#TI2011/V-IEI-N1-P1-C2/V La Granja IEI
import Datos
import Descuento


def inicio():
    #modulo solicita asistentes y precio entrada 
    entrada=Datos.SolicitudPrecioEntrada()
    asistentes =Datos.SolictusAsistentes()

    Descuento.descuentoEntrada(asistentes,entrada)

