# Given a list of integers S and a target number k,
# write a function that returns a subset of S that adds up to k. If such a subset cannot be made,
# then return null.

# Integers can appear more than once in the list.
# You may assume all numbers in the list are positive.

# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

# def find_sum_subset(arr,sumVal):
#     filter_ele = []
#     for val in arr:
#         if val < sumVal:
#             filter_ele.append(val)
#         elif val == sumVal:
#             return [val]
#     filter_ele = sorted




# print(find_sum_subset([12, 1, 61, 5, 9, 2],24))


# Class to make a Node 
class Node: 
	#Constructor which assign argument to nade's value 
	def __init__(self, value): 
		self.value = value 
		self.next = None
	
	# This method returns the string representation of the object. 
	def __str__(self): 
		return "Node({})".format(self.value) 
	
	# __repr__ is same as __str__ 
	__repr__ = __str__ 
	

class Stack: 
	# Stack Constructor initialise top of stack and counter. 
	def __init__(self): 
		self.top = None
		self.count = 0
		self.maximum = None
		
	#This method returns the string representation of the object (stack). 
	def __str__(self): 
		temp=self.top 
		out=[] 
		while temp: 
			out.append(str(temp.value)) 
			temp=temp.next
		out='\n'.join(out) 
		return ('Top {} \n\nStack :\n{}'.format(self.top,out)) 
		
	# __repr__ is same as __str__ 
	__repr__=__str__ 
	
	#This method is used to get minimum element of stack 
	def getMax(self): 
		if self.top is None: 
			return "Stack is empty"
		else: 
			print("Maximum Element in the stack is: {}" .format(self.maximum)) 



	# Method to check if Stack is Empty or not 
	def isEmpty(self): 
		# If top equals to None then stack is empty 
		if self.top == None: 
			return True
		else: 
		# If top not equal to None then stack is empty 
			return False

	# This method returns length of stack	 
	def __len__(self): 
		self.count = 0
		tempNode = self.top 
		while tempNode: 
			tempNode = tempNode.next
			self.count+=1
		return self.count 

	# This method returns top of stack	 
	def peek(self): 
		if self.top is None: 
			print ("Stack is empty") 
		else:	 
			if self.top.value > self.maximum: 
				print("Top Most Element is: {}" .format(self.maximum)) 
			else: 
				print("Top Most Element is: {}" .format(self.top.value)) 

	#This method is used to add node to stack 
	def push(self,value): 
		if self.top is None: 
			self.top = Node(value) 
			self.maximum = value 
			
		elif value > self.maximum : 
			temp = (2 * value) - self.maximum 
			new_node = Node(temp) 
			new_node.next = self.top 
			self.top = new_node 
			self.maximum = value 
		else: 
			new_node = Node(value) 
			new_node.next = self.top 
			self.top = new_node 
		print("Number Inserted: {}" .format(value)) 
	
	#This method is used to pop top of stack 
	def pop(self): 
		if self.top is None: 
			print( "Stack is empty") 
		else: 
			removedNode = self.top.value 
			self.top = self.top.next
			if removedNode > self.maximum: 
				print ("Top Most Element Removed :{} " .format(self.maximum)) 
				self.maximum = ( ( 2 * self.maximum ) - removedNode ) 
			else: 
				print ("Top Most Element Removed : {}" .format(removedNode)) 

				
			
	
# Driver program to test above class 
stack = Stack() 

stack.push(5) 
stack.push(3)
stack.getMax() 
stack.push(19) 
stack.push(7) 
stack.getMax()	 
stack.pop() 
stack.getMax() 
stack.pop() 
stack.getMax() 

# This code is contributed by Blinkii 

