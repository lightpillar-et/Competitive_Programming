class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalnum()]
        left , right = 0 , len(s) -1
        return s == s[::-1]

        