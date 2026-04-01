class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        v = ("a" , "e" , "i" , "o" , "u" , "A" , "E" , "I", "O" , "U")
        left , right  = 0 , len(s) -1
        while left < right :
            if s[left] in v and s[right] in v :
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left +=1
                right -=1
            elif s[left] in v and s[right] not in v:
                right -=1
            elif s[right] in v and s[left] not in v :
                left +=1
            else:
                left += 1
                right -= 1
            
        return "".join(s)


        