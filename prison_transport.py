import sys
from collections import deque
m = int(raw_input())
n = int(raw_input())

graph = {}
visited = {}
while n>0:
	lines = [int(x) for x in raw_input().split()]
	graph[lines[0]] = graph.get(lines[0],[]) + [lines[1]]
	graph[lines[1]] = graph.get(lines[1],[]) + [lines[0]]
	visited[lines[0]] = 0
	visited[lines[1]] = 0
	n -= 1

def highsqr(num):
	x = num**0.5
	if x%1 != 0:
		x += 1
		x = int(x/1)
	return x

def bfs(graph,node,visited,group):
	visited[node] = 1
	neighbors = deque([node])
	while len(neighbors) > 0:
		node = neighbors.popleft()
		for i in graph[node]:
			if visited[i] == 0:
				visited[i] = 1
				group[0] += 1	
				neighbors.append(i)

def dfs(graph,node,visited,group):
	visited[node] = 1
	lst = [node]
	while len(lst) > 0:
		last = lst.pop()
		for i in graph[last]:
			if visited[i] == 0:
				visited[i] = 1
				group[0] += 1
				lst.append(i)
		
		
val = 0
num_sofar = 0
for k,v in graph.items():
	if visited[k] == 0:
		group = [1]
		dfs(graph,k,visited,group)
		val += highsqr(group[0])
		num_sofar += group[0]

print val + (m - num_sofar)
