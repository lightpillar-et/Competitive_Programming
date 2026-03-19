class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        # Step 1: Count frequency
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Step 2: Create buckets
        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])

        # Step 3: Fill buckets
        for num in count:
            frequency = count[num]
            bucket[frequency].append(num)

        # Step 4: Collect top k elements
        result = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result