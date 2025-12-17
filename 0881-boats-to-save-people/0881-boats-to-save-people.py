class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        l = 0
        r = len(people) - 1
        people.sort()
        while l <= r:
            # if l == r:
            #     boat += 1
            #     break
            if people[l] + people[r] > limit:
                boat += 1
                r -= 1
            else:
                boat += 1
                l += 1
                r -= 1
        return boat
