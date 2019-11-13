# created a new file because when we modularize the program, we can make it
# work better

class Block:
    """
    block - unit of storage
    """

    def __init__(self, timestamp, last_hash, hash, data):  # block class is where data is added
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash  # data structure of the blockchain.
        self.data = data

    def __repr__(self):  # another dunder method to override the implementation of
        # standard printing of object address
        return f'Block - Data: {self.data}'
