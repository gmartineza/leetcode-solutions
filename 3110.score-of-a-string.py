class Solution:
    def scoreOfString(self, s: str) -> int:
        chars = list(s)
        print(chars)
        result = 0
        for i in range(1, len(chars)):
            result += abs(ord(chars[i]) - ord(chars[i-1]))
        return result
