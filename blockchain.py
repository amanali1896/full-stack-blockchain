from block import Block #importing from block.py
#import line evaluates the entire from that we import from
#so if we print anything in Block, it gets printed here too. 
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



def main(): 
    #whatever you write here will be executed if this file is the main method
    #otherwise it will not be


def if __name__ == '__main__': #this method will be executed
    #only if this file is a main module.
    #now main module will be found out by the file that is 
    #currently being executes
    main()
    