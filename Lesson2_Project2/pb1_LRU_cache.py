class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node    # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail = self.tail.next   # shift the tail (i.e., the back of the queue)
        self.num_elements += 1
            
    # Add the dequeue method
    def dequeue(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return value
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0

class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.data_store = dict({})
        self.data_queue = Queue()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.data_store:
            self.data_queue.dequeue()
            self.data_queue.enqueue(key)
            return self.data_store[key]
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.data_queue.size() >= self.capacity:
            oldest_key = self.data_queue.dequeue()
            del self.data_store[oldest_key]

        # if key not in self.data_store:
        self.data_store[key] = value
        self.data_queue.enqueue(key)


# Test case : 1
print("\n Test case 1")
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Test case : 2
print("\n Test case 2")
our_cache2 = LRU_Cache(3)
our_cache2.set(1, 1)
our_cache2.set(2, 2)
our_cache2.set(3, 3)
our_cache2.set(4, 4)

print(our_cache2.get(1))  # returns -1
print(our_cache2.get(2))  # returns 2
print(our_cache2.get(9))  # returns -1 because 9 is not present in the cache

# Test case : 3
print("\n Test case 3")
our_cache3 = LRU_Cache(3)

print(our_cache3.get(1))  # returns -1 because nothing is set
print(our_cache3.get(2))  # returns -1 because nothing is set
print(our_cache3.get(9))  # returns -1 because nothing is set

"""
Comment:
The solution consists of three classes, namely "LRU-Cache", "Queue" and "Node".
While the main code can be found in "LRU-Cache" class, the other two classes are
used as underlying building blocks.
The "set()" method, stores data in a dictionary which always maintains its size to be &lt; 5.
The size of the dictionary is maintained by always deleting the oldest key-value pair
from the dictionary. Further, whenever a new element is added to the dictionary, the
corresponding key is also "enqueued" into the "data_queue" (a class attribute) to keep
track of the order of the "keys" added to the "LRU-Cache".
The "get()" method, simply first looks for the "key" if that exists in the dictionary. If the
key does not exist, then it returns -1. On the other hand if the "key" exists, then the
method first dequeues the same key from the "data_queue" (a class attribute) and again
enqueues back to it. This how we ensure that we always dequeue the oldest element
from the queue.

Time complexity:
In "set()" method, storing the new entry into the "data_store" variable takes O(1) time,
since it uses a Python dictionary which in turn is a hash-map data structure. Also
"enqueue"-ing the key into "data_queue" takes constant time, O(1). Further, in cases
when removal of an element from the key is necessary, the "dequeue"-ing operation
also takes O(1) time and deleting the oldest key from the "data_store" also takes O(1)
time. Therefore overall, "set()" method takes O(1) time.

In "get()" method, the "dequeue"-ing and "enqueue"-ing methods, again takes O(1) time
each. Also fetching the value corresponding to the "key" also takes O(1) time.
Space complexity:
Both the variables, "data_store" and "data_queue" require O(n) space where n is the capacity of the cache.
"""
