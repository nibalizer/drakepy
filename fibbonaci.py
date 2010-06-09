#Spencer Krum
#Fibbonacci sequence in python
#6/8/10

print "Fibbonacci numbers"
number = raw_input("How many fibbonacci numbers would you like?")
numbers = int(number)
fibb = [1,1]
for i in range(numbers):
	fibb.append(fibb[i] + fibb[i+1])
print fibb
