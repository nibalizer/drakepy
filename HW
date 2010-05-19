#Example HW#1 
print("Example for HW#1, ")
print("   ")
from pylab import *

ion()

#Problem 1.4
#
clf()
ion()
tstep = 0.2
t3 = arange(0.0, 10.01, tstep)
theory_n1 = arange(0.0, 10.01, tstep)
theory_n2 = arange(0.0, 10.01, tstep)
n1 = arange(0.0, 10.01, tstep)
n2 = arange(0.0, 10.01, tstep)
theory_n1[0] =8.0
n1[0] = 8.0
tau1 = 1.0
tau2 = 4.0
theory_n2[0] =4.0
n2[0] = 4.0
k=1
tstep = t3[1] - t3[0]
while k <= 10/tstep:
    theory_n1[k] = n1[0]*exp(-1*t3[k]/tau1)
    theory_n2[k] = (n2[0]*exp(-1*t3[k]/tau2))+(n1[0]/(1-tau1/tau2))*(exp(-1*t3[k]/tau2)-exp(-1*t3[k]/tau1))
    n1[k] = n1[k-1]-1*tstep*n1[k-1]/tau1    
    n2[k] = n2[k-1]+1*tstep*n1[k-1]/tau1-1*tstep*n2[k-1]/tau2
    k=k+1
plot(t3, theory_n1, 'r',t3, theory_n2, 'b', t3, n1, 'r+', t3, n2, 'b+')
ylabel('Number of nuclei (arbitary units)')
xlabel('time (arbitary units)')
grid(True)
title('N vs Time, red = N1 theory/Euler; blue = N2 theory/Euler ;tau1/tau2=0.25')
draw()
hold(False)  #Do NOT overwrite graphs
raw_input("Enter return see effect of different tau ratio ")
tau1=4.0
tau2=2.0
k=1
tstep = t3[1] - t3[0]
while k <= 10/tstep:
    theory_n1[k] = n1[0]*exp(-1*t3[k]/tau1)
    theory_n2[k] = (n2[0]*exp(-1*t3[k]/tau2))+(n1[0]/(1-tau1/tau2))*(exp(-1*t3[k]/tau2)-exp(-1*t3[k]/tau1))
    n1[k] = n1[k-1]-1*tstep*n1[k-1]/tau1    
    n2[k] = n2[k-1]+1*tstep*n1[k-1]/tau1-1*tstep*n2[k-1]/tau2
    k=k+1
plot(t3, theory_n1, 'r',t3, theory_n2, 'b', t3, n1, 'r+', t3, n2, 'b+')
ylabel('Number of nuclei (arbitary units)')
xlabel('time (arbitary units)')
grid(True)
title('N vs Time, red = N1 theory/Euler; blue = N2 theory/Euler ;tau1/tau2=2.0')
draw()
raw_input("Enter return to proceed to problem 1.6 ")
#
#Problem 1.6
#
clf()
ion()
tstep = 0.0001
t3 = arange(0.0, 5.01, tstep)
theory_n1 = arange(0.0, 5.01, tstep)
theory_n2 = arange(0.0, 5.01, tstep)
n1 = arange(0.0, 5.01, tstep)
n2 = arange(0.0, 5.01, tstep)
theory_n1[0] = 100.
n1[0] = 100.0                              #starting population = 1000
tau1 = 10.
tau2 = 100.
theory_n2[0] =100.0
n2[0] = 100.0
k=1
tstep = t3[1] - t3[0]
while k <= 5/tstep:
    theory_n1[k] = n1[0]*exp(1*t3[k]/tau1)
    n1[k] = n1[k-1]+1*tstep*n1[k-1]/tau1    
    n2[k] = n2[k-1]+1*tstep*n2[k-1]/tau1-1*tstep*n2[k-1]*n2[k-1]/tau2
    k=k+1
plot(t3, theory_n1,'g+',  t3, n1, 'r-', t3, n2, 'b+')
ylabel('Population N')
xlabel('time (arbitary units)')
grid(True)
title('a=0.1, b=0: red=theory, green=Euler; a/b=10  blue=Euler ')
draw()
hold(False)  #Do NOT overwrite graphs
print("Numerical result agrees with analytic result for b=0")

raw_input("Enter return when finished ")

