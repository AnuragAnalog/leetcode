class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = [[] for _ in range(n)]
        max_probs = [0] * n
        max_probs[start_node] = 1

        for edge, p in zip(edges, succProb):
            u, v = edge
            adj[u].append((v, p))
            adj[v].append((u, p))

        q = list()
        heapq.heappush(q, (-1, start_node))

        while q:
            prob, node = heapq.heappop(q)
            prob *= -1
            for n, p in adj[node]:

                if max_probs[n] < prob * p:
                    max_probs[n] = prob * p
                    heapq.heappush(q, (-prob * p, n))

        return max_probs[end_node]
