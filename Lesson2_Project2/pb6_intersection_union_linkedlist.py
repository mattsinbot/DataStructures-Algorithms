class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
        
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

def union(llist_1, llist_2):
    # Your Solution Here
    union_linked_list = LinkedList()
    
    set_1 = set(llist_1.to_list())
    set_2 = set(llist_2.to_list())
    
    union_element = list(set_1.union(set_2))
    
    for i in union_element:
        union_linked_list.append(i)
        
    return union_linked_list
    

def intersection(llist_1, llist_2):
    # Your Solution Here
    intersection_linked_list = LinkedList()
    
    set_1 = set(llist_1.to_list())
    set_2 = set(llist_2.to_list())
    
    intersection_element = list(set_1.intersection(set_2))
    
    if not len(intersection_element):
        print("Intersection list is empty")
    
    for i in intersection_element:
        intersection_linked_list.append(i)
        
    return intersection_linked_list


# Test case 1
print("\n Test case : 1")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))


# Test case 2
print("\n Test case : 2")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3
print("\n Test case : 3")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1, 1, 2, 2, 6, 6]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

"""
Comment:
In this problem, 3 key functions have been implemented.
1. intersection(llist_1, llist_2): returns a linked list with elements obtained by union of two given linked-lists.

Given two linked-lists, linked_list_1 and linked_list_2, using to_list() method a we first obtained two lists consist of the elements of linked_list_1 and linked_list_2 respectively. Those two lists then converted to two sets using Python's built-in data structure "set". After that using set.intersection() function, we got a new set with elements which are common in both the sets. The resulting set is then converted to a list. The elements of the resultant list is then appended to a newly instantiated linked-list and returned to the user. 
The worst case time complexity of this function is dictated by the two main operations: (a) traversing the two given linked-lists -> O(n) (b) appending intersection elements into a new linked-list -> O(n). Hence overall, this function takes O(n). Using the same reasoning we can say that space complexity will also be O(n).

2. union(llist_1, llist_2): returns a linked list with elements obtained by intesection of two given linked-lists.

The implementation follow exactly same steps as in "implementation" function with only difference is that instead of calling "set.intersection()", here we called "set.union()" instead.

The time and space complexity, both are O(n), following the same reasioning as we did for "intersection" function.

3. to_list(self): a method of class "LinkedList", which returns a list, consists of the values of the nodes of the given linked-list.
Time complexity: O(n). Space complexity: O(n).
"""
