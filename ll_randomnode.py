

class Node():
	def __init__(self,value,random=None,next=None):
		self.value = value
		self.random = random
		self.next = next

def copy(root):
	tmp = root
	while tmp != None:
		new = Node(tmp.value)
		new.next = tmp.next
		tmp.next = new
		tmp = new.next
	tmp = root
	while tmp != None:
		tmp.next.random = tmp.random.next
		tmp = tmp.next.next
	tmp = root
	newroot = root.next
	while tmp.next != None:
		nxt = tmp.next
		tmp.next = tmp.next.next
		tmp = nxt
	return newroot


def printlist(root):
	tmp = root
	while tmp != None:
		try:
			print tmp.value,tmp.next.value,tmp.random.value
		except AttributeError:
			print None,tmp.random.value
		tmp = tmp.next

x5 = Node(5)
x4 = Node(4,None,x5)
x3 = Node(3,x5,x4)
x2 = Node(2,None,x3)
x1 = Node(1,x4,x2)
x2.random = x2
x4.random = x3
x5.random = x1
printlist(x1)
y1 = copy(x1)
printlist(y1)
