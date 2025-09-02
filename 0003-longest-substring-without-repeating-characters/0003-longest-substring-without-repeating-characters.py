class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s :
            return 0
        seen = set ()
        res = float ("-inf")
        cnt = 1
        left = 0 
        right = left +1
        while left  < right and right < len(s):
            seen.add (s[left])
            if s[right] not in seen :
                cnt +=1 
                seen.add(s[right])
                right +=1
            else:
                res = max (cnt , res)
                left +=1 
                right = left +1
                cnt =1 
                seen.clear()
        return res
