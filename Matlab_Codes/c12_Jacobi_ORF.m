%Gauss Jacobi method (with ORF)
%Written by Yusuf Hani Almoadhen 202107475

clc
clear
close all;

syms v1 v2 v3 x

A = [3 1 -1; 1 -5 3; 2 2 10];
B = [302;648;1548];

w = input("Enter the value of w = ");
if w>1
    disp("Over-relaxing ")
elseif w<1
    disp("Under-relaxing ")
else
    disp("Normal Gauss Jacobi ")
end
fprintf('\n')

v10=0;
v20=0;
v30=0;
v1k=0;
v2k=0;
v3k=0;
norm=100;
Error=0.0003;
index=1;
i=0;
k=input("Enter the number of iterations: ");

K=[];
V1=[];
V2=[];
V3=[];
Norm=[];

v1_eq = v1 + w/A(1,1)*(B(1,1)-A(1,1)*v1-A(1,2)*v2-A(1,3)*v3);
v2_eq = v2 + w/A(2,2)*(B(2,1)-A(2,1)*v1-A(2,2)*v2-A(2,3)*v3);
v3_eq = v3 + w/A(3,3)*(B(3,1)-A(3,1)*v1-A(3,2)*v2-A(3,3)*v3);

while i<k && norm>=Error
    K(index,1) = i;
    if i==0
        V1(index,1) = v10;
        V2(index,1) = v20;
        V3(index,1) = v30;
        V = [v10;v20;v30];
    else
        v1k = subs(v1_eq,{v1,v2,v3},{v10,v20,v30});
        V1(index,1) = v1k;
        v2k = subs(v2_eq,{v1,v2,v3},{v10,v20,v30});
        V2(index,1) = v2k;
        v3k = subs(v3_eq,{v1,v2,v3},{v10,v20,v30});
        V3(index,1) = v3k;
        V = [v1k;v2k;v3k];
    end
    normVector = abs(B-A*V);
    if normVector(1,1) >= normVector(2,1) && normVector(1,1) >= normVector(3,1)
        norm = normVector(1,1);
    elseif normVector(2,1) >= normVector(1,1) && normVector(2,1) >= normVector(3,1)
        norm = normVector(2,1);
    else
        norm = normVector(3,1);
    end
    Norm(index,1) = norm;
    v10 = v1k;
    v20 = v2k;
    v30 = v3k;
    index = index+1;
    i = i+1;
end
fprintf('\n')
T = table(K,V1,V2,V3,Norm);
disp(T)

if k>index
    fprintf('\n')
    disp("You have exceeded the number of iterations accroding to the specified Norm!!")
end

disp("The roots are: ")
disp("v1 = " + num2str(double(v1k)))
disp("v2 = " + num2str(double(v2k)))
disp("v3 = " + num2str(double(v3k)))