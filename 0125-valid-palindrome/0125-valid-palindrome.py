class Solution:
    def isPalindrome(self, s: str) -> bool:
#converting all uppercase letters into lowercase letters andremoving all non-alphanumeric characters,
        words= ""
        for char in s :
            if char.isalnum():
                words += char.lower()
        left , right = 0 , len(words) -1
        
        while left < right :
            if words[left] != words[right]:
                return False 
            else:
                left +=1
                right -=1
        return True

        
        