#Lagrange Approximation method
#Written by Yusuf Hani Yusuf 202107475

from sympy import *
import pandas as pd

x = Symbol('x')

x_val = [-1,1,2]
y_val = [-1,1,8]
k=[]
for i in range(0,len(x_val)):
    k.append(i)
Pi = 1.0
Sum = 0.0
Lx = []
for i in range(0,len(x_val)):
    for j in range(0,len(y_val)):
        if i != j:
            L = (x - x_val[j])/(x_val[i] - x_val[j])
            Pi *= L
    Lx.append(simplify(Pi))
    Pi = 1.0
table = pd.DataFrame({
    'index': k,
    'x': x_val,
    'y': y_val,
    'L': Lx
})
for i in range(0,len(Lx)):
    Sum += Lx[i]*y_val[i]
print("Lagrange Interpolation:",'\n')
print(table.to_markdown(index=False),'\n')
print("P(x) =",expand(Sum))

point = float(input("Enter the estimation point: "))
print("P({}) =".format("{:.5g}".format(point)),"{:.5g}".format(float(Sum.subs({x:point})))) 
