#include <iostream>
#include <string>
#include <cassert>
#include <vector>
#include <utility>
using namespace std;

/*
 * @lc app=leetcode id=125 lang=cpp
 *
 * [125] Valid Palindrome
 */

// @lc code=start
class Solution
{
public:
  bool isPalindrome(string s)
  {
    char *p1 = &s[0];
    char *p2 = &s[s.length() - 1];

    while (p1 < p2)
    {
      if (!isalnum(*p1))
      {
        p1++;
        continue;
      }

      if (!isalnum(*p2))
      {
        p2--;
        continue;
      }

      if (tolower(*p1) == tolower(*p2))
      {
        p1++;
        p2--;
        continue;
      }

      return false;
    }
    return true;
  }
};
// @lc code=end

int main()
{
  vector<pair<string, bool>> tests = {
    {"A man, a plan, a canal: Panama", true},
    {"race a car", false}
  };

  Solution s;

  for (auto test : tests)
  {
    bool expected = test.second;
    bool result = s.isPalindrome(test.first);
    assert(expected == result);
  }
}
