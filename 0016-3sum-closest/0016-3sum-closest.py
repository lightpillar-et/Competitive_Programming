class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort ()
        best_sum = 0
        best_distance = float("inf")

        for i in range (len(nums)):
            left , right = i+1 , len(nums)-1
            while left < right :
                cur_sum = nums[i] + nums[left] + nums[right]
                cur_distance = abs (cur_sum - target)
                if cur_distance < best_distance :
                    best_distance = cur_distance
                    best_sum = cur_sum
                if cur_sum > target :
                    right -=1
                else:
                    left +=1
        return best_sum
                
        