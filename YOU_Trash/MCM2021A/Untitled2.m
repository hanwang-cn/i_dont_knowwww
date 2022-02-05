h=0.1;%所取时间点间隔
ts=[0:0.1:300];%时间区间
x0 = [9.8734;7.0886;6.9620;5.4430;3.5443;8.6076;100];%初始条件
opt=odeset('reltol',1e-6,'abstol',1e-9);%相对误差1e-6，绝对误差1e-9
moist=100;
[t,x]=ode45(@(t,x)Kn1(t,x,moist),ts,x0,opt);
% ts=[180:0.1:500];
% x1=x(end,:);
% temp=30;
% moist=10;
% [t2,xn]=ode45(@(t,x)Kn1(t,x,temp,moist),ts,x1',opt);
% x=[x;xn];
% t=[t1;t2];
plot(t,x(:,1),t,x(:,2),t,x(:,3),t,x(:,4),t,x(:,5),t,x(:,6))
% for moist=10:0.1:90
% temp=30;
% [t,x]=ode45(@(t,x)Kn1(t,x,temp,moist),ts,x0,opt);%使用5级4阶龙格—库塔公式计算
% moi=[moi;moist];
% xx=[xx;x(end,7)];
% end
% for temp=12:0.1:30
%     moist=100;
%     [t,x]=ode45(@(t,x)Kn1(t,x,temp,moist),ts,x0,opt);%使用5级4阶龙格—库塔公式计算
%     tem=[tem;temp];
%     yy=[yy;x(end,7)];
% end
%     
% plot(moi,xx)
% figure(2);
% plot(tem,yy)