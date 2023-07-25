import random
lista_fruta=["Plátano", "Limón", "Manzana", "Pera", "Uva","Frutilla"]

def llenadodeFrutas(lista):
    variable=lista[random.randint(0, 5)]
    #print(random.randint(0, 6))        
    return variable

#print(llenadodeFrutas(lista_fruta))


def validarCreditos(credito):
    if credito>= 3:
        return True
    else:
        return False

def descontarCreditos(creditos):
    creditos=creditos-3
    return creditos

def lanzamiento(credito,lista):
    lista_lanzada=[]
    if validarCreditos(credito):
        for i in range(3):
            var=llenadodeFrutas(lista)
            lista_lanzada.append(var)
    
    return lista_lanzada

def revisarLista(lista):
    if lista[0]== lista[1] and lista[1]==lista[2]:
        return True
    else:
        return False

def granpremio(credito):
    credito=credito*100
    return credito