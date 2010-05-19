w='word'
k=[0,1]
print 'k  ',k
t=(0,17)
print 't  ',t
print 'k^2  ',k*2
print 't^2  ',t*2
print 'w^2  ',w*2
print    #just an empty line for good measure
print w[2]
print t[1]

#t[1]=5
#w[2]=3 #does not support assigment=immutable

w='wo3d' # the crude way
print w[2]
w2=k  #w2 points to the object k, it is not a copy

del k[0]
print k,w2
k[0]=5
print k,w2
k=[20,21]
print k,w2
z=range(2,10)
print z
z=range(2,10,5)  #notice limited usefulness
print z
