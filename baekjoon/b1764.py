import collections

N, M = map(int, input().split())
people = []
ans = []

for i in range(N + M):
    name = str(input())
    people.append(name)

freqs = collections.Counter(people)
# print('freqs', freqs)

for f in freqs:
    if freqs[f] == 2:
        ans.append(f)

ans.sort()

# print('ans', ans)

print(len(ans))
for name in ans:
    print(name)