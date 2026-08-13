class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = dict (Counter(nums))
        mapping  =  sorted (mapping.items() , 
                            key = lambda x : x [1],
                              reverse=True)
        res = []
        for i in range (k):
            res. append (mapping [i][0])
        return res

