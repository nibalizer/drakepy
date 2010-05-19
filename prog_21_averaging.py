"""  week 2 - - averaging"""

from pylab import*
from numpy import *

def ave(x):
    sum_x=0.                    # sum of all the x values
    sum_x2=0.                   # sum of x^2
    n=len(x)                    # total number of points
    for i in range(n):
        sum_x=sum_x+x[i]
        sum_x2=sum_x2+x[i]**2
    var=sqrt(sum_x2/(n-1))      # sample variance
    x_ave=sum_x/n
    return x_ave,var            # NOTE: 2 variables returned

#n1=10000                       #set number of points
n1=float(raw_input("Enter number of points to average -->  "))
x=zeros(n1,'d')                 # 'd' makes this double precision (i=integer)
x1=zeros(n1,'d')
z=arange(n1)
print x
print x1
print z

for i in range(len(x)):
    x[i]=rand()                 # NOTE random number uniformly distributed in the range [0,1.)
    x1[i]=randn()               # Returns zero-mean, unit-variance Gaussian random numbers
##help(randn)                     # if you want to make sure what this does
##help(rand)
##a=randn(n1)                     # shortcut to an array of length n1 uniformly distributed [0.,1)
##b=rand(n1)                      # shortcut to an array of length n1 "Gaussianly" distributed 
##print a,'\n\n',b,'\n\n'

if n1<=25:
    print x
    print x1

x_ave,var=ave(x)
sd1=sqrt(var)
error1=x_ave-0.5
x_ave=round(x_ave,4)
error1=round(error1,4)
sd1=round(sd1,4)
print '\n Uniform distribution ave=',x_ave,'  error=',error1,'  SD= ',sd1,'\n'
x_ave,var=ave(x1)
sd2=sqrt(var)
x_ave=round(x_ave,4)
sd2=round(sd2,4)
print '\n  Normal distribution ave= ',x_ave,' error= ',x_ave,' SD=',sd2,

ion()
hold(True)                      # so that we can add plots together
plot(z,x,'b-s')                  # source data

title('blue is unifrom dist., red is Gaussian, number of data pts: '+str(n1))
plot(z,x1,'r-s')


