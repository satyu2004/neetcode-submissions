class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(set)
        visited = set()
        n_components = 0

        # prepare adjacency 'matrix'
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            # explore neighbors
            for nbr in adj[node]:
                dfs(nbr)


        for node in range(n):
            if node not in visited:
                dfs(node)
                n_components += 1
        
        return n_components