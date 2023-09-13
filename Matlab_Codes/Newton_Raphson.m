%Newton Raphson method
%Written by Yusuf Hani Almoadhen 202107475

clc
clear
close all

syms x

f = 3*x-cos(x)-2;
df = diff(f);

index=1;
i=0;
k=input("Enter the number of iterations: ");
Error=10^-6;
tol=100;
x0 = 0.7;
xk = 0;

K = [];
X0 = [];
X = [];
F = [];
dF = [];
Tol = [];

while i<k && Error<=tol
    K(index,1) = i;
    X0(index,1) = x0;
    func = subs(f,x,x0);
    F(index,1) = func;
    dfunc = subs(df,x,x0);
    dF(index,1) = dfunc;
    xk = x0 - func/dfunc;
    X(index,1) = xk;
    tol = abs(xk-x0);
    Tol(index,1) = tol;
    x0 = xk;
    index = index+1;
    i = i+1;
end

fprintf('\n')

T = table(K,X0,F,dF,X,Tol);
disp(T)
fprintf('\n')
if k>index
    disp("You have exceeded the number of iterations accroding to the specified Tolerance!!")
    fprintf('\n')
end
disp("The root is " + num2str(double(xk)))
