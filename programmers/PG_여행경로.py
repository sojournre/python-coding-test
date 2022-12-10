import collections


def solution(tickets):
    answer = []
    # dfs 풀이
    # graph = collections.defaultdict(list)
    # for a, b in sorted(tickets, reverse=True):
    #     graph[a].append(b)
    #
    # def dfs(a):
    #     while graph[a]:
    #         pop = graph[a].pop()
    #         dfs(pop)
    #     answer.append(a)
    #
    # dfs('ICN')

    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)
    stack = ["ICN"]
    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    return answer[::-1]


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
l = solution(tickets)
print(l)
