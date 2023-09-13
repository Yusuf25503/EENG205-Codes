%Optimal Relaxation Factor (ORF)
%Written by Yusuf Hani Almoadhen 202107475

clc
clear
close all;

syms x

A = [4 3 0; 3 4 -1; 0 -1 4];

%Finding wopt
for i=1:3
    for j=1:3
        if i==j
            D(i,j) = A(i,j);
            I(i,j) = 1;
        else
            D(i,j) = 0;
            I(i,j) = 0;
        end
    end
end
for i=1:3
    for j=1:3
        if i>j
            L(i,j) = A(i,j);
        else
            L(i,j) = 0;
        end
    end
end
U = A-L;

T = inv(D)*(L+U)-I;

V = T-x*I;
%Finding Determinate of V matrix
V = T-x*I;
i_col = V(1,1)*(V(2,2)*V(3,3)-V(2,3)*V(3,2));
j_col = -V(1,2)*(V(2,1)*V(3,3)-V(2,3)*V(1,3));
k_col = V(1,3)*(V(2,1)*V(3,2)-V(2,2)*V(1,3));
detEq = simplify(i_col+j_col+k_col);
sol = double(abs(vpasolve(detEq)));
if sol(1)>sol(2) && sol(1)>sol(3)
    Eigen = sol(1);
elseif sol(2)>sol(1) && sol(2)>sol(3)
    Eigen = sol(2);
else
    Eigen = sol(3);
end
w = 2/(1+sqrt(1-Eigen^2));
disp("w = " + num2str(w))
if w>1
    disp("Over-relaxing ")
elseif w<1
    disp("Under-relaxing ")
else
    disp("Normal Gauss Jacobi ")
end
