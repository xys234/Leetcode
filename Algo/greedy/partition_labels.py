"""


"""

from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        positions = {}
        for i, ch in enumerate(S):
            if ch in positions:
                if i > positions[ch]:
                    positions[ch] = i
            else:
                positions[ch] = i

        partitions = []
        i = 0
        while i < len(S):
            pos = positions[S[i]]
            j = i + 1
            while j < pos:
                if positions[S[j]] > pos:
                    pos = positions[S[j]]
                j += 1
            partitions.append(pos)
            i = pos + 1

        partitions = [0] + [p + 1 for p in partitions]
        partitions = [p2 - p1 for p2, p1 in zip(partitions[1:], partitions[:-1])]
        return partitions


sol = Solution()
s = "qiejxqfnqceocmy"
print(sol.partitionLabels(s))