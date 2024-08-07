import pandas as pd
import numpy as np
import math
import wdb

x = np.pi/4

Tol = 0.5E-3

n=0
fm=[]
fx=((-1)**n)*(x**((2*n)+1))/math.factorial((2*n)+1)
E=[]
E.append(100)
fm.append(fx)
while E[n]>Tol:
     n+=1
     fx+=((-1)**n)*(x**(2*n+1))/math.factorial(2*n+1)
     fm.append(fx)
     error=abs(fm[n]-fm[n-1])
     E.append(error)

Tabla=[E,fm]
Tabla=np.transpose(Tabla)
df=pd.DataFrame(Tabla, columns=["Error", "senx"])

print(df)