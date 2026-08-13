class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len (nums)):
            cur  = target - nums [i]
            if cur in seen :
                return i , seen[cur]
            else:
                seen[nums[i]] = i
        
        