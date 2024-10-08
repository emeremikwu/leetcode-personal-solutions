#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:

  def isPalindrome(self, s: str) -> bool:
    if not s:
      return True

    p1 = 0
    p2 = len(s) - 1

    while p1 <= p2:
      if not s[p1].isalnum():
        p1 += 1
        continue

      if not s[p2].isalnum():
        p2 -= 1
        continue

      if s[p1].lower() == s[p2].lower():
        p1 += 1
        p2 -= 1
        continue

      return False

    return True
# @lc code=end


if __name__ == "__main__":
  tests = [
      ("0P", False),
      ("aa", True),
      ("A man, a plan, a canal: Panama", True),
      ("race a car", False),
      (" ", True),
      ("", True),
      ("1", True),
  ]

  s = Solution()
  for test, expected in tests:
    result = s.isPalindrome(test)
    assert result == expected, f"{test}: expected {expected}, got {result}"
