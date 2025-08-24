class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        res = ""
        lst =  s.split (" ")
        lst.reverse()
        for i in lst :
            if i.isalnum():
                res += (i + " ")
        return res[:-1]
        