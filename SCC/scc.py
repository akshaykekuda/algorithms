# Implementing the Karger min cut algorithm
# Graph is being implemented using python's inbuilt dictionary

import sys
import resource

class Graph(object):

	def __init__(self):
		self.graph_dic = {}
		self.graph_dic_rev = {}
		self.total_vertex = 0
		self.explored = [False]
		self.order =[]
		self.curr_label = None
		self.nodes_processed = 0
		self.curr_s = None
		self.leader = []
		self.finishing_time = {}

	def add_vertex(self, vertex):
		self.graph_dic[vertex] = [] #add vertex to graph
		self.graph_dic_rev[vertex] = [] #add vertex to reverse graph
		self.total_vertex +=1
		 

	def add_edge(self, src, destination):
		self.graph_dic[src].append(destination) #add directed adge from src to dest to graph
		self.graph_dic_rev[destination].append(src) #add directed edge from dest to src to reverse graph
		

	def print_graph(self):
		print(self.graph_dic)
		

	def delete_vertex(self, vertex):
		for v in self.graph_dic:
			self.delete_edge_list(v, vertex)
		return self.graph_dic.pop(vertex)

	def dfs(self, i):
		self.explored[i-1] = True
		self.leader[i-1] = self.curr_s #set the leader of the current vertex as curr_s
		for j in self.graph_dic[i]: #dfs call
			if self.explored[j-1] is False:
				self.dfs(j)


	def dfs_rev_g(self, i):
		self.explored[i-1] = True
		for j in self.graph_dic_rev[i]:
			if self.explored[j-1] is False:
				self.dfs_rev_g(j)		
		self.compute_finishing_time(i) #compute the finishing time of i as the no of nodes processed so far

	def compute_order(self, s):
		self.order[s-1] = self.curr_label
		self.curr_label -= 1

	def compute_finishing_time(self, i):
		self.nodes_processed +=1
		self.finishing_time[self.nodes_processed] = i

	def topological_sort(self):
		self.explored = self.explored * self.total_vertex
		self.order = [None] * self.total_vertex
		self.curr_label = self.total_vertex
		for v in self.graph_dic:
			if self.explored[v-1] is False:
				self.dfs(v)
		return self.order

	def dfs_loop(self, rev):
		self.explored = [False] * self.total_vertex
		if rev: #1st pass of DFS on reverse graph. This gives an order of vertices
			self.nodes_processed = 0
			self.finishing_time = {}
			for i in self.graph_dic_rev:
				if self.explored[i-1] is False:
					self.dfs_rev_g(i)
		else: #Second pass of DFS on original graph starting from vertex with highest finishing time
			self.curr_s = None
			self.leader = [None] * self.total_vertex
			for i in range(self.total_vertex, 0, -1): # #decreasing order of finishing time
				if self.explored[self.finishing_time[i] - 1] is False:
					self.curr_s = self.finishing_time[i]
					self.dfs(self.curr_s)


	def kosaraju(self):
		self.dfs_loop(rev = True)
		self.dfs_loop(rev = False)
		self.leader.sort(reverse = True)
		# print(self.leader)
		i=0
		count = 0
		scc_count = []
		prev = self.leader[0]
		while(i<len(self.leader)):
			curr = self.leader[i]
			if prev == curr:
				count += 1
			else:
				scc_count.append(count)
				count = 1
				prev = curr
			i += 1
		scc_count.append(count)
		scc_count.sort(reverse =True)
		return scc_count[0:5]




if __name__ == '__main__':
	g = Graph()
	resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
	sys.setrecursionlimit(0x100000)

	#Below converts a list of edges into a adjacency list
	with open("SCC.txt") as f:
		for num in f:
			if num == '\n':
				continue
			num = num.split()
			tail = int(num[0])
			head = int(num[1])
			
			if tail not in g.graph_dic:
				g.add_vertex(tail)
			if head not in g.graph_dic:
				g.add_vertex(head)

			g.add_edge(tail, head)
			
	# g.explored = g.explored * g.total_vertex
	print("Ordering of Vetices: {}".format(g.kosaraju()))






	







