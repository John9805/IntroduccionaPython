import math

print('El valor de A es: ')
VA=input()
VA = int(VA)
print('El valor de B es: ')
VB=input()
VB = int(VB)
print('El valor de C es: ')
VC=input()
VC = int(VC)

formula=0
expo=VB*VB
suma=-4*VA*VC
raiz=math. sqrt(expo+suma)
div1=(-VB + raiz)/(2*VA)
div=(-VB - raiz)/(2*VA)


print('Valor de X1 es igual a: %f ' %div)
print('Valor de X2es igual a %f: ' %div1)
print('Valor de X2es igual a %f: ' %div1)

