# Kosaraju's two pass algorithm to find the Strongly Connected Components of a graph

Kosaraju's algorithm uses DFS to find the SCCs of a graph G.

## Pseudocode

```
DFS_LOOP(g):
	1. Maintain a reverse graph g_rev
	2. Mark all nodes as unexplored
	3. nodes processed = 0, finishing time[node] = {}
	4. for i in g_rev:
			if i is not explored:
				dfs_g_rev(i)
	5. Mark all nodes as unexplored
	6. curr_s = None
	7. for i = [N, N-1, N-2,......1]:
			if finishing_time[i] is not explored:
				curr_s = finishing_time[i]
				dfs(i)

dfs(i):
	mark i as explored
	leader[i] = curr_s
	for j = [all heads in edges outgoing from i]:
		if j is not explored:
			dfs(j)

dfs_rev_g(i):
	mark i as explored
	for j = [all heads in edges outgoing from i]:
		if j is not explored:
			dfs_rev_g(j)
	nodes_processed ++
	finishing_time[nodes_processed] = i						
```
Running time: O(m+n)
