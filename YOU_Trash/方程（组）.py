import sympy as sp
x=sp.Symbol('x')
y=sp.Symbol('y')
value=sp.solve([2*x-y, y-6*x+9],[x, y])
print(value)
'''方程求解，方程为2x-y=0,y-6x+9=0.
方程或者方程组不能是超越方程'''