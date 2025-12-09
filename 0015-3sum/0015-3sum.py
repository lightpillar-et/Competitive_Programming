class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()   # using a set to avoid duplicates

        for i in range(len(nums)):
            target = -nums[i]
            seen = set()

            for j in range(i + 1, len(nums)):
                needed = target - nums[j]   # like inverse logic

                if needed in seen:
                    triplet = tuple(sorted([nums[i], nums[j], needed]))
                    res.add(triplet)
                seen.add(nums[j])

        return [list(t) for t in res]

        