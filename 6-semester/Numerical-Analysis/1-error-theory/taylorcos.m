%Esta funci�in calcula la serie de taylor del cos(theta) con una tolerancia
% tol determinada.

function [cosx, E, n] = taylorcos(theta,tol)
    n=0;
    E(n+1)=100;
    cosx(n+1)=(((-1)^n)*(theta^(2*n)))/factorial(2*n);
    while E(n+1)>=tol
        n=n+1;
        cosx(n+1)=cosx(n)+(((-1)^n)*(theta^(2*n)))/factorial(2*n);
        E(n+1)=abs(cosx(n+1)-cosx(n));
    end
end