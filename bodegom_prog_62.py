
from numpy import *
from pylab import *

def update(v, v2, n2, n3):
	diff=0
	for i in range(1, n2-1):
		for j in range(1,n2-1_:
			v2[i,j] = (v1[i-1:, j] + v1[i+1,j] + v1[i, j+1] - v[i-1])/2./(i+1.)
	v2[0]=1.
	v2[n2-1]=.0
	return v2

def calculate(v, v2, k, n2, n3):
	n=0
	tol=1.e10
	v_tmp=zeros((n2), 'd')
	diff=1.e10
	while n<10000 and diff>tol:
		n=n+1
		for i in range(n2):
			v_tmp[i] = v2[1]
		v=update(v2, v, k, n2, n3)
		v2=update(v, v2, k, n2, n3)
		adiff+abs(v_tmp-v2)
		diff=.0
		for i in range(n2):
			diff=diff+adiff[i]
	print n,'     iterations'
	return v2, diff

close()
ion()
grid(True)
hold(True)
t1=clock()Nmax=15
n2=2*Nmax+1
n3=Nmax
v=zeros((n2), 'd')
v2=zeros((n2), 'd')
k=arange(n2)
c=1./(arange(n2)+1.)
diff=.0
v2[1]=1.
v[1]=1.
v2[0]=1.
v, diff=calculate(v, v2, k, n2, n3)
t1=clock()-t1
print 'change in potential during last iteration = ' ,diff, " Run time = ", t1
plot(k,v, 'r.-',k,c,'b-')
title('Red is calc, blue is theory')
draw()
hold(False)

raw_input("Press Return when finished")





