from typing import List
#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start


class Solution:
    # brute
    """ 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    """

    """
    # hashmap
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # numDifs = {i: abs(i-target) for i in nums}

        numDifs = {}

        for index, number in enumerate(nums):
            # get the required number to satisfy
            compliment = target - number

            # if number is in the dictionary
            if compliment in numDifs:
                return [numDifs[compliment], index]  # return

            # add to dict if not
            numDifs[number] = index
    """

    # sorted left right converging
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = sorted(list(enumerate(nums)), key=lambda x: x[1])

        current_sum = 0
        start_indx = 0
        end_indx = len(sortedNums) - 1

        # do whiles don't exist in python
        while True:
            current_sum = sortedNums[start_indx][1] + sortedNums[end_indx][1]

            if current_sum == target:
                break

            if current_sum > target:
                end_indx -= 1

            if current_sum < target:
                start_indx += 1

        result = [sortedNums[start_indx][0], sortedNums[end_indx][0]]

        return result


# @lc code=end
# test
nums = [
    [[0, 4, 3, 0], 0],
    [[-3, 4, 3, 90], 0],
    [[2, 7, 11, 15], 9],
    [[3, 2, 4], 6],
    [[3, 3], 6]
]

for n in nums:
    print(Solution().twoSum(n[0], n[1]))
