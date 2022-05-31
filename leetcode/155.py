class Node:
    def __init__(self, item, min, next):
        self.item = item
        self.min = min
        self.next = next


class MinStack:
    # linked list 를 이용한 풀이
    def __init__(self):
        self.last = None

    def push(self, val: int) -> None:
        if self.last is None:
            self.last = Node(val, val, self.last)
        else:
            self.last = Node(val, min(val, self.last.min), self.last)

    def pop(self) -> None:
        self.last = self.last.next

    def top(self) -> int:
        return self.last.item

    def getMin(self) -> int:
        return self.last.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()