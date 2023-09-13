%Substitution method 

clc
clear 
close all;

syms x

y = 3-x^2;
f = x^4-6*x^2+x+4;
 
sol = double(vpasolve(f,x));
y1 = double(subs(y,x,sol(1,1)));
y2 = double(subs(y,x,sol(2,1)));
y3 = double(subs(y,x,sol(3,1)));
y4 = double(subs(y,x,sol(4,1)));

disp("The roots are ")
disp("("+num2str(sol(1,1))+","+num2str(y1)+")")
disp("("+num2str(sol(2,1))+","+num2str(y2)+")")
disp("("+num2str(sol(3,1))+","+num2str(y3)+")")
disp("("+num2str(sol(4,1))+","+num2str(y4)+")")
