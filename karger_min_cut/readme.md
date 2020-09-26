Goal :Given an undirected and unweighted graph, find the smallest cut (smallest number of edges that disconnects the graph into two components).

Pseudo Code:

1)  Initialize contracted graph CG as copy of original graph
2)  While there are more than 2 vertices.
      a) Pick a random edge (u, v) in the contracted graph.
      b) Merge (or contract) u and v into a single vertex (update 
         the contracted graph).
      c) Remove self-loops
3) Return cut represented by two vertices.
4) Run the above implementation a large number of times to get minimum of all min cuts

