class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans = [0] * 32
        overflow = [0] * 32

        for i in range(31, -1, -1):
            b1 = a & 1
            b2 = b & 1

            if b1 & b2 == 0:
                ans[i] = (b1 | b2) ^ overflow[i]
                overflow[i-1] = (b1 | b2) & overflow[i]

            else:
                ans[i] = overflow[i]

                overflow[i-1] = 1

            a = a >>  1
            b = b >>  1


        result = 0
        for i in ans:
            result = result << 1
            result = result | i

        if result >= (1 << 31):
            result -= (1 << 32)
        return result
                    