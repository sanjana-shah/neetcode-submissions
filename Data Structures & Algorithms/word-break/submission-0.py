class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set()
        for word in wordDict:
            words.add(word)

        valid_word = dict()

        def checkWord(word):
            if word in valid_word:
                return valid_word[word]
            
            if len(word) == 0:
                return True

            res = False
            for i in range(len(word)+1):
                if word[0:i] in words:
                    res = res or checkWord(word[i:])

            valid_word[word] = res
            return res

        return checkWord(s)