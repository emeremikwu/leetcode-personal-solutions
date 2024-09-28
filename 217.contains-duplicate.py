from typing import List
#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start


class Solution:
    # sort
    """ def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True

        return False 
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            else:
                numSet.add(num)

        return False
# @lc code=end


# test solution
nums = [1, 2, 3, 1]
output = Solution().containsDuplicate(nums)

print(output)
