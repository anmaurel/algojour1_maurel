from hashlib import sha256
from datetime import datetime
from tkinter import *
from flask import Flask, request
import json

"""
Block
"""
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

"""
Blockchain
"""
class Blockchain: 
    number_of_zero = 4

    def __init__(self):
        self.blocks = []
        self.add_first_block()
    
    def get_blocks(self):
        blocks = {}
        blocks['block'] = []
        for block in self.blocks:
            blocks['block'].append(
                {
                    'index' : block.index,
                    'previous hash' : block.previous_hash,
                    'timestamp' : block.timestamp,
                    'data' : block.data,
                    'hash' : block.hash,
                    'nonce' : block.nonce,
                }
            )

        return blocks
 
    def add_first_block(self):
        first_block = Block(0, '0', datetime.now(), 'Genesis block', '0')
        self.correct_hash(first_block)
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

        with open('blocks.json', 'w') as push:
            json.dump(push)

    def correct_hash(self, block):
        exec_hash = block.do_hash()
        block.nonce = 0

        while not exec_hash.startswith('0' * Blockchain.number_of_zero):
            block.nonce += 1
            exec_hash = block.do_hash()

        block.hash = exec_hash
    
    def submit(): 
        input_block = input.get() 
        print("The data is : " + input_block) 
    
    def delete_block(index_block):
        if index_block in self.blocks:
            self.blocks.remove(index_block)
        
        if index_block < len(self.blocks):
            for block in self.blocks:
                for b in range(index_block, len(self.blocks)):
                    self.blocks.remove(b)

    def delete_last_block():
        self.blocks.pop()

    def checkBlock(index_block):
        return self.blocks[index_block]




bchain = Blockchain()


"""
API Flask
"""
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_all_blocks():
    return json.dumps(bchain.get_blocks(), sort_keys = True, default = str, indent = 2)

@app.route('/add', methods=['POST'])
def add_block():
    data = request.form.get('data')
    block = bchain.new_block(data)
    bchain.add_block(block)
    return json.dumps(bchain.get_blocks(), sort_keys = True, default = str, indent = 2)



app.run(debug = True, port = 5000)

"""
User Interface
"""
ui = Tk()

ui.title('Blockchain IIM')
ui.geometry("600x600+20+20")

label = Label(ui, text="Nom de block :")
label.pack()
input = Entry(ui) 
input.pack()
input.focus_set()

def return_blocks():
    block = bchain.new_block(input.get())
    bchain.add_block(block)

    results.config(text = format_results())
    input.delete(0,END)

def format_results():
    blocks = []
    for block in bchain.get_blocks():
        blocks.append([
            "index : " + str(block.index) + "",
            block.previous_hash,
            block.timestamp,
            block.data,
            block.hash,
            block.nonce,
        ])

    return blocks

button = Button(ui, text = "Créer", width = 10, command = return_blocks)
button.pack()

results = Label(ui, height = 100, width = 600, wraplength = 600)
results.pack()

ui.mainloop()