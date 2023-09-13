%Ordinary Differential Equations 
%Written by Yusuf Hani Almoadhen 202107475

clc
clear
close all;

syms z1 z2 dz1 dz2

m=1;
L=1;
g=10;
tau=1;
eq = 1/(m*L^2)*(-m*g*L*sin(z1)+tau);

z_vector = [z1;z2];
dz_vector = [z2;eq];

fprintf("State Space Representation \n\n")
T1 = table(z_vector,dz_vector);
disp(T1)
fprintf("Euler's method\n\n")
Sim=input("Enter the simulation time: ");
h=input("Enter the simulation time: ");
step_counter=0;
z1_init=0;
z2_init=0;
K=[];
Step=[];
Z1=[];
Z2=[];
dZ2=[];
index=1;

for i=0:ceil(Sim/h)-1
    K(index,1) = i;
    Step(index,1) = step_counter;
    if i==0
        Z1(index,1) = z1_init;
        Z2(index,1) = z2_init;
        dZ2(index,1) = subs(eq,{z1 z2},{z1_init z2_init});
    else
        Z1_value = z1_init + h*z2_init;
        Z1(index,1) = Z1_value;
        dZ2_value = double(subs(eq,{z1 z2},{z1_init z2_init}));
        dZ2(index,1) = dZ2_value;
        Z2_value = z2_init + h*dZ2_value;
        Z2(index,1) = Z2_value;
        z1_init = Z1_value;
        z2_init = Z2_value;
    end
    index = index+1;
    step_counter  = step_counter+0.1;
end

T2 = table(K,Step,Z1,Z2,dZ2);
disp(T2)
disp("Solutions: ")
disp("Z1 = " + Z1_value)
disp("Z2 = " + Z2_value)
disp("Z2' = " + dZ2_value)

subplot(2,2,1)
scatter(Step,Z1,'ko','markerfacecolor','blue')
grid
title("Angular Displacement vs Time")
xlabel("Time (sec)")
ylabel("Angular Displacement (Radians)")

subplot(2,2,2)
scatter(Step,Z2,'ko','markerfacecolor','red')
grid
title("Angular Velocity vs Time")
xlabel("Time (sec)")
ylabel("Angular Velocity (rad/sec)")

subplot(2,2,3)
scatter(Step,dZ2,'ko','markerfacecolor','green')
grid
title("Angular Accelerations vs Time")
xlabel("Time (sec)")
ylabel("Angular Accelerations (rad/sec^2)")

subplot(2,2,4)
scatter(Step,Z1,'ko','markerfacecolor','blue')
hold;
scatter(Step,Z2,'ko','markerfacecolor','red')
scatter(Step,dZ2,'ko','markerfacecolor','green')
grid
title("Inverted Pendulum Dynamic System")
xlabel("Time (sec)")
ylabel("Amplitude")
legend(["Z1" "Z2" "Z2'"])