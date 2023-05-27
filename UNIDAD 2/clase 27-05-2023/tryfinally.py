try:
    x=2/0
except:
    print("Entra en except, ha ocurrido una excepion")
else:
    print("Entra en el else, no ha ocurrido ninguna excepcion")
finally:
    print("Entra En finally ")