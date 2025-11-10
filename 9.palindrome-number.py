class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringed = str(x)
        flipped = ""
        for char in stringed:
            flipped = char + flipped
        return stringed == flipped
