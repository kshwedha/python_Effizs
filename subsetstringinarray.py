# Given a list of words Words = ["baby", "cat", "dada", "dog"] and a random jumbled string like ctay, write a function find(words, word1) that returns the word if it can be formed from the characters of the given string.
#  - Example: 
#  - find(words, "ctay") → returns "cat"
#  - find(words, "dad") → returns "-" (not found)

def find(words, keyword):
    alpha_dict = {}
    for i in range(65, 91):
        alpha_dict[chr(i).lower()] = [0]*len(words)
    for index, word in enumerate(words):
        for char in word:
            alpha_dict[char.lower()][index] += 1
    
    wordIndex = findCharWord(keyword, 0, 0, alpha_dict, len(words), 0)
    if wordIndex == -1:
        return "-"
    return words[wordIndex]

def findCharWord(keyword, keywordIndex, wordIndex, alpha_dict, wordsLength, matchcount):
    if keywordIndex == len(keyword):
        if matchcount == len(words[wordIndex]):
            return wordIndex
        else:
            return findCharWord(keyword, 0, wordIndex+1, alpha_dict, wordsLength, 0)
    if wordIndex == wordsLength:
        return -1
    if alpha_dict[keyword[keywordIndex]][wordIndex] != 0:
        alpha_dict[keyword[keywordIndex]][wordIndex] -= 1
        return findCharWord(keyword, keywordIndex+1, wordIndex, alpha_dict, wordsLength, matchcount+1)
    else:
        return findCharWord(keyword, keywordIndex+1, wordIndex, alpha_dict, wordsLength, matchcount)


if __name__ == "__main__":
    words = ["baby", "cat", "dada", "dog"]
    word1 = "akdnndohg"
    print(find(words, word1))
