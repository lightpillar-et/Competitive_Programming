class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # summ = sum(nums[:k])
        # average  = summ / k 
        # start  = 0
        # for i in range (1  , len(nums)):
        #     summ -= nums[start]
        #     summ += nums[i]
        #     cur = summ / k
        #     average = max (average  , cur)
        #     i +=1
        # return average 
        window_sum = sum (nums[:k])
        res = window_sum / k
        
        start  =0
        for i in range ( k , len(nums)):
            window_sum -= nums[start]
            window_sum += nums[i]
            cur  = window_sum / k
            res = max (res ,cur )
            start +=1
        return res


          
        