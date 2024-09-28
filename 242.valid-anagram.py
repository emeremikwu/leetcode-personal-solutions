from collections import Counter

#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start


class Solution:
    # sort method
    """ 
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return sorted(s) == sorted(t)
    """

    # Dictionary Method 1 (hashmap) (beats more than half of runtime )
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictS = dict()
        dictT = dict()

        for character in s:
            if character in dictS:
                dictS[character] += 1
            else:
                dictS[character] = 1

        for character in t:
            if character in dictT:
                dictT[character] += 1
            else:
                dictT[character] = 1

        for (charS, countS) in dictS.items():
            if not charS in dictT:
                return False
            if dictT[charS] != countS:
                return False

        return True

    # Dictionary Method 2 (beats most memory)
    """ 
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictS, dictT = {}, {}

        for i in range(len(s)):
            dictS[s[i]] = dictS.get(s[i], 0) + 1
            dictT[t[i]] = dictT.get(t[i], 0) + 1

        for (charS, countS) in dictS.items():
            if not charS in dictT:
                return False
            if dictT[charS] != countS:
                return False
        
        return True
     """


# @lc code=end
# test solution
teststr = [
    ["anagram", "nagaram", True],
    ["rat", "car", False],
    ["a", "ab", False],
]

for i in teststr:
    print(Solution().isAnagram(i[0], i[1]), i[2])
