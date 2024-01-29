input = [   
[0,0,0, 2,6,0, 7,0,1],
[6,8,0, 0,7,0, 0,9,0],
[1,9,0, 0,0,4, 5,0,0],

[8,2,0, 1,0,0, 0,4,0],
[0,0,4, 6,0,2, 9,0,0],
[0,5,0, 0,0,3, 0,2,8],

[0,0,9, 3,0,0, 0,7,4],
[0,4,0, 0,5,0, 0,3,6],
[7,0,3, 0,1,8, 0,0,0]
]

output = [  
[4,3,5, 2,6,9, 7,8,1],
[6,8,2, 5,7,1, 4,9,3],
[1,9,7, 8,3,4, 5,6,2],

[8,2,6, 1,9,5, 3,4,7],
[3,7,4, 6,8,2, 9,1,5],
[9,5,1, 7,4,3, 6,2,8],

[5,1,9, 3,2,6, 8,7,4],
[2,4,8, 9,5,7, 1,3,6],
[7,6,3, 4,1,8, 2,5,9]
]



input1 = [   
[0,2,0, 0,0,0, 0,0,0],
[0,0,0, 6,0,0, 0,0,3],
[0,7,4, 0,8,0, 0,0,0],
  
[0,0,0, 0,0,3, 0,0,2],
[0,8,0, 0,4,0, 0,1,0],
[6,0,0, 5,0,0, 0,0,0],
  
[0,0,0, 0,1,0, 7,8,0],
[5,0,0, 0,0,9, 0,0,0],
[0,0,0, 0,0,0, 0,4,0]
]

output1 = [
[1,2,6, 4,3,7, 9,5,8],
[8,9,5, 6,2,1, 4,7,3],
[3,7,4, 9,8,5, 1,2,6],

[4,5,7, 1,9,3, 8,6,2],
[9,8,3, 2,4,6, 5,1,7],
[6,1,2, 5,7,8, 3,9,4],

[2,6,9, 3,1,4, 7,8,5],
[5,4,8, 7,6,9, 2,3,1],
[7,3,1, 8,5,2, 6,4,9]
]

import unittest
from sudokusolve import sudoku_solve

class TestSudokuSolver(unittest.TestCase):

    def test_sudoku_solver_normal(self):
        # Test case for solving a Sudoku
        sudoku_board = (
            (5, 3, 0, 0, 7, 0, 0, 0, 0),
            (6, 0, 0, 1, 9, 5, 0, 0, 0),
            (0, 9, 8, 0, 0, 0, 0, 6, 0),
            (8, 0, 0, 0, 6, 0, 0, 0, 3),
            (4, 0, 0, 8, 0, 3, 0, 0, 1),
            (7, 0, 0, 0, 2, 0, 0, 0, 6),
            (0, 6, 0, 0, 0, 0, 2, 8, 0),
            (0, 0, 0, 4, 1, 9, 0, 0, 5),
            (0, 0, 0, 0, 8, 0, 0, 7, 9)
        )
        expected_solution = (
            (5, 3, 4, 6, 7, 8, 9, 1, 2),
            (6, 7, 2, 1, 9, 5, 3, 4, 8),
            (1, 9, 8, 3, 4, 2, 5, 6, 7),
            (8, 5, 9, 7, 6, 1, 4, 2, 3),
            (4, 2, 6, 8, 5, 3, 7, 9, 1),
            (7, 1, 3, 9, 2, 4, 8, 5, 6),
            (9, 6, 1, 5, 3, 7, 2, 8, 4),
            (2, 8, 7, 4, 1, 9, 6, 3, 5),
            (3, 4, 5, 2, 8, 6, 1, 7, 9)
        )
        solved_board = sudoku_solve(sudoku_board)
        self.assertEqual(solved_board, expected_solution)



    def test_sudoku_solver_full_board(self):
        # Test case for a full board; the solver should return the same board
        sudoku_board = (
            (5, 3, 4, 6, 7, 8, 9, 1, 2),
            (6, 7, 2, 1, 9, 5, 3, 4, 8),
            (1, 9, 8, 3, 4, 2, 5, 6, 7),
            (8, 5, 9, 7, 6, 1, 4, 2, 3),
            (4, 2, 6, 8, 5, 3, 7, 9, 1),
            (7, 1, 3, 9, 2, 4, 8, 5, 6),
            (9, 6, 1, 5, 3, 7, 2, 8, 4),
            (2, 8, 7, 4, 1, 9, 6, 3, 5),
            (3, 4, 5, 2, 8, 6, 1, 7, 9)
        )
        solved_board = sudoku_solve(sudoku_board)
        self.assertEqual(solved_board, sudoku_board)


    def test_sudoku_solver_one_left(self):
        # Test case for solving a Sudoku with only one spot to fill
        sudoku_board = (
            (5, 3, 4, 6, 7, 8, 9, 1, 2),
            (6, 7, 2, 1, 9, 5, 3, 4, 8),
            (1, 9, 8, 3, 4, 2, 5, 6, 7),
            (8, 5, 9, 7, 6, 1, 4, 2, 3),
            (4, 2, 6, 8, 5, 3, 7, 9, 1),
            (7, 1, 3, 9, 2, 4, 8, 5, 6),
            (9, 6, 1, 5, 3, 7, 2, 8, 4),
            (2, 8, 7, 4, 1, 9, 6, 3, 5),
            (3, 4, 5, 2, 8, 6, 1, 7, 0)  # One spot to fill
        )
        expected_solution = (
            (5, 3, 4, 6, 7, 8, 9, 1, 2),
            (6, 7, 2, 1, 9, 5, 3, 4, 8),
            (1, 9, 8, 3, 4, 2, 5, 6, 7),
            (8, 5, 9, 7, 6, 1, 4, 2, 3),
            (4, 2, 6, 8, 5, 3, 7, 9, 1),
            (7, 1, 3, 9, 2, 4, 8, 5, 6),
            (9, 6, 1, 5, 3, 7, 2, 8, 4),
            (2, 8, 7, 4, 1, 9, 6, 3, 5),
            (3, 4, 5, 2, 8, 6, 1, 7, 9)
        )
        solved_board = sudoku_solve(sudoku_board)
        self.assertEqual(solved_board, expected_solution)

if __name__ == '__main__':
    unittest.main()

