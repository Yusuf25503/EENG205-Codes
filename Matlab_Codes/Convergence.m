%Convergence
%Written by Yusuf Hani Yusuf 

clc
clear
close all;

syms L21 L31 L32 U11 U12 U13 U22 U23 U33 x

A = [8 -1 4; 3 5 -2; 2 6 1];

L = [1 0 0; L21 1 0; L31 L32 1];
U = [U11 U12 U13; 0 U22 U23; 0 0 U33];

%Equations
for i=1:3
    for j=1:3
        Eq(i,j)=L(i,:)*U(:,j)-A(i,j);
    end
end

u11 = double(vpasolve(Eq(1,1)));
u12 = double(vpasolve(Eq(1,2)));
u13 = double(vpasolve(Eq(1,3)));
l21 = double(vpasolve(subs(Eq(2,1),{U11},{u11})));
u22 = double(vpasolve(subs(Eq(2,2),{L21 U12},{l21 u12})));
u23 = double(vpasolve(subs(Eq(2,3),{L21 U13},{l21 u13})));
l31 = double(vpasolve(subs(Eq(3,1),U11,u11)));
l32 = double(vpasolve(subs(Eq(3,2),{L31 U12 U22},{l31 u12 u22})));
u33 = double(vpasolve(subs(Eq(3,3),{L31 L32 U13 U23},{l31 l32 u13 u23})));

%U Matrix
Upper = [u11 u12 u13; 0 u22 u23; 0 0 u33];
%L Matrix
Lower = [1 0 0; l21 1 0; l31 l32 1];

%D Matrix
for i=1:3
    for j=1:3
        if i==j
            Diag(i,j)=A(i,j);
        else
            Diag(i,j)=0;
        end
    end
end
Low = [A(1,1) 0 0; A(2,1) A(2,2) 0; A(3,1) A(3,2) A(3,3)];
Up = A - Low;
for i=1:3
    for j=1:3
        if i==j
            I(i,j)=1;
        else
            I(i,j)=0;
        end
    end
end
T = Diag^-1*(Low+Up)-I;
%Finding 1st Norm of T Matrix
column=[];
col_sum=0;
for col=1:3
    for row=1:3
        col_sum = col_sum+abs(T(row,col));
    end
    column(col,1) = col_sum;
    col_sum=0;
end
if abs(column(1,1))>abs(column(2,1)) && abs(column(1,1))>abs(column(3,1))
    T1 = abs(column(1,1));
elseif abs(column(2,1))>abs(column(1,1)) && abs(column(2,1))>abs(column(3,1))
    T1 = abs(column(2,1));
else
    T1 = abs(column(3,1));
end
%Finding the 2nd Norm of T Matrix
%T_transpose=[T(1,1) T(2,1) T(3,1); T(1,2) T(2,2) T(3,2); T(1,3) T(2,3) T(3,3)];
for i=1:3
    for j=1:3
        TT(j,i) = T(i,j);
    end
end
V = TT*T-x*I;
i_col = V(1,1)*(V(2,2)*V(3,3)-V(2,3)*V(3,2));
j_col = -V(1,2)*(V(2,1)*V(3,3)-V(2,3)*V(3,1));
k_col = V(1,3)*(V(2,1)*V(3,2)-V(2,2)*V(3,1));
detEq = simplify(i_col+j_col+k_col);
sol = double(vpasolve(detEq==0,x));
if abs(sol(1))>abs(sol(2)) && abs(sol(1))>abs(sol(3))
    T2 = sqrt(abs(sol(1)));
elseif abs(sol(2))>abs(sol(1)) && abs(sol(2))>abs(sol(3))
    T2 = sqrt(abs(sol(2)));
else
    T2 = sqrt(abs(sol(3)));
end
%Finding the infinity Norm of T MAtrix
Row=[];
row_sum=0;
for row=1:3
    for col=1:3
        row_sum = row_sum+abs(T(row,col));
    end
    Row(row,1)=row_sum;
    row_sum=0;
end
if abs(Row(1,1))>abs(Row(2,1)) && abs(Row(1,1))>abs(Row(3,1))
    Tinf = abs(Row(1,1));
elseif abs(Row(2,1))>abs(Row(1,1)) && abs(Row(2,1))>abs(Row(3,1))
    Tinf = abs(Row(2,1));
else
    Tinf = abs(Row(3,1));
end

disp("||T||∞ = " + Tinf)
disp("||T||1 = " + T1)
disp("||T||2 = " + T2)

if T2 > 1
    disp("Divergent")
else
    disp("Convergent")
end
