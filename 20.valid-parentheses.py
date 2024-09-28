from collections import deque
#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start

charDict = {
    "(": ")",
    "{": "}",
    "[": "]"
}


class Solution:
  def isValid(self, s: str) -> bool:
    if not s:
      return True

    if len(s) % 2:
      return False

    if len(s) == 1:
      return False

    if s[0] not in charDict:
      return False

    stack = deque()

    for indx in range(len(s)):
      current_char = s[indx]

      if current_char in charDict:
        stack.append(charDict[current_char])
        continue

      if len(stack) and current_char == stack.pop():
        continue

      return False

    return not len(stack)


# @lc code=end

test = [
    ("()))", False),
    ("{[]}", True),
    ("()", True),
    ("(){}}{", False),
    ("){", False),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("[", False),
    ("]", False),
    ("{", False),
    ("{[", False),
    ("{[}", False),
    ("{[}]", False),
    ("{[()]}", True),
    ("{[(){}]}", True),
    ("{[(){}]", False),
    ("{[(){}]]", False),
]

for args, expected in test:
  result = Solution().isValid(args)
  assert result == expected, f"For {args}, expected {expected} but got {result}"
