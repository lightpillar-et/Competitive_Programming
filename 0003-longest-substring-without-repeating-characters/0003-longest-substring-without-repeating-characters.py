class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        cnt = 0 
        left = 0 
        
        for right in range (len(s)):
            while s[right] in seen :
                seen.remove(s[left])
                left +=1
            seen.add  (s[right])
            cnt = max (cnt , len(seen))
          
        return cnt 
        