#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

  def __init__(self):
    self._stack = []
    self._min = []

  def push(self, val: int) -> None:
    self._stack.append(val)

    if not self._min or val <= self._min[-1]:
      self._min.append(val)

  def pop(self) -> None:
    if not self._stack:
      return None

    val = self._stack.pop()
    if self._min and val == self._min[-1]:
      self._min.pop()
    return val

  def top(self) -> int:
    return self._stack[-1]

  def getMin(self) -> int:
    if not self._min:
      return None

    return self._min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end


def test_1():
  stack = MinStack()
  stack.push(-2)
  stack.push(0)
  stack.push(-3)
  assert stack.getMin() == -3
  stack.pop()
  assert stack.top() == 0
  assert stack.getMin() == -2


def test_2():
  stack = MinStack()
  stack.push(0)
  stack.push(1)
  stack.push(0)
  assert stack.getMin() == 0
  stack.pop()
  assert stack.getMin() == 0


if __name__ == "__main__":
  test_1()
  test_2()
