%Bisection Method
%Written by Yusuf Hani Almoadhen 

clc
clear
close all

a=0.3;
b=0.7;
c=0;

f = @(x) x+10^-3*exp(20*x)-9;
index=1;
i=0;
k=input("Enter the number of iterations: ");
Error=10^-4;
tol=100;

K = [];
A = [];
B = [];
C = [];
Fa = [];
Fb = [];
Fc = [];
Tol = [];

while i<k && Error<=tol
    K(index,1) = i;
    A(index,1) = a;
    B(index,1) = b;
    c = (a+b)/2;
    C(index,1) = c;
    fa = f(a);
    Fa(index,1) = fa;
    fb = f(b);
    Fb(index,1) = fb;
    fc = f(c);
    Fc(index,1) = fc;
    if i == 0
        Tol(index,1) = "-";
    else
        tol = abs(c-c_temp);
        Tol(index,1) = tol;
    end
    if fa*fc > 0
        a = c;
    else
        b = c;
    end
    c_temp = c;
    index = index+1;
    i = i+1;
end
fprintf('\n')
T = table(K,A,B,C,Fa,Fb,Fc,Tol);
disp(T)
fprintf('\n')
if k>index
    disp("You have exceeded the number of iterations accroding to the specified Tolerance!!")
    fprintf('\n')
end
disp("The root is " + num2str(c))
