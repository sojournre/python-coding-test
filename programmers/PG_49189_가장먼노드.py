# 1. 1번 노드에서 bfs 로 각 노드의 레벨을 구한다.
# 2. 가장 마지막 레벨에 있는 노드의 개수를 구한다.
def solution(n, edge):
    answer = 0
    
    def iterative_bfs(start_v):
        discovered = [start_v]
        queue = [start_v]
        while queue:
            v = queue.pop(0)
            for i in discovered:
                
    return answer
