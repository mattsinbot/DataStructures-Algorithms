def find_max_min(input_list):
	n = len(input_list)
	
	if input_list[0] < input_list[1]:
		min_val = input_list[0]
		max_val = input_list[1]
	else:
		min_val = input_list[1]
		max_val = input_list[0]

	for i in range(2, n):
		if input_list[i] > max_val:
			max_val = input_list[i]
		elif input_list[i] < min_val:
			min_val = input_list[i]
			
	return max_val, min_val

# Test case : 1
my_list = [10, 5, 9, 46, 3, 78, 1054]
max_v, min_v = find_max_min(my_list)
print(my_list)
print("max: %d, min: %d"%(max_v, min_v)) # output max: 1054, min: 3

# Test case : 2
my_list = [12, 45, 48, 12, 12]
max_v, min_v = find_max_min(my_list)
print("max: %d, min: %d"%(max_v, min_v)) # output max: 48, min: 12

# Test case : 3
my_list = [110, 550, 90, 160, 750, 10, 60]
max_v, min_v = find_max_min(my_list)
print("max: %d, min: %d"%(max_v, min_v)) # output max: 750, min: 10

"""
Comment:
In one pass of through the array, maximum and minimum element of the input list has been found. Therefore the time complexity is O(n). Space complexity O(1).
"""
