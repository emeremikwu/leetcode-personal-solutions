from typing import List
import math
#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start


class Solution:
  def maxArea(self, height: List[int]) -> int:

    left = 0
    right = len(height) - 1
    max_area = 0

    while left <= right:
      box_width = right - left
      box_height = min(height[left], height[right])
      area = box_width * box_height
      max_area = max(max_area, area)

      if height[left] < height[right]:
        left += 1
      else:
        right -= 1

    return max_area
# @lc code=end


tests = [
    ([0, 2], 0),
    ([8, 7, 2, 1], 7),
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
]

if __name__ == "__main__":
  s = Solution()
  for test, expected in tests:
    result = s.maxArea(test)
    assert result == expected, f"{result} != {expected}"
