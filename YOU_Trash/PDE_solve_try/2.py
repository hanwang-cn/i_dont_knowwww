from pde import CartesianGrid, ScalarField, MemoryStorage, DiffusionPDE, plot_kymograph
import numpy as np
import matplotlib.pyplot as plt

T_origin=25#初始温度
T_Kelvin=273.15#开式温度换算
x_max=1.5e-4#厚度
rho=1794.07#密度
c=1465.38#比热容
llambda=0.29#热导率
alpha=llambda/(rho*c)
h=1.88#换热系数

def main():
    xstep=5
    tstep=1
    v=73.82/60#Unit:cm/s
    tmin=0
    tmax=500
    bc_T=f'-1*{llambda}/{h}*c.diff(x)+(Piecewise(\
        ((25+{T_Kelvin}),tt<=20/{v}),\
        ((25+150/{v}*(tt-20/{v})+{T_Kelvin}),And(20/{v}<tt,tt<=25/{v})),\
        ((175+{T_Kelvin}),And(25/{v}<tt,tt<=197.5/{v})),\
        ((175+20/{v}*(tt-197.5/{v})+{T_Kelvin}),And(197.5/{v}<tt,tt<=202.5/{v})),\
        ((195+{T_Kelvin}),And(202.5/{v}<tt,tt<=233/{v})),\
        ((195+40/{v}*(tt-233/{v})+{T_Kelvin}),And(233/{v}<tt,tt<=238/{v})),\
        ((235+{T_Kelvin}),And(238/{v}<tt,tt<=268.5/{v})),\
        ((235+20/{v}*(tt-268.5/{v})+{T_Kelvin}),And(268.5/{v}<tt,tt<=273.5/{v})),\
        ((255+{T_Kelvin}),And(273.5/{v}<tt,tt<=344.5/{v})),\
        ((255-230/{v}*(tt-344.5/{v})+{T_Kelvin}),And(344.5/{v}<tt,tt<=435.5/{v})),\
        ((25+{T_Kelvin}),true)).subs(tt,t))' 
        #ture需要小写,f'string'string里面有{}可以传递全局参数参数
    grid = CartesianGrid([[0, x_max]], [int(xstep)],periodic=False)
    state=ScalarField(grid=grid,data=T_origin+T_Kelvin)

    eq = DiffusionPDE(diffusivity=alpha, bc={'value_expression':bc_T},)

    storage = MemoryStorage()
    eq.solve(state, t_range=(tmin,tmax),dt=1e-3, tracker=storage.tracker(tstep))

    def temp_curve():
        p=[]
        for i in range(int((tmax-tmin)/tstep)):
            p.append(storage.data[i][-1])
    
        q=np.asarray(p)
        plt.plot(np.linspace(tmin,tmax,int((tmax-tmin)/tstep),endpoint=0),q,label='Temperature')
        plt.xlabel('Time')
        plt.ylabel('Temprature')
        plt.show()

    def plotky():
        plot_kymograph(storage)

    #temp_curve()
    plotky()

if __name__=='__main__':
    main()