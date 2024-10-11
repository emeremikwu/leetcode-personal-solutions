from typing import List
# TODO: sketch on paper, implement in c
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start


class Solution:
  def search(self, nums: List[int], target: int) -> int:
    left, mid, right, = 0, None, len(nums) - 1

    while left <= right:
      mid = left + (right - left) // 2
      if target == nums[mid]:
        return mid

      # left sorted half of list
      if nums[left] <= nums[mid]:
        if target > nums[mid] or target < nums[left]:
          left = mid + 1
        else:
          right = mid - 1

      # right sorted half of list
      else:
        if target < nums[mid] or target > nums[right]:
          right = mid - 1
        else:
          left = mid + 1
    return -1

# @lc code=end


tests = [
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    ([1], 0, -1),
]

if __name__ == "__main__":
  s = Solution()
  for test, target, expected in tests:
    result = s.search(test, target)
    assert result == expected, f"{test}: {result} != {expected}"
  print('All tests passed')
