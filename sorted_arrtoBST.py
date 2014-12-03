from collections import deque
class Node:
	def __init__(self,value):
		self.value = value;
		self.left = None;	
		self.right = None;

	def printTree(self):
		if self == None:
			return
		que = deque([self])
		while(len(que)>0):
			node = que.popleft()
			print node.value
			if node.left!=None:
				que.append(node.left)
			if node.right!=None:
				que.append(node.right)


def arr_to_bst(arr,left,right):
	if left>right:
		return None
	mid = (right+left)/2
	newNode = Node(arr[mid])
	newNode.left = arr_to_bst(arr,left,mid-1)
	newNode.right = arr_to_bst(arr,mid+1,right)
	return newNode

arr = [1,2,3,4,5,6]
root = arr_to_bst(arr,0,len(arr)-1)
root.printTree()

