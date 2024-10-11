from typing import List, Tuple, Dict

# TODO: sketch on paper, implement in c
# https://leetcode.com/problems/time-based-key-value-store/solutions/5862281/beats-91-26-java-modified-binary-search-explanation-with-pics/
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start


class TimeMap:

  def __init__(self):
    # Key [[value, timestamp], ...]
    self._store: Dict[str, List[Tuple[str, int]]] = {}

  def set(self, key: str, value: str, timestamp: int) -> None:
    if key not in self._store:
      self._store[key] = []

    self._store[key].append((value, timestamp))

  def get(self, key: str, timestamp: int) -> str:
    res = ""
    list_ref = self._store.get(key, [])

    left, mid, right = 0, None, len(list_ref) - 1

    while left <= right:
      mid = left + (right - left) // 2

      if list_ref[mid][1] <= timestamp:
        res = list_ref[mid][0]
        left = mid + 1
      else:
        right = mid - 1
    return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
tests = [
    (["TimeMap", "set", "get", "get", "set", "get", "get"], [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3],
     ["foo", "bar2", 4], ["foo", 4], ["foo", 5]], [None, None, "bar", "bar", None, "bar2", "bar2"]),
    (["TimeMap", "set", "set", "get", "get", "get", "get", "get"], [[], ["love", "high", 10], ["love", "low", 20], ["love", 5],
     ["love", 10], ["love", 15], ["love", 20], ["love", 25]], [None, None, None, "", "high", "high", "low", "low"]),
]

if __name__ == "__main__":
  for operations, values, expected in tests:
    obj = None
    for i, operation in enumerate(operations):
      if operation == "TimeMap":
        obj = TimeMap()
      elif operation == "set":
        obj.set(*values[i])
      elif operation == "get":
        result = obj.get(*values[i])
        assert result == expected[i], f"{values[i]}: {result} != {expected[i]}"
    print('All tests passed')
