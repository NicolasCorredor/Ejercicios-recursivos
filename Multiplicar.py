def multiplicar(n1,n2):
    if n2==0:
        return 0
    return n1+multiplicar(n1,n2-1)

#Prueba del algoritmo
print(multiplicar(10,10))