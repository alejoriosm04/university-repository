import pandas as pd
import numpy as np
import math
import wdb
#wdb.set_trace()
x = np.pi/4

Tol = 0.5E-3

n=0
#N=[]
fm=[]
fx=((-1)**n)*(x**(2*n))/math.factorial(2*n)
E=[]
E.append(100)
fm.append(fx)
#N.append(n)
while E[n]>Tol:
     n+=1
     #N.append(n)
     fx+=((-1)**n)*(x**(2*n))/math.factorial(2*n)
     fm.append(fx)
     error=abs(fm[n]-fm[n-1])
     E.append(error)

Tabla=[E,fm]
Tabla=np.transpose(Tabla)
df=pd.DataFrame(Tabla, columns=["Error", "cosx"])
print(df)  
