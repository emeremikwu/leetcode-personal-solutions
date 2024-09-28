from typing import List, Dict

#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramDict: Dict[str, List[str]] = {}

        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString in anagramDict:
                anagramDict[sortedString].append(string)
            else:
                anagramDict[sortedString] = [string]

        return [i for (_, i) in anagramDict.items()]

#  @lc code=end


# Test cases


cases = [
    (["eat", "tea", "tan", "ate", "nat", "bat"],
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
    ([""], [[""]]),
    (["a"], [["a"]])
]

for case in cases:
    assert Solution().groupAnagrams(case[0]) == case[1]
