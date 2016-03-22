# -*- coding:utf-8 -*-
# Author: Jason Ye
# Time:	2016/03/22

def extendedEucliean(a, b):
	"""
	Inputs:
	Two number a and b
	Ouputs:
	gcd: Greatest common divisor of a and b
	s, t: s and t are integers that satifies gcd(a,b) = s*a+t*b
	"""
	# Initialization
	r1, r2 = a,b
	s1, s2 = 1,0
	t1, t2 = 0,1

	# Iteration
	while(r2 > 0):
		q = r1 / r2
		r = r1 - q * r2
		r1, r2 = r2, r

		s = s1 - q * s2
		s1, s2 = s2, s

		t = t1 - q * t2
		t1, t2 = t2, t
	gcd, s, t = r1, s1, t1
	return [gcd, s, t]

def main():
	print extendedEucliean(36,10)

if __name__ == "__main__":
	main()