import os

def read_file_recursively(path, file_extension=None):
	# If file extension is not given
	if file_extension is None:
		return "No file extension provided"
	# If given path is invalid
	if not os.path.exists(path):
		return "invalid path given"
	# If traget directory is empty
	if len(os.listdir(path)) == 0:
		return "target directory is empty"
	def read_file(path):
		store_c_file_path = list()
		all_data = os.listdir(path)
		for p in all_data:
		    new_path = os.path.join(path, p)
		    if os.path.isdir(new_path):
		        # print(new_path)
		        small_path = read_file(new_path)
		        if len(small_path) > 0:
		            for elem in small_path:
		                store_c_file_path.append(elem)
		    elif os.path.isfile(new_path):
		    	if new_path.endswith(file_extension):
		            # print(new_path)
		            store_c_file_path.append(new_path)
		return store_c_file_path
	return read_file(path)

# Test cse: 1
MAIN_PATH = "/home/nobug-ros/Desktop/testdir"
desired_path = read_file_recursively(MAIN_PATH)
print("\n Test case : 1")
print(desired_path)

# Test case: 2
MAIN_PATH = "/home/nobug-ros/Desktop/testdir"
file_ext = ".c"
desired_path = read_file_recursively(MAIN_PATH, file_ext)
print("\n Test case : 2")
print(desired_path)

# Test case: 2
MAIN_PATH = "testdir"
file_ext = ".c"
desired_path = read_file_recursively(MAIN_PATH, file_ext)
print("\n Test case : 3")
print(desired_path)

"""
Comment:
Given a "path" the "read_file_recursively" function, at first gets all possible immediate paths and stores them in a list type variable, called "all_data". Then it loops through all over the discovered paths and check if that path "is a directory" and if "yes" the function calls itself with this current path as input and so on. Otherwise if the current path points to a "*.c" file, the path is then stored in a variable named "store_c_file_path" and is returned.

Time complexity:
If there are "n" nested directories and each of these directories has "m" of the files in them, then in worst case there will be O(m*n) time to find all "*.c" files.

Space complexity:
Using similar analogy, we can say that space complexity will be O(m*n) again.
"""

