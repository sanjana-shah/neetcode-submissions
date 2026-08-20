class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map = {}
        s2_map = {}

        for char in s1:
            if char not in s1_map:
                s1_map[char] = 0

            s1_map[char] += 1

        left = 0
        for right in range(len(s2)):
            if s2[right] not in s2_map:
                s2_map[s2[right]] = 0
            s2_map[s2[right]] += 1

            if right - left + 1 == len(s1):
                temp = True

                for key in s1_map.keys():
                    if key not in s2_map or s1_map[key] != s2_map[key]:
                        temp = False

                if temp:
                    return True

                s2_map[s2[left]] -= 1
                left += 1

        return False

