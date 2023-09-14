#Ordinary Differential Equations
#Written by Yusuf Hani Yusuf 202107475

import pandas as pd
import math
import matplotlib.pyplot as plt
from matplotlib import style
from sympy import *

theta = Symbol('θ')
theta_prime = Symbol("θ'")
theta_doublePrime = Symbol("θ''")
y1 = Symbol('y1')
y2 = Symbol('y2')
y1_prime = Symbol("y1'")
y2_prime = Symbol("y2'")

#Writing the state space representation of the ODE
L=1.0
m=1.0
g=10
tau=1
eq = 1.0/(m*L**2)*(-m*g*L*sin(y1)+tau)
y_vector = [y1,y2]
y_primeVector = [y2,eq]
yVector = pd.DataFrame({
    'y': y_vector,
    "y'": y_primeVector
})
simTime = float(input("Enter the simulation time: "))
h = float(input("Enter the step time: "))
print("State Space Representation: ")
print("y1 =",theta)
print("y2 =",theta_prime)
print("y2' =",theta_doublePrime,'=',eq,'\n')
print(yVector.to_markdown(index=False),'\n')

#Euler method
n_col = []
step_col = []
y1_col = []
y2_col = []
y2_prime_col = []
y1_init = 0.0
y2_init = 0.0
iteration = math.ceil(simTime/h)
step_conter=0.0
for i in range(0,iteration):
    n_col.append(i)
    step_col.append(step_conter)
    if i>=1:
        y1Eq = y1_init + h*float(y2_init)
        y1_col.append("{:.5g}".format(float(y1Eq)))
        y2_prime = float(eq.subs({y1:y1_init}))
        y2_prime_col.append("{:.5g}".format(float(y2_prime)))
        y2_n = y2_init + y2_prime*h
        y2_col.append("{:.5g}".format(float(y2_n)))
        y1_init = y1Eq
        y2_init = y2_n
    else:
        y1_col.append(y1_init)
        y2_col.append(y2_init)
        y2_prime_col.append("{:.5g}".format(float(eq.subs({y1:y1_init}))))
    step_conter+=0.1

table = pd.DataFrame({
    'n': n_col,
    'step': step_col,
    'y1': y1_col,
    'y2': y2_col,
    "y2'": y2_prime_col
})
print(table.to_markdown(index=False),'\n')
print("y1 =","{:.5g}".format(float(y1Eq)))
print("y2 =","{:.5g}".format(float(y2_n)))
print("y2' =","{:.5g}".format(float(y2_prime)))

#Plotting
style.use('ggplot')
plt.figure("1")
plt.scatter(step_col,y1_col,marker= "*",color="blue")
plt.xlabel("Time (sec)")
plt.ylabel("Angular Displacement (Radians)")
plt.title("Angular Displacement vs Time")
plt.figure("2")
plt.scatter(step_col,y2_col,marker="*",color="red")
plt.xlabel("Time (sec)")
plt.ylabel("Angular Velocity (rad/sec)")
plt.title("Angular Velocity vs Time")
plt.figure("3")
plt.scatter(step_col,y1_col, marker= "*",color="blue")
plt.scatter(step_col,y2_col,marker="*",color="red")
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude")
plt.title("Inverted Pendulum Dynamic System")
plt.legend(["y1","y2"])
