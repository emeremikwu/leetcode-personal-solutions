from typing import List

#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start


class Solution:
  def search(self, nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
      mid = low + (high - low) // 2

      if nums[mid] == target:
        return mid

      if nums[mid] < target:
        low = mid + 1

      else:
        high = mid - 1

    return -1


# @lc code=end
tests = [
    ([-1, 0, 3, 5, 9, 12], 13, -1),
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, -1),
    ([5], 5, 0),
]

if __name__ == "__main__":
  s = Solution()
  for nums, target, expected in tests:
    result = s.search(nums, target)
    assert result == expected, f"{nums}: {result} != {expected}"
