class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        cnt = 0 
        for i in range (len(nums)) :
            left = i
            right = i+1
            while right <= len(nums)-1 :
                if nums[left]  + nums [right]  < target :
                    cnt +=1 
              
                right +=1
        return cnt 

        