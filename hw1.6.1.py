#Spencer Krum
#Computational Physics
#Drake Py

from pylab import *

#Problem 1.6

ion()
tstep = float(raw_input("Enter your time step(try 0.0001): "))
initial_pop = float(raw_input("Enter the initial population value(try 100): "))


t3 = arange(0.0, 5.01, tstep)
theory_n1 = arange(0.0, 5.01, tstep)
theory_n2 = arange(0.0, 5.01, tstep)
n1 = arange(0.0, 5.01, tstep)
n2 = arange(0.0, 5.01, tstep)
theory_n1[0] = initial_pop
n1[0] = initial_pop
tau1 = float(raw_input("Enter tau1(try 10): "))
tau2 = float(raw_input("Enter tau2(try 100): "))
theory_n2[0] = 100.0
n2[0] = 100.0
#tstep = t3[1] - t3[0]
for k in range(1, int(5/tstep)):
	theory_n1[k] = n1[0]*exp(1*t3[k]/tau1)
	n1[k] = n1[k-1] + 1*tstep*n1[k-1]/tau1
	n2[k] = n2[k-1] + 1*tstep*n2[k-1]/tau1 - 1*tstep*n2[k-1]*n2[k-1]/tau2
plot(t3, theory_n1, 'g+', t3, n1, 'r-', t3, n2, 'b+')
ylabel('Population N')
xlabel('time (arbitrary units)')
grid(True)
title('a=0.1, b=0: red=theory, green=Euler; a/b=10 blue=Euler ')
draw()
hold(False)
print("Numerical result agrees with analytic result for b=0")

raw_input("Enter return when finished")

