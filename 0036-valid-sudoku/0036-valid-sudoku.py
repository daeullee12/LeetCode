class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(9):
            r = set()
            c = set()
            if i % 3 == 0:
                sub1 = set()
                sub2 = set()
                sub3 = set()
            for j in range(9):
                # row
                if board[i][j] != ".":

                    if board[i][j] in r:
                        return False
                    else: r.add(board[i][j])

                    if j // 3 == 0: 
                        if board[i][j] in sub1:
                            return False
                        else: sub1.add(board[i][j])
                    if j // 3 == 1:
                        if board[i][j] in sub2:
                            return False
                        else: sub2.add(board[i][j])  
                    if j // 3 == 2:
                        if board[i][j] in sub3:
                            return False
                        else: sub3.add(board[i][j])                
                # column
                if board[j][i] != '.':
                    if board[j][i] in c:
                        return False
                    else: c.add(board[j][i])

        return True
