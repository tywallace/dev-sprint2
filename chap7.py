# Enter your answrs for chapter 7 here
# Name: Tyler Wallace

import math
# Ex. 7.5
def estimate_pi():
	epsilon = 10**(-15)
	x = 0.0
	pi = 0.0
	while True:
		y = (math.factorial(4.0*x)*(1103.0+26390.0*x))/(math.factorial(x)**4.0*396.0**(4.0*x))
		if abs(y) < epsilon:
			break
		pi = pi + y
		x = x + 1
		print x
	return pi

a = (2*math.sqrt(2))/9801
iter_pi = 1 /( a * estimate_pi())
print iter_pi
print math.pi
# How many iterations does it take to converge? It takes 3 iterations to converge
