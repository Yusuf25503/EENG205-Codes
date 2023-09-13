%Secant method
%Written by Yusuf Hani Almoadhen 202107475

clc
clear 
close all

syms x
f = 3*x-cos(x)-2;

x0=0.5;
x1=1;
xk=0;
tol=100;
Error=10^-6;
index=1;
i=0;
k=input("Enter the number of iterations: ");

K=[];
X=[];
X0=[];
X1=[];
F0=[];
F1=[];
Tol=[];

while i<k && tol>=Error
    K(index,1) = i;
    X0(index,1) = x0;
    X1(index,1) = x1;
    f0 = subs(f,x,x0);
    F0(index,1) = f0;
    f1 = subs(f,x,x1);
    F1(index,1) = f1;
    xk = (x0*f1-x1*f0)/(f1-f0);
    X(index,1) = xk;
    if i==0
        Tol(index,1) = "-";
    else
        tol = abs(xk-x1);
        Tol(index,1) = tol;
    end
    x0 = x1;
    x1 = xk;
    index = index+1;
    i = i+1;
end

fprintf('\n')
T = table(K,X0,X1,F0,F1,X,Tol);
disp(T)

if k>index
    fprintf('\n')
    disp("You have exceeded the number of iterations accroding to the specified Tolerance!!")
end

fprintf('\n')
disp("The root is " + num2str(double(xk)))
