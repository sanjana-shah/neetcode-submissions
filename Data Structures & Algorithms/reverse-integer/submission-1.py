class Solution:
    def reverse(self, x: int) -> int:
        mi, mx = -2**31, 2**31 - 1

        reverse = 0

        # -1234
        if x < 0:
            while x < 0:
                if reverse < (mi/10):
                    return 0

                reverse *= 10
                temp = (x * -1) % 10
                reverse -= temp
                x = int(x/10)

        else:
            while x > 0:
                if reverse > (mx/10):
                    return 0

                reverse *= 10
                reverse += (x % 10)
                x = x // 10

        return reverse


        