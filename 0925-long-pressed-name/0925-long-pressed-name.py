
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_counts = Counter(name)
        typed_counts = Counter(typed)

        for key, val in name_counts.items():
            if typed_counts[key] < val:   
                return False
        return True
