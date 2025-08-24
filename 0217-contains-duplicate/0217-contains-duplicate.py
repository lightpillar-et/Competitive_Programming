class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapping = {}
        for i in nums :
            if i in mapping :
                return True 
            else:
                mapping [i] = None
        return False 
        