conteo=1
suma=0
while conteo <= 100:
    print (conteo) 
    suma=suma+conteo
    conteo=conteo+1

print('la suma de los primeros 100 numeros es: %d' % suma) 

pares=0
suma=0
while pares <= 100:
    if pares%2==0:
        print(pares)
        suma=suma+pares

    pares=pares+1

print ('la suma es: %d' % suma)

Sucesion=0
x=0
y=1
print(x)
print(y)
while Sucesion <= 1000:
    Sucesion=x+y
    x=y
    y=Sucesion
    print(Sucesion)


ejemplo=0
while ejemplo <= 25:
    print(ejemplo)
    ejemplo=ejemplo+1

    
resta=0
while resta >= -100:
        print(resta)
        resta=resta-1 