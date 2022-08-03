import collections
from sys import stdin


# 트라이의 노드
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 단어 삽입
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    # 단어 존재 여부 판별
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

    # 버튼 입력 횟수 세기
    def count_push(self, word: str) -> int:
        cnt = 0
        node = self.root
        for char in word:
            node = node.children[char]
            # 해당 노드의 자식이 둘 이상이거나 다른 단어의 끝이면 버튼 입력
            if len(node.children) > 1 or node.word:
                cnt += 1
        return cnt


input = stdin.readline
while 1:
    t = Trie()
    words = []
    try:
        N = int(input())
    except:
        break

    for _ in range(N):
        word = input().strip()  # strip 으로 안하면 줄바꿈 문자 '\n' 이 들어감
        # word = str(input())
        t.insert(word)
        words.append(word)

    result = 0
    for word in words:
        result += t.count_push(word)

    print("%.2f" % (result / N))
