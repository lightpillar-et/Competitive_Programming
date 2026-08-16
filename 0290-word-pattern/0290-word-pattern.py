class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern) :
            return False 
        p_mapping = {}
        s_mapping = {}

        for i in range (len(pattern)):
            if pattern[i] in p_mapping :
                if p_mapping[pattern[i]] != s [i] :
                    return False 
            if s[i] in s_mapping :
                if s_mapping[s[i]] != pattern[i]:
                    return False 
            p_mapping[pattern[i]] = s[i]
            s_mapping[s[i]] = pattern[i]
        return True 


        