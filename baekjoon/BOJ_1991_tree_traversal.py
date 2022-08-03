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


def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])


def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')
