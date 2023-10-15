import math as mt
#Declaracion de variables
d,r,=0,0
r1,r2=0,0
#Lectura de datos
sa,sb,sc=input("Leer los coeficientes "),input(),input()
a=int(sa)
b=int(sb)
c=int(sc)
d=(b**2)-4*a*c#Discriminante
if a!=0:
    if d<0:
        print("No hay raices en los reales")
    elif d==0:
        r=(-b)/(2*a)
        print("La unica raiz es:",r)
    else:
        r1=((-b)+mt.sqrt(d))/(2*a)
        r2=((-b)-mt.sqrt(d))/(2*a)
        print("Las raiz 1 es:",r1," La raiz 2 es:",r2)
else:
    print("El primer coeficiente no puede ser 0")







