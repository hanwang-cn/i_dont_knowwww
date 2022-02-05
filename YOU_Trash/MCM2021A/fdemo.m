format long
clear all
clc
tspan = [0  3  5  7 9 11];
k0=[6.01052805059212,0.637257106217679,0.386753194557416,0.148155999371010,0.638275190614080,0.678579622038740,3.92079108397120,164.581314753576,2.36997005000220,6.17927897218426,0.169497154789499,0.270227698053044,0.234923245679915,3.16001303269799,720.015962558812,0.000809102055052524,0.000212405268073187,0.000137680418547612,1.24278858354482e-06,0.0434799075347541,0.000127739008672689,0.927773510097340,0,0,0,0,0];
x0 = [9.8734/24.6835;7.0886/24.6835;6.9620/24.6835;5.4430/24.6835;3.5443/24.6835;8.6076/24.6835;100/100];
lb = [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1 -1 -1 -1 -1 -1]; 
ub = [Inf Inf Inf Inf Inf Inf Inf Inf Inf Inf Inf Inf Inf Inf Inf Inf Inf Inf Inf Inf Inf 10 1 1 1 1 1 1];

data=...
    [
3       24.6835/24.6835  11.3924/24.6835  7.9747/24.6835   4.5570/24.6835   1.8987/24.6835  9.8734/24.6835  (100-8.5496)/100   
5       24.4304/24.6835  9.2405/24.6835   8.6076/24.6835   2.5316/24.6835   0.2532/24.6835  15.1899/24.6835 (100-13.6641)/100  
7       6.2025/24.6835   19.1139/24.6835  10.3797/24.6835  2.2785/24.6835   0.2532/24.6835  15.1899/24.6835 (100-16.2595)/100  
9       0.5063/24.6835   20.3797/24.6835  13.9241/24.6835  3.0380/24.6835   0.1266/24.6835  13.4177/24.6835 (100-18.6260)/100  
11      0.3797/24.6835   20.1266/24.6835  14.8101/24.6835  3.1646/24.6835   0.1266/24.6835  12.7848/24.6835 (100-19.2366)/100  
];
yexp = data(:,2:end);
options = optimoptions('lsqnonlin','Display','iter');
[k,resnorm,residual,exitflag,output,lambda,jacobian] = ...
lsqnonlin(@ObjFunc,k0,lb,ub,options,tspan,x0,yexp);       
ci = nlparci(k,residual,jacobian);

fprintf('  The sum of the squares is: %.9e\n\n',resnorm)

function f = ObjFunc(k,tspan,x0,yexp)           % 目标函数
[t Xsim] = ode45(@KineticsEqs,tspan,x0,[],k);
Xsim1=Xsim(:,1);
Xsim2=Xsim(:,2);
Xsim3=Xsim(:,3);
Xsim4=Xsim(:,4);
Xsim5=Xsim(:,5);
Xsim6=Xsim(:,6);
Xsim7=Xsim(:,7);
ysim(:,1) = Xsim1(2:end);
ysim(:,2) = Xsim2(2:end);
ysim(:,3)=Xsim3(2:end);
ysim(:,4)=Xsim4(2:end);
ysim(:,5)=Xsim5(2:end);
ysim(:,6)=Xsim6(2:end);
ysim(:,7)=Xsim7(2:end);
size(ysim(:,1));
size(ysim(:,2));
size(yexp(:,1));
size(yexp(:,2));
f = [(ysim(:,1)-yexp(:,1)) (ysim(:,2)-yexp(:,2)) (ysim(:,3)-yexp(:,3)) (ysim(:,4)-yexp(:,4)) (ysim(:,5)-yexp(:,5)) (ysim(:,6)-yexp(:,6)) (ysim(:,7)-yexp(:,7))];
end
function dx = KineticsEqs(t,x,k)              % ODE模型方程
dx=[x(1)*log(k(22)*x(7)/(x(1)+k(1)*x(2)+k(2)*x(3)+k(3)*x(4)+k(4)*x(5)+k(5)*x(6)))
    x(2)*log(k(22)*x(7)/((1/k(1))*x(1)+x(2)+k(6)*x(3)+k(7)*x(4)+k(8)*x(5)+k(9)*x(6)))
    x(3)*log(k(22)*x(7)/((1/k(2))*x(1)+(1/k(6))*x(2)+x(3)+k(10)*x(4)+k(11)*x(5)+k(12)*x(6)))
    x(4)*log(k(22)*x(7)/((1/k(3))*x(1)+(1/k(7))*x(2)+(1/k(10))*x(3)+x(4)+k(13)*x(5)+k(14)*x(6)))
    x(5)*log(k(22)*x(7)/((1/k(4))*x(1)+(1/k(8))*x(2)+(1/k(11))*x(3)+(1/k(13))*x(4)+x(5)+k(15)*x(6)))
    x(6)*log(k(22)*x(7)/((1/k(5))*x(1)+(1/k(9))*x(2)+(1/k(12))*x(3)+(1/k(14))*x(4)+(1/k(15))*x(5)+x(6)))
    -k(16)*x(1)*x(7)-k(17)*x(2)*x(7)-k(18)*x(3)*x(7)-k(19)*x(4)*x(7)-k(20)*x(5)*x(7)-k(21)*x(6)*x(7)
    ];    
end