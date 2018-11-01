text1 = "oruro"
text2 = "test"


def isCapicua(word):
    iscapicua = False
    for x in range(0, len(word) / 2, 1):
        iscapicua = word[x] == word[len(word) - x - 1]
    return iscapicua


print text1 + " is a capicua word: " + str(isCapicua(text1))
print text2 + " is a capicua word: " + str(isCapicua(text2))
