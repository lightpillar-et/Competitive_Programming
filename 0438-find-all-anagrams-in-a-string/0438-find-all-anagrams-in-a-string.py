class Solution:
    def findAnagrams(self, s: str, p: str):
        res = []
        k = len(p)
        sorted_p = sorted(p)   

        for i in range(len(s) - k + 1):   
            window = s[i:i+k]
            if sorted(window) == sorted_p:
                res.append(i)

        return res
