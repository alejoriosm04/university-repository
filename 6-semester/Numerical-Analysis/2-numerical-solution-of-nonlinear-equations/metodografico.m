%método gráfico
clc
clear all 
close all


  x=8:0.0001:14;

  f=-x.^2+10*log(x.^3)+1;
  figure
  plot(x,f,'b*','LineWidth',0.1)
%   ylim([-1,1]);
%   xlim([-5,-4.8]);



