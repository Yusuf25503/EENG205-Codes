#Newton Raphson (Multivariable)
#Written by Yusuf Hani Yusuf 202107475

import pandas as pd
import numpy as np
import sympy as sp
from sympy import Symbol, Derivative, Matrix
from mayavi import mlab
def Jacob(v0,i0,dv1_x,dv1_y,dv2_x,dv2_y): #Jacobian function
dv1_x = dv1_x.subs({x:v0,y:i0})
dv1_y = dv1_y.subs({x:v0,y:i0})
dv2_x = dv2_x.subs({x:v0,y:i0})
dv2_y = dv2_y.subs({x:v0,y:i0})
Det = dv1_x * dv2_y - dv1_y * dv2_x
matrix2 = sp.Matrix([[dv2_y,-1*dv1_y],[-1*dv2_x,dv1_x]])
Inv = 1/Det * matrix2
return Inv, Det, matrix2
def Surface1(v,i): #Surface 1 function for 3D Graph
return i+1.02*v**3
def Surface2(v1,i1): #Surface 2 function for 3D Graph
return -0.9*v1+i1**3
x0=2.0
y0=0.25
Tol = 1e-6
Norm = 10.0
i=int(input("Enter the number of iterations: "))
k=1
xNorm =[]
yNorm =[]
x=Symbol('x')
y=Symbol('y')
k_col=[]
x_col=[]
y_col =[]
x_init_col = []
y_init_col = []
det_col=[]
j1_col = []
j2_col = []
j3_col = []
j4_col = []
f1_col =[]
f2_col =[]
norm_col =[]
f1 = y + 1.02*x**3
f2 = -0.9*x + y**3
#Finding partial derivatives
pd1_x = sp.Derivative(f1, x)
pd1_y = sp.Derivative(f1, y)
pd2_x = sp.Derivative(f2, x)
pd2_y = sp.Derivative(f2, y)
df1_x = pd1_x.doit()
df1_y = pd1_y.doit()
df2_x = pd2_x.doit()
df2_y = pd2_y.doit()
xNorm.append(0.0)
yNorm.append(0.0)
while i>=k and Tol<=Norm:
k_str = str(k)
k_col.append(k_str.zfill(2))
x_init_col.append("{:.5g}".format(float(x0)))
y_init_col.append("{:.5g}".format(float(y0)))
Jacobian = Jacob(x0,y0,df1_x,df1_y,df2_x,df2_y)
T = Jacobian[2]
j1_col.append("{:.5g}".format(float(T[0,0])))
j2_col.append("{:.5g}".format(float(T[0,1])))
j3_col.append("{:.5g}".format(float(T[1,0])))
j4_col.append("{:.5g}".format(float(T[1,1])))
det_col.append("{:.5g}".format(float(1/Jacobian[1])))
f_matrix = sp.Matrix([[f1.subs({x:x0,y:y0})],[f2.subs({x:x0,y:y0})]])
f1_col.append("{:.5g}".format(float(f_matrix[0,0])))
f2_col.append("{:.5g}".format(float(f_matrix[1,0])))
R = Jacobian[0] * f_matrix
Initial_matrix = sp.Matrix([[x0],[y0]])
x_matrix = Initial_matrix - R
Result_x = float(x_matrix[0,0])
xNorm.append("{:.5g}".format(float(Result_x)))
Result_y = float(x_matrix[1,0])
yNorm.append("{:.5g}".format(float(Result_y)))
if k==1:
norm_col.append('-')
x_col.append("{:.5g}".format(float(Result_x)))
y_col.append("{:.5g}".format(float(Result_y)))
if k>=2:
xNorm_diff = abs(float(xNorm[k])-float(xNorm[k-1]))
yNorm_diff = abs(float(yNorm[k])-float(yNorm[k-1]))
if xNorm_diff >= yNorm_diff:
Norm = xNorm_diff
norm_col.append("{:.5g}".format(float(Norm)))
else:
Norm = yNorm_diff
norm_col.append("{:.5g}".format(float(Norm)))
x0 = x_matrix[0,0]
y0 = x_matrix[1,0]
k+=1
#Constructing the table
table = pd.DataFrame({
'k': k_col,
'x(k-1)': x_init_col,
'y(k-1)': y_init_col,
'1/Det': det_col,
'J1': j1_col,
'J2': j2_col,
'J3': j3_col,
'J4': j4_col,
'f1': f1_col,
'f2': f2_col,
'x(k)': x_col,
'y(k)': y_col,
'||x||∞': norm_col
})
#Printing Results
print(table.to_markdown(index=False))
if i>k:
print('\n',"You have exceeded the number of possible iterations according to the specified Tolerance!")
print('\n',"Number of iterations=",k)
print('\n','\n',"Roots:")
print('\n',"x=","{:.5g}".format(float(x_matrix[0,0])),'\n',"y=","{:.5g}".format(float(x_matrix[1,0])))
print('\n',"Infinity Norm:")
print('\n',"||x||∞ =", Norm)
#3D Graphing
a= np.arange(-2,2,0.1)
b= np.arange(-2,2,0.1)
a1= np.arange(-2,2,0.1)
b1= np.arange(-2,2,0.1)
X,Y = np.meshgrid(a,b)
X1,Y1 = np.meshgrid(a1,b1)
Z = Surface1(X,Y)
Z1 = Surface2(X1,Y1)
mlab.figure(fgcolor=(0,0,0), bgcolor=(0.65,0.65,0.65))
surf1 = mlab.surf(Z,color=(1,0,0.7))
surf2 = mlab.surf(Z1,color=(0,0.7,1))
axis = mlab.axes(color=(0,0,0),nb_labels=5)
axis.axes.font_factor = 0.8
mlab.title('3D Graph')
text1 = "y+1.02x^3"
text2 = "-0.9x+y^3"
mlab.text3d(-30,20,20,text1,color=(1,0,0.7),scale=1.5)
mlab.text3d(-32,20,15,text2,color=(0,0.7,1),scale=1.5)
mlab.outline(surf1)
mlab.show()
