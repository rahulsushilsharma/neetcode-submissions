from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_s = defaultdict(set)
        row_s = defaultdict(set)
        box_s = defaultdict(set)

        for i in range(9):
            for j in range(9):
                box_k = (i//3, j//3)
                val = board[i][j]
                if val == '.':
                    continue

                if val in col_s[i] or val in row_s[j] or val in box_s[box_k]:
                    return False
                
                col_s[i].add(val)
                row_s[j].add(val)
                box_s[box_k].add(val)
        
        return True