class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        non_divisibles_sum = 0
        divisibles_sum = 0

        for i in range(1, n+1):
            if i % m != 0:
                non_divisibles_sum += i
            else:
                divisibles_sum += i
        return non_divisibles_sum - divisibles_sum
