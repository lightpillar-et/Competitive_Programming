class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(i.lower() for i in s if i.isalnum())
        left , right = 0 , len(s) -1
        return s == s[::-1]

        