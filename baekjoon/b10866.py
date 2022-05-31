import sys
from collections import deque

n = int(input())
num = deque()
for _ in range(n):
    com = list(sys.stdin.readline().split())

    if com[0] == 'push_front':
        num.appendleft(com[1])
    elif com[0] == 'push_back':
        num.append(com[1])
    elif com[0] == 'pop_front':
        if len(num) == 0:
            print("-1")
        else: print(num.popleft())
    elif com[0] == 'pop_back':
        if len(num) == 0:
            print("-1")
        else: print(num.pop())
    elif com[0] == 'size':
        print(len(num))
    elif com[0] == 'empty':
        if len(num) == 0:
            print("1")
        else: print("0")
    elif com[0] == 'front':
        if len(num) == 0:
            print("-1")
        else: print(num[0])
    elif com[0] == 'back':
        if len(num) == 0:
            print("-1")
        else: print(num[-1])

