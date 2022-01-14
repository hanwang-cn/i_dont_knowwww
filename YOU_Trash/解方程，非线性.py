from turtle import color
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

def up(a):
    return 1100*np.exp(-0.1386*a)
def down(a):
    return 6600*(np.exp(-0.1155*a)-np.exp(-0.1386*a))
def func(a):
    return down(a)-400

root=fsolve(func,x0=3)
t=np.arange(0,30,0.01)
zero=np.zeros(3000)
up_t=np.array([up(i) for i in t])
down_t=np.array([down(i) for i in t])

plt.text(5,750,root,fontsize=16)
plt.plot(t, up_t)
plt.plot(t, down_t)

plt.show()

