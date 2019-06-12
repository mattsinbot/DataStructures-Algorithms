class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    def find_user(user, group):
    	decision = False
    	if user in group.get_users():
    		decision = True
    	
    	if not decision:
			for each_group in group.get_groups():
				# print(each_group.get_name())
				if user in each_group.get_users():
					decision = True
					# print("Yes")
					return decision
				else:
					decision = find_user(user, each_group)

    	return decision
    
    return find_user(user, group)

# Test case : 1
print("\nTest case: 1")
# Create few groups
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

# Create few users
sub_child_user1 = "sub_child_user1"
sub_child_user2 = "sub_child_user2"
child_user1 = "child_user1"
parent_user1 = "parent_user1"

# Assign the users to the group
sub_child.add_user(sub_child_user1)
sub_child.add_user(sub_child_user2)
child.add_user(child_user1)
parent.add_user(parent_user1)


# Merge sub_child group and child group to the parenet group
child.add_group(sub_child)
parent.add_group(child)

# Check if a specific user belongs to a specific group
# is_user = is_user_in_group("sdfv", parent)
is_user = is_user_in_group("sub_child_user1", parent)
print(is_user) # Should print "True"

# Test case : 2
print("\nTest case: 2")
# Create few groups
parent2 = Group("parent")
child2 = Group("child")

# Create few users
child_user1 = "child_user1"
child_user2 = "child_user2"

# Assign the users to the group
child2.add_user(child_user1)
child2.add_user(child_user2)

# Merge sub_child group and child group to the parenet group
parent2.add_group(child2)

# Check if a specific user belongs to a specific group
# is_user = is_user_in_group("sdfv", parent)
is_user = is_user_in_group(child_user1, parent)
print(is_user) # Should print "True"

# Test case : 3
print("\nTest case: 3")
is_user = is_user_in_group("child_user3", parent)
print(is_user) # Should print "False"

"""
Comment:
is_user_in_group(): 
Given a user(string) and a group, this function recursively digs into the groups user list to find if user exists in that list. If the current group has sub or sub-sub or deeper groups, the function recursively calls itself to go over all the nested groups.
The "is_user_in_group" function, actally has a nested "find_user" function which is called in recursive manner.

Time complexity:
If the number of group and all of nested sub-groups is "n" and each of those groups has "m" users, then in worst-case, finding a given user-name takes O(m*n) times.

Space complexity:
Using the same analogy as time complexity, the worst case space-complexity would be O(m*n). 
"""
