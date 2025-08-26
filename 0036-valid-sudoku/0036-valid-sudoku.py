class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        column = {}
        sqaures = {}

        for i in range(9):
            row[i] = set()
            for j in range(9):
                cur = board[i][j]
                if cur == '.':
                    continue
                if cur in row[i]:
                    return False
                row[i].add(cur)

        
        for i in range (9):
            column[i] = set ()
            for j in range (9):
                cur = board[j][i]
                if cur == ".":
                    continue 
                if cur in column[i]:
                    return False 
                column[i].add (cur)


        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur == '.':
                    continue
                key = (i // 3, j // 3)    
                if key not in sqaures:
                    sqaures[key] = set()
                if cur in sqaures[key]:    
                    return False
                sqaures[key].add(cur)

        return True
