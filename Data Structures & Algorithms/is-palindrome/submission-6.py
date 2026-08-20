class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            while i < len(s) and not s[i].isalpha() and not s[i].isdigit():
                i += 1

            while j >= 0 and not s[j].isalpha() and not s[j].isdigit():
                j -= 1

            if i >= len(s) and j < 0:
                break

            if i >= len(s) or j < 0:
                return False

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True

