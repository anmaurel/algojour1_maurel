from hashlib import sha256
from datetime import datetime
from tkinter import *
# from flask import Flask
# from flask_cors import CORS, cross_origin
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