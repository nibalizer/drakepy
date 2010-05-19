"""  week 3 - EB   
this program displays the 2-dimensional phase diagrams for the driven and undriven pendulum"""

from pylab import *
from numpy import *

##driving force strength:  g   ------ damping :q
##initial angle , angular velocity: xint,vint  

def accel(iGo,x,v,t,w,g,q):
    if iGo==1: return -x            #simplified pendulum
    if iGo==2: return -sin(x)       #regular pendulum
    if iGo==3: return -x**9
    if iGo==4: return -sin(x)-v/q
    if iGo==5: return -sin(x)-v/q +g*cos(w*t)
    return 

def RK4(iGo,x,v,tstep,xnew,vnew,t,w,g,q):   
    xk1=tstep*v
    vk1=tstep*accel(iGo,x,v,t,w,g,q)
    xk2=tstep*(v+vk1/2.)
    vk2=tstep*accel(iGo,x+xk1/2.,v+vk1/2.,t+tstep/2.,w,g,q)
    xk3=tstep*(v+vk2/2)
    vk3=tstep*accel(iGo,x+xk2/2.,v+vk2/2.,t+tstep/2.,w,g,q)
    xk4=tstep*(v+vk3)
    vk4=tstep*accel(iGo,x+xk3,v+vk3,t+tstep,w,g,q)
    vnew=v+(vk1+2.*vk2+2.*vk3+vk4)/6.
    xnew=x+(xk1+2.*xk2+2.*xk3+xk4)/6.
    return xnew,vnew

ion()
grid(True)
hold(True)
print'1=simple pendulum, 2=real pendulum, 3= strange osc., 4=damped, 5=damped&driven, <0=stop'
iGo=1
xmin,xmax=-pi,pi
ymin,ymax=-pi,pi
pi_2=2.*pi
v_plot=zeros((100000))
x_plot=zeros((100000))
x_redu=zeros((100000))
t_plot=zeros((100000))
xpoin=zeros((100000))
vpoin=zeros((100000))
raw_input(' fix your screen and hit enter; 1st example is simple pendulum ')

while iGo>0:
    close(1)
    g=0.            #driving force strength
    q=0.            #damping 
    w=1.            #driving frequency  #w=0.66666666
    xint=.0         #starting x
    rot=0           #rotations
    rot_force=0     #how many time the driving force has gone thru its cycle
    vint=float(raw_input(' v_initial: .5,1.,1.999,2.,20    --> '))
    if iGo>=4: q=float(raw_input(' damping  : .5,1.,1.999,2.,20    --> '))
    if iGo>=5: w=float(raw_input(' driving freq. :                 --> '))
    if iGo>=5: g=float(raw_input(' driving force strength:         --> '))
    x,v=xint,vint
    t=0.
    eps=1.0e-6      #change to e-10.... tolerance
    tstep=0.04
    xnew,vnew=0.,0.
    xnh,vnh=0.,0.
    xn,vn=.0,.0
    pi_w=pi_2/w
    figure(figsize=(14,10))
    v_plot[0]=vint
    x_plot[0]=xint
    i=0
    kdec=0

    while i<100000:
        xnew,vnew=RK4(iGo,x,v,tstep,xnew,vnew,t,w,g,q)   
        tshalf=tstep/2.                
        xnh,vnh=RK4(iGo,x,v,tshalf,xnh,vnh,t,w,g,q)   
        xn,vn=RK4(iGo,xnh,vnh,tshalf,xn,vn,t+tshalf,w,g,q)
        d1=abs(xn-xnew)
        d2=abs(vn-vnew)
        delta=max(d1,d2)
        if delta<eps or iGo==3:
            x=xn
            v=vn
            t=t+tstep
            if abs(x)>pi:
                rot=rot+int(abs(x)/x)
                x=x-pi_2*abs(x)/x
            x_plot[i]=x+rot*pi_2
            x_redu[i]=x
            v_plot[i]=v
            if t>pi_w:
                t=t-pi_w
                xpoin[rot_force]=x-t/tshalf*(xn-xnh)
                vpoin[rot_force]=v-t/tshalf*(vn-vnh)
                rot_force=rot_force+1
                #print '%3d \t %9.5e \t %9.5e \t %9.5e \t %8.5e' % (rot_force,t,t-t/tshalf*(xn-xnh),xpoin[rot_force-1],vpoin[rot_force-1])
            t_plot[i]=t+rot_force*pi_2/w
            i=i+1
            if iGo!=3: tstep=tstep*.95*(eps/delta)**.25
        else:
           tstep=tstep*.95*(eps/delta)**.2
           kdec=kdec+1
        if rot_force>500: break
    subplot(221)
    plot(t_plot[:i]/pi_2,x_plot[:i],'c-')
    title('x vs time  ')

    subplot(222)
    plot(x_plot[:i],v_plot[:i],'b-')
    title('v vs x')

    subplot(223)
    plot(x_redu[:i],v_plot[:i],'m.:')
    title('v vs reduced x ')

    subplot(224)
    plot(xpoin[:rot_force],vpoin[:rot_force],'r.')
    axis([-3.2, 3.2, -10, 10.])
    words='Poincare plot q='+str(q)+' w= '+str(w)+' g= '+str(g)
    title(words)
    
    print i,kdec,rot_force,'Enter condition: 1, 2, 3, 4 or 5 -->',
    iGo=int(raw_input())
close()
