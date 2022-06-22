# 1. 입력을 받는다.
# 2. 입력이 완료된 키 값으로 BST 를 만든다.
# 3. BST 를 후위 순회 (왼쪽-오른쪽-루트) 하면서 값을 출력한다.
import sys

sys.setrecursionlimit(10 ** 6)

preorder = []

while True:
    try:
        preorder.append(int(input()))
    except:
        break


def postorder(start, end):
    if start > end:
        return
    root = preorder[start]
    idx = start + 1

    while idx <= end:
        if preorder[idx] > root:
            break
        idx += 1

    postorder(start + 1, idx - 1)  # 왼쪽 트리
    postorder(idx, end)  # 오른쪽 트리
    print(root)


postorder(0, len(preorder) - 1)
