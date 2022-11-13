import itertools

a = []
for _ in range(9):
    a.append(int(input()))
a.sort()
# print(a)

b = list(itertools.combinations(a, 7))
# print(b)

for i in b:
    if sum(i) == 100:
        for j in i:
            print(j)
        break
