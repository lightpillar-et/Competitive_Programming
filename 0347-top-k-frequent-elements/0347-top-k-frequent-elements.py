class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq  = Counter (nums)
        freq = sorted (freq.items()  , key = lambda x : x[1] , reverse=False )
        last = len (freq) -1 
        while k :
            res.append(freq[last][0])
            last -=1
            k-=1
        return res

      


        