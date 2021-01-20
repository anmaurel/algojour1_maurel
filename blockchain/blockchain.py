from hashlib import sha256
from datetime import datetime
from tkinter import *
from flask import Flask
from flask_cors import CORS, cross_origin
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
        self.add_block(first_block)

    def new_block(self, data):
        new_block = Block(
            index = self.blocks[-1].index + 1,
            previous_hash = self.blocks[-1].hash,
            timestamp = datetime.now(),
            data = data,
            nonce = '0'
        )

        return new_block

    def format_data(self, block):
        data = {
            'index' : block.index,
            'previous hash' : block.previous_hash,
            'timestamp' : block.timestamp,
            'data' : block.data,
            'hash' : block.hash,
            'nonce' : block.nonce,
        }

        return data

    def add_block(self, block):
        self.correct_hash(block)
        self.blocks.append(block)
        block_formated = self.format_data(block)

        data = json.dumps(block_formated, indent = 4, default = str, ensure_ascii=False)
        with open('blocks.json', 'a') as file:
            file.write(data)

    def correct_hash(self, block):
        exec_hash = block.do_hash()
        block.nonce = 0

        while not exec_hash.startswith('0' * Blockchain.number_of_zero):
            block.nonce += 1
            exec_hash = block.do_hash()

        block.hash = exec_hash

bchain = Blockchain()


"""
User Interface
"""
ui = Tk()

ui.title('Blockchain IIM')
ui.geometry("1200x600+20+20")

label = Label(ui, text="Nom de block :")
label.pack()

data = StringVar()

input = Entry(ui, textvariable = data)
input.pack()

def create():
    block = bchain.new_block(input.get())
    bchain.add_block(block)

    data = bchain.format_data(block)

    input.delete(0,END)
    list.insert(END, data)
 
# def delete_all():
#     with open('blockchain/blocks.json', 'r') as data_file:
#         data = json.load(data_file)

#     # for element in data:
#     #     del element.pop()

#     list.delete(0, END)
 
# def delete():
# 	list.delete(ANCHOR)

button = Button(ui, text="Créer", width = 10 , command = create)
button.pack()

# btn_delete_all = Button(text = "Supprimer tout", command = delete_all)
# btn_delete_all.pack()

# btn_delete = Button(text = "Supprimer par sélection", command = delete)
# btn_delete.pack()

list = Listbox(ui, width = 600)
list.pack()

ui.mainloop()


"""
API Flask
"""
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def get_all_blocks():
    return json.dumps(bchain.get_blocks(), sort_keys = True, default = str, indent = 2)

# @app.route('/add', methods=['POST'])
# def add_block():
#     data = request.form.get('data')
#     block = bchain.new_block(data)
#     bchain.add_block(block)
#     return json.dumps(bchain.get_blocks(), sort_keys = True, default = str, indent = 2)

app.run(debug = True, port = 4000)