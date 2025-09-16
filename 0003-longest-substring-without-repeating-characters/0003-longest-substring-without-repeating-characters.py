class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        right = 0
        res = 0

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                res = max(res, right - left + 1)
                right += 1
            else:
                seen.remove(s[left])
                left += 1

        return res
