

def division(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print ("¡ No se puede dividir por cero !")
    else:
        print(result)


division(1,0)

division(1,2)