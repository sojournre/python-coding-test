import itertools

n, m = map(int, input().split())
# npr = itertools.permutations(range(1, n + 1), m)
# for i in list(npr):
#     print(*i)
s = []
li = []


def dfs():
    if len(s) == m:
        print(*s)
        # print(' '.join(map(str, s)))
        return
    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()


dfs()
