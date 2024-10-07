from typing import List
#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start


class Solution:
  # not using a stack
  def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    pairs = sorted([(position[i], speed[i]) for i in range(len(position))], reverse=True)
    current_time = 0
    fleets = 0

    for position, speed in pairs:
      destination_time = (target - position)/speed

      if current_time < destination_time:
        current_time = destination_time
        fleets += 1

    return fleets

  # # using a stack
  # def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
  #   pairs = sorted([(position[i], speed[i]) for i in range(len(position))], reverse=True)
  #   stack = []

  #   for position, speed in pairs:
  #     destination_time = (target - position)/speed
  #     stack.append(destination_time)

  #     if len(stack) >= 2 and stack[-1] <= stack[-2]:
  #       stack.pop()

  #   return len(stack)

# @lc code=end


# Test

tests = [
    (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),
    (10, [3], [3], 1),
    (100, [0, 2, 4], [4, 2, 1], 1),
]

if __name__ == '__main__':
  s = Solution()
  for target, position, speed, expected in tests:
    result = s.carFleet(target, position, speed)
    assert expected == result, f'Expected: {expected}, Got: {result}'
  print('All tests passed')
