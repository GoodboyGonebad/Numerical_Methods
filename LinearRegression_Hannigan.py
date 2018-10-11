import numpy as np
import matplotlib.pyplot as plt

#PYU33C01 | Assignment 3 | Linear Regression | Luke Hannigan | 15318526

t = [5,15,25,35,45,55,65,75,85,95,105,115] # horizontal
d =  [32,17,21,7,8,6,5,3,4,1,5,1] # vertical
N = len(t)
log_t = np.log(t) # log t values explicitly rather than by plt.xscale -- must pass log t

# form of a, b worked out by hand with simulataneous Eqs 3.9, 3.10

a = (np.sum(log_t)*np.sum(np.multiply(d, log_t)) - np.sum(d)*np.sum(np.square(log_t))) / (np.sum(log_t)**2 - N*np.sum(np.square(log_t)))

b = (np.sum(d)*np.sum(log_t) - N*np.sum(np.multiply(d, log_t))) / (np.sum(log_t)**2 - N*np.sum(np.square(log_t)))

print '\na = ', a, '\nb = ', b

def fit(t): # linear fit function
	fit_list = []
	for i in np.arange(0, len(t)):
		f = a + b*t[i]
		fit_list.append(f)
		i += 1
	return fit_list

plt.figure(1)
plt.plot(t, d, '*r', label='Data Points')
plt.title('Decay against Time scaled linearly')
plt.xlabel('Time')
plt.ylabel('Decay')
plt.grid()
plt.legend(loc=0)

plt.figure(2)
plt.plot(log_t, d, '*r', label='Data Points')
#plt.xscale('log')
plt.title('Decay against log time')
plt.xlabel('Log Time')
plt.ylabel('Decay')
plt.xlim([0, 6.0])
plt.ylim([0, 35])
plt.grid()
plt.legend(loc=0)

plt.figure(3)
plt.plot(log_t, d, '*r', label='Data Points')
plt.plot(log_t, fit(log_t), '-b', label='Linear Regression')
plt.title('Decay against log time with linear regression fit\n of coefficients a = '+str(a)+', b = '+str(b))
plt.xlabel('Log Time')
plt.ylabel('Decay')
plt.xlim([0, 6.0])
plt.ylim([0, 35.0])
#plt.xscale('log') # fit loses linearity
plt.grid()
plt.legend(loc=0)

print '\nName: Luke Hannigan\nStudent ID: 15318526'

plt.show()
