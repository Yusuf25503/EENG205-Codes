#Inverse Kinemetics 
#Written by Yusuf Hani Almoadhen

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import Symbol, Derivative, Matrix
from matplotlib import style

def Jacob(angle1,angle2,dx_angle1,dx_angle2,dy_angle1,dy_angle2):
    dx_angle1 = dx_angle1.subs({theta1:angle1,theta2:angle2})
    dx_angle2 = dx_angle2.subs({theta1:angle1,theta2:angle2})
    dy_angle1 = dy_angle1.subs({theta1:angle1,theta2:angle2})
    dy_angle2 = dy_angle2.subs({theta1:angle1,theta2:angle2})
    Det = dx_angle1 * dy_angle2 -  dx_angle2 * dy_angle1
    matrix2 = sp.Matrix([[dy_angle2,-1*dx_angle2],[-1*dy_angle1,dx_angle1]])
    Inv = 1/Det * matrix2
    return Inv, Det, matrix2

L1 = 1.0
L2 = 1.0
theta1 = Symbol('θ1')
theta2 = Symbol('θ2')

theta1_init= np.pi/4
theta2_init= np.pi/2
x_final = 1.5
y_final = 0.5
Tol = 1e-7
Norm = 100.0
i=int(input("Enter the number of iterations: "))
k=1
xNorm = []
yNorm = []
f1= L1*sp.cos(theta1) + L2*sp.cos(theta1+theta2) - x_final
f2= L1*sp.sin(theta1) + L2*sp.sin(theta1+theta2) - y_final

k_col=[]
theta1_col=[]
theta2_col =[]
theta1_init_col = []
theta2_init_col = []
x_final_col =[]
y_final_col =[]
x_init_col =[]
y_init_col =[]
norm_col =[]

pdx_theta1 = sp.Derivative(f1,theta1)
pdx_theta2 = sp.Derivative(f1,theta2)
pdy_theta1 = sp.Derivative(f2,theta1)
pdy_theta2 = sp.Derivative(f2,theta2)

dx_theta1 = pdx_theta1.doit()
dx_theta2 = pdx_theta2.doit()
dy_theta1 = pdy_theta1.doit()
dy_theta2 = pdy_theta2.doit()

xNorm.append(0.0)
yNorm.append(0.0)

while i>=k and Tol<=Norm:
    k_str = str(k)
    k_col.append(k_str.zfill(2))
    theta1_init_col.append("{:.5g}".format(float(theta1_init)))
    theta2_init_col.append("{:.5g}".format(float(theta2_init)))
    x0 = L1*np.cos(float(theta1_init))+L2*np.cos(float(theta1_init+theta2_init))
    y0 = L1*np.sin(float(theta1_init))+L2*np.sin(float(theta1_init+theta2_init))
    x_init_col.append("{:.5g}".format(float(x0)))
    y_init_col.append("{:.5g}".format(float(y0)))
    Jacobian = Jacob(theta1_init,theta2_init,dx_theta1,dx_theta2,dy_theta1,dy_theta2)
    T = Jacobian[2]
    Initial_matrix = sp.Matrix([[theta1_init],[theta2_init]])
    f_matrix = sp.Matrix([[f1.subs({theta1:theta1_init,theta2:theta2_init})],[f2.subs({theta1:theta1_init,theta2:theta2_init})]])
    R = Jacobian[0] * f_matrix
    x_matrix = Initial_matrix - R
    Result_x = float(x_matrix[0,0])
    xNorm.append(float(Result_x))
    Result_y = float(x_matrix[1,0])
    xf = L1*np.cos(Result_x)+L2*np.cos(Result_x+Result_y)
    yf = L1*np.sin(Result_x)+L2*np.sin(Result_x+Result_y)
    x_final_col.append("{:.5g}".format(float(xf)))
    y_final_col.append("{:.5g}".format(float(yf)))
    yNorm.append(float(Result_y))
    if k==1:
        norm_col.append('-')
    theta1_col.append("{:.5g}".format(float(Result_x)))
    theta2_col.append("{:.5g}".format(float(Result_y)))
    if k>=2:
        xNorm_diff = abs(float(xNorm[k])-float(xNorm[k-1]))
        yNorm_diff = abs(float(yNorm[k])-float(yNorm[k-1]))
        if xNorm_diff >= yNorm_diff:
           Norm = xNorm_diff
           norm_col.append("{:.6g}".format(float(Norm)))
        else:
           Norm = yNorm_diff
           norm_col.append("{:.6g}".format(float(Norm)))
    theta1_init = x_matrix[0,0]
    theta2_init = x_matrix[1,0]
    k+=1

table = pd.DataFrame({
    'k': k_col,
    'θ1(k-1)': theta1_init_col,
    'θ2(k-1)': theta2_init_col,
    'x(k-1)': x_init_col,
    'y(k-1)': y_init_col,
    'θ1(k)': theta1_col,
    'θ2(k)': theta2_col,
    'x(k)': x_final_col,
    'y(k)': y_final_col,
    'Norm': norm_col
})

print(table.to_markdown(index=False),'\n')
if i>k:
   print("You have exceeded the maximum number of possible iterations according to the specified parameters Tolerance!")
print('\n')
print("Final position for the robot arms: ",'\n')
print("x_final=","{:.5g}".format(float(L1*np.cos(Result_x) + L2*np.cos(Result_x+Result_y))))
print("y_final=","{:.5g}".format(float(L1*np.sin(Result_x) + L2*np.sin(Result_x+Result_y))),'\n')
print("The value of θ1 and θ2 in radian and degrees according to new position: ",'\n')
print("θ1=","{:.5g}".format(float(Result_x)),"rad",'=',"{:.5g}".format(float(Result_x*180/np.pi)),'°')
print("θ2=","{:.5g}".format(float(Result_y)),"rad",'=',"{:.5g}".format(float(Result_y*180/np.pi)),'°')

#Plotting θ1 and θ2
#Converting θ1 vlaues from radians to degrees
theta1Degree = []
theta2Degree = []
size = len(theta1_col)
for i in range(0,size):
  theta1Deg = "{:.5g}".format(float(float(theta1_col[i])*180/np.pi))
  theta1Degree.append(theta1Deg)
#Converting θ2 vlaues from radians to degrees
for i in range(0,size):
  theta2Deg = "{:.5g}".format(float(float(theta2_col[i])*180/np.pi))
  theta2Degree.append(theta2Deg)
Theta1 = np.array(theta1Degree)
Theta2 = np.array(theta2Degree)
style.use("ggplot")
plt.plot(k_col,Theta1)
plt.plot(k_col,Theta2)
plt.title("θ vs k")
plt.xlabel("k")
plt.ylabel("θ (Degrees)")
plt.legend(["θ1","θ2"])
