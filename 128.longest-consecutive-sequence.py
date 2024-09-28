from typing import List
#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start


class Solution:
  # def longestConsecutive(self, nums: List[int]) -> int:
  #     if len(nums) == 0:
  #         return 0

  #     sortedNums = sorted(nums)
  #     absMax = 1
  #     localmax = 1
  #     for i in range(len(sortedNums)):
  #         if i == len(sortedNums)-1:
  #             if localmax > absMax:
  #                 absMax = localmax
  #             break

  #         if sortedNums[i+1] == sortedNums[i]+1:
  #             localmax += 1
  #         else:
  #             if localmax > absMax:
  #                 absMax = localmax
  #             localmax = 1

  #     return absMax

  def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
      return 0

    numSet = set(nums)
    max_count = 0

    for num in nums:
      # number is start of sequence
      if num - 1 not in numSet:

        # count until end of sequence
        count = 1
        current_num = num

        while current_num + 1 in numSet:
          count += 1
          current_num += 1

        # compare sequence to current max
        max_count = max(count, max_count)

    return max_count


# @lc code=end
test = [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ([1, 2, 0, 1], 3)
]

for t in test:
  print(Solution().longestConsecutive(t[0]), t[1])
