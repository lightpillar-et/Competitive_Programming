class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        res = 0 
        skill.sort ()
        left , right  = 0 , len(skill) -1
        check  = skill [0] + skill[-1]
        while left < right :
            s = skill[left] + skill[right]
            if s != check  :
                return -1
            else:
                res += skill[left] * skill [right]
            left +=1
            right -=1

        return res

        