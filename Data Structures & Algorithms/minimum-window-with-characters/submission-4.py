class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        tmap = {}
        for char in t:
            if char not in tmap:
                tmap[char] = 0
            tmap[char] += 1

        left = 0
        smap = {}
        ans = ""
        for right in range(len(s)):
            if s[right] not in smap:
                smap[s[right]] = 0
            smap[s[right]] += 1

            if right - left + 1 >= len(t):
                while left < right and (s[left] not in tmap or smap[s[left]] > tmap[s[left]]):
                    smap[s[left]] -= 1
                    left += 1

                for key in tmap:
                    if key not in smap or smap[key] < tmap[key]:
                        break

                else:
                    if ans == "" or right - left + 1 < len(ans):
                        ans = s[left:right + 1]

        return ans
            
            