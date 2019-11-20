# My solution
class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}
        
    def suffixes(self):
        suggestion_list = []
        
        def recurse_suggestion(node, node_key):
            small_suggestion_list = []
            
            # If the current key is the last char of a word and 
            # current node has empty children, then just return 
            # empty suggestion
            if node.is_word and not node.children:
                return small_suggestion_list
            
            # If the current key is the last char of a word and 
            # current node has children, then append an empty 
            # string to the small_suggestion_list
            if node.is_word and node.children:
                small_suggestion_list.append("")
            
            # For each key in the current node's children preform the following
            for nkey in node.children:
                # Get smaller suggestions by recursively calling 
                # recurse_suggestion() in a list named small_suff
                small_suff = recurse_suggestion(node.children[nkey], nkey)
                
                # If small_suff is empty, just append the current key
                if len(small_suff) == 0:
                    small_suggestion_list.append(nkey)
                    continue
                
                # When small_suff is non empty, concatenate current key with intermediate
                # suggestions and append it to the small_suggestion_list
                for j in small_suff:
                    small_suggestion_list.append(nkey + j)
            return small_suggestion_list
        
        # Loop through all the keys of the child field of current node
        for key in self.children:
            suff = recurse_suggestion(self.children[key], key)
            for i in suff:
                suggestion_list.append(key + i)

        return suggestion_list


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root        
        for char in word:
            if not char in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_word = True            

    def exists(self, word):
        current_node = self.root        
        for char in word:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        return current_node.is_word
    
    def find(self, prefix):
        current_node = self.root
        count = 0
        # Loop through the prefix character
        for char in prefix:
            if not char in current_node.children:
                return None
            current_node = current_node.children[char]
        # Return the node obtained by last char of prefix string.
        # This node will be used for suffix computation.
        return current_node


# Case : 1
MyTrie = Trie()
wordList = ["ant", "anthology", "antagonist", "antonym", "fun", "function", "factory", "trie", "trigger", "trigonometry", "tripod"]

for word in wordList:
    MyTrie.insert(word)
MyTrie.exists("fun")

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
            # print(prefixNode.suffixes())
        else:
            print(prefix + " not found")
    else:
        print('')

interact(f,prefix='')

"""
Majority of the work goes into performing "suffixes()" method.
Time Complexity: If for a given prefix, there are n possible suffixes then they can be found in O(n) time
Space Complixity: Size of the list of all suffixes is O(n)
"""
