class Solution:
    def topo_sort(self, node, adj, visited, order):
        visited[node] = 1

        for n in adj[node]:
            if visited[n] == 0:
                self.topo_sort(n, adj, visited, order)
                order.append(n)

    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        adj = [[] for _ in range(n)]
        answer = [0] * n

        for pair in richer:
            adj[pair[1]].append(pair[0])

        for i in range(n):
            visited = [0] * n
            order = [i]
            self.topo_sort(i, adj, visited, order)

            min_person = 10**10
            mini = 10**10
            for o in order:
                if quiet[o] < mini:
                    mini = quiet[o]
                    min_person = o
            answer[i] = min_person

        return answer
