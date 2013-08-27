'''
hw2_2.py
This Python program uses Newton's Method to 
solve an equation of a wire that is catenary. 

Author: Dongpu Jin
Date: 10/9/2011
'''

import sys
import math

# Function used to calculate the height above ground
def f(x):
	return -32.85 + 62.85 * math.cosh(x/62.85)

# Derivative of f(x)
def df(x):
	return math.sinh(x/62.85)
	
# Start of the Newton's Method
p0 = 120 # starting point is 120 
N = 100 # maximum number of iteration is 30
TOL = 0.01 # tolerance is 10^-2 m = 1 cm

for i in range(0, N): 
	print "Iteration: %d"%(i + 1)
	p = p0 - f(p0)/df(p0)	# compute pi
	if abs(p - p0) < TOL:  
		print "At position %f, cable touches ground."%p
		sys.exit(0) # Stop
	p0 = p	# update p0

print "Method failed after %d iterations" %N
sys.exit(1)	# Stop
