%Punto fijo: se ingresa el valor inicial (x0), la tolerancia del error (Tol) y el màximo nùmero de iteraciones (niter) 

function [n,xn,fm,E] = pf(x0,Tol,niter,A)
    syms x
%      f=-2*x+sin(sqrt(x));
%     g=-x+sin(sqrt(x));
%    f=sin(x)-2.1*sqrt(x)+1+A/10;
%   g=((sin(x)+1+A/10)/2.1)^2;
 f=sin(x-A*10^(-3))-x;
 g=sin(x-A*10^(-3));
%  f=2*sin(sqrt(abs(x+2)))-x;
%  g=2*sin(sqrt(abs(x+2)));
 %g=-log(x+2)-2*x;
%  f=log(x+2)+3*x;
%  g=exp(-3*x)-2;
        c=0;
        fm(c+1) = eval(subs(f,x0));
        fe=fm(c+1);
        E(c+1)=Tol+1;
        error=E(c+1);
        xn(c+1)=x0;
        N(c+1)=c;
        while error>Tol && fe~=0 && c<niter
            xn(c+2)=eval(subs(g,x0));
            fm(c+2)=eval(subs(f,xn(c+2)));
            fe=fm(c+2);
            E(c+2)=abs((xn(c+2)-x0));
            error=E(c+2);
            x0=xn(c+2);
            N(c+2)=c+1;
            c=c+1;
        end
        if fe==0
           s=x0;
           n=c;
           fprintf('%f es raiz de f(x)',x0)
           disp(['      n                Xn                   Fx                   Error'])
           D=[N' xn' fm' E'];
        elseif error<Tol
           s=x0;
           n=c;
           %fprintf('%f es una aproximación de una raiz de f(x) con una tolerancia= %f',x0,Tol)
           disp(['      n                Xn                   Fx                   Error'])
           D=[N' xn' fm' E'];
            disp(D)
        else 
           s=x0;
           n=c;
           fprintf('Fracasó en %f iteraciones',niter) 
        end       
end