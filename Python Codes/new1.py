import pandas as pd
from sympy import *

x = Symbol('x')
eq = 3*x-cos(x)-2
eq_diff = eq.diff(x)
x_init = 0.7
Tol = 100
Error = 1e-6
i = 0
k = int(input("Enter the number of Iterations: "))
i_col=[]
x_col=[]
f_col=[]
f_prime_col=[]
Tol_col=[]
while i<k and Tol>=Error:
    i_col.append(str(i).zfill(2))
    x_col.append("{:.5g}".format(x_init))
    f = float(eq.subs({x:x_init}))
    f_col.append("{:.5g}".format(f))
    f_prime = float(eq_diff.subs({x:x_init}))
    f_prime_col.append("{:.5g}".format(f_prime))
    xk = x_init - f/f_prime
    if i==0:
        Tol_col.append('-')
    else:
        Tol = abs(xk-x_init)
        Tol_col.append("{:.5g}".format(float(Tol)))
    x_init = xk
    i += 1
table = pd.DataFrame({
    'i': i_col,
    'x': x_col,
    'f(x)': f_col,
    "f'(x)": f_prime_col,
    'Tol': Tol_col
})
print('\n')
print("Formula:",eq)
print("Derivative:",eq_diff,'\n')
print(table.to_markdown(index=False),'\n')
if k>i:
    print("You have exceeded the maximum number of iterations accroding to the specified Error!!",'\n')
print("The root is","{:.5g}".format(float(xk)))
