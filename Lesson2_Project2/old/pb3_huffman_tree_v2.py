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
      

# Function to build Huffman tree
def build_huffman_tree(message):
	message_dict = dict({})
	node_dict = dict({})

	# Read each character of the message and record their frequencies
	for ch in message:
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
	# print(sorted_x)

	# Build the Huffman tree
	root_tree = None
	while root_tree is None:
	  if len(sorted_x) == 1:
		root_tree = node_dict[sorted_x[0][0]]
		break
	  value = sorted_x[0][1] + sorted_x[1][1]
	  key = sorted_x[0][0] + sorted_x[1][0]
	  new_tuple = (key, value)
	  new_node = Node(value, key)
	  new_node.left_child = node_dict[sorted_x[0][0]]
	  new_node.right_child = node_dict[sorted_x[1][0]]
	  node_dict[key] = new_node
	  del mutating_dict[sorted_x[0][0]]
	  del mutating_dict[sorted_x[1][0]]
	  mutating_dict[key] = value
	  sorted_x = sorted(mutating_dict.items(), key=operator.itemgetter(1))
	return root_tree
	
# Pre-Order Tree Traversal
def pre_order(root_t):
    visit_order = list()
    encoding_dict = dict({})
    new_root = root_t
    
    def traverse(node):
      if node:
        visit_order.append(node.get_key())
        if node.get_left_child():
          node.get_left_child().set_encoding(node.get_encoding()+"0")
          traverse(node.get_left_child())
        if node.get_right_child():
          node.get_right_child().set_encoding(node.get_encoding()+"1")
          traverse(node.get_right_child())
        if not node.get_left_child():
          if not node.get_right_child():
            encoding_dict[node.get_key()] = node.get_encoding()
        
    traverse(new_root)
    return visit_order, encoding_dict
    
# Encode message
def encode_message(msg, encoding_table):
	pass
	
# Decode message
def decode_message(code_str, root_node):
	node = root_node
	indx = 1
	decoded_msg = ""
	while(indx < len(code_str)):
		if code_str[indx] == "0":
			node = node.get_left_child()
		else:
			node = node.get_right_child()
		indx += 1
		if (node.left_child is None) and (node.right_child is None):
			decoded_msg += node.key
			node = root_node
			indx += 1
	return decoded_msg


# Decode message recursion
def decode_message_recursion(code_str, root_node):
	decoded_str, indx_dict = {}, {}
	indx_dict["indx"] = 1
	decoded_str["msg"] = ""
	def decode(node):
		found = False
		if not found:
			if code_str[indx_dict["indx"]] == "0":
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
	while (indx_dict["indx"] < len(code_str)):
		decode(root_node)
	return decoded_str["msg"]

# Call Build_Huffman_Tree
msg = "The bird is the word" 
root = build_huffman_tree(msg)
root.set_encoding("0")

# Traverse the tree
visiting_order, encoded_table = pre_order(root)
print(visiting_order)
print(encoded_table)

# Using the encoding table, encode the message
encoded_str = ""
for ch in msg:
	 encoded_str += encoded_table[ch]
print(encoded_str)

# Traverse back the tree to decode the encoded string
# decoded_msg = decode_message(encoded_str, root)
# print(decoded_msg)

decoded_msg = decode_message_recursion(encoded_str, root)
print(decoded_msg)



# Check Huffman tree manually
# print(root.get_left_child().get_left_child().get_left_child().get_left_child().get_key())
# print(root.get_right_child().get_right_child().get_right_child().get_right_child().get_right_child().get_key())





