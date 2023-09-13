%Newton Gregory mehtod 
%Written by Yusuf Hani Almoadhen 202107475

clc
clear
close all;

syms x

t = [0;1;2;3;4;5;6];
I = [176;185;194;203;212;220;229];

N = "None";
Diff1=[];
Diff2=[N];
Diff3=[N;N];
Diff4=[N;N];
Diff5=[N;N;N];
Diff6=[N;N;N];

h = t(2,1)-t(1,1);

for i=1:length(I)-1
    diff1 = I(i+1,1)-I(i,1);
    Diff1(i,1) = diff1;
end

for i=1:length(Diff1)-1
    diff2 = Diff1(i+1,1)-Diff1(i,1);
    Diff2(i+1,1) = diff2;
end

for i=2:length(Diff2)-1
    diff3 = str2num(Diff2(i+1,1))-str2num(Diff2(i,1));
    Diff3(i+1,1) = diff3;
end

for i=3:length(Diff3)-1
    diff4 = str2num(Diff3(i+1,1))-str2num(Diff3(i,1));
    Diff4(i,1) = diff4;
end

for i=3:length(Diff4)-1
    diff5 = str2num(Diff4(i+1,1))-str2num(Diff4(i,1));
    Diff5(i+1,1) = diff5;
end

for i=4:length(Diff5)-1
    diff6 = str2num(Diff5(i+1,1))-str2num(Diff5(i,1));
    Diff6(i,1) = diff6;
end

Diff1(length(Diff1)+1,1) = N;

Diff2(length(Diff2)+1,1) = N;

Diff3(length(Diff3)+1,1) = N;

Diff4(length(Diff4)+1,1) = N;
Diff4(length(Diff4)+1,1) = N;

Diff5(length(Diff5)+1,1) = N;
Diff5(length(Diff5)+1,1) = N;

Diff6(length(Diff6)+1,1) = N;
Diff6(length(Diff6)+1,1) = N;
Diff6(length(Diff6)+1,1) = N;

T = table(Diff1,Diff2,Diff3,Diff4,Diff5,Diff6);
disp(T)

a0 = I(1,1);
a1 = Diff1(1,1)/h;
a2 = str2num(Diff2(2,1))/(2*h^2);
a3 = str2num(Diff3(3,1))/(6*h^3);
a4 = str2num(Diff4(3,1))/(24*h^4);
a5 = str2num(Diff5(4,1))/(120*h^5);
a6 = str2num(Diff6(4,1))/(720*h^6);

disp("a0 = " + num2str(a0))
disp("a1 = " + num2str(a1))
disp("a2 = " + num2str(a2))
disp("a3 = " + num2str(a3))
disp("a4 = " + num2str(a4))
disp("a5 = " + num2str(a5))
disp("a6 = " + num2str(a6))

Eq = a0+a1*(x-t(1,1))+a2*(x-t(1,1))*(x-t(2,1))+a3*(x-t(1,1))*(x-t(2,1))*(x-t(3,1))+a4*(x-t(1,1))*(x-t(2,1))*(x-t(3,1))*(x-t(4,1))+a5*(x-t(1,1))*(x-t(2,1))*(x-t(3,1))*(x-t(4,1))*(x-t(5,1))+a6*(x-t(1,1))*(x-t(2,1))*(x-t(3,1))*(x-t(4,1))*(x-t(5,1))*(x-t(6,1));

fprintf("\nP(x) = ")
disp(simplify(Eq))

fplot(Eq,[-5,5])
grid

xpoint = input("Enter the subtitution point x = ");
fprintf("\nAt x = %g\n",xpoint)
ypoint = double(subs(Eq,x,xpoint));
fprintf("P(%g) = %g \n",xpoint,ypoint)

close all;
fplot(Eq,[-5,5])
hold;
scatter(xpoint,ypoint,'ko','markerfacecolor','black')
grid
