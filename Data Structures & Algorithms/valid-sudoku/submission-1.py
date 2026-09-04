class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import Counter

        def is_valid_dict(key_dict):
            #func which tells if we have a valid dict/not
            #i.e return True if valid dict else False
            for key, value in key_dict.items():
                if key != '.':
                   if value > 1:
                      return False
                    #end if
                #end if
            #end for
            return True 

        for row in board:
            count_dict = Counter(row)
            if not is_valid_dict(count_dict):
              print('row_check_failed')
              return False

        for row_index, row in enumerate(board):
            l1 = []
            #col-check
            for col_index, col in enumerate(row):
                l1.append(board[col_index][row_index])
            #end for
            count_dict = Counter(l1)
            if not is_valid_dict(count_dict):
              print('col_check_failed')
              return False
        #end for

        #3*3 traversal
        l1= []
        l1.append([])
        l1.append([])
        l1.append([])
        #print(l1)
        l1_index = 0
        for row_index, row in enumerate(board):
            for col_index, col in enumerate(row):
                #print(f'row_index - {row_index}, col_index - {col_index}, l1_index - {l1_index}, board_elem - {board[row_index][col_index]}')
                l1[l1_index].append(board[row_index][col_index])
                #print(f'L1-State: {l1}')
                if (col_index + 1) % 3 == 0:
                  l1_index+=1
                  #print(f'Incrementing L1 - {l1_index}')
                #end if
            #end for
            l1_index = 0
            #print(f'Reseting L1 index- {l1_index}')
            #print(f'After reset to 0 {l1}')
            if (row_index +1) % 3 == 0:
              print(f'Reseting entire - l1 {l1}')
              for item in l1:
                count_dict = Counter(item)
                if not is_valid_dict(count_dict):
                  print('cell_check_failed')
                  return False
            #end if
              l1 = []
              l1.append([])
              l1.append([])
              l1.append([])
              l1_index = 0
        #end for
        return True