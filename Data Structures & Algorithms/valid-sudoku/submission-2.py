
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box=defaultdict(set)
        rows=defaultdict(set)
        cols=defaultdict(set)
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if (num == "."):
                   continue

                if (num in box[(i // 3, j // 3)]) or (num in rows[i]) or (num in cols[j]):
                    return False
                box[(i // 3, j // 3)].add(num)
                rows[i].add(num)
                cols[j].add(num)


        return True

