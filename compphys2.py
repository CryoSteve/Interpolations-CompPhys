from sympy import *
import numpy as np
from functools import reduce
from operator import mul
import pandas as pd
def prod(lst):
    return reduce(mul, lst, 1.0)

def DivDiffTable( x= [],y = [], numofpairs = 0):
  coef = np.zeros([numofpairs,numofpairs])
  coef[:,0] = y
  for j in range(1,n):
    for i in range(n-j):
      coef[i][j] = \
      (coef[i+1][j-1]-coef[i][j-1])/(x[i+j]-x[i])
  #np.insert(coef,0,(x),axis=1)
  return coef
def newton_poly(coef,x_data,x):
  n = len(x_data)-1
  p = coef[0][n]
  for k in range(1,n+1): 
    p = coef[0][n-k] + (x - x_data[n-k]) * p
  return p
  

def LagrangeInterpolate( xs :list,ys :list,x,mode:bool):
  lagrangepoly = ""
  InterpVal = 0.0
  num = len(xs)
  for i in range(num):
    term=ys[i]
    terms=f"{ys[i]}"
    for j in range(num):
      if(i!=j):
        term*=(x-xs[j])/(xs[i]-xs[j])
        terms+=f" * (x- {xs[j]:.5f})/({xs[i]:.5f}-{xs[j]:.5f})"
    InterpVal+=term
    lagrangepoly+=terms
    if(i<num-1):
      lagrangepoly+= " + "
  if(mode == False):
    return InterpVal
  else:
    return lagrangepoly
  """n = len(xs)
  return sum( \
  ys[j]*prod((x-xs[i])/(ys[j]-ys[i]) \
  for i in range(n) \
  if i != j) \
  for j in range(n)\
  )
  pass"""

#main code 
n = int(input("How many pairs of data (where (x,y) counts as one pair) would you like to use?\n"))
xarr = [0 for k in range(n)]
yarr = [0 for h in range(n)]
#print(xarr)
for i in range(n):
  xarr[i] = float(input("\nEnter your desired x value for entry number "+str(i)+" : "))
  yarr[i] = float(input("\nEnter your desired y value for entry number "+str(i)+" : "))
  
appro = []
n2 = int(input("Enter the amount of values that you want to be interpolated: "))
for i in range(n2):
  appro.append(float(input("Enter value # "+str(i+1)+": ")))

print(pd.DataFrame(DivDiffTable(xarr,yarr,n)))
X = symbols('x')
print("The final Newton Polynomial can be epressed as: f() = "+str((newton_poly(DivDiffTable(xarr,yarr,n),xarr,X))))
if(n2>1):
  for i in range(n2):
    print("The interpolated values in order of entering for Divided Differences are: ", newton_poly(DivDiffTable(xarr,yarr,n),xarr,float(appro[i])))
else:
  print("The interpolated value for Divided Differences is ", newton_poly(DivDiffTable(xarr,yarr,n),xarr,appro[0]))
print("The final Lagrange polynomial is ",LagrangeInterpolate(xarr,yarr,X,True))
print("The interpolated Lagrange values are: ")

for i in range(n2):
  print(LagrangeInterpolate(xarr,yarr,float(appro[i]),False))


