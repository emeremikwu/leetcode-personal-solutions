#include <iostream>
#include <vector>
#include <cassert>
#include <utility>
#include <iterator>

using namespace std;

/*
 * @lc app=leetcode id=167 lang=cpp
 *
 * [167] Two Sum II - Input Array Is Sorted
 */

// @lc code=start
class Solution
{
public:
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        vector<int>::iterator left = numbers.begin();
        vector<int>::iterator right = numbers.end() - 1;

        while (left < right)
        {
            int total = *left + *right;
            if (total > target)
                right--;
            else if (total < target)
                left++;
            else
            {
                return {
                    static_cast<int>(distance(numbers.begin(), left) + 1), static_cast<int>(distance(numbers.begin(), right) + 1)
                };
            }
        }
        return {};
    }
};
// @lc code=end

int main()
{
    Solution s;
    vector<int> numbers = {2, 7, 11, 15};
    vector<tuple<vector<int>, int, vector<int>>> testCases = {
        {{2, 7, 11, 15}, 9, {1, 2}},
        {{2, 3, 4}, 6, {1, 3}},
        {{-1, 0}, -1, {1, 2}}
    };

    for (const auto &testCase : testCases)
    {
        vector<int> numbers = get<0>(testCase);
        int target = get<1>(testCase);
        vector<int> expected = get<2>(testCase);
        vector<int> result = s.twoSum(numbers, target);
        assert(result == expected);
    }
}
