class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float ("inf")

        for i in range(len(nums) ):
            left, right = i + 1, len(nums) - 1
         

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return target
                if abs(target - total) < abs(target - result):
                    result = total

               
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return result