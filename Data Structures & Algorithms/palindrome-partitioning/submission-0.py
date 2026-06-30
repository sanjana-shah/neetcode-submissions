class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindrome = set()
        ans = []
        def isPalindrome(word: str) -> bool:
            if word in palindrome:
                return True

            if len(word) == 0 or len(word) == 1:
                palindrome.add(word)
                return True

            left, right = 0, len(word) - 1
            while left <= right:
                if word[left] != word[right]:
                    return False 
                left += 1
                right -= 1

            palindrome.add(word)
            return True

        def backtrack(palindrome_strings: List[str], word):
            if len(word) == 0:
                ans.append(list(palindrome_strings))
                return
            
            for i in range(len(word)):
                substring = word[0:i+1]
                if isPalindrome(substring):
                    palindrome_strings.append(substring)
                    backtrack(palindrome_strings, word[i+1:])
                    palindrome_strings.pop()

            return 


        backtrack([], s)
        return ans