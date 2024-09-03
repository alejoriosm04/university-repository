%Newton: se ingresa el valor inicial (x0), la tolerancia del error (Tol) y el màximo nùmero de iteraciones (niter) 

function [n,xn,fm,dfm,E] = newton(x0,Tol,niter)
    syms x

        f=sin(2*x)-(x/(3))^3+0.1;
        df=diff(f);
        c=0;
        fm(c+1) = eval(subs(f,x0));
        fe=fm(c+1);
        dfm = eval(subs(df,x0));
        dfe=dfm;
        E(c+1)=Tol+1;
        error=E(c+1);
        xn=x0;
        while error>Tol 
            xn=x0-fe/dfe;
            fm(c+2)=eval(subs(f,xn));
            fe=fm(c+2);
            dfm=eval(subs(df,xn));
            dfe=dfm;
            E(c+2)=abs(xn-x0);
            error=E(c+2);
            x0=xn;
            c=c+1;
        end
        if fe==0
           s=x0;
           n=c;
           fprintf('%f es raiz de f(x) \n',x0)

        elseif error<Tol
           s=x0;
           n=c;
           fprintf('%f es una aproximación de una raiz de f(x) con una tolerancia= %f \n',x0,Tol)

        elseif dfe==0
           s=x0;
           n=c;
           fprintf('%f es una posible raiz múltiple de f(x) \n',x0)
        else 
           s=x0;
           n=c;
           fprintf('Fracasó en %f iteraciones \n',niter) 
        end
        
end