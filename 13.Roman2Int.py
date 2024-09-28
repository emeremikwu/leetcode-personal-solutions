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
    
    def romanToInt(self, s: str) -> int:
        toInt = 0
        
        for c in s:
            if c in self.romans:
                toInt += self.romans[c]
        return toInt
    
if __name__ == '__main__':
    print(Solution().romanToInt('MCMXCIV'))