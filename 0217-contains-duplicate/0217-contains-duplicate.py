class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapping = dict (Counter (nums))
        for key , item in mapping.items() :
            if item >1 :
                return True 
        return False 
        