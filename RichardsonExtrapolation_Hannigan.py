import numpy as np
import matplotlib.pyplot as plt

#PYU33C01 | Assignment 2 | Richardson Extrapolation | Luke Hannigan | 15318526

#Given function
def f(x):
	return x*np.exp(x)

#Analytical result
def f2(x):
	return (2 + x)*np.exp(x)

#Second derivative by central diff w/ sub cancellation
def central(x,h):
	return ((f(x+h)-f(x))-(f(x)-f(x-h)))/(h**2)

L = 4 # max D order of extrapolation -- going any high than 6 causes "overflow in long_scalars"
h_0 = 4*(10**-1) # initial step size
f_list = []
x = np.arange(0, 2, 0.05)

#Second derivative in range [0,2] by CD
for i in x:
	g = central(i,h_0)
	f_list.append(g)

#Plot of second derivative in range [0,2] by CD
fig=plt.figure(1)
plt.plot(x, f_list, label='Central Difference Method')
plt.title('$f^{\prime \prime}(x)$ for $f(x)=x \exp{x}$ against $x$ by central difference method')
plt.xlabel(r'$x$')
plt.ylabel(r'$f^{\prime \prime}(x)$')
plt.legend(loc=0)
plt.grid()

D_list = []
h_list = []
flag = True #control on printing in D(x,h) function

#Richard's extrapolation
def D(x,h):
	for i in np.arange(0, L):
		
		D_i = ((2**(2**i))*central(x,h) - central(x, 2*h)) / (2**(2**i) - 1)
	
		D_list.append(D_i)
		h_list.append(h)	
	
		h /= 2
		i += 1

	if flag:
		print '\nRichard says, " second derivative of f(x=' + str(x) + ') with initial step size h =',h_0,' is ',D_list[-1], '"\nThe expected answer is ',f2(x)

		print 'The relative error is ', 100*abs( (D_list[-1]-f2(x)) / f2(x) ), '%'

D(2,h_0)
flag = False

err_list = []
D_list = [] # reintialize !!!
h_list = []

def error_D(m,h): # relative error
	D(m,h)
	for i in range(0, L):
		err = abs( (D_list[i]-f2(m)) / f2(m) )
		err_list.append(err)
		
		i += 1
	return err_list

error_D(2,h_0)

w = 10**-10

fig = plt.figure(2)
plt.plot(h_list, err_list, '--r', label='Relative error')
plt.title('Plot of relative error on second derivative by Richardson Extrapolation\nup to $i=$'+str(L)+' against step size with initial $h_{0}=$' + str(h_0))
plt.xlabel(r'step size $h$')
plt.ylabel(r'Relative Error')
ax = fig.gca()
ax.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.legend(loc=0)
plt.grid()

Di_list = []
hi_list = []
h_0 = 0.1

print '\nName: Luke Hannigan\nStudent ID: 15318526'

plt.show()
