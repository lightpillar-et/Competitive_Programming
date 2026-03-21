class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for key , value in enumerate (nums) :
            if target - value in seen :
                return (key , seen[target - value])
            else:
                seen[value] = key 
        return False         