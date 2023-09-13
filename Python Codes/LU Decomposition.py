#LU Decomposition 
#Written by Yusuf Hani Yusuf 202107475

import math
from sympy import *

u11,u12,u13 = symbols('u11:14')
u22,u23 = symbols('u22:24')
u33 = symbols('u33')
l21 = symbols('l21')
l31,l32 = symbols('l31:33')

A = Matrix([[1,3,2],
            [3,2,6],
            [2,4,8]])

U = Matrix([[u11,u12,u13],
            [0,u22,u23],
            [0,0,u33]])

L = Matrix([[1,0,0],
            [l21,1,0],
            [l31,l32,1]])

M = L*U

Eq = []
for i in range(0,int(math.sqrt(len(A)))):
    for j in range(0,int(math.sqrt(len(A)))):
        Eq.append(M[i,j]-A[i,j])
Var = [u11,u12,u13,u22,u23,u33,l21,l31,l32]
Sol = solve(Eq,Var)
print(Var)
print(Sol,'\n')
