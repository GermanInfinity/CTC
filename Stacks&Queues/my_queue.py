"""
	my_queue.py: build a queue with two stacks
"""

# QUEUE: FIFO, 
# O(1), removal
# O(1), insertion
# operations: enqueue, dequeue, and peek
# enqueue: store stack and reverse of stack
	
class MyQueue: 
    def __init__(self): 
    	self.q1 = []
    	self.q2 = []

    def enqueue(self, value):
        if self.q1: 
            for i in range(len(self.q1)):
                self.q2.append(self.q1.pop())
            self.q1.append(value)
            for i in range(len(self.q2)):
                self.q1.append(self.q2.pop())  
        else: 
            self.q1.append(value)

    def dequeue(self): 
        self.q1.pop() if self.isEmpty() is False else "Empty queue"

    def peek(self): 
        return self.q1[-1]

    def isEmpty(self):
    	return True if len(self.q1) <= 0 else False

    def show(self): 
    	print (self.q1)


if __name__=="__main__": 
	q = MyQueue()
	for i in range(12):
	    q.enqueue(i)
	q.show()
	for i in range(30): 
		q.dequeue()
	q.show()
	# print (q.peek())
	# q.show()
	# print (q.peek())
	# q.show()