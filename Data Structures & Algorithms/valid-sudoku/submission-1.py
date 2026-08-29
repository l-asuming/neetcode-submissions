def column_checker(board):
    for j in range(9):
        column = []    
        for i in range(9):
            if board[i][j] != '.':
                column.append(board[i][j])
        if len(column) != len(set(column)):
            return False
    return True

def row_checker(board):
    for i in range(9):
        row = [j for j in board[i] if j != '.']
        if len(row) != len(set(row)):
            return False
    return True

def box_checker(board):
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            box = []
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if board[i][j] != '.':
                        box.append(board[i][j])
            if len(box) != len(set(box)):
                return False
    return True

class Solution:
   def isValidSudoku(self, board: list[list[str]]) -> bool:
        return column_checker(board) and row_checker(board) and box_checker(board)