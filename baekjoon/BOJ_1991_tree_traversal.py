# 어떻게 입력을 트리 구조로 만들 수 있을까?

import sys

sys.setrecursionlimit(10 ** 6)

tree = {}

N = int(input())
for i in range(N):
    n, l, r = map(str, input().split())
    tree[n] = [l, r]


def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])


preorder('A')
