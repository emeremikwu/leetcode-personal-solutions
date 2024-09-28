from collections import Counter
from typing import List, Dict
#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start


class Solution:
    # bucket sort
    """ def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        count: Dict[int, List[int]] = {}
        freq: List[List[int]] = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] = count.get(i, 0) + 1

        for (i, j) in count.items():
            freq[j].append(i)

        res = []
        for i in reversed(freq):
            if len(res) >= k:
                break
            res += i

        # for i in range(len(freq) - 1, 0, -1)

        return res[:k] """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pass

    # using counter
    """ def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numDict = Counter(nums)
        return [pair[0] for pair in numDict.most_common(k)] """


# @lc code=end
test = [
    ([-1, -1], 1, [-1]),
    ([1, 2], 1, [1]),
    ([3, 0, 1, 0], 1, [0]),
    ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
    ([4, 1, -1, 2, -1, 2, 3], 2, [-1, 2])
]


for (nums, k, expected) in test:
    result = Solution().topKFrequent(nums, k)
    print(result, expected)
