#Gauss Seidel (Nonlinear)
#Written by Yusuf Hani Almoadhen

import pandas as pd 
import math
from sympy import *

x1 = Symbol('x1')
x2 = Symbol('x2')
x3 = Symbol('x3')

X1 = 1/3*cos(x2*x3)+1/6
X2 = -0.1+1/9*(x1**2+sin(x3)+1.06)**0.5
X3 = (3-10*math.pi)/60-1/20*exp(-x1*x2)

iteration=0
k=int(input("Enter the number of iterations: "))
Error=1e-5
Norm=100
x10=0
x20=0
x30=0
x1k=0
x2k=0
x3k=0
Maximum = 0

k_col=[]
x1_col=[]
x2_col=[]
x3_col=[]
norm_col=[]
xk = []
x0 = []

#Gauss Seidel 
while iteration<k and Norm>=Error:
    iter_str = str(iteration)
    k_col.append(iter_str.zfill(2))
    if iteration == 0:
      x1_col.append(x10)
      x2_col.append(x20)
      x3_col.append(x30)
      norm_col.append('-')
    else:
        x1k = float(X1.subs({x1:x10,x2:x20,x3:x30}))
        x1_col.append("{:.5g}".format(x1k))
        x2k = float(X2.subs({x1:x1k,x2:x20,x3:x30}))
        x2_col.append("{:.5g}".format(x2k))
        x3k = float(X3.subs({x1:x1k,x2:x2k,x3:x30}))
        x3_col.append("{:.5g}".format(x3k))
        xk.extend([x1k,x2k,x3k])
        x0.extend([x10,x20,x30])
        for i in range(0,len(xk)):
           Difference = abs(xk[i]-x0[i])
           if Difference > Maximum:
              Maximum = Difference
        Norm = Maximum 
        norm_col.append("{:.5g}".format(float(Norm)))
        Maximum = 0
    xk.clear()
    x0.clear()
    x10 = x1k
    x20 = x2k
    x30 = x3k
    iteration = iteration+1
table = pd.DataFrame({
    'k': k_col,
    'x1': x1_col,
    'x2': x2_col,
    'x3': x3_col,
    '||x(k)-x(k-1)||∞': norm_col
})
print("\nGauss Seidel",'\n')
print(table.to_markdown(index=False),'\n')
if k>iteration:
    print("You have exceeded the number of iterations according to the specified iteration Error!!",'\n')
print("Roots:")
print("x1 = ","{:.5g}".format(float(x1k)))
print("x2 = ","{:.5g}".format(float(x2k)))
print("x3 = ","{:.5g}".format(float(x3k)))
