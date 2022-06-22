import collections
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)  # 이거 안넣으면 런타임 에러 (RecursionError) 발생

tree = collections.defaultdict(list)

n = int(input())
# 양방향 그래프인 트리 구성
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    tree[u].append((v, w))
    tree[v].append((u, w))

# 거리 저장
dist = collections.defaultdict(int)
dist[1] = 0


def dfs(start, weight):
    for i in tree[start]:
        v, w = i
        if v not in dist:
            dist[v] = weight + w
            dfs(v, weight + w)


# 루트 노드 1에서 부터 가장 먼 거리에 있는 노드를 찾기 위해 각 노드까지의 dist 를 구한다.
dfs(1, 0)

# max_value = max(dist.values())
# print(max_value)

# dist 에서 value 값이 최대인 key 를 반환한다.
# max_key 가 루트 노드 1 에서 가장 거리가 먼 노드 값이 된다.
max_key = max(dist, key=dist.get)
# print(max_key)

# dist 초기화
dist = collections.defaultdict(int)
dist[max_key] = 0
dfs(max_key, 0)

print(max(dist.values()))
