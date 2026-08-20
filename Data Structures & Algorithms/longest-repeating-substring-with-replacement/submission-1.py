class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        answer = 0
        freq = dict()

        for right in range(len(s)):
            if s[right] not in freq:
                freq[s[right]] = 0

            freq[s[right]] += 1
            max_freq = max(freq.values())

            if (right - left + 1 - max_freq) > k:
                freq[s[left]] -= 1
                left += 1

            answer = right - left + 1

        return answer