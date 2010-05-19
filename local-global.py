#local variables vs globals
#locals 1st

def f(x):
    print 'f(x) ',x
    x=2
    print x

x=50
f(x)
f(x)

def g():
    global y
    y=y**2
    print 'g() ',y

y=5
g()
g()
print y

def z(x):
    return x**2

x=17
y=z(x)
print y

q=lambda x: x**3
print q(5)


