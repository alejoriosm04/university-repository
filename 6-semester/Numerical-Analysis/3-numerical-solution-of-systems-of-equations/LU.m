%LU: Calcula la solución de un sistema de ecuaciones Ax=b 
% mediante la factorización de A=LU ya sea sin pivoteo piv=0 
% o usando pivoteo parcial piv=1. Donde A es de tamaño nxn y b de tamaño nx1

function [x, L, U] = LU(A,b,n,Piv)
    P=eye(n);
    L=P;
    for k=1:n-1
        if Piv==1
            [A, P]=pivLU(A,P,n,k);
        end
        for i=k+1:n
            M=A(i,k)/A(k,k);
            for j=k:n
                A(i,j)=A(i,j)-M*A(k,j);
            end
            A(i,k)=M;
        end
    end
    U=triu(A);
    L=L+tril(A,-1);
    B=P*b;
    LB=[L,B];
    z=sustpro(LB,n);
    Uz=[U,z];
    x=sustreg(Uz,n);
end