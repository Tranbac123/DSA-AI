class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 1, int(c**0.5)
        while l <= r:
            curr = l * l + r * r
            if curr == c:
                return True
            elif curr < c:
                l += 1
            else:
                r -= 1
        return False