from pde import CartesianGrid, plot_kymograph, ScalarField, MemoryStorage, PDE
import numpy as np
import matplotlib.pyplot as plt

T_origin=25#初始温度
T_Kelvin=273.15#开式温度换算
x_max=1.5e-4#厚度
rho=1794.07#密度
c=1465.38#比热容
llambda=0.29#热导率
alpha=llambda/(rho*c)
h=llambda/x_max

xstep=15
tstep=10
tmax=500
bc_T='(-0.29)*c.diff(x)+(0.00015/0.29)*(Piecewise( \
    (25+273.15,And(0<=tt,tt<=20)), \
    (25+30*tt+273.15,And(20<tt,tt<=25)), \
    (175+273.15,And(25<tt,tt<=197.5)), \
    (175+4*tt+273.15,And(197.5<tt,tt<=202.5)), \
    (195+273.15,And(202.5<tt,tt<=233)), \
    (195+8*tt+273.15,And(233<tt,tt<=238)), \
    (235+273.15,And(238<tt,tt<=268.5)), \
    (235+4*tt+273.15,And(268.5<tt,tt<=273.5)), \
    (255+273.15,And(273.5<tt,tt<=344.5)), \
    (255-(230/91)*tt+273.15,And(344.5<tt,tt<=435.5)), \
    (25+273.15,And(435.5<tt,tt<=500))).subs(tt,t))'
#bc_T='(-0.29)*c.diff(x)+(0.00015/0.29)*(Piecewise((25+273.15,And(0<=tt,tt<=250)),(255+273.15,And(250<tt,tt<=500))))'
#bc_T='(0.00015/0.29)*(Piecewise((25+273.15,And(0<=tt,tt<=250)),(255+273.15,And(250<tt,tt<=500))).subs(tt,t))'
grid = CartesianGrid([[0, x_max]], [int(xstep)])#,periodic=False)
state=ScalarField(grid=grid,data=T_origin+T_Kelvin)

eq = PDE(rhs={'c': 'a*laplace(c)'}, 
    bc={'value_expression': bc_T},
    consts={'a':alpha})

storage = MemoryStorage()
eq.solve(state, t_range=tmax, tracker=storage.tracker(tstep))

def kymograph_pic():
    plot_kymograph(storage)

def temp_curve():
    p=[]
    for i in range(int(tmax/tstep)):
        p.append(storage.data[i][-1])
    
    q=np.asarray(p)
    plt.plot(np.linspace(0,tmax,int(tmax/tstep),endpoint=1),q,label='Temperature')
    plt.xlabel('Time')
    plt.ylabel('Temprature')
    plt.show()

#kymograph_pic()
temp_curve()