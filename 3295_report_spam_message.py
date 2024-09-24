# Time Complexity: O(m+n)
# Auxiliary Space: O(n)
# m = # words in message, n = # words in bannedWords

class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        words = set(bannedWords)
        count = 0
        for word in message:
            if word in words:
                count += 1
                if count == 2:
                    return True

        return False
