class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float ("inf")

        for i in range(len(nums) ):
            left, right = i + 1, len(nums) - 1
         

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == target:
                    return target
                if abs(target - s) < abs(target - result):
                    result = s

               
                elif s < target:
                    left += 1
                else:
                    right -= 1

        return result