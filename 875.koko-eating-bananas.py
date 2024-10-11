from typing import List
import itertools
import math
# TODO: implement in c++
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start


class Solution:
  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    # we don't need a list of all possible values, just calculate the mid values
    left = 1
    right = max(piles)
    lowest = right

    while left <= right:
      # normally we would do left + (right - left) // 2 but we don't have to worry about overflow
      k = (left + right) // 2
      accumulated_hours = sum([math.ceil(pile/k) for pile in piles])

      # imaginary binary search
      if accumulated_hours <= h:
        lowest = min(lowest, k)
        right = k - 1
      else:
        left = k + 1

    return lowest

# @lc code=end


tests = [
    [[3, 6, 7, 11], 8, 4],
    [[30, 11, 23, 4, 20], 5, 30],
    [[30, 11, 23, 4, 20], 6, 23]
]

if __name__ == '__main__':
  for [piles, h, expected] in tests:
    result = Solution().minEatingSpeed(piles, h)
    assert Solution().minEatingSpeed(piles, h) == expected, f'{piles} - h:{h}| {result} != {expected}'
