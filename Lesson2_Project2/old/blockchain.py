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
	    self.head = None
	    self.tail = None
	    self.num_element = 0

    def add_block(self, timestamp, data, previous_hash=None):
		if head is None:
		    self.head = Block(timestamp, data, previous_hash)
		    self.tail = self.head
		else:
			self.tail = Block(timestamp, data, previous_hash)
    
    def print_blockchain(self):
		pass

def calc_hash1(data):
	sha = hashlib.sha256()
	hash_str = data.encode('utf-8')
	sha.update(hash_str)
	return sha.hexdigest()

# Data
data1 = "transaction1"
data2 = "transaction2"
data3 = "transaction3"

# Timestamp
timestamp1 = "10:50 06/06/2019"
timestamp2 = "13:40 06/07/2019"
timestamp3 = "18:19 06/08/2019"

# Calculate hash
key2 = calc_hash1(data2)
my_dict = dict({})
my_dict[key2] = 1
print(my_dict)

