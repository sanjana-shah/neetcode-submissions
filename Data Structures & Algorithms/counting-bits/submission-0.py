class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        offset = 1

        for i in range(1, len(ans)):
            if 2 * offset == i:
                ans[i] = 1
                offset = i

            else:
                ans[i] = 1 + ans[i-offset]


        return ans
            