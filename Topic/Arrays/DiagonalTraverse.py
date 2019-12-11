"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in
diagonal order as shown in the below image.

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

"""


class Board:
    " nested non-public class board to maintain a 3x3 matrix "
    def __init__(self):
        self._board = [[' '] * 3 for j in range(3)]

    def __str__(self):
        rows = ['|'.join(self._board[j]) for j in range(3)]
        return '\n-----------\n'.join(rows)

    def mark(self, i, j, val):
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError('Invalid board position')
        if self._board[i][j] != ' ':
            raise ValueError('Board position already occupied')
        self._board[i][j] = val

if __name__ == "__main__":
    board = Board()
    board.mark(0, 0, ' 1 ')
    board.mark(0, 1, ' 2 ')
    board.mark(0, 2, ' 3 ')
    board.mark(1, 0, ' 4 ')
    board.mark(1, 1, ' 5 ')
    board.mark(1, 2, ' 6 ')
    board.mark(2, 0, ' 7 ')
    board.mark(2, 1, ' 8 ')
    board.mark(2, 2, ' 9 ')
    print(board)