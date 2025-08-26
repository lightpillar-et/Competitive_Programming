from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur == '.':
                    continue

                key = (i // 3, j // 3)

                if cur in row[i]:
                    return False
                if cur in col[j]:
                    return False
                if cur in square[key]:
                    return False

                row[i].add(cur)
                col[j].add(cur)
                square[key].add(cur)

        return True
