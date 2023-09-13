#Bisection method
#Written by Yusuf Hani Yusuf 202107475

import pandas as pd
from sympy import *

x = Symbol('x')

f = x + 10**-3*exp(20*x) - 9

a = 0.0
b = 1.0
c = 0.0
Tol = 100
Error = 0.00001
k = int(input("Enter the number of iterations: "))
i = 0
a_col=[]
b_col=[]
c_col=[]
i_col=[]
fa_col=[]
fb_col=[]
fc_col=[]
Tol_col=[]

fa = f.subs({x:a})
fb = f.subs({x:b})
if fa*fb > 0:
    print("There is no root in this range")
    exit()

while i<k and Tol>=Error:
    i_str = str(i)
    i_col.append(i_str.zfill(2))
    a_col.append("{:.5g}".format(float(a)))
    b_col.append("{:.5g}".format(float(b)))
    c = (a+b)/2.0
    c_col.append("{:.5g}".format(float(c)))
    fa = f.subs({x:a})
    fa_col.append("{:.5g}".format(float(fa)))
    fb = f.subs({x:b})
    fb_col.append("{:.5g}".format(float(fb)))
    fc = f.subs({x:c})
    fc_col.append("{:.5g}".format(float(fc)))
    if i==0:
        Tol_col.append('-')
        c_temp = c
    else:
        Tol = abs(c-c_temp)
        Tol_col.append("{:.5g}".format(float(Tol)))
        c_temp = c
    if fa*fc > 0:
        a = c
    elif fb*fc > 0:
        b = c
    i += 1
table = pd.DataFrame({
    'i': i_col,
    'a': a_col,
    'b': b_col,
    'c': c_col,
    'f(a)': fa_col,
    'f(b)': fb_col,
    'f(c)': fc_col,
    'Tol': Tol_col
})
print("")
print("Bisection method:",'\n')
print(table.to_markdown(index=False),'\n')
if k>i:
    print("You have exceeded the maximum number of iterations according to the specified Tolerance!!",'\n')
print("The roots is", "{:.5g}".format(float(c)))

