from typing import List
#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start


class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    # only add open parenthesis if open_count < n
    # only add close parenthesis if closed_count < open_count
    # backtrack when open_count == closed_count == n``
    stack = []
    result = []

    def backtrack(open_count: int, closed_count: int):
      if open_count == closed_count == n:
        result.append(''.join(stack))

      if open_count < n:
        stack.append('(')
        backtrack(open_count + 1, closed_count)
        stack.pop()

      if closed_count < open_count:
        stack.append(')')
        backtrack(open_count, closed_count + 1)
        stack.pop()

    backtrack(0, 0)
    return result

# @lc code=end


if __name__ == "__main__":
  solution = Solution()
  testlist = [
      (1, ["()"]),
      (2, ["(())", "()()"]),
      (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
  ]
  for n, expected in testlist:
    result = solution.generateParenthesis(n)
    print(result)
    assert result == expected
  print("All tests passed")
