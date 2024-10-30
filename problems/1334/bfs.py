import heapq

class Solution:
    def dijkstra(self, n, adj, start_node):
        distance = [10**10] * n
        distance[start_node] = 0

        q = list()
        heapq.heappush(q, (0, start_node))

        while q:
            dist, node = heapq.heappop(q)

            for n, w in adj[node]:
                if distance[n] > dist + w:
                    distance[n] = dist + w
                    heapq.heappush(q, (dist + w, n))

        return distance

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[] for _ in range(n)]
        min_cities = 1000
        city_index = 0

        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        for sn in range(n):
            dist = self.dijkstra(n, adj, sn)
            c = len([x for x in dist if x <= distanceThreshold])
            if min_cities > c:
                min_cities = c
                city_index = sn
            elif min_cities == c:
                city_index = max(city_index, sn)

        return city_index
