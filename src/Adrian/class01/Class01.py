class Kata1:

    def __init__(self):
        pass

    def factorial(self, number):
        factint = 1
        for val in range(1, number):
            factint *= val
        return factint

    def palindrome(self, text):
        for char in range(0, len(text) / 2):
            if text[char] is not text[len(text) - char - 1]:
                return False
        return True
