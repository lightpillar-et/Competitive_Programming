class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i , j = 0 , k 
        summ  = sum(nums[:k])
        avg = summ/ k
        
        while j < len(nums):
            summ = (summ + nums[j] ) - nums[i]
            cur_avg = summ / k 


            if cur_avg > avg :
                avg = cur_avg
            i+=1
            j +=1
        return avg
        