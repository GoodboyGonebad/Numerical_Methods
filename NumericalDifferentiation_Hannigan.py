# code for PY3C01-numerical methods
# differentiation, September 2014

# aim:
# numerical differentiation using Python
# backward, forward, central method
# computation of relative errors

import numpy as np
import matplotlib.pyplot as plt
np.seterr(divide='ignore', invalid='ignore') #to ignore runtime issue as approach divide by zero

def function(x):
    """ define function to be differentiated"""
    f=np.cos(x)
    return f

def analytic(x):
    """analytic derivative"""
    f= -1*np.sin(x)
    return f

def analytic_2(x):
	f = -1*np.cos(x)
	return f
    
def forward(x,h):
    f = (function(x+h)-function(x))/h
    return f

def backward(x,h):
    f = (function(x)-function(x-h))/h
    return f

def central(x,h):	
    f = (function(x+h)-function(x-h))/(2*h)
    return f

def central_2(x,h):
	f = (central(x+h,h) - central(x-h,h))/(2*h)
	return f

def central_alt(x,h):
	f = ((function(x+h)-function(x))-(function(x)-function(x-h)))/(h**2)
	return f

x = np.arange(0, 8*np.pi, 0.01)
h_val = 0.1*np.pi

#Geometric progression beginning on (np.pi) / 10; python epsilon ~ 10^-52 >> length = 52
#don't need to use this >> just zoom in on graph until change in error levels off approx value
r = 0.1
length = 40
h_range = [h_val * r ** (n - 1) for n in range(1, length + 1)]


plt.figure(1)
plt.xlabel('x')
plt.ylabel(r'$f(x)$')
plt.title(r'Plot of $f(x) = \cos{(x)}$')
plt.plot(x,function(x))


plt.figure(2)
plt.xlabel('x')
plt.ylabel(r'$f^{\prime}(x)$')
plt.title(r'Analytical result for the first derivative $f^{\prime}(x)$ of $\cos{(x)}$')
plt.plot(x,analytic(x))

plt.figure(3)
plt.xlabel('x')
plt.ylabel(r'$f^{\prime \prime}(x)$')
plt.title(r'Analytical result for the second derivative $f^{\prime \prime}(x)$ of $\cos{(x)}$')
plt.plot(x,analytic_2(x))



print "central second derivative:", central_2(1,h_val), "\n", "analytic second derivative: ", analytic_2(1), "Optimized central second derivative: ", central_alt(1, h_val)

x = np.arange(0, h_val, 0.01)

fig = plt.figure(5)
plt.xlabel(r'step size $h$')
plt.ylabel(r'$f^{\prime \prime}(x)$')
plt.title('Comparison of two expressions for the central difference method \n applied to the second derivative of $\cos{(x)}$ at $x=1$')
plt.plot((0, h_val), (analytic_2(1), analytic_2(1)), 'k-', label='Analytic')
plt.plot(x,central_2(1,x),label='Central Diff')
plt.plot(x, central_alt(1,x), label='Optimized Central Diff')
ax = fig.gca()
#ax.set_xticks(np.arange(0, h_val, 0.01))
#ax.set_yticks(np.arange(-0.88, -0.80, 0.01))
plt.ylim(-0.4, -0.7)
plt.xlim(0, h_val)
plt.grid()
plt.legend(loc=0)


#relative error
def error_forward(y):
    f= abs((forward(1,y)-analytic(1))/analytic(1))
    return f
    
def error_backward(y):
    f= abs((backward(1,y)-analytic(1))/analytic(1))
    return f

def error_central(y):
    f= abs((central(1,y)-analytic(1))/analytic(1))
    return f

# rel error on seond deriv
def error_central_2(y):
	f = abs((central_2(1,y)-analytic_2(1))/analytic_2(1))
	return f

def error_central_alt(y):
	f = abs((central_alt(1,y)-analytic_2(1))/analytic_2(1))
	return

def error_central_22(y):
	f = abs((central_2(y,0.001)-analytic_2(y))/analytic_2(y))
	return f


x = np.arange(0, 0.1*np.pi, 0.01)
#x = np.arange(0, 8*np.pi, 0.01)


#most accurate method converges on the origin fastest (h --> 0 && error --> 0)

plt.figure(6)
plt.xlabel('step size h')
plt.ylabel('relative error')
plt.title('central difference method converges fastest')
plt.loglog(x,error_forward(x),label='forward')
plt.loglog(x,error_backward(x),label='backward')
plt.loglog(x,error_central(x),label='central')
plt.legend(loc=4)

"""
#this isn't working
plt.figure(7) #linearly scaled
plt.xlabel(r'step size $h$')
plt.ylabel('relative error')
plt.title('Relative error on $f^{\prime \prime}(x)$ of $\cos{(x)}$ by \n central difference method against step size $h$')
plt.plot(x, error_central_2(x),label='Central diff')
plt.plot(x, error_central_alt(x), label='Optimized central diff')
plt.legend(loc=4)
"""

plt.figure(8) #log scaled
plt.xlabel(r'step size $h$')
plt.ylabel('relative error')
plt.title('Log-log plot of Relative error on $f^{\prime \prime}(x)$ of $\cos{(x)}$ by \n central difference method against step size $h$ ')
plt.loglog(x, error_central_2(x),label='Central diff')
plt.legend(loc=4)

m = np.arange(0, 8*np.pi, 0.01)

fig = plt.figure(9)
plt.xlabel('x')
plt.ylabel('Relative Error')
plt.title('Relative error on $f^{\prime \prime}(x)$ of $\cos{(x)}$ with  $h=0.001$ \n and $x$ varying over four cycles')
#plt.ylim(-0.5, 0.5)
ax = fig.gca()
ax.set_xticks(np.arange(0, 8*np.pi, 2))
#ax.set_yticks(np.arange(-0.88, -0.80, 0.01))
plt.grid()
plt.plot(m, error_central_22(m), '-k')
#plt.plot(m, analytic_2(m), '-b')

plt.figure(10)
plt.xlabel('x')
plt.ylabel(r'$f^{\prime \prime}(x)$')
plt.title('Plot of analytical and numerical second derivative of $\cos{(x)}$')
plt.plot(m, analytic_2(m), label='Analytic')
plt.plot(m, central_2(m,0.1), label='Numerical')
plt.plot((0, 30), (0, 0), 'k-')
plt.legend(loc=0)


print('Name: Luke Hannigan\nStudent ID: 15318526')

plt.show()
