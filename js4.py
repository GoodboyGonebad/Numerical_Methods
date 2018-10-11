import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
import timeit

#PYU33C01 | Assignment 4 | Numerical Integration | Luke Hannigan | 15318526

N = np.array([4, 8, 16, 32, 64, 128, 256, 512, 1024])
a = 0.0
b = np.pi

f = lambda x: np.sin(x) # given function
ex = 2.0 # exact analytical result
flag = True # control on euler-maclaurin correction (true=on;false=off)

def I(func, N): # trapezoid rule
	int_list = []
	for j in range(0, len(N)):
		h = (b-a)/N[j]
		Int = 0
		if not flag: # no E-M correction
			for i in range(0, N[j]+1):
				strip = (0.5*h)*(func(i*h) + func((i+1)*h))
				Int += strip
			int_list.append(Int)
		return (int_list)

		if flag:
			for i in range(0, N[j]+1): # E-M corrected
				strip = (0.5*h)*(func(i*h) + func((i+1)*h)) + ((h**2)/12)*(derivative(func,a,dx=1e-6) - derivative(func,b,dx=1e-6)) - ((h**4)/720)*(derivative(func,a,dx=1e-6,order=3) - derivative(func,b,dx=1e-6,order=3))
				Int += strip
			int_list.append(Int)
		return (int_list)		

def err_I(func, N): # relative error
	err_list = []
	for i in range(0, len(N)): ### ERROR: list index out of range ??
		err = abs( (I(func,N)[i]-ex) / ex )
		err_list.append(err)
	return err_list

print('For\nN = ',N,'\nrelative error is\n',err_I(f,N))

plt.figure(1)
plt.loglog(N, err_I(f,N), '--r')
if not flag:
	plt.title('Variation in relative error against $N$\nfor the trapezoid Rule')
if flag:
	plt.title('Variation in relative error against $N$\nfor the trapezoid Rule with correction terms')
plt.xlabel('N')
plt.ylabel('Relative Error')
plt.grid()
#plt.legend(loc=0)

plt.show()
