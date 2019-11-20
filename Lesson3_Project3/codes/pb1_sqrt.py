tol = 0.0001
def diff_fx(a):
	return 2*a
	
def fx(a, num):
	return a**2 - num

def find_sqrt(x, n):
	if abs(x**2 - n) < tol:
		return x
	x = x - fx(x, n)/diff_fx(x)
	return find_sqrt(x, n)

# Test case: 1
val = 9.06
initial_guess = 2
sqrt_val = find_sqrt(initial_guess, val)
print(sqrt_val) # Should print 3.0099998103859167

# Test case: 2
val = 4.01
initial_guess = 1
sqrt_val = find_sqrt(initial_guess, val)
print(sqrt_val) # Should print 2.00249853499702

# Test case: 2
val = 95.09
initial_guess = 9
sqrt_val = find_sqrt(initial_guess, val)
print(sqrt_val) # Should print 9.751410154563747

"""
Comment: the time complexity of Newton's method is
O(log n) where n is the precision of tolerance. The space complexity
is O(1).
"""

"""
prev = 3
for _ in range(5):
	next = prev - fx(prev)/diff_fx(prev)
	prev = next
	print(prev, prev**2)
"""
