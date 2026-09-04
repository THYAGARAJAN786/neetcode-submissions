class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Elegant solution
        #Code is minimal
        #Trick is to use the formula for squares: (row //3) * 3 + (col//3)
        row_set_list = [set() for i in range(9)]
        col_set_list  = [set() for i in range(9)]
        square_set_list = [set() for i in range(9)]
        for row, rows in enumerate(board):
            for col, elem in enumerate(rows):
                if board[row][col] == '.':
                    continue
                #end if
                square_index = (row //3) * 3 + (col//3)
                if elem in row_set_list[row] or\
                   elem in col_set_list[col] or \
                   elem in square_set_list[square_index]:\
                    return False
                row_set_list[row].add(board[row][col])
                col_set_list[col].add(board[row][col])
                square_set_list[square_index].add(board[row][col])
            #end for
        #end for
        return True