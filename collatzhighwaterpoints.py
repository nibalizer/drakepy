#Spencer Krum
#Collatz Conjecture
#9 June 2010


print "Collatz Conjecture."
print "Collatz conjecture is that any positive integer will become 1 after the following procedure is applied a sufficient number of times."
print "If the number is even, divide it by two. If the number is odd multiply by three and add one."

#the number 63728127 has length 948
def theNumber(prompt):
	while True:	
		number = raw_input(prompt)
		try:	
			number = abs(int(number))
			return number
		except ValueError:
			print "Please enter an integer"
def collatz(number_):
	length = -1
	number = number_
	while (number > 1):
		print "The number is %d" % number
		length += 1
		if (number % 2 == 0):
		#	print "The number is even, therefore divide by two"
			number = number/2
		else:
		#	print "The number is odd, therefore multiply by three and add one"
			number = (number*3)+1

	print "The number is %d, the number of steps was %d" % (number_,length)
	return length, number_
x = 1
start = theNumber("Please give a starting integer: ")
end = theNumber("Please give an ending integer: ")
for i in range(start + 1 ,end + 1):
	y, a = collatz(i)
	if x <= y:
		x = y
		z = a	
print "The number %d has length %d" % (z, x)
