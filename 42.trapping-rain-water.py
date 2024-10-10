from typing import List

# TODO: implement in c++
#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start


class Solution:
  def trap(self, height: List[int]) -> int:
    if not height:
      return 0

    left_index = 0
    right_index = len(height) - 1

    left_max = height[left_index]
    right_max = height[right_index]

    total_vol = 0
    # move the left and right pointers towards each other based on the maximum height on each side
    while left_index < right_index:

      # If the left height is less than the right height
      if left_max < right_max:
        left_index += 1  # Move the left pointer to the right
        left_max = max(left_max, height[left_index])  # Update the maximum height on the left
        total_vol += left_max - height[left_index]  # Calculate the trapped water at the current position

      # If the right height is less than the left height
      else:
        right_index -= 1
        right_max = max(right_max, height[right_index])
        total_vol += right_max - height[right_index]

    return total_vol
# @lc code=end


tests = [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([4, 2, 0, 3, 2, 5], 9),
]

if __name__ == "__main__":
  s = Solution()
  for test, expected in tests:
    result = s.trap(test)
    assert result == expected, f"{test}: {result} != {expected}"
