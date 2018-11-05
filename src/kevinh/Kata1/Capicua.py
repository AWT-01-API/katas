class Capicua:
    def __init__(self):
        pass

    def checkWord(self, word):
        iscapicua = False
        for x in range(0, len(word) / 2, 1):
            iscapicua = word[x] == word[len(word) - x - 1]
        return iscapicua