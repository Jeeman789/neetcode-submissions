class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            row = set()
            for j in i:
                prev = len(row)
                row.add(j)
                if j != '.' and len(row) == prev:
                    return False
        for i in range(len(board)):
            column = set()
            for j in range(len(board)):
                prev = len(column)
                column.add(board[j][i])
                if board[j][i] != '.' and len(column) == prev:
                    return False
        for i in range(len(board)):
            box = set()
            for j in range(len(board)):
                prev = len(box)
                index = board[int(3 * int(i/3) + (j/3))][int((i%3) * 3 + j%3)]
                box.add(index)
                if index != '.' and len(box) == prev:
                    return False
        return True
        
