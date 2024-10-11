from typing import List
# TODO: implement in cpp
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start


class Solution:
  def findMin(self, nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    mid = None
    lowest: int = float("inf")

    while left <= right:
      if nums[left] < nums[right]:
        lowest = min(lowest, nums[left])
        break

      mid = left + (right - left) // 2
      lowest = min(nums[mid], lowest)

      # if true, then we're in the left half of the list
      if nums[mid] >= nums[left]:
        left = mid + 1
      else:
        right = mid - 1

    return lowest

# @lc code=end


if __name__ == "__main__":
  tests = [
      ([4, 5, 1, 2, 3], 1),
      ([11, 13, 15, 17], 11),
      ([3, 1, 2], 1),
      ([3, 4, 5, 1, 2], 1),
      ([4, 5, 6, 7, 0, 1, 2], 0),
      # ([2, 1], 1),
      # ([1], 1),
      # ([1, 2], 1),
      # ([2, 1, 3], 1),
      # ([2, 3, 1], 1),
      # ([1, 2, 3], 1),
      # ([3, 1, 2, 3], 1),
      # ([3, 3, 1, 3], 1),
  ]

  s = Solution()
  for test, lowest in tests:
    result = s.findMin(test)
    assert result == lowest, f"{test}: {lowest} != {result}"
  print("All tests passed.")
