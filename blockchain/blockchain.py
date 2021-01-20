from hashlib import sha256
from datetime import datetime

class Block:

    def __init__(self, index, previous_hash, timestamp, data, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = hash

    def do_hash(self):
        block = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.data) + str(self.nonce)
        return sha256(block.encode('utf-8')).hexdigest()


class Blockchain: 
    number_of_zero = 4

    def __init__(self):
        self.blocks = []
        self.add_first_block()
    
    def get_blocks(self):
        return self.blocks
 
    def add_first_block(self):
        first_block = Block(0, '0', datetime.now(), 'Genesis block', '0')
        first_block.hash = first_block.do_hash()
        self.blocks.append(first_block)

    def new_block(self, data):
        new_block = Block(
            index = self.blocks[-1].index + 1,
            previous_hash = self.blocks[-1].hash,
            timestamp = datetime.now(),
            data = data,
            nonce = '0'
        )

        return new_block

    def add_block(self, block):
        self.correct_hash(block)
        self.blocks.append(block)

    def correct_hash(self, block):
        exec_hash = block.do_hash()
        block.nonce = 0

        while not exec_hash.startswith('0' * Blockchain.number_of_zero):
            block.nonce += 1
            exec_hash = block.do_hash()

        block.hash = exec_hash
    

bchain = Blockchain()

block_n1 = bchain.new_block("Second Block")
bchain.add_block(block_n1)

block_n2 = bchain.new_block("Third Block")
bchain.add_block(block_n2)

block_n3 = bchain.new_block("Fourth Block")
bchain.add_block(block_n3)

for block in bchain.get_blocks():
    print("index : ", block.index)
    print("previous hash : ", block.previous_hash)
    print("timestamp : ", block.timestamp)
    print("data : ", block.data)
    print("hash : ", block.hash)
    print("nonce : ", block.nonce)
    print("\n")