class Solution:
    def isValidSudoku(self, board: list[list[str]]):
        # nums = ["1","2","3","4","5","6","7","8","9"]
        # hashmap = dict()
        # dashmap=dict()
        # hellmap= dict()
        # if (len(board) != 9):
        #     return False

        # for i in range(len(board)):
        #     for j in range(len(board[i])):
        #         if (len(board[i]) == 9):
        #             if board[i][j] in nums:
        #                 if board[i][j] in hashmap:
        #                     hashmap[board[i][j]] += 1
        #                 else:
        #                     hashmap[board[i][j]] = 1

        #             if (board[j][i] in nums):
        #                 if (board[j][i] in dashmap):
        #                     dashmap[board[j][i]] += 1
        #                 else:
        #                     dashmap[board[j][i]] = 1

        #             #box-checking!!
        #             num = board[i][j]
        #         if num != ".":
        #             box_key = (i // 3, j // 3)

        #             # Use .get() to create the set if it doesn't exist
        #             if box_key not in hellmap:
        #                 hellmap[box_key] = set()

        #             # Now, check for duplicates and add the number
        #             if num in hellmap[box_key]:
        #                 return False # Found a duplicate in the box
        #             hellmap[box_key].add(num)

                
                
        #         else:
        #             return False

                

        #     #Swallow the fucking keys!!
        #     keys = hashmap.keys()
        #     deys= dashmap.keys()
            

        #     #Looping starts in dictionaries
        #     for k in keys:
        #         if hashmap[k]>1:
        #             return False
                
        #     for d in deys:
        #         if dashmap[d]>1:
        #             return False
                
        #     #Looping ends in dictionaries sucker!!.
        #     #empty them.
        #     hashmap = {}
        #     dashmap={}
        
        # return True     
        
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                val = int(board[r][c]) - 1
                if (1 << val) & rows[r]:
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & squares[(r // 3) * 3 + (c // 3)]:
                    return False
                    
                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                squares[(r // 3) * 3 + (c // 3)] |= (1 << val)

        return True     

if __name__ == '__main__':
    sol = Solution()
    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    
    print(sol.isValidSudoku(board))