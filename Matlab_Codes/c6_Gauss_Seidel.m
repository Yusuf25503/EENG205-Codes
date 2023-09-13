%Gauss Seidel method (Nonlinear)
%Written by Yusuf Hani Almoadhen 202107475

clc
clear
close all;

syms x1 x2 x3
x1_eq = 1/3*cos(x2*x3)+1/6;
x2_eq = -0.1+1/9*(x1^2+sin(x3)+1.06)^0.5;
x3_eq = (3-10*pi)/60-1/20*exp(-x1*x2);

x10=0;
x20=0;
x30=0;
x1k=0;
x2k=0;
x3k=0;
norm=100;
Error=10^-5;
index=1;
i=0;
k=input("Enter the number of iterations: ");

K=[];
X1=[];
X2=[];
X3=[];
Norm=[];

while i<k && norm>=Error
    K(index,1) = i;
    if i==0
       X1(index,1) = x10;
       X2(index,1) = x20;
       X3(index,1) = x30;
       Norm(index,1) = "-";
    else
       x1k = subs(x1_eq,{x2,x3},{x20,x30});
       X1(index,1) = x1k;
       x2k = subs(x2_eq,{x1,x3},{x1k,x30});
       X2(index,1) = x2k;
       x3k = subs(x3_eq,{x1,x2},{x1k,x2k});
       X3(index,1) = x3k;
       x1norm = abs(x1k-x10);
       x2norm = abs(x2k-x20);
       x3norm = abs(x3k-x30);
       if x1norm >= x2norm && x1norm >= x3norm
           norm = x1norm;
       elseif x2norm >= x1norm && x2norm >= x3norm
           norm = x2norm;
       else
           norm = x3norm;
       end
       Norm(index,1) = norm;
    end
    x10 = x1k;
    x20 = x2k;
    x30 = x3k;
    index = index+1;
    i = i+1;
end

T = table(K,X1,X2,X3,Norm);
fprintf('\n')
disp(T)

if k>index 
    fprintf('\n')
    disp("You have exceeded the number of iterations accroding to the specified Norm!!")
end

fprintf('\n')
disp("The roots are: ")
disp("x1 = " + num2str(double(x1k)))
disp("x2 = " + num2str(double(x2k)))
disp("x3 = " + num2str(double(x3k)))