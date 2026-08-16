class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        s_mapping = {}
        t_mapping = {}

        for i in range (len(s)):
            if s[i] in s_mapping and s_mapping[s[i]] != t[i]:
                return False 
            if t[i] in t_mapping and t_mapping[t[i]] != s[i]:
                return False 
            s_mapping[s[i]] = t[i]
            t_mapping[t[i]] = s[i]
        return True 
        

       
