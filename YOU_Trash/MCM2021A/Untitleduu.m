h=0.1;%所取时间点间隔
ts=[0:h:500];%时间区间
x0 = [10;200];%初始条件
opt=odeset('reltol',1e-6,'abstol',1e-9);%相对误差1e-6，绝对误差1e-9
tm=[];
c0=[];
for c=-1:0.1:1
    [t,x]=ode45(@(t,x)INFY(t,x,c),ts,x0,opt);%使用5级4阶龙格—库塔公式计算
    en=diff(x(:,2));
    tm=[tm log(-en(1000)/0.1)];
    c0=[c0 c];
end
plot(c0,tm,'-*')