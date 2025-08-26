class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0

        s = set(nums)          
        res = 0
        
        for num in s:
            
            if num - 1 not in s:
                cnt = 0
                
                while num + cnt  in s:
                    cnt += 1
                res = max(cnt, res)
                

        return res
