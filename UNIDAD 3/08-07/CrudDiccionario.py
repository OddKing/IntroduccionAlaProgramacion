def mostrar_registros(registro):
    if registro:
        print('Registro: ')
        for nombre,datos in registro.items():
            print(f"Nombre: {nombre}")
            print(f"Edad: {datos['edad']}")
            print(f"Sexo: {datos['sexo']}")
            print(f"Correo {datos['correo']}")
            print("-------------------------------")

    else: 
        print("no hay registros")


def agregar_registro(registro,nombre,edad,sexo,correo):
    registro[nombre] = {
        'edad' : edad,
        'sexo' :sexo,
        'correo': correo
    }
    print("se agrego registro")

def modificar_registro():
    break