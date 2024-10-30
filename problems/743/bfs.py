import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        distance = [10**10] * n
        distance[k - 1] = 0

        for u, v, w in times:
            adj[u - 1].append((v - 1, w))

        q = list()
        heapq.heappush(q, (0, k - 1))
        
        while q:
            dist, node = heapq.heappop(q)
            for n, w in adj[node]:
                if distance[n] > dist + w:
                    distance[n] = dist + w
                    heapq.heappush(q, (dist + w, n))
        
        if max(distance) == 10**10:
            return -1
        return max(distance)
