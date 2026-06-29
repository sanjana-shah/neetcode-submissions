class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force: for each word, generate frequency compare freq

        anagrams = defaultdict(list)
        for word in strs:
            lex_sort = "".join(sorted(word))
            anagrams[lex_sort].append(word)

        print(anagrams)
        ans = []
        for key in anagrams.keys():
            ans.append(anagrams[key])


        return ans