import time


class BlockChain:
	""" a block chain implementaion in python
	used for learning purpose and translated from 
	javascript code of 
	"""

	def __init__(self):
		self.chain = []
		self.pending_transactions= []

	def create_block(self, nonce, previous_block_hash, current_block_hash):
		new_block = {
			'index': len(self.chain) + 1,
			'timestamp': time.now(),
			'transactions: self.pending_transactions',
			'nonce': nonce,
		 	'hash': current_block_hash,
			'previous_block_hash': previous_block_hash
		}

		self.pending_transactions = []
		self.chain.append(new_block);

	def get_last_block(self):
		return self.chain[-1]

	def create_transaction(self, amount, sender, recipient):
		new_transaction = {
			'amount': amount,
			'sender': sender,
			'recipient': recipient
		}
		this.pending_transactions.append(new_transaction);

	def hash_block(block_data):
		pass

	