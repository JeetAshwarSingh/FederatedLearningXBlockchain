import  hashlib 
from time import time
import json
import numpy as np

class Blockchain:

    def __init__(self, difficulty=4):
        self.chain = []
        self.difficulty = difficulty
        genesis_block = self.create_block("This is the genesis block", "0")
        self.chain.append(genesis_block)

    def create_block(self, data, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'data': data,
            'previous_hash': previous_hash,
            'nonce': 0,
            'hash': None
        }
        block['hash'] = self.mine_block(block)
        return block
    
    def compute_hash(self, block):
        block_copy = block.copy()
        block_copy['hash'] = None
        block_string = json.dumps(block_copy, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, block):
        while True:
            hash_value = self.compute_hash(block)
            if hash_value.startswith('0' * self.difficulty):
                return hash_value
            else:
                block['nonce'] += 1

    def add_block(self, data):
        previous_hash = self.chain[-1]['hash']
        new_block = self.create_block(data, previous_hash)
        self.chain.append(new_block)

    def print_chain(self):
        print("\n Blockchain ")
        for block in self.chain:
            print(f"\nBlock {block['index']}")
            print(f"Timestamp: {block['timestamp']}")
            print(f"Data: {block['data']}")
            print(f"Previous Hash: {block['previous_hash']}")
            print(f"Nonce: {block['nonce']}")
            print(f"Hash: {block['hash']}")
    
    def get_last_block(self):
            return self.chain[-1]


class hospital_data :
    def __init__(self,hospital_name = None,hospital_id = None,hospital_weight = None):
        self.hospital_name = hospital_name
        self.hospital_id = hospital_id
        self.hospital_weight = hospital_weight
    def get_hospital_weight(self):
        return self.hospital_weight
    
class FederatedModelData:
    def __init__(self, list1=None):
        if list1 is None or len(list1) == 0:
            raise ValueError("list1 must be a non-empty list of dictionaries containing numpy arrays")
        avg_dict = {}
        for key in list1[0].keys():
            arrays = [d[key] for d in list1]
            avg_dict[key] = np.mean(arrays, axis=0)
        self.avg_dict = avg_dict
    def get_avg(self):
        return self.avg_dict