class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs.sort(key = len)
        short = strs[0]
        strs.remove (short)

        for i in range (len(short)):
            for j in range (len(strs)):
                if short[i] != strs[j][i]:
                    return ans 
            else:
                ans+= short[i]
        return ans 

