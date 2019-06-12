import operator
import copy

class Node:
  def __init__(self, value=None, key=None):
    self.value = value
    self.key = key
    self.left_child = None
    self.right_child = None

message = "The bird is the word"
message_dict = dict({})
node_dict = dict({})

for ch in message:
  if ch not in message_dict:
    message_dict[ch] = 1
  else:
    message_dict[ch] += 1


for key in message_dict:
  node_dict[key] = Node(message_dict[key], key)

mutating_dict = copy.deepcopy(message_dict)
node_info_dict = copy.deepcopy(message_dict)
sorted_x = sorted(message_dict.items(), key=operator.itemgetter(1))
root = None
while root is None > 0:
  if len(sorted_x) == 1:
    root = node_dict[sorted_x[0][0]]
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
  node_info_dict[key] = value
  sorted_x = sorted(mutating_dict.items(), key=operator.itemgetter(1))

print(root.left_child.left_child.left_child.left_child.key)
