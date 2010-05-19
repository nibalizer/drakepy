"""  week 2 : passing variables to functions """
from numpy import *

def test(y):
    for k in range(3):
        y=y+h
    return y    # note: we pass y back to the main program

h=2.
y=.5
print'i','\t','y','\t','h'
for i in range(3,6):
    y=test(y)
    print i,'\t',y,'\t',h


raw_input('waiting.... \n')

print '\t','k','\t','y'
for k in range(3,6):        # note k is used BOTH in test and in main prog.
    y=.5
    test(y)                 # y changes in test, but it is not changed in the main program
    print 'testing  ',k,'\t',y      # y does not change!
print"""---------------------------------------------------------"""

def test2():
    y=.5        # try commenting this out, y will then be a static variable and cannot be changed
    for k in range(4):
        y=y+h
    return y

r=1.
for i in range(3,6):
    y=5000000.                   
    test2()                         # of course does not matter what y is, not passed
    y=test2()
    print 'testing 2 ','\t', i,'\t',y,'\t',r
print"""---------------------------------------------------------"""

def test3(z):
    print 'testing 3, printing z ',z
    z[0]=17.
    z[1]=.0
    return

x=zeros((2),'f')                    # array with floating pts #=0.
x[1]=5.
test3(x)
print 'testing 3, but now x ',x     # note that x has changed!!!!
