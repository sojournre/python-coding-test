import collections
from typing import List

# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []

        def dfs(a):
            # 첫 번째 값을 읽어 어휘 순 방문
            route.append(a)
            while graph[a]:
                dfs(graph[a].pop(0))

        dfs('JFK')
        # 다시 뒤집어 어휘 순 결과로
        return route


itinerary = Solution().findItinerary(tickets)
print(itinerary)
