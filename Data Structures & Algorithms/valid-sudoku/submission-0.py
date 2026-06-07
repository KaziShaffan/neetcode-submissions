class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        squares = collections.defaultdict(set)

        for i in range(len(board)):
            col = set()
            row = set()
            for k in range(len(board)):
                print(row)
                print(col)
                if((board[i][k] in row) or (board[k][i] in col) or board[k][i] in squares[(i // 3, k // 3)]):
                    return False
                
                if(board[i][k] != "."):
                    row.add(board[i][k])
                if(board[k][i] != "."):
                    col.add(board[k][i])
                if(board[k][i] != "."):
                    squares[(i // 3, k //3)].add(board[k][i])

                
        return True