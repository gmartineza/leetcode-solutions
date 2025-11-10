class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringed = str(x)
        flipped = ""
        for char in stringed:
            print(flipped)
            flipped = char + flipped
            print(flipped)
        return stringed == flipped
