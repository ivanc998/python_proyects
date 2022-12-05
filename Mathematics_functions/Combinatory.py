import numpy as np


def mC1(m):
	if not((type(m) is int)):
		raise TypeError('m must be an integers')
	else:
		return [list(row) for row in np.identity(m, dtype = int)]

# Return a list of lists where each one of these represents a way to choose n elements of m.
# Each list has 0 or 1. 0 presents the element was not be choosen and 1 that it was. 
# Raise a TypeError if the m or n not satisfy the conditions of mCn
def combinatory_mn(m,n):
	
	if not((type(m) is int) and (type(n) is int)):
		raise TypeError('m and n must be both integers')
	elif m < 0:
		raise TypeError('It was expected m as natural number')
	elif n > m:
		combinations = []
	elif m == n:
		combinations = [[1]*m]

	else:
		if n == 1:
			combinations = mC1(m)
		elif n == 0:
			combinations = [[0]*m]
		else:
			combinations = []
			if n > 1:
				for k in range(1, m - n + 2):
					recursive_comb = combinatory_mn(m-k, n-1)
					aux_comb = [mC1(k)[-1] + x for x in recursive_comb]
					combinations += aux_comb

	return combinations
