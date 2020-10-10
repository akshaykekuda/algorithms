class Graph(object):

	def __init__(self):
		self.graph_dic = {}
		self.total_vertex = 0

	def add_vertex(self, vertex):
		self.graph_dic[vertex] = [] #add vertex to graph
		self.total_vertex +=1
		 

	def add_edge(self, src, destination):
		self.graph_dic[src].append(destination) #add directed adge from src to dest to graph		

	def print_graph(self):
		print(self.graph_dic)

	def dijkstra(self, src, vertex_list):
		A = [0] * self.total_vertex #initialize all shortest dis to zero
		X =[src]
		while(len(X) < self.total_vertex): 
			first = True
			for v in X: #for all a belonging to X
				for w in self.graph_dic[v]:
					if w[0] in X: #discard w already in X
						continue
					if first: #assign min as the first tuple of v
						min_vertex = w[0]
						min_vertex_score = A[v-1] + w[1]
						first = False

					if A[v-1] + w[1] < min_vertex_score: #update minimum to w
						min_vertex = w[0]
						min_vertex_score = A[v-1] + w[1]
			
			X.append(min_vertex)
			A[min_vertex-1] = min_vertex_score

		output_len = []
		for v in vertex_list:
			if A[v-1] == 0:
				output_len.append(1000000)
			else:
				output_len.append(A[v-1])


		print("shortest path: {}".format(output_len))

			

if __name__ == '__main__':
	g = Graph()
	# destination_vertices = [1,2,3,4,5,6,7,8]
	destination_vertices = [7,37,59,82,99,115,133,165,188,197] #destination vertices for shortest path

	#Below stores the adjacency list as a dicrionary
	with open("dijkstraData.txt") as f:
		for num in f:
			if num == '\n':
				continue
			num = num.split()
			src = int(num[0])
			g.add_vertex(src)
			for x in num[1:]:
				dst = tuple(x.split(','))
				dst = (int(dst[0]), int(dst[1]))
				g.add_edge(src, dst)
	g.dijkstra(1, destination_vertices)
			