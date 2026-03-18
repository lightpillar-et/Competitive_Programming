class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i in range (len(nums)):
            cur = nums[i]
            check = target - cur 
            if check in seen :
                return (i , seen[check])
            seen[cur] = i 
        return False 
        