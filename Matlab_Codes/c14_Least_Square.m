%Least Square method 
%Written by Yusuf Hani Almoadhen 202107475

clc
clear
close all;

syms x

X = [0;1;2;3;4;5;6];
Y = [1.0;1.8;1.3;2.5;6.3;10;15];

sum1=0;
sumx=0;
sumx2=0;
sumx3=0;
sumx4=0;
sumy=0;
sumyx=0;
sumyx2=0;

One=[];
X2=[];
X3=[];
X4=[];
YX=[];
YX2=[];

for i=1:length(X)
    One(i,1) = 1;
    sum1 = sum1+1;
    sumx = sumx+X(i,1);
    X2(i,1) = X(i,1)^2;
    sumx2 = sumx2+X(i,1)^2;
    X3(i,1) = X(i,1)^3;
    sumx3 = sumx3+X(i,1)^3;
    X4(i,1) = X(i,1)^4;
    sumx4 = sumx4+X(i,1)^4;
    sumy = sumy+Y(i,1);
    YX(i,1) = Y(i,1)*X(i,1);
    sumyx = sumyx+Y(i,1)*X(i,1);
    YX2(i,1) = Y(i,1)*X(i,1)^2;
    sumyx2 = sumyx2+Y(i,1)*X(i,1)^2;
end

One(length(X)+1,1) = sum1;
X(length(X)+1,1) = sumx;
X2(length(X),1) = sumx2;
X3(length(X),1) = sumx3;
X4(length(X),1) = sumx4;
Y(length(X),1) = sumy;
YX(length(X),1) = sumyx;
YX2(length(X),1) = sumyx2;

T = table(One,X,Y,X2,X3,X4,YX,YX2);
disp(T)

A = [sum1 sumx sumx2;
    sumx sumx2 sumx3;
    sumx2 sumx3 sumx4];

b = [sumy;sumyx;sumyx2];

Sol = inv(A)*b;

Eq = 0;
j=0:length(Sol)-1;
for i=1:length(Sol)
    Eq = Eq+Sol(i,1)*x^j(1,i);
end
fprintf("\n\n P(x)= ")
sympref('PolynomialDisplayStyle','descend');
disp(simplify(Eq))