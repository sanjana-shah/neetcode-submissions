class Solution:

    def encode(self, strs: List[str]) -> str:

        words = []

        for word in strs:
            words.append(str(len(word)) + "#" + word)

        return "".join(words)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            separator = s.find("#", i)
            if separator != -1:
                length = int(s[i:separator])
                word = s[separator+1: separator+1 + length]
                res.append(word)
                i = separator + 1 + length
            else:
                break

        return res