"""
Write down the merge sort algorithm. Currently we are calling python;s built-in sorting() method.
The main work is done in the while-loop which takes O(n) computations in worst case.
"""

def MaxSumNumbers(input_list):
	input_list.sort()
	input_list.reverse()
	print(input_list)
	
	n = len(input_list)

	first_num, second_num = 0, 0
	index = 0
	if n % 2 == 0:
		print("input list has even number of elements")
	else:
		print("input list has odd number of elements")
		first_num = input_list[0]
		index = 1

	while index < n-1:
		first_num = first_num*10 + input_list[index]
		second_num = second_num*10 + input_list[index + 1]
		index += 2

	return first_num, second_num

# Test case : 1
input_list = [4, 6, 2, 7, 9, 8]
first, second = MaxSumNumbers(input_list)
print(first, second)

# Test case : 2
input_list = [1, 2, 3, 4, 5]
first, second = MaxSumNumbers(input_list)
print(first, second)
	


	
