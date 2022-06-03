class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        for i in stones:
            for j in jewels:
                if stones[i] == jewels[j]:
                    count = count + 1
        return count
