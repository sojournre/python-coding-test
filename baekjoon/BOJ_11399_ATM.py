N = int(input())
P = list(map(int, input().split()))

P.sort()
cnt = 0
for i in range(1, len(P)):
    P[i] += P[i - 1]
print(sum(P))
