class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping  = dict(Counter (nums))
        mapping = sorted (mapping.keys() , key = lambda x : mapping[x] , reverse = True )
        print (mapping)
        return mapping [:k]
        
      


        