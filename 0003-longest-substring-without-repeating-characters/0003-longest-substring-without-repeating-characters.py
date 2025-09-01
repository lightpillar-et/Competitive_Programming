class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = 0 
        for i in range (len(s)):
            seen = set()
            cur  = 0
            for j in range (i , len(s)) :
                if s[j] in seen :
                    break 
                else:
                    seen.add(s[j])
                    cur +=1 
            cnt = max (cnt , cur)
        return cnt
        