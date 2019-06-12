import hashlib

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        
    def calc_hash(self):
	    sha = hashlib.sha256()
	    hash_str = self.data.encode('utf-8')
	    sha.update(hash_str)
	    return sha.hexdigest()

class BlockChain:
    def __init__(self):
	    self.block_dict = dict({})
	    self.head = None
		
    def add_block(self, timestamp, data):
    	if not self.head:
		    previous_hash = None
        else:
		    previous_hash = self.head
        new_block = Block(timestamp, data, previous_hash)
        self.block_dict[new_block.hash] = new_block
        self.head = new_block.hash
        
    def __str__(self):
    	if not self.head:
    		print("BlockChain is empty")
    	else:
        	self.print_blockchain(self.head)
        return "End of BlockChain"
        
    def print_blockchain(self, hash_key):
        new_key = hash_key
        if not new_key:		    
		    return
        else:
		    print("------------------------")
		    print("Block: ")
		    print("data: %s"%(self.block_dict[new_key].data))
		    print("Time-stamp: %s"%(self.block_dict[new_key].timestamp))
		    print("------------------------")
		    new_key = self.block_dict[new_key].previous_hash
		    self.print_blockchain(new_key)

# Test case : 1
print("\n Tets case : 1")
# Data
data1 = "transaction1"
data2 = "transaction2"
data3 = "transaction3"

# Timestamp
timestamp1 = "10:50 06/06/2019"
timestamp2 = "13:40 06/07/2019"
timestamp3 = "18:19 06/08/2019"

# Instantiate a BlockChain
block_chain = BlockChain()

# Add blocks to the BlockChain
block_chain.add_block(timestamp1, data1)
block_chain.add_block(timestamp2, data2)
block_chain.add_block(timestamp3, data3)

# Manual test
# print(block_chain.block_dict[block_chain.head].data)
# print(block_chain.block_dict[block_chain.head].timestamp)
# print(block_chain.block_dict[block_chain.head].previous_hash)

# Check print_blockchain() method
# block_chain.print_blockchain(block_chain.head)
print(block_chain)

# Test case : 1
print("\n Tets case : 2")

# Instantiate a BlockChain
block_chain2 = BlockChain()

print(block_chain2)

# Test case : 3
print("\n Tets case : 3")
block_chain3 = BlockChain()

data = "transaction"
timestamp = "18:19 06/08/2019"
block_chain3.add_block(timestamp, data)
print(block_chain3)



"""
Comment:
The main work geos into creating the "BlockChain" class and modifying "calc_hash" method of "Block" class.
1. Modifying "calc_hash" method:
This function id changed in such a way, it can use its "data" attribute to finally return a hash-string out of data.
Time complexity: creating the "hash-string" is a O(1) operation

2. The main container of "BlockChain" class is a dictionary, named "block_dict". Each block of information is stored 
as a value of the dictonary whereas keys are generated using "calc_hash" method.
In order to add linked-list flavor to accessing the data stored in "block_dict", we simply shift the head to point it to the newly created block object. The ultimate block is linked to its prior through the "previous_hash" attribute of the Block object.
Time complexity:
"add_block()" method needs O(1) time.
"print_blockchain()" method needs O(n) time where n is the number of blocks present
"""
