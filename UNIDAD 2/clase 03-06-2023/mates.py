import math


'''
g)log(3x+15)
(x+2)^2
a^2+b^2
'''
def castigo(a):
    contador=0
    while True:
        print (a)
        print("vuelta ",contador+1)
        try:
            x=int(input("Ingrese un valor para X: "))
            a=int(input("Ingrese un valor para a: "))
            b=int(input("Ingrese un valor para b: "))
            print('\n')
        except ValueError:

            print('ingreso variable que no es numerica')

        else:

            print("Aca  se calcula log(3X + 15)")
            var=math.log10(3*x+15)
            #var2= math.log(18,10)
            #var3 = math.log10(18)
            #print (var)
            print("El resultadp es: {}\n".format(var))

            print ("Aca se calcula a(x)= (x+2)^2")
            k = math.pow(x+2,2)
            print("resultado es : ",k,'\n')

            print("Aqui se calcula a^2+b^2 \n")
            p=math.sqrt(math.pow(a,2)+math.pow(b,2))
            print(f'el resultado es: {p} \n')
            contador +=1
            print(a == contador)
            if a == contador:
                break
