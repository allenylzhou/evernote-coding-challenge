class MyCircularBuffer:
	def __init__(self, max_size):
		self.current_size = 0
		self.max_size = max_size
		self.data = [None] * max_size
		self.start_index = self.end_index = 0
	
	def add(self, item):
		# Add item
		self.data[self.end_index] = item
		if self.end_index == self.start_index and self.current_size > 0:
			self.start_index += 1
		self.end_index += 1
		
		# Handle overflow
		if self.start_index >= self.max_size:
			self.start_index = 0
		if self.end_index >= self.max_size:
			self.end_index = 0
		
		self.current_size += 1
	
	def remove(self, n):
		self.start_index = (self.start_index + n) % self.max_size
		self.current_size -= n

	def list(self):
		if self.end_index <= self.start_index:
			temp = self.data[self.start_index:] + self.data[0:self.end_index]
		else:
			temp = self.data[self.start_index:self.end_index]
		for item in temp:
			print item 

size = int(raw_input())
buffer = MyCircularBuffer(size)
while True:
	command = raw_input().split()
	if command[0] == 'A':
		items = int(command[1])
		for i in range(items):
			item = raw_input()
			buffer.add(item)
	elif command[0] == 'R':
		buffer.remove(int(command[1]))
	elif command[0] == 'L':
		buffer.list()
	elif command[0] == 'Q':
		break
