class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        current = 0
        left = 0
        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                current = right - left + 1
                longest = max(longest, current)

            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1

                seen.add(s[right])
                current = right - left + 1
                longest = max(longest, current)

        return longest
