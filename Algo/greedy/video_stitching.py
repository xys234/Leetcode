"""

1024.
Medium


"""

from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        n = len(clips)
        clips = sorted(clips)
        # print(clips)
        pos, current, e, select = 0, 0, 0, []

        while current < T and pos < n:

            while e < T:
                while pos < n and clips[pos][0] <= current:
                    e = max(e, clips[pos][1])
                    pos += 1
                if e == current:
                    return - 1
                current = e
                select.append(clips[pos - 1])

        if current >= T:
            return len(select)
        else:
            return -1