class Block:
    """
    block - unit of storage
    """
    def __init__(self, data): #block class is where data is added
        self.data = data

    def __repr__(self): #another dunder method to override the implementation of
        #standard printing of object address
        return f'Block - Data: {self.data}'

class Blockchain:
    """
    implemented as a list of blocks
    - datasets of transactions

    """
    def __init__(self):
        self.chain = []
    
    def add_block(self, data):
        self.chain.append(Block(data)) # we append the block to the list
    
    def __repr__(self):
        return f'Blockchain : {self.chain}'
'''
blockchain = Blockchain()
blockchain.add_block('one')
blockchain.add_block('two')
print(blockchain)
# this is the test for following lines : 
####
class Block:
    """
    block - unit of storage
    """
    def __init__(self, data): #block class is where data is added
        self.data = data

    def __repr__(self): #another dunder method to override the implementation of
        #standard printing of object address
        return f'Block - Data: {self.data}'

class Blockchain:
    """
    implemented as a list of blocks
    - datasets of transactions

    """
    def __init__(self):
        self.chain = []
    
    def add_block(self, data):
        self.chain.append(Block(data)) # we append the block to the list
    
    def __repr__(self):
        return f'Blockchain : {self.chain}'
        '''
'''