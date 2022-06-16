import collections
from typing import List

equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]


# a -- 2--> b        b -- 3--> c
#  <--1/2--           <--1/3--
# a -- ?--> c

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        i = 0
        for a, b in equations:
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))
            i = i + 1

        print(graph)

        def bfs(c, d):
            if c not in graph or d not in graph:
                return -1.0

            Q = [(1.0, c)]
            visited = []

            for value, node in Q:
                if node == d:
                    return value
                visited.append(node)
                for v, w in graph[node]:
                    if v not in visited:
                        Q.append((value * w, v))
            return -1.0

        return [bfs(c, d) for c, d in queries]


output = Solution().calcEquation(equations, values, queries)
print(output)
