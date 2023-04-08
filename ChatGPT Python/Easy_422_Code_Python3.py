
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        num_rows = len(words)
        num_cols = max(len(word) for word in words)
        
        for i in range(num_rows):
            for j in range(len(words[i])):
                # check if the corresponding column exists with the same length
                if j >= num_rows:
                    return False
                # check if the character matches
                if i < len(words[j]) and words[i][j] == words[j][i]:
                    continue
                else:
                    return False
        return True
