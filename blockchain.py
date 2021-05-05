import datetime
import hashlib
import json
from flask import Flask, jsonify


# Building a Blockchain

class BlockChain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')  # Creates the Genesis Block

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash
                 }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

# Mining the Blockchain
