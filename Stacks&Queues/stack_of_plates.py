"""
	stack_of_plates.py: mimcs stack of plate behaviour with capacity threshold
"""
import unittest
class SetOfStacks: 
	def __init__(self): 
		self.stack = [[]]
		self.threshold = 3

	def push(self, plate):
		if len(self.stack[-1]) >= self.threshold: 
			self.stack.append([plate])
		else: 
			self.stack[-1].append(plate)


	def pop(self):
		if self.stack[-1] == []: 
			self.stack.pop()

		pos = len(self.stack) - 1#self.num_of_plates // self.threshold
		if self.stack[pos]:
			self.stack[pos].pop(-1)

		else: 
			print ("No plate to remove")

		self.left_shift()

	def popAt(self, idx): 
		if idx < self.threshold * len(self.stack) and idx >= 0: 
			self.stack[idx // self.threshold].pop(-1)

		else: 
			print ("No plate there")
		self.left_shift()

	def left_shift(self): 
		for i in range(len(self.stack) - 1):
			if len(self.stack[i]) < self.threshold: 
				drop = self.stack[i+1][0]
				self.stack[i+1].pop(0)
				self.stack[i].append(drop)

	def show(self): 
		print (self.stack)


class Tests(unittest.TestCase):
    def test_stacks(self):
        stacks = SetOfStacks(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(35):
            lst.append(stacks.pop())
        self.assertEqual(lst, list(reversed(range(35))))

    def test_pop_at(self):
        stacks = SetOfStacks(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(31):
            lst.append(stacks.pop_at(0))
        self.assertEqual(lst, list(range(4, 35)))

    

if __name__=="__main__": 
	unittest.main()
	# dishes = SetOfStacks()
	# for plate in range(18): 
	# 	dishes.push(plate)

	# for plate in range(3): 
	# 	dishes.push(plate)

	# dishes.show() 

	# dishes.pop()
	# dishes.pop()
	# dishes.pop()
	# dishes.pop()
	# dishes.pop()
	# dishes.popAt(50)
	# dishes.popAt(0)


	# dishes.show()