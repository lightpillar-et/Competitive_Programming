class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        res = []
        ans = 0
        skill.sort ()
        
        left , right  = 0 , len (skill) -1
        while left < right  :
            
            res .append  ([skill[left] , skill [right]])
            left +=1
            right -=1
        print (res)
        s = sum (res [0])
        print (s)
        for i in range (len (res) ) :
            if sum (res[i]) == s :
                ans +=  res[i][0] * res [i][1]
                print (ans)
            else :
                return -1 
        return ans 
        # for i in range(len(res)):
        #     if sum(res[i]) != s:
        #         return -1
        #     ans += res[i][0] * res[i][1]
        
        # return ans
        
            


        
        