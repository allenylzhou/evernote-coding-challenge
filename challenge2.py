# Term Frequency
class Term:
	def __init__(self, word, freq):
		self.word = word
		self.freq = freq
	
	def __lt__(self, other):
		if self.freq < other.freq:
			return True
		elif self.freq == other.freq:
			return self.word > other.word
		else:
			return False

	def __gt__(self, other):
		if self.freq > other.freq:
			return True
		elif self.freq == other.freq:
			return self.word < other.word
		else:
			return False
	
	def __repr(self):
		return self.word

	def __str__(self):
		return self.word

# Priority Queue
class MaxBinaryHeap:
	def __init__(self):
		self.data = []
		self.current_size = 0

	def insert(self, term):
		self.data.append(term)
		self.current_size += 1
		self.swapUp(self.current_size - 1)
	
	def delete(self):
		temp = self.data[0]
		if self.current_size > 1:
			self.data[0] = self.data.pop()
			self.current_size -= 1
			self.swapDown(0)
		else:
			self.data.pop()
			self.current_size = 0
		return temp

	def swapUp(self, current_pos):
		while self.current_size > 1:
			parent_pos = (current_pos - 1) / 2
			if self.data[current_pos] > self.data[parent_pos]:
				#swap
				temp = self.data[parent_pos]
				self.data[parent_pos] = self.data[current_pos]
				self.data[current_pos] = temp
			current_pos = parent_pos
			if current_pos == 0:
				break
	
	def swapDown(self, current_pos):
		while current_pos * 2 + 1 <= self.current_size - 1:
			left_child_pos = 2 * current_pos + 1
			if left_child_pos == self.current_size - 1:
				max_child_pos = left_child_pos
			else:
				right_child_pos = left_child_pos + 1 
				if self.data[left_child_pos] > self.data[right_child_pos]:
					max_child_pos = left_child_pos
				else:
					max_child_pos = right_child_pos
			# compare current with max child
			if self.data[max_child_pos] > self.data[current_pos]:
				temp = self.data[max_child_pos]
				self.data[max_child_pos] = self.data[current_pos]
				self.data[current_pos] = temp
				current_pos = max_child_pos
			else:
				break
			
	def list(self):
		print [term.word for term in self.data]

frequencies = {}
terms = int(raw_input())
for i in range(terms):
	term = raw_input()
	frequencies[term] = frequencies.get(term, 0) + 1


#Insert terms into heap
heap = MaxBinaryHeap()
for key, value in frequencies.iteritems():
	heap.insert(Term(key, value))

#Pop k terms into list
k = int(raw_input())
for i in range(k):
	term = heap.delete()
	print term
