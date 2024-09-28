from typing import List, Dict
#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start


class Solution:
    # brutish but faster then pre|postfix
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0

        # Calculate product of all non-zero numbers and count zeros
        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_count += 1

        # If more than one zero, all elements will be zero
        if zero_count > 1:
            return [0] * len(nums)

        # Build the result array
        result = []
        for num in nums:
            if zero_count == 0:
                result.append(product // num)
            elif num == 0:
                result.append(product)
            else:
                result.append(0)

        return result
    """

    # pre|post-fix method
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result: List[int] = [1 for _ in range(len(nums))]

        # for i in range(len(nums)):
        #     if i != 0:
        #         result[i] *= result[i-1]

        # preix
        fix = 1
        for indx in range(len(result)):
            result[indx] = fix
            fix *= nums[indx]

        # postfix
        fix = 1
        # for (indx, num) in reversed(list(enumerate(result))): # slower
        for indx in range(len(nums) - 1, -1, -1):
            result[indx] *= fix
            fix *= nums[indx]

        return result


# @lc code=end
inputs = [
    [0, 0],  # [0, 0]
    [1, 2, 3, 4],  # [24,12,8,6]
    [-1, 1, 0, -3, 3],  # [0,0,9,0,0]
    [1, 0],  # [0,1]
    [0, 1]  # [1,0]
]

for i in inputs:
    print(Solution().productExceptSelf(i))
