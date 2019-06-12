import operator
import copy
import sys

# Node class
class Node:
  def __init__(self, value=None, key=None):
    self.value = value
    self.key = key
    self.left_child = None
    self.right_child = None
    self.encoding = None
    
  # Setter methods
  def set_left_child(self, node):
    self.left_child = node
    
  def set_right_child(self, node):
    self.right_child = node
    
  def set_encoding(self, val):
    self.encoding = val
    
  # Getter methods
  def get_value(self):
    return self.value
    
  def get_key(self):
    return self.key
  
  def get_left_child(self):
    return self.left_child
    
  def get_right_child(self):
    return self.right_child
    
  def get_encoding(self):
    return self.encoding

# Huffman_Tree class
class Huffman_Tree:
	def __init__(self, text_message):
		self.root = None
		self.message = text_message
		self.encoded_msg = ""
		self.visit_order = list()
		self.encoding_dict = dict({})
		
	# Function to build Huffman tree
	def build_huffman_tree(self):
		message_dict = dict({})
		node_dict = dict({})

		# Read each character of the message and record their frequencies
		for ch in self.message:
		  if ch not in message_dict:
			message_dict[ch] = 1
		  else:
			message_dict[ch] += 1

		# Generate dictionary with keys as each character and value as Node objects 
		for key in message_dict:
		  node_dict[key] = Node(message_dict[key], key)

		# Create a temporary dictionary with characters and frequencies of the message
		mutating_dict = copy.deepcopy(message_dict)

		# Get a sorted list of characters based on their frequencies
		sorted_x = sorted(mutating_dict.items(), key=operator.itemgetter(1))
		
		# Build the Huffman tree
		while self.root is None:
		  if len(sorted_x) == 1:
			self.root = node_dict[sorted_x[0][0]]
			break
		  value = sorted_x[0][1] + sorted_x[1][1]
		  key = sorted_x[0][0] + sorted_x[1][0]
		  new_node = Node(value, key)
		  new_node.left_child = node_dict[sorted_x[0][0]]
		  new_node.right_child = node_dict[sorted_x[1][0]]
		  node_dict[key] = new_node
		  del mutating_dict[sorted_x[0][0]]
		  del mutating_dict[sorted_x[1][0]]
		  mutating_dict[key] = value
		  sorted_x = sorted(mutating_dict.items(), key=operator.itemgetter(1))
		  
	# Pre-Order Tree Traversal
	def pre_order(self):
		self.build_huffman_tree() # Build the tree
		self.root.set_encoding("0")		
		def traverse(node):
		  if node:
		    self.visit_order.append(node.get_key())
		    if node.get_left_child():
		      node.get_left_child().set_encoding(node.get_encoding()+"0")
		      traverse(node.get_left_child())
		    if node.get_right_child():
		      node.get_right_child().set_encoding(node.get_encoding()+"1")
		      traverse(node.get_right_child())
		    if not node.get_left_child():
		      if not node.get_right_child():
		        self.encoding_dict[node.get_key()] = node.get_encoding()		    
		traverse(self.root)
		
	# Encode message
	def encode_message(self):
		self.pre_order() # traverse the tree and generate encodings
		for ch in self.message:
			self.encoded_msg += self.encoding_dict[ch]

	# Decode message
	def decode_message(self):
		node = self.root
		indx = 1
		decoded_msg = ""
		while(indx < len(self.encoded_msg)):
			if self.encoded_msg[indx] == "0":
				node = node.get_left_child()
			else:
				node = node.get_right_child()
			indx += 1
			if (node.left_child is None) and (node.right_child is None):
				decoded_msg += node.key
				node = self.root
				indx += 1
		return decoded_msg

	# Decode message recursion
	def decode_message_recursion(self):
		decoded_str, indx_dict = {}, {}
		indx_dict["indx"] = 1
		decoded_str["msg"] = ""
		def decode(node):
			found = False
			if not found:
				if self.encoded_msg[indx_dict["indx"]] == "0":
					node = node.get_left_child()
				else:
					node = node.get_right_child()
				indx_dict["indx"] += 1
				if (node.left_child is None) and (node.right_child is None):
					decoded_str["msg"] += node.key
					indx_dict["indx"] += 1
					found = True
					return found
				else:
					decode(node)
		while (indx_dict["indx"] < len(self.encoded_msg)):
			decode(self.root)
		return decoded_str["msg"]
		
# Test case 1:
print("\nTest case: 1")
msg = "The bird is the word"
huff_tree1 = Huffman_Tree(msg)
huff_tree1.encode_message()
print(huff_tree1.encoded_msg)
print(huff_tree1.decode_message())
print(huff_tree1.decode_message_recursion())

# Test case 2:
print("\nTest case: 2")
msg = "Insanity: doing the same thing over and over again and expecting different results"
huff_tree2 = Huffman_Tree(msg)
huff_tree2.encode_message()
print(huff_tree2.encoded_msg)
print(huff_tree2.decode_message())
print(huff_tree2.decode_message_recursion())

# Test case 3:
print("\nTest case: 3")
msg = "+*/1234"
huff_tree3 = Huffman_Tree(msg)
huff_tree3.encode_message()
print(huff_tree3.encoded_msg)
print(huff_tree3.decode_message())
print(huff_tree3.decode_message_recursion())

"""
Comment:
Implemented "Huffman_Tree" class. The constructor needs one input argument which is the the text message to be encoded. The "encode_message()" method is the main function that encodes the text message and stores it in the class attribute named "encoded_msg". The "encode_message()" calls "pre_order()" method under the hood to traverse the tree which in turn calls "build_huffman_tree()" method to actually build the tree.

In order to decode, either of the two methods namely "decode_message" or "decode_message_recursion" can be used. Both these functions uses the encoded string stored in the class attribute "encoded_msg".

Time complexity:
In greedy approach, we put "n" characters into "n" leaves and move upward by creating new nodes by adding two least frequent nodes recursively. At each iteration we need to perform sorting operation to find two least frequent nodes. This sorting operation takes O(log n) time. To encode "n" distinct characters we need "n" such iteration which requires O(n) time. Hence all total encoding requires O(nlogn) times.
"""
