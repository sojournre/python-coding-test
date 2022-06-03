import collections

N = int(input())
books = []

for _ in range(N):
    books.append(str(input()))

books.sort()

best = collections.Counter(books).most_common(1)[0][0]

print(best)

