#Spencer Krum
#Collatz Conjecture pickle renderer w/ pylab

from pylab import *
from matplotlib import *

import pickle

filename = raw_input("Please give the path to the pickled array of high water marks: ")
length_low = raw_input("Please give the lower bound of the range that was tested: ")
length_high = raw_input("Please give the upper bound of the range that was tested: ")
name = raw_input("Please give the name of the file you would like to save the resulting graph in: ")

start = int(length_low)
end = int(length_high)

picklefile = open(filename, 'r')
highwater = pickle.load(picklefile)



blank = []
i = start
while i < end:
	blank.append(i)
 	i += 1

ion()
plot(blank,highwater, 'o')
ylabel('Number of steps to one')
xlabel('Initial number')
grid(True)
draw()
hold(False)
savefig(name)
raw_input("Press return to quit")
