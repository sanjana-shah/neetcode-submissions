class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(list(s.lower()))
        t = sorted(list(t.lower()))
        return s == t