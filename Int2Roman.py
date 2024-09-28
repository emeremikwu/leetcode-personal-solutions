from math import floor as floor

class Solution:

    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: int) -> str:
        #convert to integer
        s = int(s)

        RomanToString = ""
        count = 0
        for rNumeral, rValue in reversed(self.romans.items()):
            if rValue <= s:
                count = floor(s / rValue)
                RomanToString += rNumeral * count
                s -= (rValue * count)
                continue

        return RomanToString


if __name__ == "__main__":
    print(Solution().romanToInt(4))
