# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler_name):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler_name)

    def insert(self, path2list, handler_name):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        n = len(path2list)
        for indx, part in enumerate(path2list):
            if not part in current_node.children:
                if indx == n - 1:
                    current_node.children[part] = RouteTrieNode(handler_name)
                else:
                    current_node.children[part] = RouteTrieNode()
            current_node = current_node.children[part]

    def find(self, path2list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root        
        for part in path2list:
            if part in current_node.children:
                current_node = current_node.children[part]
            else:
                return None
        return current_node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self):
        # Insert the node as before
        pass


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler_name):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(root_handler_name)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path2list = self.split_path(path)
        self.route_trie.insert(path2list, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path2list = self.split_path(path)
        return self.route_trie.find(path2list)
        # print(handler)

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path2list = path.split("/")
        if path[-1] == "/":
            path2list = path2list[1:-1]
        else:
            path2list = path2list[1:]
        return path2list
        
# Test case : 1
# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print("==========Test case 1============================")
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print None
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler'
print(router.lookup("/home/about/me")) # should print None

# Test case : 2
# create the router and add a route
print("==========Test case 2============================")
router2 = Router("root handler2")
router2.add_handler("/home/name_page/name", "name handler")  # add a route

# some lookups with the expected output
print(router2.lookup("/")) # should print 'root handler2'
print(router2.lookup("/home")) # should print None
print(router2.lookup("/home/name_page")) # should print None
print(router2.lookup("/home/name_page/")) # should print None
print(router2.lookup("/home/name_page/name")) # should print 'name handler'
print(router2.lookup("/home/name_page/name/")) # should print 'name handler'

# Test case : 3
# create the router and add a route
print("==========Test case 3============================")
router3 = Router("root handler3")
router3.add_handler("/home/portfolio_page/subject/robotics", "robotics page handler")  # add a route

# some lookups with the expected output
print(router3.lookup("/")) # should print 'root handler3'
print(router3.lookup("/home/name_page")) # should print None
print(router3.lookup("/home/name_page/")) # should print None
print(router3.lookup("/home/portfolio_page/subject/robotics")) # should print "robotics page handler"
print(router3.lookup("/home/portfolio_page/subject/robotics/")) # should print "robotics page handler"



"""
Most of the work goes into performing "add_handler" method and "lookup method"
Time Complexity: is proportional to O(n) for add_handler method if there are n words in the path and O(1) for lookup method since hash-map has been used to store the paths 
Space Complexity: O(n) for add_handler method and O(1) for loopup method
"""
