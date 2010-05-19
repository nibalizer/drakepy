# EB: plotting 

from pylab import *     # load graphing routines
from numpy import *
from scipy import *


ion()  # some magic needed here.....  Interactive mode ON
# go do show() at the end for very complex drawing...... control but at what price?

hold(True)  # True means you will overwriting graphs
plot([1,2,3,4], [1,4,9,16], 'ro')   # This means x and y,"stuff"
axis([0, 6, 0, 20])
#savefig('fig.png')                  # save a figure
title("red circles")
raw_input("Hit enter to continue: coming up: green +'s")

plot([1,2,3,4], [1,2,12,10], 'g--+')
title("green +'s")
raw_input("Hit enter to continue: next rescale")
axis([0, 6, 0, 20])
title("rescale")
raw_input("Change hold to false, change #'s and hit enter to continue")
#clf()                          #  clears a figure
hold(False)  # Now old data in the graph will be deleted

plot([1,2,3,4], [-15,4,9,16], 'b-o') # change # of x,y,"stuff"
axis([0, 6, -20, 20])
title('last graph')
raw_input('Now we are going to open a new window and close the old')
figure(2)
close(1)                    # closes a figure window
raw_input('Now only the new window open')
close(2)
hold(True)
ioff()      # Interactive mode OFF, if you plot 10^17 points, it will take to long
plot([1,2,3,4], [1,4,9,16], 'ro') #This means x and y,"stuff"
axis([0, 6, 0, 20])
title("A new graph")
ion()       # the alternative to this is: use of show() 
draw()
# notice that this is nasty: to shut down you need to kill it
raw_input("See how nasty?")  # we will never get here
# HOWEVER: there still will be something hanging in the air!

# Animation
clf()
import time
tstart = time.time()                # for profiling, how many frames per sec
x = arange(0, 2*pi, 0.01)           # x-array
line, = plot(x, sin(x),'rx:')
for i in range(1,20):
    print i
    line.set_ydata(sin(x+i/10.))    # update the data, notice floating point 10.0
    draw()                          # redraw the canvas
print 'Frames per Second: ' , 20/(time.time()-tstart)
raw_input('Hit enter to plot a nice graph, w/ labels')

clf()                               # just plotting and solving ODE's
z = arange(0.0, 5.2, 0.2)
plot(z, z, 'r--', z, z**2, 'bs', z, z**3, 'g^')  # red dashes, blue squares and green triangles
ylabel('velocity [km/s]')
xlabel('time [s]')
grid(True)
title('A random plot to show that it can be done')
raw_input("Done plotting a nice graph, w/ labels.    On to ODE's")
hold(False)                         # Do NOT overwrite graphs
                                    # Note that "holds" remains if you rerun the program....

# integration of a 1st order ODE
# dx/dt=g*x     x[t=0] = 17.
# dx=g*x *dt     math: the way, only a physicist loves it
# we want to find out what happens in 2.5 sec. and we know it is sec, because t is in sec

dt=float(raw_input("Enter time step [0.1] -->  "))  # enter a floating point number
n=int(2.5/dt)+1      # turn 2.5/dt into an integer so we know how many steps to take to get to 2.5 sec
print n
g=-2.
t=zeros(10000,'d')   # One way to generate zero's.  'd' means a float, it is superfluous
x=.0*arange(10000)   # another way to generate zero's.  
x[0]=17.
print "time   x(t)     true value"
for i in range(n):
    t[i+1]=t[i]+dt
    x[i+1]=x[i]+g*x[i]*dt

print t[i],"\t",x[i],"\t", x[0]*exp(g*t[i])

w=x[0]*exp(g*t)     # the correct solution.... OK, so we know how to integrate
t=t[:n]             # slicing of arrays  WHY?
x=x[:n]             # so that we do not have trailing zeros... 
w=w[:n]             # yes, w is an array as well: t is one --> hence w as well

plot(t,x,'g--', t, w,'r--')
title("green = Euler integration and red = true solution")
