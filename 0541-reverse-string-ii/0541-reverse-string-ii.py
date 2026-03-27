class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""

        for i in range(0, len(s), 2 * k):
            chunk = s[i:i + 2 * k]

            first_part = chunk[:k]
            second_part = chunk[k:]

            result += first_part[::-1] + second_part

        return result