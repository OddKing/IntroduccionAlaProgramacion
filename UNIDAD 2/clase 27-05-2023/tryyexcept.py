try:
    print('')
    #c=5/0
    d=2 + "Hola"
#except ZeroDivisionError:
#    print("No se Puede dividir entre cero!")
#except TypeError:
#    print("Problemas de tipos!")
except Exception as e:
    print("Ha habido una excepción", type(e))
