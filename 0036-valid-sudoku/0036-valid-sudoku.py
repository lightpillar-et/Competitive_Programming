from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):

                value = board[r][c]

                # Empty cell
                if value == ".":
                    continue

                box = (r // 3, c // 3)

                # Check for duplicate
                if value in rows[r]:
                    return False

                if value in cols[c]:
                    return False

                if value in boxes[box]:
                    return False

                # Remember this value
                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)

        return True