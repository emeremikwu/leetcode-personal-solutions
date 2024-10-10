from typing import List
#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start


class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1
    total = numbers[left] + numbers[right]

    while total != target:
      total = numbers[left] + numbers[right]
      if total > target:
        right -= 1
        continue

      if total < target:
        left += 1
        continue

    return [left + 1, right + 1]


# @lc code=end

if __name__ == "__main__":

  tests = [
      ([2, 7, 11, 15], 9, [1, 2]),
      ([2, 3, 4], 6, [1, 3]),
      ([-1, 0], -1, [1, 2])
  ]

  for test, target, expected in tests:
    results = Solution().twoSum(test, target)
    assert results == expected, f"{test}: expected {expected} but got {results}"
