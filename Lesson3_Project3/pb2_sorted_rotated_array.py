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
			print(start, end)
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
	if input_list[mid] == num:
		return mid
	if input_list[mid] > num:
		end = mid - 1
	else:
		start = mid + 1
	return BinarySearch(input_list, num, start, end)

# Sorted and rotated list
a_list = [78, 82, 99, 105, 23, 35, 49, 51, 60]
pivot_index = FindPivot(a_list)
print(pivot_index)

"""
O(log n) for pivot finding
O(log n) for binary search
Total time complexity: O(log n) + O(log n) ~ O(log n)
"""
a_list = [105, 110, 120, 150, 10, 23, 35, 49, 51, 60]
search_for = 120
pivot_index_recursion = FindPivotCall(a_list)
print(pivot_index_recursion)
if search_for >= a_list[pivot_index] and search_for <= a_list[len(a_list) - 1]:
	start_index, end_index = pivot_index, len(a_list) - 1
else:
	start_index, end_index = 0, pivot_index - 1
searched_index = BinarySearch(a_list, search_for, start_index, end_index)
print(searched_index)
