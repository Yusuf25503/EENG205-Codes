#Least Square method
#Written by Yusuf Hani Almoadhen

from sympy import *

x = [0,1,2,3,4]
y = [1.0,1.8,1.3,2.5,6.3]

sum1=0.0
sumx=0.0
sumx2=0.0
sumx3=0.0
sumx4=0.0
sumy=0.0
sumyx=0.0
sumyx2=0.0

for i in range(0,len(x)):
    sum1 += 1
    sumx += x[i]
    sumx2 += x[i]**2
    sumx3 += x[i]**3
    sumx4 += x[i]**4
    sumy += y[i]
    sumyx += y[i]*x[i]
    sumyx2 += y[i]*x[i]**2

A = Matrix([[sum1,sumx,sumx2],
            [sumx,sumx2,sumx3],
            [sumx2,sumx3,sumx4]])

b = Matrix([[sumy],
            [sumyx],
            [sumyx2]])

Sol = A.inv()*b

x = Symbol('x')

Eq = float("{:.5g}".format(Sol[2]))*x**2 + float("{:.5g}".format(Sol[1]))*x + float("{:.5g}".format(Sol[0]))

print("P(x) =",simplify(Eq))
