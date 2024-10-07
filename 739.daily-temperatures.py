from typing import List
#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start


class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # monotonic decreasing stack
    stack = []
    result = [0] * len(temperatures)

    count = 0
    for current_temp_index, current_temp in enumerate(temperatures):
      # while stack is not empty and top of top of stack is greater then curernt temp
      while stack and current_temp > stack[-1][0]:
        popped_temp, popped_temp_index = stack.pop()
        result[popped_temp_index] = current_temp_index - popped_temp_index

      stack.append([current_temp, current_temp_index])

    return result
# @lc code=end


if __name__ == "__main__":
  solution = Solution()

  tests = [
      ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
      ([30, 40, 50, 60], [1, 1, 1, 0]),
      ([30, 60, 90], [1, 1, 0]),
  ]

  for temps, expected in tests:

    result = solution.dailyTemperatures(temps)
    assert result == expected
