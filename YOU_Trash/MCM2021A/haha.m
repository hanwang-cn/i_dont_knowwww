h=0.1;%所取时间点间隔
ts=[0:h:50];%时间区间
x0 = [9.8734/24.6835;7.0886/24.6835;1];%初始条件
opt=odeset('reltol',1e-6,'abstol',1e-9);%相对误差1e-6，绝对误差1e-9
[t,x]=ode45(@Kn1,ts,x0,opt);%使用5级4阶龙格—库塔公式计算
plot(t,x(:,1),t,x(:,2),t,x(:,3),'LineWidth',2),grid,legend;