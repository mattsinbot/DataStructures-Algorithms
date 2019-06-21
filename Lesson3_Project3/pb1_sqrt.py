tol = 0.0001
def diff_fx(a):
	return 2*a
	
def fx(a):
	return a**2 - 9.06

"""
prev = 3
for _ in range(5):
	next = prev - fx(prev)/diff_fx(prev)
	prev = next
	print(prev, prev**2)
"""

def find_sqrt(x, n):
	if abs(x**2 - n) < tol:
		return x
	x = x - fx(x)/diff_fx(x)
	return find_sqrt(x, n)
	
sqrt_val = find_sqrt(3, 9.06)
print(sqrt_val)

"""
Comment: the time complexity of Newto's method is
O(log n) where n is the precision of tolerance.
"""
