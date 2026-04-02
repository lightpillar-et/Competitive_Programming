class Solution:
    def findLengthOfShortestSubarray(self, arr):
        n = len(arr)

        i = 0
        while i + 1 < n and arr[i] <= arr[i + 1]:
            i += 1

        if i == n-1 :
            return 0

        j = n - 1
        while j > 0 and arr[j - 1] <= arr[j]:
            j -= 1

        answer = min(n - i - 1, j)

        left = 0
        right = j

        while left <= i and right < n:
            if arr[left] <= arr[right]:
                answer = min(answer, right - left - 1)
                left += 1
            else:
                right += 1

        return answer