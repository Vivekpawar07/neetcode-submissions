class Solution:
    def is_valid(self,board,row,col,value):
        if value == ".":
            return True
        for i in range(9):
            if board[row][i] == value  and col!=i:
                return False
        for j in range(9):
            if board[j][col] == value and row!=j:
                return False

        box_row = (row//3) * 3
        box_col = (col//3) * 3
        for r in range(box_row,box_row+3):
            for c in range(box_col,box_col+3):
                if(r!= row or c !=col) and board[r][c]==value:
                    return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        len_board = len(board)
        hashmap = []

        for row in range(len_board):
            for col in range(len_board):
                hashmap.append((row,col,board[row][col]))

        for row, col, value in hashmap:
            if not self.is_valid(board, row, col, value):

                return False
        return True



