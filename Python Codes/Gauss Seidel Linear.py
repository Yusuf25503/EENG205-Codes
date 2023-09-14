#Gauss Seidel (Linear)
#Written by Yusuf Hani Yusuf 202107475

import pandas as pd
from sympy import *

x1 = Symbol('x1')
x2 = Symbol('x2')
x3 = Symbol('x3')
x4 = Symbol('x4')
x5 = Symbol('x5')
x6 = Symbol('x6')

x10 = 0
x20 = 0
x30 = 0
x40 = 0
x50 = 0
x60 = 0
A = Matrix([[3,-0.4,0,-0.9,0.02,0.01],
            [-1.2,4.2,-1,0,-0.88,0],
            [0.03,-1.2,4.5,0,0,-1.2],
            [-0.9,0,0,3.7,-1,0],
            [0,-1.2,0,-1.1,4,-1],
            [0,0.02,-1.4,0,-0.7,3.5]])

b = Matrix([[1.2],[0],[0],[0],[0.03],[0]])
#non OR Gauss Seidel 
X1 = 1/A[0,0]*(b[0,0]-A[0,1]*x2-A[0,2]*x3-A[0,3]*x4-A[0,4]*x5-A[0,5]*x6)
X2 = 1/A[1,1]*(b[1,0]-A[1,0]*x1-A[1,2]*x3-A[1,3]*x4-A[1,4]*x5-A[1,5]*x6)
X3 = 1/A[2,2]*(b[2,0]-A[2,0]*x1-A[2,1]*x2-A[2,3]*x4-A[2,4]*x5-A[2,5]*x6)
X4 = 1/A[3,3]*(b[3,0]-A[3,0]*x1-A[3,1]*x2-A[3,2]*x3-A[3,4]*x5-A[3,5]*x6)
X5 = 1/A[4,4]*(b[4,0]-A[4,0]*x1-A[4,1]*x2-A[4,2]*x3-A[4,3]*x4-A[4,5]*x6)
X6 = 1/A[5,5]*(b[5,0]-A[5,0]*x1-A[5,1]*x2-A[5,2]*x3-A[5,3]*x4-A[5,4]*x5)
iteration=0
k=100
Error=1e-6
Norm=100
Maximum=0
k_col=[]
x1_col=[]
x2_col=[]
x3_col=[]
x4_col=[]
x5_col=[]
x6_col=[]
norm_col=[]
x=[]
x0=[]
while iteration<k and Norm>=Error:
    iter_str = str(iteration) 
    k_col.append(iter_str.zfill(2))
    x1k = X1.subs({x1:x10,x2:x20,x3:x30,x4:x40,x5:x50,x6:x60})
    x1_col.append("{:.5g}".format(float(x1k)))
    x2k = X2.subs({x1:x1k,x2:x20,x3:x30,x4:x40,x5:x50,x6:x60})
    x2_col.append("{:.5g}".format(float(x2k)))
    x3k = X3.subs({x1:x1k,x2:x2k,x3:x30,x4:x40,x5:x50,x6:x60})
    x3_col.append("{:.5g}".format(float(x3k)))
    x4k = X4.subs({x1:x1k,x2:x2k,x3:x3k,x4:x40,x5:x50,x6:x60})
    x4_col.append("{:.5g}".format(float(x4k)))
    x5k = X5.subs({x1:x1k,x2:x2k,x3:x3k,x4:x4k,x5:x50,x6:x60})
    x5_col.append("{:.5g}".format(float(x5k)))
    x6k = X6.subs({x1:x1k,x2:x2k,x3:x3k,x4:x4k,x5:x5k,x6:x60})
    x6_col.append("{:.5g}".format(float(x6k)))
    #Norm 
    x.extend([x1k,x2k,x3k,x4k,x5k,x6k])
    x0.extend([x10,x20,x30,x40,x50,x60])
    for i in range(0,6):
        Difference = abs(x[i]-x0[i])
        if Difference>Maximum:
            Maximum = Difference
    Norm = Maximum 
    norm_col.append(Norm)
    Maximum = 0
    x.clear()
    x0.clear()
    x10 = x1k
    x20 = x2k
    x30 = x3k
    x40 = x4k
    x50 = x5k
    x60 = x6k
    iteration+=1
table = pd.DataFrame({
    'k': k_col,
    'x1': x1_col,
    'x2': x2_col,
    'x3': x3_col,
    'x4': x4_col,
    'x5': x5_col,
    'x6': x6_col,
    '||x(k)-x(k-1)||∞': norm_col
})
print("non OR Gauss Seidel",'\n')
print(table.to_markdown(index=False),'\n')
print("Roots:")
print("x1 =","{:.5g}".format(float(x1k)))
print("x2 =","{:.5g}".format(float(x2k)))
print("x3 =","{:.5g}".format(float(x3k)))
print("x4 =","{:.5g}".format(float(x4k)))
print("x5 =","{:.5g}".format(float(x5k)))
print("x6 =","{:.5g}".format(float(x6k)),'\n')
