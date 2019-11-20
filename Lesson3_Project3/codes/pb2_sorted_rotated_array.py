"""
Following code returns index of pivot_element (minimum elment) in the array. At each iteration, the search interval is halved making it a 
O(log n) time algorithm.
"""
def FindPivot(input_list):
	# Check if sorted array in unrotated
	if input_list[0] < input_list[-1]:
		return 0
		
	start_index, end_index = 0, len(input_list) - 1
	while (start_index <= end_index):
		mid_index = (start_index + end_index) // 2
		# Chech if mid index is pivot
		if input_list[mid_index] > input_list[mid_index + 1]:
			return mid_index + 1
		# Adjust start or end index for next iteration
		if input_list[start_index] > input_list[mid_index]:
			end_index = mid_index - 1
		else:
			start_index = mid_index + 1
			
def FindPivotCall(input_list):
	# Check if sorted array in unrotated
	if input_list[0] < input_list[-1]:
		return 0
		
	start_index, end_index = 0, len(input_list) - 1
	def FindPivotRecursion(start, end):
		if start >= end:
			# print(start, end)
			return start + 1
		mid = (start + end) // 2
		
		# Chech if mid index is pivot
		if input_list[mid] > input_list[mid + 1]:
			return mid + 1

		# Adjust start or end index for next iteration
		if input_list[start] > input_list[mid]:
			end = mid - 1
		else:
			start = mid + 1
			
		return FindPivotRecursion(start, end)
	
	return FindPivotRecursion(start_index, end_index)

"""
The following function implements Binary Search in recursive manner. The time complexity of this BS implementation is O(log n).
"""
def BinarySearch(input_list, num, start, end):
	mid = (start + end) // 2
	if mid >= end:
		return None
	if input_list[mid] == num:
		return mid
	if input_list[mid] > num:
		end = mid - 1
	else:
		start = mid + 1
	return BinarySearch(input_list, num, start, end)


def FindNum(iplist, num):
	search_for = num
	pivot_index_recursion = FindPivotCall(a_list)
	# print(pivot_index_recursion)
	if search_for >= a_list[pivot_index_recursion] and search_for <= a_list[len(a_list) - 1]:
		start_index, end_index = pivot_index_recursion, len(a_list) - 1
	else:
		start_index, end_index = 0, pivot_index_recursion - 1
	searched_index = BinarySearch(a_list, search_for, start_index, end_index)
	return searched_index
	
# Test case : 1
a_list = [78, 82, 99, 105, 23, 35, 49, 51, 60]
num = 51
found_index = FindNum(a_list, num)
print("Test case 1: %d"%found_index) # should print 7

# Test case : 2
a_list = [105, 110, 120, 150, 10, 23, 35, 49, 51, 60]
num = 120
found_index = FindNum(a_list, num)
print("Test case 2: %d"%found_index) # should print 2

# Test case : 3
a_list = [105, 110, 120, 150, 78, 82, 99]
num = 100
found_index = FindNum(a_list, num)
print("Test case 3: {}".format(found_index)) # should print None

"""
Time Complexity:
O(log n) for pivot finding
O(log n) for binary search
Total time complexity: O(log n) + O(log n) ~ O(log n)

Space Complexity:
O(1) for pivot finding
O(1) for binary search
Total time complexity: O(1) + O(1) ~ O(1)
"""
