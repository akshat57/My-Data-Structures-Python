class Node:
	def __init__(self, value = None, next = None):
		self.value = value
		self.next = next
		self.len = 0
	
	def append_node(self, node):
		if self.next == None:
			self.next = node
			self.len += 1
		else:
			cursor = self.next
			while cursor.next != None:
				cursor = cursor.next
			
			cursor.next = node
			self.len += 1


	def append_value(self, value):
		if self.next == None:
			self.next = Node(value)
			self.len += 1
		else:
			cursor = self.next
			while cursor.next != None:
				cursor = cursor.next

			cursor.next = Node(value)
			self.len += 1


	def insert_node(self, node, n):
		if n > self.len :
			print('WARNING: Index larger than length of linked list. Element added to the end of the list')
			self.append_node(node)
		else:
			counter = 0
			cursor = self
			while counter < n:
				cursor = cursor.next
				counter += 1
			node.next = cursor.next
			cursor.next = node
			self.len += 1
			
	def insert_value(self, value, n):
		if n > self.len :
			print('WARNING: Index larger than length of linked list. Element added to the end of the list')
			self.append_value(value)
		else:
			counter = 0
			cursor = self
			while counter < n:
					cursor = cursor.next
					counter += 1
			new_node = Node(value)
			new_node.next = cursor.next
			cursor.next = new_node
			self.len += 1

	def delete_value(self, value):
		if self.len > 0:
			cursor = self
			while cursor.next.next != None and cursor.next.value != value:	
				cursor = cursor.next
			
			if cursor.next.value == value:
				if cursor.next.next == None:
					cursor.next = None
					self.len -= 1
				else:
					cursor.next = cursor.next.next

					self.len -= 1
		else:
			print('Linked List is empty.')

	def delete_position(self, n):
		if n > self.len - 1:
			print('WARNIN: INDEX LARGER THAN ANY POSITION')
			self.pop()
		else:
			if n == 0 and self.len == 1:
				self.next = None
				self.len -= 1
			else:
				cursor = self
				counter = 0
				while counter < n:
					cursor = cursor.next
					counter += 1

				if cursor.next.next == None:
					cursor.next = None
					self.len -= 1
				else:
					cursor.next = cursor.next.next
					self.len -= 1

	def pop(self):
		if self.len > 0:
			cursor = self
			while cursor.next.next != None:
				cursor = cursor.next

			cursor.next = None
			self.len -= 1
		else:
			print('Linked list is empty. Cannot Pop.')

	def show(self):
		values = []
		cursor = self
		while cursor.next != None:
			cursor = cursor.next
			values.append(cursor.value)

		print(values)

	def length(self):
		return self.len

