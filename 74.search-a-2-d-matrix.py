

from typing import List
# TODO: implement in cpp
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start


class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    bottom = 0
    top = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    mid_row = 0
    mid_col = 0

    while bottom <= top:
      mid_row = bottom + (top - bottom) // 2

      # Check if x is present at mid
      if matrix[mid_row][0] == target:
        return True

      if target > matrix[mid_row][0] and target <= matrix[mid_row][right]:
        break

      # If x is greater, ignore left half
      if matrix[mid_row][0] < target:
        bottom = mid_row + 1

      # If x is smaller, ignore right half
      else:
        top = mid_row - 1

    while left <= right:
      mid_col = left + (right - left) // 2

      if matrix[mid_row][mid_col] == target:
        return True

      if matrix[mid_row][mid_col] <= target:
        left = mid_col + 1

      else:
        right = mid_col - 1

    return False
# @lc code=end


tests = [
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 1, True),
]

if __name__ == "__main__":
  s = Solution()
  for matrix, target, expected in tests:
    result = s.searchMatrix(matrix, target)
    assert result == expected, f"{matrix}: {result} != {expected}"
