class Capicua:
    def __init__(self):
        pass

    def checkword(self, word):
        word_is_capicua = False
        for x in range(0, len(word) / 2, 1):
            word_is_capicua = word[x] == word[len(word) - x - 1]
        return word_is_capicua
