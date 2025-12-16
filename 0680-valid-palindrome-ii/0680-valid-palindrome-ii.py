class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        check1 , check2 = True , True 

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                l1, r1 = left + 1, right
                while l1 < r1:
                    if s[l1] != s[r1]:
                        check1 = False
                        break
                    l1 += 1
                    r1 -= 1

                l2, r2 = left, right - 1
                while l2 < r2:
                    if s[l2] != s[r2]:
                        check2 = False
                        break
                    l2 += 1
                    r2 -= 1

                return check1 or check2

        return True
