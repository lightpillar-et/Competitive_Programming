class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cnt = 0 
        p1  , p2 = 0 , 0 

        while p1 < len(g) and p2 < len(s):
            if g[p1] <= s[p2] :
                cnt +=1
                p1+=1
                p2+=1
            elif g[p1] > s[p2]:
                p2+=1
        return cnt 
            
        