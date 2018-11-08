class ReverseWord:
    def __init__(self):
        pass

    @staticmethod
    def reverse_alternate(string):
        words = string.split()
        for index in range(1, len(words), 2):
            if index % 1 == 0:
                words[index] = words[index][::-1]
        return " ".join(words)
