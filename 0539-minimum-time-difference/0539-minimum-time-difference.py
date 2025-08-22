from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for tp in timePoints:
            h = int(tp[:2])
            m = int(tp[3:])
            minutes.append(h * 60 + m)

        minutes.sort()

        ans = 1440
        for i in range(len(minutes)-1):
            ans = min(ans, minutes[i+1] - minutes[i])

        ans = min(ans, minutes[0] + 1440 - minutes[-1])
        return ans
