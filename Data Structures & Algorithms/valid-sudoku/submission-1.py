class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        SubBox=[[ set() for i in range(3)] for i in range(3)]
        Row=[set() for i in range(9)]
        Col = [set() for i in range(9)]
        for i in range(3):
            for j in range(3):
                for x in range(3):
                    for y in range(3):
                        X=(3*i)+x
                        Y=(3*j)+y
                        StringNum=board[X][Y]
                        if(StringNum!="."):
                            num=int(StringNum)
                            if(num in SubBox[i][j])or(num in Row[X])or (num in Col[Y]) :
                                return False
                            SubBox[i][j].add(num)
                            Row[X].add(num)
                            Col[Y].add(num)

        return True

