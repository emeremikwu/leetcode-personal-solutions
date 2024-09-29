from typing import List
#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start

valid = set(['+', '-', '*', '/'])


class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    if len(tokens) == 1:
      return int(tokens[0])

    tokenStack = []
    for token in tokens:
      if token not in valid:
        tokenStack.append(token)
        continue

      var2 = int(tokenStack.pop())
      var1 = int(tokenStack.pop())

      if token == '+':
        tokenStack.append(var1 + var2)
      elif token == '-':
        tokenStack.append(var1 - var2)
      elif token == '*':
        tokenStack.append(var1 * var2)
      elif token == '/':
        tokenStack.append(int(var1 / var2))

    return tokenStack[0]

# @lc code=end

# test code


if __name__ == "__main__":
  solution = Solution()
  testlist = [
      (["18"], 18),
      (["4", "13", "5", "/", "+"], 6),
      (["2", "1", "+", "3", "*"], 9),
      (["4", "13", "5", "/", "+"], 6),
      (["10", "6", "9", "3", "/", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
      (["4", "3", "-"], 1),
      (["4", "3", "+"], 7),
      (["4", "3", "*"], 12),
      (["4", "3", "/"], 1),
      (["4", "3", "+", "5", "2", "-", "*"], 21),
      (["4", "3", "+", "5", "2", "+", "*"], 49),
      (["4", "3", "+", "5", "2", "*", "+"], 15),
      (["4", "3", "+", "5", "2", "+"], 14),
      (["4", "3", "+", "5", "2", "-"], 0),
      (["4", "3", "+", "5", "2", "/"], 1),
      (["4", "3", "+", "5", "2", "*"], 26),
  ]
  for tokens, result in testlist:
    result = solution.evalRPN(tokens)
    assert result == result
    print(f'{tokens} = {result}')
  print('All tests passed')
