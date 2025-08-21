class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split versions into their revisions
        p1 = version1.split(".")
        p2 = version2.split(".")

        # Loop until the longer one finishes
        n = max(len(p1), len(p2))

        for i in range(n):
            if i < len(p1):
                a = int(p1[i])
            else:
                a = 0

            if i < len(p2):
                b = int(p2[i])
            else:
                b = 0

            if a < b:
                return -1
            if a > b:
                return 1

        return 0
