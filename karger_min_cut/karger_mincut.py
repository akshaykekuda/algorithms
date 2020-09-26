# Implementing the Karger min cut algorithm
# Graph is being implemented using python's inbuilt dictionary

import random
import copy
import math

class Graph(object):

	def __init__(self):
		self.graph_dic = {}
		self.total_vertex = 0

	def add_vertex(self, vertex):
		self.graph_dic[vertex] = []
		self.total_vertex +=1
		return 

	def add_edge(self, src, destination):
		vertex_neighbours = self.graph_dic.get(src)
		self.graph_dic[src].append(destination)
		return

	def print_graph(self):
		print(self.graph_dic)
		return

	def delete_vertex(self, vertex):
		for v in self.graph_dic:
			self.delete_edge_list(v, vertex)
		return self.graph_dic.pop(vertex)

	def merge_delete_vertex(self, src, dest):
		for v in self.graph_dic:
			self.merge_delete_edge_list(v, src, dest)
		return self.graph_dic.pop(dest)


	def merge_delete_edge_list(self, v, src, dest):
		arr = self.graph_dic[v]

		for i in range(len(arr)):
			if arr[i] == dest:
				arr[i] = src

		self.graph_dic[v] = arr
		return
	
	
	def merge_no_dupl(self,v,a,b):
		arr = []
		for i in range(len(a)):
			if a[i] != v:
				arr.append(a[i])
		for i in range(len(b)):
			if b[i] !=v:
				arr.append(b[i])

		return arr

	def contract(self, src, dest):
		dest_edge_list = self.merge_delete_vertex(src, dest)
		merge_edge = self.merge_no_dupl(src, self.graph_dic[src], dest_edge_list)
		self.total_vertex -=1
		self.graph_dic[src] = merge_edge
		return



	def min_cut(self, N):
		self.total_vertex = N
		min_cut_contraction = []
		while self.total_vertex >2:
			src = random.choice(list(self.graph_dic.keys()),)
			dst = random.choice(self.graph_dic[src])
			self.contract(src, dst)
		
		min_cut_vertex = list(self.graph_dic.keys())
		return len(self.graph_dic[min_cut_vertex[0]])





if __name__ == '__main__':
	g = Graph()
	with open("karger_mincut.txt") as f:
		for num in f:
			num = num.split()
			node = int(num[0])
			g.add_vertex(node)
			for x in num[1:]:
				g.add_edge(node, int(x))
	N = g.total_vertex
	minimum_cut = []
	for i in range(100):
		dup = copy.deepcopy(g)
		minimum_cut.append(dup.min_cut(N))
		print("min cut = {}".format(min(minimum_cut)))


	print("min cut = {}".format(min(minimum_cut)))





	







