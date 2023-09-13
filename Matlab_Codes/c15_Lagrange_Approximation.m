%Lagrange Approximation method 
%Written by Yusuf Hani Almoadhen 202107475

clc
clear
close all;

syms x

X = [-1;1;2];
Y = [-1;1;8];
K=[];

for i=1:length(X)
    K(i,1) = i;
end

Pi = 1;
Sum = 0;
Lx = [];

for i=1:length(X)
    for j=1:length(Y)
        if i~=j
            L = (x-X(j,1))/(X(i,1)-X(j,1));
            Pi = expand(Pi*L);
        end
    end
    Lx = [Lx;expand(Pi)];
    Pi = 1;

end
T = table(K,X,Y,Lx);

for i=1:length(Lx)
    Sum = Sum + Lx(i,1)*Y(i,1);
end

fprintf("Lagrange Interpolation \n\n")
disp(T)
fprintf("P(x) = ")
sympref('PolynomialDisplayStyle','descend');
disp(simplify(Sum))