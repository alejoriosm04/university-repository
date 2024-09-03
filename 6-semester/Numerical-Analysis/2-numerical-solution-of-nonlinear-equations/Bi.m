%busquedas incrementales: se ingresa el valor inicial de x (x0), el tamaño de paso(Delta) y el màximo nùmero de iteraciones (niter) 

function [solucion,c] = Bi(x0,Delta,niter)
    syms x
    %f=9.8*x*(1-exp(-15*9/x))/15-35;
    f=x^2-5*x+6*sin(x);
    f0=eval(subs(f,x0));
    if f0==0
        solucion=x0;
        fprintf('%f es raiz de f(x)',x0)
    else
        x1=x0+Delta;
        c=1;                 %contador
        f1=eval(subs(f,x1));
        while f0*f1>0 && c<=niter
            x0=x1;
            f0=f1;
            x1=x0+Delta;
            f1=eval(subs(f,x1));
            c=c+1;
        end
        if f1==0             %verifica que sea raiz
            solucion=x1;
            fprintf('%f es raiz de f(x)',x1)
        elseif f0*f1<0                             %verifica cambio de signo
            solucion=x1;
            fprintf('Existe una raiz de f(x) entre %f y %f',x0,x1)
        else                                       %verifica fracaso
            solucion=x1;
           fprintf('Fracasó en %f iteraciones',niter) 
        end
    end
    
end