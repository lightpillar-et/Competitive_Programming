class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float ("inf")
        prfoite = 0
        
        for i in prices :
            if i < min_price :
                min_price = i
            else:
                prfoite = max (prfoite ,  i - min_price)
        return prfoite
        