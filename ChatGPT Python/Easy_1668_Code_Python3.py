
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        k = 1
        # repeat the word until it is no longer a substring of the sequence
        while word * k in sequence:
            count += 1
            k += 1
        return count
