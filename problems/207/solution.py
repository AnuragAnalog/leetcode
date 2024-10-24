class Solution:
    def __init__(self):
        self.topo_q = list()

    def create_adj_list(self, adj_list, links):
        for link in links:
            if link[0] not in adj_list:
                adj_list[link[0]] = list()
            adj_list[link[0]].append(link[1])

        return adj_list

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not len(prerequisites):
            return True

        if numCourses == 1:
            return False

        adj_list = dict()
        adj_list = self.create_adj_list(adj_list, prerequisites)

        # Create an in-degree array
        in_deg = [0] * numCourses
        for i in range(numCourses):
            for n in adj_list.get(i, []):
                in_deg[n] += 1

        topo_count = 0
        for i in range(numCourses):
            if in_deg[i] == 0:
                topo_count += 1
                self.topo_q.append(i)
                in_deg[i] = -1

        while self.topo_q:
            node = self.topo_q.pop(0)
            for n in adj_list.get(node, []):
                in_deg[n] -= 1
                if in_deg[n] == 0:
                    self.topo_q.append(n)
                    in_deg[n] = -1
            topo_count += 1

        for ind in in_deg:
            if ind not in [0, -1]:
                return False

        return True
