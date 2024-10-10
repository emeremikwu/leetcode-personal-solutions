from typing import List, Tuple
#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start


class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    visited = set()
    combinations: List[List[int]] = []

    for fixed_index, fixed_num in enumerate(nums):
      if fixed_num in visited:
        continue

      visited.add(fixed_num)
      left_index = fixed_index + 1
      right_index = len(nums) - 1
      total = 0

      while left_index < right_index:
        total = sum([fixed_num, nums[left_index], nums[right_index]])

        # if total = 0
        if not total:
          combinations.append([fixed_num, nums[left_index], nums[right_index]])
          left_index += 1
          while left_index < right_index and nums[left_index] == nums[left_index - 1]:
            left_index += 1
          continue

        if total < 0:
          left_index += 1
        elif total > 0:
          right_index -= 1

    return combinations
# @lc code=end


tests = [
    ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 0, 1], []),
    ([0, 0, 0, 0], [[0, 0, 0]]),
]

if __name__ == "__main__":
  for test, expected in tests:
    result = Solution().threeSum(test)
    check_true = all([x in expected for x in result])
    assert check_true, f"{test}: {result} != {expected}"
