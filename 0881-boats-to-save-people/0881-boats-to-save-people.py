class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()  
        left = 0
        right = len(people) -1
        boat = 0

        while left <= right:
            
            
            if left < right and people[left] + people[right] <= limit:
                boat += 1
                left += 1
                right -= 1
            
            else:
                boat += 1
                right -= 1
        
        return boat