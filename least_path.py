
from collections import deque

class Node():
	def __init__(self,edges=[]):
		self.edges = edges
	def prnt(self):
		for i in self.edges:
			i.prnt()

class Edge():
	def __init__(self,cost,vertex):
		self.cost = cost
		self.vertex = vertex
	def prnt(self):
		print self.cost
		print self.vertex

x1 = Node()
x2 = Node()
x3 = Node([Edge(2,x1),Edge(3,x2)])
x4 = Node()
x5 = Node()
x6 = Node([Edge(3,x4),Edge(3,x5)])
x7 = Node([Edge(4,x3),Edge(2,x6)])


#x3.prnt()


graph = {}
graph[1] = [2,3]
graph[2] = 4
graph[3] = [5,1]

#x = float('Inf')

def bfsgraph(node):
	que = deque([(node,0)])
	minsum = float('Inf')
	while len(que) > 0:
		fst = que.popleft()
		if len(fst[0].edges) == 0:
			if minsum > fst[1]:
				minsum = fst[1]
		else:
			for i in fst[0].edges:
				if i.cost+fst[1] < minsum:
					que.append((i.vertex,i.cost+fst[1]))
	return minsum

print bfsgraph(x1)


visited = {1:0,2:0,3:0,4:0,5:0}


def bfs(graph,node,visited):
	neighbors = deque([node])
	while len(neighbors) > 0:
		tmp = neighbors.popleft()
		print tmp
		if visited[tmp] == 0:
			visited[tmp] = 1
			if graph.has_key(tmp):
				if type(graph[tmp]) is not list:
					graph[tmp] = [graph[tmp]]
				for i in graph[tmp]:
					neighbors.append(i)


#bfs(graph,1,visited)
