#Spencer Krum
#Fibbonacci sequence in python
#6/8/10


from pylab import *
from matplotlib import *

print "Fibbonacci numbers"

fibba = lambda i: fibb.append(fibb[i] + fibb[i+1])
fibb = [1,1]
blank = [1,2]
i = 0 
while i < 100:
	fibba(i)
	i += 1
	blank.append(i+2)

ion()
plot(blank,fibb, 'g-')
ylabel('fibbonacci')
grid(True)
draw()
hold(True)
raw_input()



