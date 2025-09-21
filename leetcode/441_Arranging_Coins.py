class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            k = (l + r) // 2
            need = k * (k + 1) // 2
            if need == n:
                return k
            if need < n:
                l = k + 1
            else:
                r = k - 1
        return r
