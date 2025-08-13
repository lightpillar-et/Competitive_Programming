class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        zipped = list (zip(word1 , word2))
        res = ""
        for i in zipped :
            i = list (i)
            ans = "".join(i)
            res += ans
        longer = max (word1 , word2 , key = len )
        if longer == word1 :
            cut = len(word2)
            res += word1[cut:]
            return res 
        if longer == word2 :
            cut = len(word1)
            res += word2[cut:]
            return res
     




        
        