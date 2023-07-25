#[Carlos Campaña][18528298-8]
#[Ejercicio 1]
#[TI2011/V-IEI-N1-P1-C2/V La Granja IEI]

from numpy import array

def CalculoDeTraceArray():
    #se crear los array indicados en el ejercicio
    a=array([[-55,69,77],[-83,-66,-58],[73,89,61],[43,-31,-76]])
    b=array([[-8,68,98],[-24,5,-57],[-8,45,-14],[38,-85,77]])
    #se muestra el resultado de los traza de los array
    print(a.trace())
    print(b.trace())