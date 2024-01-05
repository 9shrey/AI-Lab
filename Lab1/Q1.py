class Stack:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []
	def enqueue(self, item):
		self.stack1.append(item)
	def dequeue(self):
		if not self.stack2:
			while(self.stack1):
				element = self.stack1.pop()
				self.stack2.append(element)
			return self.stack2.pop()
		else:
			return self.stack2.pop()

def main():
	queue = Stack()
	queue.enqueue(1)
	queue.enqueue(2)
	queue.enqueue(3)
	queue.enqueue(4)
	print(queue.dequeue())
	queue.enqueue(5)
	print(queue.dequeue())

if __name__ == "__main__":
	main()


	


