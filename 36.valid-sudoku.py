from typing import List, Dict, Tuple
from math import ceil
#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # (section_x, section_y), [numbers in section..., ]
        section_boxes: Dict[Tuple[int, int], List[int]] = {
            (x+1, y+1): [] for x in range(3) for y in range(3)}
        section_rows: Dict[int, List[int]] = {x: [] for x in range(9)}
        section_cols: Dict[int, List[int]] = {y: [] for y in range(9)}

        for row in range(len(board)):
            for col in range(len(board[row])):
                value = board[row][col]
                coord = (ceil((row+1)/3), ceil((col+1)/3))

                if not value.isnumeric():
                    continue

                if value in section_rows[row]:
                    return False

                if value in section_cols[col]:
                    return False

                if value in section_boxes[coord]:
                    return False

                section_rows[row].append(value)
                section_cols[col].append(value)
                section_boxes[coord].append(value)

        return True


# @lc code=end
board = [
    [".", ".", "4", ".", ".", ".", "6", "3", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["5", ".", ".", ".", ".", ".", ".", "9", "."],
    [".", ".", ".", "5", "6", ".", ".", ".", "."],
    ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
    [".", ".", ".", "7", ".", ".", ".", ".", "."],
    [".", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]
]

print(Solution().isValidSudoku(board))
