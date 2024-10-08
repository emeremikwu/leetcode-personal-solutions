from typing import List, Tuple
#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start


class Solution:
  # Monotonic Decreasing Stack
  def largestRectangleArea(self, heights: List[int]) -> int:
    max_area = 0
    stack: List[Tuple[int, int]] = []  # index, height

    # iterate through heights
    for index, height in enumerate(heights):
      start_index = index
      while stack and stack[-1][1] > height:
        # pop stack
        top_index, top_height = stack.pop()

        # compute max area
        max_area = max(max_area, top_height * (index - top_index))
        start_index = top_index

      stack.append((start_index, height))

    # compute remaining areas
    for index, height in stack:
      max_area = max(max_area, height * (len(heights) - index))

    return max_area


# @lc code=end


tests = [
    ([2, 1, 5, 6, 2, 3], 10),
    ([0, 9], 9),
    ([2, 4], 4),
]


if __name__ == "__main__":
  s = Solution()
  for heights, expected in tests:
    result = s.largestRectangleArea(heights)
    assert expected == result, f"{expected} != {result}"
