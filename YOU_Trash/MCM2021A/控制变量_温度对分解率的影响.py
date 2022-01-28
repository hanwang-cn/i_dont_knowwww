#天数能少尽量少，300天没有100天效果好

from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

def deriv(t, w,tem,moist):
    n0,n1,n2,n3,n4,n5,x=w.tolist()
    dn0dt = n0*np.log(1.399549*x/(n0+11.17546*n1+0.448686*n2+0.284405*n3+0.101572*n4+0.433724*n5-0.863503))
    dn1dt = n1*np.log(1.399549*x/((1/11.17546)*n0+n1+0.375706*n2+7.783609*n3+196.1559*n4+4.485611*n5-0.450677))
    dn2dt = n2*np.log(1.399549*x/((1/0.448686)*n0+(1/0.375706)*n1+n2+10.12895*n3+0.149357*n4+0.144114*n5-0.035456))
    dn3dt = n3*np.log(1.399549*x/((1/0.284405)*n0+(1/7.782609)*n1+(1/10.12895)*n2+n3+5.001182*n4+5.563094*n5+0.37097))
    dn4dt = n4*np.log(1.399549*x/((1/0.101572)*n0+(1/196.1559)*n1+(1/0.149357)*n2+(1/5.001182)*n3+n4+15141.41*n5+0.00074))
    dn5dt = n5*np.log(1.399549*x/((1/0.433724)*n0+(1/4.485611)*n1+(1/0.144114)*n2+(1/0.563014)*n3+(1/15141.41)*n4+n5+0.92217))
    dxdt = -1*x*(0.000832*n0+0.000373*n1+0.0000287*n2+0.00000246*n3+0.07549*n4+0.000000466*n5)

    if (tem<18):
        dn0dt=dn0dt-(18-tem)/18*n0
        dn1dt=dn1dt-(24-tem)/24*n1
        dn2dt=dn2dt-(24-tem)/24*n2
        dn3dt=dn3dt-(27-tem)/27*n3
        dn4dt=dn4dt-(27-tem)/27*n4
        dn5dt=dn5dt-(27-tem)/27*n5
    elif (tem>=18 and tem<24):
        dn1dt=dn1dt-(24-tem)/24*n1
        dn2dt=dn2dt-(24-tem)/24*n2
        dn3dt=dn3dt-(27-tem)/27*n3
        dn5dt=dn5dt-(27-tem)/27*n5
    elif (tem>=24 and tem<27):
        dn3dt=dn3dt-(27-tem)/27*n3
        dn5dt=dn5dt-(27-tem)/27*n5

    if (moist<96 and moist>69):
        dn5dt=dn5dt-(96-moist)/96*n5
    elif (moist<=69 and moist>=50):
        dn5dt=dn5dt-(96-moist)/96*n5
        dn3dt=dn3dt-(69-moist)/69*n3
    elif (moist<50 and moist>48):
        dn5dt=dn5dt-(96-moist)/96*n5
        dn3dt=dn3dt-(69-moist)/69*n3
        dn4dt=dn4dt-(50-moist)/50*n4
    elif (moist<=48 and moist>=27):
        dn5dt=dn5dt-(96-moist)/96*n5
        dn3dt=dn3dt-(69-moist)/69*n3
        dn4dt=dn4dt-(50-moist)/50*n4
        dn2dt=dn2dt-(48-moist)/48*n2
    elif (moist<27):
        dn5dt=dn5dt-(96-moist)/96*n5
        dn3dt=dn3dt-(69-moist)/69*n3
        dn4dt=dn4dt-(50-moist)/50*n4
        dn2dt=dn2dt-(48-moist)/48*n2
        dn1dt=dn1dt-(27-moist)/48*n1


    return dn0dt,dn1dt,dn2dt,dn3dt,dn4dt,dn5dt,dxdt

y_0=(9.8734,7.0886,6.9620,5.4430,3.5443,8.6076,100)
t=np.linspace(0,100,101,endpoint=True)
y_temp=[]

temp=np.linspace(3,30,100,endpoint=True)

    
for temm in temp:
    y_b=solve_ivp(deriv,t_span=(0,100),y0=y_0,method='DOP853', t_eval=t,args=(temm,100),rtol=3e-14,atol=3e-18)
    y_temp.append(y_b.y[6][-1])

fig=plt.figure(dpi=120,tight_layout=True)

def showplt():
    plt.scatter(temp,y_temp,color='k',marker='*',label='Data Point')
    plt.show()


def writexlsx():
    data = {'temp':temp,'rate': y_temp}
    df = DataFrame(data)
    df.to_excel('temp_decompos.xlsx')


writexlsx()
showplt()
#print(y_temp)