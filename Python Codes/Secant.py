#Secant method
#Written by Yusuf Hani Almoadhen

import pandas as pd
from sympy import *

x = Symbol('x')

eq = x**3-5*x+1

x0 = 0.0
x1 = 1.0
Tol = 100
Error = 1e-6
i = 0
k = int(input("Enter the number of iterations: "))
i_col=[]
x0_col=[]
x1_col=[]
f0_col=[]
f1_col=[]
Tol_col=[]
while i<k and Tol>=Error:
    i_col.append(str(i).zfill(2))
    x0_col.append("{:.5g}".format(x0))
    x1_col.append("{:.5g}".format(x1))
    f0 = float(eq.subs({x:x0}))
    f0_col.append("{:.5g}".format(f0))
    f1 = float(eq.subs({x:x1}))
    f1_col.append("{:.5g}".format(f1))
    xk = (x1*f0-x0*f1)/(f0-f1)
    if i==0:
        Tol_col.append('-')
    else:
        Tol = abs(xk-x1)
        Tol_col.append('{:.5g}'.format(Tol))
    x0 = x1
    x1 = xk
    i += 1
table = pd.DataFrame({
    'i': i_col,
    'x n-2': x0_col,
    'f(x n-2)': f0_col,
    'x n-1': x1_col,
    'f(x n-1)': f1_col,
    'Tol': Tol_col
})
print('')
print("Formula:",eq,'\n')
print(table.to_markdown(index=False),'\n')
if k>i:
    print("You have exceeded the maximum number of iterations according to the specified Tolerance!!",'\n')
print("The root is","{:.5g}".format(float(xk)))
