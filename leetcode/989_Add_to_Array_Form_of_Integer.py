from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        carry = k
        ans = []

        while i >= 0 or carry > 0:
            if i >= 0:
                carry += num[i]
                i -= 1
            ans.append(carry % 10)
            carry //= 10

        return ans[::-1]
