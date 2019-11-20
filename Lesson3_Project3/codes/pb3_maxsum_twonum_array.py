"""
Write down the merge sort algorithm. Currently we are calling python;s built-in sorting() method.

The heap sort takes O(log n) computation. The main work is done in the while-loop of MaxSumNumbers() function which takes O(n) computations in worst case. Therefore all together, finding the answer takes O(n) computations.

The space complexity is O(n) for heap sort whereas MaxSumNumbers() function takes O(1) space. Hence, total space requirement is O(n).
"""

def MaxSumNumbers(input_list):
	# input_list.sort()
	heapsort(input_list)
	input_list.reverse()
	# print(input_list)
	
	n = len(input_list)

	first_num, second_num = 0, 0
	index = 0
	if n % 2 == 0:
		# print("input list has even number of elements")
		index = 0
	else:
		# print("input list has odd number of elements")
		first_num = input_list[0]
		index = 1

	while index < n-1:
		first_num = first_num*10 + input_list[index]
		second_num = second_num*10 + input_list[index + 1]
		index += 2

	return first_num, second_num

# Heap sort algorithm implementation
def heapify(arr, n, i):    
    # consider current index as largest
    largest_index = i 
    left_node = 2 * i + 1     
    right_node = 2 * i + 2     
  
    # compare with left child
    if left_node < n and arr[i] < arr[left_node]: 
        largest_index = left_node
  
    # compare with right child
    if right_node < n and arr[largest_index] < arr[right_node]: 
        largest_index = right_node
  
    # if either of left / right child is the largest node
    if largest_index != i: 
        arr[i], arr[largest_index] = arr[largest_index], arr[i] 
    
        heapify(arr, n, largest_index) 
        
def heapsort(arr):
    # array is sorted
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0)

# Test case : 1
input_list = [4, 6, 2, 7, 9, 8]
first, second = MaxSumNumbers(input_list)
print(first, second) # should print 974 862

# Test case : 2
input_list = [1, 2, 3, 4, 5]
first, second = MaxSumNumbers(input_list)
print(first, second) # should print 542 31

# Test case : 3
input_list = [1, 6, 4, 9, 3, 7]
first, second = MaxSumNumbers(input_list)
print(first, second) # should print 963 741


	
