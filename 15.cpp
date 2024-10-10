#include <vector>
#include <algorithm>
#include <iostream>
#include <utility>
#include <cassert>
#include <unordered_set>

using namespace std;

/*
 * @lc app=leetcode id=15 lang=cpp
 *
 * [15] 3Sum
 */

// @lc code=start
class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        // Sort the input array to make it easier to avoid duplicates and use two pointers
        vector<int> sorted_nums = nums;
        sort(sorted_nums.begin(), sorted_nums.end());
        unordered_set<int> visited = {};
        vector<vector<int>> combinations = {};

        // Iterate through the sorted array, treating each number as the fixed number
        for (int fixed_index = 0; fixed_index < sorted_nums.size(); fixed_index++)
        {
            int fixed_num = sorted_nums[fixed_index];
            
            // Skip this number if we have already processed it
            if (visited.find(fixed_num) != visited.end())
                continue;
                
            visited.insert(fixed_num);
            
            // Use two pointers to find pairs that sum up to the negative of the fixed number
            auto left = sorted_nums.begin() + fixed_index + 1;
            auto right = sorted_nums.end() - 1;

            while (left < right)
            {
                int sum = fixed_num + *left + *right;
                
                // found a combination
                if (sum == 0)
                {
                    combinations.push_back({fixed_num, *left, *right});
                    
                    // Move the left pointer to the right, skipping duplicates
                    left++;
                    while (left < right && *left == *(left - 1))
                        left++;
                }
                // Move the pointers based on the sum
                else if (sum < 0) left++;
                else right--;
            }
        }
        
        return combinations;
    }
};
// @lc code=end

int main()
{
    vector<tuple<vector<int>, vector<vector<int>>>> tests = {
        {{-1, 0, 1, 2, -1, -4}, {{-1, -1, 2}, {-1, 0, 1}}},
        // {{-2, 0, 0, 2, 2}, {{-2, 0, 2}}},
        // {{0, 0, 1}, {}},
        // {{0, 0, 0, 0}, {{0, 0, 0}}},
    };

    Solution solution;
    for (auto &[test, expected] : tests)
    {
        vector<vector<int>> result = solution.threeSum(test);
        bool sub_test = all_of(result.begin(), result.end(), [&expected](vector<int> &combination)
                               { return find(expected.begin(), expected.end(), combination) != expected.end(); });

        assert(sub_test);
    }
}
