# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelorder(root):
    q = [root]
    while q:
        t = q.pop(0)
        print(t.val, '', end='')
        if t.left is not None:
            q.append(t.left)
        if t.right is not None:
            q.append(t.right)


def creatBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index] is None:
            return
        pNode = TreeNode(data[index])
        pNode.left = creatBTree(data, 2 * index + 1)  # [1, 3, 7, 15, ...]
        pNode.right = creatBTree(data, 2 * index + 2)  # [2, 5, 12, 25, ...]
    return pNode


class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            # 부모 노드부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)
                levelorder(root)
                print()

        return root


# lst = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
lst = [4, 2, 7, 1, 3, 6, 9]
root = creatBTree(lst, 0)
levelorder(root)
print()

tree = Solution().invertTree(root)
# levelorder(tree)
