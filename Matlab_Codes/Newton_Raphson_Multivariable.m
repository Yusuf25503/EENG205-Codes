%Newton Raphson method (Multivariable)
%Written by Yusuf Hani Almoadhen 202107475

clc
clear
close all;

syms v i   

f1 = v^2-2*v-i+0.5;
f2 = v^2+4*i^2-4;

df1v = diff(f1,v);
df1i = diff(f1,i);
df2v = diff(f2,v);
df2i = diff(f2,i);

v0=2;
i0=0.25;

index=1;
k=input("Enter the number of iterations: ");
norm=100;
Error=10^-6;

K=[];
V0=[];
I0=[];
J1=[];
J2=[];
J3=[];
J4=[];
F1=[];
F2=[];
V=[];
I=[];
Norm=[];

while index<k && norm>=Error
    K(index,1) = index;
    V0(index,1) = v0;
    I0(index,1) = i0;
    init = [v0;i0];
    dF1V = subs(df1v,{v,i},{v0,i0});
    J1(index,1) = dF1V;
    dF1I = subs(df1i,{v,i},{v0,i0});
    J2(index,1) = dF1I;
    dF2V = subs(df2v,{v,i},{v0,i0});
    J3(index,1) = dF2V;
    dF2I = subs(df2i,{v,i},{v0,i0});
    J4(index,1) = dF2I;
    J = [dF1V dF1I; dF2V dF2I];
    f1_sub = subs(f1,{v,i},{v0,i0});
    F1(index,1) = f1_sub;
    f2_sub = subs(f2,{v,i},{v0,i0});
    F2(index,1) = f2_sub;
    f = [f1_sub; f2_sub];
    Sol = init - inv(J)*f;
    V(index,1) = Sol(1,1);
    I(index,1) = Sol(2,1);
    vNorm = abs(Sol(1,1)-v0);
    iNorm = abs(Sol(2,1)-i0);
    if vNorm > iNorm
        norm = vNorm;
    else
        norm = iNorm;
    end
    Norm(index,1) = norm;
    v0 = Sol(1,1);
    i0 = Sol(2,1);
    index = index+1;
end

fprintf('\n')
T = table(K,V0,I0,J1,J2,J3,J4,F1,F2,V,I,Norm);
disp(T)

if k>index
    fprintf('\n')
    disp("You have exceeded the number of iterations accroding to the specified Norm!!")
end

fprintf('\n')
disp("The roots are: ")
disp("v = " + num2str(double(Sol(1,1))))
disp("i = " + num2str(double(Sol(2,1))))
