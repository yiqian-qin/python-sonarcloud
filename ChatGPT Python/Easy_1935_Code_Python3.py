
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # Split the text into individual words and make a set of broken letters
        words = text.split()
        broken_set = set(brokenLetters)
        # Keep track of the number of valid words
        valid_words = 0
        # Loop through each word in the text
        for word in words:
            # Check if the set of broken letters is disjoint from the set of letters in the word
            if broken_set.isdisjoint(set(word)):
                # If there are no broken letters in the word, increment the counter
                valid_words += 1
        # Return the total number of valid words
        return valid_words
